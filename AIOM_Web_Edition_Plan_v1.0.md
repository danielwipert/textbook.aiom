# AIOM Web Edition: plan v1.0

Status: **ADOPTED 2026-08-13.** All five opening decisions are ruled and are
logged as Decisions 60 through 64 in `AIOM_Workplan_v5.md`, which is the numbering
authority. Section 7 records them. **Phases W1 and W2 are built and green as of
2026-08-13, and Phase W3, the front door, followed the same day. Phase W4, the
reference layer and search, followed, and Phase W5, the site build and deploy,
is built. Host and analytics are ruled as Decisions 65 and 66.
Only the DOMAIN is outstanding.**
Sections 8 through 11 record what each phase learned.

The web edition is a second PRESENTATION of the book, never a second text. That
sentence is the whole plan, and gate W1 in section 3 is what makes it true rather
than intended.

---

## 1. The finding that should decide the architecture

The four files in `Web Version/` are a retired pipeline, and two of them are
already in the repository.

| File | What it actually is |
|---|---|
| `convert_ch1.py` | Byte-identical to the repo's `convert_ch1.py`. Already here. |
| `aiom_registry.py` | Byte-identical to the repo's `aiom_registry.py`. Already here. |
| `aiom_md.py` | **Deleted from the repo on 2026-08-10, commit `0f4f3ea`, on Dan's ruling.** Its docstring asserts the premise Decision 50 overturned: "The canonical source for a chapter is AIOM_chNN.md." |
| `AIOM_ch01.md` | **Byte-identical to `archive/AIOM_ch01_markdown_noncanonical.md`.** Named noncanonical by whoever archived it. |

The markdown chapter is not merely an older draft. It is a **pre-fact-check**
draft, and it carries sentences that Stages 3 and 7 cut on the record:

- "after which usage continued to bill against real rates" is the automatic
  continuation mechanism that SF2 removed on 2026-08-06. The register note on
  `truell-2025-pricing` states the reversing condition and it has not been met.
- "the upstream cost of serving heavy users under a flat price had become
  untenable" is the shape FC9 cut on 2026-08-13, an inferred economic mechanism
  presented as Truell's explanation.
- "Anthropic introduced and then tightened usage limits" restores the word
  *introduced* that the note on `techcrunch-2025-anthropic-limits` explicitly
  forbids.
- The whole file predates the Stage 6 copy edit, Decision 58 (`.nb`), Decision 59
  (`lang="en-US"`), and gate 15.

Building the website from that file would ship, under the book's name, claims
Dan ruled out. It would also be the fifth instance of the failure CLAUDE.md
section 10 names: a ruled claim narrowing reverted with every date and figure
intact, so no check on values can see it go.

**RULED as Decision 61: the markdown pipeline is retired permanently, and the web
edition is built from the locked chapter HTML, which is Decision 50 already.** The
uploaded folder is worth keeping only as evidence that the idea was tried. The
one part worth carrying forward is the *directive vocabulary* in `aiom_md.py`
(theorem, lemma, figure, definition, evidence, problem, provenance), which is a
good taxonomy. The locked HTML already expresses every one of those as a class:
`.theorem`, `.definition`, `.dated`, `.problem`, `.provenance`, `figure`. Nothing
is lost by dropping the parser.

---

## 2. What the locked HTML already gives the web for free

Chapter 1 was inspected directly. It is in unusually good shape for a second
renderer:

- **Semantic, class-driven, no inline styles.** The CSS header rule holds: "This
  file is the sole control of appearance. Chapter HTML files carry content only."
  So a second stylesheet is a complete second design, not a fight with the first.
- **Figures are inline SVG**, not raster. They scale, they are selectable, they
  are accessible, and they need no export step.
- **Citations are `<cite src="key">` elements** carrying source keys and an
  editorial gloss, resolved against a JSON source register embedded in the file
  itself (Decision 51). `footnotes.py` and `cite_format.py` already turn those
  into formatted footnote text. The web renderer reuses both and changes only the
  presentation: sidenotes rather than page-bottom footnotes.
- **The six-slot skeleton is a navigation spine that already exists.**
  `.slot-label` marks every one. The web gets a sidebar, a progress rail, and
  deep links out of structure that is already in the file.
- **The design tokens are already a palette.** `--paper #F4ECDD`, `--navy
  #16314F`, `--amber #B4551F`, `--teal #0E7A72`, `--ink #2B2620`, plus the three
  tints. Jost for display, IBM Plex Sans for text, both committed under `fonts/`
  with OFL licences, so the site self-hosts its fonts and calls no CDN.

