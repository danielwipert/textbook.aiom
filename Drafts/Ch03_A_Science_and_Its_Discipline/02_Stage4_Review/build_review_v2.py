#!/usr/bin/env python3
"""Assemble the Stage 4 second-model review package for the redesigned Chapter 3.

Process v4, step 3 (Decision 77): ONE file carrying the instructions, the
output format and three documents (the chapter, the reference extract, the
Chapter 1 exemplar), read by a model that did not draft the chapter and
WITHOUT Claude's findings. Redesign of Decision 85; the 2026-10-06 package in
this folder reviewed the version that no longer exists.

prose_extract.py drops tables (fix-between-chapters list), so Table 3.1 is
patched in here from the chapter's own HTML, at its caption.

Run from the repo root:
    python3 Drafts/Ch03_A_Science_and_Its_Discipline/02_Stage4_Review/build_review_v2.py
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CH3 = ROOT / "Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html"
CH1 = ROOT / "Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html"
PLAN = ROOT / "Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_Plan.md"
OUT = HERE / "AIOM_Ch03_Review_v2_package.md"


def extract(path):
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "x.md"
        subprocess.run([sys.executable, str(ROOT / "prose_extract.py"), str(path),
                        "--out", str(out)], check=True, capture_output=True)
        return out.read_text(encoding="utf-8")


def cell(s):
    s = re.sub(r"<cite\b.*?</cite>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def table_md(src):
    t = re.search(r"<table\b.*?</table>", src, flags=re.S).group(0)
    rows = []
    for tr in re.findall(r"<tr>(.*?)</tr>", t, flags=re.S):
        rows.append([cell(c) for c in re.findall(r"<t[hd]>(.*?)</t[hd]>", tr, flags=re.S)])
    md = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
    md += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(md)


def chapter3():
    text = extract(CH3)
    cap = "Table 3.1. The four neighboring disciplines."
    assert text.count(cap) == 1, "Table 3.1 caption not found once"
    i = text.index(cap)
    return text[:i] + table_md(CH3.read_text(encoding="utf-8")) + "\n\n" + text[i:]


def lines(path, start, stop):
    """Lines from the first starting with `start` up to (not including) `stop`."""
    src = path.read_text(encoding="utf-8").split("\n")
    a = next(k for k, l in enumerate(src) if l.startswith(start))
    b = next(k for k in range(a + 1, len(src)) if src[k].startswith(stop))
    return "\n".join(src[a:b]).rstrip()


def reference():
    parts = [
        "# Chapter 3 review: reference extract",
        "",
        "Everything the reviewer grades against, extracted verbatim from the book's "
        "planning documents.",
        "",
        "## 1. Part I and Chapter 3, from the structure document",
        "",
        lines(ROOT / "AIOM_Structure_v1.md", "### Part I:", "### Part II:"),
        "",
        "## 2. Competency C4 and assessment 4, from the exit competencies",
        "",
        "Competency C4: " + numbered_after(ROOT / "AIOM_Exit_Competencies_v1.md", "4. Place"),
        "",
        "Assessment 4: " + numbered_after(ROOT / "AIOM_Exit_Competencies_v1.md", "4. Function audit"),
        "",
        "## 3. The approved chapter plan (version 2)",
        "",
        lines(PLAN, "## The chapter in one line", "## Decisions as put to Dan"),
        "",
        "## 4. The seven craft criteria, from the prose standard",
        "",
        lines(ROOT / "AIOM_Prose_Standard_v2.0.md", "## 26.", "## 27."),
    ]
    return "\n".join(parts)


def numbered_after(path, prefix):
    src = path.read_text(encoding="utf-8").split("\n")
    line = next(l for l in src if l.startswith(prefix))
    # Drop the trailing "(Decision 85 ... Was: ...)" history: the reviewer
    # grades against the competency, not its record.
    return re.sub(r"\s*\((?:Moved|Decision 85).*\)\s*$", "", line[3:])


HEAD = """# Review package: Chapter 3, "A Science and Its Discipline" (redesigned)

This is ONE self-contained file. Everything you need is inside it: your
instructions, the required output format, and all the material to review. Do not
ask for other files. Read the whole file before you begin.

---

## PART 1. Your task

You are reviewing one chapter of an academic textbook for business graduate
students, titled *AI Operations Management*. Chapter 3 is under review. It closes
Part I of the book. It has just been redesigned: an earlier version taught readers
to read formal claims from the book's underlying registry; this version keeps that
registry behind the scenes and teaches the discipline itself, its five functions
and its borders.

This file contains three documents, each between clear BEGIN and END markers in
Part 3 below:

