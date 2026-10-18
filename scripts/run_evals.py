#!/usr/bin/env python3
"""run_evals.py — run golden + corpus evals against route_matcher.

Two suites:
  * evals/golden/*.json          — single-assertion cases (expected_route/gate/blocks).
  * evals/routing-cases.json     — 139-case corpus with must_/exclude capability
                                   and workflow assertions.

Exit 0 = all pass, 1 = any failure.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend" / "app" / "services"))
from route_matcher import load_workflows, match_route  # noqa: E402

GOLDEN_DIR = ROOT / "evals" / "golden"
CORPUS_PATH = ROOT / "evals" / "routing-cases.json"

passed = 0
failed = 0


def _fail(label: str, msg: str) -> None:
    global failed
    failed += 1
    print(f"FAIL {label}: {msg}")


def _pass() -> None:
    global passed
    passed += 1


def run_golden() -> None:
    routes = load_workflows()
    route_ids = set(routes)
    for case_file in sorted(GOLDEN_DIR.glob("*.json")):
        case = json.loads(case_file.read_text(encoding="utf-8"))
        label = f"golden/{case_file.name}"
        result = match_route(case["query"])
        if case.get("expected_route"):
            if not result.get("matched") or result.get("route_id") != case["expected_route"]:
                _fail(label, f"expected route={case['expected_route']}, got={result.get('route_id')}")
                continue
        if "expected_gate_level" in case and result.get("gate_level") != case["expected_gate_level"]:
            _fail(label, f"expected gate={case['expected_gate_level']}, got={result.get('gate_level')}")
            continue
        if "expected_blocks" in case and result.get("blocks_on_failure") != case["expected_blocks"]:
            _fail(label, f"expected blocks={case['expected_blocks']}, got={result.get('blocks_on_failure')}")
            continue
        if case.get("expected_route") and case["expected_route"] not in route_ids:
            _fail(label, f"expected_route {case['expected_route']} not in routes.json")
            continue
        _pass()


def run_corpus() -> None:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    for case in corpus["cases"]:
        label = f"corpus/{case['id']}"
        result = match_route(case["request"])
        got_caps = set(result.get("capabilities", []))
        got_wfs = set(result.get("workflows", []))
        problems = []
        if not result.get("matched"):
            problems.append("not matched")
        for c in case.get("must_include_capabilities", []):
            if c not in got_caps:
                problems.append(f"missing capability {c}")
        for w in case.get("must_include_workflows", []):
            if w not in got_wfs:
                problems.append(f"missing workflow {w}")
        for c in case.get("must_exclude_capabilities", []):
            if c in got_caps:
                problems.append(f"unexpected capability {c}")
        for w in case.get("must_exclude_workflows", []):
            if w in got_wfs:
                problems.append(f"unexpected workflow {w}")
        if problems:
            _fail(label, "; ".join(problems) + f" | req={case['request']!r} caps={sorted(got_caps)} wfs={sorted(got_wfs)}")
        else:
            _pass()


def main() -> int:
    run_golden()
    run_corpus()
    total = passed + failed
    if failed:
        print(f"\nFAILED: {failed}/{total} cases failed ({passed} passed)")
        return 1
    print(f"PASS: {total}/{total} eval cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
