#!/usr/bin/env python3
"""Assemble the two Chapter 3 Stage 3 fact-check packages, one file each.

One-off for Chapter 3, kept beside its output so the step can be rebuilt (a
packet built by a scratchpad script died with its container on Chapter 1).
The general tool is on the fix-between-chapters list as review_package.py.

Inputs, all in this folder:
    AIOM_Ch03_Stage3_render.pdf   the fresh render (AIOM_build.py)
    AIOM_Ch03_Stage3_packet.md    factcheck_packet.py --stage 3 on that render

Outputs:
    AIOM_Ch03_Stage3_package_A.md   check A: render text + packet (reads sources)
    AIOM_Ch03_Stage3_package_B.md   check B: render text only

Run from the repo root:
    python3 Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/build_packages.py
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
RENDER = HERE / "AIOM_Ch03_Stage3_render.pdf"
PACKET = HERE / "AIOM_Ch03_Stage3_packet.md"

# factcheck_packet.py does not read inside <table> (fix-between-chapters list),
# so the three Table 3.1 citations never reach Part 1 of the packet. Added here
# by hand, quoting the table cells as they stand in the live text.
TABLE_ADDENDUM = """
## Part 1a. Table 3.1 citations, added by hand

`factcheck_packet.py` does not read inside tables, so these three cited
cells are missing from Part 1 above. They are quoted from Table 3.1 as it
stands. Their register entries follow.

### T1 (Table 3.1, AIOps row, "What it is for")

> Applying machine learning to run IT operations: correlating events, detecting anomalies, finding causes

CITES: `gartner-aiops`. IN-CHAPTER GLOSS: The originating definition of AIOps.

### T2 (Table 3.1, MLOps row, "What it is for")

> Building, deploying, and monitoring machine learning models in production

CITES: `kreuzberger-2023-mlops`. IN-CHAPTER GLOSS: Definition and scope of MLOps.

### T3 (Table 3.1, FinOps row, "What it is for")

> Financial accountability for technology spending, through collaboration among engineering, finance, and business teams

CITES: `finops-what-is`. IN-CHAPTER GLOSS: The Foundation's own definition of the practice.

The same row's last cell reads: "It was built around cloud billing. A
practitioner told its own survey that no one could yet say whether AI
provides value." It carries no citation of its own; it restates C4.

### `gartner-aiops`

- **type**: web
- **authors**: {"org": "Gartner"}
- **title**: AIOps (Artificial Intelligence for IT Operations)
- **container**: Gartner Information Technology Glossary
- **url**: https://www.gartner.com/en/information-technology/glossary/aiops-artificial-intelligence-operations
- **accessed**: 2026-10-01

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C, AND THE URL IS A CANDIDATE. Search coverage attributes to the Gartner glossary: AIOps combines big data and machine learning to automate IT operations processes, including event correlation, anomaly detection and causality determination. Table 3.1 paraphrases it. Check A must find the live glossary page, confirm the wording, and correct the URL.

### `kreuzberger-2023-mlops`

- **type**: article
- **authors**: Dominik Kreuzberger, Niklas Kühl, Sebastian Hirschl
- **title**: Machine Learning Operations (MLOps): Overview, Definition, and Architecture
- **container**: IEEE Access, volume 11, 2023, pages 31866-31879
- **doi**: 10.1109/ACCESS.2023.3262138

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C. Bibliographic details from search results. Table 3.1 paraphrases the scope of MLOps as building, deploying and monitoring machine learning models in production. Check A must confirm the paper's own definition supports that paraphrase, and the volume, pages and DOI.
"""

RENDER_NOTE = """The chapter text below was extracted from the typeset PDF, so it
carries typesetting artifacts that are NOT in the text. Do not report them:

- Running heads, page numbers and small capitals set with spaces between the
  letters ("PA R T I", "D AT E D").
- Words broken at a line end. A broken word may appear with a hyphen and a
  line break ("state-" / "ment") or, where the word already held a hyphen,
  joined ("Ninetyeight" is "Ninety-eight" in the book).
