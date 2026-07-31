# AIOM Design QA Specification, Section 8: The Ten Gates

Version 1.0 · 2026-07-30 · Reconstructed from `AIOM_build.py` v6.0 `qa()`
and verified against `AIOM_book.css` v6.6.

Status: documentation of the suite as implemented. Where the implementation
and a standing rule disagree, this document says so and marks the item for
ruling rather than resolving it silently.

---

## 0. Why this document exists

`AIOM_build.py` runs ten gates after every render and prints PASS or FAIL.
The gates are correct and thorough, but their constants were embedded in code
with no stated derivation. An unenumerated suite cannot be audited, extended
with confidence, or handed to anyone else. This document states, for each gate:
what it tests, the constant it uses, where that constant comes from, and what
a failure means.

Invocation:

```
python3 AIOM_build.py --fonts                 # once per session
python3 AIOM_build.py AIOM_ch01.html          # render, then run all ten gates
```

Exit code is 0 only if all ten gates pass.

---

## 1. Page geometry, from which most constants derive

From `AIOM_book.css` v6.6:

| Property | Value |
|---|---|
| Trim | 486pt x 684pt (6.75in x 9.5in) |
| Right (odd) page margins | top 61.2, right 57.6, bottom 57.6, left 68.4 |
| Left (even) page margins | top 61.2, right 68.4, bottom 57.6, left 57.6 |
| Text block width | 360pt on both sides |
| Body | Plex (IBM Plex Sans Text) 11pt |
| Running head | Jost 500, 8pt |
| Folio | Plex 9pt in `--folio` |

Derived text-block edges, used by gates 1 and 8:

| Page | Left edge | Right edge |
|---|---|---|
| Odd (right) | 68.4pt | 428.4pt |
| Even (left) | 57.6pt | 417.6pt |

## 2. Palette tokens the gates key on

| Token | Hex | Gates that use it |
|---|---|---|
| `--tint-def` | `#EDE3D0` | 4 (narrow), 6 (wide) |
| `--tint-thm` | `#F7EDE2` | none, see gap G-A |
| `--hairline` / `--kt-head` | `#DCCFB4` | 6 |
| `--amber` | `#B4551F` | 7, 8, 9 |
| `--folio` | `#9B8F7C` | 3 |
| `--axis` | `#6E6353` | 9 (as RGB 110, 99, 83) |

Gates discriminate objects by fill colour plus a geometric test. Changing any
palette value without updating the suite silently disables the gates keyed to it.

---

## 3. The ten gates

### Gate 1. Right-margin overflow

Tests every character on every page against the derived right text edge.

- Limit: 428.4pt on odd pages, 417.6pt on even pages
- Tolerance: 1.5pt
- Vertical band: only characters with `60 < top < 640`, which excludes the
  running head above and the folio below
- Fails if any character's `x1` exceeds limit plus tolerance

Catches: unbreakable strings, oversized SVG text, table cells that will not wrap.

Does not catch: overflow past the bottom margin. See gap G-C.

### Gate 2. Em and en dashes

Fails on any `U+2014` or `U+2013` character in the rendered PDF.

**Conflict to rule.** The standing rule bans em dashes only. This gate also
bans en dashes outright, including in numeric ranges, which is stricter than
the standing rule and stricter than the Stage 3 voice gate. See open question
Q2.

### Gate 3. Running heads and folios

Per page, identifies:

- Folio: a 9pt character filled `#9B8F7C`
- Running head: an 8pt character in a Jost face

Three assertions:

1. Every page carries a folio
2. Every page after page 1 carries a running head
3. Page 1 carries no running head (suppressed by `@page :first`)

### Gate 4. Definition callout splits

Finds rectangles filled `--tint-def` with width under 200pt, which selects the
narrow floated definition callouts and excludes the full-width Key Terms
fields. Fails any whose `top` is within 0.5pt of 61.2pt, the top margin.

Rationale: a callout beginning flush at the top of the text block is the
signature of a callout that broke across a page and continued. WeasyPrint 69
ignores `break-inside: avoid` on floated elements, so this cannot be prevented
in CSS.

Remedy on failure: run `place.py` on the chapter to reposition the callout
while preserving its order relative to the prose occurrence of the term.

Does not cover the theorem callout, which uses `--tint-thm`. See gap G-A.

### Gate 5. Font faces

Collects every font name in the PDF, strips the subset prefix, and compares
against the expected set:

```
Jost-Medium · Jost-Semi-Bold · Plex · Plex-Italic · Plex-Medium · Plex-Semi-Bold
```

Fails on any face outside that set.

