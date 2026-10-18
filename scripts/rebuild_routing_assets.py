#!/usr/bin/env python3
"""Deterministically rebuild QHSJ registry, route graph, and package manifest.

No unique knowledge is removed. Byte-identical reference bodies are stored once;
former duplicate paths remain navigable compatibility aliases with original SHA-256
metadata, complete inherited section routing, and explicit redirect semantics.
"""
from __future__ import annotations
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit("需要 PyYAML：请先安装 pyyaml 后重建路由资产") from exc

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "routing/route-registry.json"
GRAPH_PATH = ROOT / "routing/route-graph.json"
MANIFEST_PATH = ROOT / "MANIFEST.json"
VERSION = "3.0.0"
DISPLAY_NAME = "QHSJ AIGC 全能影视"
META_FILES = {"MANIFEST.json", "routing/route-registry.json", ".gitignore"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ALIAS_MARKER = "<!-- QHSJ-CONTENT-ALIAS "

def parse_alias_stub(text: str) -> dict[str, str] | None:
    """Read a lightweight compatibility alias without mistaking ordinary Markdown for one."""
    first = text.splitlines()[0] if text.splitlines() else ""
    if not first.startswith(ALIAS_MARKER) or not first.endswith("-->"):
        return None
    body = first[len(ALIAS_MARKER):-3].strip()
    fields: dict[str, str] = {}
    for item in re.findall(r"([a-z0-9_]+)=\"([^\"]*)\"", body):
        fields[item[0]] = item[1]
    return fields if fields.get("canonical") else None


def make_alias_stub(rel: str, canonical: str, original_sha256: str, source_text: str) -> str:
    """Keep a former path navigable while storing byte-identical knowledge only once."""
    title = Path(rel).name
    for line in source_text.splitlines():
        m = re.match(r"^#{1,2}\s+(.+?)\s*#*\s*$", line)
        if m:
            title = m.group(1).strip()
            break
    relative_target = Path(canonical).name if Path(rel).parent == Path(canonical).parent else canonical
    return (
        f'{ALIAS_MARKER}canonical="{canonical}" original_sha256="{original_sha256}"-->' + "\n"
        f"# 兼容路由别名：{title}\n\n"
        "> 本文件原正文与规范正文完全相同，为避免重复维护，正文只保留一份。\n\n"
        f"> 规范正文：`{canonical}`（[`{Path(canonical).name}`]({relative_target})）\n\n"
        "> 路由、工作流和显式旧路径仍可通过此别名定位规范正文；需要执行任何规则时，必须继续读取上方规范正文，不得把本页当作完整知识正文。\n"
    )


def dedupe_exact_reference_bodies(root: Path, old_registry: dict[str, Any]) -> dict[str, Any]:
    """Collapse only byte-identical reference Markdown into path-preserving aliases.

    No unique paragraph or rule is removed: each alias is created only after its SHA-256
    matches the canonical file. Original hashes and route paths stay recorded.
    """
    old_by_path = {r.get("file"): r for r in old_registry.get("resources", []) if isinstance(r, dict)}
    reference_root = root / "references"
    files = [p for p in reference_root.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".markdown"}]
    # First convert registered byte-identical aliases while their source bodies are still present.
    for path in files:
        rel = path.relative_to(root).as_posix()
        prior = old_by_path.get(rel, {})
        prior_target = prior.get("alias_of")
        if not prior_target:
            continue
        target = root / prior_target
        if not target.is_file():
            continue
        current_text = path.read_text(encoding="utf-8", errors="replace")
        marker = parse_alias_stub(current_text)
        if marker:
            continue
        current_hash = sha256(path)
        if current_hash == sha256(target):
            path.write_text(make_alias_stub(rel, prior_target, current_hash, current_text), encoding="utf-8")
    # Find any further exact copies that were added since the last build. Existing alias stubs
    # are intentionally excluded because they hold routing metadata, not a second knowledge body.
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        txt = path.read_text(encoding="utf-8", errors="replace")
        if parse_alias_stub(txt):
            continue
        groups[sha256(path)].append(path)
    collapsed = []
    for content_hash, group in groups.items():
        if len(group) < 2:
            continue
        rels = [x.relative_to(root).as_posix() for x in group]
        old_canonicals = [x for x in rels if old_by_path.get(x, {}).get("status") == "canonical" and not old_by_path.get(x, {}).get("alias_of")]
        candidates = old_canonicals or rels
        canonical = min(candidates, key=lambda rel: (
            bool(re.match(r"references/(p1-|v\d|old-|archive-)", rel, re.I)), len(rel), rel
        ))
        canonical_path = root / canonical
        for alias_rel in rels:
            if alias_rel == canonical:
                continue
            alias_path = root / alias_rel
            original_text = alias_path.read_text(encoding="utf-8", errors="replace")
            alias_path.write_text(make_alias_stub(alias_rel, canonical, content_hash, original_text), encoding="utf-8")
            collapsed.append({"alias": alias_rel, "canonical": canonical, "original_sha256": content_hash})
    return {"collapsed": collapsed, "existing_aliases": sum(1 for r in old_registry.get("resources", []) if r.get("status") == "alias")}


