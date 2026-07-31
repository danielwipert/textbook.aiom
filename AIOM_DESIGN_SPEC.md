# AI Operations Management: Design Specification

**Version:** 6.8
**Date:** 2026-07-25
**Status:** LOCKED
**Applies to:** all chapters, front matter, and back matter of *AI Operations Management*

## 0. How this document came to exist

Chapter 1 was designed through five iterations (v1 through v5) that produced PDFs but no
saved source. This specification was recovered from `AIOM_Ch1_DesignProof_v5_FINAL.pdf` by
forensic extraction: type sizes and colors from the PDF text layer, page and box geometry
from vector rectangles, and font identity from the embedded font files' name tables.

The rebuild was verified against v5 page by page. Body text blocks match within 0.2pt on
all seven pages, and pages 3, 4, and 6 match exactly, including the theorem panel.

One correction was made in the recovery. The body typeface was initially assumed to be a
serif because the PDF font resource is labelled `Plex`. That label is the CSS family name,
not the file. The embedded font's name table identifies the real face as **IBM Plex Sans,
Text weight**. A metric fingerprint (mean absolute glyph-advance error of 0.00141 em against
a method validation floor of 0.00150 em) confirms it. Do not substitute IBM Plex Serif.

## 1. Files and the rule that governs them

| File | Role |
|---|---|
| `AIOM_book.css` | Sole control of appearance. Locked. |
| `AIOM_DESIGN_SPEC.md` | This document. The reasoning behind the CSS. |
| `AIOM_chNN.html` | Content only. |
| `AIOM_build.py` | Render plus the ten QA gates. |
| `place.py` | Callout placement pass. Run when gate 4 fails. |

**Absolute rule:** no chapter HTML file may contain a `<style>` block or a `style=`
attribute. Every appearance decision lives in `AIOM_book.css`. Scoped per-chapter overrides
are how a fifteen-chapter book becomes fifteen slightly different books.

## 2. Page

| Property | Value |
|---|---|
| Trim | 486 x 684 pt (6.75 x 9.5 in) |
| Text block | 360 pt wide, 565.2 pt tall |
| Margins, recto (odd) | top 61.2, inner (left) 68.4, outer (right) 57.6, bottom 57.6 |
| Margins, verso (even) | top 61.2, outer (left) 57.6, inner (right) 68.4, bottom 57.6 |

Margins are mirrored. The inner margin is 10.8 pt wider than the outer to allow for binding.

**Running heads.** 8 pt Jost Medium, amber, uppercase, letter-spacing 0.196em, positioned on
the outer edge, baseline block 24.8 pt above the text block. Verso carries the book title,
recto carries the chapter title (set automatically from the `h1` via `string-set`). The
chapter opening page carries no running head.

**Folios.** 9 pt IBM Plex Sans, folio grey, centered, 23 pt below the text block.

## 3. Color

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#F4ECDD` | page background |
| `--navy` | `#16314F` | all headings, callout terms |
| `--amber` | `#B4551F` | labels, rules, figure numbers, key terms |
| `--amber-fig` | `#C0521A` | event-model curve and ticks in figures |
| `--teal` | `#0E7A72` | seat-model line in figures, second figure accent |
| `--ink` | `#2B2620` | body text |
| `--folio` | `#9B8F7C` | folios |
| `--axis` | `#6E6353` | figure axes and axis labels; dated evidence box rule |
| `--tint-def` | `#EDE3D0` | definition callout background |
| `--tint-thm` | `#F7EDE2` | theorem panel background |
| `--hairline` | `#DCCFB4` | reserved hairline rule value |
| `--kt-head` | `#DCCFB4` | key term header band field |

## 4. Type

**Two families only.** Jost for display, IBM Plex Sans for text.

