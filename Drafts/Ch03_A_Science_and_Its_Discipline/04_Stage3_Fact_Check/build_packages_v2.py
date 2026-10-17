#!/usr/bin/env python3
"""Assemble the two Stage 3 fact-check packages for the REDESIGNED Chapter 3.

Version 2 of build_packages.py (Decision 85 redesign; the first version
checked the text that locked at be55e84). One markdown file per check, as Dan
asked (2026-10-17). Same two checks, different prompts (Decision 76):
A reads the sources, B reads only the render.

Inputs, all in this folder:
    AIOM_Ch03_v2_Stage3_render.pdf   fresh render of the post-author-pass text
    AIOM_Ch03_v2_Stage3_packet.md    factcheck_packet.py --stage 3 on that render

factcheck_packet.py does not read inside <table> (fix-between-chapters list),
so Table 3.1's cited cells and their register entries are added here, read
from the live text rather than typed by hand.

Run from the repo root:
    python3 Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/build_packages_v2.py
"""
import html as htmllib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LIVE = ROOT / "Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html"
RENDER = HERE / "AIOM_Ch03_v2_Stage3_render.pdf"
PACKET = HERE / "AIOM_Ch03_v2_Stage3_packet.md"


def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    return htmllib.unescape(s).strip()


def table_addendum():
    src = LIVE.read_text(encoding="utf-8")
    reg_raw = re.search(r'<pre id="aiom-sources-data">(.*?)</pre>', src, re.S).group(1)
    reg = json.loads(htmllib.unescape(reg_raw))
    table = re.search(r"<table\b.*?</table>", src, re.S).group(0)
    out = ["", "## Part 1a. Table 3.1 citations, added from the live text", "",
           "`factcheck_packet.py` does not read inside tables, so these cited cells",
           "are missing from Part 1. They are quoted from Table 3.1 as it stands,",
           "and their register entries follow.", ""]
    keys = []
    for n, tr in enumerate(re.findall(r"<tr>(.*?)</tr>", table, re.S)[1:], 1):
        cells = re.findall(r"<td>(.*?)</td>", tr, re.S)
        for c in cells:
            m = re.search(r'<cite src="([^"]+)">.*?</span>(.*?)</cite>', c, re.S)
            if not m:
                continue
            text = plain(re.sub(r"<cite\b.*?</cite>", "", c, flags=re.S))
            row = plain(cells[0])
            out += [f"### T{len(keys) + 1} (Table 3.1, {row} row, \"What it is for\")", "",
                    f"> {text}", "",
                    f"CITES: `{m.group(1)}`. IN-CHAPTER GLOSS: {plain(m.group(2))}", ""]
            keys.append(m.group(1))
    for k in keys:
        e = reg[k]
        out += [f"### `{k}`", ""]
        for f in ("type", "title", "container", "date", "url", "doi", "accessed"):
            if e.get(f):
                out.append(f"- **{f}**: {e[f]}")
        out += ["", "NOTE, verbatim:", "", f"> {e.get('note', '')}", ""]
    return "\n".join(out), len(keys)


RENDER_NOTE = """The chapter text below was extracted from the typeset PDF, so it
carries typesetting artifacts that are NOT in the text. Do not report them:

- Running heads, page numbers and small capitals set with spaces between the
  letters ("PA R T I", "D AT E D").
- Words broken at a line end, shown with a hyphen and a line break, or joined.
- Footnotes printed at the foot of each page, in the middle of the running
  text. Footnote numbers appear as plain digits after a word or a period.
- Figure 3.1 is a drawing; only its caption and labels survive extraction.
  Table 3.1 may come out as broken columns.

If a finding depends on one of these, it is an artifact. When in doubt, quote
it and say you are unsure, rather than reporting a defect."""

HOUSE_RULES = """- **A proposed remedy is welcome and will be judged separately from the
  finding.** House rules a remedy must obey, or it is rejected while the finding
  stands: **no em dashes or en dashes** anywhere; **no hedging** ("perhaps",
  "some argue"); **no contractions**. Accurate qualification is not hedging.
  Making a sentence narrower is a good remedy; making it vaguer is not.
- **Do not comment on prose quality, structure, or teaching.** Other steps own
  those.
- **Ignore page layout.** The render has known layout defects (an overflowing
  line, a definition box split across a page, a footnote on the wrong page);
  they belong to the design step."""

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
If you do not, say so. **Do not simulate a lookup you cannot perform.** If you
cannot open a document, the answer is CANNOT CONFIRM, never a summary from
memory presented as a check.

