"""QHSJ-AIGC route matching — single source of truth (see docs/adr/0002).

Pure Python standard library; never imports FastAPI. Implements docs/routing.md.

Deterministic multi-label routing: it reports which capabilities and workflows a
request maps to. It never claims a workflow has been executed and never invents
deliverables.

Single-source data:
- ``routes.json``            — workflow(route) table: triggers, priority, gate, capabilities.
- ``capabilities/*/SPEC.md`` — each capability's standard triggers (``## 典型触发``).
- ``capability-routes.json`` — capability machine metadata: semantic_triggers,
  auto/conditional workflow routes, dependencies, priority.

Contract highlights:
- Multi-task (叠加/并行): every matching workflow is scheduled, not a forced single pick.
- Negative scope: a trigger the user excludes ("不要分镜") is dropped with clause-local
  isolation so it cannot leak across sentences.
- Vague intent: a request that names a creative cue but no explicit deliverable falls back
  to ``intent-analysis`` + ``general_orchestration``; an unrelated request returns
  ``NO_ROUTE_MATCHED``.
"""
from __future__ import annotations

import difflib
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]  # backend/app/services -> repo root
ROUTES_PATH = ROOT / "routes.json"
CAPABILITY_META_PATH = ROOT / "capability-routes.json"
CAPABILITIES_DIR = ROOT / "capabilities"

FALLBACK_ROUTE = "intent-analysis"
FALLBACK_CAPABILITY = "general_orchestration"
MAX_CANDIDATES = 3

# A request that names a creative cue but no deliverable should still enter intent-analysis.
_VAGUE_MARKERS = tuple([
    "做", "搞", "弄", "搞个", "弄个", "来一个", "来一部", "来个", "设计", "创作", "生成",
    "内容", "方案", "优化", "专业", "调整", "改一改", "帮我", "帮我做", "分析", "理解",
    "看下", "看看", "弄得更", "更好", "提升", "完善",
])

_PUNCT = re.compile(r"[\s\u3000,，。.!！?？:：;；、·()（）\[\]【】{}<>《》\"'`|/\\_-]+")


@lru_cache(maxsize=30000)
def normalize(text: str) -> str:
    """NFKC-fold, lowercase and strip punctuation/whitespace for robust CJK matching."""
    text = unicodedata.normalize("NFKC", text).lower()
    return _PUNCT.sub("", text)


_NEGATORS = tuple(normalize(x) for x in [
    "不需要", "不要", "不做", "不生成", "不想", "不想要", "无需", "不用", "禁止", "别要", "避免", "拒绝", "不必",
    "别做", "别生成", "别弄", "别给", "免去", "勿", "不采用", "不涉及", "不加", "不配", "别加", "别配",
    "没有", "别看", "别管", "别用", "莫要", "切勿", "切忌", "去掉", "删除", "删掉", "移除", "去除", "略去", "删去", "取消",
])
# Removal verbs placed *immediately after* the phrase ("把运镜去掉") negate it; matched only
# when adjacent so that "生成图片，然后删除背景" keeps the image deliverable.
_REMOVAL_SUFFIX = tuple(normalize(x) for x in ["去掉", "删掉", "删除", "移除", "去除", "删了", "删去", "略去", "砍掉"])
_SCOPE_BREAKERS = tuple(normalize(x) for x in [
    "只要", "只需要", "只做", "只生成", "改为", "而是", "但是", "但", "转而", "同时", "并且", "另外", "不过",
    "只给我", "只输出", "仅给", "仅需", "给我", "想要", "请生成", "帮我生成",
])
# 顿号“、”故意不切分，使“不要音效、运镜、打斗”这类共享否定的列举仍被整体否定。
_CLAUSE_SPLIT = re.compile(r"[。！？；，,;!?:\n]+")


@lru_cache(maxsize=8192)
def _split_clauses(text: str) -> tuple[str, ...]:
    return tuple(part for part in _CLAUSE_SPLIT.split(text) if part.strip())


def _local_negation(nclause: str, idx: int, plen: int) -> bool:
    """True when the phrase occurrence at ``idx`` is negated inside its own clause."""
    prefix = nclause[max(0, idx - 30):idx]
    last_break = -1
    break_len = 0
    for breaker in _SCOPE_BREAKERS:
        j = prefix.rfind(breaker)
        if j > last_break:
            last_break = j
            break_len = len(breaker)
    if last_break >= 0:
        prefix = prefix[last_break + break_len:]
    if prefix and prefix[-1] in "不别勿没莫":
        return True
    for neg in _NEGATORS:
        j = prefix.rfind(neg)
        if j >= 0 and len(prefix) - (j + len(neg)) <= 9:
            return True
    suffix = nclause[idx + plen: idx + plen + 6]
    if suffix and any(suffix.startswith(rem) for rem in _REMOVAL_SUFFIX):
        return True
    return False


@lru_cache(maxsize=30000)
def phrase_is_negated(text: str, phrase: str) -> bool:
    """Clause-local negative scope: a phrase is negated only if *every* clause that
    mentions it negates it there; any positively-requested occurrence wins."""
    nphrase = normalize(phrase)
    if not nphrase:
        return False
    any_positive = False
    found = False
    for clause in _split_clauses(text):
        nclause = normalize(clause)
        start = 0
        while True:
            idx = nclause.find(nphrase, start)
            if idx < 0:
                break
            found = True
            start = idx + max(1, len(nphrase))
            if not _local_negation(nclause, idx, len(nphrase)):
                any_positive = True
    return found and not any_positive


# ---------------------------------------------------------------------------
# Data loading (single source of truth)
# ---------------------------------------------------------------------------

def _capability_id_from_spec(text: str) -> str | None:
    m = re.search(r"能力 ID[:：]\s*`([a-z0-9_]+)`", text)
    return m.group(1) if m else None


