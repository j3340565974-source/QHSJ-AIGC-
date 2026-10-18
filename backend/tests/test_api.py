"""Tests for backend FastAPI endpoints."""
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["name"] == "qhsj-aigc"
    assert body["version"] == "7.0.0"
    assert body["declared_counts"]["capabilities"] == 29
    assert body["declared_counts"]["workflows"] == 16
    assert body["declared_counts"]["references"] == 684


def test_manifest():
    resp = client.get("/manifest")
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "qhsj-aigc"
    assert body["version"] == "7.0.0"
    assert "declared_counts" in body


def test_route_match_asset_lock():
    resp = client.post("/route", json={"query": "帮我做角色资产锁定"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["matched"] is True
    assert body["route_id"] == "asset-lock"
    assert body["gate_level"] == "P0"


def test_route_match_storyboard():
    resp = client.post("/route", json={"query": "我需要分镜表和镜头表"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["matched"] is True
    assert body["route_id"] == "storyboard-only"


def test_route_no_match():
    resp = client.post("/route", json={"query": "今天天气怎么样"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["matched"] is False
    assert body["error_code"] == "NO_ROUTE_MATCHED"
    assert "candidates" in body
    assert len(body["candidates"]) <= 3


def test_route_empty_query():
    resp = client.post("/route", json={"query": ""})
    assert resp.status_code == 400


def test_route_missing_query():
    resp = client.post("/route", json={})
    assert resp.status_code == 422
