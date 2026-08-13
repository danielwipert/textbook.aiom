#!/usr/bin/env python3
"""ledger.py  |  read AIOM_Continuity_Ledger.md as data

The ledger is the G3 record: terms owned per chapter, forward references and
whether they are paid, registry glosses, and a chapter log. `continuity.py`
writes it at Stage 9 and gate G3 checks against it.

This module only READS it, so the web edition's glossary is the same record the
continuity gate enforces rather than a second list assembled by scraping chapter
HTML. That matters twice over. It is one source of truth, and it is automatically
correct about scope: entries are appended at lock, so a term can only reach the
site from a chapter that Decision 64 already permits publishing.

Nothing here writes to the ledger. Appending is `continuity.py --update` at
Stage 9, and CLAUDE.md is explicit that entries are never edited to make
something pass.

    from ledger import load_ledger
    led = load_ledger()
    led["terms"]     # [{term, owner, definition}]
    led["forward"]   # [{frm, to, promise, status}]
    led["registry"]  # [{object, first_used, gloss}]
    led["log"]       # [{chapter, locked, terms, forward, objects}]
"""
import os
import re
import sys

LEDGER = "AIOM_Continuity_Ledger.md"

SECTION_RE = re.compile(r"^## \d+\.\s*(.+?)\s*$")
ROW_RE = re.compile(r"^\|(.+)\|\s*$")

# (key, field names, the table's own header labels).
#
# THE HEADER LABELS ARE CARRIED EXPLICITLY AND THAT IS NOT REDUNDANT. The first
# draft dropped a header row by testing the first cell against the first FIELD
# name, which works only while the two are spelled the same. "From" is a Python
# keyword so the field is `frm`, the test failed, and the header row
# "From | To | Promise | Status" was parsed as a sixth forward reference and
# would have been published on the site as one.
SECTIONS = {
    "Terms owned": ("terms", ["term", "owner", "definition"],
                    ["Term", "Owner", "Definition as given"]),
    "Forward references": ("forward", ["frm", "to", "promise", "status"],
                           ["From", "To", "Promise", "Status"]),
    "Registry glosses": ("registry", ["object", "first_used", "gloss"],
                         ["Object", "First used", "Gloss as given"]),
    "Chapter log": ("log", ["chapter", "locked", "terms", "forward", "objects"],
                    ["Chapter", "Locked", "Terms owned", "Forward refs made",
                     "Registry objects"]),
}


def _cells(line):
    return [c.strip() for c in ROW_RE.match(line).group(1).split("|")]


def load_ledger(path=LEDGER):
    """Parse the ledger's tables. Header and separator rows are skipped."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found; run from the repository root")
    out = {key: [] for key, _, _ in SECTIONS.values()}
    current = None
    for line in open(path, encoding="utf-8").read().split("\n"):
        m = SECTION_RE.match(line)
        if m:
            current = SECTIONS.get(m.group(1))
            continue
        if current is None or not ROW_RE.match(line):
            continue
        cells = _cells(line)
        key, fields, headers = current
        if len(cells) != len(fields):
            continue
        # Drop the table's header row and its --- separator. The header is
        # matched against the LABELS the ledger actually prints, not against the
        # Python field names, which differ wherever a field name would collide
        # with a keyword.
        if cells == headers or re.fullmatch(r"[-: ]+", cells[0]):
            continue
        out[key].append(dict(zip(fields, cells)))
    return out


def chapter_of(owner):
    """The chapter number in an owner or first-used cell. '1' and 'Ch1' both."""
    m = re.search(r"(\d+)", owner or "")
    return int(m.group(1)) if m else None


def check(led):
    """Structural checks. A ledger that stops parsing must not read as empty."""
    fails = []
    if not led["terms"]:
        fails.append("no terms parsed from the ledger")
    if not led["log"]:
        fails.append("no chapter log entries parsed from the ledger")
    for t in led["terms"]:
        if chapter_of(t["owner"]) is None:
            fails.append(f"term {t['term']!r} has no parseable owning chapter")
        if not t["definition"]:
            fails.append(f"term {t['term']!r} has no definition")
    # The log states how many terms each locked chapter owns. If the terms table
    # and the log disagree, one of them is stale and the glossary would be wrong
    # without anything reporting it.
    for row in led["log"]:
        n = chapter_of(row["chapter"])
        claimed = int(row["terms"]) if row["terms"].isdigit() else None
        actual = sum(1 for t in led["terms"] if chapter_of(t["owner"]) == n)
        if claimed is not None and claimed != actual:
            fails.append(f"chapter {n} log claims {claimed} terms owned, "
                         f"the terms table holds {actual}")
    return fails


if __name__ == "__main__":
    led = load_ledger()
    for key in ("terms", "forward", "registry", "log"):
        print(f"{key}: {len(led[key])}")
    for t in led["terms"]:
        print(f"   {t['term']} (Ch{chapter_of(t['owner'])})")
    fails = check(led)
    print("\nLEDGER " + ("OK" if not fails else "FAILED"))
    for f in fails:
        print("   " + f)
    sys.exit(0 if not fails else 1)