def _capability_name_from_spec(text: str) -> str | None:
    m = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    return m.group(1).strip() if m else None


_PRIORITY_LABELS = {"high": 10, "normal": 100, "low": 200}


def _parse_priority(value: Any, default: int = 100) -> int:
    """Accept both numeric and label priorities ("high"/"normal"/"low")."""
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        label = value.strip().lower()
        if label in _PRIORITY_LABELS:
            return _PRIORITY_LABELS[label]
        try:
            return int(label)
        except ValueError:
            return default
    return default


def _capability_triggers_from_spec(text: str) -> list[str]:
    m = re.search(r"^##\s*典型触发\s*\n(.+)$", text, re.M)
    if not m:
        return []
    raw = m.group(1).strip()
    return [p.strip() for p in re.split(r"[、，,/]", raw) if p.strip()]


@lru_cache(maxsize=1)
def load_capabilities() -> dict[str, dict[str, Any]]:
    """capability id -> {name, spec, triggers, semantic_triggers, auto, conditional, dependencies, priority}."""
    meta: dict[str, dict[str, Any]] = {}
    if CAPABILITY_META_PATH.is_file():
        raw = json.loads(CAPABILITY_META_PATH.read_text(encoding="utf-8"))
        meta = raw.get("capabilities", {})
    caps: dict[str, dict[str, Any]] = {}
    if not CAPABILITIES_DIR.is_dir():
        return caps
    for spec in sorted(CAPABILITIES_DIR.glob("*/SPEC.md")):
        text = spec.read_text(encoding="utf-8")
        cid = _capability_id_from_spec(text)
        if not cid:
            continue
        m = meta.get(cid, {})
        caps[cid] = {
            "id": cid,
            "name": m.get("name") or _capability_name_from_spec(text) or cid,
            "spec": f"capabilities/{spec.parent.name}/SPEC.md",
            "triggers": _capability_triggers_from_spec(text),
            "semantic_triggers": list(m.get("semantic_triggers", [])),
            "auto": list(m.get("auto", [])),
            "conditional": list(m.get("conditional", [])),
            "dependencies": list(m.get("dependencies", [])),
            "priority": _parse_priority(m.get("priority", 100)),
        }
    return caps


@lru_cache(maxsize=1)
def load_workflows() -> dict[str, dict[str, Any]]:
    """workflow id -> {id, name, file, priority, triggers, capabilities(ids), always_run}."""
    caps = load_capabilities()
    spec_to_id = {meta["spec"]: cid for cid, meta in caps.items()}
    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))
    wfs: dict[str, dict[str, Any]] = {}
    for r in routes:
        if r.get("deprecated"):
            continue
        cap_ids = [spec_to_id[p] for p in r.get("capabilities", []) if p in spec_to_id]
        wfs[r["id"]] = {
            "id": r["id"],
            "name": r.get("name", r["id"]),
            "file": r.get("workflow"),
            "priority": int(r.get("priority", 100)),
            "triggers": list(r.get("triggers", [])),
            "capabilities": cap_ids,
            "always_run": bool(r.get("always_run") or r.get("entrypoint")),
            "gate_level": r.get("gate_level", "P1"),
            "blocks_on_failure": bool(r.get("blocks_on_failure", False)),
        }
    return wfs


def _all_creative_cues() -> frozenset[str]:
    cues: set[str] = set()
    for meta in load_capabilities().values():
        for t in meta["triggers"] + meta["semantic_triggers"]:
            n = normalize(t)
            if n:
                cues.add(n)
    for wid, wf in load_workflows().items():
        if wid == FALLBACK_ROUTE:
            continue
        for t in wf["triggers"]:
            n = normalize(t)
            if n:
                cues.add(n)
    for m in _VAGUE_MARKERS:
        n = normalize(m)
        if n:
            cues.add(n)
    return frozenset(cues)


def _has_creative_cue(norm: str) -> bool:
    return any(cue in norm for cue in _all_creative_cues())


# ---------------------------------------------------------------------------
# Constraint + capability detection (deterministic dispatch layer)
# ---------------------------------------------------------------------------

def explicit_architecture_audit(text: str, normalized: str) -> bool:
    """Recognize explicit Skill/package routing-audit intent in formal and plain Chinese."""
    strong = [
        "路由缺失", "没有路由", "没路由", "路由完善", "路由注册", "模块注册", "注册表",
        "逻辑矛盾", "找漏洞", "查bug", "修复bug", "架构重构", "技能整改", "skill整改",
        "skill修复", "完整审计", "全量审计", "检查所有文件", "全自动skill", "整改完全体",
        "全套体系", "百分百全路由", "百分百路由", "全路由", "全量路由", "所有板块全部覆盖",
        "所有模块全部覆盖", "全部板块都要路由", "所有板块都要路由", "所有模块都要路由",
        "全部模块都要连通", "所有板块全部连通", "全部都要增上连通", "全面路由覆盖",
        "路由全部连通", "所有资源都接上路由", "全部文件接入路由", "全量资源路由",
        "路由覆盖率百分百", "全面分析理解用户的要求", "全面理解用户需求并自动路由",
        "自动识别所有需求并路由", "不要遗漏任何模块", "不能遗漏任何板块",
    ]
    has_skill_context = any(x in normalized for x in [
        "skill", "技能", "路由", "模块", "板块", "工作流", "文件包", "代码", "架构", "系统", "整套", "注册表", "资源图",
    ])
    has_audit_action = any(x in normalized for x in [
        "整改", "审计", "重构", "修复", "漏洞", "bug", "断链", "缺失", "覆盖率", "覆盖", "连通",
        "增上", "补齐", "接上", "全路由", "全量路由", "全面分析", "理解用户要求", "理解用户需求",
        "自动路由", "自动识别", "所有模块", "所有板块", "全部板块", "全部模块", "每个板块", "每个模块",
    ])
    broad_closure_request = (
        any(x in normalized for x in ["所有", "全部", "每个", "百分百", "全量", "全面", "全路由"])
        and any(x in normalized for x in ["板块", "模块", "文件", "资源", "路由", "工作流", "代码"])
        and any(x in normalized for x in ["覆盖", "连通", "路由", "接上", "补齐", "增上", "遗漏", "分析理解", "自动识别"])
    )
    return any(normalize(t) in normalized for t in strong) or (has_skill_context and has_audit_action) or broad_closure_request