Catches: a missing `@font-face`, an unstaged font falling back to a system
face, and stray faces embedded inside SVG.

### Gate 6. Key Terms register integrity

- Term fields: rectangles filled `--tint-def` with width 200pt or greater
- Header bands: rectangles filled `--kt-head` (`#DCCFB4`)

Fails if the two counts differ, which means an entry lost its header band.

Does not verify that the terms present are the correct terms, or that they
match the body definition callouts. See gap G-E.

### Gate 7. Opening case provenance line

On page 1 only, requires at least one character at 7pt, filled `--amber`, in a
Semi-Bold face. That combination is unique to the provenance line beneath the
opening case title.

Enforces the standing rule that every case is dated where perishable and
constructed material is labelled as constructed.

### Gate 8. Footnote placement

The hardest gate. Footnote calls and footnote texts share a style (7pt,
`--amber`, not Semi-Bold), so they are distinguished by horizontal position:

- A **note** begins within 0.6pt of the left text edge (68.4 odd, 57.6 even)
- Anything else at that style is a **call**

Characters are grouped into rows by rounded `top`, each row assembled into a
number, and per page the suite compares the set of call numbers against the
set of note numbers.

Fails if the sets differ on any page, meaning a footnote rendered on a
different page from its call.

### Gate 9. Dated evidence boxes

Two-part gate, the only one that rasterizes.

Part one, count the labels. Finds 7pt `--amber` Semi-Bold rows whose leftmost
character sits between the left edge plus 6pt and 200pt. The indent is what
separates a dated box label inside a box from the provenance line at the
margin (gate 7).

Part two, confirm the rules rendered. Rasterizes at 110 dpi and runs a
vertical scan line just inside the left margin, looking for unbroken runs of
`--axis` (RGB 110, 99, 83) longer than 15px. Each run is the box's left rule.

Fails if the rule count differs from the label count, or if a rule measures
wider than 3px when it should be a hairline.

Rationale for pixel sampling: SVG and CSS borders with rounded corners render
as curve paths in WeasyPrint and do not appear in pdfplumber's `.rects`, so
geometry has to be confirmed optically.

### Gate 10. Problem label and title separation

Finds 8.5pt Jost rows matching `^P\d`, which selects problem labels such as
`P1 · Worked`. For each label, requires an 11.5pt Jost title positioned below
it on the same page.

Fails if a label has no title beneath it, meaning the label was stranded at a
page bottom and its title pushed to the following page.

---

## 4. Known coverage gaps

The suite covers apparatus and typography well. These are the holes.

| ID | Gap | Risk |
|---|---|---|
| **G-A** | **Theorem callout splits are not checked.** Gate 4 keys on `--tint-def`; the theorem uses `--tint-thm` (`#F7EDE2`) and is unguarded. | **High.** THM-009's statement is a single 74-word sentence that cannot break. Ch1's highest-risk object is the one object with no gate. |
| **G-B** | **No figure validation at all.** Nothing confirms a figure rendered, sits inside its frame, or kept its geometry. Gate 5 catches fallback fonts in SVG text and gate 1 catches horizontal overflow; everything else fails silently. | **High.** Ch1 carries two hand-built SVG figures. |
| G-C | Gate 1 checks the right edge only. No bottom-margin baseline check. | Medium |
| G-D | No widow or orphan detection. | Medium |
| G-E | Gate 6 counts Key Terms rows but does not verify identity, or reconcile them against the body definition callouts. | Low |
| G-F | No check that a part's assigned colour is the colour in use. | Low, until Part II |

## 5. Open questions for D0

- **Q1.** Close G-A and G-B before running Stage 4 on Ch1, or run the suite as
  built and inspect figures and the theorem callout by eye?
- **Q2.** En dashes: banned outright as gate 2 implements, or permitted in
  numeric ranges as the standing rule implies? The Stage 3 voice gate currently
  permits them in ranges, so the two suites disagree.
- **Q3.** Part palette. `--teal` is declared and never used (zero `var(--teal)`
  references). Part III and Part IV colours do not exist in the CSS. Not
  blocking for Ch1; blocking for Ch4.
- **Q4.** Version and reference integrity. Build script is v6.0, CSS is v6.6,
  and the CSS states it was reverse-engineered from
  `AIOM_Ch1_DesignProof_v5_FINAL.pdf`, which is not in project files. The
  design proof of record needs to be identified and stored.

---

## 6. Standing rule for this file

This document and `AIOM_build.py` must move together. A gate added, removed,
or retuned in code without a matching entry here reopens the audit hole this
document was written to close.