| Element | Face | Size | Leading | Color |
|---|---|---|---|---|
| Body | Plex Sans Text | 11 | 16.5 | ink |
| Body, bold run-in | Plex Sans SemiBold | 11 | 16.5 | ink |
| Part label | Jost Medium | 9 | 11 | amber |
| Chapter title | Jost SemiBold | 27 | 30 | navy |
| Slot label (Opening case, Theorem n) | Jost SemiBold | 8.5 | 10 | amber |
| Case title | Jost SemiBold | 15 | 17 | navy |
| Provenance line | Plex Sans SemiBold | 7 | 9 | amber |
| Dated box date label | Plex Sans SemiBold | 7 | 9 | amber |
| Dated box text | Plex Sans Text | 10 | 14.6 | ink |
| Section heading | Jost SemiBold | 14 | 17 | navy, numeral amber |
| Definition label | Plex Sans SemiBold | 7 | 9 | amber |
| Definition term | Plex Sans SemiBold | 11 | 13 | navy |
| Definition text | Plex Sans Text | 9 | 12.85 | ink |
| Theorem statement | Jost SemiBold | 12.5 | 15 | navy |
| Theorem body | Plex Sans Text | 10.5 | 15.5 | ink |
| Figure number | Jost SemiBold | 9 | - | amber |
| Figure caption | Plex Sans Italic | 9 | 12.2 | ink |
| Key term (header band) | Plex Sans SemiBold | 11 | 13 | navy |
| Key term definition | Plex Sans Text | 9.5 | 13.4 | ink |
| Tail head (summary, key terms, problems) | Jost SemiBold | 14 | 17 | navy |
| Chapter summary text | Plex Sans Text | 10.5 | 15.5 | ink |
| Discussion numeral | Jost Medium | 11 | 15 | amber |
| Discussion text | Plex Sans Text | 10 | 15 | ink |
| Problem label | Jost SemiBold | 8.5 | 10 | amber |
| Problem title | Jost SemiBold | 11.5 | 14 | navy |
| Problem text | Plex Sans Text | 10 | 15 | ink |
| Model answer label | Plex Sans SemiBold | 7 | 9 | amber |
| Model answer text | Plex Sans Text | 9.5 | 13.8 | ink |
| Table header | Jost SemiBold | 7.5 | 9.5 | amber |
| Table cell | Plex Sans Text | 8.5 | 11.8 | ink |
| Running head | Jost Medium | 8 | - | amber |
| Folio | Plex Sans Text | 9 | - | folio grey |

Body is justified with automatic hyphenation. Paragraph spacing is 6.8 pt, giving a
baseline-to-baseline interval of 23.3 pt across a paragraph break. No first-line indents.

Letter-spacing on display elements, measured from v5: part label 0.238em, slot label
0.215em, running head 0.196em, definition label 0.14em, theorem label 0.16em, key term
label 0.09em, chapter title -0.009em.

## 5. Apparatus

**Definition callout.** Floats right, 154.1 pt wide including padding (`box-sizing:
border-box`; without it the padding is added to the width and the box renders 20 pt too
wide). Padding 8 / 8.6 / 7.7 / 8.6. Background `--tint-def`, 2 pt `--amber` top border. Gutter
to body text 15.8 pt, giving a 190.1 pt narrow measure. Placement rule: the callout is
positioned immediately before the paragraph in which its term is first used.

**Theorem panel.** Full measure, background `--tint-thm`, 3 pt `--amber` left border,
padding 12.9 / 16 / 11.9 / 16, margins 17.3 above and 17.2 below.

