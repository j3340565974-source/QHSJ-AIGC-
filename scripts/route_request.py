#!/usr/bin/env python3
"""QHSJ AIGC 全能影视 deterministic natural-language route preview.

This script recommends capabilities, workflows, references and section headings.
It does not invoke remote models or claim that a workflow has been executed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "routing" / "route-registry.json"


@lru_cache(maxsize=30000)
def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return re.sub(
        r"[\s\u3000,，。.!！?？:：;；、·()（）\[\]【】{}<>《》\"'`|/\\_-]+", "", text
    )


def phrase_is_negated(text: str, phrase: str) -> bool:
    """Detect local negative scope for a phrase without letting one clause erase another.

    This is a deterministic guard, not a full Chinese syntactic parser. The host intent workflow
    remains authoritative for ambiguous scope; this helper prevents common modality false positives.
    """
    ntext = normalize(text)
    nphrase = normalize(phrase)
    if not nphrase:
        return False
    negators = [normalize(x) for x in ["不需要", "不要", "不做", "不生成", "不想", "无需", "不用", "禁止", "别要", "避免", "拒绝", "不必"]]
    scope_breakers = [normalize(x) for x in ["只要", "只需要", "只做", "只生成", "改为", "而是", "但是", "但", "转而", "同时", "并且", "另外", "不过", "只给我", "只输出", "仅给", "仅需", "给我", "想要", "请生成", "帮我生成"]]
    start = 0
    while True:
        idx = ntext.find(nphrase, start)
        if idx < 0:
            return False
        prefix = ntext[max(0, idx - 30):idx]
        last_break = -1
        break_len = 0
        for breaker in scope_breakers:
            j = prefix.rfind(breaker)
            if j > last_break:
                last_break = j
                break_len = len(breaker)
        if last_break >= 0:
            prefix = prefix[last_break + break_len:]
        for neg in negators:
            j = prefix.rfind(neg)
            if j >= 0 and len(prefix) - (j + len(neg)) <= 9:
                return True
        start = idx + max(1, len(nphrase))


@lru_cache(maxsize=1)
def load_registry() -> dict[str, Any]:
    if not REGISTRY_PATH.is_file():
        raise FileNotFoundError(f"路由注册表不存在：{REGISTRY_PATH}")
    with REGISTRY_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    for key in ("capabilities", "workflows", "resources"):
        if not isinstance(data.get(key), list):
            raise ValueError(f"注册表字段 {key!r} 必须是数组")
    # Precompute normalized match keys once per process. This keeps 15k+ heading indexes searchable
    # without normalizing every heading again for every user request.
    for resource in data["resources"]:
        rel = resource.get("file", "")
        resource["_runtime_path_norm"] = normalize(rel)
        resource["_runtime_name_norm"] = normalize(Path(rel).name)
        resource["_runtime_stem_norm"] = normalize(Path(rel).stem)
        resource["_runtime_trigger_pairs"] = [(t, normalize(t)) for t in resource.get("triggers", [])]
        resource["_runtime_heading_pairs"] = [(h, normalize(h.get("heading", ""))) for h in resource.get("headings", [])]
    for cap in data["capabilities"]:
        cap["_runtime_trigger_pairs"] = [(t, normalize(t)) for t in cap.get("triggers", [])]
        cap["_runtime_semantic_pairs"] = [(t, normalize(t)) for t in cap.get("semantic_triggers", [])]
    for wf in data["workflows"]:
        wf["_runtime_trigger_pairs"] = [(t, normalize(t)) for t in wf.get("triggers", [])]
    return data



@lru_cache(maxsize=1)
def load_route_graph() -> dict[str, Any]:
    graph_path = ROOT / "routing" / "route-graph.json"
    if not graph_path.is_file():
        return {"nodes": [], "edges": [], "coverage": {}}
    try:
        with graph_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {"nodes": [], "edges": [], "coverage": {}}


def graph_coverage_status(registry: dict[str, Any]) -> dict[str, Any]:
    """Check the live graph's registered capability/workflow/resource/section closure."""
    graph = load_route_graph()
    node_ids = {n.get("id") for n in graph.get("nodes", []) if isinstance(n, dict)}
    edges = {(e.get("from"), e.get("relation"), e.get("to")) for e in graph.get("edges", []) if isinstance(e, dict)}
    caps = registry.get("capabilities", [])
    workflows = registry.get("workflows", [])
    resources = registry.get("resources", [])
    missing_caps = ["capability:" + c.get("id", "") for c in caps if "capability:" + c.get("id", "") not in node_ids]
    missing_workflows = ["workflow:" + w.get("id", "") for w in workflows if "workflow:" + w.get("id", "") not in node_ids]
    missing_resources = ["resource:" + r.get("file", "") for r in resources if "resource:" + r.get("file", "") not in node_ids]
    missing_cap_resource_edges = []
    for resource in resources:
        rid = "resource:" + resource.get("file", "")
        for tag in resource.get("tags", []):
            edge = ("capability:" + tag, "routes_to_resource", rid)
            if edge not in edges:
                missing_cap_resource_edges.append(edge)
    missing_auto_edges = []
    for cap in caps:
        for wid in cap.get("workflow_routes", {}).get("auto", []):
            edge = ("capability:" + cap.get("id", ""), "routes_auto_to", "workflow:" + wid)
            if edge not in edges:
                missing_auto_edges.append(edge)
    missing_sections = []
    missing_section_edges = []
    expected_sections = 0
    for resource in resources:
        rel = resource.get("file", "")
        rid = "resource:" + rel
        for heading in resource.get("headings", []):
            expected_sections += 1
            sid = f"section:{rel}#{heading.get('anchor', '')}"
            if sid not in node_ids:
                missing_sections.append(sid)
            if (rid, "contains_section", sid) not in edges:
                missing_section_edges.append((rid, "contains_section", sid))
    incoming_workflow = {edge[2] for edge in edges if edge[1] in {"routes_auto_to", "routes_conditional_to", "precedes_all_workflows"}}
    known_wids = {w.get("id") for w in workflows}
    unreachable_workflows = ["workflow:" + wid for wid in known_wids if "workflow:" + wid not in incoming_workflow]
    problems = missing_caps + missing_workflows + missing_resources + missing_cap_resource_edges + missing_auto_edges + missing_sections + missing_section_edges + unreachable_workflows
    return {
        "ok": not problems,
        "capability_nodes": len(caps) - len(missing_caps),
        "workflow_nodes": len(workflows) - len(missing_workflows),
        "resource_nodes": len(resources) - len(missing_resources),
        "section_nodes": expected_sections - len(missing_sections),
        "expected_section_nodes": expected_sections,
        "capability_resource_edges": sum(1 for e in edges if e[1] == "routes_to_resource"),
        "auto_workflow_edges": sum(1 for e in edges if e[1] == "routes_auto_to"),
        "missing_capability_nodes": missing_caps[:20],
        "missing_workflow_nodes": missing_workflows[:20],
        "missing_resource_nodes": missing_resources[:20],
        "missing_capability_resource_edges": missing_cap_resource_edges[:20],
        "missing_auto_workflow_edges": missing_auto_edges[:20],
        "missing_section_nodes": missing_sections[:20],
        "missing_section_edges": missing_section_edges[:20],
        "unreachable_workflow_nodes": unreachable_workflows[:20],
    }