What does **not** transfer: `@page` geometry, point units, the floated definition
callout, `place.py`, and gates 1, 4, 8, 12, 13 and 14, which are all pagination
checks. A large part of the print build's complexity simply does not exist on the
web.

---

## 3. Recommended architecture

One source, two renderers.

```
Drafts/ChNN_*/00_Stage0_Draft/AIOM_ChNN_redraft.html   <-- the single source
        |                                                  (Decision 50)
        |
        +-- AIOM_build.py  + AIOM_book.css  --> print PDF   (exists, 15 gates)
        |
        +-- web_build.py   + AIOM_web.css   --> static site (new)
                 |
                 +-- reuses footnotes.py, cite_format.py, status_check.py
```

**Language: Python, plus Jinja2, plus vanilla JavaScript. Decision 62.** No Node
toolchain. The repository is already a Python build system with a pinned
`requirements.txt` and a one-command build, and `web_build.py` sits beside
`AIOM_build.py` and imports the same citation modules. The decisive argument is
that citation formatting, gate W1's PDF extraction, and lock status are all
already Python, so a JavaScript build would not remove Python from the build. It
would put the language boundary in the middle of the citation path, and a second
implementation of citation text is a second source of truth for it. Jinja2 is the
only new pinned dependency.

**The toolchain does not constrain the design, and this was tested rather than
assumed.** Scroll-driven animation (`animation-timeline: scroll()`), cross-page
morphing (`@view-transition`), container queries, `text-wrap: pretty`, variable
font interpolation and `scroll-snap` are browser platform features, available to
any static page regardless of what emitted it. The one place a framework could
have raised the ceiling is rich interactive figures, and Decision 62 keeps that
door open by permitting a self-contained island on any figure that earns one.
Figure 1.1 is the obvious first candidate: a usage slider where the reader drags
consumption and watches the seat-model line stay flat while the event-model area
accumulates. That is a thing the PDF structurally cannot do, and this book is full
of that shape.

**Output: a fully static site.** HTML, CSS, self-hosted fonts, inline SVG, one
small JavaScript bundle for the reader chrome and search. It hosts on Cloudflare
Pages or GitHub Pages behind a custom domain, costs nothing to run, and cannot
break at request time. Rendered output is never committed (Decision 63), so a
chapter's text exists once in version control rather than twice.

### The gate that matters most

The recurring failure in this repository is not a bad judgment call. It is a
check that reads green while measuring nothing, or two artifacts of one chapter
that silently disagree. A second renderer is a machine for producing exactly
that, so the web build carries a control the print build never needed:

- **Gate W1, text equivalence.** AS BUILT, and this is sharper than the sentence
  that stood here before W1: the comparison is against the PRINT HTML, the exact
  document WeasyPrint receives, not against text extracted from the PDF. Both
  artifacts descend from one `footnotes.inject()` call, so the gate measures the
  web transform rather than pdfplumber's line joining, and it needs no tolerance.
  Two channels, both exact. Channel A is the prose with all footnote apparatus
  removed from both sides. Channel B is the ordered list of note texts. Any
  divergence in either fails the build. The web edition is a second
  *presentation*, never a second text, and this is the check that keeps it honest.
- **Gate W2, lock status.** `web_build.py` refuses to publish a chapter that
  `status_check.py` does not report at Stage 9. Publishing an unlocked chapter
  means publishing pre-fact-check prose to the open internet. A `--preview` flag
  builds it to a local, `noindex`, unlinked path for review.
- **Gate W3, marks.** Port gate 2 (no em dash, no en dash) and gate 15 (no
  straight quote or apostrophe) to the rendered web output. Both are properties
  of the text, so both apply.
- **Gate W4, links and anchors.** Every internal link resolves, every anchor is
  unique, every `<cite src>` key resolves in the chapter's register, every figure
  is referenced in the prose it sits beside.
- **Gate W5, `lang="en-US"`.** Decision 59. Cheap, and invisible when omitted.
- **Gate W6, horizontal overflow.** ADDED IN W2. Loads the page at twenty viewport
  widths from 320px to 2560px and fails if the document scrolls sideways. The web
  analogue of print gate 1, and worse in its symptom: print puts one element off
  the paper, while a horizontal document scroll drags every block on the page with
  it. The only optional gate, because it needs a headless browser. It prints
  SKIPPED, appends "W6 NOT RUN" to the verdict line, and is never counted as
  passed. Skip it deliberately with `--no-browser`.

