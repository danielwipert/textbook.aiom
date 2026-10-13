#!/usr/bin/env python3
"""Assemble the Chapter 3 scoped re-review package, one file.

The scoped re-run matrix (CLAUDE.md section 4): body prose edited after the
review re-runs the review FOR THE CHANGED PASSAGES. Sitting 3 (commit 1eca9c9,
plus the paragraph split in ae64f47) edited body prose after Stage 4 passed,
so this package carries every block that differs from the pre-sitting text,
before and after, inside the whole current chapter for context.

One-off for Chapter 3, kept beside its output so the step can be rebuilt. The
general tool is on the fix-between-chapters list as review_package.py.

Run from the repo root:
    python3 Drafts/Ch03_A_Science_and_Its_Discipline/02_Stage4_Review/build_scoped_review.py
"""
import difflib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import copyedit_export as ce  # noqa: E402

HERE = Path(__file__).resolve().parent
LIVE = "Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html"
BASE = "966b7b9"          # the last commit before sitting 3 touched the text
OUT = HERE / "AIOM_Ch03_Review_scoped_package.md"
REFERENCE = HERE / "ch03_reference_extract.md"

PLACE_KINDS = {"SLOT", "CASE TITLE", "SECTION HEAD", "PROBLEM TITLE"}
SKIP_KINDS = {"FIGURE TEXT"}


def blocks_at(rev):
    if rev is None:
        r = ce.extract(str(ROOT / LIVE))
    else:
        raw = subprocess.run(["git", "show", f"{rev}:{LIVE}"], cwd=ROOT, check=True,
                             capture_output=True, text=True).stdout
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                         encoding="utf-8") as f:
            f.write(raw)
        r = ce.extract(f.name)
    return r[0] if isinstance(r, tuple) else r


def place(blocks, i):
    for j in range(i, -1, -1):
        if blocks[j]["kind"] in PLACE_KINDS:
            return blocks[j]["text"]
    return "Chapter opening"


def main():
    old, new = blocks_at(BASE), blocks_at(None)
    a = [b["text"] for b in old]
    b = [b["text"] for b in new]
    changes = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        before = [old[k] for k in range(i1, i2) if old[k]["kind"] not in SKIP_KINDS]
        after = [new[k] for k in range(j1, j2) if new[k]["kind"] not in SKIP_KINDS]
        if not before and not after:
            continue
        where = place(new, j1 if j1 < len(new) else len(new) - 1)
        changes.append((where, before, after))

    parts = []
    for n, (where, before, after) in enumerate(changes, 1):
        kinds = sorted({x["kind"] for x in before + after})
        lines = [f"### P{n}. {where}  [{', '.join(kinds)}]", ""]
        lines += ["BEFORE:", ""] + [f"> {x['text']}" for x in before] + [""]
        lines += ["AFTER:", ""] + [f"> {x['text']}" for x in after] + [""]
        parts.append("\n".join(lines))
    changed = "\n".join(parts)

    chapter = "\n\n".join(f"[{x['kind']}] {x['text']}" for x in new
                          if x["kind"] not in SKIP_KINDS)
    reference = REFERENCE.read_text(encoding="utf-8")

    body = PROMPT.format(n=len(changes)) + (
        f"\n<<<<< BEGIN DOCUMENT 1: THE {len(changes)} CHANGED PASSAGES, BEFORE AND AFTER >>>>>\n\n"
        f"{changed}\n<<<<< END DOCUMENT 1 >>>>>\n"
        "\n<<<<< BEGIN DOCUMENT 2: CHAPTER 3 AS IT NOW STANDS >>>>>\n\n"
        f"{chapter}\n\n<<<<< END DOCUMENT 2 >>>>>\n"
        "\n<<<<< BEGIN DOCUMENT 3: REFERENCE EXTRACT >>>>>\n\n"
        f"{reference.strip()}\n\n<<<<< END DOCUMENT 3 >>>>>\n"
        "\nEND OF PACKAGE. Now produce your review in the format given in Part 2.\n")
    for bad in ("\u2014", "\u2013"):
        assert bad not in body, "a dash in the package"
    OUT.write_text(body, encoding="utf-8")
    print(f"wrote {OUT.name}: {len(changes)} changed passages, {len(body.split())} words")


