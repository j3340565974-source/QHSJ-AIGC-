"""QHSJ-AIGC Skill Backend — FastAPI app.

Endpoints:
  GET  /health    — liveness + version
  POST /route     — match a user query to a route (single source of truth)
  GET  /manifest  — return manifest.json
"""
from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .services.route_matcher import match_route

ROOT = Path(__file__).resolve().parents[2]  # backend/app -> repo root
MANIFEST_PATH = ROOT / "manifest.json"

app = FastAPI(
    title="QHSJ-AIGC Skill API",
    version="8.0.0",
    description="Route matching & manifest service for the QHSJ-AIGC skill.",
)


class RouteRequest(BaseModel):
    query: str


@app.get("/health")
def health() -> dict:
    manifest = _load_manifest()
    return {
        "status": "ok",
        "name": manifest["name"],
        "version": manifest["version"],
        "declared_counts": manifest["declared_counts"],
    }


@app.post("/route")
def route(req: RouteRequest) -> dict:
    if not req.query or not req.query.strip():
        raise HTTPException(status_code=400, detail="query must be non-empty")
    return match_route(req.query)


@app.get("/manifest")
def manifest() -> dict:
    return _load_manifest()


def _load_manifest() -> dict:
    try:
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="manifest.json not found")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"manifest.json invalid: {e}")