**Provenance line.** 7 pt Plex Sans SemiBold, amber, uppercase, letter-spacing 0.14em, set
flush left directly under the opening case title, 5 pt below it and 12.5 pt above the first
paragraph. It carries either the date range of the episode ("Dated: June 2025 to June 2026")
or the constructed-data label for the Chapter 9 and Chapter 13 openers ("Constructed: not a
real organization").

This one device discharges two locked editorial rules at once: the fifty-year rule, which
quarantines perishable specifics inside dated cases, and the constructed-material rule, which
requires constructed material to be labelled as constructed. Quarantine only works if the
reader can see the quarantine wall, and before v6.4 nothing typographically distinguished a
dated case from timeless argument prose. A reader in 2032 can now tell at a glance which
material is time-stamped and which is the argument. Every opening case carries the line
without exception; the case title's bottom margin assumes it is present.

**Dated evidence box.** The single-paragraph dated reference inside the teaching body, which
the case reuse policy defines as not a featured slot. Full measure, no fill, 1.5 pt `--axis`
left rule, 12 pt left padding, 12.5 pt margins above and below, 9.5 pt when two boxes are
consecutive. A 7 pt amber date label sits above the text, which is set 10 pt on 14.6 pt.

The absence of a fill is the point. The theorem panel is filled and amber-ruled, and evidence
must not compete with the registry for weight. A neutral rule and an amber date label read as
provenance rather than as a second kind of authority.

**Footnotes.** Full source citations sit at the foot of the page carrying the claim.

This amends B.8 of the Consolidated Specification, which ruled author-date inline with the
bibliography at back. Ruled on 2026-07-26: footnotes by page, with the back-of-book
bibliography retained as the aggregated list. This requires an addendum entry to the
consolidated specification, continuing the decision log from Decision 21. The reasoning is
that the book's sources are largely perishable web content requiring an archive capture date,
which is unwieldy inside a parenthetical and reads naturally in a note, and that notes-plus-
bibliography is house style at both target presses.

Inline author-date parentheticals are removed where a footnote carries the same source. The
two together are redundant, and the dates the reader needs are already visible in the prose
and in the provenance and dated-box labels.

| Element | Value |
|---|---|
| Call | 7 pt Plex Sans, amber, superscript |
| Marker | 7 pt Plex Sans, amber, superscript, 2.5 pt right padding |
| Note text | 8 pt Plex Sans Text on 11 pt, ink, ranged left, no hyphenation |
| Separator | 0.5 pt `--axis`, full measure, 11 pt above and 5.5 pt below |
| Measure | Full measure. Not negotiable, see below. |
| Policy | `footnote-policy: line` |

**The footnote area must be full measure.** Set narrower (168 pt was tried first), each note
runs to four or five lines, the area grows past 100 pt, and WeasyPrint cannot fit it on the
calling page, so it defers the note to the next page. Footnote 1 was called on page 1 and
printed on page 2. `footnote-policy: line` does not rescue this: it moves the calling line
only, and does not help when the call sits mid-page with a page of text after it. Full measure
keeps each note to two lines and the defect disappears. Verified by QA gate 8, which checks
that every note prints on the page of its call.

The separator uses `--axis` rather than `--hairline` because the key term header bands use the
hairline value as a field, and a full-measure hairline rect at the page foot is indistinguishable
from a key term band to rect-based QA. Two elements sharing a color made a gate lie once
already; see the gate 4 note.

No chapter-end source list is added. The chapter skeleton is fixed at six slots with no
optional slots, a chapter-end sources block would be a seventh element, and the footnotes now
carry full sources on the page where they are needed. The working content drafts carry a
"Sources referenced" section as a drafting aid; it does not survive into the typeset chapter.

**Figures.** Full measure. SVG `viewBox` must be sized to actual content; WeasyPrint clips
silently on overflow and renders blank bands on excess. Figure blocks carry
`break-after: avoid` so a figure travels with the paragraph that discusses it, which is why
Figure 1.1 sits at the head of page 5 rather than in the gap at the foot of page 4.

## 6. Key terms, slot 5 (Option C, tinted row register)

Revised from Option B (ruled register) on 2026-07-25 to carry more color and to echo the
definition callouts in the body.

Rationale: Chapter 3 carries eleven key terms. A single tinted panel spanning all entries
breaks badly at that length because WeasyPrint moves an entire `break-inside: avoid` block to
the next page rather than splitting it. Tinting each entry separately avoids that: the list
is `break-inside: auto` and each entry is its own `break-inside: avoid` block, so a long
register flows across a page break at entry level with every entry intact. The tint and the
amber rule are borrowed from the callout rather than invented, so the register adds color
without adding a new decorative vocabulary.

Structure: one entry per term, each a full-measure echo of the definition callout, and each
divided into a header band and a definition field.

- 2 pt `--amber` top rule across the full measure.
- Header band, full bleed to the entry edges, filled `--kt-head`, padding 5.4 / 9 / 5 / 9 on
  a 13 pt line. It carries the term alone, in 11 pt Plex Sans SemiBold navy, sentence case,
  matching the callout term exactly, ranged left at 77.4 pt on the same edge as the
  definition text beneath it.
- Definition field, filled `--tint-def`, padding 7 / 9 / 8 / 9, set in 9.5 pt Plex Sans Text
  on 13.4 pt, ranged left, no hyphenation.
- 6.5 pt of space to the next entry.

The section heading carries no rule of its own; the first entry's amber rule serves that
purpose.

**Entries are not numbered.** Numerals were tried in v6.2 and removed: they competed with the
terms for attention and implied a sequence the register does not have. The key terms slot is a
reference list, and its entries are peers. The amber top rule carries the color the numerals
were carrying. Any ordering the list does have lives in the order of the entries themselves,
not in a label.

Entries are plain blocks with `break-inside: avoid`, on a list set `break-inside: auto`, so a
long register flows across a page break without splitting an entry and without separating a
header band from its definition. `box-sizing: border-box` is required on the entry, or the
padding widens it past the measure. Verified at eleven entries: six on the first page, five
on the second, header band count equal to definition field count on both.

## 7. Chapter tail: slots 4 and 6

Slot 4 is the chapter summary, slot 5 the key terms, slot 6 the discussion questions and
problems. All three carry the same 14 pt head so the tail reads as one family.

**Chapter summary (slot 4).** Head, 2 pt `--amber` rule, then a single paragraph at 10.5 pt on
15.5 pt. The larger size against the 11 pt body is deliberate: the summary is one paragraph
and is read as a statement, not as continuing prose.

**Discussion questions (slot 6, first part).** An amber slot label with a 2 pt `--amber` rule
beneath it, then a two-cell table per question: 22 pt numeral column in 11 pt Jost Medium
amber, body in 10 pt on 15 pt, ranged left. Each question is `break-inside: avoid` on a list
set `break-inside: auto`, the same mechanism as the key terms register.

**Problems (slot 6, second part).** Same labelled-and-ruled head. Each problem carries a label
line, a title, the problem statement, and, where the fading policy calls for one, a model
answer.

**The fading marker is a word, not a graphic.** The label reads "P1 · WORKED",
"P3 · COMPLETION", "P2 · UNGUIDED". A graphical guidance meter was considered and rejected
against the locked pedagogy commitment that the book carries no decorative apparatus. The
fading policy is information, so it is set as information. The label is 8.5 pt Jost SemiBold
amber, the same face and size as the "Opening case" slot label, because it does the same job:
naming what the reader is looking at.

Without the marker the fading policy is invisible, and a book that withdraws scaffolding
between Chapter 7 and Chapter 12 without saying so does not read as a design. It reads as a
book that got harder. The marker converts a hidden pedagogical decision into a stated one.

The label carries `break-after: avoid` so it cannot be stranded at the foot of a page while
its title starts the next. This is checked by QA gate 10, which was written after the defect
appeared in the first build of this section.

**Model answers.** Ruled 0.5 pt `--amber` above and below, no fill, 9.5 pt on 13.8 pt, with a
7 pt amber label for each part ("Model reply", "Annotated reasoning", "Model inventory"). The
treatment is deliberately distinct from the three existing panels: the definition callout is a
tinted float, the theorem panel is tinted with an amber left rule, the dated evidence box has
a neutral left rule and no fill.

Model answers are `break-inside: auto`. A worked model reply runs long and must be allowed to
break; WeasyPrint's default `box-decoration-break: slice` puts the top rule on the first
fragment and the bottom rule on the last, with no rules at the break itself, which is the
correct reading.

**This treatment is reused by the craft section (slot 3).** The craft section presents
procedure, template, and fully worked example, and its worked example is the same kind of
object as a model answer. Designing one device for both is the reason the model block is
defined here rather than inside the problems styling.

**Tables.** Amber 7.5 pt uppercase headers over a 1 pt `--amber` rule, cells at 8.5 pt on
11.8 pt with 0.5 pt `--hairline` rules between rows, `break-inside: avoid` on the row and
`auto` on the table so long tables break at row level. A completion problem's blank column
uses `td.blank`, which draws a 58 pt `--axis` rule for the reader to write on rather than a
row of underscores.

## 8. Build

```
python3 -c "from weasyprint import HTML; HTML('AIOM_ch01.html', base_url='.').write_pdf('out.pdf')"
```

`base_url='.'` is required for font and asset resolution. WeasyPrint 69.

**Fonts.** Stage to `fonts/use/`. Copy files individually; shell brace expansion fails in
this environment.

| File | Source |
|---|---|
| `IBMPlexSans-Text.ttf`, `-SemiBold`, `-Medium`, `-Italic` | IBM/plex release `@ibm/plex-sans`, `fonts/complete/ttf/` |
| `Jost-Medium.ttf`, `Jost-SemiBold.ttf` | Google Fonts `ofl/jost/Jost[wght].ttf`, instanced at wght 500 and 600 with `fontTools.varLib.instancer` |

## 9. QA gates, all must pass before delivery

All nine are implemented in `AIOM_build.py` and run automatically after every render.

1. Zero characters past the right measure (428.4 pt recto, 417.6 pt verso, 1.5 pt tolerance).
2. Zero em dashes and zero en dashes.
3. Running head and folio present on every page; no running head on the chapter opener.
4. Every definition callout intact and not split across a page break. Blocking. When it
   fails, run `place.py` on the chapter (see section 11).
   Scoped to boxes narrower than 200 pt, or the key term fields register as false positives
   since they share `--tint-def`.
5. Only the six expected font faces present.
6. Key term header band count equals key term field count, so no entry is separated from its
   header by a page break. Scoped to full-measure bands, or the footnote separator counts as
   a band.
7. The opening case carries a provenance line.
8. Every footnote prints on the page carrying its call. Calls and markers are both 7 pt amber
   Plex Sans; they are told apart by the left edge, a marker sits flush to the measure and a
   call does not. Both are set in regular weight so they cannot be confused with the 7 pt
   SemiBold amber labels used by the provenance line and the dated boxes.
9. Every dated evidence box renders its left rule, and the rule renders as a hairline of at
   most 3 px at 110 dpi rather than a filled block. Verified by pixel sampling, not by rect
   inspection, for the reason in section 10. Dated box labels are distinguished from the
   provenance line by the left edge of the label line: the provenance line is flush to the
   measure, a dated box label is indented past the rule and padding.
10. No problem label is stranded on a page without its title. Verified negatively: with
   `break-after: avoid` removed, the gate correctly reports "P3 · COMPLETION" stranded on
   page 10. A gate that has never failed has not been tested.

## 10. Known CSS and WeasyPrint pitfalls

- `box-sizing: border-box` on any fixed-width padded box, or padding inflates the width.
- Unicode escapes in CSS `content:` strings consume the following space as an escape
  terminator. Use literal UTF-8 characters.
- Hex escapes followed by hex-like letters parse as one invalid codepoint and can silently
  suppress running heads. Use literal characters.
- SVG `rx` renders as curve paths, invisible to pdfplumber `.rects`. Verify by pixel sampling.
- Long tables with `break-inside: avoid` jump entirely to the next page. Use `auto`.
- Floated boxes ignore `break-inside: avoid` in WeasyPrint 69 and will split across pages.
  Verified directly on 2026-07-26 rather than inherited: a floated box carrying
  `break-inside: avoid`, pushed onto a page boundary at six different offsets, split at three
  of them. There is no CSS fix. See section 11.
- A narrow `@footnote` area is a trap. Notes grow taller than the page can accommodate and
  WeasyPrint silently defers them to the following page, breaking the one promise footnotes
  make. Keep the area at full measure.
- Every time two elements are given the same color, a rect-based QA gate starts lying. The key
  term bands, the footnote separator, and the definition callouts have each triggered a false
  positive in some gate. Prefer a distinct token, or scope the gate by width.
- A box with a background fill exposes its borders to pdfplumber `.rects`: WeasyPrint paints a
  rect the size of the border box in the border color, then the background over the padding
  box. A box with **no** fill draws its borders as paths instead, which are invisible to
  `.rects` entirely. The dated evidence box has no fill, so its left rule can only be verified
  by pixel sampling. Do not conclude a rule is missing because no rect appears.

## 11. Callout placement pass (resolves the v5 split defect)

Floated definition callouts split across page boundaries, and `break-inside: avoid` does not
prevent it in WeasyPrint 69. This was carried as a tolerated defect from v5 through v6.6. It
is now resolved, and gate 4 is blocking rather than advisory.

**The fix is placement, not CSS.** The design is untouched. `place.py` renders the chapter,
detects any callout that split, moves it to a neighbouring anchor paragraph, and re-renders,
repeating until every callout is intact. Chapter 1 resolved in three renders: "Access price"
moved one paragraph later, "Meter relocation" one paragraph earlier.

**Constraints on a move.** A callout may only move within its own section, so a term is never
defined outside the section that uses it. Moves are tried nearest-first and earlier before
later, because moving a callout earlier keeps it before the paragraph that first uses its
term, which is the placement rule in section 5. A later move is taken only when no earlier
move resolves the split.

**What this costs.** The placement rule becomes a preference rather than a guarantee. A
callout may end up immediately after the paragraph that first uses its term rather than
immediately before it, and two callouts may end up adjacent. Both happened in Chapter 1:
"Access price" now follows its anchor paragraph and sits directly beneath "Software access
model" on page 3. Ruled acceptable on 2026-07-26: an intact callout a paragraph out of place
reads better than a callout cut in half by a page break.

**Adjacent callouts are sorted into prose order.** When the placement pass pushes two callouts
onto the same anchor, document order need not match the order the reader meets the terms.
After placement, `place.py` finds each run of adjacent callouts and sorts it by the character
offset of each term's first use in the body prose, with the callouts themselves excluded from
that search so a term does not match its own definition. The result is re-rendered and
verified; if the reorder were to reintroduce a split, it is reverted and the placed order
stands.

On Chapter 1 page 3 this puts "Access price" above "Software access model", matching the
prose, where placement alone had left them the other way round. Ruled on 2026-07-26: an
intact callout may sit a paragraph away from its anchor, but a reader must never meet two
definitions in the wrong order.

**The pass is idempotent.** Running it on a resolved chapter renders once, finds nothing, and
leaves the file byte-identical. Verified.

**When to run it.** After any prose edit that changes pagination. Gate 4 tells you when it is
needed; `place.py` is not part of the normal render path because it rewrites the chapter file.
It writes a `.bak` beside the chapter before it starts.

## 12. Addendum, 2026-07-28

**Version 6.7 of the CSS. Decision 37: figure fills use `--tint-fig`.**

A new token, `--tint-fig: #E7DECB`, is reserved for filled areas inside figures.
Figures never use `--tint-def` or `--tint-thm`.

Those two tints identify the definition callout and the theorem panel to the
rect-based gates. Figure 1.2 carried a full-measure meter band filled
`--tint-def`, and gate 6 counted it as an eighth key term field against seven
header bands, reporting a defect in a register that was correct. This is the
fourth time two elements sharing a color have made a gate lie, and the first
time the collision came from a figure rather than from apparatus.

The value sits one step deeper than `--tint-def` so that a filled figure band
reads as recessed rather than as a callout that has lost its rule. Figures
carry the literal hex, as they already do for `--amber-fig`, `--teal` and
`--axis`; the token is the value of record.

**Figure 1.2 is now rendered and gated.** The anatomy figure was specified but
never built through v14. It renders correctly: a three-box pipeline with
arrows, dashed drops to a full-measure meter band, and a dashed drop from the
band to the record note. No clipping, no blank bands, `viewBox` sized to
content.

**The craft section is typeset for the first time.** Slot 3 was absent from
every proof through v14. It reuses the `.model` treatment as section 7
anticipated, and the reuse holds: procedure prose, then a labelled model
inventory with four `mlab` parts. No new styling was required, which is the
result section 7 predicted when it defined the model block outside the problems
styling.

**Chapter 1 at full length is 17 pages.** Every prior proof measured a partial
chapter. The 350 to 450 page target for the book assumed roughly 19 to 20 pages
per chapter, and Chapter 1 is specified as one of the two tightest.

## 13. Addendum, 2026-07-28, second entry

**Decision 38: chapter source register, classed as apparatus.**

This amends the rule in section 5 that no chapter-end source list is added. That
rule reasoned from the fixed six-slot skeleton: a sources block would be a
seventh element. The amendment holds the skeleton and reclassifies the element.

The skeleton governs pedagogical content. Running heads, folios, and footnotes
already sit outside the six slots without violating it, because they are
apparatus. A source register is the same category.

**The test, so the exemption has a boundary.** Apparatus carries no pedagogical
content and could be stripped without changing what the chapter teaches. A
worked example fails that test. A source list passes it. Nothing else is
admitted to the chapter end on this reasoning without meeting the same test.

**Why two levels rather than one.** Section 5 documents that a tall footnote
area is a trap: notes grow past what the page can hold and WeasyPrint defers
them to the following page, breaking gate 8. Full citations with URL and access
date run four or five lines each and would do exactly that. Page notes therefore
carry the short form, enough to identify the source at the point of the claim,
and the register at the chapter end carries the full citation.

**Decision 39: Chicago 17, notes and bibliography, with access dates.**

MLA was considered and set aside on fit. It is the humanities standard, and both
target presses use notes-plus-bibliography, which is Chicago. Chicago normally
reserves access dates for undated sources but permits them and recommends them
for content likely to change. This book's sources are largely perishable web
content, which is that case exactly.

Access dates also serve the fifty-year rule directly. A reader in 2032 who finds
a dead link needs the capture date to search an archive, and Chicago carries it
in a standard position rather than an invented one.

**Styling.** Amber slot label over a 0.5 pt `--axis` rule, distinguishing it from
the 2 pt amber rules that head the six slots. Entries at 8.5 pt on 12.2 pt with a
14 pt hanging indent, ranged left, no hyphenation, `break-inside: avoid` per
entry on a section set `auto`. No fill: a filled full-measure block would collide
with gate 6, per the figure fill rule.

**Outstanding.** Access dates record verification against the live record on
2026-07-28. Verification is not archival capture. Five of the seven entries also
lack exact permalinks. Both must close before the chapter locks, and neither can
be done from inside the build.

## 14. Addendum, 2026-07-28, third entry

**Decision 40: archival standard for cited sources.**

Two parts, in order. Upgrade before archiving, because upgrading changes what
gets archived.

**Part one, source upgrade.** Cite the most durable available form of the claim.
A number disclosed in an earnings call and also filed with the SEC is cited to
the filing, because EDGAR outlives every vendor link. Documentation published
from a public repository is cited to a permalinked revision rather than to the
live page, which pins the exact text relied on. A claim carried only by a social
post gets a second independent path, cited with Chicago's "quoted in"
construction. A DOI needs nothing further.

**Part two, triple capture.** Perma.cc, built at Harvard Law Library for citation
rot and used by law reviews and university presses. The Wayback Machine, free
and universally recognized. And a local dark archive under the author's control,
named to match the citation. One archive is a single point of failure for a book
aiming at fifty years, and the local copy is the one that lets a press verify a
claim without chasing links.

**Register entry format.** Original URL, then archive link, then access date. The
access date records actual capture, not verification against the live record.

**This is enforced at G1 and it is blocking.** The prior wording, "every source
archived," was too vague to fail on. It now reads as four separate checks: source
upgrade considered, both public captures made, local copy filed, register entry
carrying all three fields.

**Why this book in particular.** The design already quarantines perishable
specifics inside dated cases and provenance lines, on the reasoning that a reader
in 2032 must be able to tell time-stamped material from timeless argument. That
commitment only pays off if the quarantined material is still retrievable. A
dated case pointing at a dead link is worse than no case, because it looks like
evidence and is not.