def explicit_architecture_audit(text: str, normalized: str) -> bool:
    """Recognize explicit Skill/package routing-audit intent in formal and plain Chinese.

    This is a deterministic dispatch guard. The intent-analysis workflow still performs
    contextual interpretation; the goal here is to keep colloquial 'all boards connected'
    requests from falling through to the generic orchestrator only.
    """
    strong = [
        "路由缺失", "没有路由", "没路由", "路由完善", "路由注册", "模块注册", "注册表",
        "逻辑矛盾", "找漏洞", "查bug", "修复bug", "架构重构", "技能整改", "skill整改",
        "skill修复", "完整审计", "全量审计", "检查所有文件", "全自动skill", "整改完全体",
        "全套体系", "百分百全路由", "百分百路由", "全路由", "全量路由", "所有板块全部覆盖",
        "所有模块全部覆盖", "全部板块都要路由", "所有板块都要路由", "所有模块都要路由",
        "全部模块都要连通", "所有板块全部连通", "全部都要增上连通", "全面路由覆盖",
        "路由全部连通", "所有资源都接上路由", "全部文件接入路由", "全量资源路由",
        "路由覆盖率百分百", "全面分析理解用户的要求", "全面理解用户需求并自动路由",
        "自动识别所有需求并路由", "不要遗漏任何模块", "不能遗漏任何板块"
    ]
    has_skill_context = any(x in normalized for x in [
        "skill", "技能", "路由", "模块", "板块", "工作流", "文件包", "代码", "架构", "系统", "整套", "注册表", "资源图"
    ])
    has_audit_action = any(x in normalized for x in [
        "整改", "审计", "重构", "修复", "漏洞", "bug", "断链", "缺失", "覆盖率", "覆盖", "连通",
        "增上", "补齐", "接上", "全路由", "全量路由", "全面分析", "理解用户要求", "理解用户需求",
        "自动路由", "自动识别", "所有模块", "所有板块", "全部板块", "全部模块", "每个板块", "每个模块"
    ])
    # Colloquial closure requests need not contain the literal word "Skill".
    broad_closure_request = (
        any(x in normalized for x in ["所有", "全部", "每个", "百分百", "全量", "全面", "全路由"])
        and any(x in normalized for x in ["板块", "模块", "文件", "资源", "路由", "工作流", "代码"])
        and any(x in normalized for x in ["覆盖", "连通", "路由", "接上", "补齐", "增上", "遗漏", "分析理解", "自动识别"])
    )
    return any(normalize(t) in normalized for t in strong) or (has_skill_context and has_audit_action) or broad_closure_request


def explicit_output_constraints(text: str, norm: str) -> dict[str, bool]:
    """Parse output exclusions with local scope and modality-specific semantics.

    Exact deny phrases catch common white-language forms; phrase_is_negated catches natural
    variants such as “不需要分镜或视频提示词”. These are rules for deterministic dispatch,
    while intent-analysis remains responsible for genuinely ambiguous expressions.
    """
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
    # Audio-only wording implies no visual deliverables only when the user did not request them positively.
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

    no_storyboard = has_any([
        "不要分镜", "不需要分镜", "不做分镜", "不生成分镜", "不需要分镜表", "不要镜头表", "不需要镜头表",
        "不要故事板", "不需要故事板",
    ]) or negates_any(["分镜", "分镜表", "镜头表", "故事板", "storyboard"])
    storyboard_requested = has_any(["只要分镜", "只做分镜", "只要分镜表", "分镜表", "镜头表", "逐镜分镜", "逐镜拆解"])
    no_full = has_any(["不需要完整项目", "不要全流程", "不要完整制作", "只要一个提示词", "只要一张图", "不要完整项目", "不做全流程"])
    writing_only = has_any(["只要小说", "只写小说", "不要视觉设计", "不做视觉设计", "只要剧本", "只写剧本"])
    prompt_only = has_any(["只要提示词", "只输出提示词", "只生成提示词", "不要解释", "不需要完整项目"])
    full_pipeline = has_any(["从创意到成片", "完整项目", "全流程制作", "全链路交付", "完整短片", "完整制作", "一整套全流程", "完整制作一条短片"])
    # A package audit can mention creative modules merely as inventory targets. When the user
    # explicitly asks not to generate deliverables, inspect the route architecture without
    # activating those creative output pipelines.
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
    # A package-wide architecture audit is audit-only by default when its deliverables are
    # reports/patches/tests, not creative media. Explicit positive creation tasks retain their routes.
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