Gate W1 is the whole discipline of this project transposed into a new medium. I
would build it before building a single page.

---

## 4. The site

Four surfaces, in build order.

**1. The reader.** The core, and the thing that has to be excellent. One chapter
per page. Measure held near 34em. The six slots become a sticky left rail that
tracks reading position, so the reader always knows whether they are in the
opening case, the teaching body, or the problems. Definition callouts become
margin cards on a wide screen and inline cards on a narrow one. Citations become
sidenotes, numbered, expanding in place on a small screen. Registry panels keep
their formal typography and their object ID, because the ID is what a reader
follows to the verbatim statement, and that promise is what makes the panel
trustworthy (CLAUDE.md rule 4a). Figures animate in on first scroll, once, and
never again. A per-chapter progress bar, a next and previous pair, and a
keyboard shortcut layer.

**2. The front door.** The landing page carries the argument, not a book jacket:
the category error stated in one screen, the two named layers (AI Business
Economics as the science, AI Operations Management as the practice), the four
parts, and one unambiguous "Start reading" action. This is the surface where the
inspiration site matters most and where I most need your input (section 6).

**3. The reference layer.** Three generated indexes, all built from data the
repository already holds:

- **Glossary**, from the key-terms slots plus `AIOM_Continuity_Ledger.md`, which
  already records which chapter owns which term. Every term links to the chapter
  that defines it.
- **Object index**, from the registry objects cited in chapters: `/objects/thm-009`
  showing the verbatim statement and every chapter that invokes it. This is the
  thing a PDF cannot do, and it is genuinely distinctive. It is also the one place
  the project could go wrong: **the registry justifies the book, it does not
  organize it** (CLAUDE.md rule 4). The object index is an appendix reached from
  chapters. It is never the navigation spine, and no chapter page is ever laid out
  around registry objects.
- **Sources**, per chapter, from the Decision 51 register already embedded in each
  chapter file. This turns the book's sourcing discipline into a visible feature
  rather than a footnote apparatus.

**4. Search.** A prebuilt JSON index over chapter text, terms, and object IDs,
queried client side. At fifteen chapters of roughly seven thousand words each the
whole index is small enough to ship in one request.

### Look and feel

The palette is not chosen, it is inherited, and that is a strength. The print
book is warm paper, deep navy, amber accent, teal second accent. A site built on
those tokens will look like the book rather than like a template, and it will
look like nothing else in this category, which is uniformly cold white and blue.
Dark mode needs a designed inverted palette, not an automatic filter: the warm
paper has no correct automatic inverse. The SVG figures carry literal hex fills
and will need a token pass before dark mode is credible, which is an argument for
shipping light-first and adding dark mode as its own piece of work.

---

## 5. Phasing

Chapter 1 is the exemplar the other fourteen are drafted against, and it is the
only locked chapter. The web edition should be built the same way: prove the whole
pipeline on one chapter before scaling it.

- **Phase W0, decisions. CLOSED 2026-08-13.** Section 7, Decisions 60 to 64.
- **Phase W1, the pipeline. BUILT AND GREEN 2026-08-13.** `web_build.py`,
  `AIOM_web.css` v0.1, `web_templates/`, and gates W1 to W5 rendering Chapter 1.
  Chapter 1 reports 43,204 characters of prose identical to print, six footnotes
  identical, all six slots anchored, twenty-six unique anchors, both figures
  captioned and referenced. `web_gates_selftest.py` runs twenty-seven negative
  controls and all twenty-seven behave. What W1 deliberately did NOT do: the
  visual direction, which is W2, and the inspiration site, which is still
  unreviewed. See section 8 for what W1 learned.
- **Phase W2, the reader. BUILT AND GREEN 2026-08-13.** The full reading experience on Chapter 1: slot rail,
  sidenotes, margin definitions, progress, motion, responsive behaviour, keyboard
  layer. Design review against the same standard the print book gets.
- **Phase W3, the front door. BUILT AND GREEN 2026-08-13.** Landing page, table of contents, about, the
  author. Depends on the section 6 input and on Decision W-A below.
- **Phase W4, the reference layer and search. BUILT AND GREEN 2026-08-13.** Glossary, object index, sources,
  search index.
- **Phase W5, deploy. BUILT 2026-08-13, pending Dan's domain and host rulings.** Domain, hosting, analytics posture, and the build hook that
  publishes a chapter when it locks.
