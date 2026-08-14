#!/usr/bin/env python3
"""
Claim preservation. Does the chapter still say what the fact checks ruled it must
say, and does it still not say what they ruled out?

THE FAILURE THIS ANSWERS. A ruled claim narrowing does not survive a copy edit,
and nothing mechanical sees it go. SF8, SF9 and SF10 were reverted during the
Stage 6 rounds of 2026-08-08 with every date and figure intact, so no check on
values could detect them. FC2 repeated the shape on a second vendor, and the case
bank carried the pre-SF3 wording for seventy days. Five instances of one failure,
and until this file existed no gate could see any of them.

WHY IT READS A LEDGER RATHER THAN THE REGISTER NOTES. Both were tried. The notes
use the apostrophe as delimiter and as possessive at once, so `the team's
heaviest users` inside a quotation cannot be parsed by any delimiter rule. Worse,
a note holds SUPERSEDED ruled forms beside the current one: the note on
altman-2025-pro carries two sentences introduced by "the sentence now reads", the
SF1 form and the later form that replaced it. Treating every "now reads" as
required would demand a sentence the chapter is right not to contain. The notes
record how the text got here. AIOM_Claim_Ledger.md states where it must be now.

Run standalone, or through web gate W14 which calls check().
"""

import html
import os
import re
import sys

LEDGER = "AIOM_Claim_Ledger.md"

# A ruling block opens with "### <ID> :: ..." and a chapter section with "## ChNN".
CHAPTER_RE = re.compile(r"^##\s+(Ch\d+)\s*$", re.M)
RULING_RE = re.compile(r"^###\s+(\S+)\s*::\s*(.*)$")
FIELD_RE = re.compile(r"^-\s+(REQUIRED|FORBIDDEN|REVIEW|REVERSES-IF|SOURCE-KEY|DRIFT-FOUND[^:]*):\s*(.*)$")


def normalize(text):
    """Fold a chapter or a ledger line to one comparable form.

    Markup out, entities decoded, typographic quotes folded to straight, runs of
    whitespace collapsed. Case is PRESERVED: these are quotations, and a ruling
    that turns on a capital is a ruling this check should still see.
    """
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    # The dashes are escapes rather than literals: standing rule 1 bans an em
    # dash anywhere in this repository, and a normalization table is not an
    # exemption. \u2014 is the em dash, \u2013 the en dash.
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'),
                 ("\u201d", '"'), ("\u2014", "-"), ("\u2013", "-")):
        text = text.replace(a, b)
    return " ".join(text.split())


def chapter_body(path):
    """The chapter's prose, WITHOUT its Decision 51 source register.

    The register quotes both the ruled sentences and the withdrawn ones, so a
    check run over the whole file would find every FORBIDDEN string sitting in
    the note that records its withdrawal and fail every chapter always. The split
    is the same one the privacy sweep used: the register opens at the paragraph
    naming Decision 51.
    """
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    cut = next((i for i, l in enumerate(lines) if "Decision 51" in l), len(lines))
    return normalize("\n".join(lines[:cut]))


def load_ledger(path=LEDGER):
    """Parse the ledger into {chapter_id: [ruling, ...]}."""
    text = open(path, encoding="utf-8").read()
    out, chapter, ruling = {}, None, None
    for line in text.split("\n"):
        m = CHAPTER_RE.match(line)
        if m:
            chapter = m.group(1)
            out.setdefault(chapter, [])
            ruling = None
            continue
        m = RULING_RE.match(line)
        if m and chapter:
            ruling = {"id": m.group(1), "head": m.group(2), "required": [],
                      "forbidden": [], "review": []}
            out[chapter].append(ruling)
            continue
        m = FIELD_RE.match(line)
        if m and ruling is not None:
            field, value = m.group(1), m.group(2).strip()
            if field == "REQUIRED":
                ruling["required"].append(value)
            elif field == "FORBIDDEN":
                ruling["forbidden"].append(value)
            elif field == "REVIEW":
                ruling["review"].append(value)
    return out


def chapter_id_for(path):
    """ChNN from a chapter path, e.g. Drafts/Ch01_The_Category_Error/... -> Ch01."""
    m = re.search(r"(Ch\d+)", os.path.abspath(path))
    return m.group(1) if m else None