- Footnotes printed at the foot of each page, in the middle of the running
  text. Footnote numbers appear as plain digits after a word or a period.
- Figure 3.1 and Figure 3.2 are drawings; only their captions and labels
  survive extraction.

If a finding depends on one of these, it is an artifact. When in doubt, quote
it and say you are unsure, rather than reporting a defect."""

PROMPT_A = """# Fact-check package A: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file. Everything you need is inside it: your
instructions, the required output format, and the material, between BEGIN and
END markers in Part 3. Read the whole file before you begin.

---

## PART 1. Your task

You are fact checking one chapter of an academic textbook for business graduate
students, *AI Operations Management*, before it is typeset for good. Work to the
standard of a university press fact checker: a claim is verified when you have
seen the document that supports it, not when it sounds right.

**Your first line must say whether you have live web access in this session.**
If you do not, say so and treat every "verified" below as unavailable to you.
**Do not simulate a lookup you cannot perform.** If you cannot open a document,
the answer is CANNOT CONFIRM, never a summary from memory presented as a check.
An earlier checker on this book disclosed that it had no web access, and that
disclosure was the most useful line in its report.

### What you have

- **Document 1** is the chapter as it will print, as text extracted from the PDF.
- **Document 2** is the source packet: every passage carrying a citation, the
  source key it cites, and the source register entry behind each key with its
  note verbatim. Every note says UNVERIFIED: **nobody on this project has read
  any of these sources.** They were found by web search only.

### Out of scope: the registry

Twelve passages (C5 to C11 and C13 to C16 in the packet) cite
`aibe-registry-2026`, the book's private formal registry. You cannot reach it.
They have been checked separately against the pinned registry version, word for
word. **Do not check them and do not report that you could not reach the
registry.** If such a passage makes a claim about the outside world, beyond what
the registry says, you may report that.

### Your task, in priority order

For every item, give a verdict: **VERIFIED**, **CONTRADICTED**, **PARTLY
SUPPORTED** (say which part fails), or **CANNOT CONFIRM** (say why: no access,
paywall, page gone). Quote the source language you relied on and give the
exact URL you read it at.

**1. The opening case (packet C1 to C4), the chapter's largest exposure.** It is
dated, it was found by search, and its provenance line tells the reader it has
not been checked against the report. Verify each separately:

- The FinOps Foundation changed its mission statement in **February 2026**.
- The **old** wording described its purpose as advancing the people who manage
  "cloud value" (the value of cloud), and the **new** wording "technology value"
  (the value of technology). Quote both wordings exactly as the Foundation gives
  them. The chapter says the new statement "replaced one word": is that
  accurate?
- The change **accompanied** the 2026 State of FinOps survey.
- The 2026 survey had **1,192 respondents**, responsible for **more than $83
  billion** in annual cloud spending.
- **98 percent** of respondents managed AI spending in 2026, **up from 31
  percent two years earlier**. Confirm that the 31 percent is the 2024 survey's
  figure and that the two figures measure the same thing.
- The quotation **"No one can answer that question yet."** appears in the report
  itself (not only in press coverage), is attributed to **a practitioner**, and
  answers a question about **whether AI was providing value**.
- Give the report's own title, publisher and location. If the press release or a
  Foundation page is a better source for the mission change than the current
  citation (a Yahoo Finance syndication), name it.

**2. The three definitions.**

- **FinOps** (C3, C12, T3): on the Foundation's live "What is FinOps?" page,
  quote the definition. Does it support (a) "maximizing the business value of
  technology", (b) accountability through collaboration among engineering,
  finance and business teams, and (c) the chapter's account that FinOps arose
  because cloud let engineers buy capacity in code while the bills arrived after
  use? Report (c) separately: it may need a different source.
- **AIOps** (T1): find Gartner's glossary entry, quote it, say whether it
  supports the table's paraphrase, and **give the correct URL** (the current one
  is a guess). The chapter's gloss calls it "the originating definition of
  AIOps": does Gartner originate the term?