- **Phase W6, dark mode and the SVG token pass.** Separable, and deliberately last.

Phases W1 and W2 are the sub-project. W3 to W6 are comparatively mechanical once
W1 holds.

---

## 6. What I could not do, and what I need

**I could not review messyjobs.ai.** The container's network egress proxy refuses
the domain: `gateway answered 403 to CONNECT (policy denial)`, confirmed against
the proxy status endpoint. A text-extraction proxy was blocked the same way. A web
search establishes what the book is (Garicano, Li and Wu, *Messy Jobs: The Work
That AI Cannot Reach*, LSE and HKU CAMO, launched June 2026) but says nothing
about the site's design, which is what was actually asked for.

Nothing in this plan is derived from that site, and no description of it should be
assumed. Three ways to close the gap, any one is enough:

1. Add `messyjobs.ai` to the environment's network allowlist and I read it
   directly.
2. Send screenshots of the pages that made the impression: landing, a chapter,
   the navigation.
3. Tell me in a sentence or two what specifically appealed. Whether it was the
   typography, the motion, the way the argument is staged on the landing page, or
   the reading experience itself, changes different parts of this plan.

Worth naming a structural difference regardless: *Messy Jobs* is a trade book sold
on Amazon, so its site is almost certainly a marketing surface with samples. What
you described is the entire book hosted as a website. Those are different products
even if they share a visual language, which is Decision W-A.

---

## 7. Decisions, all ruled 2026-08-13

Logged as Decisions 60 through 64 in `AIOM_Workplan_v5.md`. Summarized here; that
file carries the full text and is authoritative.

| | Question | Ruling |
|---|---|---|
| **W-A** | Free full text, or marketing site with samples? | **Decision 60.** Full text free. The paid product is print and ebook plus the apparatus: Appendix A, Northmoor, solutions, instructor materials. Chapters publish as they lock. No free-forever promise is published, so a press conversation stays open. |
| **W-B** | Retire the markdown pipeline? | **Decision 61.** Retired permanently. `aiom_md.py` stays deleted. The archived markdown is kept for its diff value, with a hard warning naming the three retracted claims it carries. |
| **W-C** | Python or a JavaScript framework? | **Decision 62.** Python and Jinja2, no Node, plus self-contained interactive islands for any figure that earns one. |
| **W-D** | One repository or two? | **Decision 63.** This one. Rendered output is not committed. CI builds, gates, and publishes. |
| **W-E** | Which chapters may the site show? | **Decision 64.** Locked only, enforced by gate W2, with a local `noindex` preview path for in-flight chapters. |

Two carry-forward warnings came out of these rulings and are recorded with them:

1. **`archive/AIOM_ch01_markdown_noncanonical.md` must never be read for prose.**
   Section 1 is the reasoning, and `archive/README.md` carries the warning at the
   file itself.
2. **The web render is never the artifact for an external fact check.** It is
   HTML, so it reproduces the extraction phantoms that produced both production
   flags on Chapter 1's first check: the dropped `<li>` contents of the theorem
   panel, and the empty table cells collapsing leftward. Stages 3 and 7 keep
   getting the PDF.

### What is still open, and belongs to Phase W2

Not decisions in the sense above, because they are design questions that want
pixels rather than reasoning:

- **The visual direction itself.** Nothing is settled beyond the inherited palette
  and the two committed typefaces.
- **The inspiration site was never reviewed.** Section 6 stands. `messyjobs.ai` is
  refused by the container's egress proxy and no part of this plan derives from it.
- **Dark mode**, deferred to Phase W6 with the SVG token pass, on the reasoning in
  section 4.
- **Which figures earn an interactive island.** Figure 1.1, the seat model against
  the event model, is the obvious first candidate.

---

## 8. What Phase W1 learned

Recorded here rather than left in a commit message, because each of these binds
the phases that follow.

**Equivalence was made structural rather than checked after the fact.** The first
design compared the web output against the chapter source. The shipped design
compares it against the PRINT artifact, because both now descend from one
`footnotes.inject()` call: the web renderer transforms the exact HTML WeasyPrint
receives. That turns gate W1 from a comparison of two implementations into a
check on the web transform, which is the thing that can actually go wrong.