def heading_records(path: Path) -> list[dict[str, Any]]:
    out = []
    seen: dict[str, int] = defaultdict(int)
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if not m:
            continue
        heading = m.group(2).strip()
        base = re.sub(r"[^\w\u4e00-\u9fff -]", "", heading.lower())
        base = re.sub(r"\s+", "-", base).strip("-")
        count = seen[base]
        seen[base] += 1
        slug = base if count == 0 else f"{base}-{count}"
        out.append({"level": len(m.group(1)), "heading": heading, "anchor": slug,
                    "triggers": [heading] if len(heading) >= 4 else []})
    return out


def norm_path(p: str) -> str:
    return p.replace("\\", "/").strip("./")


def list_files() -> dict[str, Path]:
    # Exclude build/cache/VCS artifacts so the manifest and registry never reference
    # files that are absent from a clean checkout.
    ignored_parts = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".tox", ".git", ".idea", ".vscode"}
    ignored_suffixes = {".pyc", ".pyo"}
    return {
        p.relative_to(ROOT).as_posix(): p
        for p in ROOT.rglob("*")
        if p.is_file() and p.suffix not in ignored_suffixes and not ignored_parts.intersection(p.parts)
    }


def infer_type(rel: str) -> str:
    p = Path(rel)
    if rel.startswith("references/") and p.suffix.lower() in {".md", ".markdown"}:
        return "reference"
    if rel.startswith("workflows/") and p.suffix.lower() in {".yaml", ".yml"}:
        return "workflow"
    if rel.startswith("scripts/") and p.suffix.lower() == ".py":
        return "script"
    if rel.startswith("schemas/") or p.name.endswith(".schema.json"):
        return "schema"
    if rel.startswith("templates/"):
        return "template"
    if rel.startswith("assets/"):
        return "asset"
    if p.suffix.lower() in {".yaml", ".yml"}:
        return "yaml"
    if p.suffix.lower() == ".json":
        return "data"
    if p.suffix.lower() in {".md", ".markdown"}:
        return "md"
    return "file"


def discover_path_aliases(files: dict[str, Path]) -> dict[str, str]:
    by_lower = {rel.lower(): rel for rel in files}
    # Previous versions used case-variant paths for these two references.
    fixed = {
        "references/15-qhsj-master-engine.md": "references/15-qhsj-master-engine.md",
        "references/qh-qhsj-system-core.md": "references/qh-qhsj-system-core.md",
    }
    return by_lower | fixed


