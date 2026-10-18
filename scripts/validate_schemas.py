#!/usr/bin/env python3
"""validate_schemas.py — validate all JSON schemas and data files."""
import json, sys
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parent.parent
errors = []

# 1. Validate all schemas/*.schema.json against meta-schema
for s in (ROOT / "schemas").glob("*.schema.json"):
    try:
        schema = json.loads(s.read_text(encoding="utf-8"))
        jsonschema.Draft7Validator.check_schema(schema)
    except Exception as e:
        errors.append(f"{s.name}: invalid schema: {e}")

# 2. Validate manifest.json
try:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    man_schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(manifest, man_schema)
except Exception as e:
    errors.append(f"manifest.json: {e}")

# 3. Validate routes.json
try:
    routes = json.loads((ROOT / "routes.json").read_text(encoding="utf-8"))
    route_schema = json.loads((ROOT / "schemas" / "route.schema.json").read_text(encoding="utf-8"))
    for r in routes:
        jsonschema.validate(r, route_schema)
except Exception as e:
    errors.append(f"routes.json: {e}")

# 4. Validate capability inputs/outputs schemas
for cap in (ROOT / "capabilities").iterdir():
    if not cap.is_dir(): continue
    for sname in ["inputs.schema.json", "outputs.schema.json"]:
        sp = cap / sname
        if not sp.exists():
            errors.append(f"{cap.name}/{sname}: missing")
            continue
        try:
            schema = json.loads(sp.read_text(encoding="utf-8"))
            jsonschema.Draft7Validator.check_schema(schema)
        except Exception as e:
            errors.append(f"{cap.name}/{sname}: {e}")

if errors:
    for e in errors:
        print(e)
    print(f"\nFAILED: {len(errors)} errors")
    sys.exit(1)
else:
    print("PASS: all schemas valid")
    sys.exit(0)
