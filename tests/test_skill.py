"""QHSJ-AIGC v7 契约与路由回归测试。

覆盖：
- 包结构一致性（counts / 版本 / 索引 / schema）
- 路由匹配单一实现 `route_matcher.match_route`（多任务叠加、模糊意图 fallback、未命中候选）
- 子句级否定隔离
- 每条能力/工作流都存在可命中的真实触发入口
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.app.services.route_matcher import (  # noqa: E402
    load_capabilities,
    load_workflows,
    match_route,
    normalize,
    phrase_is_negated,
)


def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class PackageStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read_json("manifest.json")
        cls.routes = read_json("routes.json")
        cls.cap_meta = read_json("capability-routes.json")["capabilities"]
        cls.skill_fm = yaml.safe_load(read_text("SKILL.md").split("---")[1])

    def test_declared_counts_match_actual(self):
        declared = self.manifest["declared_counts"]
        cap_dirs = [d for d in (ROOT / "capabilities").iterdir() if d.is_dir()]
        wf_dirs = [d for d in (ROOT / "workflows").iterdir() if d.is_dir()]
        ref_mds = [
            r for r in (ROOT / "references").rglob("*.md")
            if "_unsorted" not in str(r) and not (r.name == "index.md" and r.parent != ROOT / "references")
        ]
        self.assertEqual(len(cap_dirs), declared["capabilities"])
        self.assertEqual(len(wf_dirs), declared["workflows"])
        self.assertEqual(len(ref_mds), declared["references"])

    def test_version_consistent_across_manifest_and_skill(self):
        self.assertEqual(self.manifest["version"], self.skill_fm["metadata"]["version"])
        self.assertEqual(self.manifest["name"], self.skill_fm["name"])

    def test_routes_reference_existing_workflow_and_capability_files(self):
        for r in self.routes:
            self.assertTrue((ROOT / r["workflow"]).is_file(), r["id"])
            for c in r["capabilities"]:
                self.assertTrue((ROOT / c).is_file(), f"{r['id']} -> {c}")

    def test_each_route_matches_route_schema(self):
        import jsonschema

        schema = read_json("schemas/route.schema.json")
        for r in self.routes:
            jsonschema.validate(r, schema)

    def test_no_orphan_capabilities_or_workflows(self):
        referenced_caps = {c for r in self.routes for c in r["capabilities"]}
        referenced_wfs = {r["workflow"] for r in self.routes}
        for d in (ROOT / "capabilities").iterdir():
            if d.is_dir():
                self.assertIn(f"capabilities/{d.name}/SPEC.md", referenced_caps, d.name)
        for d in (ROOT / "workflows").iterdir():
            if d.is_dir():
                self.assertIn(f"workflows/{d.name}/WORKFLOW.md", referenced_wfs, d.name)

    def test_capability_trio_present(self):
        for d in (ROOT / "capabilities").iterdir():
            if not d.is_dir():
                continue
            for f in ("SPEC.md", "inputs.schema.json", "outputs.schema.json"):
                self.assertTrue((d / f).is_file(), f"{d.name}/{f}")

    def test_capability_meta_and_spec_ids_align(self):
        spec_ids = set(load_capabilities())
        self.assertEqual(spec_ids, set(self.cap_meta), "capability-routes.json 与 SPEC.md 能力 ID 不一致")

    def test_indexes_exist(self):
        for rel in ("capabilities/index.md", "workflows/index.md", "references/index.md"):
            self.assertTrue((ROOT / rel).is_file(), rel)
        for d in (ROOT / "references").iterdir():
            if d.is_dir() and not d.name.startswith("_"):
                self.assertTrue((d / "index.md").is_file(), f"references/{d.name}/index.md")


class MatcherContractTests(unittest.TestCase):
    def caps(self, query):
        return set(match_route(query)["capabilities"])

    def wfs(self, query):
        return set(match_route(query)["workflows"])

    def test_intent_analysis_always_scheduled(self):
        self.assertIn("intent-analysis", self.wfs("请把内容做得更有感染力"))

    def test_multi_task_overlay_returns_all_routes(self):
        result = match_route("从创意到成片，写剧本、分镜、角色资产、图片提示词、视频提示词、声音设计、Seedance适配、API集成和全量质量审查")
        self.assertTrue(result["multi_task"])
        self.assertGreater(len(result["routes"]), 5)
        self.assertEqual({r["id"] for r in result["routes"]}, set(result["workflows"]))

    def test_compound_script_storyboard_video_prompt(self):
        caps, wfs = self.caps("把这段剧本拆成逐镜分镜表，并给每镜生成视频提示词"), self.wfs("把这段剧本拆成逐镜分镜表，并给每镜生成视频提示词")
        self.assertTrue({"screenwriting", "storyboard", "video_prompt", "prompt_engineering"}.issubset(caps))
        self.assertTrue({"script-to-screen", "visual-prompt"}.issubset(wfs))

    def test_vague_colloquial_intent_falls_back_to_intent_analysis(self):
        result = match_route("帮我把这段内容弄得更专业更有感染力")
        self.assertTrue(result["matched"])
        self.assertTrue({"intent-analysis"} <= set(result["workflows"]))
        self.assertIn("general_orchestration", result["capabilities"])

    def test_unrelated_request_returns_no_match_with_candidates(self):
        result = match_route("今天天气怎么样")
        self.assertFalse(result["matched"])
        self.assertEqual(result["error_code"], "NO_ROUTE_MATCHED")
        self.assertLessEqual(len(result["candidates"]), 3)

    def test_asset_lock_is_p0_and_blocks(self):
        result = match_route("帮我做角色资产锁定")
        self.assertEqual(result["route_id"], "asset-lock")
        self.assertEqual(result["gate_level"], "P0")
        self.assertTrue(result["blocks_on_failure"])

    def test_primary_route_prefers_explicit_trigger_over_capability_autoroute(self):
        result = match_route("帮我做角色资产锁定和场景资产锁定")
        self.assertEqual(result["route_id"], "asset-lock")

    def test_static_image_prompt_does_not_overroute_video(self):
        caps, wfs = self.caps("给我一段图片提示词，做成冷艳赛博朋克女性机械人"), self.wfs("给我一段图片提示词，做成冷艳赛博朋克女性机械人")
        self.assertIn("image_prompt", caps)
        self.assertIn("visual-prompt", wfs)
        self.assertTrue({"video_prompt", "model_adaptation", "reverse_engineering"}.isdisjoint(caps))
        self.assertNotIn("storyboard-only", wfs)

    def test_audio_only_with_negations_suppresses_visual_deliverables(self):
        result = match_route("只设计音效，不需要分镜或视频提示词，也不要图片提示词")
        caps, wfs, c = set(result["capabilities"]), set(result["workflows"]), result["constraints"]
        self.assertIn("audio_design", caps)
        self.assertTrue({"storyboard", "video_prompt", "image_prompt", "prompt_engineering"}.isdisjoint(caps))
        self.assertNotIn("visual-prompt", wfs)
        self.assertTrue(c["explicit_no_prompt"])

    def test_short_video_prompt_does_not_dispatch_social_pipeline(self):
        result = match_route("不要全流程，只给我一个短视频提示词")
        self.assertIn("video_prompt", result["capabilities"])
        self.assertIn("visual-prompt", result["workflows"])
        self.assertNotIn("short_video_content", result["capabilities"])
        self.assertNotIn("platform-short-video", result["workflows"])

    def test_consistency_defect_wording_is_not_asset_locking(self):
        caps = self.caps("修复分镜里人物位置不一致")
        self.assertIn("spatial_continuity", caps)
        self.assertNotIn("asset_locking", caps)

    def test_explicit_negated_asset_images_do_not_activate_asset_pipeline(self):
        result = match_route("不要人物图和场景图，只要文字分镜，不要提示词")
        caps, wfs = set(result["capabilities"]), set(result["workflows"])
        self.assertIn("storyboard", caps)
        self.assertTrue({"asset_first", "asset_locking", "character_design", "image_prompt", "video_prompt", "prompt_engineering"}.isdisjoint(caps))
        self.assertNotIn("asset-first", wfs)
        self.assertNotIn("asset-lock", wfs)
        self.assertNotIn("visual-prompt", wfs)

    def test_local_negation_does_not_fabricate_excluded_capability(self):
        cases = [
            ("做个视频，不要音效", "audio_design"),
            ("不要运镜", "cinematography"),
            ("不要打斗", "action_choreography"),
            ("不要爆炸特效", "vfx_physics"),
            ("别做分镜", "storyboard"),
            ("不生成图片", "image_prompt"),
            ("没有运镜要求", "cinematography"),
            ("把运镜去掉", "cinematography"),
        ]
        for request, excluded in cases:
            self.assertNotIn(excluded, self.caps(request), f"否定泄露：{request}")

    def test_clause_scoped_negation_keeps_later_positive_deliverable(self):
        self.assertIn("video_prompt", self.caps("不要运镜，就要个静态视频提示词"))
        self.assertIn("visual-prompt", self.wfs("不要运镜，就要个静态视频提示词"))


class NegationUnitTests(unittest.TestCase):
    def test_phrase_is_negated_scope(self):
        self.assertTrue(phrase_is_negated("不要音效", "音效"))
        self.assertTrue(phrase_is_negated("不生成图片", "生成图片"))
        self.assertTrue(phrase_is_negated("别做分镜", "分镜"))
        self.assertTrue(phrase_is_negated("不要分镜，只生成图片提示词", "分镜"))
        self.assertFalse(phrase_is_negated("要音效，不要分镜", "音效"))
        self.assertFalse(phrase_is_negated("只要图片", "图片"))

    def test_postfix_removal_and_none_requirement(self):
        self.assertTrue(phrase_is_negated("没有运镜要求", "运镜"))
        self.assertTrue(phrase_is_negated("把运镜去掉", "运镜"))
        self.assertFalse(phrase_is_negated("生成图片然后删除背景", "生成图片"))

    def test_positive_occurrence_rescues_trailing_negated_variant(self):
        self.assertFalse(phrase_is_negated("只要分镜不要分镜表", "分镜"))


class LiveTriggerTests(unittest.TestCase):
    def test_every_workflow_has_a_live_trigger(self):
        wfs = load_workflows()
        for wid, wf in wfs.items():
            triggers = sorted(wf["triggers"], key=lambda x: len(normalize(x)), reverse=True)
            self.assertTrue(triggers, f"工作流缺少触发入口：{wid}")
            self.assertTrue(
                any(wid in match_route(t)["workflows"] for t in triggers),
                f"工作流无命中入口：{wid}",
            )

    def test_every_capability_has_a_live_trigger(self):
        caps = load_capabilities()
        for cid, cap in caps.items():
            phrases = list(dict.fromkeys(cap["triggers"] + cap["semantic_triggers"]))
            self.assertTrue(phrases, f"能力缺少触发词：{cid}")
            ordered = sorted(phrases, key=lambda x: len(normalize(x)), reverse=True)
            self.assertTrue(
                any(cid in match_route(p)["capabilities"] for p in ordered),
                f"能力无可命中入口：{cid}",
            )

    def test_every_capability_has_auto_workflow_route(self):
        known = set(load_workflows())
        for cid, meta in load_capabilities().items():
            self.assertTrue(meta["auto"], f"能力缺少 auto 路由：{cid}")
            self.assertTrue(set(meta["auto"]).issubset(known), f"能力路由到未知工作流：{cid}")


if __name__ == "__main__":
    unittest.main()
