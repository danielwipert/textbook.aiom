#!/usr/bin/env python3
"""Build the one-file external package for the review of Chapters 1 to 3.

Decision 83, scoped by Decision 87 (2026-10-19): one outside checker with web
access does two jobs at once. (1) A red-flag sweep: has any claim in the three
locked chapters been disproven in a major way? (2) Stronger evidence: verify
Claude's candidate list of major new reporting, find more, and say which claim
each supports or cuts against. Major outlets and first-party company material
only. The chapters are read as they PUBLISH: the typeset PDFs of each last lock.

Run from the repo root, after `web_build.py --site` has written build/web:
    python3 Drafts/Review_Decision83/build_package.py
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PDFS = [
    ("1", "The Category Error", ROOT / "build/web/ch01/AIOM_Ch01_The_Category_Error.pdf"),
    ("2", "The Flow", ROOT / "build/web/ch02/AIOM_Ch02_The_Flow.pdf"),
    ("3", "A Science and Its Discipline",
     ROOT / "build/web/ch03/AIOM_Ch03_A_Science_and_Its_Discipline.pdf"),
]
OUT = HERE / "AIOM_Review_Ch01-03_package.md"

PROMPT = """# Review package: Chapters 1 to 3 of *AI Operations Management*

This is ONE self-contained file: your instructions, the output format, and the
three chapters between BEGIN and END markers. Read it all before you begin.

**Your first line must say whether you have live web access in this session**
(`WEB ACCESS: yes` or `WEB ACCESS: no`). Do not simulate a lookup you cannot
perform: if you cannot open a document, say CANNOT CONFIRM.

---

## PART 1. Your task

You are checking the first three chapters of an academic textbook for business
graduate students. They are published. The author wants to REFINE them, not
rebuild them. You have two jobs, done together.

### Job 1. The red-flag sweep

Has anything the chapters claim been **disproven or seriously undercut** by
reporting or events since it was written? Major problems only:

- A cited fact that the source, or later reporting, now contradicts.
- A general claim about how AI is bought, priced, consumed or managed that
  major events since have shown to be wrong, or true only in a much narrower
  form.
- A dated case whose story later changed in a way the chapter's use of it
  depends on.

**Do NOT report**: wording, style, minor imprecision, a figure that moved by a
little, or a claim that is merely debatable. If you find nothing major in a
chapter, say so plainly; that is a useful result.

The book separates timeless teaching prose from dated, sourced material
(company names, dates and figures appear only in dated boxes and cases). A dated
box being out of date is NOT a red flag: it is dated on purpose. It is a red flag
only if it was wrong when written, or if a later chapter would mislead a reader
by relying on it.

### Job 2. Stronger evidence from major sources

The author wants major new evidence, from large, well-known companies, that
supports what the chapters argue, and to know where major evidence cuts against
them.

