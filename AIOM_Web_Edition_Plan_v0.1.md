# AIOM Web Edition: proposal v0.1

Status: **PROPOSAL, NOT ADOPTED.** Written 2026-08-13 on branch
`claude/textbook-website-design-h9nk9t`. Nothing here is a ruling. The decisions
in section 7 are Dan's, and no code should be written against this document
until they are ruled. Not yet listed in the CLAUDE.md repository map, because the
map records adopted artifacts.

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

**Recommendation: retire the markdown pipeline permanently and build the web
edition from the locked chapter HTML, which is Decision 50 already.** The
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

**Language: Python, plus Jinja2, plus vanilla JavaScript.** No Node toolchain.
The repository is already a Python build system with a pinned `requirements.txt`
and a one-command build, and `web_build.py` sits beside `AIOM_build.py` and
imports the same citation modules. An Astro or Next.js site would be faster to
make pretty and would introduce a second dependency universe, a second idea of
what a build is, and a standing temptation to keep chapter content in the site
repo. That temptation is exactly what Decision 50 exists to prevent. Jinja2 is
the only new pinned dependency.

**Output: a fully static site.** HTML, CSS, self-hosted fonts, inline SVG, one
small JavaScript bundle for the reader chrome and search. It hosts on Cloudflare
Pages or GitHub Pages behind a custom domain, costs nothing to run, and cannot
break at request time.

### The gate that matters most

The recurring failure in this repository is not a bad judgment call. It is a
check that reads green while measuring nothing, or two artifacts of one chapter
that silently disagree. A second renderer is a machine for producing exactly
that, so the web build carries a control the print build never needed:

- **Gate W1, text equivalence.** Extract the body text of the web page and the
  body text of the print render, normalize whitespace, and require them to be
  character-identical. Any divergence fails the build. The web edition is a
  second *presentation*, never a second text, and this is the check that keeps
  it honest.
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

- **Phase W0, decisions.** Section 7. Nothing is built first.
- **Phase W1, the pipeline.** `web_build.py`, `AIOM_web.css`, and gates W1 to W5,
  rendering Chapter 1 only. Success is defined by gate W1 passing: the web text is
  character-identical to the locked print text. Design is deliberately plain at
  this phase. This is the load-bearing work and it is where the risk is.
- **Phase W2, the reader.** The full reading experience on Chapter 1: slot rail,
  sidenotes, margin definitions, progress, motion, responsive behaviour, keyboard
  layer. Design review against the same standard the print book gets.
- **Phase W3, the front door.** Landing page, table of contents, about, the
  author. Depends on the section 6 input and on Decision W-A below.
- **Phase W4, the reference layer and search.** Glossary, object index, sources,
  search index.
- **Phase W5, deploy.** Domain, hosting, analytics posture, and the build hook that
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

## 7. Decisions, in the order they block work

**W-A. Is the whole book free on the web, or is the site a marketing surface with
sample chapters?** This is first because it changes the build, not just the
content. Full text means a pure static site and no auth. Samples plus purchase
means a store, a paywall or an email gate, and a decision about which chapters are
open. Full text hosted openly also interacts with the PDF and ebook editions and
with any university press conversation, which is a business question rather than a
technical one. *No recommendation offered: this is a business ruling.*

**W-B. Retire the markdown pipeline permanently?** Recommendation: yes. Delete
nothing that is already archived, and add a line to the CLAUDE.md repository map
recording that `archive/AIOM_ch01_markdown_noncanonical.md` is a pre-fact-check
draft that must never be used as a source, so the next session does not
rediscover this. Section 1 is the reasoning.

**W-C. Python and Jinja2, or a JavaScript framework?** Recommendation: Python and
Jinja2, one new pinned dependency, for the reasons in section 3.

**W-D. Does the web edition live in this repository or its own?** Recommendation:
this one. The web build must import `footnotes.py` and `cite_format.py` and must
read the chapter HTML directly, and any split creates the copy that drifts.
Publishing is a deploy step, not a second repository.

**W-E. Which chapters may the site show, and when?** Recommendation: locked
chapters only, enforced by gate W2 rather than by intention. Today that is Chapter
1 alone, which is enough to build and prove everything.