**Gate W1 has two channels because one would have been blurry.** Channel A is the
prose with all footnote apparatus removed from both sides. Channel B is the
ordered list of note texts. Combining them into a single comparison would have
forced a tolerance, and a check with a tolerance is a check that can be talked
into passing. Both channels are exact, and the exclusions are named in the
docstring: SVG figure internals, which are copied byte for byte, and the audit
block, which print also drops.

**THE SELF-TEST IS NOT OPTIONAL AND IT PAID FOR ITSELF ON THE FIRST RUN.** Five of
twenty-five controls did not fire. Four were gate W3's typographic marks, injected
into the chapter title, which lives in `<head>`, which the extractor skips: gate
W3 reported green on four faults it had never seen. The fifth deleted no sidenote
at all. Both were faults in the CONTROLS, not the gates, and that is precisely the
point. Without them, a green W3 was evidence about nothing, which is the failure
CLAUDE.md records five times over. Every gate added in W2 or later gets a control
in the same commit.

**A check rewritten from memory reacquires the defect the original was fixed for.**
The print-side footnote scanner was written to count nested spans, with a comment
explaining that a non-greedy regex truncates a note containing `<span class="url">`.
The web-side note extractor was then written twenty lines later as a non-greedy
regex. There is now ONE `find_spans` used by both sides. This is the same shape as
the hyphenation scan that was rewritten with gate 12's page-boundary blind spot.

**Two faults were found by the gates during the build, and both were real.** Gate
W1a failed at char 0 because the print extractor was reading `<title>`. Gate W4c
found the teaching-body anchor pointing at a target that no longer existed,
because section numbering ran after slot anchoring and overwrote the id. Neither
was visible by reading the code.

**A raster check found what no gate could see.** The sticky header was set at 88
percent opacity with an 8px blur, and body text read straight through it. This is
the web's version of the rule already in force for print: a chapter whose
pagination moves must have its pages READ, not merely gated. Screenshots are part
of a web design review, not a nicety.

**Chrome outside the article is a load-bearing boundary, not a layout choice.**
Gate W1 measures `<article id="chapter-text">` and nothing else, so navigation
labels, the rail, the footer and the progress bar can say anything. Nothing may be
added INSIDE the article, which is why the teaching-body slot takes the first
numbered section's anchor rather than gaining a visible label of its own.

**Open, and carried into W2:**

- The visual direction. W1's stylesheet is v0.1 and restrained by intent.
- The sidenote gutter reads as dead space where a stretch of prose calls no note,
  which is a real design problem at this measure and not a bug.
- The inspiration site is still unreviewed. Section 6 stands unchanged.
- No dark mode, deliberately. It is Phase W6 with the SVG token pass.

---

## 9. What Phase W2 learned

**The dead gutter was a layout error, not a taste problem.** v0.1 made the article
the measure PLUS a sidenote gutter and centred that whole block, so the prose sat
left of optical centre and the empty gutter read as a mistake wherever a stretch
of prose called no note. The reading area is now a three-track grid with the
article in the middle track at exactly the measure. With no note the page is
symmetrical, and a note floats into the track beside it. The same change stopped a
note from landing on the right border of a full-measure box such as `.dated`.

**A RESPONSIVE BREAKPOINT IS ARITHMETIC AND SHOULD BE WRITTEN DOWN AS ARITHMETIC.**
A margin note needs `--note + --note-gap` of side track, and the side track is
`(viewport - --rail - --measure) / 2`, so notes fit only from 1411px up. The first
draft put the breakpoint at 1240px by eye, leaving a 170px band where every note
ran off the right edge of the window. The sum now sits in a comment beside the
media query, because the next person to change the measure will not rederive it.

**GATE W6 EXISTS BECAUSE THE WIDTH SWEEP FOUND SOMETHING NO RENDER SHOWED.** A
sweep across twenty viewport widths caught the P3 inventory table forcing the
whole document to scroll sideways below 390px. On the web that defect is worse
than its print analogue: print gate 1 puts one element off the paper, while a
horizontal document scroll drags every other block on the page with it. The table
is now wrapped in its own scroll box by `wrap_tables`, which adds an element and
no text, so gate W1 is unaffected. That is the test for whether a presentation
change belongs in the transform at all.

**W6 is the only optional gate and it had to be made noisy.** It needs a headless
browser. It prints SKIPPED, appends "W6 NOT RUN" to the verdict line, and is never
counted as a pass. An optional gate that quietly reports success is the exact
failure this repository keeps finding in its own suite.

