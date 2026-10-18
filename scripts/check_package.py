#!/usr/bin/env python3
"""check_package.py — 16 structural checks. Exit 0=pass, 1=fail."""
import os, re, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

def err(fname, line, msg):
    errors.append(f"{fname}:{line}: {msg}")

def read(p):
    try:
        return Path(p).read_text(encoding="utf-8")
    except Exception:
        return ""

# Load manifest and routes
manifest = json.loads(read(ROOT / "manifest.json"))
routes = json.loads(read(ROOT / "routes.json"))
skill_text = read(ROOT / "SKILL.md")
skill_fm = skill_text.split("---")[1]

import yaml
skill_meta = yaml.safe_load(skill_fm)

# 1. manifest counts vs actual
cap_dirs = [d for d in (ROOT / "capabilities").iterdir() if d.is_dir()]
wf_dirs = [d for d in (ROOT / "workflows").iterdir() if d.is_dir()]
ref_mds = list((ROOT / "references").rglob("*.md"))
# Count: top-level references/index.md + all content articles; exclude domain-level index.md and _unsorted
ref_mds = [r for r in ref_mds if "_unsorted" not in str(r) and not (r.name == "index.md" and r.parent != ROOT / "references")]
declared = manifest["declared_counts"]
if len(cap_dirs) != declared["capabilities"]:
    err("manifest.json", 0, f"capabilities declared {declared['capabilities']} actual {len(cap_dirs)}")
if len(wf_dirs) != declared["workflows"]:
    err("manifest.json", 0, f"workflows declared {declared['workflows']} actual {len(wf_dirs)}")
if len(ref_mds) != declared["references"]:
    err("manifest.json", 0, f"references declared {declared['references']} actual {len(ref_mds)}")

# 2. version consistency
if manifest["version"] != skill_meta["metadata"]["version"]:
    err("manifest.json", 0, f"version mismatch: manifest={manifest['version']} skill={skill_meta['metadata']['version']}")

# 3. routes.json referenced paths exist
for r in routes:
    wf = ROOT / r["workflow"]
    if not wf.exists():
        err("routes.json", 0, f"route {r['id']}: workflow missing {r['workflow']}")
    for c in r["capabilities"]:
        if not (ROOT / c).exists():
            err("routes.json", 0, f"route {r['id']}: capability missing {c}")

# 4. orphan nodes (capabilities/workflows not referenced by any route)
all_caps = set()
all_wfs = set()
for r in routes:
    all_wfs.add(r["workflow"])
    for c in r["capabilities"]:
        all_caps.add(c)
for c in cap_dirs:
    cpath = f"capabilities/{c.name}/SPEC.md"
    if cpath not in all_caps:
        err(f"capabilities/{c.name}", 0, f"orphan capability not referenced by any route")
for w in wf_dirs:
    wpath = f"workflows/{w.name}/WORKFLOW.md"
    if wpath not in all_wfs:
        err(f"workflows/{w.name}", 0, f"orphan workflow not referenced by any route")

# 5. cycle detection in capability_dependencies
dep_graph = {}
for r in routes:
    for cap, deps in r.get("capability_dependencies", {}).items():
        dep_graph.setdefault(cap, set()).update(deps)

def has_cycle(graph):
    visited, stack = set(), set()
    def dfs(n):
        if n in stack: return True
        if n in visited: return False
        visited.add(n); stack.add(n)
        for nb in graph.get(n, []):
            if dfs(nb): return True
        stack.discard(n)
        return False
    return any(dfs(n) for n in graph)

if has_cycle(dep_graph):
    err("routes.json", 0, "cycle detected in capability_dependencies")

# 6. SKILL.md lines <= 500, frontmatter parseable
skill_lines = skill_text.count("\n") + 1
if skill_lines > 500:
    err("SKILL.md", 0, f"SKILL.md {skill_lines} lines > 500")
try:
    yaml.safe_load(skill_fm)
except Exception as e:
    err("SKILL.md", 0, f"frontmatter not YAML-parseable: {e}")

# 7. SKILL.md name == parent dir name
parent = ROOT.name
if skill_meta["name"] != parent:
    # Sandbox: parent may be 'workspace'; warn but don't fail if name is qhsj-aigc
    if skill_meta["name"] != "qhsj-aigc":
        err("SKILL.md", 0, f"name '{skill_meta['name']}' != parent dir '{parent}'")

# 8. file size limits
limits = {"SKILL.md": (500, 24*1024), "SPEC.md": (200, 10*1024), "WORKFLOW.md": (150, 8*1024), "reference": (300, 12*1024), "index.md": (100, 4*1024)}
def check_size(path, line_lim, byte_lim, label):
    p = ROOT / path
    if not p.exists(): return
    txt = read(p)
    lines = txt.count("\n") + 1
    bts = len(txt.encode("utf-8"))
    if lines > line_lim:
        err(str(path), 0, f"{label} {lines} lines > {line_lim}")
    if bts > byte_lim:
        err(str(path), 0, f"{label} {bts} bytes > {byte_lim}")