- **Document 1: Chapter 3, the text under review.**
- **Document 2: the reference extract.** What the chapter is meant to do (its
  structure entry, its competency and assessment, its approved plan with the
  author's rulings) and the book's seven craft criteria, C1 to C7.
- **Document 3: Chapter 1 of the same book**, locked and published. It is the
  exemplar the craft standard was measured from. Calibrate against Chapter 1,
  not against how closely Chapter 3 resembles itself.

### Four warnings

1. **Sourcing is out of bounds.** Whether any figure or fact is true is checked
   separately, later, against the sources. You may still flag a sentence that
   makes an empirical claim with no visible support.
2. **Some wording is fixed elsewhere.** The one-sentence reading of THM-004 in
   Section 3.1 ("Once a deployment reaches scale ...") repeats Chapter 2's
   locked wording word for word. The opening case, Section 3.3, Section 3.4 and
   the Part I cumulative case were kept from the earlier version, which was
   fact-checked. You may judge all of them; say so if one no longer fits the
   redesigned chapter around it.
3. **Dated boxes are deliberate.** Perishable reporting (company names, dates,
   figures) is kept in dated boxes so that the body prose stays timeless. Judge
   whether each box earns its place, not whether the body should carry its facts.
4. **"No findings" is not an answer.** A review that says the chapter meets the
   criteria with no findings will be discarded as confirmatory.

The chapter is about 5,600 words, below the book's usual 6,000 to 7,500. The
author accepted that deliberately rather than pad it. If you find a real teaching
gap, say where; do not recommend length for its own sake.

### How to review

Review in three separate sections. In every section, do not report whether
something is met. Quote the WEAKEST evidence, say precisely what is wrong, and
say whether it is a defect, a deliberate choice serving something else, or noise.

**Section A, structure.** Does every slot serve the chapter's stated purpose?
Is competency C4 DELIVERED, meaning a reader could perform assessment 4 after
this chapter, unaided, on a real deployment the book has not worked? Does each
dated box show its function, or only sit beside it? Does the chapter front-run
anything a later chapter is meant to reveal? Does anything in the plan go
missing, and does anything appear that the plan does not call for? Now that the
registry is behind the scenes, does Section 3.1 still give the science enough
weight that the two-layer claim is believable?

**Section B, teaching.** Where would a sceptical, busy MBA-level reader stall,
lose the thread, or stop believing the argument? Judge clarity, pacing,
cognitive load, example fitness, and transitions. Name the single paragraph you
would cut first and the single place most in need of a concrete example.

**Section C, voice and craft.** One finding per criterion, C1 to C7, quoting the
weakest passage by section and the strongest, so your calibration is visible.

---

## PART 2. Required output format

Reply in Markdown, using exactly this structure and nothing else. No preamble.

```
# Second-model review: Chapter 3 (redesigned)

## Section A: Structure
## Section B: Teaching
## Section C: Voice and craft

## Findings

| ID | Sec | Where (section heading) | Quote (exact, under 30 words) | What is wrong | Type | Severity | Suggested fix |
|---|---|---|---|---|---|---|---|
| S-1 | A | ... | "..." | ... | defect | high | ... |

## Fix first
1. S-n: one line on why
2. S-n: ...
3. S-n: ...
```

Rules for the table:

- **ID**: S-1, S-2, and so on, numbered across all three sections.
- **Sec**: A, B or C. For Section C, start the "What is wrong" cell with the
  criterion (C1 to C7). Give every criterion at least one row.
- **Quote**: copied exactly from Document 1, so the author can find it.
- **Type**: one of `defect`, `deliberate`, `noise`.
- **Severity**: one of `high`, `medium`, `low`.
- Under each Section heading, write at most five sentences of overall judgment.
  The findings themselves go only in the table.
- Do not use em dashes or en dashes anywhere in your reply.

---

## PART 3. The material
"""


def main():
    body = [HEAD,
            "<<<<< BEGIN DOCUMENT 1: CHAPTER 3, UNDER REVIEW >>>>>", "",
            chapter3().strip(), "",
            "<<<<< END DOCUMENT 1 >>>>>", "",
            "<<<<< BEGIN DOCUMENT 2: REFERENCE EXTRACT >>>>>", "",
            reference(), "",
            "<<<<< END DOCUMENT 2 >>>>>", "",
            "<<<<< BEGIN DOCUMENT 3: CHAPTER 1, THE EXEMPLAR >>>>>", "",
            extract(CH1).strip(), "",
            "<<<<< END DOCUMENT 3 >>>>>", ""]
    text = "\n".join(body)
    for bad in ("—", "–"):
        assert bad not in text, f"a dash U+{ord(bad):04X} in the package"
    assert "Claude" not in text.split("## PART 3.")[0], "Claude named in the instructions"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.name}: {len(text.split())} words")


if __name__ == "__main__":
    main()