**Motion is applied by script, never in the markup.** A markup-side `opacity: 0`
plus a scroll observer means a reader with JavaScript disabled gets a blank
column. The script adds the class itself. The observer's `rootMargin` is zero for
a related reason: a negative bottom inset delays the reveal slightly and buys a
bug, because an element sitting entirely inside the inset band at maximum scroll
never intersects and stays invisible with no way to recover it.

**Every gate added in a later phase gets its negative control in the same commit.**
W6 shipped with two, and the self-test is now at twenty-nine controls.

### Open, and carried into W3 or later

- **The inspiration site is STILL unreviewed.** Section 6 stands unchanged. This is
  now the oldest open item on the project and it belongs to the front door, which
  is the surface it would most inform.
- The scrollable table has no visual affordance beyond the cut column edge.
- The rail scrolls away with the page in the last screen of a chapter, which is
  correct sticky behaviour and may still want handling.
- Search, the glossary, the object index and the sources page are all Phase W4.
- Dark mode and the SVG token pass remain Phase W6.

---

## 10. What Phase W3 learned

**The book's shape is parsed, not retyped.** `book_structure.py` reads the four
parts and fifteen chapters out of `AIOM_Structure_v1.md`, which CLAUDE.md already
names as the authority on chapter structure. A Python literal would have been a
second copy of the book's own table of contents, and two copies of one thing that
silently disagree is this project's signature failure.

**GATE W7 GUARDS THE JOINT WHERE THE BOOK COULD SPLIT IN TWO.** A chapter's
published title comes from its own locked HTML. The navigation's comes from the
structure document. Those can drift, and nothing else would notice: the chapter
renders correctly, the nav renders correctly, and they name different chapters.
W7 fails the build on a disagreement, and on a structure document that stops
parsing as four parts and fifteen chapters.

**A GATE THAT ONLY EVER SEES ONE PAGE IS EVIDENCE ABOUT ONE PAGE.** Gates W3 and
W5 had only ever been handed the chapter. The landing page was therefore ungated
from the moment it existed, and it shipped four straight apostrophes that W3 would
have failed instantly had it been looking. Two of the four came from the structure
document, which is planning prose and was never held to the typographic standard.
`gate_pages()` now runs the page-level checks over every page the build emits.

**PLANNING PROSE IS NOT PUBLISHABLE PROSE, and the difference is not stylistic.**
The part descriptions are Purpose lines from the structure document, and only the
FIRST SENTENCE is published. Part III's line continues "Chapter titles use the
manifesto's own verbs. The capstone dataset is introduced at the top of this part
with its construction note. Worked-example fading: completion problems early in
the part, unguided by its end." That is a note to the drafter. No chapter's "Big
idea", "Competency" or "Anchor theorem" line is published at all, because CLAUDE.md
section 9 rules that later chapters withhold things deliberately and an earlier
surface must not front-run them.

**Gate W6 found a regression introduced by the W3 stylesheet itself**, and its
failure message was misleading in the same way print gate 12's is. Adding a buy
CTA to the chapter bar overflowed the row at 320px, and the gate blamed the
inventory table, because an element inside an `overflow-x` container legitimately
extends past the viewport. W6 now excludes elements a scroll container clips, so
it names the element that actually caused the page to scroll.

**What was adopted from the inspiration site, now that it could be seen.** The
rail carries the WHOLE book rather than the current chapter, with the current one
expanded to its slots. The landing page uses a hairline part-card grid with the
numeral as a graphic mark. A persistent buy CTA sits in the bar, which Decision 60
requires somewhere. What was NOT adopted: the palette, which stays inherited from
the locked print system; justified text, which produces rivers; and the lead-capture
chat widget, which is the wrong register for this book.

**Decision W-F, ruled 2026-08-13: the web keeps IBM Plex Sans.** The inspiration
sets body text in a serif. AIOM's body face was established by metric fingerprint
against the v5 design proof, and diverging would mean a reader who buys the PDF and
reads the site sees two visibly different books. Structure was adopted; typography
was not.

### Open, and carried into W4

- **The landing page copy is DRAFT and needs Dan's ruling.** The hero, the lede and
  the editions section are written from ruled material but are not themselves ruled.
  The part descriptions are one-sentence placeholders.
- The site has no author, about, or praise surface. The inspiration has all three.
- Search, the glossary, the object index and the per-chapter sources page are W4.
- Dark mode and the SVG token pass remain W6.

---

## 11. What Phase W4 learned

