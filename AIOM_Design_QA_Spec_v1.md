# AIOM Design QA Specification, Section 8: The Eleven Gates

Version 1.3 · 2026-07-30 · Documents `AIOM_build.py` v6.2 `qa()`
and verified against `AIOM_book.css` v6.6.

Status: documentation of the suite as implemented. Where the implementation
and a standing rule disagree, this document says so and marks the item for
ruling rather than resolving it silently.

---

## 0. Why this document exists

`AIOM_build.py` runs fourteen gates after every render and prints PASS or FAIL.
The gates are correct and thorough, but their constants were embedded in code
with no stated derivation. An unenumerated suite cannot be audited, extended
with confidence, or handed to anyone else. This document states, for each gate:
what it tests, the constant it uses, where that constant comes from, and what
a failure means.

Invocation:

```
python3 AIOM_build.py --fonts                 # once per session
python3 AIOM_build.py AIOM_ch01.html          # footnotes, render, fourteen gates
```

The build has three steps. `footnotes.inject()` reads the chapter's own
`<pre id="aiom-sources-data">` block, formats each entry through
`cite_format.py`, and replaces every authored `<cite src="...">` with a
`<span class="fn">`. WeasyPrint renders the result. The gates then run against
the PDF, with the injected footnote count passed to gate 8.

Citation style: Chicago notes-bibliography, note form. Full citation at the
foot of the page carrying the claim, per the ruling recorded in
`AIOM_book.css` section 3.

**URL policy: `none` (ruled 2026-07-30).** URLs do not appear in footnotes.
They live in the source block, which travels with every draft under Decision
51, and in the back-of-book bibliography. The accessed date does appear in the
footnote, which is what the evidence policy requires for perishable web
content. Rendering with `--url-policy full` pushes footnote 5 of Ch1 to 876
characters, which cannot fit one page and trips gate 8.

Exit code is 0 only if all fourteen gates pass. Exit code 2 means the
toolchain is missing and NO gate ran; see requirements.txt.

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

## 3. The fourteen gates

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

Amended v6.2 to close gap G-H. `qa()` accepts `expected_footnotes`, which the
build passes from the injection step. The gate now also fails when the
rendered count differs from the count the source block should have produced.
Before this, a chapter whose footnote apparatus was not wired rendered zero
footnotes and the gate reported success. That is exactly what happened on the
first Ch1 Stage 4 render: the CSS put `float: footnote` on `.fn` while the
chapter HTML used `<cite>`, all six citations fell into the body text as
inline italic, and gate 8 passed.

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

### Gate 11. Theorem panel integrity

Added v6.1 to close gap G-A.

`.theorem` is a normal block with `break-inside: avoid`, so the WeasyPrint
float bug that necessitates gate 4 does not apply to it. This gate catches the
two failures the property cannot prevent: WeasyPrint ignoring it, and a panel
forced to break because it does not fit the space remaining.

- Panels: rectangles filled `--tint-thm` (`#F7EDE2`)
- Labels: rows of 8.5pt Jost characters filled `--amber` whose text begins
  `THEOREM`
- Left rule: matched as a **border box**, not a sliver. WeasyPrint paints a
  border as a filled rect covering the whole border box and then paints the
  background over it, so a 3pt left border never appears as a 3pt rect. The
  gate requires an amber rect on the same page with matching `top` and height
  whose `x0` sits at or left of the panel's `x0`.

Three failure conditions:

1. A panel truncated at the bottom text edge (626.4pt), which proves a break
2. More panels than labels, since a continuation carries no label of its own
3. A panel with no matching amber border box

**Position is deliberately not a failure signal.** A panel that legitimately
begins at the top of a page is indistinguishable by position from a
continuation. The first draft of this gate used flush-at-top as a split
signal and produced a false positive on Ch1, whose theorem panel opens page 8
legitimately. Gate 4 still uses that discarded heuristic. See gap G-G.

---

## 4. Known coverage gaps

The suite covers apparatus and typography well. These are the holes.

