#!/usr/bin/env python3
"""build_routes.py — 非破坏性同步 routes.json 与 workflows/*/WORKFLOW.md。

routes.json 是人工精心维护的权威路由表（triggers / priority / gate_level /
capability_dependencies / always_run 等）。本脚本只做“同步”，绝不覆盖已有字段：

- 为新增的 workflows/<id>/WORKFLOW.md 生成一条骨架路由（触发器为空并告警）。
- 删除 workflow 文件已不存在的路由。
- 对已存在的路由**原样保留**，不重写 triggers/priority/gate_level/dependencies。
- 修正 workflow 路径字段，使其指向实际文件。

运行：python3 scripts/build_routes.py [--check]
  --check  只报告差异，不写回文件；有差异时退出码为 1。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / "workflows"
ROUTES_OUT = ROOT / "routes.json"

SKELETON = {
    "triggers": [],
    "capabilities": [],
    "capability_dependencies": {},
    "gate_level": "P1",
    "blocks_on_failure": False,
    "priority": 100,
    "deprecated": False,
}


def discover_workflows() -> dict[str, str]:
    """route id -> relative WORKFLOW.md path."""
    found: dict[str, str] = {}
    if not WORKFLOWS.is_dir():
        return found
    for wf_dir in sorted(WORKFLOWS.iterdir()):
        if not wf_dir.is_dir():
            continue
        rel = f"workflows/{wf_dir.name}/WORKFLOW.md"
        if (ROOT / rel).is_file():
            found[wf_dir.name] = rel
    return found


def load_routes() -> list[dict]:
    if ROUTES_OUT.is_file():
        return json.loads(ROUTES_OUT.read_text(encoding="utf-8"))
    return []


def sync(existing: list[dict], workflows: dict[str, str]) -> tuple[list[dict], list[str]]:
    notes: list[str] = []
    by_id = {r["id"]: r for r in existing}

    # Drop routes whose workflow file no longer exists.
    for rid in [r["id"] for r in existing if r["id"] not in workflows]:
        notes.append(f"删除已不存在工作流的路由：{rid}")
        del by_id[rid]

    merged: list[dict] = []
    for rid, rel in workflows.items():
        if rid in by_id:
            route = by_id[rid]
            if route.get("workflow") != rel:
                notes.append(f"修正路由 {rid} 的 workflow 路径：{route.get('workflow')} -> {rel}")
                route["workflow"] = rel
        else:
            route = {"id": rid, "workflow": rel, **SKELETON}
            notes.append(f"新增骨架路由：{rid}（triggers 为空，需人工补全）")
        merged.append(route)

    merged.sort(key=lambda r: r["id"])
    return merged, notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只检查差异，不写回")
    args = parser.parse_args()

    workflows = discover_workflows()
    existing = load_routes()
    merged, notes = sync(existing, workflows)
    changed = json.dumps(existing, ensure_ascii=False, sort_keys=True) != json.dumps(merged, ensure_ascii=False, sort_keys=True)

    for n in notes:
        print(n)

    empty = [r["id"] for r in merged if not r.get("triggers")]
    if empty:
        print(f"WARNING: {len(empty)} 条路由 triggers 为空（不会被匹配），需人工补全：{empty}")

    if args.check:
        if changed:
            print("DRIFT: routes.json 与 workflows/ 不同步")
            return 1
        print("OK: routes.json 与 workflows/ 同步")
        return 0

    if changed:
        ROUTES_OUT.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"已同步 {len(merged)} 条路由 -> {ROUTES_OUT}")
    else:
        print(f"无需变更，{len(merged)} 条路由已同步")
    return 0


if __name__ == "__main__":
    sys.exit(main())