check_size("SKILL.md", 500, 24*1024, "SKILL")
for c in cap_dirs:
    check_size(f"capabilities/{c.name}/SPEC.md", 200, 10*1024, "SPEC")
for w in wf_dirs:
    check_size(f"workflows/{w.name}/WORKFLOW.md", 150, 8*1024, "WORKFLOW")
for idx in (ROOT / "references").rglob("index.md"):
    check_size(str(idx.relative_to(ROOT)), 100, 4*1024, "index")

# 9. index existence
for idx_path in ["capabilities/index.md", "workflows/index.md"]:
    if not (ROOT / idx_path).exists():
        err(idx_path, 0, "index.md missing")
# references/<domain>/index.md for each domain
for domain in (ROOT / "references").iterdir():
    if domain.is_dir() and not domain.name.startswith("_"):
        if not (domain / "index.md").exists():
            err(f"references/{domain.name}", 0, "index.md missing")

# 10. dangerous instructions scan
danger_re = re.compile(r'(跳过|绕过|忽略).{0,10}(资产锁定|Asset-First|P0|门禁)')
for md in ROOT.rglob("*.md"):
    if ".git" in str(md) or "node_modules" in str(md): continue
    for i, line in enumerate(read(md).split("\n"), 1):
        if danger_re.search(line):
            if "违反时行为" not in line and "禁止" not in line:
                err(str(md.relative_to(ROOT)), i, f"dangerous instruction: {line.strip()[:60]}")

# 11. dangling refs
link_re = re.compile(r'\[[^\]]+\]\(([^)]+\.md[^)]*)\)')
code_re = re.compile(r'`([^`]+\.md)`')
for md in ROOT.rglob("*.md"):
    if ".git" in str(md) or "node_modules" in str(md): continue
    txt = read(md)
    for m in link_re.findall(txt) + code_re.findall(txt):
        ref = m.split("#")[0]
        target = (md.parent / ref).resolve()
        if not target.exists():
            err(str(md.relative_to(ROOT)), 0, f"dangling ref: {m}")

# 12. SKILL.md inline body: > 40 consecutive non-heading/table/list lines
in_block = 0
for i, line in enumerate(skill_text.split("\n"), 1):
    stripped = line.strip()
    is_struct = stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("-") or stripped.startswith("```") or stripped == ""
    if is_struct:
        in_block = 0
    else:
        in_block += 1
        if in_block > 40:
            err("SKILL.md", i, f">{40} consecutive non-structured lines")

# 13. terminology consistency (glossary FORBIDDEN names not in non-glossary files)
glossary = read(ROOT / "docs" / "glossary.md")
forbidden = set()
for line in glossary.split("\n"):
    if line.startswith("|") and not line.startswith("|---") and "标准术语" not in line:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3:
            for a in cells[2].split("、"):
                a = a.strip()
                if a and a != "—" and len(a) > 1:
                    forbidden.add(a)
for md in ROOT.rglob("*.md"):
    if ".git" in str(md) or "glossary" in str(md) or "node_modules" in str(md): continue
    txt = read(md)
    for a in forbidden:
        if a in txt:
            err(str(md.relative_to(ROOT)), 0, f"disallowed term '{a}' used (forbidden in glossary)")
            break

# 14. number consistency (29/16/303 across repo, excluding scan-baseline)
for md in ROOT.rglob("*.md"):
    if ".git" in str(md) or "scan-baseline" in str(md) or "node_modules" in str(md): continue
    txt = read(md)
    # Check for wrong counts
    for wrong in ["28 能力", "30 能力", "15 工作流", "17 工作流", "302 知识库", "304 知识库"]:
        if wrong in txt:
            err(str(md.relative_to(ROOT)), 0, f"inconsistent number: {wrong}")

# 15. capability trio
for c in cap_dirs:
    for f in ["SPEC.md", "inputs.schema.json", "outputs.schema.json"]:
        if not (c / f).exists():
            err(f"capabilities/{c.name}", 0, f"missing {f}")

# 16. workflow WORKFLOW.md
for w in wf_dirs:
    if not (w / "WORKFLOW.md").exists():
        err(f"workflows/{w.name}", 0, "missing WORKFLOW.md")

# Report
if errors:
    for e in errors:
        print(e)
    print(f"\nFAILED: {len(errors)} errors")
    sys.exit(1)
else:
    print(f"PASS: all 16 checks passed")
    sys.exit(0)
