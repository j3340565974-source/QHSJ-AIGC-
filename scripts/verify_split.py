#!/usr/bin/env python3
"""verify_split.py — validate that split reference subdirectories have
a complete index pointing to all content parts, and no part exceeds limits.

Exit 0 = pass (100% coverage), 1 = fail.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
LINE_LIMIT = 300

errors = []
checked = 0
covered = 0

link_re = re.compile(r'\]\(([^)]+\.md[^)]*)\)')
code_re = re.compile(r'`([^`{}]+\.md)`')

for domain in REFS.iterdir():
    if not domain.is_dir() or domain.name.startswith("_"):
        continue
    for sub in domain.iterdir():
        if not sub.is_dir():
            continue
        index = sub / "index.md"
        if not index.exists():
            continue  # not a split dir
        checked += 1
        idx_text = index.read_text(encoding="utf-8")
        referenced = set()
        for m in link_re.findall(idx_text) + code_re.findall(idx_text):
            ref = m.split("#")[0]
            # Match by basename since links may use different relative paths
            referenced.add(Path(ref).name)
        content_files = sorted(
            p.name for p in sub.glob("*.md") if p.name != "index.md"
        )
        missing = [f for f in content_files if f not in referenced]
        if missing:
            errors.append(
                f"{sub.relative_to(ROOT)}: index.md missing links to {missing}"
            )
        else:
            covered += 1
        # line limit per part
        for f in content_files:
            p = sub / f
            lines = p.read_text(encoding="utf-8").count("\n") + 1
            if lines > LINE_LIMIT:
                errors.append(
                    f"{sub.relative_to(ROOT)}/{f}: {lines} lines > {LINE_LIMIT}"
                )

print(f"Split dirs checked: {checked}, fully covered: {covered}")
if errors:
    for e in errors:
        print(e)
    print(f"\nFAILED: {len(errors)} errors")
    sys.exit(1)
print("PASS: all split directories have complete index coverage")
sys.exit(0)