| ID | Gap | Risk |
|---|---|---|
| ~~G-A~~ | ~~Theorem callout splits are not checked.~~ **Closed in v6.1 by gate 11.** | resolved |
| **G-B** | **PARTLY CLOSED in v6.3 by gate 12**, which checks that every figure is captioned, that captions run in order, and that each is referenced in the text. Figure GEOMETRY is still unvalidated: SVG `rx` renders as curve paths that never appear in pdfplumber's `.rects`, so a frame that lost its shape reads as absent rather than wrong. Inspect by pixel-sampling a raster. | **Medium.** Reduced from High: a missing or misnumbered figure now fails a gate. |
| ~~G-C~~ | ~~Gate 1 checks the right edge only. No bottom-margin baseline check.~~ **Closed in v6.3 by gate 13**, which measures the bottom margin with the folio excluded by colour. | resolved |
| ~~G-D~~ | ~~No widow or orphan detection.~~ **Closed in v6.3 by gate 14**, which also detects stranded section heads. AMENDED 2026-08-06 at Ch1 Stage 5: gate 14 counted key-term names as body prose. A term name is a full line in the semibold face at body size, so every one read as a one-line paragraph, and the first on a page scored as a widow while the last scored as an orphan. Chapter 1 carried one phantom widow and one phantom orphan on its Key terms page as CD7, booked as real design work. `is_body` now excludes a line that is entirely semibold, testing the whole line rather than its first character, because body prose legitimately carries inline bold at a term's first use. | resolved |
| **G-I** | **A floated definition callout can collide with a following block panel, and no gate sees it.** Found at Ch1 G2, 2026-08-06, while testing alternative callout placements. One candidate put the callout beside the theorem panel: the panel's title wrapped into a narrow column and its first line was indented while the rest ran full measure. All fourteen gates passed on that render. Gate 11 checks the theorem panel is present, labelled, ruled, and unsplit; it does not check that it kept its measure. The same happens against a dated evidence box. `place.py` rejects candidates that break another gate, so it cannot reintroduce a gate failure, but nothing stops it choosing a placement that collides visually. | **Medium.** Until closed, a chapter whose callout placement moves must have the affected pages read, not merely gated. |
| **G-J** | **WeasyPrint 69 can render a footnote pages away from its call, and reserve the space it then does not use.** Booked at Ch1 Stage 5, 2026-08-08, on Dan's ruling, as a defect of the renderer rather than of the chapter. Two of Chapter 1's six footnotes fail: note 4 is called on page 11 and prints on page 12, note 6 is called on page 18 and prints on page 21. The SAME defect also shortens both pages, which is the part gate 8 does not say: page 11's body ends at 427.9pt and page 18's at 562.0pt against a normal 626.1pt, so each prints roughly a third empty. The reserved footnote space is never filled. WHAT WAS RULED OUT, each by experiment rather than by argument: it is not pagination luck, since four perturbations of the prose in 1.1 and 1.2 moved the chapter's text without moving either failure; it is not call position, since moving either call off the last sentence of its block changed nothing; `footnote-policy: line` is load-bearing and must stay, because removing it ADDS a third failure, and `footnote-policy: block` changes nothing. It does not reproduce in a minimal document: a harness sweeping filler length, container height and `break-inside` in both configurations, including the exact shape of both failures, is clean every time. Two CSS levers each fix note 6 and NEITHER fixes note 4: `aside.definition { float: none }` (26 pages), and `.dated { break-inside: auto }` (25 pages, but it lets a dated evidence box split). Both are design-system changes that re-run Stage 5 and G2 book-wide for half a fix, which is why neither was taken. | **Medium.** Gate 8 stays red on Chapter 1 and the gate is NOT relaxed: a red gate that is understood is worth more than a green one that is not. Revisit on a WeasyPrint version change, which is the only lever with a chance at note 4, and which re-runs Stage 5 and G2 book-wide in its own right. |
| **G-K** | **Gate 14 cannot tell a one-line paragraph from a widow.** The 2026-08-06 amendment closed this for key-term names by excluding a line that is entirely semibold, which works only because a term name has a font signal. A one-line paragraph in ORDINARY body prose has none, and the first one on a page still scores as a widow. Found 2026-08-08, when the Q1 ruling set section 1.4's five diagnostic questions as five short standalone paragraphs: "Where is the resource being used?" opens page 14 and gate 14 reports it as a widow. It is a whole paragraph, not the last line of one. The obvious discriminator, whether the previous page's last line filled the measure, does not work: `width()` sums glyph widths and excludes inter-word spaces, so a justified mid-paragraph line at a page break measures short too. | **Medium.** One of Chapter 1's two reported widows is this phantom; the other, on page 13, is real. Until closed, a widow count must be read against the pages, not trusted. |
| G-E | Gate 6 counts Key Terms rows but does not verify identity, or reconcile them against the body definition callouts. | Low |
| G-F | No check that a part's assigned colour is the colour in use. | Low, until Part II |
| **G-G** | **Gate 4 uses the flush-at-top split heuristic that gate 11 discarded.** A definition callout legitimately landing at the top of a page will be reported as split. The failure mode is false positives, not false negatives, so a passing result is trustworthy. | Medium |
| ~~G-H~~ | ~~Gate 8 passes vacuously.~~ **Closed in v6.2** by passing the expected footnote count from the build into gate 8. | resolved |

## 5. Open questions for D0

- **Q1.** Close G-A and G-B before running Stage 4 on Ch1, or run the suite as
  built and inspect figures and the theorem callout by eye?
- **Q2.** En dashes: banned outright as gate 2 implements, or permitted in
  numeric ranges as the standing rule implies? The Stage 3 voice gate currently
  permits them in ranges, so the two suites disagree.
- ~~**Q5.** Gloss form.~~ **Ruled 2026-07-30.** A gloss is one or more
  complete sentences naming which source carries what. All six Ch1 glosses
  were rewritten to this convention. The formatter does not auto-capitalise,
  by design: capitalisation is an editorial property of the gloss, and
  auto-capitalising a continuation produces "Which reproduces both
  statements." Convention applies from Chapter 2 onward.
- **Q3.** Part palette. `--teal` is declared and never used (zero `var(--teal)`
  references). Part III and Part IV colours do not exist in the CSS. Not
  blocking for Ch1; blocking for Ch4.
- **Q4.** Version and reference integrity. Build script is v6.0, CSS is v6.6,
  and the CSS states it was reverse-engineered from
  `AIOM_Ch1_DesignProof_v5_FINAL.pdf`, which is not in project files. The
  design proof of record needs to be identified and stored.

---

## 6. Files in the pipeline

| File | Role |
|---|---|
| `AIOM_build.py` v6.3 | fonts, footnote injection, render, fourteen gates, toolchain preflight |
| `AIOM_book.css` v6.6 | sole control of appearance; chapters carry content only |
| `cite_format.py` | source entry to Chicago note-form citation |
| `footnotes.py` | build step; `<cite>` to `<span class="fn">` |
| `place.py` | floated callout placement, gate 4 remedy |

The chapter HTML keeps `<cite src="...">` with its `.ckey` span as the authored
form. It carries the source keys and the editorial gloss, and it is what the
audit draft shows. `.audit-only` hides the source block from the render.

---

## 7. Standing rule for this file

This document and `AIOM_build.py` must move together. A gate added, removed,
or retuned in code without a matching entry here reopens the audit hole this
document was written to close.