def _failures(chapter_path, ledger_path=LEDGER, chapter=None):
    """[(ruling_id, message)] for every ruling this chapter breaks.

    check() wants the messages and amend.py --rule wants the identities, and both
    must be answers to ONE evaluation. Deriving the id set by regexing check()'s
    prose would create a second reader of the same question, which is how this
    repository's recurring defect starts. The id is None for the setup failures,
    which belong to no ruling.
    """
    chapter = chapter or chapter_id_for(chapter_path)
    if chapter is None:
        return [(None, "W14: cannot infer a chapter id from %s" % chapter_path)]
    if not os.path.exists(ledger_path):
        return [(None, "W14: %s not found; the claim ledger is required"
                 % ledger_path)]

    ledger = load_ledger(ledger_path)
    if chapter not in ledger:
        # A chapter with no rulings yet is not a failure. A chapter whose
        # section was DELETED from the ledger would look identical, which is why
        # the caller reports the count it checked.
        return []

    body = chapter_body(chapter_path)
    fails = []
    for r in ledger[chapter]:
        for want in r["required"]:
            if normalize(want) not in body:
                fails.append((r["id"],
                    "W14: %s %s: REQUIRED text is missing from %s. A ruled "
                    "narrowing has been reverted or reworded.\n        wanted: %r"
                    % (chapter, r["id"], os.path.basename(chapter_path), want)))
        for bad in r["forbidden"]:
            if normalize(bad) in body:
                fails.append((r["id"],
                    "W14: %s %s: FORBIDDEN text is present in %s. A withdrawn "
                    "claim has returned.\n        found: %r"
                    % (chapter, r["id"], os.path.basename(chapter_path), bad)))
    return fails


def check(chapter_path, ledger_path=LEDGER, chapter=None):
    """Returns a list of failure strings. Empty list means the chapter holds."""
    return [m for _, m in _failures(chapter_path, ledger_path, chapter)]


def broken_rulings(chapter_path, ledger_path=LEDGER, chapter=None):
    """The IDs of the rulings this chapter currently breaks, sorted.

    THIS SEES ONLY WHAT THE GATE SEES, which is the whole caveat on amend.py
    --rule. A ruling is broken here when a REQUIRED string is absent or a
    FORBIDDEN string is present, both matched literally. A withdrawn claim
    restated in DIFFERENT WORDS breaks the ruling in substance and appears in
    neither set, so it is never retired and never reported. That is not a defect
    in this function; it is the reason SF8 exists as a separate entry from SF2,
    and the reason REVIEW rulings say they are enforced by reading.
    """
    return sorted({rid for rid, _ in _failures(chapter_path, ledger_path, chapter)
                   if rid})


def summary(chapter_path, ledger_path=LEDGER, chapter=None):
    """How much was actually checked. A gate that checked nothing must say so."""
    chapter = chapter or chapter_id_for(chapter_path)
    ledger = load_ledger(ledger_path) if os.path.exists(ledger_path) else {}
    rulings = ledger.get(chapter, [])
    # ONLY RULINGS THAT STILL ENFORCE SOMETHING ARE COUNTED. A ruling Dan has
    # superseded keeps its block in the ledger as history, with its fields
    # renamed out of enforcement. Counting it here would report protection that
    # is no longer in force, which is the precise failure this whole gate exists
    # to prevent, committed by the gate's own progress line.
    live = [r for r in rulings if r["required"] or r["forbidden"] or r["review"]]
    return (len(live),
            sum(len(r["required"]) for r in live),
            sum(len(r["forbidden"]) for r in live),
            sum(len(r["review"]) for r in live))


def main(argv):
    if len(argv) < 2:
        print("usage: claimcheck.py <chapter.html> [--ledger PATH]")
        return 2
    path = argv[1]
    ledger_path = LEDGER
    if "--ledger" in argv:
        ledger_path = argv[argv.index("--ledger") + 1]

    chapter = chapter_id_for(path)
    n_rul, n_req, n_forb, n_rev = summary(path, ledger_path, chapter)
    fails = check(path, ledger_path, chapter)

    print("claim preservation, %s" % (chapter or "unknown chapter"))
    print("  %d ruling(s): %d required, %d forbidden, %d review-only"
          % (n_rul, n_req, n_forb, n_rev))
    if n_rul == 0:
        print("  NO RULINGS FOR THIS CHAPTER. This check measured nothing.")
    for r in load_ledger(ledger_path).get(chapter, []):
        for note in r["review"]:
            print("  REVIEW (never mechanical) %s: %s" % (r["id"], note[:96]))
    print()
    if fails:
        for f in fails:
            print("  " + f)
        print("\nCLAIM CHECK FAILED")
        return 1
    print("CLAIM CHECK PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