def explicit_output_constraints(text: str, norm: str) -> dict[str, bool]:
    """Parse output exclusions with local scope and modality-specific semantics."""
    def has_any(phrases: list[str]) -> bool:
        return any(normalize(x) in norm for x in phrases)

    def negates_any(phrases: list[str]) -> bool:
        return any(normalize(x) in norm and phrase_is_negated(text, x) for x in phrases)

    image_terms = ["图片提示词", "图像提示词", "绘图提示词", "出图提示词", "静帧提示词", "生图提示词", "一张图片提示词", "一张图的提示词"]
    video_terms = ["视频提示词", "视频prompt", "视频生成提示词", "文生视频提示词", "图生视频提示词"]
    prompt_engineering_terms = ["提示词工程", "prompt工程", "提示词优化", "提示词设计"]
    generic_no_prompt = has_any([
        "不要任何提示词", "不需要任何提示词", "不要提示词", "不需要提示词", "不做提示词", "不生成提示词",
        "不需要生成提示词", "不要prompt", "不需要prompt", "不生成prompt", "不做prompt", "不需要任何prompt",
    ])
    broad_no_both = has_any([
        "不要图片或视频提示词", "不需要图片或视频提示词", "不要图片和视频提示词", "不需要图片和视频提示词",
        "不要图像或视频提示词", "不需要图像或视频提示词", "不生成图片或视频提示词", "不需要生成图片或视频提示词",
        "不要图片提示词和视频提示词", "不需要图片提示词和视频提示词",
    ])
    no_image_prompt = broad_no_both or negates_any(image_terms) or has_any([
        "不要图片提示词", "不需要图片提示词", "不生成图片提示词", "不做图片提示词", "不要图像提示词",
        "不需要图像提示词", "不需要生成图片提示词", "不要绘图提示词", "不需要绘图提示词", "不要出图提示词",
    ])
    no_video_prompt = broad_no_both or negates_any(video_terms) or has_any([
        "不要视频提示词", "不需要视频提示词", "不生成视频提示词", "不做视频提示词", "不需要生成视频提示词",
        "不要视频prompt", "不需要视频prompt", "只做音效不需要视频提示词", "只做音效不需要生成视频提示词",
        "只做声音不需要视频提示词", "只设计配音不需要视频提示词",
    ])
    no_prompt_engineering = negates_any(prompt_engineering_terms) or has_any([
        "不要提示词工程", "不需要提示词工程", "不做提示词工程", "不需要prompt工程",
    ])
    audio_only = has_any([
        "只做音效", "只设计音效", "只做声音", "只设计声音", "只设计配音", "只做配音", "只做音频",
        "仅音效", "仅声音设计", "只做配音和音效", "只做声音设计", "仅制作音频",
    ])
    image_asked = any(normalize(x) in norm and not phrase_is_negated(text, x) for x in image_terms + ["生成图片", "生成图像", "生图", "出图"])
    video_asked = any(normalize(x) in norm and not phrase_is_negated(text, x) for x in video_terms + ["文生视频", "图生视频", "生成视频", "视频生成方案"])
    audio_prompt_asked = any(normalize(x) in norm and not phrase_is_negated(text, x) for x in ["声音提示词", "音效提示词", "配音提示词", "声音prompt", "音频prompt"])
    if audio_only and not image_asked:
        no_image_prompt = True
    if audio_only and not video_asked:
        no_video_prompt = True
    no_prompt = generic_no_prompt or (no_image_prompt and no_video_prompt and not audio_prompt_asked)
    if no_prompt:
        no_image_prompt = True
        no_video_prompt = True
        no_prompt_engineering = True

    _storyboard_terms = ["分镜", "分镜表", "镜头表", "故事板", "storyboard"]
    storyboard_negated = negates_any(_storyboard_terms)
    storyboard_requested_positively = any(
        normalize(x) in norm and not phrase_is_negated(text, x) for x in _storyboard_terms
    )
    no_storyboard = storyboard_negated and not storyboard_requested_positively
    storyboard_requested = has_any(["只要分镜", "只做分镜", "只要分镜表", "分镜表", "镜头表", "逐镜分镜", "逐镜拆解"])
    no_full = has_any(["不需要完整项目", "不要全流程", "不要完整制作", "只要一个提示词", "只要一张图", "不要完整项目", "不做全流程"])
    writing_only = has_any(["只要小说", "只写小说", "不要视觉设计", "不做视觉设计", "只要剧本", "只写剧本"])
    prompt_only = has_any(["只要提示词", "只输出提示词", "只生成提示词", "不要解释", "不需要完整项目"])
    full_pipeline = has_any(["从创意到成片", "完整项目", "全流程制作", "全链路交付", "完整短片", "完整制作", "一整套全流程", "完整制作一条短片"])
    explicit_audit = explicit_architecture_audit(text, norm) and has_any([
        "全包审计", "运行审计", "全量审计", "路由审计", "回归测试", "检查所有文件",
        "检查所有模块", "全路由覆盖审计", "检查路由图", "路由覆盖率",
    ])
    explicit_no_creation = has_any([
        "不要实际生成", "不实际生成", "不要生成任何内容", "不要生成创作内容", "只检查路由",
        "只做路由审计", "只做审计", "只检查模块", "不用生成内容", "不生成内容",
    ])
    positive_creation = any(
        normalize(term) in norm and not phrase_is_negated(text, term)
        for term in [
            "写一篇小说", "写小说", "写一章", "写剧本", "编写剧本", "创作小说", "续写章节",
            "生成图片", "生成图像", "生成视频", "制作视频", "给我图片提示词", "给我视频提示词",
            "生成分镜表", "拆成分镜", "制作角色卡", "做角色四视图", "生成关键帧",
        ]
    )
    audit_only = explicit_architecture_audit(text, norm) and (explicit_no_creation or (explicit_audit and not positive_creation))
    return {
        "writing_only": writing_only,
        "storyboard_only": storyboard_requested and (has_any(["只要分镜", "只做分镜", "只要分镜表"]) or no_prompt),
        "prompt_only": prompt_only,
        "full_pipeline_explicit": full_pipeline,
        "explicit_no_prompt": no_prompt,
        "explicit_no_image_prompt": no_image_prompt,
        "explicit_no_video_prompt": no_video_prompt,
        "explicit_no_prompt_engineering": no_prompt_engineering,
        "audio_only": audio_only,
        "explicit_no_storyboard": no_storyboard,
        "explicit_no_full_project": no_full,
        "audit_only": audit_only,
        "explicit_no_creative_content": audit_only,
    }