- **MLOps** (T2): does Kreuzberger, Kühl and Hirschl (2023) define MLOps in a way
  that supports "building, deploying, and monitoring machine learning models in
  production"? Confirm the journal, volume 11, pages 31866-31879, and the DOI.

**3. The Klarna case (C17).** Against Klarna's own press release of 27 February
2024, verify each figure: **2.3 million conversations** in the first month;
**two-thirds** of customer-service chats; the work of **700 full-time agents**;
resolution in **under two minutes against eleven** previously; an estimated
**$40 million** profit improvement in 2024. Also: is the assistant described as
built on **OpenAI's** models, and is the date right? **Check the announcement
only.** Later reporting about Klarna is deliberately outside this chapter, which
uses the announcement as the company's own claim. Do not propose adding later
reporting.

**4. Anything else.** Name any sentence in Document 1 that states a fact about
the outside world (a date, a figure, a named organization's action, how often
organizations do something) and carries **no** citation. Do not report
sentences that are plainly the book's own argument or a labelled constructed
example.

### Rules for your findings

- **Number every finding** (A-1, A-2, ...).
- **Separate "the source contradicts this" from "I could not reach the source".**
  They get different rulings.
- **A proposed remedy is welcome and will be judged separately from the
  finding.** House rules a remedy must obey, or it is rejected while the finding
  stands: **no em dashes or en dashes** anywhere; **no hedging** ("perhaps",
  "some argue"); **no contractions**. Accurate qualification is not hedging.
  Making a sentence narrower is a good remedy; making it vaguer is not.
- **Do not comment on prose quality, structure, or teaching.** Other steps own
  those.
- **Ignore page layout.** Footnote 7 is known to print on the wrong page; that is
  booked to the design step.

---

## PART 2. Required output format

Start with one line: `WEB ACCESS: yes` or `WEB ACCESS: no`.

Then one block per finding, in this form:

```
A-<n>. <VERDICT>  [packet item, e.g. C2 or T1]
Sentence: "<the exact sentence from Document 1>"
Checked against: <document title, URL, date read>
Source says: "<quoted source language>"
Finding: <one or two sentences>
Proposed remedy: <exact replacement wording, or "none">
```

Report every priority item, including the ones you verify: a VERIFIED verdict
with its quotation is a result, and silence is not. End with a short list
headed `NOT CHECKED` naming anything in priorities 1 to 3 you could not reach.

---

## PART 3. The material
"""

PROMPT_B = """# Fact-check package B: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file: your instructions, the required output format,
and the chapter, between BEGIN and END markers in Part 3. Read the whole file
before you begin.

**You have the chapter and nothing else, on purpose.** Another checker is reading
the sources. You get no source notes, no register, and not that checker's
output. A claim that survives only because the reader trusts a footnote they
cannot open is the failure this check exists to find.

---

## PART 1. Your task

You are reading one chapter of an academic textbook for business graduate
students, *AI Operations Management*. **Do not look anything up, and do not tell
us whether its facts are true.** Your question is different: **does this chapter
claim more than it has shown?**

### What to look for

**1. A confident sentence and a careful sentence that disagree.** The chapter is
explicit about the limits of evidence: its opening case carries a line saying
its figures have not been checked against the report, it says what formal claims
do NOT establish, and it says the book cites only certified claims. Find every
place where a flat assertion elsewhere in the chapter claims more than one of
those careful passages allows. Quote both.

**2. Quantities and their scope.** For every figure, proportion, count and range
(the survey figures, "nearly all", the registry counts in the dated box, the
Klarna figures), ask what population or version it covers, whether the sentence
says so, and whether a later sentence reuses it as though it covered something
broader. "Nearly all" restating a percentage is one to test.

**3. One organization, described consistently.** FinOps and the FinOps Foundation
appear in the opening case, in Section 3.5, in Table 3.1, and in the questions.
Check that what the chapter says FinOps is, was built for, and now does is the
same everywhere, and that a quotation and its paraphrase say the same thing.
Do the same for Klarna across the Part I cumulative case.