def detect_capabilities(text: str, registry: dict[str, Any], constraints: dict[str, bool]) -> tuple[list[str], dict[str, int], dict[str, list[str]], set[str]]:
    norm = normalize(text)
    scores: dict[str, int] = {}
    hits: dict[str, list[str]] = {}
    direct: set[str] = set()
    for cap in registry["capabilities"]:
        cid = cap["id"]
        matched: list[str] = []
        score = 0
        standard_triggers = list(cap.get("triggers", []))
        semantic_triggers = list(cap.get("semantic_triggers", []))
        # The semantic list is not decorative metadata: it is an active route input.
        # Exact domain phrases receive stronger weight than generic conversational verbs.
        generic_semantics = {normalize(x) for x in ["帮我做", "帮我处理", "帮我完成", "做一下", "写一下", "帮我", "处理一下", "优化一下", "分析一下"]}
        for trigger in list(dict.fromkeys(standard_triggers + semantic_triggers)):
            tnorm = normalize(trigger)
            if not tnorm or tnorm not in norm:
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
        strong_semantic_hit = any(normalize(x) in norm and len(normalize(x)) >= 5 and normalize(x) not in generic_semantics for x in semantic_triggers)
        if score >= 3 or (len(set(matched)) >= 2 and score >= 2.5) or strong_semantic_hit:
            direct.add(cid)

    # Chinese plain-language semantic cue pass. This complements phrase weights because
    # many valid Chinese intent nouns are only two characters long.
    def has(*phrases: str) -> bool:
        return any(normalize(x) in norm for x in phrases)

    if has("小说", "长篇小说", "网文", "章节", "故事大纲", "小说大纲"):
        direct.add("novel_writing")
    if has("剧本", "剧作", "分场", "对白", "台词", "编剧") and not constraints["writing_only"]:
        direct.add("screenwriting")
    if has("分镜", "逐镜", "镜头表", "镜头脚本", "故事板", "storyboard", "shot list") and not constraints["explicit_no_storyboard"]:
        direct.add("storyboard")
    if has("视频提示词", "视频prompt", "文生视频", "图生视频", "视频生成提示词", "视频续写", "视频投喂") and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_video_prompt", False):
        direct.add("video_prompt")
    if has("图片提示词", "图像提示词", "绘图提示词", "出图提示词", "静帧提示词", "一张图片提示词", "一张图的提示词") and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_image_prompt", False):
        direct.add("image_prompt")
    if (has("提示词工程", "负面提示词", "正向提示词", "灯光方案", "视觉基因") or (has("提示词") and not phrase_is_negated(text, "提示词")) or (has("prompt") and not phrase_is_negated(text, "prompt"))) and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_prompt_engineering", False):
        direct.add("prompt_engineering")
    if has("运镜", "推镜", "拉镜", "低机位", "焦段", "景别", "摄影机", "摄影方案", "镜头节奏", "构图", "灯光方案"):
        direct.add("cinematography")
    if has("视频提示词", "文生视频", "图生视频") and has("时间码", "动作", "表情", "运镜", "镜头") and not constraints["explicit_no_prompt"] and not constraints.get("explicit_no_video_prompt", False):
        direct.add("storyboard")
    if has("站位", "轴线", "越轴", "人物位置", "位置不一致", "空间关系", "场面调度", "镜头接不上", "走位", "连续性"):
        direct.add("spatial_continuity")
    if has("检查", "审查", "质检", "找bug", "查bug", "找漏洞", "修复", "排查", "逻辑矛盾", "一致性检查", "是否自洽", "避免漂浮", "避免穿模"):
        direct.add("quality_assurance")
    if has("角色四视图", "角色卡", "角色设定", "人物设定", "角色脸型", "发色", "服装和配饰", "角色定妆", "人物外观", "角色一致性", "人物服装", "角色服装", "服饰造型", "人物造型") or (has("角色") and has("恐惧", "愤怒", "微表情", "表演", "眼神", "呼吸")):
        direct.add("character_design")
    if has("资产包", "资产板", "资产前置", "先做资产", "先做角色", "四视图资产", "场景和道具"):
        direct.add("asset_first")
    if has("资产锁定", "锁定资产", "角色资产锁定", "人物资产锁定", "场景资产锁定", "资产冻结", "锁定人物和场景", "先锁定角色和场景", "分镜资产引用", "资产版本锁定", "资产漂移修复") or (has("人物资产", "角色资产", "场景资产") and has("先锁定", "锁定后", "版本锁定", "引用资产", "分镜资产")):
        direct.add("asset_locking")
    if has("古风", "国风", "赛博朋克", "冷艳", "导演风格", "视觉基因", "色彩体系", "配色", "美术指导", "灯光方案"):
        direct.add("aesthetics_style")
    if has("音效", "声音设计", "环境音", "拟音", "配音", "配乐", "旁白", "声音分层"):
        direct.add("audio_design")
    if has("api", "接口", "json请求", "请求参数", "端点", "webhook"):
        direct.add("api_integration")
    if has("外部skill", "claude code", "codex", "dify", "coze", "智能体集成", "agent集成", "安装skill"):
        direct.add("external_skill_integration")
    if has("参考图", "参考视频", "反推", "反向工程", "拍摄方案") and (has("参考", "反推") or "reverse" in norm):
        direct.add("reverse_engineering")
    if has("参考图", "参考视频", "参考素材") and has("保持一致", "完全一致", "一比一还原", "按图还原", "照着", "参考图一致", "还原人物", "复刻构图", "保持角色一致"):
        direct.add("reverse_engineering")
    if has("武打", "打斗", "动作戏", "攻防", "战斗动作", "受力反馈", "动作预演"):
        direct.add("action_choreography")
    if has("粒子", "爆炸特效", "特效", "物理模拟", "穿模", "重力", "惯性"):
        direct.add("vfx_physics")
    if has("项目状态", "状态文件", "跨轮次", "设定锁", "人物关系", "已埋伏笔", "世界观连续性", "项目记忆"):
        direct.add("project_state_management")
    if has("seedance", "可灵", "veo", "runway", "sora", "模型语法", "模型适配"):
        direct.add("model_adaptation")
    if has("版权", "原创性", "平台合规", "侵权", "内容审核"):
        direct.add("safety_originality")
    short_video_content_intent = (
        has("短视频文案", "口播", "抖音脚本", "小红书视频文案", "视频号脚本", "tiktok脚本", "竖屏短剧", "短视频脚本", "短视频平台方案", "开头三秒", "黄金三秒", "完播率", "转粉", "转化率", "短视频选题")
        or (has("短视频") and has("文案", "脚本", "选题", "开头三秒", "黄金三秒", "完播率", "转粉", "转化率", "口播"))
        or (has("抖音", "小红书", "视频号", "tiktok") and has("脚本", "文案", "口播", "开头三秒", "短视频发布"))
    )
    if short_video_content_intent:
        direct.add("short_video_content")
    if has("平台适配", "发布策略", "字幕安全区", "比例适配", "视频内容适配"):
        direct.add("platform_adaptation")
    if has("从创意到成片", "完整制作", "全流程制作", "全链路交付", "一整套全流程"):
        direct.add("full_production")
    if has("角色卡", "四视图", "角色定妆", "角色外观", "角色脸型") and has("一致", "资产", "设定", "人物"):
        direct.add("asset_first")
    # Compound asset-first phrasing appears in many forms. Treat natural wording such as
    # “先设计人物和场景图，再做分镜” as an ordered asset pipeline, even when the user
    # does not use the technical word “资产”. Local negation must suppress only the excluded asset.
    character_visual_terms = (
        "角色图", "人物图", "人设图", "角色设定图", "人物设定图", "角色四视图", "人物四视图",
        "角色三视图", "人物三视图", "角色定妆照", "人物定妆照", "角色资产图", "人物资产图",
        "角色立绘", "人物立绘", "角色卡", "人物卡", "角色造型图", "人物造型图"
    )
    scene_visual_terms = (
        "场景图", "环境图", "场景设定图", "环境设定图", "场景资产图", "场景概念图",
        "环境概念图", "场景布局图", "背景设定图", "场景原画", "场景美术图"
    )
    paired_asset_phrases = (
        "人物和场景图", "角色和场景图", "人物与场景图", "角色与场景图", "人物场景设定图",
        "角色场景设定图", "人物和场景设定图", "角色和场景设定图", "人物图和场景图",
        "角色图和场景图", "人设图和场景图", "人物设定图和场景设定图", "角色设定图和场景设定图",
        "人物和环境图", "角色和环境图", "人物场景资产", "角色场景资产"
    )
    positive_character_visual = any(has(term) and not phrase_is_negated(text, term) for term in character_visual_terms)
    positive_scene_visual = any(has(term) and not phrase_is_negated(text, term) for term in scene_visual_terms)
    positive_paired_assets = any(has(term) and not phrase_is_negated(text, term) for term in paired_asset_phrases)
    creation_action = has("设计", "生成", "制作", "绘制", "出图", "做出", "先做", "先出", "创建", "构建", "定稿")
    colloquial_asset_first = positive_paired_assets or (positive_character_visual and positive_scene_visual and creation_action)
    if colloquial_asset_first:
        direct.update({"asset_first", "character_design"})
        # A later storyboard stage must consume the canonical character/scene assets.
        if has("分镜", "故事板", "逐镜", "关键帧", "镜头图") and not constraints["explicit_no_storyboard"]:
            direct.update({"asset_locking", "storyboard", "spatial_continuity"})
        elif has("锁定", "定稿", "保持一致", "不要变化", "不能变", "跨镜头"):
            direct.add("asset_locking")
    # Technical phrasing is also supported for callers who explicitly say “asset”.
    if has("人物和场景资产", "人物资产和场景资产", "角色和场景资产", "角色资产和场景资产", "人物资产图", "场景资产图", "角色资产图", "场景资产图") and has("分镜图", "分镜资产", "镜头图", "逐镜图"):
        direct.update({"asset_first", "asset_locking", "character_design", "storyboard", "spatial_continuity"})

    # Resource evidence is deliberately narrow: workflow/reference tags describe all modules
    # a file can support, not all modules the user has requested. Generic resource hits must
    # never turn every tag on (the former cause of visual-prompt over-dispatch).
    capabilities_valid = {c.get("id") for c in registry.get("capabilities", [])}
    resources = registry.get("resources", [])
    basename_counts: dict[str, int] = {}
    trigger_owner: dict[str, set[str]] = {}
    heading_owner: dict[str, set[str]] = {}
    for rec in resources:
        if rec.get("type") != "reference" or rec.get("status") == "alias":
            continue
        basename = rec.get("_runtime_name_norm", normalize(Path(rec.get("file", "")).name))
        basename_counts[basename] = basename_counts.get(basename, 0) + 1
        rel = rec.get("file", "")
        for trig, tn in rec.get("_runtime_trigger_pairs", []):
            if len(tn) >= 8:
                trigger_owner.setdefault(tn, set()).add(rel)
        for heading, hn in rec.get("_runtime_heading_pairs", []):
            if len(hn) >= 10:
                heading_owner.setdefault(hn, set()).add(rel)
    for resource in resources:
        rel = resource.get("file", "")
        path_norm = resource.get("_runtime_path_norm", normalize(rel))
        name_norm = resource.get("_runtime_name_norm", normalize(Path(rel).name))
        # An explicit complete path is precise. A basename is accepted only when unique.
        explicit_path_hit = bool(path_norm and len(path_norm) >= 8 and path_norm in norm)
        explicit_name_hit = bool(name_norm and len(name_norm) >= 10 and basename_counts.get(name_norm, 0) == 1 and name_norm in norm)
        if explicit_path_hit or explicit_name_hit:
            primary = resource.get("primary_capability")
            if primary in capabilities_valid:
                direct.add(primary)
                hits.setdefault(primary, []).append("显式资源路径：" + rel)
                scores[primary] = scores.get(primary, 0) + 4
            continue
        if resource.get("type") != "reference" or resource.get("status") == "alias":
            continue
        primary = resource.get("primary_capability")
        if primary not in capabilities_valid:
            continue
        specific_hit = any(
            len(tn) >= 8 and tn in norm and trigger_owner.get(tn) == {rel} and not phrase_is_negated(text, trig)
            for trig, tn in resource.get("_runtime_trigger_pairs", [])
        )
        section_hit = any(
            len(hn) >= 10 and hn in norm and heading_owner.get(hn) == {rel} and not phrase_is_negated(text, heading.get("heading", ""))
            for heading, hn in resource.get("_runtime_heading_pairs", [])
        )
        if specific_hit or section_hit:
            direct.add(primary)
            hits.setdefault(primary, []).append("专属知识触发：" + rel)
            scores[primary] = scores.get(primary, 0) + 3

    # Explicit task families take precedence when the target deliverable is clear.
    if explicit_architecture_audit(text, norm): direct.add("skill_architecture_audit")
    if constraints["full_pipeline_explicit"]: direct.add("full_production")
    if constraints["writing_only"]:
        direct.add("novel_writing" if any(x in norm for x in ["小说", "章节", "世界观", "续写"]) else "screenwriting")
    if constraints["storyboard_only"]: direct.add("storyboard")
    if constraints["prompt_only"] and not constraints["explicit_no_prompt"]: direct.add("prompt_engineering")

    # Hard negative constraints remove deliverable routes before and during dependency expansion.
    forbidden: set[str] = set()
    if constraints["explicit_no_prompt"]:
        forbidden.update({"image_prompt", "video_prompt", "prompt_engineering"})
    else:
        if constraints.get("explicit_no_image_prompt", False): forbidden.add("image_prompt")
        if constraints.get("explicit_no_video_prompt", False): forbidden.add("video_prompt")
        if constraints.get("explicit_no_prompt_engineering", False): forbidden.add("prompt_engineering")
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
            "aesthetics_style", "platform_adaptation", "full_production"
        }
        forbidden.update(creative_deliverables)
        direct.difference_update(creative_deliverables)
    if not direct:
        # Do not leave a white-language request un-routed, even when it is unusual or underspecified.
        direct.add("general_orchestration")

    selected = set(direct)
    cap_by_id = {c["id"]: c for c in registry["capabilities"]}
    pending = list(selected)
    while pending:
        cid = pending.pop()
        for dep in cap_by_id.get(cid, {}).get("dependencies", []):
            if dep in forbidden or dep in selected:
                continue
            selected.add(dep)
            pending.append(dep)

    # Explicit negatives remain authoritative after closure; a blocked dependency is not a deliverable route.
    selected.difference_update(forbidden)
    production_like = selected.intersection({"novel_writing", "screenwriting", "storyboard", "character_design", "image_prompt", "video_prompt", "prompt_engineering", "reverse_engineering", "action_choreography", "audio_design", "full_production", "asset_first"})
    if production_like:
        selected.update({"quality_assurance", "safety_originality"})
    return sorted(selected), scores, hits, direct