def special_metadata(rel: str) -> tuple[list[str], list[str], str | None]:
    """Defaults for newly-added files; existing resource tags are preserved when possible."""
    table: dict[str, tuple[list[str], list[str], str | None]] = {
        "references/qhsj-asset-locking-protocol.md": (
            ["asset_locking", "asset_first", "character_design", "quality_assurance"],
            ["资产锁定", "锁定资产", "角色资产版本", "场景资产版本", "分镜资产引用", "canonical asset", "asset lock"], "asset_locking"),
        "references/qhsj-spatial-gaze-distance-ledger.md": (
            ["spatial_continuity", "storyboard", "cinematography", "quality_assurance"],
            ["空间关系", "人物距离", "视线目标", "身体朝向", "头部朝向", "眼睛朝向", "空间账本", "gaze target"], "spatial_continuity"),
        "references/qhsj-multiagent-review-protocol.md": (
            ["skill_architecture_audit", "general_orchestration", "quality_assurance"],
            ["多智能体审查", "多代理协作", "红队审查", "回归审查", "审查角色", "agent review"], "skill_architecture_audit"),
        "templates/asset-lock-ledger.md": (
            ["asset_locking", "asset_first", "project_state_management"],
            ["资产锁定台账", "版本台账", "资产依赖", "锁定状态"], "asset_locking"),
        "templates/spatial-continuity-ledger.md": (
            ["spatial_continuity", "storyboard", "project_state_management"],
            ["空间连续性台账", "人物站位", "人物距离", "视线目标", "镜头状态"], "spatial_continuity"),
        "workflows/asset-lock.yaml": (
            ["asset_locking", "asset_first", "character_design", "spatial_continuity", "quality_assurance"],
            ["人物资产锁定", "角色资产锁定", "场景资产锁定", "先锁定角色和场景", "资产冻结", "分镜资产引用角色图", "资产版本锁定"], "asset_locking"),
        "scripts/rebuild_routing_assets.py": (
            ["skill_architecture_audit", "general_orchestration"],
            ["重建路由资产", "更新路由图", "更新资源清单", "rebuild routing assets"], "skill_architecture_audit"),
        "AUDIT_REPORT.md": (
            ["skill_architecture_audit", "quality_assurance"],
            ["整改审计报告", "回归测试报告", "审计结果", "测试结果"], "skill_architecture_audit"),
    }
    if rel in table:
        return table[rel]
    if rel.startswith("schemas/"):
        tags = ["output_formatting", "project_state_management", "quality_assurance"]
        return tags, ["schema", Path(rel).name, "结构校验", "数据契约"], "output_formatting"
    if rel.startswith("workflows/"):
        if rel == "workflows/index.yaml":
            return ["general_orchestration", "skill_architecture_audit"], ["工作流索引", "全量工作流", "工作流路由"], "general_orchestration"
        return ["general_orchestration", "quality_assurance"], [Path(rel).stem, "工作流", "执行阶段", "失败回退"], "general_orchestration"
    if rel.startswith("scripts/"):
        return ["skill_architecture_audit", "quality_assurance"], [Path(rel).stem, "脚本检查", "自动化校验"], "skill_architecture_audit"
    if rel.startswith("templates/"):
        return ["output_formatting", "project_state_management"], [Path(rel).stem, "模板", "台账"], "output_formatting"
    if rel.startswith("references/"):
        return ["general_orchestration", "quality_assurance"], [Path(rel).stem, Path(rel).name, "专业参考"], "general_orchestration"
    if rel.startswith("evals/") or rel.startswith("tests/"):
        return ["skill_architecture_audit", "quality_assurance"], [Path(rel).stem, "回归测试", "路由评估"], "skill_architecture_audit"
    if rel.startswith("assets/"):
        return ["general_orchestration"], [Path(rel).name, "项目图标"], "general_orchestration"
    if rel in {"SKILL.md", "README.md", "CHANGELOG.md"}:
        return ["general_orchestration", "skill_architecture_audit"], [Path(rel).name, "QHSJ AIGC 全能影视", "总控"], "general_orchestration"
    return ["general_orchestration", "quality_assurance"], [Path(rel).name, Path(rel).stem], "general_orchestration"