**4. Statements about what organizations generally do.** Quote every sentence
claiming or implying how often, how commonly, or how typically organizations,
managers, or practitioners do something, including ones with no frequency word
that imply frequency through a generic plural ("companies ...", "managers
...").

**5. The worked examples and the problems.** For each example in the teaching
body and each problem, say whether it rests on facts the chapter established,
facts it labelled as constructed or stipulated, or facts it neither established
nor labelled. **Report the third kind.**

**6. Claims about the registry.** The chapter describes a formal registry: what it
contains, what its validator checks, what it records. You cannot see the
registry. Report any description that is internally inconsistent across the
chapter, or that a reader could reasonably take as a stronger claim than the
chapter supports elsewhere.

### Rules for your findings

- **Number every finding** (B-1, B-2, ...). Quote the exact sentence and give its
  section.
- **Say what a reader would wrongly conclude.** A finding with no wrong
  conclusion attached is a style note, and style is not this step.
- **Rank your findings** and name the single one you would fix if you could fix
  only one.
- **A proposed remedy is welcome and will be judged separately.** House rules it
  must obey, or it is rejected while the finding stands: **no em dashes or en
  dashes** anywhere; **no hedging** ("perhaps", "some argue"); **no
  contractions**. Making a sentence vaguer is not a fix; making it narrower is.
- **Formal statements are not prose.** Quoted statements of theorems, lemmas and
  propositions (identifiers such as THM-004, LEM-020, PROP-043) are verbatim from
  the registry. Do not judge their wording.
- **Do not comment on prose quality, rhythm, structure, or teaching.** Those steps
  have closed.
- **Ignore page layout.** Footnote 7 is known to print on the wrong page.

---

## PART 2. Required output format

One block per finding, in this form:

```
B-<n>. Rank <r>  [section]
Sentence: "<the exact sentence>"
Conflicts with: "<the other sentence, if any>"   [section]
A reader would wrongly conclude: <one sentence>
Proposed remedy: <exact replacement wording, or "none">
```

End with one line: `FIX FIRST: B-<n>`, and one sentence saying why.

---

## PART 3. The material
"""


def render_text():
    out = subprocess.run(["pdftotext", str(RENDER), "-"], check=True,
                         capture_output=True, text=True).stdout
    return out.replace("\f", "\n")


def doc(n, title, body):
    return (f"\n<<<<< BEGIN DOCUMENT {n}: {title} >>>>>\n\n{body.strip()}\n\n"
            f"<<<<< END DOCUMENT {n} >>>>>\n")


def main():
    text = render_text()
    chapter = RENDER_NOTE + "\n\n---\n\n" + text
    packet = PACKET.read_text(encoding="utf-8").rstrip() + "\n" + TABLE_ADDENDUM

    a = (PROMPT_A + doc(1, "CHAPTER 3, AS IT WILL PRINT", chapter)
         + doc(2, "SOURCE PACKET", packet)
         + "\nEND OF PACKAGE. Now produce your findings in the format given in Part 2.\n")
    b = (PROMPT_B + doc(1, "CHAPTER 3, AS IT WILL PRINT", chapter)
         + "\nEND OF PACKAGE. Now produce your findings in the format given in Part 2.\n")

    for name, body in (("A", a), ("B", b)):
        for bad in ("\u2014", "\u2013"):
            assert bad not in body.replace(text, ""), f"dash in package {name} prompt"
        p = HERE / f"AIOM_Ch03_Stage3_package_{name}.md"
        p.write_text(body, encoding="utf-8")
        print(f"wrote {p.name}: {len(body.split())} words")

    # Check B must never see the sources. Negative control on its own contents.
    for leak in ("NOTE, verbatim", "finops.org/introduction", "klarna.com/international",
                 "UNVERIFIED", "Part 2. Register entries"):
        assert leak not in b, f"package B leaks source material: {leak!r}"
        assert leak in a, f"control failed: {leak!r} not in package A either"
    print("package B carries no packet material (checked against package A)")


if __name__ == "__main__":
    main()