def select_workflows(text: str, norm: str, registry: dict[str, Any], constraints: dict[str, bool], capabilities: list[str], direct_capabilities: set[str] | None = None) -> list[dict[str, Any]]:
    """Return every compatible workflow route; no presentation limit is applied here."""
    wf_by_id = {w["id"]: w for w in registry["workflows"]}
    found: dict[str, dict[str, Any]] = {}
    reasons: dict[str, list[str]] = {}
    direct_capabilities = set(capabilities) if direct_capabilities is None else set(direct_capabilities)

    def is_blocked(wid: str) -> bool:
        if wid == "full-production" and constraints.get("explicit_no_full_project") and not constraints.get("full_pipeline_explicit"):
            return True
        if wid == "visual-prompt" and (constraints.get("explicit_no_prompt") or (constraints.get("explicit_no_image_prompt") and constraints.get("explicit_no_video_prompt"))):
            return True
        if wid == "visual-prompt" and constraints.get("explicit_no_video_prompt") and not constraints.get("explicit_no_image_prompt") and "image_prompt" not in capabilities:
            return True
        if wid == "storyboard-only" and constraints.get("explicit_no_storyboard"):
            return True
        if wid == "storyboard-only" and not constraints.get("storyboard_only"):
            compound_deliverables = {"screenwriting", "video_prompt", "image_prompt", "full_production", "action_choreography", "asset_locking", "asset_first"}
            if compound_deliverables.intersection(direct_capabilities):
                return True
            if any(x in found for x in ("asset-lock", "asset-first", "script-to-screen", "full-production")):
                return True
        if wid == "writing" and not any(c in capabilities for c in ("novel_writing", "screenwriting")):
            return True
        return False

    def add(wid: str, reason: str):
        wf = wf_by_id.get(wid)
        if not wf or is_blocked(wid):
            return
        found[wid] = wf
        reasons.setdefault(wid, [])
        if reason not in reasons[wid]: reasons[wid].append(reason)

    # The intent analysis router is a non-optional front door and runs on every request.
    for wf in registry["workflows"]:
        if wf.get("always_run") or wf.get("entrypoint") or wf.get("execution_mode") == "always":
            add(wf["id"], "强制入口：所有请求先执行意图解析")

    # Explicit macro-workflow triggers.
    for wf in registry["workflows"]:
        matched = [tr for tr, tn in wf.get("_runtime_trigger_pairs", [(tr, normalize(tr)) for tr in wf.get("triggers", [])]) if tn and tn in norm and not phrase_is_negated(text, tr)]
        if not matched:
            continue
        excluded = [x for x in wf.get("exclude_if", []) if normalize(x) in norm]
        if excluded: continue
        for tr in matched: add(wf["id"], f"显式工作流触发：{tr}")

    # Macro workflows are auto-dispatched only from directly requested capabilities.
    # Dependency-expanded capabilities contribute their rules as support modules; they do not
    # launch unrelated standalone macros (e.g. a camera dependency must not force storyboard-only).
    cap_by_id = {c["id"]: c for c in registry["capabilities"]}
    for cid in direct_capabilities:
        cap = cap_by_id.get(cid, {})
        for wid in cap.get("workflow_routes", {}).get("auto", []):
            add(wid, f"直接能力自动路由：{cid}")

    # Add declared conditional routes only when directly asked or a known compound route is present.
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
        if required.issubset(direct): add(wid, reason)

    # Conditional capability routes do not all fire indiscriminately. They activate on a matched macro-workflow
    # trigger, an explicitly selected capability bundle, or an explicit request to create a full project.
    explicit_workflow_ids = set(found)
    for cid in direct:
        cap = cap_by_id.get(cid, {})
        for wid in cap.get("workflow_routes", {}).get("conditional", []):
            if wid in explicit_workflow_ids:
                add(wid, f"条件路由确认：{cid} 与工作流触发兼容")
            elif constraints.get("full_pipeline_explicit") and wid == "full-production":
                add(wid, f"全流程硬约束：{cid}")

    if constraints.get("full_pipeline_explicit"):
        add("full-production", "用户明确要求完整制作全流程")

    # Keep the front door first, then primary work pipelines by priority; never slice this list.
    wf_items = list(found.items())
    wf_items.sort(key=lambda kv: (kv[0] != "intent-analysis", -int(kv[1].get("priority", 0)), kv[0]))
    return [{"id": wid, "name": wf.get("name", wid), "file": wf.get("file"),
             "matched_triggers": reasons.get(wid, []), "priority": wf.get("priority", 0),
             "always_run": bool(wf.get("always_run") or wf.get("entrypoint") or wf.get("execution_mode") == "always")}
            for wid, wf in wf_items]


