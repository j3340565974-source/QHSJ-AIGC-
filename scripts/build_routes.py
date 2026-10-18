#!/usr/bin/env python3
"""Build routes.json by scanning workflows/*/WORKFLOW.md.
Generates route skeletons; humans fill triggers/gate_level/priority."""
import os, re, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / "workflows"
ROUTES_OUT = ROOT / "routes.json"

def read_workflow(path):
    return path.read_text(encoding="utf-8")

def extract_triggers(text):
    m = re.search(r'## 触发条件\s*\n((?:- .*\n)+)', text)
    if m:
        return [l.strip('- ').strip() for l in m.group(1).strip().split('\n') if l.strip()]
    return []

def extract_capabilities(text):
    """Extract capabilities/xxx/SPEC.md references."""
    caps = set(re.findall(r'capabilities/[a-z0-9-]+/SPEC\.md', text))
    return sorted(caps)

def extract_gate_level(text):
    """Default P1; if mentions 资产锁定/Asset-First as hard gate, P0."""
    if re.search(r'(资产锁定|Asset-First).{0,20}(硬门禁|P0|不可跳过|不可绕过)', text):
        return "P0"
    if re.search(r'P0', text):
        return "P0"
    return "P1"

def main():
    routes = []
    for wf_dir in sorted(WORKFLOWS.iterdir()):
        if not wf_dir.is_dir():
            continue
        wf_md = wf_dir / "WORKFLOW.md"
        if not wf_md.exists():
            continue
        text = read_workflow(wf_md)
        route_id = wf_dir.name
        triggers = extract_triggers(text)
        caps = extract_capabilities(text)
        gate_level = extract_gate_level(text)
        blocks = gate_level == "P0"
        route = {
            "id": route_id,
            "triggers": triggers,
            "workflow": f"workflows/{route_id}/WORKFLOW.md",
            "capabilities": caps,
            "capability_dependencies": {},
            "gate_level": gate_level,
            "blocks_on_failure": blocks,
            "priority": 100,
            "deprecated": False
        }
        routes.append(route)

    with open(ROUTES_OUT, "w", encoding="utf-8") as f:
        json.dump(routes, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(routes)} routes -> {ROUTES_OUT}")
    empty = [r["id"] for r in routes if not r["triggers"]]
    if empty:
        print(f"WARNING: {len(empty)} routes with empty triggers (won't match): {empty}")
    print("请人工审核 triggers / gate_level / priority；空 triggers 的 route 不会被匹配，需补全")

if __name__ == "__main__":
    main()
