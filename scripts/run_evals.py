#!/usr/bin/env python3
"""run_evals.py — run golden eval cases against route_matcher."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend" / "app" / "services"))
from route_matcher import load_routes, match_route

GOLDEN_DIR = ROOT / "evals" / "golden"
routes = load_routes()
route_ids = {r["id"] for r in routes}

failures = 0
total = 0
for case_file in sorted(GOLDEN_DIR.glob("*.json")):
    case = json.loads(case_file.read_text(encoding="utf-8"))
    total += 1
    query = case["query"]
    result = match_route(query, routes)

    if case.get("expected_route"):
        if not result.get("matched") or result.get("route_id") != case["expected_route"]:
            print(f"FAIL {case_file.name}: expected route={case['expected_route']}, got={result}")
            failures += 1
            continue
    if "expected_gate_level" in case:
        if result.get("gate_level") != case["expected_gate_level"]:
            print(f"FAIL {case_file.name}: expected gate={case['expected_gate_level']}, got={result.get('gate_level')}")
            failures += 1
            continue
    if "expected_blocks" in case:
        if result.get("blocks_on_failure") != case["expected_blocks"]:
            print(f"FAIL {case_file.name}: expected blocks={case['expected_blocks']}, got={result.get('blocks_on_failure')}")
            failures += 1
            continue
    # Check expected_route exists in routes
    if case.get("expected_route") and case["expected_route"] not in route_ids:
        print(f"FAIL {case_file.name}: expected_route {case['expected_route']} not in routes.json")
        failures += 1

if failures:
    print(f"\nFAILED: {failures}/{total} cases failed")
    sys.exit(1)
else:
    print(f"PASS: {total}/{total} golden cases passed")
    sys.exit(0)