**Allowed sources only**: the Financial Times, the Wall Street Journal,
Bloomberg, Reuters, The Information, the New York Times, The Economist, and
first-party company material (earnings calls and transcripts, SEC filings,
official announcements, a named executive's own published statement). Trade
press, blogs and aggregators may help you FIND a story; they may never be the
source you report. If only trade press carries something, report it as NOT
USABLE.

**2a. Verify these candidates.** Claude found them by web search and has read
none of the articles. For each: open the original in an allowed source, quote
the exact sentences that carry the facts, give the date and URL, and correct
anything the summary below gets wrong.

| # | Candidate (as summarized from search, UNVERIFIED) | Likely original |
|---|---|---|
| K1 | AT&T runs about 40% of its AI workloads on open-weight models and aims for 70% within a year; it processes about 45 billion tokens a day, and its chief data and AI officer, Andy Markus, said that at that scale cost is extremely important. US companies are turning to open-weight models to cut costs (late September 2026). | Financial Times, about 27 September 2026 |
| K2 | Earlier AT&T figures: open models about 25% of usage, savings up to 90%, longer-term target 70% to 80%. | Wall Street Journal (date unknown) |
| K3 | AT&T cut the cost of coding and some advanced tasks by up to 56% by routing employees' queries to cheaper models; target of 60% to 70% open-model share. | The Information, about August 2026 |
| K4 | Uber set a monthly cap of $1,500 per employee per agentic coding tool (such as Claude Code and Cursor), with a usage dashboard and an exceptions process, after exhausting its 2026 AI budget early in the year. | Bloomberg, about June 2026 |
| K5 | Meta told about 6,000 employees it would centrally control AI token use because costs were on track for billions of dollars; 73.7 trillion tokens in about 30 days; a dashboard called AI Gateway; CTO Andrew Bosworth: "token usage alone is not a measure of impact". Conflicting later reporting says no per-employee caps were yet in force. | The Information, about June 2026 |
| K6 | ServiceNow used up its annual budget for Anthropic products early in 2026; its CIO linked the unpredictability partly to a lack of per-employee usage data, and the company tracks daily Claude use with its own AI Control Tower. | The Information, about 14 May 2026 |
| K7 | Inference token spending shifted from closed to open-weight models from mid-July 2026 (SiliconData figures); OpenAI and Anthropic cut prices in response. | Financial Times, about September 2026 |
| K8 | The FinOps Foundation's State of FinOps 2026 reports that 73% of organizations said AI costs exceeded their original projections. | FinOps Foundation report (first party) |

**2b. Find more.** Look for major-source reporting from 2025 and 2026 on large
organizations that shows, in their own words or numbers, any of these:

1. AI use behaving as metered consumption whose cost grows with use, rather
   than as a fixed software purchase (Chapter 1's central claim).
2. Costs arriving by default while value has to be built and shown; an
   organization losing track of AI spend, or putting a governing control in
   place once use reached scale (Chapter 2).
3. Organizations doing one of the five functions of Chapter 3 deliberately:
   matching models to work and changing providers on cost (sourcing), budgeting
   AI consumption, recording and charging back use by team (metering and
   attribution), routing work between cheap and capable models (allocation and
   routing), or setting a value test before spending (holding value to account).

Prefer a few strong items over many weak ones: aim for three to six per chapter.
Report evidence that CUTS AGAINST a claim with the same care as evidence for it.

**Do not use these cases; later chapters own them**: Klarna's later correction
of its AI claims; the MIT NANDA "GenAI Divide" study; provider pricing changes
and usage limits (Cursor, Claude Code limits, GitHub Copilot, OpenAI Pro, OpenAI
service tiers, Salesforce or other vendors' pricing plans); shadow AI;
Air Canada's chatbot case. You may mention one only as a red flag, if a
chapter's existing use of it is now wrong.

---

## PART 2. Required output format

Start with `WEB ACCESS: yes` or `WEB ACCESS: no`. Then three sections.

```
## Red flags
R-<n>. [Chapter N, section]  SEVERITY: major | serious
Claim: "<exact sentence from the chapter>"
What happened: <one or two sentences>
Source: <allowed source, title, date, URL>, quoting: "<exact words>"
Proposed narrowing: <exact replacement wording, or "cut">

## Candidates verified (K1 to K8)
K<n>. VERIFIED | PARTLY | NOT FOUND IN AN ALLOWED SOURCE
Source: <title, outlet, date, URL>
Exact words: "<quoted sentences carrying the facts>"
Corrections to the summary: <or "none">
Supports or cuts against: Chapter N, "<the sentence or idea>"

## New evidence found
E-<n>. [supports | cuts against]  Chapter N, "<the sentence or idea>"
Source: <title, outlet, date, URL>
Exact words: "<quoted sentences carrying the facts>"
Why it matters: <one sentence>
```

End with `NOT CHECKED`, naming anything you could not open.

House rules for any wording you propose: no em dashes or en dashes; no
contractions; no hedging ("perhaps", "some argue"). Accurate qualification is
fine, and making a sentence narrower is better than making it vaguer.

---

## PART 3. The chapters

The text below was extracted from the typeset PDFs, so it carries typesetting
artifacts: running heads, page numbers, letter-spaced small capitals, words
broken at line ends, and footnotes printed mid-page. Ignore them. Figures are
drawings; only their labels survive.
"""


def text(pdf):
    out = subprocess.run(["pdftotext", str(pdf), "-"], check=True,
                         capture_output=True, text=True).stdout
    return out.replace("\f", "\n").strip()


def main():
    parts = [PROMPT]
    for n, title, pdf in PDFS:
        parts.append(f"\n<<<<< BEGIN CHAPTER {n}: {title.upper()} >>>>>\n\n"
                     f"{text(pdf)}\n\n<<<<< END CHAPTER {n} >>>>>\n")
    parts.append("\nEND OF PACKAGE. Now produce your findings in the format given in Part 2.\n")
    body = "".join(parts)
    for bad in ("—", "–"):
        assert bad not in PROMPT, "a dash in the instructions"
    OUT.write_text(body, encoding="utf-8")
    print(f"wrote {OUT.name}: {len(body.split())} words")


if __name__ == "__main__":
    main()