**Every page in the reference layer is generated from a record that is already
enforced somewhere else.** The glossary and the object index come from
`AIOM_Continuity_Ledger.md`, which gate G3 already checks every chapter against.
The sources come from the chapter's own Decision 51 register through
`cite_format`. Nothing is assembled by scraping the rendered chapter, which would
have made the reference layer a second reading of the book rather than a view of
its records. Scope is then correct automatically: ledger entries are appended at
lock, so a term can only reach the site from a chapter Decision 64 already permits
publishing.

**GATE W8 GUARDS THE JOINT BETWEEN THE TWO.** W8a requires the ledger's definition
of a term to be character-identical to the chapter's key-term text. That is the
right check because a definition is precisely the kind of text that can be
reworded with no date and no figure changing, which is the shape CLAUDE.md records
as having reverted four times on Chapter 1 with nothing mechanical able to see it.
W8b requires every cited key to appear on the sources page. W8c refuses an object
index that claims an object no chapter renders.

**THE SOURCES PAGE IS WHERE URLs BELONG.** Print rules URLs out of footnotes, and
the chapter page matches print so that gate W1's note comparison stays exact and
needs no tolerance. A bibliography is the right home for a URL, so the sources
page is built with `url_policy="full"` while the chapter stays at `"none"`. One
generator produces both.

**A NON-GREEDY REGEX OVER NESTED ELEMENTS HAS NOW BEEN THE DEFECT THREE TIMES IN
ONE FILE.** Gate W8a's first draft matched key terms with
`<div class="kt">(.*?)</div>`, which closes on the nested `.kt-h` div and swallows
the neighbouring terms. The balanced scanner already existed for exactly this and
was not reached for. `find_spans(doc, opener, tag)` now takes a tag, and it is the
tool for any nested element.

**A FAILED SEARCH INDEX MUST NOT BE ABLE TO REPORT "NO RESULTS".** Opened from a
file path the index fetch is blocked, and the first version answered a query with
"No results for meter", which reads as a statement about the book rather than as a
broken page. Load state is now tracked separately from result count. That is the
same error this project spends most of its care preventing in gates, appearing in
a user interface instead.

**The search index is per SECTION, not per chapter.** A hit lands the reader on
the passage rather than at the top of a 25,000 pixel page. Twenty-six entries and
roughly 40 kB for one chapter, so the whole book will still ship in one request.

### Open, and carried into W5

- **The landing page copy is still DRAFT and still needs Dan's ruling.**
- The object index holds one object, because Chapter 1 invokes one. It will look
  thin until Part II lands, and that is honest rather than a defect.
- No author, about, or praise surface yet.
- Deploy, the domain, and the CI workflow are W5. Dark mode and the SVG token pass
  remain W6.

---

## 12. The editorial review, and the landing page rebuild

Dan asked for a publisher-grade critique of the mock-up before any further work.
The verdict was that the reading experience and the reference layer were strong
and the front door was inert: no author anywhere above the footer, no image or
figure of any kind, one value and one rhythm repeated four times, incompleteness
advertised twice in the two places a visitor looks for confidence, and a "Published
chapters" band holding a single item. The deepest problem was that the book's three
best assets, the figures, the formal spine and the sourcing discipline, were all
invisible until a reader was already reading.

All seven items were taken. The page now runs **argument, proof, evidence, author,
contents, conversion**, which is the order a reader needs rather than the order the
material happens to exist in.

**The hero carries a live model.** The seat line stays flat while the event curve
accumulates, and a slider drives both. It sweeps once on first view and then waits.
It is a DIAGRAM OF A MODEL, not data: there are no units on either axis and no
figure is claimed, and the caption says so. Both curves are definitional, which is
exactly what Chapter 1 argues.

**One inverted band gives the page a middle.** Navy ground, carrying THM-009 in
the chapter's own panel markup with only its colours overridden. Rule 4a again:
the panel is a rendering of the registry statement and is never re-set in
different words.

**GATE W9a: THE LANDING PAGE QUOTES THE BOOK AND NEVER PARAPHRASES IT.** The
theorem and one specimen paragraph are lifted from the locked chapter by
`build_specimens()` and must appear verbatim in both. Rule 4a forbids paraphrase
inside a chapter; the front page is where it would do the most damage, because it
is where a reader forms their idea of what the book says.

