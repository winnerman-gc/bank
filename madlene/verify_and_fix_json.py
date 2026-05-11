#!/usr/bin/env python3
"""Verify and repair Madlene MCQ JSON files.

This script validates the JSON syntax and a minimal schema for the two quiz
banks in this folder. If a file contains unescaped double quotes inside string
values, it will attempt to repair them and can optionally write the normalized
JSON back to disk.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_FILES = [
    "advanced_excel_mastery_200_mcqs_json.json",
    "advanced_excel_mastery_MCQs.json",
]


def escape_inner_quotes(line: str) -> str:
    """Escape raw quotes inside a single JSON string line.

    The quiz banks are formatted with one string value per line. For lines that
    are clearly JSON string literals, this converts internal unescaped quotes to
    escaped quotes while leaving already-escaped sequences intact.
    """

    line_ending = "\n" if line.endswith("\n") else ""
    stripped = line.rstrip("\n")

    # Match either:
    # - "key": "value"
    # - "value"
    # - "value",
    pattern = re.compile(r'^(?P<prefix>\s*(?:"[^"]+"\s*:\s*)?")(?P<body>.*)(?P<suffix>",?\s*)$')
    match = pattern.match(stripped)
    if not match:
        return line

    body = match.group("body")
    fixed_body = re.sub(r'(?<!\\)"', r'\\"', body)
    return f"{match.group('prefix')}{fixed_body}{match.group('suffix')}{line_ending}"


def repair_json_text(text: str) -> str:
    repaired_lines = [escape_inner_quotes(line) for line in text.splitlines(keepends=True)]
    return "".join(repaired_lines)


def load_json_with_repair(path: Path) -> tuple[Any, str, bool]:
    raw_text = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw_text), raw_text, False
    except json.JSONDecodeError:
        repaired_text = repair_json_text(raw_text)
        data = json.loads(repaired_text)
        return data, repaired_text, True


def validate_schema(data: Any, source_name: str) -> list[str]:
    errors: list[str] = []

    if not isinstance(data, list):
        return [f"{source_name}: top-level JSON value must be an array"]

    for index, item in enumerate(data):
        prefix = f"{source_name}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: each item must be an object")
            continue

        if not isinstance(item.get("question_number"), int):
            errors.append(f"{prefix}: question_number must be an integer")

        if not isinstance(item.get("question_text"), str):
            errors.append(f"{prefix}: question_text must be a string")

        options = item.get("options")
        if not isinstance(options, list) or not all(isinstance(option, str) for option in options):
            errors.append(f"{prefix}: options must be a list of strings")

        correct_answer = item.get("correct_answer")
        if not isinstance(correct_answer, list) or not all(isinstance(answer, str) for answer in correct_answer):
            errors.append(f"{prefix}: correct_answer must be a list of strings")

    return errors


def write_normalized_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify and repair Madlene quiz JSON files.")
    parser.add_argument(
        "files",
        nargs="*",
        default=DEFAULT_FILES,
        help="JSON files to check (defaults to the two Madlene question banks)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Write repaired/normalized JSON back to disk when parsing succeeds or is repaired",
    )
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    overall_ok = True

    for relative_name in args.files:
        path = (base_dir / relative_name).resolve()
        if not path.exists():
            print(f"{path.name}: missing")
            overall_ok = False
            continue

        try:
            data, repaired_text, was_repaired = load_json_with_repair(path)
        except json.JSONDecodeError as exc:
            print(f"{path.name}: JSON syntax error at line {exc.lineno}, column {exc.colno}: {exc.msg}")
            overall_ok = False
            continue

        schema_errors = validate_schema(data, path.name)
        if schema_errors:
            overall_ok = False
            for error in schema_errors:
                print(error)
            continue

        if args.fix:
            write_normalized_json(path, data)
            if was_repaired:
                print(f"{path.name}: repaired and normalized")
            else:
                print(f"{path.name}: validated and normalized")
        else:
            status = "repaired in-memory" if was_repaired else "valid"
            print(f"{path.name}: {status}, {len(data)} questions")

    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