def select_resources(registry: dict[str, Any], capabilities: list[str], text: str, max_modules: int=30, direct_capabilities: set[str] | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Build the complete route-candidate set, then rank a bounded load plan separately.

    max_modules limits initial reference loading only. It never drops candidate resources or graph edges.
    """
    norm = normalize(text)
    selected_tags = set(capabilities)
    direct_tags = set(direct_capabilities or set())
    infra = {"SKILL.md", "routing/route-registry.json", "routing/route-graph.json", "workflows/index.yaml",
             "workflows/intent-analysis.yaml", "scripts/route_request.py", "scripts/audit_package.py"}
    candidates = []
    aliases_by_path = {r.get("file"): r for r in registry.get("resources", [])}
    for resource in registry["resources"]:
        path = resource.get("file", "")
        status = resource.get("status", "canonical")
        tags = set(resource.get("tags", []))
        tag_hits = selected_tags.intersection(tags)
        direct_tag_hits = direct_tags.intersection(tags)
        path_norm = resource.get("_runtime_path_norm", normalize(path))
        name_norm = resource.get("_runtime_name_norm", normalize(Path(path).name))
        stem_norm = resource.get("_runtime_stem_norm", normalize(Path(path).stem))
        explicit_path = bool(norm and (path_norm in norm or name_norm in norm or (len(stem_norm) >= 6 and stem_norm in norm)))
        trigger_hits = []
        for trig, tn in resource.get("_runtime_trigger_pairs", [(trig, normalize(trig)) for trig in resource.get("triggers", [])]):
            if not tn or tn not in norm: continue
            if len(tn) < 4 or phrase_is_negated(text, trig): continue
            trigger_hits.append(trig)
        heading_hits = []
        for h, hn in resource.get("_runtime_heading_pairs", [(h, normalize(h.get("heading", ""))) for h in resource.get("headings", [])]):
            if hn and len(hn) >= 5 and hn in norm and not phrase_is_negated(text, h.get("heading", "")):
                heading_hits.append(h)
        is_infra = path in infra
        audit_request = "skill_architecture_audit" in selected_tags
        if not (tag_hits or explicit_path or trigger_hits or heading_hits or is_infra or audit_request):
            continue
        # Direct intent gets a larger weight than dependency/support tags.
        score = len(tag_hits) * 2 + len(direct_tag_hits) * 6 + len(trigger_hits) * 4 + len(heading_hits) * 12
        reasons = []
        if tag_hits: reasons.append("capability_tags=" + ",".join(sorted(tag_hits)))
        if direct_tag_hits: reasons.append("direct_intent_tags=" + ",".join(sorted(direct_tag_hits)))
        if trigger_hits: reasons.append("resource_triggers=" + ",".join(trigger_hits[:8]))
        if heading_hits: reasons.append("exact_heading_match")
        if explicit_path: score += 100; reasons.append("explicit_resource_path")
        if is_infra: score += 8; reasons.append("route_infrastructure")
        if status == "alias": score -= 2
        if status == "retained_source" and not audit_request and not explicit_path: score -= 2
        canonical = resource.get("alias_of") or path
        # Exact alias request remains traceable but default reads the canonical content once.
        candidates.append({"file": canonical, "source_path": path, "type": resource.get("type"),
                           "status": status, "score": int(score), "tags": sorted(tags),
                           "route_reasons": reasons or ["reachable_by_registry_graph"],
                           "alias_redirect": canonical if canonical != path else None,
                           "explicit_path_match": explicit_path,
                           "matched_trigger_count": len(trigger_hits),
                           "matched_heading_count": len(heading_hits)})

    # If the task explicitly asks for a deep audit, include every registered resource as a candidate.
    if "skill_architecture_audit" in selected_tags:
        existing = {x["source_path"] for x in candidates}
        for resource in registry.get("resources", []):
            if resource["file"] in existing: continue
            candidates.append({"file": resource.get("alias_of") or resource["file"], "source_path": resource["file"],
                "type":resource.get("type"), "status":resource.get("status","canonical"), "score":0,
                "tags":resource.get("tags",[]), "route_reasons":["full-audit-inventory"],
                "alias_redirect":resource.get("alias_of"), "explicit_path_match":False,
                "matched_trigger_count":0,"matched_heading_count":0})

    # Preserve each registry source path as a separate route candidate (including aliases).
    # Deduplicate only the actual read list, so aliases stay auditable without re-reading duplicate text.
    candidates.sort(key=lambda x: (-x["score"], x["source_path"]))
    all_candidates = candidates
    reference_candidates = []
    seen_canonical_files = set()
    for item in all_candidates:
        if item.get("type") != "reference":
            continue
        canonical_file = item.get("file")
        if canonical_file in seen_canonical_files:
            continue
        seen_canonical_files.add(canonical_file)
        reference_candidates.append(item)
    load_plan = reference_candidates[:max_modules]
    # Section matching is distinct from resource loading. Any exact requested heading is returned even if its document is deferred.
    sections=[]
    for resource in registry.get("resources", []):
        if resource.get("type") != "reference" or resource.get("status") == "alias": continue
        if not (selected_tags.intersection(resource.get("tags", [])) or "skill_architecture_audit" in selected_tags): continue
        for h, hn in resource.get("_runtime_heading_pairs", [(h, normalize(h.get("heading", ""))) for h in resource.get("headings", [])]):
            if hn and len(hn)>=5 and hn in norm and not phrase_is_negated(text, h.get("heading", "")):
                sections.append({"file":resource["file"],"heading":h["heading"],"anchor":h["anchor"],"level":h["level"],"match":"exact_heading_in_request"})
    # Don't silently cap section results. Return all true exact matches.
    return load_plan, sections, all_candidates


def route(text: str, max_modules: int=30) -> dict[str, Any]:
    registry=load_registry()
    norm=normalize(text)
    constraints=explicit_output_constraints(text,norm)
    caps,scores,hits,direct_caps=detect_capabilities(text,registry,constraints)
    workflows=select_workflows(text,norm,registry,constraints,caps,direct_caps)
    modules,sections,resource_candidates=select_resources(registry,caps,text,max_modules=max_modules,direct_capabilities=direct_caps)
    all_reference_candidates=[r for r in resource_candidates if r.get("type")=="reference"]
    loaded_files = {r.get("file") for r in modules}
    deferred = []
    deferred_seen = set()
    for r in all_reference_candidates:
        canonical_file = r.get("file")
        if canonical_file not in loaded_files and canonical_file not in deferred_seen:
            deferred.append(r)
            deferred_seen.add(canonical_file)
    cap_names={c["id"]:c["name"] for c in registry["capabilities"]}
    graph_status = graph_coverage_status(registry)
    return {
        "input":text,
        "skill_version":registry.get("skill",{}).get("version"),
        "intent_analysis_required":True,
        "selected_capabilities":[{"id":cid,"name":cap_names.get(cid,cid),"matched_triggers":hits.get(cid,[]),"score":scores.get(cid,0),"direct_match":cid in direct_caps} for cid in caps],
        "direct_capability_ids":sorted(direct_caps),
        "workflows":workflows,
        "primary_workflow":next((w for w in workflows if w["id"]!="intent-analysis"), workflows[0] if workflows else None),
        "recommended_modules":modules,
        "deferred_reference_resources":deferred,
        "resource_route_candidates":resource_candidates,
        "resource_route_candidate_count":len(resource_candidates),
        "resource_candidate_truncated":False,
        "matched_sections":sections,
        "matched_section_count":len(sections),
        "constraints":constraints,
        "intent_analysis": {
            "raw_request_preserved": text,
            "direct_capabilities": sorted(direct_caps),
            "dependency_expanded_capabilities": sorted(set(caps) - set(direct_caps)),
            "hard_constraints": constraints,
            "matched_capability_evidence": {cid: hits.get(cid, []) for cid in sorted(caps) if hits.get(cid)},
            "needs_host_semantic_review": True,
            "semantic_review_contract": "宿主模型必须结合上下文复核隐含意图、并列交付物、否定范围、例外与歧义；本地触发器提供可审计候选路由，不等同于对任意表述的完美语义理解。"
        },
        "module_limit":max_modules,
        "module_list_truncated":len(all_reference_candidates)>len(modules),
        "route_coverage":{
            "all_requests_enter_intent_analysis":any(w["id"]=="intent-analysis" for w in workflows),
            "all_selected_capabilities_have_declared_auto_workflow":all(
                bool(next((c for c in registry["capabilities"] if c["id"]==cid),{}).get("workflow_routes",{}).get("auto")) for cid in caps),
            "all_registered_resources_kept_in_registry_graph":graph_status["ok"],
            "route_graph_status":graph_status,
            "candidate_routes_not_silently_truncated":True,
            "selected_capability_count":len(caps),
            "direct_capability_count":len(direct_caps),
            "workflow_count":len(workflows),
            "all_candidate_resource_count":len(resource_candidates),
            "loaded_reference_count":len(modules),
            "deferred_reference_count":len(deferred)
        },
        "execution_note":"已生成完整路由候选集合；recommended_modules 是当前上下文预算下的首批读取清单，deferred_reference_resources 保留其余候选，不代表路由被删除。该脚本执行本地路由规划，不会自动调用外部模型/API；外部执行需要宿主工具权限。"
    }

def main() -> int:
    parser=argparse.ArgumentParser(description="QHSJ AIGC 全能影视 白话多标签路由预览")
    parser.add_argument("request",nargs="?",help="用户白话需求")
    parser.add_argument("--json",action="store_true",help="以 JSON 输出")
    parser.add_argument("--max-modules",type=int,default=30,help="首批加载的规范参考模块数量上限，默认 30；不截断完整路由候选集")
    parser.add_argument("--list-routes",action="store_true",help="列出所有能力路由 ID 和触发词")
    args=parser.parse_args()
    try:
        registry=load_registry()
        if args.list_routes:
            print(json.dumps([{"id":c["id"],"name":c["name"],"triggers":c["triggers"],"dependencies":c["dependencies"]} for c in registry["capabilities"]],ensure_ascii=False,indent=2))
            return 0
        if not args.request:
            parser.error("必须提供用户白话需求，或使用 --list-routes")
        if args.max_modules<1 or args.max_modules>300:
            parser.error("--max-modules 必须在 1 至 300 之间")
        result=route(args.request,args.max_modules)
        if args.json:
            print(json.dumps(result,ensure_ascii=False,indent=2))
        else:
            print(f"QHSJ AIGC 全能影视 路由预览 v{result['skill_version']}")
            print(f"\n输入：{result['input']}")
            print("\n【命中能力】")
            for item in result["selected_capabilities"]:
                hits="、".join(item["matched_triggers"][:8]) or "依赖扩展"
                print(f"- {item['id']} — {item['name']}（匹配：{hits}）")
            print("\n【工作流】")
            for item in result["workflows"]:
                print(f"- {item['id']}：{item['file']}")
            print("\n【建议读取的模块】")
            for item in result["recommended_modules"]:
                print(f"- {item['file']}（score={item['score']}）")
            print(f"\n完整资源路由候选：{result['resource_route_candidate_count']} 项；首批读取：{len(result['recommended_modules'])} 项；延后读取：{len(result['deferred_reference_resources'])} 项")
            print("\n【工作流调度顺序】")
            for item in result["workflows"]:
                print(f"- {item['id']}（priority={item.get('priority')}）：{'; '.join(item.get('matched_triggers', []))}")
            if result["matched_sections"]:
                print("\n【直接命中的章节】")
                for item in result["matched_sections"]:
                    print(f"- {item['file']} :: {item['heading']}")
            print("\n说明："+result["execution_note"])
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"路由错误：{e}",file=sys.stderr)
        return 2
    return 0

if __name__=="__main__":
    raise SystemExit(main())