def build_registry() -> tuple[dict[str, Any], dict[str, Path]]:
    files = list_files()
    path_alias = discover_path_aliases(files)
    old = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    old_by_actual: dict[str, dict[str, Any]] = {}
    for rec in old.get("resources", []):
        raw = norm_path(rec.get("file", ""))
        actual = path_alias.get(raw.lower(), raw if raw in files else None)
        if actual and actual in files:
            old_by_actual[actual] = dict(rec)

    # Repair case drift in capability and workflow references without renaming content files.
    for cap in old.get("capabilities", []):
        repaired = []
        for ref in cap.get("reference_files", []):
            raw = norm_path(ref)
            target = path_alias.get(raw.lower(), raw)
            repaired.append(target)
        cap["reference_files"] = list(dict.fromkeys(repaired))

    caps = old.get("capabilities", [])
    cap_ids = {c.get("id") for c in caps}
    if "asset_locking" not in cap_ids:
        caps.append({
            "id": "asset_locking",
            "name": "资产版本锁定与分镜资产引用",
            "triggers": [
                "资产锁定", "锁定资产", "角色资产锁定", "人物资产锁定", "场景资产锁定", "资产冻结",
                "锁定人物和场景", "先锁定角色和场景", "分镜资产引用", "分镜资产引用角色图", "资产版本管理",
                "资产版本锁定", "角色资产版本", "场景资产版本", "资产漂移修复"
            ],
            "semantic_triggers": [
                "先生成并锁定人物和场景资产", "锁定资产后再生成分镜图", "分镜引用已锁定参考图",
                "人物与场景先定稿", "资产版本不得漂移", "资产依赖影响扫描"
            ],
            "dependencies": ["character_design", "spatial_continuity", "project_state_management"],
            "reference_files": [
                "references/qhsj-asset-locking-protocol.md",
                "references/qhsj-spatial-gaze-distance-ledger.md",
                "references/qhsj-multiagent-review-protocol.md",
                "references/asset-ledger.md",
                "references/asset-package-spec.md",
                "references/asset-validation-cases-500.md",
                "templates/asset-lock-ledger.md",
                "templates/spatial-continuity-ledger.md",
                "schemas/project-state.schema.json",
                "schemas/storyboard.schema.json"
            ],
            "selection_policy": "strong_asset_lock_or_explicit_shot_asset_reference_intent",
            "priority": "high",
            "workflow_routes": {"auto": ["asset-lock"], "conditional": ["asset-first", "script-to-screen", "full-production"]},
            "route_contract": {
                "requires_intent_analysis": True,
                "dependency_closure": "recursive",
                "asset_lock_before_storyboard_asset_generation": True,
                "explicit_exclusions_win": True,
                "route_edges_verified": True
            }
        })
    # Strengthen asset-first/full-production dependencies, without adding a cycle.
    by_cap = {c["id"]: c for c in caps}
    for cid in ("asset_first", "full_production"):
        if cid in by_cap and "asset_locking" not in by_cap[cid].setdefault("dependencies", []):
            by_cap[cid]["dependencies"].append("asset_locking")
    # Ensure all capabilities have a valid automatic workflow, known dependencies, and route contracts.
    known_wf_ids = {w.get("id") for w in old.get("workflows", [])}
    known_wf_ids.add("asset-lock")
    for c in caps:
        c.setdefault("semantic_triggers", [])
        c.setdefault("selection_policy", "include_on_strong_phrase_or_two_independent_weak_signals")
        c.setdefault("workflow_routes", {"auto": ["intent-analysis"], "conditional": []})
        c.setdefault("route_contract", {})
        c["route_contract"].update({"requires_intent_analysis": True, "explicit_exclusions_win": True, "route_edges_verified": True})
        c["dependencies"] = list(dict.fromkeys(x for x in c.get("dependencies", []) if x in {x["id"] for x in caps}))
        c["workflow_routes"]["auto"] = [wid for wid in c["workflow_routes"].get("auto", []) if wid in known_wf_ids]
        if not c["workflow_routes"]["auto"]:
            c["workflow_routes"]["auto"] = ["intent-analysis"]
        c["workflow_routes"]["conditional"] = [wid for wid in c["workflow_routes"].get("conditional", []) if wid in known_wf_ids]

    # Read the human-authored workflow index as the routing source of truth for trigger/name metadata.
    index_path = ROOT / "workflows/index.yaml"
    index_data = yaml.safe_load(index_path.read_text(encoding="utf-8")) or {}
    index_workflows = {item.get("id"): item for item in index_data.get("workflows", []) if isinstance(item, dict)}
    old["workflow_index_version"] = index_data.get("version", VERSION)

    # Incorporate and register asset-lock workflow from its actual YAML definition.
    if not any(w.get("id") == "asset-lock" for w in old.get("workflows", [])):
        wf_path = ROOT / "workflows/asset-lock.yaml"
        wf_data = yaml.safe_load(wf_path.read_text(encoding="utf-8"))
        old.setdefault("workflows", []).append({
            "id": "asset-lock", "name": wf_data.get("name", "资产锁定与分镜引用工作流"),
            "file": "workflows/asset-lock.yaml", "priority": 85,
            "triggers": wf_data.get("triggers", []),
            "capabilities": ["asset_locking", "asset_first", "character_design", "spatial_continuity", "quality_assurance"],
            "entrypoint": False, "always_run": False, "execution_mode": "on_demand",
            "description": wf_data.get("description", ""), "routed_capabilities": ["asset_locking"]
        })

    # Refresh workflow metadata from index + actual workflow YAML while preserving extended fields.
    for wf in old.get("workflows", []):
        indexed = index_workflows.get(wf.get("id"), {})
        for key in ("name", "description", "priority", "triggers", "capabilities", "entrypoint", "always_run", "execution_mode"):
            if key in indexed:
                wf[key] = indexed[key]
        wf_path = ROOT / norm_path(wf.get("file", ""))
        if wf_path.is_file() and wf_path.suffix.lower() in {".yaml", ".yml"}:
            try:
                y = yaml.safe_load(wf_path.read_text(encoding="utf-8")) or {}
            except Exception:
                y = {}
            if isinstance(y, dict):
                if y.get("triggers"):
                    wf["triggers"] = list(dict.fromkeys(y["triggers"]))
                wf.setdefault("description", y.get("description", ""))
                wf["version"] = VERSION
        wf["file"] = norm_path(wf.get("file", ""))

    # Resource inventory: every package file except registry and manifest is registered.
    resources: list[dict[str, Any]] = []
    cap_id_set = {c["id"] for c in caps}
    for rel, path in sorted(files.items()):
        if rel in META_FILES:
            continue
        prior = old_by_actual.get(rel, {})
        tags = [t for t in prior.get("tags", []) if t in cap_id_set]
        triggers = list(prior.get("triggers", []))
        primary = prior.get("primary_capability")
        if not tags or not triggers:
            stags, striggers, sprimary = special_metadata(rel)
            if not tags:
                tags = stags
            if not triggers:
                triggers = striggers
            if not primary:
                primary = sprimary
        if not primary or primary not in tags:
            primary = next((t for t in tags if t in cap_id_set), "general_orchestration")
        # Add the actual canonical path and basename as searchable explicit names.
        for trig in (rel, Path(rel).name):
            if trig not in triggers:
                triggers.append(trig)
        # Recompute route anchors for every reference Markdown file; other files don't expose section-route nodes.
        typ = prior.get("type") or infer_type(rel)
        alias_meta = parse_alias_stub(path.read_text(encoding="utf-8", errors="replace")) if typ == "reference" and path.suffix.lower() == ".md" else None
        alias_target = (alias_meta or {}).get("canonical") or prior.get("alias_of")
        is_alias = bool(alias_target and alias_target in files and alias_meta)
        if typ == "reference" and path.suffix.lower() == ".md":
            heading_source = files.get(alias_target) if is_alias else path
            headings = heading_records(heading_source) if heading_source else []
        else:
            headings = []
        prior_status = prior.get("status", "canonical")
        if prior_status not in {"canonical", "alias", "retained_source"}:
            prior_status = "canonical"
        resource_id = re.sub(r"[^a-zA-Z0-9_-]+", "_", Path(rel).with_suffix("").as_posix()).strip("_").lower()
        record = {
            "id": resource_id,
            "file": rel,
            "type": typ,
            "tags": list(dict.fromkeys(tags)),
            "triggers": list(dict.fromkeys(str(x) for x in triggers if str(x).strip())),
            "status": "alias" if is_alias else ("retained_source" if prior_status == "retained_source" else "canonical"),
            "alias_of": alias_target if is_alias else None,
            "load_policy": "redirect_to_canonical_no_duplicate_load" if is_alias else prior.get("load_policy", "route_by_task"),
            "sha256": sha256(path),
            "headings": headings,
            "route_policy": "alias_redirect_to_canonical_with_explicit_alias_access" if is_alias else prior.get("route_policy", "explicit_path_or_specific_trigger_then_primary_capability"),
            "primary_capability": primary,
        }
        if is_alias:
            record["source_content_sha256"] = (alias_meta or {}).get("original_sha256") or prior.get("source_content_sha256") or prior.get("sha256", "")
        resources.append(record)

    # Build exact-content alias groups over Markdown knowledge/reference files only. Source files remain present.
    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    path_to_resource = {r["file"]: r for r in resources}
    for r in resources:
        if Path(r["file"]).suffix.lower() in {".md", ".markdown"} and r.get("status") != "alias":
            by_hash[r["sha256"]].append(r)
    for group in by_hash.values():
        if len(group) < 2:
            continue
        # Retain the previous canonical when it is still part of the exact-hash group; otherwise prefer a clear non-versioned name.
        old_canonicals = [r for r in group if old_by_actual.get(r["file"], {}).get("status") == "canonical"]
        candidates = old_canonicals or group
        canonical = min(candidates, key=lambda r: (
            bool(re.match(r"references/(p1-|v\d|old-|archive-)", r["file"], re.I)),
            len(r["file"]), r["file"]
        ))
        canonical["status"] = "canonical"
        canonical["alias_of"] = None
        for r in group:
            if r is canonical:
                continue
            r["status"] = "alias"
            r["alias_of"] = canonical["file"]
            r["load_policy"] = "redirect_to_canonical_no_duplicate_load"

    # Original source extracts remain directly addressable, but not loaded by default in ordinary requests.
    for r in resources:
        if r["status"] == "retained_source":
            r["load_policy"] = "deep_audit_or_explicit_source_request"
        if r["status"] == "alias":
            r["load_policy"] = "redirect_to_canonical_no_duplicate_load"

    old["schema_version"] = "6"
    old["skill"] = {
        "name": "qhsj-aigc-film",
        "display_name": DISPLAY_NAME,
        "version": VERSION,
        "language_policy": "中文为主，必要术语附英文",
        "routing_mode": "semantic-first multi-label dependency-aware routing with explicit negative constraints, primary intent dispatch, full resource graph, asset-lock gates, and auditable review contracts",
        "license": "MIT",
        "brand": "QHSJ",
    }
    old["routing_contract"] = {
        "all_user_requests_must_route": True,
        "sequence": [
            "preserve_raw_request_and_extract_hard_constraints",
            "direct_capability_detection_using_capability_triggers_and_semantic_cues",
            "apply_explicit_negative_constraints_before_dependency_closure",
            "recursive_dependency_closure_without_macro_workflow_overdispatch",
            "workflow_selection_from_direct_intent_and_explicit_workflow_triggers",
            "reference_resource_ranking_with_primary_capability_evidence",
            "asset_specification_then_asset_image_generation_then_QA_lock",
            "spatial_state_and_gaze_distance_ledger",
            "storyboard_asset_generation_only_after_locked_asset_refs_exist",
            "quality_red_team_and_regression",
            "manifest_and_route_graph_validation",
        ],
        "parallel_rules": "Parallelize independent requirements review, reference classification, and read-only code checks. Serialize any dependency-sensitive writes: registry before graph, locked character/scene assets before storyboard assets, edits before regression tests, and any conflicting merge behind the orchestrator.",
        "alias_policy": "Keep every historical source path addressable. Exact byte-identical Markdown knowledge bodies are stored once; legacy paths become small compatibility stubs with original SHA-256 provenance, route to the canonical body, and inherit all canonical section routes.",
        "uncertainty_policy": "Route deterministic direct evidence, present unresolved ambiguity to the host model, and never claim exact natural-language semantic coverage without tests. Mark unavailable references or external tool executions as unverified.",
        "priority": "safety_and_policy > explicit_user_constraints > source_facts_and_canon > causality_spatial_action_physics > output_and_platform_contract > task_domain > aesthetics > optional_decoration",
        "asset_lock_gate": "Character and scene canonical assets must be specified, generated/received, validated, versioned and locked (or marked provisional) before generating any per-shot storyboard asset. Shot-level outputs must reference the locked asset IDs and versions.",
        "agent_review_contract": "Define independent review roles and findings contracts. A runtime must only claim genuine multi-agent execution if the host actually started separate agents; sequential role simulation must be labelled as such.",
    }
    old["capabilities"] = caps
    old["resources"] = resources
    # Recompute aggregate metadata.
    old["statistics"] = {
        "resource_count": len(resources),
        "reference_markdown_count": sum(1 for r in resources if r["file"].startswith("references/") and r["file"].endswith(".md")),
        "section_heading_count": sum(len(r.get("headings", [])) for r in resources),
        "exact_duplicate_alias_count": sum(1 for r in resources if r.get("status") == "alias"),
        "workflow_count": len(old["workflows"]),
        "capability_count": len(caps),
        "manifest_excluded_files": sorted(META_FILES),
    }
    # Stable ordering makes diffs reviewable and avoids silent churn.
    old["capabilities"] = sorted(old["capabilities"], key=lambda c: c["id"])
    old["workflows"] = sorted(old["workflows"], key=lambda w: (w.get("id") != "intent-analysis", -int(w.get("priority", 0)), w.get("id", "")))
    old["resources"] = sorted(resources, key=lambda r: r["file"])
    return old, files


