# -*- coding: utf-8 -*-
"""Rebuild every ME 492 question bank, in order.

The steps depend on each other, so run this rather than the pieces:

  1. build_ai_questions.py    writes ai-generated-100.json
  2. build_site_questions.py  writes site-extracted-48.json
  3. tabulate_compiled.py     puts the data tables into compiled.json
  4. enrich_explanations.py   adds the hooks and the calculation workings

Step 4 must come last. The first three write the explanation field, and step 4
is what adds the hook to all three files.
"""
import subprocess
import sys

STEPS = [
    "build_ai_questions.py",
    "build_site_questions.py",
    "tabulate_compiled.py",
    "enrich_explanations.py",
]

for step in STEPS:
    print("\n=== %s ===" % step)
    result = subprocess.run([sys.executable, step])
    if result.returncode != 0:
        sys.exit("%s failed" % step)
print("\nall banks rebuilt")