**GATE W9b IS THE ONE THAT MATTERS, AND IT EXISTS BECAUSE THE FIRST DRAFT WAS
WRONG.** The specimen band was built to show the register entry behind a citation,
including its editorial note, because that note is the most persuasive artifact
this project has. It is also unpublishable. Register notes carry fact-check
finding IDs, instructions to later checkers, and VERBATIM QUOTATIONS OF SENTENCES
THE BOOK HAS CUT: the note behind Chapter 1's first citation quotes both the SF2
continuation mechanism and the FC9 absorbed-cost inference. Publishing it would
have put the book's retracted claims on its most public surface. Gate W3 caught
the draft only because register notes contain straight apostrophes, which is luck
and not a check. W9b is the check: no register note text on any published page,
only bibliographic fields.

The band still makes the point. It shows the paragraph as published with its real
sidenote, the bibliographic record, and a description of what the note field holds
without quoting any of it.

**The count is reframed rather than hidden.** Not "1 of 15 published" beside the
contents headline, but "1 published, the rest in preparation" with a line
explaining that a chapter locks only after thirteen steps and that nothing is
published early to fill the page. Same fact, and it now reads as rigour.

### Still open after the rebuild

- **THE AUTHOR BAND AND THE HERO FRAMING ARE DRAFT AND NEED DAN'S RULING.** Nothing
  about the author is invented: the band carries only what this repository states,
  which is a name, an organization, and the method. **It needs real biography, a
  real claim to authority, and a portrait**, and none of that can be written here.
- The author monogram is a typographic placeholder standing in for a photograph.
- No praise, endorsement, or adoption surface exists. For a founding textbook that
  will matter, and it cannot be built until there is something real to put in it.
- Part descriptions remain one-sentence placeholders.

---

## 13. What Phase W5 learned

**`web_build.py` built one chapter, and a deploy needs a site.** That gap was the
real work of W5. `--site` discovers every locked chapter from `Drafts/`, builds a
page for each, then builds the reference layer, the search index and the deploy
files once over the whole set. Per-chapter gates run per chapter; site-level gates
run once over every emitted page. A failing chapter does not stop the others being
reported, because a deploy needs the full list of what is wrong rather than the
first thing that is wrong.

**DISCOVERY MUST NEVER BE ABLE TO PICK A STALE FORK, AND ONE IS STILL SITTING
THERE.** Chapter 1's Stage 0 folder holds `DRAFT-AIOM_ch01.html` alongside the live
text: a superseded copy carrying `lang="en"` and no source register. It is exactly
the hazard CLAUDE.md records under Decision 50, where a superseded fork survived
long enough to diverge by 150 lines and a ruling was applied to the wrong copy.
`discover_chapters()` excludes it by name, fails loudly if more than one candidate
remains, and prints what it skipped on every build. **Deleting the file is Dan's
call and it should be made**: an exclusion rule is a guard, not a fix.

**THE TWO-CHAPTER PATH IS PROVEN BEFORE CHAPTER 2 EXISTS.** Code that works for one
chapter is not thereby known to work for two, and the site builder had only ever
seen one. The self-test now synthesises a second locked chapter in a throwaway
tree and asserts that two chapter pages are emitted and both appear in the
sitemap. Four controls, and they cost nothing to keep.

**CI INSTALLS A HEADLESS BROWSER, DELIBERATELY.** Gate W6 is optional because it
needs one, and the tempting shortcut is to run CI with `--no-browser`. That would
produce a green tick on a suite with a known hole in it, which is this repository's
signature failure wearing a badge. The workflow installs Chromium and runs the
full width sweep.

**Publishing is gated twice.** `web_build.py` refuses any chapter that
`status_check.py` does not report at Stage 9 (Decision 64), and the deploy job runs
only if every gate passed. Rendered output is never committed (Decision 63), so
the site is built from source on every push and a chapter's text exists once in
version control rather than twice.

### Open, and all three are Dan's

- **The domain.** `--base-url` sets the CNAME and makes sitemap URLs absolute. It
  is unset, so no hostname is invented and the sitemap emits site-relative paths,
  which are valid and become absolute the moment a domain is supplied.
- **The host. RULED as Decision 65: GitHub Pages**, published from `main`. Chosen
  over Cloudflare Pages and Netlify because it needs no third-party account and no
  API token in repository secrets.
- **The analytics posture. RULED as Decision 66: none.** ENFORCED BY GATE W11
  rather than by intention, because "we did not add a tracker" is true only until
  somebody adds one. Every subresource must be same-origin. Outbound anchor links
  are exempt: a link a reader chooses to follow is not a request the page makes
  for them, and the sources page exists to link out to every cited source.