def build_graph(registry: dict[str, Any], files: dict[str, Path]) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, str]] = []
    node_ids: set[str] = set()
    edge_keys: set[tuple[str, str, str]] = set()

    def add_node(node_id: str, typ: str, name: str = ""):
        if node_id in node_ids:
            return
        node_ids.add(node_id)
        n = {"id": node_id, "type": typ}
        if name:
            n["name"] = name
        nodes.append(n)

    def add_edge(source: str, relation: str, target: str):
        key = (source, relation, target)
        if source not in node_ids or target not in node_ids or key in edge_keys:
            return
        edge_keys.add(key)
        edges.append({"from": source, "relation": relation, "to": target})

    cap_by_id = {c["id"]: c for c in registry["capabilities"]}
    wf_by_id = {w["id"]: w for w in registry["workflows"]}
    res_by_path = {r["file"]: r for r in registry["resources"]}
    for c in registry["capabilities"]:
        add_node("capability:" + c["id"], "capability", c.get("name", c["id"]))
    for w in registry["workflows"]:
        add_node("workflow:" + w["id"], "workflow", w.get("name", w["id"]))
    for r in registry["resources"]:
        add_node("resource:" + r["file"], "resource", r["file"])
        for h in r.get("headings", []):
            add_node(f"section:{r['file']}#{h.get('anchor', '')}", "section", h.get("heading", ""))

    # Capabilities close over dependencies, route to resources, and point to macro workflows.
    for c in registry["capabilities"]:
        cid = c["id"]
        for dep in c.get("dependencies", []):
            add_edge("capability:" + cid, "depends_on", "capability:" + dep)
        for wid in c.get("workflow_routes", {}).get("auto", []):
            add_edge("capability:" + cid, "routes_auto_to", "workflow:" + wid)
        for wid in c.get("workflow_routes", {}).get("conditional", []):
            add_edge("capability:" + cid, "routes_conditional_to", "workflow:" + wid)
    for r in registry["resources"]:
        rid = "resource:" + r["file"]
        for tag in r.get("tags", []):
            add_edge("capability:" + tag, "routes_to_resource", rid)
        for h in r.get("headings", []):
            add_edge(rid, "contains_section", f"section:{r['file']}#{h.get('anchor', '')}")
        if r.get("alias_of"):
            add_edge(rid, "aliases_to", "resource:" + r["alias_of"])

    # Workflow -> capabilities/resources/stages creates inspectable end-to-end connections.
    for wid, w in wf_by_id.items():
        wn = "workflow:" + wid
        for cid in w.get("capabilities", w.get("routed_capabilities", [])):
            if cid in cap_by_id:
                add_edge(wn, "uses_capability", "capability:" + cid)
        wf_path = ROOT / w.get("file", "")
        if not wf_path.is_file():
            continue
        try:
            data = yaml.safe_load(wf_path.read_text(encoding="utf-8")) or {}
        except Exception:
            data = {}
        if not isinstance(data, dict):
            continue
        module_count = 0
        stage_count = 0
        def walk_modules(value: Any, stage_node: str | None = None):
            nonlocal module_count
            if isinstance(value, dict):
                if isinstance(value.get("modules"), list):
                    for m in value["modules"]:
                        if isinstance(m, str) and m in res_by_path:
                            add_edge(wn if stage_node is None else stage_node, "loads_resource", "resource:" + m)
                            module_count += 1
                for key, child in value.items():
                    if key == "modules":
                        continue
                    walk_modules(child, stage_node)
            elif isinstance(value, list):
                for child in value:
                    walk_modules(child, stage_node)
        stages = data.get("stages", [])
        if isinstance(stages, list):
            prev_stage: str | None = None
            for ix, stage in enumerate(stages):
                if not isinstance(stage, dict):
                    continue
                sid = str(stage.get("id", f"S{ix}"))
                node_id = f"stage:{wid}#{sid}"
                add_node(node_id, "stage", str(stage.get("name", sid)))
                add_edge(wn, "contains_stage", node_id)
                if prev_stage:
                    add_edge(prev_stage, "precedes", node_id)
                else:
                    add_edge(wn, "starts_with_stage", node_id)
                prev_stage = node_id
                stage_count += 1
                for mod in stage.get("modules", []):
                    if isinstance(mod, str) and mod in res_by_path:
                        add_edge(node_id, "loads_resource", "resource:" + mod)
                        module_count += 1
        # For workflows without stage lists, still expose modules anywhere in the definition.
        if stage_count == 0:
            walk_modules(data)
        if wid == "intent-analysis":
            for other in wf_by_id:
                if other != wid:
                    add_edge(wn, "precedes_all_workflows", "workflow:" + other)

    nodes.sort(key=lambda n: (n["type"], n["id"], n.get("name", "")))
    edges.sort(key=lambda e: (e["from"], e["relation"], e["to"]))
    adjacency: dict[str, list[dict[str, str]]] = defaultdict(list)
    for e in edges:
        adjacency[e["from"]].append({"relation": e["relation"], "to": e["to"]})
    graph = {
        "schema_version": "3",
        "skill": "qhsj-aigc-film",
        "display_name": DISPLAY_NAME,
        "skill_version": VERSION,
        "description": "QHSJ AIGC 全能影视全路由依赖图，连接能力、工作流、阶段、资源和章节。",
        "policy": {
            "preserve_all_resources": True,
            "all_requests_enter_intent_analysis": True,
            "dependency_closure": True,
            "resource_read_budget_does_not_remove_routes": True,
            "asset_lock_before_storyboard_assets": True,
            "aliases_keep_source_and_redirect_reads": True,
        },
        "coverage": {
            "capabilities": len(registry["capabilities"]),
            "workflows": len(registry["workflows"]),
            "resources": len(registry["resources"]),
            "sections": sum(1 for n in nodes if n["type"] == "section"),
            "stages": sum(1 for n in nodes if n["type"] == "stage"),
            "edges": len(edges),
            "capabilities_with_auto_workflow": sum(1 for c in registry["capabilities"] if c.get("workflow_routes", {}).get("auto")),
            "resources_with_capability_tags": sum(1 for r in registry["resources"] if r.get("tags")),
            "workflows_with_resource_or_capability_edges": sum(1 for w in registry["workflows"] if any(e["from"] == "workflow:" + w["id"] for e in edges)),
        },
        "nodes": nodes,
        "edges": edges,
        "adjacency": dict(sorted(adjacency.items())),
    }
    return graph


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_manifest(registry: dict[str, Any], files: dict[str, Path]) -> dict[str, Any]:
    current = list_files()
    inventory = []
    for rel, path in sorted(current.items()):
        if rel == "MANIFEST.json":
            continue
        inventory.append({
            "path": rel,
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
            "category": infer_type(rel),
        })
    return {
        "manifest_version": "3",
        "skill": "qhsj-aigc-film",
        "display_name": DISPLAY_NAME,
        "version": VERSION,
        "license": "MIT",
        "generated_by": "scripts/rebuild_routing_assets.py",
        "manifest_excludes_self": True,
        "routing_coverage": {
            "capabilities": len(registry["capabilities"]),
            "workflows": len(registry["workflows"]),
            "resources": len(registry["resources"]),
            "reference_markdown_files": registry["statistics"]["reference_markdown_count"],
            "reference_section_headings": registry["statistics"]["section_heading_count"],
            "exact_duplicate_aliases": registry["statistics"]["exact_duplicate_alias_count"],
        },
        "inventory_count": len(inventory),
        "files": inventory,
    }


