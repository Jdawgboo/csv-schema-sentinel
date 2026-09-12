"""Infer and validate simple CSV schemas."""
from __future__ import annotations
import csv
from collections import defaultdict


def kind(value: str) -> str:
    if value == "": return "empty"
    if value.lower() in {"true", "false"}: return "bool"
    try: int(value); return "int"
    except ValueError: pass
    try: float(value); return "float"
    except ValueError: return "str"


def infer(rows: list[dict[str, str]]) -> dict[str, str]:
    observed: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        for key, value in row.items():
            if kind(value) != "empty": observed[key].add(kind(value))
    result = {}
    for key, values in observed.items():
        result[key] = "float" if "float" in values else "int" if values == {"int"} else "bool" if values == {"bool"} else "str"
    return result


def validate(rows: list[dict[str, str]], expected: dict[str, str]) -> list[str]:
    errors = []
    for index, row in enumerate(rows, 1):
        for key, expected_kind in expected.items():
            if key not in row: errors.append(f"row {index}: missing {key}")
            elif row[key] and kind(row[key]) not in ({expected_kind, "int"} if expected_kind == "float" else {expected_kind}): errors.append(f"row {index}: {key} is not {expected_kind}")
    return errors


if __name__ == "__main__":
    import argparse, json
    parser = argparse.ArgumentParser(); parser.add_argument("csv_file"); args = parser.parse_args()
    with open(args.csv_file, newline="", encoding="utf-8") as handle: print(json.dumps(infer(list(csv.DictReader(handle))), indent=2, sort_keys=True))