def detect_capabilities(text: str, caps_by_id: dict[str, dict[str, Any]], constraints: dict[str, bool]) -> tuple[list[str], dict[str, int], dict[str, list[str]], set[str]]:
    """Return (all_selected_capabilities, scores, hit_evidence, directly_requested)."""
    norm = normalize(text)
    scores: dict[str, int] = {}
    hits: dict[str, list[str]] = {}
    direct: set[str] = set()

    for cid, cap in caps_by_id.items():
        matched: list[str] = []
        score = 0.0
        standard_triggers = list(cap.get("triggers", []))
        semantic_triggers = list(cap.get("semantic_triggers", []))
        generic_semantics = {normalize(x) for x in ["帮我做", "帮我处理", "帮我完成", "做一下", "写一下", "帮我", "处理一下", "优化一下", "分析一下"]}
        for trigger in list(dict.fromkeys(standard_triggers + semantic_triggers)):
            tnorm = normalize(trigger)
            if not tnorm or tnorm not in norm:
                continue
            if phrase_is_negated(text, trigger):
                continue
            if len(tnorm) <= 3 and any(
                len(normalize(other)) > len(tnorm) and tnorm in normalize(other) and normalize(other) in norm
                for other in standard_triggers + semantic_triggers if other != trigger
            ):
                continue
            matched.append(trigger)
            is_semantic = trigger in semantic_triggers and trigger not in standard_triggers
            if is_semantic:
                if tnorm in generic_semantics:
                    score += 0.5
                elif len(tnorm) >= 5:
                    score += 3
                elif len(tnorm) == 4:
                    score += 2
                elif len(tnorm) == 3:
                    score += 1
                else:
                    score += 0.5
            else:
                if len(tnorm) >= 5:
                    score += 3
                elif len(tnorm) == 4:
                    score += 2.5
                elif len(tnorm) == 3:
                    score += 1.5
                else:
                    score += 1
        scores[cid] = int(round(score))
        hits[cid] = matched
        strong_semantic_hit = any(
            normalize(x) in norm and len(normalize(x)) >= 5 and normalize(x) not in generic_semantics and not phrase_is_negated(text, x)
            for x in semantic_triggers
        )
        if score >= 3 or (len(set(matched)) >= 2 and score >= 2.5) or strong_semantic_hit:
            direct.add(cid)

    # Chinese plain-language semantic cue pass (many valid intent nouns are only two chars).
    def has(*phrases: str) -> bool:
        return any(normalize(x) in norm for x in phrases)

    def pos(*phrases: str) -> bool:
        return any(normalize(x) in norm and not phrase_is_negated(text, x) for x in phrases)

    if pos("小说", "长篇小说", "网文", "章节", "故事大纲", "小说大纲"):
        direct.add("novel_writing")
    if pos("剧本", "剧作", "分场", "对白", "台词", "编剧", "短剧") and not constraints["writing_only"]:
        direct.add("screenwriting")
    if pos("分镜", "逐镜", "镜头表", "镜头脚本", "故事板", "storyboard", "shot list",
           "分个镜", "分一下镜", "做分镜", "出分镜", "拆镜", "拆成分镜",
           "转成镜头", "转镜头", "改成镜头", "转成分镜", "镜头化") and not constraints["explicit_no_storyboard"]:
        direct.add("storyboard")
    if pos("视频提示词", "视频prompt", "文生视频", "图生视频", "视频生成提示词", "视频续写", "视频投喂",
           "做个片子", "做片子", "拍个片子", "做个视频", "做视频", "生成视频", "一段视频", "做条视频", "拍个视频",
           "做一个视频", "做个小视频", "小视频", "搞个片子", "片子", "来段视频", "整段视频", "做段视频", "生视频",
           "的片", "部片", "来部片", "微电影") and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_video_prompt", False):
        direct.add("video_prompt")
    if pos("图片提示词", "图像提示词", "图提示词", "静态图提示词", "绘图提示词", "出图提示词", "静帧提示词", "一张图片提示词", "一张图的提示词",
           "只要图片", "只要图", "出张图", "出一张图", "生图", "出图", "生成图片", "生成图像", "画一张", "画张图",
           "来张图", "来一张图", "来图", "大图", "插画", "插图", "画个图", "画一幅", "封面图", "海报") and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_image_prompt", False):
        direct.add("image_prompt")
    if (pos("提示词工程", "负面提示词", "正向提示词", "灯光方案", "视觉基因") or (has("提示词") and not phrase_is_negated(text, "提示词")) or (has("prompt") and not phrase_is_negated(text, "prompt"))) and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_prompt_engineering", False):
        direct.add("prompt_engineering")
    if pos("运镜", "推镜", "拉镜", "低机位", "焦段", "景别", "摄影机", "摄影方案", "镜头节奏", "构图", "灯光方案",
           "机位", "镜头语言", "运镜方案", "分镜语言"):
        direct.add("cinematography")
    if pos("视频提示词", "文生视频", "图生视频") and pos("时间码", "动作", "表情", "运镜", "镜头") and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_video_prompt", False):
        direct.add("storyboard")
    if pos("站位", "轴线", "越轴", "人物位置", "位置不一致", "空间关系", "场面调度", "镜头接不上", "走位", "连续性"):
        direct.add("spatial_continuity")
    if pos("检查", "审查", "质检", "找bug", "查bug", "找漏洞", "修复", "排查", "逻辑矛盾", "一致性检查", "是否自洽", "避免漂浮", "避免穿模",
           "不一致", "对不上", "怎么修", "怎么改", "修一下", "修正"):
        direct.add("quality_assurance")
    if pos("角色四视图", "角色卡", "角色设定", "人物设定", "角色脸型", "发色", "服装和配饰", "角色定妆", "人物外观", "角色一致性", "人物服装", "角色服装", "服饰造型", "人物造型",
           "角色图", "人物图", "人设图", "角色立绘", "人物立绘", "角色资产图", "人物资产图", "角色造型图", "角色三视图", "人物三视图",
           "立绘", "三视图", "角色设定图", "人物设定图") or (pos("角色") and pos("恐惧", "愤怒", "微表情", "表演", "眼神", "呼吸")):
        direct.add("character_design")
    if pos("角色", "人物", "主角", "男主角", "女主角", "主人公") and pos(
           "长得一样", "保持一致", "前后一致", "跨镜一致", "跨镜头一致", "跨集一致", "每集一样",
           "形象一致", "外观一致", "模样一样", "形象统一", "不能变", "别变", "不要变", "保持不变"):
        direct.update({"character_design", "asset_locking"})
    if pos("微表情", "演技", "怎么演", "情绪转折", "情绪曲线", "表演层次", "情绪外化", "身体表演", "表演调度"):
        direct.add("performance_emotion")
    if pos("资产包", "资产板", "资产前置", "先做资产", "先做角色", "四视图资产", "场景和道具",
           "设定图", "先出设定图", "资产设定", "先定稿"):
        direct.add("asset_first")
    if pos("资产锁定", "锁定资产", "角色资产锁定", "人物资产锁定", "场景资产锁定", "资产冻结", "锁定人物和场景", "先锁定角色和场景", "分镜资产引用", "资产版本锁定", "资产漂移修复",
           "锁定角色", "锁定人物", "锁定场景", "锁住角色", "锁住人物", "把角色锁", "把人物锁", "角色锁住") or (pos("人物资产", "角色资产", "场景资产") and pos("先锁定", "锁定后", "版本锁定", "引用资产", "分镜资产")) or (pos("锁住", "锁定", "定型", "锁死", "定死") and pos("别变", "不要变", "不能变", "保持一致", "不变", "统一", "别再变")) or (pos("定型", "锁死", "定死", "固定住") and pos("角色", "人物", "脸", "形象", "外观", "资产", "场景", "设定", "造型", "模样")):
        direct.add("asset_locking")
    if pos("古风", "国风", "赛博朋克", "冷艳", "导演风格", "视觉基因", "色彩体系", "配色", "美术指导", "灯光方案",
           "整体风格", "什么风格", "风格走", "美学", "美术风格", "视觉风格", "画面风格", "色调"):
        direct.add("aesthetics_style")
    if pos("音效", "声音设计", "环境音", "拟音", "配音", "配乐", "旁白", "声音分层"):
        direct.add("audio_design")
    if pos("api", "接口", "json请求", "请求参数", "端点", "webhook"):
        direct.add("api_integration")
    if pos("外部skill", "claude code", "codex", "dify", "coze", "智能体集成", "agent集成", "安装skill"):
        direct.add("external_skill_integration")
    if pos("参考图", "参考视频", "反推", "反向工程", "拍摄方案") and (pos("参考", "反推") or "reverse" in norm):
        direct.add("reverse_engineering")
    if pos("参考图", "参考视频", "参考素材") and pos("保持一致", "完全一致", "一比一还原", "按图还原", "照着", "参考图一致", "还原人物", "复刻构图", "保持角色一致"):
        direct.add("reverse_engineering")
    if pos("照着这张", "照着这", "按这张图", "按这图", "按图", "同款", "仿一个", "仿一张", "仿造", "复刻") and pos("图", "照片", "画面", "素材", "视频", "片"):
        direct.add("reverse_engineering")
    if pos("武打", "打斗", "动作戏", "打戏", "武戏", "攻防", "战斗动作", "受力反馈", "动作预演", "动作设计", "动作编排"):
        direct.add("action_choreography")
    if pos("粒子", "爆炸特效", "特效", "物理模拟", "穿模", "重力", "惯性"):
        direct.add("vfx_physics")
    if pos("项目状态", "状态文件", "跨轮次", "设定锁", "人物关系", "已埋伏笔", "世界观连续性", "项目记忆"):
        direct.add("project_state_management")
    if pos("seedance", "可灵", "veo", "runway", "sora", "模型语法", "模型适配"):
        direct.add("model_adaptation")
    if pos("版权", "原创性", "平台合规", "侵权", "内容审核"):
        direct.add("safety_originality")
    short_video_content_intent = (
        pos("短视频文案", "口播", "抖音脚本", "小红书视频文案", "视频号脚本", "tiktok脚本", "竖屏短剧", "短视频脚本", "短视频平台方案", "开头三秒", "黄金三秒", "完播率", "转粉", "转化率", "短视频选题")
        or (pos("短视频") and pos("文案", "脚本", "选题", "开头三秒", "黄金三秒", "完播率", "转粉", "转化率", "口播"))
        or (pos("抖音", "小红书", "视频号", "tiktok") and pos("脚本", "文案", "口播", "开头三秒", "短视频发布"))
        or pos("做个短视频", "做条短视频", "做一条短视频", "拍个短视频", "拍条短视频", "做个短剧", "做条短剧", "生成短视频", "制作短视频")
        or pos("短剧", "ai短剧", "竖屏短剧")
    )
    if short_video_content_intent:
        direct.add("short_video_content")
    if pos("平台适配", "发布策略", "字幕安全区", "比例适配", "视频内容适配", "竖屏", "横屏", "竖版", "横版", "画幅", "尺寸适配") or (
        pos("抖音", "小红书", "视频号", "tiktok", "b站", "快手", "油管", "youtube") and pos("发布", "怎么发", "上传", "运营", "投放", "适配", "涨粉", "引流")
    ):
        direct.add("platform_adaptation")
    if pos("从创意到成片", "完整制作", "全流程制作", "全链路交付", "一整套全流程"):
        direct.add("full_production")
    if pos("角色卡", "四视图", "角色定妆", "角色外观", "角色脸型") and pos("一致", "资产", "设定", "人物"):
        direct.add("asset_first")
    if pos("输出格式", "json输出", "双区输出", "导出json", "转成json", "转json", "json格式", "输出成json", "导出excel", "导出表格", "表格输出", "markdown输出",
           "输出json", "json导出", "json文件", "输出表格", "导出csv", "csv输出"):
        direct.add("output_formatting")

    # Natural wording such as “先设计人物和场景图，再做分镜” is an ordered asset pipeline,
    # even without the technical word “资产”. Local negation suppresses only the excluded asset.
    character_visual_terms = (
        "角色图", "人物图", "人设图", "角色设定图", "人物设定图", "角色四视图", "人物四视图",
        "角色三视图", "人物三视图", "角色定妆照", "人物定妆照", "角色资产图", "人物资产图",
        "角色立绘", "人物立绘", "角色卡", "角色造型图", "人物造型图",
    )
    scene_visual_terms = (
        "场景图", "环境图", "场景设定图", "环境设定图", "场景资产图", "场景概念图",
        "环境概念图", "场景布局图", "背景设定图", "场景原画", "场景美术图",
    )
    paired_asset_phrases = (
        "人物和场景图", "角色和场景图", "人物与场景图", "角色与场景图", "人物场景设定图",
        "角色场景设定图", "人物和场景设定图", "角色和场景设定图", "人物图和场景图",
        "角色图和场景图", "人设图和场景图", "人物设定图和场景设定图", "角色设定图和场景设定图",
        "人物和环境图", "角色和环境图", "人物场景资产", "角色场景资产",
    )
    positive_character_visual = any(has(term) and not phrase_is_negated(text, term) for term in character_visual_terms)
    positive_scene_visual = any(has(term) and not phrase_is_negated(text, term) for term in scene_visual_terms)
    positive_paired_assets = any(has(term) and not phrase_is_negated(text, term) for term in paired_asset_phrases)
    creation_action = has("设计", "生成", "制作", "绘制", "出图", "做出", "先做", "先出", "创建", "构建", "定稿")
    if positive_paired_assets or (positive_character_visual and positive_scene_visual and creation_action):
        direct.update({"asset_first", "character_design"})
        if has("分镜", "故事板", "逐镜", "关键帧", "镜头图") and not constraints["explicit_no_storyboard"]:
            direct.update({"asset_locking", "storyboard", "spatial_continuity"})
        elif has("锁定", "定稿", "保持一致", "不要变化", "不能变", "跨镜头"):
            direct.add("asset_locking")
    if has("人物和场景资产", "人物资产和场景资产", "角色和场景资产", "角色资产和场景资产", "人物资产图", "场景资产图", "角色资产图") and has("分镜图", "分镜资产", "镜头图", "逐镜图"):
        direct.update({"asset_first", "asset_locking", "character_design", "storyboard", "spatial_continuity"})

    # Explicit task families take precedence when the target deliverable is clear.
    if explicit_architecture_audit(text, norm):
        direct.add("skill_architecture_audit")
    if constraints["full_pipeline_explicit"]:
        direct.add("full_production")
    if constraints["writing_only"]:
        direct.add("novel_writing" if any(x in norm for x in ["小说", "章节", "世界观", "续写"]) else "screenwriting")
    if constraints["storyboard_only"]:
        direct.add("storyboard")
    if constraints["prompt_only"] and not constraints["explicit_no_prompt"]:
        direct.add("prompt_engineering")

    # Hard negative constraints remove deliverable routes before and during dependency expansion.
    forbidden: set[str] = set()
    if constraints["explicit_no_prompt"]:
        forbidden.update({"image_prompt", "video_prompt", "prompt_engineering"})
    else:
        if constraints.get("explicit_no_image_prompt", False):
            forbidden.add("image_prompt")
        if constraints.get("explicit_no_video_prompt", False):
            forbidden.add("video_prompt")
        if constraints.get("explicit_no_prompt_engineering", False):
            forbidden.add("prompt_engineering")
    direct.difference_update(forbidden)
    if constraints["explicit_no_storyboard"]:
        forbidden.add("storyboard")
        direct.discard("storyboard")
    if constraints["explicit_no_full_project"] and not constraints["full_pipeline_explicit"]:
        forbidden.add("full_production")
        direct.discard("full_production")
    if constraints.get("explicit_no_creative_content"):
        creative_deliverables = {
            "novel_writing", "screenwriting", "short_video_content", "storyboard", "cinematography",
            "character_design", "image_prompt", "video_prompt", "prompt_engineering", "model_adaptation",
            "reverse_engineering", "asset_first", "action_choreography", "vfx_physics", "audio_design",
            "aesthetics_style", "platform_adaptation", "full_production",
        }
        forbidden.update(creative_deliverables)
        direct.difference_update(creative_deliverables)

    # A request with no directly-requested capability still routes when it carries a creative
    # cue; otherwise it is genuinely unrelated and returns NO_ROUTE_MATCHED.
    if not direct:
        if _has_creative_cue(norm):
            direct.add(FALLBACK_CAPABILITY)
        elif not any(normalize(m) in norm for m in _VAGUE_MARKERS):
            return [], scores, hits, set()

    selected = set(direct)
    pending = list(selected)
    while pending:
        cid = pending.pop()
        for dep in caps_by_id.get(cid, {}).get("dependencies", []):
            if dep in forbidden or dep in selected:
                continue
            selected.add(dep)
            pending.append(dep)
    selected.difference_update(forbidden)

    production_like = selected.intersection({"novel_writing", "screenwriting", "storyboard", "character_design", "image_prompt", "video_prompt", "prompt_engineering", "reverse_engineering", "action_choreography", "audio_design", "full_production", "asset_first"})
    if production_like:
        selected.update({"quality_assurance", "safety_originality"})
    return sorted(selected), scores, hits, direct


