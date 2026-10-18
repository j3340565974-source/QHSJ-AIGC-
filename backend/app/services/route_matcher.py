"""Route matching logic — single source of truth.
Pure Python, stdlib only, no fastapi import.
Implements docs/routing.md algorithm."""
import json
import os
import difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # backend/app/services -> repo root
ROUTES_PATH = ROOT / "routes.json"


def load_routes():
    with open(ROUTES_PATH, encoding="utf-8") as f:
        return json.load(f)


def match_route(query, routes=None):
    """Match a query against routes.
    Returns dict with matched info or NO_ROUTE_MATCHED / ROUTE_CONFLICT."""
    if routes is None:
        routes = load_routes()

    query_lower = query.lower()
    scored = []
    for r in routes:
        if r.get("deprecated"):
            continue
        triggers = r.get("triggers", [])
        score = sum(1 for t in triggers if t.lower() in query_lower)
        if score > 0:
            scored.append((score, r))

    if not scored:
        # No match — return top 3 candidates by difflib similarity
        candidates = []
        for r in routes:
            if r.get("deprecated"):
                continue
            all_text = " ".join(r.get("triggers", [])) + " " + r["id"]
            sim = difflib.SequenceMatcher(None, query_lower, all_text.lower()).ratio()
            candidates.append((sim, r))
        candidates.sort(key=lambda x: -x[0])
        top3 = [
            {"id": c[1]["id"], "gate_level": c[1]["gate_level"], "score": round(c[0], 3)}
            for c in candidates[:3]
        ]
        return {
            "matched": False,
            "error_code": "NO_ROUTE_MATCHED",
            "candidates": top3,
        }

    # Sort by score desc, then priority desc
    scored.sort(key=lambda x: (-x[0], -x[1].get("priority", 100)))
    top_score = scored[0][0]
    top_priority = scored[0][1].get("priority", 100)
    tied = [s for s in scored if s[0] == top_score and s[1].get("priority", 100) == top_priority]

    if len(tied) > 1:
        return {
            "matched": False,
            "error_code": "ROUTE_CONFLICT",
            "candidates": [
                {"id": s[1]["id"], "gate_level": s[1]["gate_level"], "score": s[0]}
                for s in tied
            ],
        }

    best = scored[0][1]
    return {
        "matched": True,
        "route_id": best["id"],
        "gate_level": best["gate_level"],
        "blocks_on_failure": best.get("blocks_on_failure", False),
        "matched_triggers": [t for t in best.get("triggers", []) if t.lower() in query_lower],
        "score": top_score,
    }
