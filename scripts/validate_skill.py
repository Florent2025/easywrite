#!/usr/bin/env python3
"""Structural validation for the Easywrite skill. Run in CI on every push/PR.

Checks (all must pass):
  1. SKILL.md has YAML frontmatter with `name:` (== easywrite) and `description:`.
  2. Every references/*.md linked from SKILL.md actually exists.
  3. All .claude-plugin/*.json parse as valid JSON.
  4. All assets/*.svg are well-formed XML.
  5. The six core reference lanes are present.
This is a lint, not a style judge; it never inspects prose quality.
"""
import glob
import json
import os
import re
import sys
import xml.dom.minidom as minidom
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def rel(p: str) -> str:
    return os.path.relpath(p, ROOT)


# 1. SKILL.md frontmatter
skill_path = ROOT / "SKILL.md"
if not skill_path.exists():
    errors.append("SKILL.md is missing")
    skill = ""
else:
    skill = skill_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    if not m:
        errors.append("SKILL.md: missing YAML frontmatter")
    else:
        fm = m.group(1)
        for key in ("name:", "description:"):
            if key not in fm:
                errors.append(f"SKILL.md frontmatter missing '{key}'")
        nm = re.search(r"^name:\s*(\S+)", fm, re.M)
        if nm and nm.group(1) != "easywrite":
            errors.append(f"SKILL.md name is '{nm.group(1)}', expected 'easywrite'")

# 2. referenced reference files exist
for ref in re.findall(r"\(references/([A-Za-z0-9_\-]+\.md)\)", skill):
    if not (ROOT / "references" / ref).exists():
        errors.append(f"SKILL.md links a missing file: references/{ref}")

# 3. JSON manifests parse
for j in glob.glob(str(ROOT / ".claude-plugin" / "*.json")):
    try:
        json.loads(Path(j).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"{rel(j)}: invalid JSON ({e})")

# 4. SVG assets well-formed
for s in glob.glob(str(ROOT / "assets" / "*.svg")):
    try:
        minidom.parseString(Path(s).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"{rel(s)}: malformed SVG ({e})")

# 5. core reference lanes present
for req in (
    "ai-tells-english.md",
    "ai-tells-chinese.md",
    "academic-discipline.md",
    "detector-science.md",
    "scoring-rubric.md",
    "examples.md",
):
    if not (ROOT / "references" / req).exists():
        errors.append(f"missing core lane: references/{req}")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print("All Easywrite skill checks passed.")