def select_workflows(caps_by_id: dict[str, dict[str, Any]], wfs_by_id: dict[str, dict[str, Any]], constraints: dict[str, bool], direct_capabilities: set[str]) -> list[dict[str, Any]]:
    """Return every compatible workflow route, ordered; no presentation limit is applied."""
    found: dict[str, dict[str, Any]] = {}
    reasons: dict[str, list[str]] = {}
    explicit_hits: set[str] = set()

    def is_blocked(wid: str) -> bool:
        if wid == "full-production" and constraints.get("explicit_no_full_project") and not constraints.get("full_pipeline_explicit"):
            return True
        if wid == "visual-prompt" and (constraints.get("explicit_no_prompt") or (constraints.get("explicit_no_image_prompt") and constraints.get("explicit_no_video_prompt"))):
            return True
        if wid == "visual-prompt" and constraints.get("explicit_no_video_prompt") and not constraints.get("explicit_no_image_prompt") and "image_prompt" not in direct_capabilities:
            return True
        if wid == "storyboard-only" and constraints.get("explicit_no_storyboard"):
            return True
        if wid == "storyboard-only" and not constraints.get("storyboard_only"):
            compound_deliverables = {"screenwriting", "video_prompt", "image_prompt", "full_production", "action_choreography", "asset_locking", "asset_first"}
            if compound_deliverables.intersection(direct_capabilities):
                return True
            if any(x in found for x in ("asset-lock", "asset-first", "script-to-screen", "full-production")):
                return True
        if wid == "writing" and not any(c in direct_capabilities for c in ("novel_writing", "screenwriting")):
            return True
        return False

    def add(wid: str, reason: str):
        wf = wfs_by_id.get(wid)
        if not wf or is_blocked(wid):
            return
        found[wid] = wf
        reasons.setdefault(wid, [])
        if reason not in reasons[wid]:
            reasons[wid].append(reason)

    # The intent-analysis front door runs on every request.
    for wid, wf in wfs_by_id.items():
        if wf.get("always_run"):
            add(wid, "强制入口：所有请求先执行意图解析")

    # Explicit macro-workflow triggers.
    norm = normalize(_LAST_TEXT)
    for wid, wf in wfs_by_id.items():
        matched = [tr for tr in wf.get("triggers", []) if normalize(tr) and normalize(tr) in norm and not phrase_is_negated(_LAST_TEXT, tr)]
        if not matched:
            continue
        for tr in matched:
            add(wid, f"显式工作流触发：{tr}")
            explicit_hits.add(wid)

    # Macro workflows auto-dispatch only from directly requested capabilities.
    for cid in direct_capabilities:
        for wid in caps_by_id.get(cid, {}).get("auto", []):
            add(wid, f"直接能力自动路由：{cid}")

    direct = set(direct_capabilities)
    combo_rules = [
        ({"screenwriting", "storyboard"}, "script-to-screen", "剧本+分镜复合任务"),
        ({"screenwriting", "video_prompt"}, "script-to-screen", "剧本+视频提示词复合任务"),
        ({"character_design", "image_prompt"}, "asset-first", "角色资产+图像输出复合任务"),
        ({"image_prompt", "reverse_engineering"}, "reverse-engineering", "图片生成+参考反推复合任务"),
        ({"video_prompt", "storyboard"}, "script-to-screen", "分镜+视频提示词复合任务"),
        ({"action_choreography", "storyboard"}, "action-design", "动作+分镜复合任务"),
        ({"audio_design", "short_video_content"}, "platform-short-video", "短视频+声音复合任务"),
        ({"model_adaptation", "image_prompt"}, "visual-prompt", "图像提示词+模型适配复合任务"),
        ({"model_adaptation", "video_prompt"}, "visual-prompt", "视频提示词+模型适配复合任务"),
        ({"quality_assurance", "spatial_continuity"}, "continuity-repair", "连续性+质检复合任务"),
        ({"api_integration", "external_skill_integration"}, "api-integration", "API+Skill/Agent集成复合任务"),
        ({"short_video_content", "platform_adaptation"}, "platform-short-video", "短视频+平台适配复合任务"),
        ({"full_production"}, "full-production", "全流程生产复合任务"),
    ]
    for required, wid, reason in combo_rules:
        if required.issubset(direct):
            add(wid, reason)

    # Conditional capability routes activate only on a matched macro trigger, an explicitly
    # selected capability bundle, or an explicit full-pipeline request.
    explicit_workflow_ids = set(found)
    for cid in direct:
        for wid in caps_by_id.get(cid, {}).get("conditional", []):
            if wid in explicit_workflow_ids:
                add(wid, f"条件路由确认：{cid} 与工作流触发兼容")
            elif constraints.get("full_pipeline_explicit") and wid == "full-production":
                add(wid, f"全流程硬约束：{cid}")

    if constraints.get("full_pipeline_explicit"):
        add("full-production", "用户明确要求完整制作全流程")

    wf_items = list(found.items())
    # Front door (intent-analysis) first; then workflows with an explicit trigger match
    # outrank ones merely auto-routed from a capability; then priority, then id.
    wf_items.sort(key=lambda kv: (
        kv[0] != FALLBACK_ROUTE,
        kv[0] not in explicit_hits,
        -int(kv[1].get("priority", 0)),
        kv[0],
    ))
    return [{
        "id": wid,
        "name": wf.get("name", wid),
        "file": wf.get("file"),
        "gate_level": wf.get("gate_level", "P1"),
        "blocks_on_failure": bool(wf.get("blocks_on_failure", False)),
        "matched_triggers": reasons.get(wid, []),
        "priority": wf.get("priority", 0),
        "always_run": bool(wf.get("always_run")),
    } for wid, wf in wf_items]


