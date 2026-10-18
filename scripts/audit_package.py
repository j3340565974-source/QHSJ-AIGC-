#!/usr/bin/env python3
"""QHSJ AIGC 全能影视 离线包结构审计：路由覆盖、文件哈希、Schema/YAML、Markdown 链接与 Python 语法。"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, subprocess, sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
META_FILES = {"MANIFEST.json", "routing/route-registry.json", ".gitignore"}
# Transient caches and VCS/editor dirs are not part of the shipped package.
IGNORED_DIR_PARTS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".pydantic_cache", ".tox", ".git", ".idea", ".vscode"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}


def is_shipped_file(path: Path) -> bool:
    """A shipped file is a real source file, not a build/editor/VCS cache artifact."""
    return (
        path.is_file()
        and path.suffix not in IGNORED_SUFFIXES
        and not IGNORED_DIR_PARTS.intersection(path.parts)
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def alias_stub_metadata(path: Path) -> dict[str, str] | None:
    """Return compatibility-alias metadata if a Markdown file is a QHSJ alias stub."""
    try:
        first = path.read_text(encoding="utf-8", errors="replace").splitlines()[0]
    except (OSError, IndexError):
        return None
    if not first.startswith("<!-- QHSJ-CONTENT-ALIAS ") or not first.endswith("-->"):
        return None
    body = first[len("<!-- QHSJ-CONTENT-ALIAS "):-3].strip()
    return {k: v for k, v in re.findall(r'([a-z0-9_]+)="([^"]*)"', body)}


def markdown_links(text: str):
    # Covers inline links and images; intentionally does not parse reference-style links.
    pattern = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)")
    for match in pattern.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        target = target.split()[0] if target else ""
        yield target


def heading_records(path: Path):
    records=[]
    seen={}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m=re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$",line)
        if m:
            h=m.group(2).strip()
            base=re.sub(r"[^\w\u4e00-\u9fff -]","",h.lower())
            base=re.sub(r"\s+","-",base).strip("-")
            count=seen.get(base,0); seen[base]=count+1
            slug=base if count==0 else f"{base}-{count}"
            records.append((len(m.group(1)), h, slug))
    return records


def main() -> int:
    ap=argparse.ArgumentParser(description="离线审计 QHSJ AIGC 全能影视 Skill 包")
    ap.add_argument("--json", action="store_true")
    args=ap.parse_args()
    errors=[]; warnings=[]; stats={}
    registry_path=ROOT/"routing/route-registry.json"
    if not registry_path.is_file():
        errors.append("缺失 routing/route-registry.json")
        registry={}
    else:
        try: registry=json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception as exc: registry={}; errors.append(f"路由注册表 JSON 解析失败：{exc}")

    files={p.relative_to(ROOT).as_posix():p for p in ROOT.rglob("*") if is_shipped_file(p)}
    stats["package_files"] = len(files)

    # Manifest must cover every shipped file except itself, with current byte sizes and SHA-256.
    manifest_path = ROOT / "MANIFEST.json"
    manifest_errors = []
    manifest_record_count = 0
    if not manifest_path.is_file():
        manifest_errors.append("缺失 MANIFEST.json")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest_items = manifest.get("files", [])
            manifest_paths = [x.get("path") for x in manifest_items if isinstance(x, dict)]
            manifest_record_count = len(manifest_paths)
            if manifest.get("version") != "3.0.0":
                manifest_errors.append(f"Manifest 版本与发行版本不一致：{manifest.get('version')}")
            if manifest.get("inventory_count") != len(manifest_items):
                manifest_errors.append("Manifest inventory_count 与 files 条目数不一致")
            if len(manifest_paths) != len(set(manifest_paths)):
                manifest_errors.append("Manifest 存在重复文件路径")
            expected_paths = set(files) - {"MANIFEST.json"}
            actual_paths = set(manifest_paths)
            if expected_paths != actual_paths:
                manifest_errors.append(
                    f"Manifest 清单路径不完整：缺少 {len(expected_paths-actual_paths)}，多出 {len(actual_paths-expected_paths)}"
                )
            for item in manifest_items:
                if not isinstance(item, dict):
                    continue
                rel = item.get("path", "")
                actual = files.get(rel)
                if actual is None:
                    continue
                if item.get("size_bytes") != actual.stat().st_size:
                    manifest_errors.append(f"Manifest 文件大小已过期：{rel}")
                if item.get("sha256") != sha256(actual):
                    manifest_errors.append(f"Manifest SHA-256 已过期：{rel}")
        except Exception as exc:
            manifest_errors.append(f"Manifest JSON/结构解析失败：{exc}")
    errors.extend(manifest_errors)
    stats["manifest_entries"] = manifest_record_count
    stats["manifest_errors"] = len(manifest_errors)

    # Old package identity must not remain embedded in user-facing source files or artwork.
    brand_markers = ["漫剧" + "老李", "老" + "李", "轻" + "绘", "QING" + "HUI", "QHSJ" + "-Film", "Light" + " drawing"]
    brand_errors = []
    textual_suffixes = {".md", ".markdown", ".yaml", ".yml", ".json", ".py", ".svg", ".txt", ".toml", ".xml"}
    for rel, path in files.items():
        if path.suffix.lower() not in textual_suffixes:
            continue
        # The auditor necessarily contains brand-detection logic. Do not scan its
        # implementation as user-facing payload, or the detector self-reports.
        if rel == "scripts/audit_package.py":
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for marker in brand_markers:
            if marker.casefold() in content.casefold():
                brand_errors.append(f"旧项目品牌残留 {marker!r}：{rel}")
    errors.extend(brand_errors)
    stats["brand_leak_errors"] = len(brand_errors)

    resource_by_path={r.get("file"):r for r in registry.get("resources",[]) if isinstance(r,dict) and r.get("file")}
    missing=[rel for rel in files if rel not in META_FILES and rel not in resource_by_path]
    extra=[rel for rel in resource_by_path if rel not in files]
    if missing: errors.append(f"路由资源注册表遗漏文件 {len(missing)} 个："+", ".join(missing[:30]))
    if extra: errors.append(f"路由资源注册表引用不存在文件 {len(extra)} 个："+", ".join(extra[:30]))
    stats["registered_resources"] = len(resource_by_path)
    stats["unregistered_files"] = len(missing)
    stats["unresolved_registry_paths"] = len(extra)

    # Every resource hash is recalculated against the actual file.
    hash_mismatch=[]
    for rel,rec in resource_by_path.items():
        path=files.get(rel)
        if not path: continue
        expected=rec.get("sha256")
        if expected and sha256(path)!=expected: hash_mismatch.append(rel)
    if hash_mismatch: errors.append(f"资源 SHA-256 过期 {len(hash_mismatch)} 项："+", ".join(hash_mismatch[:25]))
    stats["hash_mismatch"] = len(hash_mismatch)

    # Capability coverage, valid dependency identifiers, no dependency cycles.
    caps=registry.get("capabilities",[])
    cap_by_id={c.get("id"):c for c in caps if isinstance(c,dict)}
    cap_issues=[]
    for c in caps:
        cid=c.get("id", "<missing-id>")
        if not c.get("triggers"): cap_issues.append(f"能力 {cid} 没有触发词")
        if not c.get("reference_files"): warnings.append(f"能力 {cid} 暂无引用知识文件（可由工作流/其他能力支撑）")
        for dep in c.get("dependencies",[]):
            if dep not in cap_by_id: cap_issues.append(f"能力 {cid} 依赖不存在的能力 {dep}")
        for ref in c.get("reference_files",[]):
            if ref not in files: cap_issues.append(f"能力 {cid} 引用了不存在的知识文件 {ref}")
    color={}; stack=[]
    def visit(cid):
        if color.get(cid)==1:
            cycle=stack[stack.index(cid):]+[cid] if cid in stack else stack+[cid]
            cap_issues.append("能力依赖存在循环："+" -> ".join(cycle)); return
        if color.get(cid)==2: return
        color[cid]=1; stack.append(cid)
        for dep in cap_by_id.get(cid,{}).get("dependencies",[]):
            if dep in cap_by_id: visit(dep)
        stack.pop(); color[cid]=2
    for cid in cap_by_id: visit(cid)
    errors.extend(cap_issues)
    stats["capabilities"] = len(caps)

    # A duplicate body is retained once. Its former paths may either remain byte-identical
    # compatibility copies (older packages) or become small, hash-stamped alias stubs.
    alias_errors=[]; alias_count=0; alias_stub_count=0
    for rel,rec in resource_by_path.items():
        if rec.get("status")!="alias": continue
        alias_count+=1; target=rec.get("alias_of")
        if target not in files:
            alias_errors.append(f"别名目标不存在：{rel} -> {target}")
            continue
        if sha256(files[rel]) == sha256(files[target]):
            continue
        meta = alias_stub_metadata(files[rel])
        if not meta or meta.get("canonical") != target:
            alias_errors.append(f"别名既非规范正文的字节副本，也不是指向正确目标的兼容别名：{rel} -> {target}")
            continue
        expected_source_hash = rec.get("source_content_sha256")
        if expected_source_hash and meta.get("original_sha256") != expected_source_hash:
            alias_errors.append(f"别名原正文哈希与注册表不一致：{rel}")
        alias_stub_count += 1
    errors.extend(alias_errors)
    stats["aliases"] = alias_count
    stats["alias_stub_files"] = alias_stub_count

    # Heading-level route index is complete for reference Markdown files.
    heading_errors=[]; headings_total=0
    for rel,path in files.items():
        if rel.startswith("references/") and path.suffix==".md":
            rec=resource_by_path.get(rel)
            if not rec: continue
            heading_path = files.get(rec.get("alias_of")) if rec.get("status") == "alias" and rec.get("alias_of") in files else path
            actual=heading_records(heading_path); indexed=rec.get("headings",[]); headings_total+=len(indexed)
            actual_tuple=[(lv,h,slug) for lv,h,slug in actual]
            indexed_tuple=[(h.get("level"),h.get("heading"),h.get("anchor")) for h in indexed]
            if actual_tuple!=indexed_tuple:
                heading_errors.append(f"章节索引与文件标题不一致：{rel}（文件 {len(actual)} / 注册表 {len(indexed)}）")
            if not rec.get("tags"): heading_errors.append(f"参考模块没有能力标签：{rel}")
    errors.extend(heading_errors)
    stats["indexed_reference_headings"] = headings_total
    stats["reference_markdown_files"] = sum(1 for rel in files if rel.startswith("references/") and rel.endswith(".md"))

    # Workflow registry, YAML syntax, and referenced local modules.
    try:
        import yaml
    except ImportError:
        yaml=None; warnings.append("未安装 PyYAML；已跳过 YAML 结构解析，但不影响 JSON/Python 检查")
    workflow_index_path=ROOT/"workflows/index.yaml"
    wf_index={}
    if not workflow_index_path.is_file(): errors.append("缺失 workflows/index.yaml")
    elif yaml:
        try: wf_index=yaml.safe_load(workflow_index_path.read_text(encoding="utf-8")) or {}
        except Exception as exc: errors.append(f"workflows/index.yaml 解析失败：{exc}")
    index_ids=set(); indexed_files=set()
    # The index cross-checks below require a parsed workflows/index.yaml. When PyYAML is
    # unavailable they must be skipped, not silently produce false "未登记" errors.
    if yaml:
        for item in wf_index.get("workflows",[]) if isinstance(wf_index,dict) else []:
            if not isinstance(item,dict): errors.append("workflows/index.yaml 中存在非对象条目"); continue
            wid=item.get("id"); rel=(Path("workflows")/str(item.get("file",""))).as_posix()
            if wid in index_ids: errors.append(f"工作流 ID 重复：{wid}")
            index_ids.add(wid); indexed_files.add(rel)
            if rel not in files: errors.append(f"工作流索引指向不存在文件：{rel}")
    wf_defs=registry.get("workflows",[])
    reg_wf_ids=set()
    for wf in wf_defs:
        wid=wf.get("id"); rel=wf.get("file")
        if wid in reg_wf_ids: errors.append(f"路由注册表工作流 ID 重复：{wid}")
        reg_wf_ids.add(wid)
        if rel not in files: errors.append(f"路由注册表引用不存在工作流文件：{rel}")
        if yaml and wid not in index_ids: errors.append(f"工作流未登记到 workflows/index.yaml：{wid}")
    if yaml:
        for wid in sorted(index_ids-reg_wf_ids): errors.append(f"workflows/index.yaml 中有工作流未进入路由注册表：{wid}")
    yaml_errors=[]; missing_module_refs=[]
    for rel,path in files.items():
        if path.suffix.lower() not in (".yaml", ".yml"): continue
        if yaml:
            try: data=yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc: yaml_errors.append(f"YAML 解析失败：{rel}: {exc}"); continue
            if rel.startswith("workflows/") and rel!="workflows/index.yaml" and isinstance(data,dict):
                def inspect(obj):
                    if isinstance(obj,dict):
                        mods=obj.get("modules")
                        if isinstance(mods,list):
                            for mod in mods:
                                if isinstance(mod,str) and (mod.startswith("references/") or mod.startswith("schemas/") or mod.startswith("scripts/") or mod.startswith("templates/")) and mod not in files:
                                    missing_module_refs.append(f"{rel} -> {mod}")
                        for v in obj.values(): inspect(v)
                    elif isinstance(obj,list):
                        for v in obj: inspect(v)
                inspect(data)
    errors.extend(yaml_errors)
    errors.extend(["工作流模块路径不存在："+x for x in missing_module_refs])
    stats["workflows"] = len(wf_defs)

    # Markdown local paths: report broken file targets; fragments are left as native Markdown anchors.
    broken_links=[]
    for rel,path in files.items():
        if path.suffix.lower() not in (".md", ".markdown"): continue
        raw=path.read_text(encoding="utf-8",errors="replace")
        for target in markdown_links(raw):
            if not target or target.startswith(("https://","http://","mailto:","tel:","data:")) or target.startswith("//"):
                continue
            target=target.split("#",1)[0]
            if not target: continue
            # Preserve references to host-specific absolute paths and template substitution variables.
            if target.startswith(("~/", "$HOME/", "${", "<", "{{")): continue
            candidate=(path.parent/target).resolve()
            try: candidate.relative_to(ROOT.resolve())
            except ValueError: continue
            if not candidate.exists(): broken_links.append(f"{rel} -> {target}")
    if broken_links: errors.append(f"Markdown 本地链接断裂 {len(broken_links)} 项："+"; ".join(broken_links[:35]))
    stats["broken_markdown_links"] = len(broken_links)

    # Python syntax check for every shipped Python source.
    py_files=[p for p in files.values() if p.suffix==".py"]
    py_errors=[]
    for path in py_files:
        try: compile(path.read_text(encoding="utf-8"),str(path),"exec")
        except Exception as exc: py_errors.append(f"Python 语法错误：{path.relative_to(ROOT)}: {exc}")
    errors.extend(py_errors); stats["python_files"] = len(py_files)

    # Every JSON/JSON Schema file parses and schemas themselves pass meta-schema validation.
    json_errors=[]; json_count=0
    try:
        import jsonschema
    except ImportError:
        jsonschema=None; warnings.append("未安装 jsonschema；仅检查 JSON 语法，跳过 Schema 实例校验")
    schema_paths=[p for rel,p in files.items() if p.suffix==".json" and ("schema" in p.name or p.name.endswith(".schema.json"))]
    for rel,path in files.items():
        if path.suffix.lower()!=".json": continue
        json_count+=1
        try: data=json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc: json_errors.append(f"JSON 解析失败：{rel}: {exc}"); continue
        if jsonschema and path in schema_paths:
            try: jsonschema.Draft7Validator.check_schema(data)
            except Exception as exc: json_errors.append(f"JSON Schema 无效：{rel}: {exc}")
    errors.extend(json_errors); stats["json_files"] = json_count; stats["schemas"] = len(schema_paths)

    # Full-route contract checks: capability dispatch, resource tags, and graph reachability.
    valid_cap_ids=set(cap_by_id)
    route_map_errors=[]
    workflow_by_id={w.get("id"):w for w in wf_defs if isinstance(w,dict)}
    resources_by_tag= {cid:0 for cid in valid_cap_ids}
    for c in caps:
        wr=c.get("workflow_routes",{}) if isinstance(c,dict) else {}
        auto=wr.get("auto",[]) if isinstance(wr,dict) else []
        conditional=wr.get("conditional",[]) if isinstance(wr,dict) else []
        if not auto: route_map_errors.append(f"能力没有自动工作流路由：{c.get('id')}")
        if not any(wid in workflow_by_id for wid in auto): route_map_errors.append(f"能力自动工作流路由无效：{c.get('id')} -> {auto}")
        for wid in auto+conditional:
            if wid not in workflow_by_id: route_map_errors.append(f"能力引用不存在工作流：{c.get('id')} -> {wid}")
    for rel,rec in resource_by_path.items():
        tags=rec.get("tags",[])
        if not tags: route_map_errors.append(f"资源无能力路由标签：{rel}")
        for tag in tags:
            if tag not in valid_cap_ids: route_map_errors.append(f"资源标签指向不存在能力：{rel} -> {tag}")
            else: resources_by_tag[tag]+=1
        if not rec.get("triggers") and rel not in META_FILES: route_map_errors.append(f"资源无触发/检索入口：{rel}")
    for cid,count in resources_by_tag.items():
        if count==0: route_map_errors.append(f"能力没有任何可路由资源：{cid}")
    errors.extend(route_map_errors)
    stats["capabilities_with_auto_workflow_route"] = sum(1 for c in caps if c.get("workflow_routes",{}).get("auto"))
    stats["resources_with_valid_capability_tags"] = sum(1 for rel,rec in resource_by_path.items() if rec.get("tags") and all(t in valid_cap_ids for t in rec.get("tags",[])))

    graph_path=ROOT/"routing/route-graph.json"
    graph_errors=[]
    if not graph_path.is_file(): graph_errors.append("缺失 routing/route-graph.json")
    else:
        try:
            graph=json.loads(graph_path.read_text(encoding="utf-8"))
            node_ids={n.get("id") for n in graph.get("nodes",[]) if isinstance(n,dict)}
            edge_pairs={(e.get("from"),e.get("relation"),e.get("to")) for e in graph.get("edges",[]) if isinstance(e,dict)}
            for c in caps:
                nid="capability:"+str(c.get("id"))
                if nid not in node_ids: graph_errors.append("路由图缺少能力节点："+nid)
                for wid in c.get("workflow_routes",{}).get("auto",[]):
                    edge=(nid,"routes_auto_to","workflow:"+str(wid))
                    if edge not in edge_pairs: graph_errors.append(f"路由图缺少自动工作流边：{edge}")
            for rel,rec in resource_by_path.items():
                rid="resource:"+rel
                if rid not in node_ids: graph_errors.append("路由图缺少资源节点："+rid)
                for tag in rec.get("tags",[]):
                    edge=("capability:"+str(tag),"routes_to_resource",rid)
                    if edge not in edge_pairs: graph_errors.append(f"路由图缺少资源连接边：{edge}")
                for heading in rec.get("headings",[]):
                    sid=f"section:{rel}#{heading.get('anchor','')}"
                    if sid not in node_ids: graph_errors.append("路由图缺少章节节点："+sid)
                    if (rid,"contains_section",sid) not in edge_pairs: graph_errors.append(f"路由图缺少章节父边：{rid} -> {sid}")
            for c in caps:
                for dep in c.get("dependencies",[]):
                    edge=("capability:"+str(c.get("id")),"depends_on","capability:"+str(dep))
                    if edge not in edge_pairs: graph_errors.append(f"路由图缺少能力依赖边：{edge}")
            reachable_workflows={e.get("to") for e in graph.get("edges",[]) if e.get("relation") in {"routes_auto_to","routes_conditional_to","precedes_all_workflows"}}
            for wf in wf_defs:
                wid="workflow:"+str(wf.get("id"))
                if wid not in node_ids: graph_errors.append("路由图缺少工作流节点："+wid)
                if wid not in reachable_workflows: graph_errors.append("工作流没有来自能力或入口工作流的调度边："+wid)
            if graph.get("coverage",{}).get("capabilities") != len(caps): graph_errors.append("路由图能力覆盖统计与注册表不一致")
            if graph.get("coverage",{}).get("resources") != len(resource_by_path): graph_errors.append("路由图资源覆盖统计与注册表不一致")
            section_count=sum(len(rec.get("headings",[])) for rec in resource_by_path.values())
            actual_section_nodes=sum(1 for node in graph.get("nodes",[]) if isinstance(node,dict) and node.get("type")=="section")
            if actual_section_nodes != section_count: graph_errors.append(f"路由图章节节点计数不一致：图 {actual_section_nodes} / 注册表 {section_count}")
            stats["route_graph_section_nodes"] = actual_section_nodes
            stats["route_graph_workflow_nodes"] = sum(1 for node in graph.get("nodes",[]) if isinstance(node,dict) and node.get("type")=="workflow")
            stats["route_graph_edges"] = len(graph.get("edges",[]))
        except Exception as exc: graph_errors.append(f"路由图 JSON/结构读取失败：{exc}")
    errors.extend(graph_errors)
    stats["route_graph_errors"] = len(graph_errors)

    result={"package_root":str(ROOT),"passed":not errors,"errors":errors,"warnings":warnings,"statistics":stats}
    if args.json: print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print("QHSJ AIGC 全能影视 离线包结构审计")
        print("状态："+("通过" if result["passed"] else "未通过"))
        for k,v in stats.items(): print(f"- {k}: {v}")
        if errors:
            print("\n错误：")
            for x in errors: print("  [ERROR] "+x)
        if warnings:
            print("\n警告：")
            for x in warnings: print("  [WARN] "+x)
    return 0 if result["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