PROMPT = """# Scoped review package: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file: your instructions, the required output format,
and all the material, between BEGIN and END markers in Part 3. Do not ask for
other files. Read the whole file before you begin.

---

## PART 1. Your task

You are reviewing part of one chapter of an academic textbook for business
graduate students, *AI Operations Management*. The whole chapter was reviewed
earlier and passed. Since then, a fact check led to {n} passages being changed,
mostly to make sentences claim no more than their sources or the book's formal
registry support. **Review only those {n} passages.** The rest of the chapter is
there for context and is out of scope.

- **Document 1** gives each changed passage BEFORE and AFTER, labelled with its
  section. Some passages are footnote glosses, table cells, a figure caption, or
  a key-term entry rather than body paragraphs.
- **Document 2** is the whole chapter as it now stands, as tagged blocks.
- **Document 3** is the reference extract: what the chapter must do, and the
  seven craft criteria C1 to C7.

### Three warnings

1. **The narrowing is settled.** Each change was ruled by the author for
   accuracy. A finding that a passage should claim more, or return to its
   BEFORE wording, will be discarded. A fix you propose must keep what the
   AFTER wording claims and does not claim. Fixing HOW it says it is in scope.
2. **Formal statements are not prose.** Statements of theorems, lemmas and
   propositions (THM-004, LEM-021, PROP-043 and so on) and their names are
   verbatim from the registry. Judge the prose around them.
3. **Sourcing is out of scope.** The fact check has closed.

### What to look for, in each changed passage

**Section A, structure.** Does the change disturb what its slot or section is
for? Does it front-run something a later chapter is meant to reveal, or add a
promise the chapter does not keep? Does an added sentence repeat what a nearby
sentence already says?

**Section B, teaching.** Read each AFTER passage with its neighbors in Document
2. Where does the edit leave a seam: a repeated word or idea, a pronoun whose
referent changed, a sentence that no longer follows from the one before, a
paragraph that now ends weakly? Would a sceptical, busy MBA reader stall here?

**Section C, voice and craft.** Grade the changed passages against C1 to C7.
Quote the WEAKEST changed passage for each criterion. If a criterion is met
everywhere, say so in one row and quote the passage that comes closest to
failing it. House rules: no em or en dashes, no contractions, no rhetorical
questions, no hedging ("perhaps", "some argue"); accurate qualification is not
hedging.

Read adversarially. A review that finds nothing will be discarded as
confirmatory; one that invents a defect will waste a round. Mark the
difference with the Type column.

---

## PART 2. Required output format

Reply in Markdown, using exactly this structure and nothing else. No preamble.

```
# Scoped review: Chapter 3

## Section A: Structure
## Section B: Teaching
## Section C: Voice and craft

## Findings

| ID | Sec | Passage (P-number) | Quote (exact, under 30 words) | What is wrong | Type | Severity | Suggested fix |
|---|---|---|---|---|---|---|---|
| SR-1 | B | P3 | "..." | ... | defect | medium | ... |

## Fix first
1. SR-n: one line on why
```

Rules for the table:

- **ID**: SR-1, SR-2, and so on, across all three sections.
- **Sec**: A, B or C. For Section C, start "What is wrong" with the criterion
  (C1 to C7), and give every criterion at least one row.
- **Quote**: copied exactly from the AFTER text in Document 1.
- **Type**: one of `defect`, `deliberate`, `noise`.
- **Severity**: one of `high`, `medium`, `low`.
- **Suggested fix**: exact replacement wording that keeps the AFTER claim.
- Under each Section heading, at most five sentences of overall judgment.
- Do not use em dashes or en dashes anywhere in your reply.

---

## PART 3. The material
"""


if __name__ == "__main__":
    main()
