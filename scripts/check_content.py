#!/usr/bin/env python3
"""check_content.py — content audit (C1-C9). Skeleton; fills in stage G."""
import re, sys, os, difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []

def read(p):
    try: return Path(p).read_text(encoding="utf-8")
    except: return ""

def check_deprecated():
    """C9: files with deprecation marker must have 替代:"""
    for md in ROOT.rglob("*.md"):
        if ".git" in str(md) or "node_modules" in str(md): continue
        txt = read(md)
        # Only flag actual deprecation markers: blockquote DEPRECATED or Chinese 已废弃
        has_marker = bool(re.search(r'(^|\n)>\s*DEPRECATED|已废弃', txt, re.IGNORECASE))
        if has_marker:
            if "替代:" not in txt and "替代：" not in txt:
                errors.append(f"{md.relative_to(ROOT)}:0: deprecated without 替代:")

def check_gate_phrases():
    """C2: workflows with 跳过/可选 + P0/资产锁定 -> error"""
    for wf in (ROOT / "workflows").rglob("WORKFLOW.md"):
        txt = read(wf)
        for i, line in enumerate(txt.split("\n"), 1):
            if re.search(r'(跳过|可选|可略过)', line) and re.search(r'(P0|资产锁定|Asset-First)', line):
                if "禁止" not in line and "违反时" not in line:
                    errors.append(f"{wf.relative_to(ROOT)}:{i}: gate conflict: {line.strip()[:60]}")

def check_numbers():
    """C6: 29/16/303 consistency"""
    import json
    manifest = json.loads(read(ROOT / "manifest.json"))
    dc = manifest["declared_counts"]
    for md in ROOT.rglob("*.md"):
        if ".git" in str(md) or "scan-baseline" in str(md) or "node_modules" in str(md): continue
        txt = read(md)
        for wrong in [f"{dc['capabilities']-1} 能力", f"{dc['capabilities']+1} 能力",
                      f"{dc['workflows']-1} 工作流", f"{dc['workflows']+1} 工作流",
                      f"{dc['references']-1} 知识库", f"{dc['references']+1} 知识库"]:
            if wrong in txt:
                errors.append(f"{md.relative_to(ROOT)}:0: inconsistent number: {wrong}")

def check_terms():
    """C5: forbidden terms from glossary"""
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
                errors.append(f"{md.relative_to(ROOT)}:0: forbidden term: {a}")
                break

def check_dangling_refs():
    """C8: dangling markdown refs"""
    link_re = re.compile(r'\[[^\]]+\]\(([^)]+\.md[^)]*)\)')
    code_re = re.compile(r'`([^`]+\.md)`')
    glob_chars = set("*?{}[]")
    for md in ROOT.rglob("*.md"):
        if ".git" in str(md) or "node_modules" in str(md): continue
        txt = read(md)
        for m in link_re.findall(txt) + code_re.findall(txt):
            if any(ch in m for ch in glob_chars):
                continue  # intentional glob/pattern reference, not a concrete file
            ref = m.split("#")[0]
            if not ref:
                continue
            target = (md.parent / ref).resolve()
            if not target.exists():
                errors.append(f"{md.relative_to(ROOT)}:0: dangling: {m}")

def check_duplicates():
    """C4: duplicate paragraphs. Fast hash-based detection."""
    import hashlib
    para_map = {}  # hash -> [(file, para)]
    for md in ROOT.rglob("*.md"):
        if ".git" in str(md) or "node_modules" in str(md): continue
        txt = read(md)
        for para in re.split(r'\n\s*\n', txt):
            para = para.strip()
            if len(para) > 40 and not para.startswith("#") and not para.startswith("|"):
                h = hashlib.md5(para.encode("utf-8")).hexdigest()
                para_map.setdefault(h, []).append((str(md.relative_to(ROOT)), para))
    dups = []
    for h, occurrences in para_map.items():
        files = set(o[0] for o in occurrences)
        if len(files) > 1:
            for i in range(len(occurrences)):
                for j in range(i+1, len(occurrences)):
                    if occurrences[i][0] != occurrences[j][0]:
                        dups.append((occurrences[i][0], occurrences[j][0], 1.0, occurrences[i][1][:60]))
    with open(ROOT / "docs" / "content-duplicates.md", "w", encoding="utf-8") as f:
        f.write("# 重复段落候选 (C4)\n\n")
        if dups:
            f.write("| 文件1 | 文件2 | 相似度 | 片段 |\n|---|---|---|---|\n")
            for a, b, r, p in dups[:100]:
                f.write(f"| {a} | {b} | {r:.2f} | {p} |\n")
        else:
            f.write("未发现重复段落\n")
    if dups:
        warnings.append(f"C4: {len(dups)} duplicate paragraph pairs (see docs/content-duplicates.md)")

check_deprecated()
check_gate_phrases()
check_numbers()
check_terms()
check_dangling_refs()
check_duplicates()

for w in warnings:
    print(f"WARNING: {w}")
if errors:
    for e in errors:
        print(e)
    print(f"\nFAILED: {len(errors)} errors")
    sys.exit(1)
else:
    print("PASS: content checks passed")
    sys.exit(0)
