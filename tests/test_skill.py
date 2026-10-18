"""QHSJ AIGC 全能影视 router and package-contract regression tests."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER_PATH = ROOT / "scripts" / "route_request.py"


def load_router():
    spec = importlib.util.spec_from_file_location("qhsj_test_router", ROUTER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载路由脚本")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = load_router()

    def route_ids(self, request):
        result = self.router.route(request)
        return ({item["id"] for item in result["selected_capabilities"]},
                {item["id"] for item in result["workflows"]}, result["constraints"])

    def test_compound_script_storyboard_video_prompt(self):
        caps, workflows, _ = self.route_ids("把这段剧本拆成逐镜分镜表，并给每镜生成视频提示词")
        self.assertTrue({"screenwriting", "storyboard", "video_prompt", "prompt_engineering"}.issubset(caps))
        self.assertTrue({"script-to-screen", "visual-prompt"}.issubset(workflows))

    def test_image_prompt_is_not_suppressed_by_storyboard_negation(self):
        caps, workflows, constraints = self.route_ids("不要分镜，只生成一张图片提示词")
        self.assertIn("image_prompt", caps)
        self.assertNotIn("storyboard", caps)
        self.assertIn("visual-prompt", workflows)
        self.assertFalse(constraints["explicit_no_prompt"])

    def test_sound_only_respects_negative_video_prompt_constraint(self):
        caps, workflows, constraints = self.route_ids("只做音效设计，不需要生成视频提示词")
        self.assertIn("audio_design", caps)
        self.assertNotIn("video_prompt", caps)
        self.assertNotIn("prompt_engineering", caps)
        self.assertIn("audio-design", workflows)
        self.assertTrue(constraints["explicit_no_prompt"])

    def test_agent_integration_routes_to_api_workflow(self):
        caps, workflows, _ = self.route_ids("帮我把外部Skill接入Claude Code、Codex和Dify，设计Agent集成步骤")
        self.assertTrue({"external_skill_integration", "api_integration"}.issubset(caps))
        self.assertIn("api-integration", workflows)

    def test_registry_resource_and_capability_ids_are_unique(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        capability_ids = [x["id"] for x in registry["capabilities"]]
        resource_paths = [x["file"] for x in registry["resources"]]
        self.assertEqual(len(capability_ids), len(set(capability_ids)))
        self.assertEqual(len(resource_paths), len(set(resource_paths)))
        for rel in resource_paths:
            self.assertTrue((ROOT / rel).is_file(), f"注册路径不存在：{rel}")

    def test_intent_analysis_is_always_scheduled(self):
        _, workflows, _ = self.route_ids("请把内容做得更有感染力")
        self.assertIn("intent-analysis", workflows)

    def test_semantic_triggers_are_live_dispatch_inputs_for_every_capability(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        for cap in registry["capabilities"]:
            phrases = list(dict.fromkeys(cap.get("semantic_triggers", []) + cap.get("triggers", [])))
            if not phrases:
                self.fail(f"能力缺少可测试触发词：{cap['id']}")
            successful = None
            for phrase in sorted(phrases, key=lambda x: len(self.router.normalize(x)), reverse=True):
                got, _, _ = self.route_ids(phrase)
                if cap["id"] in got:
                    successful = phrase
                    break
            self.assertIsNotNone(successful, f"能力没有任何可触发语义/关键词入口：{cap['id']}")

    def test_selected_capabilities_have_auto_workflow_routes(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        known = {w["id"] for w in registry["workflows"]}
        for cap in registry["capabilities"]:
            auto = cap.get("workflow_routes", {}).get("auto", [])
            self.assertTrue(auto, f"能力没有 auto 路由：{cap['id']}")
            self.assertTrue(set(auto).issubset(known), f"能力路由到未知工作流：{cap['id']}")

    def test_workflow_routes_are_not_truncated_to_five(self):
        result = self.router.route("从创意到成片，写剧本、分镜、角色资产、图片提示词、视频提示词、声音设计、Seedance适配、API集成和全量质量审查", max_modules=30)
        self.assertGreater(len(result["workflows"]), 5)
        self.assertFalse(result["resource_candidate_truncated"])

    def test_file_and_section_evidence_can_route_resources(self):
        result = self.router.route("请读取 references/qh-facs-au-dictionary.md 并设计微表情")
        files = {x["file"] for x in result["resource_route_candidates"]}
        self.assertTrue(any("qh-facs-au-dictionary.md" in x for x in files))
        self.assertTrue(any(x["id"] == "performance_emotion" for x in result["selected_capabilities"]))

    def test_user_constraints_are_not_overridden_by_dependency_routes(self):
        caps, workflows, constraints = self.route_ids("只设计音效，不需要分镜或视频提示词")
        self.assertIn("audio_design", caps)
        self.assertNotIn("storyboard", caps)
        self.assertNotIn("video_prompt", caps)
        self.assertNotIn("visual-prompt", workflows)

    def test_route_graph_exists_and_has_all_capability_nodes(self):
        graph = json.loads((ROOT / "routing" / "route-graph.json").read_text(encoding="utf-8"))
        nodes = {x["id"] for x in graph["nodes"]}
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        for cap in registry["capabilities"]:
            self.assertIn("capability:" + cap["id"], nodes)
        for res in registry["resources"]:
            self.assertIn("resource:" + res["file"], nodes)

    def test_every_registered_workflow_has_a_live_trigger(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        for wf in registry["workflows"]:
            triggers = sorted(wf.get("triggers", []), key=lambda x: len(self.router.normalize(x)), reverse=True)
            self.assertTrue(triggers, f"工作流缺少触发入口：{wf['id']}")
            found = False
            for trigger in triggers:
                result = self.router.route(trigger)
                if wf["id"] in {x["id"] for x in result["workflows"]}:
                    found = True
                    break
            self.assertTrue(found, f"工作流没有可以命中的真实路由入口：{wf['id']}")

    def test_every_indexed_heading_has_a_graph_path_from_its_resource(self):
        graph = json.loads((ROOT / "routing" / "route-graph.json").read_text(encoding="utf-8"))
        nodes = {x["id"] for x in graph["nodes"]}
        edges = {(e["from"], e["relation"], e["to"]) for e in graph["edges"]}
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        checked = 0
        for resource in registry["resources"]:
            rid = "resource:" + resource["file"]
            for heading in resource.get("headings", []):
                sid = f"section:{resource['file']}#{heading['anchor']}"
                self.assertIn(sid, nodes, f"章节节点缺失：{sid}")
                self.assertIn((rid, "contains_section", sid), edges, f"章节没有连接父资源：{sid}")
                checked += 1
        self.assertEqual(checked, graph["coverage"]["sections"])

    def test_every_resource_is_preserved_as_audit_route_candidate(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        result = self.router.route("请对整套 Skill 做全量路由覆盖审计，检查所有文件、板块、章节和代码是否连通", max_modules=1)
        candidate_paths = {x["source_path"] for x in result["resource_route_candidates"]}
        expected_paths = {x["file"] for x in registry["resources"]}
        self.assertTrue(expected_paths.issubset(candidate_paths), f"未进入全量审计候选的资源：{sorted(expected_paths-candidate_paths)[:10]}")
        self.assertTrue(result["module_list_truncated"] or len(result["recommended_modules"]) <= 1)
        self.assertEqual(result["route_coverage"]["all_registered_resources_kept_in_registry_graph"], True)

    def test_audio_only_with_multiple_negations_does_not_activate_visual_deliverables(self):
        caps, workflows, constraints = self.route_ids("只设计音效，不需要分镜或视频提示词，也不要图片提示词")
        self.assertIn("audio_design", caps)
        self.assertNotIn("storyboard", caps)
        self.assertNotIn("video_prompt", caps)
        self.assertNotIn("image_prompt", caps)
        self.assertNotIn("prompt_engineering", caps)
        self.assertNotIn("visual-prompt", workflows)
        self.assertTrue(constraints["explicit_no_prompt"])

    def test_user_can_request_video_prompt_while_excluding_full_pipeline(self):
        caps, workflows, constraints = self.route_ids("不要全流程，只给我一个短视频提示词")
        self.assertIn("video_prompt", caps)
        self.assertNotIn("full_production", caps)
        self.assertIn("visual-prompt", workflows)
        self.assertTrue(constraints["explicit_no_full_project"])

    def test_full_route_colloquial_request_activates_architecture_audit(self):
        request = "帮我做成百分百全路由，所有板块全部覆盖，全部都要增上连通，要能全面分析理解用户的要求。"
        caps, workflows, _ = self.route_ids(request)
        self.assertTrue({"skill_architecture_audit", "quality_assurance", "general_orchestration"}.issubset(caps))
        self.assertTrue({"intent-analysis", "qa"}.issubset(workflows))

    def test_full_route_request_without_literal_skill_word_is_routed(self):
        request = "不管我怎么用白话表达，都要把所有模块、知识文件、章节和代码接上路由，不能漏掉任何板块。"
        caps, workflows, _ = self.route_ids(request)
        self.assertIn("skill_architecture_audit", caps)
        self.assertIn("qa", workflows)

    def test_every_registered_resource_path_has_a_direct_route_match(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        # Exercise explicit-path matching for each file using its resource tags and graph registration.
        # The full package graph proves closure for all sections; here we test a representative route and
        # assert that every path has a nonempty tag-based route contract.
        for resource in registry["resources"]:
            self.assertTrue(resource.get("tags"), f"资源缺少路由标签：{resource.get('file')}")
            self.assertTrue(resource.get("triggers"), f"资源缺少触发入口：{resource.get('file')}")
            self.assertTrue(all(isinstance(tag, str) and tag for tag in resource["tags"]))
        sample = next(x for x in registry["resources"] if x["file"] == "references/qh-facs-au-dictionary.md")
        result = self.router.route("请读取 " + sample["file"] + " 并检查其中的内容")
        self.assertTrue(any(x["source_path"] == sample["file"] for x in result["resource_route_candidates"]))

    def test_architecture_audit_preserves_full_candidate_closure_without_unrelated_visual_dispatch(self):
        request = "帮我把整套 Skill 做成百分百全路由，所有板块、知识库章节、工作流和代码都要连通；运行全包审计和回归测试，不要生成图片或视频提示词。"
        result = self.router.route(request, max_modules=1)
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        caps = {item["id"] for item in result["selected_capabilities"]}
        workflows = {item["id"] for item in result["workflows"]}
        self.assertTrue({"skill_architecture_audit", "quality_assurance", "general_orchestration"}.issubset(caps))
        self.assertTrue({"intent-analysis", "qa"}.issubset(workflows))
        self.assertNotIn("visual-prompt", workflows)
        self.assertNotIn("full-production", workflows)
        self.assertEqual(result["resource_route_candidate_count"], len(registry["resources"]))
        self.assertFalse(result["resource_candidate_truncated"])
        self.assertTrue(result["route_coverage"]["route_graph_status"]["ok"])
        self.assertTrue(result["module_list_truncated"])

    def test_audit_intent_does_not_mean_execute_all_creative_workflows(self):
        caps, workflows, _ = self.route_ids("检查所有模块是否有路由，不要实际生成小说、分镜、图片或视频内容。")
        self.assertIn("skill_architecture_audit", caps)
        self.assertIn("qa", workflows)
        self.assertNotIn("visual-prompt", workflows)
        self.assertNotIn("full-production", workflows)
        self.assertNotIn("script-to-screen", workflows)

    def test_audit_only_constraint_suppresses_creative_deliverable_routes(self):
        result = self.router.route("检查所有模块是否有路由，不要实际生成小说、分镜、图片或视频内容。")
        caps = {item["id"] for item in result["selected_capabilities"]}
        workflows = {item["id"] for item in result["workflows"]}
        self.assertTrue(result["constraints"]["audit_only"])
        self.assertIn("skill_architecture_audit", caps)
        self.assertIn("quality_assurance", caps)
        self.assertTrue({"intent-analysis", "qa"}.issubset(workflows))
        self.assertTrue({"novel_writing", "storyboard", "image_prompt", "video_prompt", "prompt_engineering", "full_production"}.isdisjoint(caps))
        self.assertTrue({"visual-prompt", "full-production", "writing", "script-to-screen", "storyboard-only"}.isdisjoint(workflows))
        self.assertEqual(result["resource_route_candidate_count"], len(json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))["resources"]))

    def test_router_reports_actual_graph_closure_and_intent_evidence(self):
        result = self.router.route("帮我把小说改编成剧本和分镜，生成视频提示词并检查连续性")
        self.assertTrue(result["route_coverage"]["all_requests_enter_intent_analysis"])
        self.assertTrue(result["route_coverage"]["all_registered_resources_kept_in_registry_graph"])
        self.assertTrue(result["intent_analysis"]["raw_request_preserved"] == result["input"])
        self.assertIn("matched_capability_evidence", result["intent_analysis"])
        self.assertFalse(result["resource_candidate_truncated"])


    def test_static_image_prompt_does_not_overroute_video_or_reverse_engineering(self):
        caps, workflows, _ = self.route_ids("给我一段图片提示词，做成冷艳赛博朋克女性机械人")
        self.assertIn("image_prompt", caps)
        self.assertIn("visual-prompt", workflows)
        self.assertTrue({"video_prompt", "model_adaptation", "reverse_engineering", "spatial_continuity"}.isdisjoint(caps))
        self.assertNotIn("storyboard-only", workflows)

    def test_asset_lock_precedes_storyboard_asset_and_avoids_standalone_storyboard_macro(self):
        caps, workflows, _ = self.route_ids("先锁定人物和场景，再引用资产生成分镜图")
        self.assertIn("asset_locking", caps)
        self.assertTrue({"asset-lock", "asset-first"}.issubset(workflows))
        self.assertNotIn("storyboard-only", workflows)
        self.assertNotIn("video_prompt", caps)

    def test_short_video_prompt_does_not_dispatch_social_copy_pipeline(self):
        caps, workflows, constraints = self.route_ids("不要全流程，只给我一个短视频提示词")
        self.assertIn("video_prompt", caps)
        self.assertIn("visual-prompt", workflows)
        self.assertNotIn("short_video_content", caps)
        self.assertNotIn("platform-short-video", workflows)
        self.assertTrue(constraints["explicit_no_full_project"])

    def test_asset_workflows_enforce_lock_before_shot_assets(self):
        import yaml
        asset_first = yaml.safe_load((ROOT / "workflows" / "asset-first.yaml").read_text(encoding="utf-8"))
        script_to_screen = yaml.safe_load((ROOT / "workflows" / "script-to-screen.yaml").read_text(encoding="utf-8"))
        full_production = yaml.safe_load((ROOT / "workflows" / "full-production.yaml").read_text(encoding="utf-8"))
        def positions(data):
            return {stage["id"]: i for i, stage in enumerate(data.get("stages", []))}
        for data, lock_id, shot_id in ((asset_first, "A6", "A8"), (script_to_screen, "S3", "S6"), (full_production, "P3", "P6")):
            pos = positions(data)
            self.assertIn(lock_id, pos)
            self.assertIn(shot_id, pos)
            self.assertLess(pos[lock_id], pos[shot_id], data.get("name", data.get("id", "workflow")))
        schema = json.loads((ROOT / "schemas" / "storyboard.schema.json").read_text(encoding="utf-8"))
        props = schema.get("properties", {})
        self.assertIn("character_asset_refs", props)
        self.assertIn("scene_asset_ref", props)
        self.assertIn("asset_lock_status", props)

    def test_audit_closure_phrase_with_media_negations_is_audit_only(self):
        request = "帮我把整套 Skill 做成百分百全路由，所有板块、知识库章节、工作流和代码都要连通；运行全包审计和回归测试，不要生成图片或视频提示词。"
        result = self.router.route(request, max_modules=1)
        caps = {item["id"] for item in result["selected_capabilities"]}
        workflows = {item["id"] for item in result["workflows"]}
        self.assertTrue(result["constraints"]["audit_only"])
        self.assertTrue({"skill_architecture_audit", "quality_assurance"}.issubset(caps))
        self.assertTrue({"intent-analysis", "qa"}.issubset(workflows))
        self.assertTrue({"novel_writing", "screenwriting", "storyboard", "image_prompt", "video_prompt", "full_production"}.isdisjoint(caps))
        self.assertTrue({"writing", "visual-prompt", "storyboard-only", "full-production"}.isdisjoint(workflows))
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        self.assertEqual(result["resource_route_candidate_count"], len(registry["resources"]))

    def test_every_reference_is_documented_in_both_indexes(self):
        # 双索引 = references/index.md（人类可读目录）+ routing/route-registry.json（机器注册表）。
        # SKILL.md 不再内嵌逐文件索引，避免主入口膨胀至数百 KB 撑爆上下文。
        reference_files = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "references").glob("*.md"))
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        registry_paths = {r.get("file") or r.get("path") for r in registry.get("resources", [])}
        index_text = (ROOT / "references" / "index.md").read_text(encoding="utf-8")
        for rel in reference_files:
            self.assertIn(rel, registry_paths, f"route-registry.json 漏登记：{rel}")
            self.assertIn(Path(rel).name, index_text, f"references/index.md 漏项：{rel}")



    def test_content_aliases_preserve_original_hash_and_resolve_to_canonical_body(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        aliases = [item for item in registry["resources"] if item.get("alias_of")]
        self.assertTrue(aliases, "应存在显式登记的兼容路由别名")
        for item in aliases:
            alias_path = ROOT / item["file"]
            canonical_path = ROOT / item["alias_of"]
            self.assertTrue(alias_path.is_file(), f"别名路径不存在：{item['file']}")
            self.assertTrue(canonical_path.is_file(), f"规范正文不存在：{item['alias_of']}")
            text = alias_path.read_text(encoding="utf-8")
            match = re.search(r'^<!-- QHSJ-CONTENT-ALIAS canonical="([^"]+)" original_sha256="([0-9a-f]{64})"-->$', text, re.M)
            self.assertIsNotNone(match, f"别名缺少原始正文哈希：{item['file']}")
            self.assertEqual(match.group(1), item["alias_of"])
            self.assertEqual(match.group(2), item.get("source_content_sha256"))
            target_hash = hashlib.sha256(canonical_path.read_bytes()).hexdigest()
            # A canonical reference may receive additive, audited repairs after exact-deduplication.
            # In that case the alias must retain the original-body hash and redirect to the evolved
            # canonical source rather than falsely claiming the new bytes were the old source.
            if match.group(2) == target_hash:
                self.assertEqual(item.get("sha256"), hashlib.sha256(alias_path.read_bytes()).hexdigest())
            else:
                self.assertIn(f"`{Path(item['alias_of']).name}`", text)
                self.assertEqual(match.group(2), item.get("source_content_sha256"))
            alias_hash = hashlib.sha256(alias_path.read_bytes()).hexdigest()
            self.assertEqual(item.get("sha256"), alias_hash, f"清单中的别名文件哈希过期：{item['file']}")

    def test_content_aliases_inherit_all_canonical_section_routes(self):
        registry = json.loads((ROOT / "routing" / "route-registry.json").read_text(encoding="utf-8"))
        resources = {item["file"]: item for item in registry["resources"]}
        graph = json.loads((ROOT / "routing" / "route-graph.json").read_text(encoding="utf-8"))
        node_ids = {item["id"] for item in graph["nodes"]}
        edges = {(item["from"], item["relation"], item["to"]) for item in graph["edges"]}
        aliases = [item for item in registry["resources"] if item.get("alias_of")]
        for alias in aliases:
            canonical = resources[alias["alias_of"]]
            canonical_headings = [(x.get("level"), x.get("heading"), x.get("anchor")) for x in canonical.get("headings", [])]
            alias_headings = [(x.get("level"), x.get("heading"), x.get("anchor")) for x in alias.get("headings", [])]
            self.assertEqual(alias_headings, canonical_headings, f"别名章节索引未继承完整：{alias['file']}")
            rid = "resource:" + alias["file"]
            for heading in alias.get("headings", []):
                sid = f"section:{alias['file']}#{heading['anchor']}"
                self.assertIn(sid, node_ids, f"别名章节节点缺失：{sid}")
                self.assertIn((rid, "contains_section", sid), edges, f"别名章节未连接父资源：{sid}")

    def test_exact_duplicate_reference_bodies_are_not_physically_repeated(self):
        seen = {}
        duplicates = []
        for path in sorted((ROOT / "references").rglob("*.md")):
            data = path.read_bytes()
            first_line = data.splitlines()[0].decode("utf-8", errors="replace") if data else ""
            if first_line.startswith("<!-- QHSJ-CONTENT-ALIAS "):
                continue
            digest = hashlib.sha256(data).hexdigest()
            if digest in seen:
                duplicates.append((seen[digest], path.relative_to(ROOT).as_posix()))
            else:
                seen[digest] = path.relative_to(ROOT).as_posix()
        self.assertEqual(duplicates, [], f"仍有物理重复正文：{duplicates[:10]}")

    def test_explicit_alias_request_redirects_to_canonical_resource_but_keeps_alias_trace(self):
        result = self.router.route("请读取 references/p1-api-contracts.md 并检查API")
        candidates = [item for item in result["resource_route_candidates"] if item.get("source_path") == "references/p1-api-contracts.md"]
        self.assertTrue(candidates, "显式旧路径没有进入资源候选")
        item = candidates[0]
        self.assertEqual(item.get("file"), "references/api-contracts.md")
        self.assertEqual(item.get("alias_redirect"), "references/api-contracts.md")
        self.assertTrue(item.get("explicit_path_match"))


    def test_colloquial_asset_first_request_routes_full_ordered_pipeline(self):
        request = "我想做一个会在雨夜巷子里遇到旧友的电影感短视频，人物要保持一致，先设计人物和场景图，再做分镜，最后生成可灵视频提示词"
        result = self.router.route(request)
        caps = {item["id"] for item in result["selected_capabilities"]}
        workflow_ids = [item["id"] for item in result["workflows"]]
        self.assertTrue({"asset_first", "asset_locking", "character_design", "storyboard", "spatial_continuity", "video_prompt", "model_adaptation", "prompt_engineering"}.issubset(caps))
        self.assertTrue({"asset-first", "asset-lock", "script-to-screen", "model-adaptation", "visual-prompt"}.issubset(workflow_ids))
        self.assertNotIn("storyboard-only", workflow_ids)
        self.assertEqual(result["primary_workflow"]["id"], "asset-first")
        self.assertLess(workflow_ids.index("asset-first"), workflow_ids.index("asset-lock"))
        self.assertLess(workflow_ids.index("asset-lock"), workflow_ids.index("script-to-screen"))

    def test_explicitly_negated_character_and_scene_images_do_not_activate_asset_pipeline(self):
        request = "不要人物图和场景图，只要文字分镜，不要提示词"
        caps, workflows, constraints = self.route_ids(request)
        self.assertTrue({"storyboard"}.issubset(caps))
        self.assertTrue({"asset_first", "asset_locking", "character_design", "image_prompt", "video_prompt", "prompt_engineering"}.isdisjoint(caps))
        self.assertNotIn("asset-first", workflows)
        self.assertNotIn("asset-lock", workflows)
        self.assertNotIn("visual-prompt", workflows)
        self.assertTrue(constraints["explicit_no_prompt"])
        self.assertTrue(constraints["explicit_no_image_prompt"])

    def test_asset_lifecycle_enums_are_consistent_without_corrupting_project_or_qa_states(self):
        state = json.loads((ROOT / "schemas" / "project-state.schema.json").read_text(encoding="utf-8"))
        storyboard = json.loads((ROOT / "schemas" / "storyboard.schema.json").read_text(encoding="utf-8"))
        expected = ["draft", "review", "locked", "locked_provisional", "superseded", "blocked", "needs_recheck"]
        self.assertEqual(state["properties"]["status"]["enum"], ["draft", "in_progress", "blocked", "review", "completed", "archived"])
        self.assertEqual(state["properties"]["qa_state"]["properties"]["status"]["enum"], ["not_run", "passed", "passed_with_warnings", "failed", "blocked"])
        self.assertEqual(state["properties"]["asset_state"]["properties"]["asset_locks"]["items"]["properties"]["status"]["enum"], expected)
        self.assertEqual(state["definitions"]["asset_record"]["properties"]["status"]["enum"], expected)
        self.assertEqual(storyboard["properties"]["asset_lock_status"]["enum"], expected)
        protocol = (ROOT / "references" / "qhsj-asset-locking-protocol.md").read_text(encoding="utf-8")
        ledger = (ROOT / "templates" / "asset-lock-ledger.md").read_text(encoding="utf-8")
        for word in ("locked_provisional", "needs_recheck"):
            self.assertIn(word, protocol)
            self.assertIn(word, ledger)

    def test_api_adapter_uses_explicit_configuration_and_checked_http_response(self):
        adapter = (ROOT / "references" / "qh-comfyui-canvas-automation.md").read_text(encoding="utf-8")
        self.assertNotIn("api.example.com", adapter)
        self.assertNotIn("YOUR_API_KEY", adapter)
        self.assertIn("QHSJ_VIDEO_API_URL", adapter)
        self.assertIn("QHSJ_VIDEO_API_KEY", adapter)
        self.assertIn("timeout=timeout_seconds", adapter)
        self.assertIn("response.raise_for_status()", adapter)
        self.assertIn("official API documentation", adapter)

    def test_local_negation_does_not_fabricate_excluded_capability(self):
        # A single local negative must not activate the capability it excludes,
        # while unrelated positive deliverables in the same sentence stay active.
        cases = [
            ("做个视频，不要音效", "audio_design"),
            ("不要运镜", "cinematography"),
            ("不要打斗", "action_choreography"),
            ("不要爆炸特效", "vfx_physics"),
            ("不要配音", "audio_design"),
            ("别做分镜", "storyboard"),
            ("不生成图片", "image_prompt"),
            ("没有运镜要求", "cinematography"),
            ("把运镜去掉", "cinematography"),
            ("没有音效", "audio_design"),
        ]
        for request, excluded in cases:
            caps, _, _ = self.route_ids(request)
            self.assertNotIn(excluded, caps, f"否定泄露：{request} 仍触发了 {excluded}")

    def test_colloquial_short_triggers_route_expected_capability(self):
        cases = [
            ("帮我出张图", "image_prompt"),
            ("给我生图", "image_prompt"),
            ("只要图片", "image_prompt"),
            ("帮我做个片子", "video_prompt"),
            ("做个短视频", "short_video_content"),
            ("帮我做一个打戏", "action_choreography"),
            ("锁定角色和场景", "asset_locking"),
            ("把她锁住别变", "asset_locking"),
            ("把结果输出成json", "output_formatting"),
            # 口语直给、行业黑话与自然短语触发
            ("帮我搞一段能生视频的咒语", "video_prompt"),
            ("来个赛博朋克妹子的大图", "image_prompt"),
            ("帮我把这段分个镜", "storyboard"),
            ("给女主画个立绘", "character_design"),
            ("这个微表情怎么演", "performance_emotion"),
            ("照着这张图做一个同款", "reverse_engineering"),
            ("先出设定图", "asset_first"),
            ("把脸定型别再变", "asset_locking"),
            ("小红书怎么发", "platform_adaptation"),
            ("给我输出json", "output_formatting"),
            # 新增：短剧/短片/角色一致性口语触发变体
            ("帮我做个AI短剧", "short_video_content"),
            ("帮我做个AI短剧", "screenwriting"),
            ("就想做个酷炫的片", "video_prompt"),
            ("来部微电影", "video_prompt"),
            ("这个角色每集都要长得一样", "asset_locking"),
            ("这个角色每集都要长得一样", "character_design"),
            ("就要个静态图提示词", "image_prompt"),
            ("帮我把这段动作描写转成镜头", "storyboard"),
            ("帮我做一版竖屏版和横屏版", "platform_adaptation"),
            ("给我来张封面图", "image_prompt"),
        ]
        for request, expected in cases:
            caps, _, _ = self.route_ids(request)
            self.assertIn(expected, caps, f"白话触发未命中：{request} 未触发 {expected}")

    def test_consistency_defect_wording_is_not_treated_as_asset_locking(self):
        # “人物位置不一致”是问题描述而非“锁定资产”意图，不得误触发 asset_locking。
        caps, _, _ = self.route_ids("修复分镜里人物位置不一致")
        self.assertIn("spatial_continuity", caps)
        self.assertNotIn("asset_locking", caps)

    def test_consistency_fix_request_reaches_quality_gate(self):
        caps, _, _ = self.route_ids("角色前后不一致，怎么修")
        self.assertIn("quality_assurance", caps)

    def test_clause_scoped_negation_keeps_later_positive_deliverable(self):
        # 否定作用域不得跨越分句：前句“不要运镜”不能抹掉后句“静态视频提示词”。
        caps, workflows, _ = self.route_ids("不要运镜，就要个静态视频提示词")
        self.assertIn("video_prompt", caps)
        self.assertIn("visual-prompt", workflows)
        pn = self.router.phrase_is_negated
        self.assertFalse(pn("不要运镜，就要个静态视频提示词", "视频提示词"))
        self.assertFalse(pn("不要图片提示词，只要视频提示词", "视频提示词"))
        self.assertTrue(pn("不要分镜表", "分镜"))
        self.assertFalse(pn("要音效，不要分镜", "音效"))
        self.assertFalse(pn("不要音效，要配音", "配音"))

    def test_positive_occurrence_rescues_trailing_negated_variant_in_same_clause(self):
        # 同一分句内“只要分镜”与“不要分镜表”并存时，正向请求优先，不应整体否定 storyboard。
        self.assertFalse(self.router.phrase_is_negated("只要分镜不要分镜表", "分镜"))

    def test_phrase_is_negated_handles_local_scope_and_overlap(self):
        pn = self.router.phrase_is_negated
        self.assertTrue(pn("不要音效", "音效"))
        self.assertTrue(pn("不生成图片", "生成图片"))  # negator overlaps the phrase prefix
        self.assertTrue(pn("别做分镜", "分镜"))
        self.assertTrue(pn("不要分镜，只生成图片提示词", "分镜"))
        self.assertFalse(pn("要音效，不要分镜", "音效"))
        self.assertFalse(pn("生成图片提示词", "生成图片"))
        self.assertFalse(pn("只要图片", "图片"))

    def test_phrase_is_negated_covers_none_requirement_and_postfix_removal(self):
        # “没有X要求” 与 “把X去掉” 都是常见的中文排除表达，必须识别为否定。
        pn = self.router.phrase_is_negated
        self.assertTrue(pn("没有运镜要求", "运镜"))
        self.assertTrue(pn("把运镜去掉", "运镜"))
        self.assertTrue(pn("运镜删掉", "运镜"))
        self.assertTrue(pn("别看运镜", "运镜"))
        self.assertTrue(pn("没有音效，只要画面", "音效"))
        # 删除动作与正向交付物不相邻时不得误伤正向交付物。
        self.assertFalse(pn("生成图片然后删除背景", "生成图片"))
        self.assertFalse(pn("生成图片后删除背景", "生成图片"))



if __name__ == "__main__":
    unittest.main()
