#!/usr/bin/env python3
"""
aiom_registry.py  |  version 1.0  |  2026-07-30

Registry verification gate for the AIOM textbook.

A chapter carries the object ID directive and the inline text. This module
asserts that inline text against the AI Business Economics Locked Registry.
Comparison normalizes whitespace only: line wrapping and repeated spaces
collapse, everything else must match exactly.
"""

import re
import openpyxl

SHEET = "Locked_Registry"
LAYER_FOR = {"theorem": "Theorem", "lemma": "Lemma", "proposition": "Proposition"}
NEEDED = ("layer", "object_id", "object_name", "formal_statement", "status")


def norm(s):
    """Collapse every run of whitespace to one space. Nothing else changes."""
    return re.sub(r"\s+", " ", str(s or "")).strip()


def load_registry(path, sheet=SHEET):
    ws = openpyxl.load_workbook(path, data_only=True)[sheet]
    rows = list(ws.iter_rows(values_only=True))
    ix = {h: i for i, h in enumerate(rows[0])}
    missing = [c for c in NEEDED if c not in ix]
    if missing:
        raise KeyError(f"registry sheet is missing columns: {missing}")
    reg = {}
    for r in rows[1:]:
        oid = r[ix["object_id"]]
        if not oid:
            continue
        reg[str(oid).strip().upper()] = {
            "name":      r[ix["object_name"]],
            "statement": r[ix["formal_statement"]],
            "layer":     r[ix["layer"]],
            "status":    r[ix["status"]],
        }
    return reg


def _first_diff(a, b):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    lo = max(0, i - 45)
    return (f"at character {i}\n"
            f"       chapter:  ...{a[lo:i + 45]}\n"
            f"       registry: ...{b[lo:i + 45]}")


def verify(objects, reg, version="v1.3"):
    """Return a list of build-blocking errors. Empty means the chapter is clean."""
    errors = []
    for o in objects:
        oid, kind = o["id"], o["kind"]
        entry = reg.get(oid)
        if entry is None:
            errors.append(f"{oid} is not in the locked registry {version}")
            continue
        if norm(entry["layer"]).lower() != LAYER_FOR[kind].lower():
            errors.append(f"{oid} is a {norm(entry['layer'])} in the registry "
                          f"but is written as ::: {kind}")
        if norm(o["title"]) != norm(entry["name"]):
            errors.append(f"{oid} title drift\n"
                          f"       chapter:  {norm(o['title'])}\n"
                          f"       registry: {norm(entry['name'])}")
        a, b = norm(o["statement"]), norm(entry["statement"])
        if a != b:
            errors.append(f"{oid} statement drift {_first_diff(a, b)}")
    return errors