# ``select_workflows`` needs the raw request for trigger/negation checks; the public
# entry point is single-threaded and deterministic, so it is passed via this holder.
_LAST_TEXT = ""


def match_route(query: str, routes: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Match a Chinese-language request against the routing table.

    Returns a backward-compatible dict (matched/route_id/gate_level/...) extended
    with multi-task fields: ``routes``, ``workflows``, ``capabilities``.
    """
    global _LAST_TEXT
    _LAST_TEXT = query
    caps_by_id = load_capabilities()
    wfs_by_id = load_workflows()

    constraints = explicit_output_constraints(query, normalize(query))
    selected, scores, hits, direct = detect_capabilities(query, caps_by_id, constraints)

    if not selected and not direct:
        return _no_match(query, wfs_by_id)

    workflows = select_workflows(caps_by_id, wfs_by_id, constraints, direct)
    if not workflows:
        return _no_match(query, wfs_by_id)

    wf_ids = [w["id"] for w in workflows]
    ordered_caps = sorted(selected, key=lambda c: (-scores.get(c, 0), c))
    primary = next((w for w in workflows if w["id"] != FALLBACK_ROUTE), workflows[0])
    strictest = _strictest_gate(workflows)
    is_fallback = {"matched"} if False else False
    fallback = direct == {FALLBACK_CAPABILITY}
    gate_rank = {"P0": 2, "P1": 1, "P2": 0}

    return {
        "matched": True,
        "route_id": primary["id"],
        "gate_level": primary["gate_level"],
        "blocks_on_failure": primary["blocks_on_failure"],
        "matched_triggers": [t for cid in ordered_caps for t in hits.get(cid, [])][:32],
        "score": sum(scores.get(c, 0) for c in selected),
        # Multi-task orchestration (叠加/并行): every matched workflow is scheduled.
        "multi_task": len(workflows) > 1,
        "routes": [{
            "id": w["id"], "gate_level": w["gate_level"], "blocks_on_failure": w["blocks_on_failure"],
            "priority": w["priority"], "matched_triggers": w["matched_triggers"],
        } for w in workflows],
        "workflows": wf_ids,
        "primary_workflow": primary["id"] if not fallback else None,
        "capabilities": ordered_caps,
        "direct_capabilities": sorted(direct),
        "constraints": constraints,
        "intent_analysis_required": True,
        "strictest_gate_level": strictest,
        "blocks_on_failure_any": any(w["blocks_on_failure"] for w in workflows),
        "fallback": fallback,
        "fallback_reason": "未命中显式交付物，转入意图解析" if fallback else None,
        "error_code": "INTENT_ANALYSIS_FALLBACK" if fallback else None,
    }


def _strictest_gate(workflows: list[dict[str, Any]]) -> str:
    gate_rank = {"P0": 2, "P1": 1, "P2": 0}
    worst = "P2"
    for w in workflows:
        if gate_rank.get(w.get("gate_level", "P1"), 1) > gate_rank.get(worst, 0):
            worst = w.get("gate_level", "P1")
    return worst


def _no_match(query: str, wfs_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        "matched": False,
        "route_id": None,
        "gate_level": None,
        "blocks_on_failure": False,
        "matched_triggers": [],
        "score": 0,
        "error_code": "NO_ROUTE_MATCHED",
        "candidates": _similar_candidates(query, wfs_by_id),
    }


def _similar_candidates(query: str, wfs_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    nq = normalize(query)
    candidates = []
    for wid, wf in wfs_by_id.items():
        if wid == FALLBACK_ROUTE:
            continue
        all_text = normalize(" ".join(wf.get("triggers", [])) + " " + wid)
        sim = difflib.SequenceMatcher(None, nq, all_text).ratio()
        candidates.append((sim, wf))
    candidates.sort(key=lambda x: (-x[0], x[1]["id"]))
    return [
        {"id": c[1]["id"], "gate_level": c[1].get("gate_level", "P1"), "score": round(c[0], 3)}
        for c in candidates[:MAX_CANDIDATES]
    ]