def main() -> int:
    try:
        prior_registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except Exception:
        prior_registry = {"resources": []}
    dedupe_report = dedupe_exact_reference_bodies(ROOT, prior_registry)
    registry, files = build_registry()
    write_json(REGISTRY_PATH, registry)
    # The graph does not embed file hashes, so its hash can be refreshed into the registry
    # after graph generation without a circular dependency.
    files = list_files()
    graph = build_graph(registry, files)
    write_json(GRAPH_PATH, graph)
    graph_resource = next((r for r in registry["resources"] if r["file"] == "routing/route-graph.json"), None)
    if graph_resource:
        graph_resource["sha256"] = sha256(GRAPH_PATH)
    write_json(REGISTRY_PATH, registry)
    files = list_files()
    manifest = build_manifest(registry, files)
    write_json(MANIFEST_PATH, manifest)
    print(json.dumps({
        "status": "rebuilt",
        "skill": DISPLAY_NAME,
        "version": VERSION,
        "resources": len(registry["resources"]),
        "capabilities": len(registry["capabilities"]),
        "workflows": len(registry["workflows"]),
        "reference_headings": registry["statistics"]["section_heading_count"],
        "aliases": registry["statistics"]["exact_duplicate_alias_count"],
        "collapsed_this_run": len(dedupe_report.get("collapsed", [])),
        "graph_nodes": len(graph["nodes"]),
        "graph_edges": len(graph["edges"]),
        "manifest_files": manifest["inventory_count"],
    }, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