### What you have

- **Document 1** is the chapter as it will print, as text extracted from the PDF.
- **Document 2** is the source packet: every passage carrying a citation, the
  source key it cites, and the register entry behind each key with its note
  verbatim. A note marked **UNVERIFIED, GRADE C** means nobody on this project
  has read that source: it was found by web search only. A note recording an
  earlier external check means that source was read then, against an earlier
  version of the sentence.

The packet's header says that 14 rulings are in force and that a ruled-form
check fails. That is expected: the chapter was redesigned and its author
rewrote it, so several earlier rulings no longer match the text word for word.
Your findings are what they will be re-ruled against.

### Your task, in priority order

For every item, give a verdict: **VERIFIED**, **CONTRADICTED**, **PARTLY
SUPPORTED** (say which part fails), or **CANNOT CONFIRM** (say why: no access,
paywall, page gone). Quote the source language you relied on and give the
exact URL you read it at.

**1. The five dated boxes and the Lindy box, never read by anyone (the
chapter's largest exposure).** Each is Grade C. Verify every figure, date,
name and quotation separately, against the primary where one exists:

- **Airbnb (October 2025)**: the customer-service agent built on **13 models**
  from OpenAI, Google, Alibaba and open-source providers; heavy reliance on
  Alibaba's **Qwen**, called **"very good"** and **"also fast and cheap"**; OpenAI's
  tools for connecting its models to Airbnb's systems **not yet ready**. Name the
  interview and its date.
- **Pigment (October 2026)**: about **2,000** finance leaders in the US, UK,
  France and Germany; **83 percent** said consumption-based pricing pushed AI
  spending above expectations; **13 percent** stayed within budget; average
  overrun about **27 percent**; the report's release date.
- **DoiT (February 2026)**: commissioned by DoiT, conducted by **Sapio
  Research** in February 2026; **500** finance leaders at US and UK organizations
  with **1,000 or more** employees; **79 percent** reported AI-related overruns in
  the previous twelve months; accountability named as technology leadership
  **55 percent** and finance **53 percent**. The chapter infers "at least 8
  percent named both": confirm that the question allowed more than one answer.
- **Microsoft (July 2026)**: Bloomberg reported that Microsoft began sending
  some Copilot prompts in **Excel and Outlook** to its own **MAI** models instead
  of OpenAI and Anthropic models, **citing cost**; **tens of thousands of prompts
  a week**; routine tasks moved, complex reasoning could still go outside;
  **Mustafa Suleyman** said the goal was to reduce and ultimately eliminate its
  payments to Anthropic. Find the Bloomberg report if you can.
- **JPMorgan (October 2025, with a later update)**: **Jamie Dimon** on Bloomberg
  Television, about **$2 billion** a year spent and about the same in benefit,
  quotation **"We have shown that for $2 billion of expense, we have about $2
  billion of benefit."**; then the **chief financial officer** putting annual AI
  spending **closer to $700 million**, calling the earlier figure **"a little
  stale"**, and the report saying the benefits were **not yet visible in quarterly
  earnings**. Name the CFO and the date of that later report. If the cited
  article does not carry the later update, say so plainly.
- **Lindy (April to July 2026)**: about **25 people**; **Flo Crivello**; the largest
  expense was Anthropic's models, **"Like, more than payroll."**; in **June 2026**
  all traffic moved to **DeepSeek V4**; the move would **save millions**; **"100x
  more work than we thought."**; open to returning if prices fell; expects to keep
  spending more on AI than on payroll. Say which outlet carries each item.

**2. Sentences rewritten since their last check.** Each of these was verified
against its source on 2026-10-13 in different words. Confirm the new words are
still supported, and say if the rewrite claims more:

- Opening case: "Its central finding was how far FinOps had expanded into AI
  spending: 98 percent of respondents now managed it, up from 31 percent two
  years earlier." Does the report make AI spending its central finding?
- Opening case: "FinOps was built to address a specific problem: cloud bills
  varied with use and arrived after capacity had been consumed."
- Opening case: "by 2026 nearly all respondents to the Foundation's survey were
  managing it."
- Section 3.1, the Cursor paragraph: "After June 2025, each request drew down a
  twenty-dollar monthly credit at the model provider's rate, and further use was
  priced at the same rates." Check against `truell-2025-pricing`; its note
  records what the post does and does not establish about billing.

**3. Carried sources, restated in this chapter.** Uber (C13), the Australian
Copilot trial (C14) and Klarna (C15) were verified in earlier checks. Confirm
only that this chapter's sentences match their sources; do not re-verify what
the notes already record.

**4. Table 3.1** (Part 1a of the packet): confirm the three cited cells still
match their sources as recorded.

**5. Anything else.** Name any sentence in Document 1 that states a fact about
the outside world (a date, a figure, a named organization's action, how often
organizations do something) and carries **no** citation. Do not report
sentences that are plainly the book's own argument or a labelled constructed
example.

### Rules for your findings

- **Number every finding** (A-1, A-2, ...).
- **Separate "the source contradicts this" from "I could not reach the source".**
  They get different rulings.
""" + HOUSE_RULES + """

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
headed `NOT CHECKED` naming anything in priorities 1 to 4 you could not reach.

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

**1. A dated box and the prose around it.** Six dated boxes report real
companies (Airbnb, Pigment, DoiT, Microsoft, JPMorgan, Lindy). For each, does
the body prose next to it, or a later worked example, draw a conclusion the box
does not support? Quote both.

**2. Quantities and their scope.** For every figure, proportion, count and range
(the FinOps survey, "nearly all", the two finance-leader surveys, the JPMorgan
figures, Uber's costs, the Klarna figures), ask what population or period it
covers, whether the sentence says so, and whether a later sentence reuses it as
though it covered something broader. Two surveys come from vendors: is that
said where it matters?

**3. The function audit's verdicts.** The craft section and problem P1 mark
functions as performed, partly performed, or not shown, from public reporting.
Find any verdict that says more than the reporting quoted in the chapter shows,
or any place where "not shown" slides into "not done".

**4. One organization, described consistently.** FinOps appears in the opening
case, Section 3.3, Table 3.1 and problem P3. Check that what the chapter says
FinOps is, was built for, and now does is the same everywhere, and that a
quotation and its paraphrase say the same thing. Do the same for Klarna in the
Part I cumulative case and for Cursor in Section 3.1.

**5. Statements about what organizations generally do.** Quote every sentence
claiming or implying how often, how commonly, or how typically organizations,
managers, or practitioners do something, including ones with no frequency word
that imply frequency through a generic plural ("companies ...", "managers
...").

**6. Constructed examples.** For each example and problem, say whether it rests
on facts the chapter established, facts it labelled as constructed, or facts it
neither established nor labelled. **Report the third kind.**

### Rules for your findings

- **Number every finding** (B-1, B-2, ...). Quote the exact sentence and give its
  section.
- **Say what a reader would wrongly conclude.** A finding with no wrong
  conclusion attached is a style note, and style is not this step.
- **Rank your findings** and name the single one you would fix if you could fix
  only one.
- **Formal statements are not prose.** A theorem identifier such as THM-004 names
  a formal result; do not judge its wording.
""" + HOUSE_RULES + """

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
    addendum, n_table = table_addendum()
    assert n_table == 3, f"expected 3 cited table cells, found {n_table}"
    packet = PACKET.read_text(encoding="utf-8").rstrip() + "\n" + addendum

    a = (PROMPT_A + doc(1, "CHAPTER 3, AS IT WILL PRINT", chapter)
         + doc(2, "SOURCE PACKET", packet)
         + "\nEND OF PACKAGE. Now produce your findings in the format given in Part 2.\n")
    b = (PROMPT_B + doc(1, "CHAPTER 3, AS IT WILL PRINT", chapter)
         + "\nEND OF PACKAGE. Now produce your findings in the format given in Part 2.\n")

    for name, body in (("A", a), ("B", b)):
        for bad in ("—", "–"):
            assert bad not in body.replace(text, ""), f"dash in package {name}"
        p = HERE / f"AIOM_Ch03_v2_Stage3_package_{name}.md"
        p.write_text(body, encoding="utf-8")
        print(f"wrote {p.name}: {len(body.split())} words")

    # Check B must never see the sources. Negative control on its own contents.
    for leak in ("NOTE, verbatim", "GRADE C", "Part 2. Register entries",
                 "fortune.com/2025/10/21", "Part 1a. Table 3.1"):
        assert leak not in b, f"package B leaks source material: {leak!r}"
        assert leak in a, f"control failed: {leak!r} not in package A either"
    print("package B carries no packet material (checked against package A)")


if __name__ == "__main__":
    main()
