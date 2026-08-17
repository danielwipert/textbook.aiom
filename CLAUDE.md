# CLAUDE.md

Project context for *AI Operations Management*. Read this before touching anything
in this repository.

---

## 1. What this is

A founding academic textbook establishing AI Operations Management as a discipline.
Fifteen chapters, four parts. Print-quality PDF produced through a WeasyPrint
pipeline in this repo.

Two named layers, both load-bearing:

- **AI Business Economics** is the science.
- **AI Operations Management** is the practice discipline that acts on it.

Reader: an intelligent, busy, sceptical MBA-level graduate student who has read
business books before and can tell when one is padded. Standard: university press
(Chicago or Oxford caliber). The book is intended to last fifty years.

Author of all decisions: Dan (Daniel S. Wipert, Chorus AI Systems). Claude drafts
and builds. Claude does not rule.

---

## 2. Standing rules, non-negotiable

These have all been explicitly ruled and re-affirmed. Do not relitigate them.

1. **No em dashes. Anywhere.** Body prose, cases, craft sections, summaries, key
   terms, discussion questions, problems, back matter, and every file in this
   repo including commit messages. Rewrite with commas, colons, periods,
   parentheses, or restructure the sentence. This is the single most-violated
   rule under stress. A build gate enforces it.
2. **Every empirical claim is cited to a real source, rewritten as a formal
   conditional, or cut.** No third option. Never invent a citation, a statistic,
   or a source. If the claim cannot be sourced, cut it and say so.
3. **The fixed six-slot skeleton applies to all fifteen chapters, without
   exception.** See section 3.
4. **The registry justifies the book. It does not organize the book.** Never
   restructure a chapter around registry objects.
4a. **The registry is the third rail. The book is an interpretation of it.**
   Ruled 2026-08-09 at Ch1 DE9. A registry object is never edited to suit a
   chapter, and a panel rendering it is never paraphrased into plainer words:
   the ID in the panel label is what a reader follows to the verbatim form, and
   that promise is what makes the panel trustworthy. When a registry statement
   reads as wordy or technical, the remedy is always the prose beside it, never
   the statement. Give every antecedent a plain-English twin in the gloss and
   let the panel stay formal. If the shorthand itself is genuinely wrong, that
   is an AI Business Economics change, upstream of the book, not a chapter edit.
   Note also that the Locked Registry workbook is NOT in this repo, so no panel
   wording can be verified from a Claude session; `aiom_registry.py` expects the
   workbook to be supplied.
5. **No decorative apparatus.** Signposting is done through the skeleton, not
   through prose. Do not tell the reader what the chapter is about to say before
   saying it.
6. **Theorem statement form.** A registry conditional carrying more than two
   antecedents is set as a structured conditional, never as running prose: scope
   boundary first, before the word "if"; antecedents enumerated in lower-case
   roman, one per line; consequent on its own line opening with "then". Render
   registry shorthand into full parallel English, and never change the logic. No
   antecedent added, dropped, merged, split, weakened, or strengthened. The
   registry statement is the authority and the panel is a rendering of it. Full
   rule in `AIOM_DESIGN_SPEC.md` section 5; ruled as Decision 56.

### Voice

- **Register:** magisterial. Combative energy transmuted into cold economic
  analysis. Not neutral about the argument, completely neutral about individual
  actors. Do not scold providers, derive their behavior. Do not sneer at buyers
  who bought AI as software, explain why the mental model was legible and where
  it breaks. The manifesto's taunting register is out.
- **Person:** third person throughout body prose. Second person permitted
  sparingly in craft sections and discussion questions.
- **No contractions** in body prose. Permitted in dialogue inside cases and in
  discussion questions where they serve the register.
- **No exclamation points.**
- **No rhetorical questions** in body prose. Permitted in discussion questions,
  which is what they are for.
- **No hedging.** No "perhaps," no "some argue," no "one might say." Hedging is
  a signal that citation, formalization, or omission was skipped.
- **Fifty-year rule:** body prose is timeless. Perishable specifics are
  quarantined in dated cases.

### Craft, the positive half of the voice standard

The rules above are prohibitions. Prose can break none of them and still be dead
on the page. `AIOM_Voice_and_Craft_v1.md` is the positive standard, and it is
binding at drafting time, not only at check time. Read it before drafting a
chapter, not after.

Six criteria, each drawn from a named exemplar. They appear verbatim as
sub-checkboxes under Stage 4 in every chapter checklist, and `status_check.py`
fails a Stage 4 marked passed with one of them left open.

- **C1. Concrete particular.** Every abstraction carrying argumentative weight is
  anchored to a named, specific instance. Constrained by the fifty-year rule, so
  it lives mostly in cases, worked examples, and craft artifacts.
- **C2. Context and stakes.** Every mechanism states the conditions that made it
  available and what it settles, not only what it does. The highest-value
  criterion, and the only one with no mechanical proxy.
- **C3. Front-loaded sentences.** Findings lead, qualifications subordinate, no
  throat clearing.
- **C4. Deliberate rhythm.** Sentence length varies. No long stretch at a uniform
  length.
- **C5. Paragraph close.** Paragraphs end on the load-bearing clause, not a
  trailing qualifier.
- **C6. The guard holds.** No hero or villain framing, no populist register, no
  character-driven causation where a structural account is available. This guard
  is what keeps the borrowed techniques from reimporting a register already ruled
  out.

`voicecheck.py` prints advisory craft metrics alongside the mechanical bans. They
are proxies, permanently advisory, and never a pass-or-fail threshold. C2 and C6
have no proxy at all and are enforced only by reading.

### The prose standard is TWO files, and they divide cleanly

Adopted 2026-08-12. `AIOM_Prose_Style_Guide_v1.md` was written on 2026-08-05 and
stranded on an unmerged branch for a week, during which Chapter 1 passed a
developmental edit, a fact check, a voice pass, a design review, a production
gate and two copy-edit rounds without it. Both it and
`AIOM_Voice_and_Craft_v1.md` were adopted the same day by sessions that could not
see each other, both name the same four exemplars, and neither mentioned the
other. The division:

- **`AIOM_Voice_and_Craft_v1.md` governs the six craft criteria C1 to C6**, the
  exemplars, and the guard. Stage 4 grades against it and `status_check.py`
  enforces it.
- **`AIOM_Prose_Style_Guide_v1.md` governs everything else about prose:** the
  reader model, altitude and contextualization, sentence-level craft, the
  drafting protocol, and the house style sheet. **Read it before drafting.**
- The style guide's Part 6 duplicated the craft file and is retired to a pointer.

**THE RULE THAT ANSWERS THE MOST COMMON COMPLAINT ABOUT THIS BOOK'S PROSE IS
PART 5.** The ideas are complex; the sentences do not need to be. Vary length
with load, keep the actor in the sentence, and ration the parenthetical
interrupter: never separate a subject from its verb by more than about three
words, never stack two interrupters in one sentence, prefer the right-branching
alternative. Part 4 adds a hard rule that is not in section 2 above, no comma
splices and no run-on sentences.

Two items are booked and NOT done. Consolidated Spec B.2 still duplicates the
register and mechanical rules and is not yet demoted to a pointer. And the Part 8
source-level checks are not in `voicecheck.py`: they were written against a
262-line version of that script and `main`'s is now 470 lines, so they must be
ported individually rather than merged.

---

## 3. The fixed six-slot skeleton

Every chapter, in this order, no optional slots:

1. Opening case
2. Teaching body
3. Craft section
4. Chapter summary
5. Key terms
6. Discussion questions and problems

The opening-case slot permits variation in **form** (a dashboard, a contract
clause, a failed executive memo can all serve). That is drafting freedom inside
the slot, not a structural exception.

Every opening case carries a provenance line beneath the title. Perishable
sources are dated. Constructed material is labelled as constructed.

---

## 4. Repository map

| Path | What it is |
|---|---|
| `AIOM_build.py` | Font staging, WeasyPrint render, fifteen QA gates, toolchain preflight. One command. |
| `AIOM_book.css` | The locked design system, print. |
| `web_build.py` | The web edition renderer and its seventeen gates. It also renders the typeset PDF each locked chapter publishes, from the same injected document the page is transformed from (Decision 67). Reads the same locked chapter HTML and reuses `footnotes.py`, `cite_format.py` and `status_check.py`. Both artifacts descend from ONE `footnotes.inject()` call, so text equivalence is structural rather than hoped for. Run from the repository root. |
| `AIOM_web.css` | The web presentation layer, v0.1. Tokens are inherited from `AIOM_book.css`, never chosen. Sole control of web appearance, same rule as print. |
| `web_templates/` | Jinja2 templates. `chapter.html.j2` is the reader; `index.html.j2` is a placeholder front page, not the Phase W3 landing page. **Chrome lives OUTSIDE `<article id="chapter-text">` and the boundary is load bearing:** gate W1 measures the article and nothing else. |
| `ledger.py` | Reads `AIOM_Continuity_Ledger.md` as data. The web glossary, object index and promise list are the SAME record gate G3 enforces, not a second list scraped from chapter HTML. Read only; appending is `continuity.py --update` at Stage 9. |
| `book_structure.py` | The four parts and fifteen chapters, PARSED from `AIOM_Structure_v1.md` rather than retyped. The site's navigation and its table of contents come from here, so the book's own structure document is the single source for the book's shape. |
| `.github/workflows/web.yml` | Builds the site, runs every gate, runs the self-test, and publishes to GitHub Pages from `main`. **It installs a headless browser so gate W6 actually runs in CI, and `poppler-utils` so gate W17 does**, because a job that quietly skipped either would be this repo's signature failure with a green tick on top. Without poppler the deploy is green and carries no PDF. |
| `web_gates_selftest.py` | Negative controls for the web gates. Injects one fault at a time and asserts the owning gate fails. Run after any change to `web_build.py`. It found two dead gates and one blind spot on its first run. |
| `place.py` | Definition-callout placement pass. See section 6. |
| `specimen.py` | Type specimen. Sets the chapter's own prose in candidate faces at the shipping size, embeds each face so the page needs no network, and reports set width, x-height and what the measure becomes. A face is chosen by reading this, never by reading a description of the face. |
| `copyedit_export.py` | Chapter HTML to a copy-editing `.docx` plus a round-trip manifest. Stage 6 happens in Word; this is how it gets there. Excludes the source register by design. |
| `copyedit_import.py` | The copy-edited `.docx` back into the chapter HTML, block by block, by span. Applies what is unambiguous and refuses the rest rather than guessing. |
| `factcheck_packet.py` | Builds the Stage 3 and Stage 7 packet: every cited passage paired with its register entry, notes reproduced verbatim, plus the mechanical checks run locally. It verifies nothing, because both stages are structurally external. Promoted to the root 2026-08-10 after the same throwaway work came due twice on one chapter. |
| `AIOM_Continuity_Ledger.md` | The G3 record: terms owned per chapter, forward references and whether paid, registry glosses, Northmoor figures, and the canonical Founding Questions and maturity stages. Appended at lock, never edited to make a gate pass. |
| `continuity.py` | Gate G3. Seven checks against the ledger. `--update` appends at Stage 9; `--pay N` marks promises kept. |
| `AIOM_Claim_Ledger.md` | The W14 record: every ruled claim narrowing as REQUIRED text the chapter must contain and FORBIDDEN text it must not. Written from the CHAPTER, never from the register note's description of it. Adopted 2026-08-13. |
| `claimcheck.py` | Gate W14 and a standalone pass. Does the chapter still say what the fact checks ruled? Answers the one class of damage no other check can see. |
| `snapshot.py` | What the site publishes: each chapter's LAST LOCK, derived from the commits that touched its checklist, never the working tree. Materializes a Drafts-shaped tree so every path-dependent check runs unchanged. |
| `amend.py` | Edit a LOCKED chapter in one command. Reopens nothing, the chapter never leaves Stage 9, and Dan's edit is approved by definition. Runs the mechanical gates only. `--supersede` retires a fact-check ruling he overturns. |
| `reopen.py` | Reopens a chapter at a stage: resets that step and everything after it, archives their findings in place rather than destroying them, and writes a dated reopen record. The mechanism CLAUDE.md section 8 always assumed and never had. |
| `renumber_stage_folders.py` | One-time Process v1 to v2 stage-folder migration. Run 2026-08-05 across all eighteen units. |
| `git_hygiene.py` | Is any work stranded, and is the tree fit to hand over? Deepens the shallow clone FIRST, because an undeepened sweep counts merged branches as stranded. Run before every merge and every session close. See section 9. |
| `requirements.txt` | Pinned build toolchain. WeasyPrint line breaking and float placement move between releases, and gates 4 and 14 are sensitive to exactly that. |
| `AIOM_Design_QA_Spec_v1.md` | Gate-by-gate spec. Moves with `AIOM_build.py`. |
| `AIOM_Consolidated_Spec_v1.md` | The full pre-drafting specification. Authoritative. Markdown despite the earlier `.pdf` reference. |
| `AIOM_Voice_and_Craft_v1.md` | The positive voice standard: the four borrowed techniques, the guard, and the six craft criteria. Binds from Stage 0. Read before drafting. |
| `AIOM_Prose_Style_Guide_v1.md` | The other half of the prose standard, adopted 2026-08-12 after a week stranded on an unmerged branch. Reader model, altitude, sentence-level craft, drafting protocol, house style sheet. **Part 5 is the answer to prose that reads denser than its ideas.** Read before drafting. See section 2. |
| `AIOM_Specification_Addendum_v1.0.docx` | Decisions 1 through 21 and the Addendum rulings. |
| `AIOM_Structure_v1.md` | Chapter structure and structural devices. |
| `AIOM_Exit_Competencies_v1.md` | The twenty-four competencies. Backward-design root. |
| `AIOM_Maturity_Model_v1.md` | Stage definitions. Ch13 craft. |
| `AIOM_Case_Bank_v1.md` | Cited cases with reuse policy. |
| `AIOM_Northmoor_Dataset_v1.md` | Capstone dataset design. |
| `AIOM_Workplan_v5.md` | Current workplan and per-chapter tracker. Supersedes v4, which is retired. **The decision-numbering authority.** Decisions run to 66. |
| `AIOM_Web_Edition_Plan_v1.0.md` | The web edition: architecture, the web gates, the site, and phasing. Adopted 2026-08-13 with Decisions 60 to 64. The web is a second PRESENTATION of the book, never a second text, and gate W1 is what makes that true rather than intended. |
| `AIOM_Validation_Matrix_v1.xlsx` | The 28-row Appendix A trace matrix. Working artifact, never book content. Distinct from the full 228-object registry, which lives in Drive. |
| `Drafts/ChNN_<Name>/` | Chapter working directories, one per chapter, plus `Case_Part_I` through `III`. Each holds thirteen stage folders on Process v2 numbering and the chapter checklist. The live text sits in `00_Stage0_Draft/`. **There is no `chapters/` directory**, and this row claimed one until 2026-08-10. |
| `fonts/` | Committed fonts (IBM Plex Sans and Jost for print, Archivo and Jost for the web) plus their OFL licenses. `fonts/use/` holds every face either stylesheet loads, so rendering needs no network staging. Print and web do not load the same body family; `fonts/README.md` has the table and the reason. |

When spec placeholders conflict with operative content, trust the operative
content: the maturity model, Stage definitions, and chapter assignments win over
placeholder glosses.

---

## 5. Build commands

There is no chapter path that works for every tool, because the build and
`place.py` want the file in different places. Read the comments before copying a
line.

```bash
pip install -r requirements.txt                  # once per session, first
apt-get update -qq && apt-get install -y poppler-utils

# The live text. Every chapter has its own path; this is Chapter 1's.
LIVE=Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html

# Render plus all fifteen QA gates. AIOM_build.py sets base_url to the HTML's
# OWN directory, so building in place under Drafts/ loses AIOM_book.css and
# fonts/ and reports dozens of false defects. Copy to the repo root, build
# there, delete the copy and its .print.html sibling. Create build/ first: the
# render raises FileNotFoundError rather than making the directory. Without
# --out it writes beside the input, which leaves a fourth file to clean up.
mkdir -p build
cp "$LIVE" _ch01_build.html
python3 AIOM_build.py _ch01_build.html --out build/Ch1.pdf
rm -f _ch01_build.html _ch01_build.print.html

# Callout placement pass, the gate 4 remedy. place.py REWRITES the file it is
# given, so unlike the build it runs on the live text path itself, from the
# repo root, and needs AIOM_book.css and fonts/ symlinked beside the live text.
# Those symlinks are not committed, so create them. It leaves a .bak next to
# the chapter that is not gitignored; delete it or a second chapter HTML sits
# in the live-text directory.
python3 place.py "$LIVE"

# These two read the source and need no design system, so they take the live
# text path directly.
python3 voicecheck.py "$LIVE"                    # Stage 4 mechanical plus craft metrics
python3 status_check.py                          # lifecycle status, authoritative
python3 reopen.py <checklist.md> --from "Stage 2" --reason "..."   # reopen

# Stage 6 round trip. The export needs a current production render, and the
# UNEDITED export must round-trip at zero reported changes before either tool
# is trusted on a chapter. Without --apply the importer is a dry run.
python3 copyedit_export.py "$LIVE" --pdf build/Ch1.pdf --out <name>
python3 copyedit_import.py <name>.docx <name>.manifest.json "$LIVE"
```

Fonts are committed under `fonts/`, so `--fonts` is not needed and the render
requires no network. The build exits 2 without running any gate if its toolchain
is missing.

System dependencies WeasyPrint requires: `libpango-1.0-0`, `libpangoft2-1.0-0`,
`libcairo2`, `libgdk-pixbuf-2.0-0`, `libffi-dev`, `shared-mime-info`.
Python: `weasyprint`, `pdfplumber`, `pdf2image`, `pillow`, `openpyxl`, `fonttools`,
`jinja2`, `python-docx`, which the Stage 6 pair needs and which went unpinned
until 2026-08-10, and `playwright`, which gate W6 needs and which went unpinned
until 2026-08-13. All are pinned in `requirements.txt`; install from the file
rather than from this list. **Pinning `playwright` pins the rendering engine**,
because `playwright install chromium` fetches the build matching the installed
library, and W6 measures rendered layout across twenty viewport widths. The
browser BINARY is not carried by pip, so a fresh environment still runs
`python -m playwright install --with-deps chromium` after the requirements
install, which is what `.github/workflows/web.yml` does.

**THE WEB BUILD NOW NEEDS THE PRINT TOOLCHAIN TOO, INCLUDING `poppler-utils`**,
because it renders and gates the typeset PDF each chapter publishes. Without it
the build does not fail: it prints `W17 SKIPPED`, publishes a site with no
download, and says so in the verdict line. `--no-pdf` skips it deliberately and
is named in that line the same way.

---

## 6. QA gates and their remedies

The suite is fifteen gates. Full detail in `AIOM_Design_QA_Spec_v1.md`. The ones
that fail most often:

- **Gate 1, horizontal overflow.** 428.4pt odd pages, 417.6pt even, 1.5pt
  tolerance. Catches unbreakable strings, oversized SVG text, table cells that
  will not wrap.
- **Gate 2, em and en dashes.** Fails on any `U+2014` or `U+2013`. Note this is
  stricter than the standing rule, which bans em dashes only. Q2 asked what happens
  where Chicago requires an en dash. **RULED 2026-08-13 for number ranges: the
  hyphen wins and the gate stands.** A journal page range therefore sets as
  `889-942`, which is correct Chicago in every respect except the dash, and the
  register must STORE the range with a hyphen. An entry holding an en dash fails
  the build rather than passing silently, which is the right failure mode. Q2
  remains open for any other construction Chicago would set with an en dash.
- **Gate 4, definition callout splits.** Fails a callout sitting flush at the top
  margin, the signature of one that broke across a page. **Remedy: run
  `place.py`.** Do not try to fix this in CSS. WeasyPrint 69 ignores
  `break-inside: avoid` on floated elements.
- **Gate 5, font faces.** Expected set only. Catches a missing `@font-face`, an
  unstaged font falling back to a system face, and stray faces inside SVG.
- **Gate 7, provenance line.** Page 1 must carry the 7pt amber semibold line
  beneath the opening case title.

- **A checklist's box TEXT can go stale even when its ticks are correct.**
  `gen_checklists.py` moved to a seventeen-box G2 list on 2026-08-05; Chapter 1's
  checklist still carried the old ten-box list at G2, because `reopen.py` resets
  ticks and does not regenerate box text. This file claimed the mirroring was in
  place, which was true of the generator and false of the only checklist that
  exists. After a reopen, check the box text against the generator, not just the
  ticks.
- **Gate 14 excludes key-term names, amended 2026-08-06.** A term name is a full
  line in the semibold face at body size, so gate 14 read every one as a
  one-line paragraph: the first on a page scored as a widow, the last as an
  orphan. Chapter 1 carried one of each as a booked design defect for two days
  before Stage 5 found they were phantoms. Body prose carries inline bold, so
  the exclusion tests the whole line, not its first character.
- **`place.py` had three defects, all found at Ch1 Stage 5 on 2026-08-06.** It
  rendered the chapter source rather than the footnote-injected document the
  build ships, and footnotes move body text about 50pt down the page, so it
  reported zero splits on a chapter gate 4 failed. It treated paragraphs inside
  the theorem panel and the dated boxes as legal anchors, so it could float a
  definition callout inside either. And it scored gate 4 alone, so a placement
  that fixed the split and pushed a footnote off its calling page counted as a
  success. All three are fixed; the pass now renders through `AIOM_build.build()`
  and accepts a candidate only if it adds no new gate failure.
- **Gates 12, 13, 14, added 2026-08-05.** Figure captioning, numbering, order,
  and in-text reference; bottom margin with the folio excluded by colour; and
  widows, orphans, and stranded heads. These three were claimed by the G2
  checklist for months while `AIOM_build.py` performed none of them, so the
  boxes were ticked by hand and the gate read green. On first run gate 14 found
  a real defect the eleven-gate suite had passed: the "Craft section" slot label
  stranded alone at the foot of page 12, with the section it labels opening on
  page 13.
- **Gate 12 counted in-text figure references LINE BY LINE until 2026-08-09, so a
  reference that wrapped was invisible.** Justified text breaks wherever the
  measure ends, and applying Ch1 DE1 moved a break so the page read "... total
  cost. Figure" / "1.2 makes visible ...". The gate then failed a chapter whose
  prose names the figure in the sentence beside it. It also dropped any body-size
  line OPENING with a figure label, which it excluded as a caption on size and
  then excluded again as a reference for starting the line. References are now
  counted on the joined page text with captions subtracted one for one; caption
  detection is unchanged. This is the second silent defect in gate 12, after the
  mirrored-margin bug of 2026-08-05, and both were found by changing the input
  rather than by re-reading the code. When a check and the prose disagree, fix
  whichever is wrong and say which: rewording the sentence so the reference did
  not wrap would have passed the gate and left every later chapter exposed.

Gap G-I, added 2026-08-06 at Ch1 G2: a floated definition callout can collide
with a following block panel and no gate sees it. A placement that put the
callout beside the theorem panel wrapped the panel's title into a narrow column
and passed all fourteen gates. Gate 11 checks the panel is present, labelled,
ruled, and unsplit, not that it kept its measure. Until this closes, a chapter
whose callout placement moves must have the affected pages read, not merely gated.

Remaining known gap: the theorem callout is unguarded by gate 4 (it uses
`--tint-thm`, gate 4 keys on `--tint-def`), though gate 11 now checks the panel
directly. Figure GEOMETRY is still not validated, because SVG `rx` renders as
curve paths that do not appear in `pdfplumber`'s `.rects`; that check and the
page-level raster review are the two items marked MANUAL in the G2 checklist.
Inspect both by eye.

The build refuses to start without its toolchain (`pip install -r
requirements.txt`, plus `poppler-utils`) and exits 2. A gate that did not run is
not a gate that passed.

---

## 7. Environment quirks, learned the hard way

- The registry `.xlsx` must be loaded with `openpyxl` and `data_only=True` to
  read computed values rather than formulas. Load rows via
  `ws.iter_rows(values_only=True)`, index columns off the header row, then use
  `Counter` and set operations for cross-checks.
- The founding paper and spec files carry `.docx` extensions but are plain
  markdown. `grep`, `sed`, and `wc` work on them. `python-docx` fails.
- CSS `content:` strings: a Unicode hex escape consumes the following space as an
  escape terminator. Use literal UTF-8 characters instead.
- SVG figures with `rx` render as curve paths in WeasyPrint and do not appear in
  `pdfplumber`'s `.rects`. Verify that geometry by pixel-sampling a raster.
- WeasyPrint is invoked with `base_url` set to the HTML file's own directory.

---

## 8. Chapter lifecycle (Process v2)

Thirteen steps, gates separated from passes. Process v2 (2026-08-01) inserts a
developmental edit as Stage 2 and renumbers the stages that follow. The shape is
ten stages (0 through 9) plus three gates. Lock is Stage 9, a pass, not a gate.
There is no G4. `(C)` is Claude, `(D)` is Dan working outside the Claude system.

| Step | Name | Owner |
|------|------|-------|
| Stage 0 | Draft | C |
| G1 | Structural gate | C |
| Stage 1 | Content review | D |
| Stage 2 | Developmental edit | C; Dan gut-checks with a second model |
| Stage 3 | Source and fact check 1 | D |
| Stage 4 | Voice and craft check | C |
| Stage 5 | Design review | C |
| G2 | Production gate | C |
| Stage 6 | Copy edit | D |
| Stage 7 | Final fact check 2 | D |
| G3 | Continuity gate | C |
| Stage 8 | Final read | D |
| Stage 9 | Locked | C |

**Stage 2, developmental edit.** The teaching-quality pass, held early so its
line edits land before fact check, voice, design, and production, and do not
churn them. It interrogates clarity, pacing, cognitive load, example fitness,
transitions, and whether the argument carries the target reader without a stall.
Claude runs it as a fresh critical pass; Dan gut-checks with a different model
and rules, the same independence he applies to fact checking.

**Stage 6, copy edit.** Runs in Word, on a proof generated by
`copyedit_export.py` and returned through `copyedit_import.py`. The live text
stays the HTML (Decision 50); the `.docx` is a proof, never a second source. The
importer is deliberately unhelpful: it applies only what it can place
unambiguously inside a block's own span, and prints everything else for a human.
Before trusting either tool on a new chapter, round-trip the UNEDITED export and
require zero reported changes. That check found both bugs in the pair, and
neither would have been visible any other way.

**Stage 4, voice and craft check.** Two halves. The mechanical half is
`voicecheck.py`, which fails on the prohibitions. The judgment half reads the
chapter against the six craft criteria in `AIOM_Voice_and_Craft_v1.md` and
records a finding per criterion, not a single verdict. The criteria appear as
sub-checkboxes in the generated checklist, so `status_check.py` fails a Stage 4
marked passed with one left open and unexplained. The craft standard binds from
Stage 0, at drafting time; Stage 4 is where it is verified, not where it is first
consulted.

**Process v1 to v2 mapping**, for reading records written before 2026-08-01:
Stages 0 and 1 and gates G1, G2, G3 are unchanged. v1 Stage 2 (source and fact
check 1) is now Stage 3; v1 Stage 3 (voice) is now Stage 4; v1 Stage 4 (design)
is now Stage 5; v1 Stage 5 (copy edit) is now Stage 6; v1 Stage 6 (final fact
check 2) is now Stage 7; v1 Stage 7 (final read) is now Stage 8; v1 Stage 8
(locked) is now Stage 9. Dated records keep their original v1 numbers.

Sequencing rules:

- **Gates are not passes.** A gate is a mechanical pass-or-fail check run by
  Claude against a stated standard, and it stops the chapter where it stands.
  A pass is editorial judgment. They are tracked separately.
- **Edits re-run only what they can break, per the scoped re-run matrix below.**
  A render that passed against older prose has not passed, but a figure move need
  not re-run the voice check.
- Stages 6, 7, and 8 are all external and may run in one sitting. Stage 1 may
  not be batched with them: it runs early or it is worthless.
- A reopen after Stage 9 re-runs every step from the one that owns the change.
- No chapter is Locked until every step is complete.

**POST-LOCK (POST-LIVE) AUTHOR EDITS, THE AMENDMENT PATH. Ruled 2026-08-13, and
it is the answer to a locked chapter that is still being written.** Dan is the
author and the final editor. An edit he makes is approved by definition and
SUPERSEDES, so it does NOT go through the lifecycle: `amend.py` reopens nothing,
asks nothing about the merit of the edit, and the chapter never leaves Stage 9.
The thirteen steps are for producing a chapter, not for changing a comma in one
that exists. This is the ONLY path by which a locked or published chapter
changes, and it applies whatever the size of the edit: a comma and a rewrite of
every paragraph in the chapter run the same way.

- **What still runs is the mechanical half only, about thirty to forty-five
  seconds.** W14, `voicecheck` mechanical, the print render with its fifteen
  gates, and the web build with its full suite. These have no opinion about the
  writing. They measure the rendered object, and they catch what is invisible in
  the source because it is not in the sentence that changed: a one-sentence
  reorder in this chapter pushed footnotes off their calling pages ELEVEN PAGES
  LATER, twice. They report and stop before committing damage; they never
  overrule the edit, and `--force` commits anyway on Dan's authority.
- **THE COST IS PER RUN, NOT PER PARAGRAPH, SO EDITS ARE BATCHED.** Ten
  paragraphs cost what one costs. A separate amendment per paragraph buys
  nothing and produces a commit log and a checklist record nobody can read.
  Batch by slot, or by however much Dan sends at once.
- **THE CHECKLIST IS TOUCHED ON EVERY AMENDMENT AND THAT IS LOAD BEARING.**
  `snapshot.py` resolves what publishes as the newest commit whose CHECKLIST
  reported Stage 9. An amendment that changed only the chapter HTML would leave
  the lock commit behind and the site would serve the pre-amendment text with
  nothing reporting it. Appending the record is what advances the snapshot, and
  it also clears the divergence warning, because the record moves with the text.
- **A fact-check ruling Dan overturns is SUPERSEDED, never bypassed.**
  `--supersede ID "reason"` retires it in `AIOM_Claim_Ledger.md`, dated and
  attributed, with the old text kept as history and its fields renamed out of
  enforcement. Switching W14 off instead would leave the ledger claiming
  protection that is not in force, which is the failure the gate exists to
  prevent. `claimcheck.summary` counts only rulings that still enforce
  something, for the same reason.
- **`--rule` IS THAT RULING APPLIED IN ADVANCE, AND IT IS THE DEFAULT FOR AN
  EDITING RUN. Added 2026-08-14 on Dan's ruling.** Naming each ID by hand costs
  a round trip containing no decision: the gate fails, the IDs are read off the
  failure, the command is retyped. Dan's edit supersedes whatever it breaks, so
  `--rule` retires exactly those, dated and attributed and kept as history like
  any named supersede. It can never retire a ruling that still holds, because
  the set comes from `claimcheck.broken_rulings`, the same evaluation W14 runs.
- **WHAT `--rule` CANNOT SEE IS THE SAME BLIND SPOT W14 HAS, and it is the
  reason the reading half did not get faster.** A withdrawn claim RESTATED IN
  DIFFERENT WORDS matches no forbidden string. It breaks the ruling in
  substance, the gate stays silent, and `--rule` retires nothing because nothing
  failed. This is precisely how SF2 came back as SF8, and it happened a third
  time on 2026-08-14, when an amendment reintroduced the continuation mechanism
  in new words. SF2 and SF8 were retired by hand that day because the gate could
  not have named them.
- Stages 3 and 7 are unaffected and still bind: an amendment that introduces a
  NEW empirical claim needs a source like any other, and standing rule 2 is not
  a lifecycle step that an amendment can skip. **This is the one thing Claude
  still raises unprompted during an editing run**, in a line rather than a
  review, because no gate reads it and Dan cannot rule on what he is not told.
  Everything else about the prose is his and is not commented on.

**THE WORKING PROTOCOL FOR AN EDITING RUN, ruled 2026-08-14.** Dan sends
paragraphs and Claude does not negotiate them.

1. Dan sends replacement prose, as many paragraphs at a time as he likes.
2. Claude applies it VERBATIM to the one live text. Not a copy, not a fork, not
   a working draft to diff against. If the previous wording is needed it comes
   from `git show <sha>:<path>`, which puts no second file on disk.
3. Claude runs `python3 amend.py Ch01 -m "what changed" --rule`.
4. Claude reports ONE line: committed, or what broke in the render.

No proposed alternatives, no ruling-by-ruling analysis, no second opinion on the
writing. Dan already ran the chapter through the thirteen steps; the amendment
path exists because he is past them.

**Scoped re-run matrix.** After a step passes, an edit re-runs only the steps it
can invalidate:

| Edit class | Re-runs | Leaves intact |
|---|---|---|
| Body prose (claim or teaching change) | Stage 2 dev, Stage 3 fact, Stage 4 voice, Stage 5 design, G2 | G1, unless a slot moves |
| Citation or source only | Stage 3 or Stage 7 fact check, G2 | dev, voice, design |
| Figure order, geometry, or number (caption text unchanged) | Stage 5 design, G2 | dev, fact, voice |
| Copy edit (typo, punctuation, no meaning change) | G2 | dev, fact, voice, design |
| CSS or design system | Stage 5 design and G2, every chapter | dev, fact, voice |
| Voice or craft standard change | Stage 4, every chapter not yet Locked | fact, design, G2, unless the re-run changes prose |
| Structural (slot added, removed, reordered) | G1, then every downstream step | nothing |

Status is single-sourced: the per-chapter checklist checkbox is authoritative,
and `status_check.py` prints and validates it. CLAUDE.md section 10 and the
Workplan tracker must mirror what it prints.

---

## 9. How to work here

- **Present decisions one at a time**, with options, a recommendation, and the
  reasoning. Dan rules quickly when the framing is complete. Do not proceed past
  an unruled decision.
- **Structure before content.** Structure is treated as almost more important
  than the content itself.
- **Verify programmatically before delivering.** Do not report a build as clean
  without running the gates.
- **Single attempts over retries.** Token waste is flagged explicitly.
- **Protect pedagogical surprises.** Later chapters withhold things deliberately.
  Do not front-run them.
- **Real cited evidence over constructed material,** every time it is available.

### Git hygiene is Claude's job, not Dan's

Ruled 2026-08-12, after four sessions worked Chapter 1 in three days without
seeing each other and produced three disagreeing records of one chapter.
Reconciling them cost a full session of file management instead of drafting.
**Dan's time goes to writing and ruling. Keeping the repository coherent is
Claude's.** The rules below are what that means in practice.

1. **Run `python3 git_hygiene.py` BEFORE any merge and BEFORE closing a
   session.** Not after. On 2026-08-12 the sweep was run as a post-hoc
   confirmation and found nine branches of outstanding work AFTER `main` had
   already moved.
2. **A SHALLOW CLONE LIES ABOUT STRANDED WORK, and this is the single most
   expensive thing learned here.** The container clones with `fetch --depth 50`,
   so an older branch's common ancestor sits beyond the boundary,
   `git merge-base` fails, and `git rev-list origin/main..<branch>` counts the
   branch's WHOLE history as unmerged. That reported seven dead branches as 137
   stranded commits; after `--unshallow` the true figure was 24 across three
   branches, and four of the seven were fully merged. `git_hygiene.py` deepens
   before measuring. Never hand-roll the sweep instead.
3. **"Merge main up" means make the two level. It is never a licence to force.**
   Fetch first. If `git log origin/main ^HEAD` is non-empty, STOP AND READ WHAT
   IS THERE. `main` carried no commits of its own for months, and every entry
   written in that period assumed a fast-forward; that assumption died on
   2026-08-12 and will die again.
4. **Merge up BEFORE a branch is retired, not after the last commit anyone
   remembers.** Every stranding incident here has the same shape: a session
   levelled its branch, committed once more, and ended.
5. **One session, one branch, and say so in HANDOFF.** Concurrent sessions
   collide on more than text. Two numbered their copy-edit findings from CE1 and
   two produced files called round 6. **Before numbering a finding or an
   artifact, check what the checklist already owns.**
6. **Delete a branch once `git_hygiene.py` lists it as fully merged.** Thirteen
   branches were merged and undeleted on 2026-08-12, which is what made the
   stranded three hard to see.

---

## 10. Current state

`status_check.py` is the only authority on where a chapter stands, and
`HANDOFF.md` carries the perishable working state: which findings are open, which
artifact is current, what is committed. **This section holds only what binds later
chapters.** A finding belonging to one chapter lives in that chapter's checklist,
where a reopen archives it in place rather than destroying it. Do not restate it
here.

Chapter 1 is the exemplar the other fourteen are drafted against, and it is not yet
locked. Chapter 2 ("The Flow") is the immediate next drafting target and is
unblocked. Chapters 3 through 15 follow in sequence. Front and back matter come
after the manuscript.

### What every chapter must carry

- **`lang="en-US"`, never `lang="en"`. Decision 59, found by G2.** In Pyphen,
  which WeasyPrint hyphenates through, `en` is an ALIAS FOR en_GB rather than a
  neutral English, so a Chicago-styled American book breaks on British points:
  "organiz-ation" for "or-ga-ni-za-tion". THERE IS NO CSS LEVER FOR THIS. It is a
  per-document attribute, so a chapter that omits it hyphenates British silently
  with no gate reporting it.
- **`.nb` on proper nouns. Decision 58, CSS v7.1.** DR6 broke "ChatGPT" as
  ChatG-PT in the narrow column beside a floated callout, and DR7 broke "GitHub" as
  Git-Hub ACROSS THE PAGE 11 TO 12 TURN. The class switches hyphenation off for a
  proper noun; body prose keeps `hyphens: auto`, which is right for a justified
  measure. The durable claim is not a count, which moves with every reflow, but
  that zero line-end breaks fall inside a proper noun. Chapter 1 has held that at
  every measurement while the count itself moved: 88 at the fix, 95 once Decision
  59 switched the dictionary, 93 as of 2026-08-11.
- **One live text per chapter, and the chapter HTML is it. Supersede and delete,
  never fork.** This is Decision 50. Chapter 1's is
  `Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`. Check
  the path before editing, every time. A superseded fork of it survived undeleted
  long enough to diverge by roughly 150 lines, and Decision 56 was applied to the
  wrong copy and had to be reverted and re-applied. Stage-folder render PDFs are
  kept: they are artifacts of a step, not competing texts.

### The web edition, adopted 2026-08-13

The book ships as a print PDF and as a website, from ONE source. Full plan in
`AIOM_Web_Edition_Plan_v1.0.md`; Decisions 60 to 64 in the Workplan are the
rulings. What binds outside that document:

- **The web is a second PRESENTATION, never a second text.** `web_build.py` and
  `AIOM_web.css` sit beside `AIOM_build.py` and `AIOM_book.css` and read the same
  locked chapter HTML, reusing `footnotes.py` and `cite_format.py` rather than
  reimplementing citations. **Gate W1 requires the web body text to be
  character-identical to the print body text.** A second renderer is a machine for
  producing two artifacts of one chapter that silently disagree, which is this
  repo's signature failure, and W1 is the control against it.
- **THE ARCHIVED MARKDOWN CHAPTER MUST NEVER BE READ FOR PROSE.**
  `archive/AIOM_ch01_markdown_noncanonical.md` is a PRE-FACT-CHECK draft. It
  carries the SF2 continuation mechanism, the FC9 absorbed-cost inference, and the
  word "introduced" that a register note forbids, in prose that reads well and
  whose dates and figures are all correct. It is kept only for diffing against
  pre-fact-check prose. Decision 61 retires the markdown pipeline permanently;
  `aiom_md.py` was deleted 2026-08-10 and is not restored.
- **The web render is never the artifact for an external fact check.** It is HTML,
  so it reproduces the extraction phantoms that produced both production flags on
  Chapter 1's first check. Stages 3 and 7 keep getting the PDF.
- **THE SITE PUBLISHES THE TYPESET PDF, ONE PER LOCKED CHAPTER. Decision 67,
  ruled 2026-08-15.** `web_build.py` renders it from the SAME `footnotes.inject()`
  output the web page is transformed from, which is the equivalence gate W1 holds
  between page and print extended to the third artifact rather than a second
  render hoped to agree. It lands in the chapter's own directory, is linked from
  the chapter rail and footer and from the landing page's editions card, and is
  listed in `sitemap.xml` and `llms.txt`. A whole-book PDF is NOT this: it needs
  continuous folios, front matter and the appendix, and is booked for the
  completed manuscript.
- **GATE W17 GATES THE PDF, BECAUSE IT IS THE ONE PUBLISHED ARTIFACT NOBODY
  READS.** A broken page is seen the moment it opens; a download is opened once,
  elsewhere, by a reader who does not report back. W17a runs `AIOM_build.qa()`,
  all fifteen print gates unchanged and unforked, on the file the site serves.
  W17b checks page 1 carries that chapter's title, which is trivially true at one
  chapter and the whole point at two. W17c resolves every `.pdf` link on every
  page to a file in the tree and fails a chapter that publishes a download its
  own page does not link. **W15 cannot cover W17c**: it follows `a[href^="#"]`,
  because it measures where a click lands, and a download has no landing.
- **`source_html` IS NOT OPTIONAL WHEN CALLING `AIOM_build.qa()`, AND OMITTING IT
  FAILS A CLEAN CHAPTER.** Gate 14 excludes a one-line paragraph from its widow
  count by comparing the line against the chapter's whole paragraphs, which it
  reads from `source_html`; passed None it returns an empty set SILENTLY. W17's
  first run did exactly that and reported a phantom widow on page 13, the same
  phantom Chapter 1 carried as a booked design defect for two days in August
  2026. The clean baseline in `web_gates_selftest.py` is the control for it.
- **THE PRINT TOOLCHAIN IS RESOLVED BEFORE THE FIRST CHAPTER RENDERS, NEVER BY
  CATCHING THE RENDER'S EXCEPTION.** Missing `weasyprint`, `pdfplumber` or
  `pdftoppm` prints `W17 SKIPPED`, publishes no download, and names the skip in
  the verdict line; a render that fails with the toolchain present is a FAILURE.
  A check that reads its own missing dependency as an absence of defects is
  switched off by the fault it exists to catch, which is W16b's recorded failure.
  **CI installs `poppler-utils` for exactly this reason**: without it the deploy
  would be green and carry no PDF at all.
- **Only locked chapters publish, enforced by gate W2 against `status_check.py`,
  not by intention.** In-flight chapters build to a local `noindex` preview path
  that CI never publishes.
- **Phases W1 and W2 are built and green, 2026-08-13.** SIX gates run on every
  build: W1 text equivalence in two channels, W2 lock status, W3 typographic
  marks (ports print gates 2 and 15), W4 structure and links, W5 document
  attributes, W6 horizontal overflow across a twenty-width sweep. Chapter 1
  renders at 43,204 characters of prose identical to print, six notes identical,
  all six slots anchored. Build with:
  `python3 web_build.py Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`
- **W6, W15 AND W16's SERVED HALF ARE THE OPTIONAL CHECKS AND THEY ARE LOUD ABOUT
  IT.** All need a headless browser, which nothing else in the build does, so each
  prints SKIPPED and the verdict line gains "W6, W15, W16b AND W16c NOT RUN"
  rather than quietly passing. **The skip notice names the parts, not the gate,
  because W16a does run**: it reads the stylesheet against the committed font
  files and needs no browser, and a notice overstating what was skipped is the
  same defect as one understating it.
  `--no-browser` skips them deliberately. W6 is the web analogue of print gate 1: the symptom is
  not ink off the paper but the whole document scrolling sideways, dragging every
  other block with it. It found the P3 inventory table doing exactly that below
  390px, which no amount of looking at a desktop render would have shown.
- **A RESPONSIVE BREAKPOINT IS ARITHMETIC, NOT TASTE.** The sidenote needs
  `--note + --note-gap` of side track, and the side track is
  `(viewport - --rail - 2 x .reading padding - --measure) / 2`. The first draft
  set the breakpoint by eye at 1240px, leaving a 170px band where notes ran off
  the right edge of the window. Any change to those four tokens, to that padding,
  or to either stop of the section 3 type clamp must redo the sum. The comment in
  `AIOM_web.css` section 17 carries it, and it is solved in rem rather than px
  because v0.4 made the root size fluid, so every term scales together.
- **THE SECOND VERSION OF THAT SUM WAS ALSO WRONG, AND IT READ AS RIGHT FOR TWO
  MONTHS.** It computed 1411px while omitting the `.reading` padding entirely, and
  the media query sat at 1440px, so a 29px cushion nobody had reasoned about was
  the only thing covering a dropped term. A sum that is off by a term and lands
  inside its own safety margin is indistinguishable from a correct one until a
  token moves. **When re-deriving it, enumerate every term that consumes
  horizontal space rather than the ones the previous comment listed.**
- **THE MEASURE IS MEASURED IN A BROWSER, NEVER CALCULATED: 71 CHARACTERS AT v0.4
  AND 73 SINCE v0.6, AND IT WAS NEVER THE 66 THE STYLESHEET CLAIMED.** That 66
  stood from v0.2 until 2026-08-13 and was the 0.5em rule of thumb applied to a
  32rem column rather than anything measured. The real figure comes from the
  average glyph advance of this chapter's own prose in its own face at its own
  size, so **it is a property of the face and moves whenever the face does.**
  Both figures sit in the upper half of the 45 to 75 band. **The column was never
  too narrow.** What reads as thin on a wide screen is the ratio: before v0.4 it held
  28 per cent of a 1920px window with 556px of air on each side.
- **ONLY THREE THINGS CAN MOVE THE TEXT COLUMN: the measure, the type size, and
  the alignment rule.** Capping the reading area cannot, because a centred child
  of a centred container lands in the same place at every cap, and a variant that
  capped it rendered pixel-identical to the build it was meant to improve. Rule
  this out before anyone spends an afternoon on it.
- **v0.4 BUYS PRESENCE WITH TYPE SIZE RATHER THAN WITH MEASURE, 2026-08-13.** The
  root is `clamp(17px, 8px + 0.625vw, 20px)`, which passes through exactly 17px at
  1440 and exactly 20px at 1920, so neither clamp bound is a place where the size
  jumps. The column grows from 544px to 640px while holding its character count,
  71 at v0.4 and 73 since the v0.6 face change, so nothing is spent on readability. Below 1440px nothing moves, and the 620px rule
  still holds phones at 16px and 49 characters. **Mobile was never the problem and
  is untouched.**
- **THE RAIL IS CONTENT AND THE NOTE TRACK IS CLEARANCE, SO THE CLEARANCE GIVES
  WAY.** Fluid type scales the sidenote along with the column, which pushed the
  breakpoint to about 1565px and would have cost a 1512px laptop its margin notes.
  Narrowing `--rail` as well was tried first and wrapped the contents, breaking
  "Ch. 3 A Science and Its Discipline" across two lines. Only `--note` narrows,
  15.5rem to 14rem, and the breakpoint lands at 1420px, BELOW the 1440px it was,
  so a 1440px window gains margin notes it did not have.
- **THE WEB BODY ROMAN IS A TRUE REGULAR 400 AND PRINT KEEPS PLEX SANS TEXT.
  v0.5, ruled by Dan 2026-08-13.** IBM Plex Sans Text is a distinct face at
  `usWeightClass` 450, half a step above Regular, and `AIOM_web.css` declared it
  as `font-weight: 400` from v0.1, so web body prose was heavier than it
  announced. The italic beside it is a true 400, so **the roman and its own
  italic never matched.** Print is unchanged: ink on paper does not gain weight
  the way a backlit screen does, the print system is locked at v7.1, and the
  re-run matrix makes any change there re-run Stage 5 and G2 on every chapter.
  This is the division already in force for colour.
- **THE WEB BODY FACE IS ARCHIVO AS OF v0.6, 2026-08-14, ruled by Dan.** v0.5
  fixed the WEIGHT and left the SHAPE, and the shape was the remaining objection.
  Print still sets Plex Sans Text, so the two stylesheets now diverge in three
  places, on colour, on the v0.5 roman and on the face itself, for the same
  reason each time. **The measure is 73 characters, measured, not 71**: Archivo
  sets 2.4 per cent narrower, so the same 32rem column holds more of them.
  `--measure` did not move and neither did any other term of the section 17 sum,
  which is why the 1420px breakpoint stands and was re-swept rather than assumed.
- **A BODY FACE IS CHOSEN AGAINST THE WEIGHT LADDER FIRST AND THE SHAPE SECOND.**
  Seven faces were compared on real chapter prose at the shipping size. Three
  were ruled out before taste entered: two carried no 600 and one had no static
  italic at all, so each would have broken the design's ladder of 400, a drawn
  italic at that same 400, 500 and 600. A fourth set 6.9 per cent narrower and
  took the measure to 76 characters, past the top of the 45 to 75 band. **Compare
  faces by rendering the book's own prose, never by reading a description of the
  face**, which is the same rule already in force for the drawn marks.
- **GATE W16 CLOSES THE TYPEFACE HOLE, 2026-08-14 ON DAN'S RULING.** A face swap
  changes no text, so W1's equivalence holds perfectly, and print gate 5 inspects
  the faces embedded in the PDF rather than the weight a web stylesheet declares.
  The body face was half a step heavier than it announced for six phases, and the
  v0.5 entry left the hole open on the reasoning that the line changes about once
  a year. It then changed twice in two days. Three checks, each answering a
  different way this fails:
  - **W16a, the declaration against the file.** Every `@font-face` is staged, its
    `usWeightClass` is the weight declared, and its italic bit is the style
    declared. Static, so it always runs. **Its control is the real defect**: Plex
    Sans Text at 450 declared as 400, which it fails.
  - **W16b, the served page against the declaration.** Body prose computes to the
    family `--body-face` names, a FontFace at that family AND weight AND style is
    `loaded`, and a probe string measures within tolerance of the COMMITTED
    file's own metrics. All three, because each catches what the others miss:
    `getComputedStyle` reports the family REQUESTED whether or not anything
    loaded, so it cannot see a fallback at all.
  - **W16c, figure labels.** Inside a chapter, an SVG label must resolve to the
    body family; elsewhere, to a family the stylesheet declares, since the
    landing page's marks legitimately set Jost. This is W12's rule for colour
    applied to type.
- **A FILE IS COMPARED TO A FILE AND A RENDERING TO A RENDERING. THE FIRST
  VERSION MIXED THEM AND WAS GREEN HERE AND RED IN CI ON EVERY PAGE.** W16b
  originally measured a probe string in the browser against the font file's own
  `hmtx` metrics, which answers two independent questions at once, which face
  rendered and how the renderer measures it, so a failure cannot say which one
  moved and a pass cannot be trusted on an untested machine. **The CI runner
  disagreed by about two per cent in both directions and could not be reproduced
  here, because the pinned browser build will not download into this container.**
  Now the staged font file is compared to the committed one by SHA-256 in W16a,
  which is where a file question belongs, and every W16b comparison has both
  sides measured in the same browser, in the same page, at the same moment.
- **W16b's THIRD LEG IS THE PAGE'S OWN FALLBACK CHAIN WITH THE DECLARED FACE
  REMOVED.** Body prose must measure the same as a reference span forced to the
  declared family AND different from that fallback. It needs no knowledge of
  which face a platform substitutes, which is what makes it portable, and it is
  the leg that answers the question the CI failure raised: is the reader actually
  seeing the book's face.
- **W16'S TOLERANCE IS 0.5 PER CENT, AND WHAT IT HAS TO CLEAR CHANGED WHEN THE
  DESIGN DID.** Now that both sides of every comparison are rendered in the same
  browser, the same face measured twice agrees to floating-point noise, so the
  number's only job is to stay BELOW the distance to a fallback. **Liberation
  Sans, which is what generic `sans-serif` resolves to on the build container,
  sets the probe 0.91 per cent from Archivo**, and that is the closest fallback
  measured. Under the first design the floor was kerning instead, at most 0.165
  per cent, and a round one per cent would have passed that same Liberation Sans.
  **Measure the fallback before setting a tolerance, never just the noise.**
- **A GATE THAT REPORTS SKIPPED WHEN IT HITS ITS OWN FAULT IS SWITCHED OFF BY THE
  DEFECT IT EXISTS TO CATCH.** W16b's first version read the expected metrics
  inside the browser block, so deleting the font file raised, hit the broad
  `except`, and printed "SKIPPED, browser unavailable" while a browser sat there
  running. The control caught it. Any check whose setup can fail on the fault it
  hunts needs that setup outside the catch-all, or the fault reads as an absence.
- **VERIFY A FONT SWAP BY MEASURING A STRING, NEVER BY LOOKING. THIS IS NOW GATE
  W16b AND IT RUNS ON EVERY BUILD.** A face that fails to load renders
  identically to a face that changed nothing, so "it looks right" is not
  evidence. The method, kept here because it is what the gate does and what to do
  by hand when the browser is unavailable: measure a fixed probe string in the
  SERVED page at a fixed size and check it reports the incoming face's number,
  not the outgoing one. At v0.6 the 73-character probe sets at 3310.9px per 100px of type in
  Archivo against 3388.3px in Plex Regular, a 2.4 per cent move. **Select an
  actual body paragraph when measuring, and print what you selected.** The first
  run of this check at v0.6 caught the provenance line, which is Jost at 0.76rem,
  and dutifully reported a face and a measure belonging to neither the body nor
  the question.
- **THE CHAPTER'S FIGURES CARRY THE PRINT BODY FAMILY LITERALLY, AND IT IS
  REMAPPED ON THE WAY OUT.** Ten `font-family="Plex"` attributes sit in the
  locked Chapter 1 SVGs, exactly as its colours do. Once the web body face
  diverged, a label left alone would have sat in a different face from the prose
  beside it, so `tokenize_svg` substitutes `var(--body-face)` the same way it
  substitutes colour tokens: an attribute changes, no text does, gate W1 is
  unaffected, and the locked chapter is never edited. **`var()` resolves in an
  SVG `font-family` presentation attribute**, verified in a browser against
  computed style rather than assumed, which is how the colour remap was cleared
  too.
- **AND RE-RUN THE PRINT BUILD, BECAUSE "PRINT IS UNAFFECTED" IS A CLAIM.** Gate
  5 reporting no unexpected face is what proves a new file in `fonts/use/` is
  embedded nowhere in the book. `web_build.py` globs `fonts/use/*.ttf`, so a web
  face must be a TTF to be staged at all, which also means it sits in the same
  directory print reads from.
- **THE NOTE-OFF-THE-EDGE DEFECT IS NOT A GATE AND CANNOT BE.** A floated note
  hanging past the window does not make the page scroll, so W6 is blind to it, and
  it is the exact defect the 1240px breakpoint shipped. It is checked by sweeping
  widths and comparing each floated note's right edge with the viewport. **Run
  that sweep after any change to the four tokens or the clamp**, because a green
  W6 is evidence about sideways scroll and about nothing else.
- **EVERY WEB GATE HAS A NEGATIVE CONTROL, AND THIS IS WHY.** `web_gates_selftest.py`
  injects one fault at a time and asserts the owning gate fails. On its first run
  five of twenty-five controls did not fire: four mark controls landed in `<head>`,
  which the extractor skips, so gate W3 had never seen them, and the sidenote
  deletion control deleted nothing. Both were faults in the CONTROLS rather than
  the gates, which is the point: without the controls, a green W3 was evidence of
  nothing. It also found a real defect, W1b's note extractor carrying the same
  non-greedy defect the print-side scanner was written to avoid, which is the
  hyphenation-scan failure repeating. Run it after any change to `web_build.py`.
- **Phase W3 is built and green, 2026-08-13.** The front door, the whole-book
  navigation rail, and gate W7. SEVEN gates now.
- **GATE W7 GUARDS THE ONE PLACE THE BOOK CAN SILENTLY SPLIT IN TWO.** The site's
  navigation is parsed from `AIOM_Structure_v1.md`; a chapter's published title
  comes from its own locked HTML. Those two can disagree, and the chapter and the
  nav would each render correctly while naming different chapters. W7 fails the
  build on that, and on a structure document that stops parsing as four parts and
  fifteen chapters.
- **A GATE THAT ONLY EVER SEES ONE PAGE IS EVIDENCE ABOUT ONE PAGE.** W3 and W5
  were handed the chapter and nothing else, so the landing page was ungated from
  the moment it existed and shipped four straight apostrophes W3 would have failed
  instantly. `gate_pages()` now runs the page-level checks over every emitted page.
  Add a page, add it there.
- **PLANNING PROSE IS NOT PUBLISHABLE PROSE.** The site's part descriptions come
  from the Purpose lines in `AIOM_Structure_v1.md`, and only the FIRST SENTENCE is
  published. The rest is production talk: Part III's continues into
  "Worked-example fading: completion problems early in the part". Chapter "Big
  idea", "Competency" and "Anchor theorem" lines are never published at all,
  because CLAUDE.md section 9 rules that later chapters withhold deliberately.
  Those descriptions are PLACEHOLDER until Dan writes real ones.
- **Phase W4 is built and green, 2026-08-13.** Glossary, per-chapter sources,
  object index, promises between chapters, and client-side search. EIGHT gates.
- **GATE W8 GUARDS THE REFERENCE LAYER AGAINST THE CHAPTER IT DESCRIBES.** W8a
  requires the ledger's definition of a term to be character-identical to the
  chapter's key-term text, because a definition is exactly the kind of text that
  can be reworded with no date or figure changing, which is the shape that
  reverted four times on Chapter 1. W8b requires every cited key to appear on the
  sources page. W8c refuses an object index that claims an object no chapter
  renders, because the Locked Registry workbook is not in this repo (rule 4a).
- **THE REFERENCE LAYER IS GENERATED FROM RECORDS THAT ARE ALREADY ENFORCED**, never
  by scraping the rendered chapter: the glossary and object index from the
  continuity ledger, the sources from the chapter's own Decision 51 register
  through `cite_format`. Scraping would have made the reference layer a second
  reading of the book.
- **THE SOURCES PAGE IS WHERE URLs LIVE.** Print rules them out of footnotes and
  the chapter page matches print so gate W1's note comparison stays exact. The
  bibliography is the right home for a URL, and it is built with
  `url_policy="full"`.
- **A NON-GREEDY REGEX OVER NESTED ELEMENTS HAS NOW BEEN THE DEFECT THREE TIMES IN
  `web_build.py`.** `find_spans(doc, opener, tag)` is the balanced scanner and it
  takes a tag. Reach for it rather than writing `(.*?)</div>`.
- **GATE W15 SERVES THE SITE AND USES IT. Added 2026-08-13 on Dan's ruling,
  because nothing in either suite had ever exercised the site.** It does two
  things a static reading cannot: it follows every in-page link in a real
  browser, and it serves the tree over HTTP AT THE PREFIX IT DEPLOYS TO and
  fails when any subresource 404s.
  It loads each emitted page, clears the hash, clicks each internal link and
  measures where the target lands. W4's hardened parse would catch the dead
  anchor that prompted it; W15 exists because the CLASS is larger than that
  fault. An anchor can be well formed and still unreachable: on an element that
  is `display:none`, inside a collapsed rail, or under a handler that swallows
  the click. **No reading of the markup settles any of those.** Its three
  controls are exactly those three faults, and two of them are invisible to
  every other gate.
- **ONE URL POLICY FOR EVERY EMITTER: `site_url(base_url, base_path, path)`.**
  Absolute when a domain is set, root-absolute with the deploy prefix otherwise,
  taking the origin WITHOUT its path so the prefix cannot appear twice. **Three
  emitters had answered this question separately and two had it wrong**: the
  sitemap emitted `/ch01/` and robots.txt pointed at `/sitemap.xml`, which on a
  project site at `/textbook.aiom/` both address the root of the USER site, the
  same defect as the 404 page's stylesheet. A policy repeated in three places is
  a policy that is wrong in two of them.
- **`/llms.txt` IS GENERATED AND QUOTES THE SITE, never written by hand.** The
  llmstxt.org convention: an H1 name, a blockquote summary, then H2 sections of
  links. Its summary is lifted from the landing page's own hero, extracted from
  the rendered index rather than retyped, so the two cannot drift into
  describing the book differently. Everything else comes from records already
  enforced: the chapter list from what locked and built, the counts from the
  transformed body, the part names from the structure document. This is gate
  W9a's rule applied to a second marketing surface.
- **llms.txt WITHHOLDS WHAT EVERY OTHER PAGE WITHHOLDS.** No chapter "Big idea",
  "Competency" or "Anchor theorem" line, because section 9 rules that later
  chapters withhold deliberately and **a file addressed to a machine is not an
  exemption from that**. No register note either, which W9b enforces everywhere.
  Only a part's first Purpose sentence is public, via `public_purpose`.
- **A LIST OF ADDRESSES NOBODY FOLLOWS IS THE SAME DEFECT AS AN ANCHOR NOBODY
  CLICKS.** Gate W10 resolves every address in `llms.txt` and `sitemap.xml` back
  to a file in the tree, checks a fragment is a real anchor on its target, and
  checks the chapters listed are exactly the chapters built. **W15 cannot cover
  these**: it drives a browser over emitted HTML pages, and neither file is one.
- **THE 404 PAGE IS THE ONE PAGE THAT CANNOT USE A RELATIVE PATH, and it shipped
  broken because of it.** GitHub Pages serves it for ANY missing address at any
  depth, so `../assets` resolves differently every time. Root-absolute is wrong
  too: on a PROJECT site at `/textbook.aiom/` it points at the root of the USER
  site. The live page therefore came up unstyled with every link leading out of
  the book, and it was the only file in the build with a root-absolute path.
  `--base-path` supplies the prefix, CI derives it from the repository name so a
  rename cannot leave it stale, and it is empty when a custom domain serves the
  site at the root.
- **A `file://` RENDER CANNOT SEE A PATH-PREFIX BUG, WHICH IS WHY W15 SERVES
  OVER HTTP.** Every screenshot and every browser check before this one loaded
  the build from the filesystem, where a wrong absolute path is merely odd
  rather than fatal. Serving the tree at its real prefix is what turned an
  invisible defect into a failing gate. W10 checks the asset exists and W11
  checks it is same-origin; neither has ever loaded a page.
- **CLEAR THE HASH BEFORE FOLLOWING A LINK, or the check measures nothing.**
  Clicking a link whose hash is already current is a no-op in every browser, so
  a second visit to the same anchor would report the previous landing as a fresh
  pass. W15 calls `history.replaceState` and scrolls to the top before each
  click. This is the same shape as every other silent-pass defect here.
- **AN ID IS COLLECTED BY PARSING START TAGS, NEVER BY REGEX, and the difference
  is a whole class of dead link.** `\bid="([^"]+)"` matches inside
  `</p id="slot-craft-section">`, an attribute on a CLOSING tag that every parser
  discards, so the id sits in the file and never reaches the DOM. Gates W4b and
  W4c read ids that way and therefore counted two dead anchors as live targets
  and reported "all internal links resolve" for two rail links that did nothing.
  `AnchorCollector` in `web_build.py` is the reader; both the chapter check and
  the page check use it, and they were changed together so the landing page does
  not keep the defect the chapter is protected from. **A regex answers whether
  text is present. It cannot answer whether an element exists.**
- **A LINK IS VERIFIED BY FOLLOWING IT.** The two dead anchors were found on
  2026-08-13 by Dan clicking one, after passing every build since Phase W1. No
  check had ever followed a link; they had only looked for the string. When a
  navigation change lands, drive the browser: click each link and assert where it
  lands, which is about fifteen lines of Playwright.
- **INSERTING AN ATTRIBUTE INTO A MATCH REQUIRES KNOWING WHETHER THE MATCH IS A
  TAG OR AN ELEMENT.** Three `SLOTS` patterns match a bare opening tag and two
  match a whole element, because matching the label text is the only way to tell
  one slot from another. `add_anchors` wrote the id before the match's last
  character, which is right only for the first shape. Cut at the first `>`.
- **A `find_spans` OPENER MUST CONSUME THE WHOLE TAG, NOT JUST ENOUGH TO IDENTIFY
  IT.** The function returns the text after the opener MATCH, so an opener widened
  to `<div class="kt"[ >]` leaves the rest of the tag, id and all, inside the
  block. Found 2026-08-13 when term linking gave every `.kt` block an id: W8a
  immediately reported all eight key terms as differing from the ledger. Write
  `[^>]*>`. **And the openers that read the same markup must move together**, or
  the failure is silent in the other direction: an opener demanding an immediate
  `>` matches nothing, and W8a compares an EMPTY set of chapter terms against the
  ledger and reports a pass.
- **A BOLDED KEY TERM LINKS TO THE DEFINITION THAT OWNS IT, and the chapter carries
  no links.** `web_build.link_terms()` gives each definition callout and key-term
  entry an id and wraps the matching bold runs, adding attributes and an element
  and no text, so gate W1 is unaffected. The chapter HTML is shared with print and
  is never edited for this.
- **THE MATCH IS ON THE TERM, NEVER ON THE TAG, because bold does two jobs in this
  book.** Five of Chapter 1's nineteen bold runs are terms; the other fourteen are
  craft-section worksheet labels. Matching folds case, collapses whitespace and
  drops ONE leading article, so prose "the consumption event" reaches the callout
  headed "Consumption event". **Trailing punctuation is deliberately NOT stripped**,
  because stripping the colon from the worksheet label "Meter:" would let it match
  a term named Meter and turn a form field into a definition link. That trades a
  missing link for a wrong one, and the missing link is the cheaper failure.
- **A TERM WITH NO CALLOUT STILL LINKS, to its key-term entry.** "Resource
  consumption model" is bolded and is a key term but has no callout, and leaving
  it alone gives a page where four bolded terms are links and a fifth
  identical-looking one is not. The callout wins when a term has both, because it
  sits beside the prose that introduces the term.
- **A LINKED TERM LOOKS EXACTLY LIKE UNLINKED BOLD AT REST.** Bold already carries
  meaning in the prose, so an ordinary link colour would put a second signal on
  the same word and turn a page of definitions into a page of link decoration,
  which is close to what standing rule 5 forbids. The affordance is a hairline
  that fills in on hover.
- **THE TERM-LINK COUNT IS PRINTED AND A ZERO WARNS, because nothing else would
  notice.** Reword a term, every link disappears, and no gate fails: a missing
  anchor breaks nothing. It reports rather than fails, like the snapshot
  divergence warning.
- **THE LANDING PAGE QUOTES THE BOOK AND NEVER PARAPHRASES IT, enforced by gate
  W9a.** The theorem and a specimen paragraph are lifted verbatim from the locked
  chapter and must appear in both. Rule 4a forbids paraphrasing a registry
  statement inside a chapter; a marketing surface is where that matters most,
  because it is where a reader forms their idea of what the book says.
- **THE REGISTER'S `note` FIELD IS NEVER PUBLISHED, enforced by gate W9b.** It is
  the fact checkers' working record: finding IDs, instructions to later checkers,
  and VERBATIM QUOTATIONS OF SENTENCES THE BOOK HAS CUT. The note behind Chapter
  1's first citation quotes both the SF2 continuation mechanism and the FC9
  absorbed-cost inference. A first draft of the landing page printed it in full,
  and gate W3 caught it only because the note contains straight apostrophes, which
  is luck rather than a check. Only bibliographic fields may be published.
- **Phase W5 is built, 2026-08-13. `web_build.py --site` builds the WHOLE site**,
  discovering every locked chapter from `Drafts/`, and emits sitemap, robots, 404
  and (with `--base-url`) CNAME. TEN gates. Gate W10 is deploy readiness: every
  locked chapter built, no `noindex` page in a publish build, sitemap complete,
  assets present.
- **DISCOVERY MUST NEVER BE ABLE TO PICK A STALE FORK, AND ONE IS STILL SITTING
  THERE.** `Drafts/Ch01_.../00_Stage0_Draft/` holds `DRAFT-AIOM_ch01.html`, a
  superseded copy with `lang="en"` and no source register: exactly the Decision 50
  hazard. `discover_chapters()` excludes `DRAFT-*`, `_*` and `*.print.html` by
  name, fails if more than one candidate remains, and PRINTS WHAT IT SKIPPED on
  every build so the choice is never silent. Deleting the stale file is Dan's.
- **THE TWO-CHAPTER PATH IS PROVEN BEFORE CHAPTER 2 EXISTS.** `web_gates_selftest.py`
  synthesises a second locked chapter in a throwaway tree and asserts the site
  builds two chapter pages with both in the sitemap. Code that works for one
  chapter is not thereby known to work for two.
- **NO ANALYTICS AND NO CDN, ENFORCED BY GATE W11.** Decision 66. Every
  subresource the site fetches must be same-origin: no analytics script, no CDN
  stylesheet, no remote image, and fonts stay self-hosted. Outbound ANCHOR links
  are deliberately exempt, because a link a reader chooses to follow is not a
  request the page makes for them, and the sources page exists to link out.
- **Hosted on GitHub Pages, published from `main`. Decision 65.** The domain is
  still unruled; `--base-url` is unset, so no hostname is invented and the sitemap
  emits site-relative paths that become absolute the moment one is supplied.
- **Phase W6 is built, 2026-08-13: dark mode and the figure token pass.**
  THIRTEEN gates. `AIOM_web.css` v0.3.
- **WHAT PUBLISHES IS EACH CHAPTER'S LAST LOCK, NEVER THE WORKING TREE. Ruled
  2026-08-13, and it is what makes a locked chapter editable.** Before it,
  reopening Chapter 1 failed the entire site build with "W10: no locked chapter
  found", so CI stayed red for the length of any revision and nothing else could
  deploy. `snapshot.py` resolves each chapter's lock as the newest commit whose
  version of its checklist reported Stage 9, materializes that state into a
  Drafts-shaped tree, and the build runs against that. Editing the working tree
  now has no effect on the live site at all. **The site keeps serving the old
  snapshot SILENTLY while a revision is open**, which is Dan's ruling and is what
  a publisher does. `--from-worktree` builds the working tree for local preview
  and CI never uses it.
- **THE SNAPSHOT IS DERIVED, NOT STORED, AND BOTH ALTERNATIVES WERE REJECTED FOR
  NAMED REASONS.** A committed `published/` copy would put the chapter text in
  the repository twice, which is the Decision 50 hazard with no possible gate,
  because the two copies are SUPPOSED to differ while a revision is open. An
  explicit lock tag can be forgotten, and a forgotten tag publishes a stale
  chapter with nothing reporting it. Deriving from the checklist cannot be
  forgotten and needs no new artifact.
- **CI MUST FETCH FULL HISTORY AND THIS IS NOT AN OPTIMIZATION TO REMOVE.**
  `actions/checkout` defaults to depth 1, at which the walk over checklist
  commits sees nothing, every chapter resolves to "never locked", and the build
  fails. `.github/workflows/web.yml` sets `fetch-depth: 0` with a comment saying
  why.
- **THE HOLE THE SNAPSHOT LEAVES IS REPORTED, NOT HIDDEN.** If a locked
  chapter's text is edited without reopening its checklist, the record has
  stopped being true while the snapshot stays correct. Every build prints a
  WARNING naming that chapter. It is deliberately NOT a failure, because failing
  would reintroduce the exact coupling this removes.
- **GATE W14 IS THE ONLY GATE IN EITHER SUITE THAT READS MEANING, AND IT EXISTS
  BECAUSE MEANING IS WHERE THIS PROJECT'S DAMAGE HAPPENS.** Added 2026-08-13.
  SF8, SF9 and SF10 were reverted during a copy edit with every date and figure
  intact, so nothing checking values could see it; FC2 repeated the shape and the
  case bank carried a withdrawn claim for seventy days. Five instances, none
  visible to any check that existed. W14 reads `AIOM_Claim_Ledger.md` and fails
  the build when a REQUIRED sentence goes missing or a FORBIDDEN one returns.
  Verified against all six historical reverts rather than against invented
  faults, and its controls in the self-test reproduce the real ones.
- **THE CLAIM LEDGER IS WRITTEN FROM THE CHAPTER, NEVER FROM THE REGISTER NOTE.**
  Reading the notes directly was tried first and is wrong twice over. They use
  the apostrophe as delimiter and possessive at once, so a quoted `the team's
  heaviest users` cannot be parsed. Worse, **a note holds SUPERSEDED ruled forms
  beside the current one**: the `altman-2025-pro` note carries two sentences
  introduced by "the sentence now reads", and the `microsoft-2026-q2-call` note
  records "over 4.7 million" where the chapter, after SF7, says "had passed 4.7
  million". The first draft of the ledger copied that superseded form and W14
  failed on it immediately, which is the trap working as intended. Notes record
  how the text got here; the ledger states where it must be now.
- **TWO REGISTER NOTES QUOTE SENTENCES THE CHAPTER DOES NOT CONTAIN.** Found
  2026-08-13 while building W14. The SF3 note omits "for Copilot"; the
  `altman-2025-pro` note keeps a pre-SF11 form. Both are the SF7 and SF11 drift
  shape recurring inside the very notes that exist to prevent it. The chapter is
  correct in both cases and the notes are imprecise, so nothing is broken, but
  **the notes should be corrected at the next reopen** and the ledger records the
  discrepancy at each entry.
- **A GATE IS ONE W-NUMBER, NOT ONE CHECK, AND THIS COUNT DRIFTED FOR FIVE
  PHASES BEFORE ANYONE RE-DERIVED IT.** The web suite is W1 through W17, so it is
  SEVENTEEN gates as of 2026-08-15, when W17 was added. Phase counts above are
  stated as they stood at that phase and are not restated here. Sub-lettered
  checks are parts of their gate, never gates: `W1a` and `W1b` are one gate, and so
  are `W4a` through `W4g`, `W7a` and `W7b`, `W8a` through `W8c`, `W9a` and
  `W9b`, `W16a` through `W16c`, and `W17a` through `W17c`. The Phase W1 and W2 entry was right at SIX and every entry after it ran
  one high, because W1's two channels were silently counted as two gates while no
  other gate's sub-parts ever were. Corrected 2026-08-13, on Dan's ruling, after a
  README draft asserted fourteen and the number was checked against the build
  output for the first time. **Re-derive this from `web_build.py` output rather
  than copying it forward, which is how it got to five documents.**
- **THE ACCENT PASS, 2026-08-13: paper grain and the department line.** Dan's
  brief was "New Yorker meets Comptoir des Cotonniers", accents rather than an
  overhaul, and **marks in chrome only**. Two things landed. `--grain` puts a
  whisper of tooth on the ground through an inline SVG turbulence data URI, and
  `.eyebrow` gained a short rule running into it, which is the magazine rubric.
  Both borrow the TECHNIQUE and refuse the REGISTER, which is the same rule
  `AIOM_Voice_and_Craft_v1.md` already applies to the four prose exemplars: a
  New Yorker spot drawing would import a whimsy that C6 rules out, so any future
  spot marks are drawn as instruments rather than as jokes.
- **THE SPOT MARKS ARE CHROME ONLY, AND GATE W4g ENFORCES IT.** Ruled twice by
  Dan, 2026-08-13: the chapter is a reading surface, the sidenote layout is
  already its distinctive thing, and a mark there competes with the prose rather
  than framing it. Nine marks live on the landing page and the reference layer,
  in `web_templates/_marks.html.j2`. **W1 CANNOT COVER THIS RULE**, which is why
  it needed its own check: a mark is an SVG carrying no text, so text
  equivalence with print stays perfect while a reading page fills with ornament.
  The hero and the author band are unmarked on purpose too, since each already
  carries its own object.
- **EVERY MARK MEANS SOMETHING, WHICH IS WHAT KEEPS IT OUT OF STANDING RULE 5.**
  A mark that is about its section is a rubric device; a mark that is merely
  pretty is the decorative apparatus rule 5 forbids. The theorem mark sits above
  the theorem panel and states the same shape.
- **A MARK'S COLOUR IS NEVER LITERAL.** Two scoped properties, `--mark-ink` and
  `--mark-accent`, are redirected on `.invert` to `--invert-fg` and
  `--invert-accent`. Hardcoding `--navy` paints dark navy on the navy band,
  which is the defect gate W13 already found in the theorem panel's numerals.
- **DRAWN MARKS ARE JUDGED AT THE SIZE THEY SHIP AT, NEVER AT DISPLAY SIZE.**
  Three of the nine were redrawn after rendering a contact sheet at both sizes,
  and one took three attempts: a cross over the branch it cancelled turned to
  mud, and the stop bar replacing it shared an angle with its own branch so the
  mark read as a single arrow at 2.35rem. Render the sheet, do not reason about
  the geometry.
- **THE GRAIN SITS BEHIND THE CONTENT, NOT OVER IT.** The paper colour moved to
  `html` so `body::before` can carry the texture at `z-index: -1`. A fixed
  overlay painted on top would put noise over every line of type, which at this
  opacity is nearly invisible, and "nearly" is not a standard for a book. A
  tinted panel therefore covers the grain, which is correct: a panel is a
  different stock laid on the paper.
- **`--grain` IS A GAP IN GATE W13 AND THE TWO DARK BLOCKS MUST BE KEPT IN STEP
  BY HAND.** W13's token regex captures `--name: #rrggbb;` only, so a unitless
  opacity is invisible to it, including to the control that checks the two dark
  blocks agree. Any future non-hex token inherits the same gap.
- **THE FIRST GRAIN VALUE DID NOTHING AND WAS ONLY CAUGHT BY MEASURING.** At 0.055
  the rendered spread was 5 levels out of 255, which is indistinguishable from a
  flat fill. The value was swept against screenshots at 1x and 2x and set to 0.13
  light and 0.08 dark, the dark value lower because identical noise reads as
  banding once the ground is dark. Judge this by rendering and measuring, never
  by reading the number.
- **DARK MODE IS DESIGNED, NOT INVERTED.** The ground becomes a deep navy black
  derived from the book's own navy, which keeps the two-colour identity. A theme
  toggle sits in every topbar; the preference is applied in `<head>` before first
  paint, so there is no flash on navigation.
- **THE PRINT PALETTE FAILS WCAG AA AND THE WEB CORRECTS IT, MEASURED NOT
  GUESSED.** Five foreground tokens fail against paper and its tints: `--folio`
  worst at 2.38:1, then `--amber-fig`, `--amber`, `--teal`, `--axis`. Print has no
  WCAG floor and different physics, so **`AIOM_book.css` is untouched and the print
  values remain the values of record.** `AIOM_web.css` carries web text
  derivatives darkened by the minimum needed; four of five move imperceptibly and
  only `--folio` moves visibly. Gate W13 enforces the floor in both themes.
- **CHAPTER FIGURES ARE RETOKENIZED ON THE WAY TO THE WEB, never in the chapter.**
  `tokenize_svg()` maps each literal hex to the token that owns it, so figures
  follow the theme while the locked chapter stays untouched. It adds attributes
  and no text, so gate W1 is unaffected. Verified rather than assumed: `var()`
  DOES resolve in an SVG presentation attribute and DOES follow a theme change.
  An unregistered colour is left literal on purpose and failed by gate W12,
  because silently rewriting it would hide the drift.
- **GATE W13 SPENT ITS FIRST RUN MEASURING NOTHING.** Its token regex captured
  `--folio` while every lookup used `folio`, so the contrast loop skipped every
  pair and printed a pass. The self-test control caught it, and the fixed gate
  immediately found a real defect: in the LIGHT theme the theorem panel's roman
  numerals were dark amber on the navy band at 2.19:1. The inverted band now has
  its own `--invert-accent`, because that band is dark in both themes.
- **Print gates do not carry over and web gates are not print gates.** Pagination
  is the bulk of the print suite (gates 1, 4, 8, 12, 13, 14 and `place.py`) and
  none of it exists on the web. What carries is anything that is a property of
  the text: gates 2 and 15 became W3, and Decision 59 became W5.

### Rules that came from a check being wrong

The recurring failure in this repo is not a bad judgment call. It is a check that
reads green while measuring nothing, or a record claiming work nobody did.

- **Write a scope claim from what was done, never from what was intended.** A
  Stage 5 record said ten pages were rasterized and read; nine were, and the page
  it wrongly claimed is exactly where the next defect was sitting. That was the
  fifth instance in this repo of a check claimed in a record but not performed, and
  the first authored by Claude rather than inherited.
- **PUNCTUATION WENT UNGATED UNTIL 2026-08-12, AND GATE 15 NOW COVERS IT.** Gate 2
  tests em and en dashes and nothing else, so Chapter 1 shipped straight quotation
  marks in every generated footnote past fourteen green gates. When
  `cite_format.py` was corrected to emit `“Title,”` the fix doubled the comma in
  all six footnotes, because `_join` suppressed the separator by testing
  `endswith((',"', ",", "."))`, keyed on the ASCII quote, and those same fourteen
  gates passed the doubled comma twice: on the build that introduced it and the
  build that removed it. Gate 15, typographic marks, closes the first half of this
  by failing on any straight quote or apostrophe in the render. **It does not close
  the second half.** No gate reads a doubled comma, a spliced clause, or any other
  punctuation defect, so the general lesson stands: a green suite is evidence about
  what the gates measure and about nothing else.
- **A one-line change to shared tooling is not too small to re-verify, because a
  glyph-width change is a reflow.** Rebuild, RE-READ the pages the fix touches, and
  re-run any scan whose input it could move. A check whose input a fix could move
  is re-run AFTER the fix, not before it: a page read taken before a fix is
  invalidated by that fix.
- **When writing any check over rendered pages, decide explicitly what it does at
  a page boundary.** Gate 12 counted in-text figure references line by line, so a
  reference that wrapped was invisible. The hyphenation scan was later rewritten
  from memory with the same defect, testing only the following line within a page,
  which is exactly the blind spot that hid DR7 until it turned up across a page
  turn. Join the pages in reading order with folios and running heads stripped.
- **Gate 12's failure MESSAGE is misleading, though the check is sound.** A figure
  reference split across a page boundary vanishes from both pages' joined text, so
  the gate correctly fails and reports "captioned but never referenced", sending a
  reader hunting for a sentence that is present in the source.
- **A defect a raster raises is not a defect proved.** DR6 was seen by eye and that
  only raised the question; scanning every hyphenated line end against the
  chapter's proper nouns is what found DR7 and proved the list complete at exactly
  two. Eyeing 25 pages finds the first and misses the second, because a break at a
  page foot reads as an ordinary hyphen until the page turns.
- **Rewording is not a fix for a break.** A break is a property of the measure, not
  of the sentence, so it returns at the next reflow.

### Sourcing and fact checking

- **No source host is reachable from the Claude environment**, verified 2026-08-06
  against six of them, so Stages 3 and 7 are structurally external rather than
  external by preference. Claude can rule on whether prose stays inside what a
  register note says. Claude cannot verify the note against the source, and must
  not offer to.
- **Stage 7's external check must be fed a RENDER, never the chapter HTML.** Both
  production flags on Chapter 1's check 1 were phantoms of HTML extraction: it
  dropped the `<li>` contents of the theorem panel and reported the antecedents
  missing, and it collapsed the empty cells of a table leftward and reported a
  student-blank column misplaced. Disproving them cost a build. Note the sharper
  form: the table flag would reproduce even against the PDF under naive text
  extraction, because an empty cell contributes no text. It dies only to a read or
  to the geometry.
- **Run two external checks on different prompts rather than one thorough check.**
  Chapter 1's 2026-08-06 pair agreed on one finding out of six. The disagreement is
  the value.
- **Judge a proposed remedy separately from the finding it answers.** In that same
  pair both findings survived and neither proposed fix did: one proposed hedging
  language the voice rules prohibit, the other a second-source path below the floor
  already in force.
- **A ruled claim narrowing does not survive a copy edit on its own, and nothing
  mechanical sees it go.** SF8, SF9 and SF10 were reverted while every date and
  figure stayed intact, so no gate and no check on values could detect them. They
  were recoverable only because each register note quoted the exact ruled SENTENCE.
  FC2 then repeated the shape a fourth time on a second vendor, which makes it a
  drafting attractor rather than a closed incident: the copy edit reaches for "the
  vendor began charging" because it is shorter than "began enforcing allowances and
  offered a paid overage". Both sources are scheduled for reuse in Chapters 4 and
  11. Two consequences: quoting the sentence a fix adds is a control rather than a
  convenience, and a chapter whose fact check predates a copy edit must be diffed
  against the audited artifact before that fact check is credited.
- **Write every fact-check ruling back into the register note, with the condition
  that would reverse it.** A ruling recorded only in a checklist is one the next
  checker raises again.
- **Read the in-chapter Decision 51 register before using a figure from a cited
  study.** It can carry rulings the shorter `AIOM_Source_Ledger.md` note does not.
  G1 caught a real breach of exactly this: a published agent count reserved for
  Chapter 6 had been put into Chapter 1's prose.

### Design and pagination

- **Pagination in this design is tightly coupled, and a craft edit is not a local
  change.** A one-sentence reorder inside Chapter 1 failed the build twice, once by
  splitting a figure reference across a page turn and both times by pushing
  footnotes off their calling pages ELEVEN PAGES LATER. Build after any craft edit
  rather than reasoning about it, and attribute a new gate failure by rebuilding
  the committed state rather than assuming the edit caused it.
- **Gap G-II: gate 14 cannot see a stranded head GROUP.** It tests whether a HEAD
  is the last block on a page, so any non-head block trailing the group hides the
  defect. Decision 56a puts `break-after: avoid` on `.slot-label`, chained through
  `h2.case-title` and `p.provenance`, so a chapter is held off this by CSS rather
  than by the check. Until gate 14 treats a run of head-like blocks as one unit, a
  chapter whose pagination moves must have its slot openings READ, not merely
  gated. Gap G-I, in section 6, has the same consequence for callout placement.
- **DR3a is an accepted cost, recorded so it is not rediscovered.** Holding an
  inventory table whole leaves the page carrying its instruction about four inches
  short and separates the two. `break-before: avoid` was tried on `table.inv` and
  rejected: WeasyPrint binds it to the preceding LINE BOX rather than the preceding
  block, so it split the problem statement across the spread. A short page is a
  smaller defect than a split paragraph.

### What Chapter 1 leaves standing for Chapters 2 to 15

- **No craft baseline band is in force, and that is deliberate.** The band recorded
  at Stage 4 on 2026-08-06 measures a chapter the copy edit replaced.
  `AIOM_Voice_and_Craft_v1.md` section 4 makes Chapter 1 the band later chapters are
  read against, so the stale numbers would grade Chapter 2 against a text that no
  longer exists. Dan ruled the reset deferred to Stage 9 so it is taken from the
  locked text, and it is booked as a Stage 9 pending action. **Until then no chapter
  is read against a band.**
- **Chapter 1's craft verdict rests on one read by the model that drafted it and
  wrote the standard it grades against.** Stage 2 and Stage 4 were both closed with
  their second-model gut-check still open, on Dan's ruling, with the adversarial
  method and the per-section table as the only correctives. This matters twice
  over, because the baseline band above comes from that read and Chapter 1 is the
  exemplar. The verification prompts are in the chapter checklist and can be run at
  any time; a finding either raises reopens its step.
- **The Stage 2 developmental rulings D1 through D6 and the four voice rulings,
  Decisions 42 to 45, still stand as rules** even though the steps that produced
  them were reset.
- **A reopen archives rather than destroys.** Every step's findings stay in the
  checklist marked superseded, because they state what was examined and how it was
  ruled, and a re-run should not have to rediscover that.

### Registry, ledger, and the open decision

The design system is locked: CSS at v7.1, design spec at v7.1. Design finalization
is complete (D0 closed, 2026-07-28). The registry is validated: 228 objects load
(200 propositions, 20 lemmas, 8 theorems), eight book-mapped theorem IDs resolve,
zero dangling references in the dependency graph.

**The continuity ledger is built.** `AIOM_Continuity_Ledger.md` holds the record
and `continuity.py` is gate G3, running all seven checks the G3 checklist names. It
currently holds no entries, which is correct: entries are appended at Stage 9, and
no chapter has locked. Lock is not blocked.

One decision still open: **Decision 28**, the Northmoor property gap. The M3 build
asserts properties A through F; Decision 18 in the Addendum extended the list to A
through I. G, H, and I remain unbuilt. This gates the Ch9, Ch12, and Ch13 problem
sets, not Ch2.

Registry flags to carry into the appendix build (Phase 3, Appendix A):

- LEM-015 is retired. Skip it explicitly. IDs run LEM-001 through LEM-021 with
  LEM-015 absent.
- The "20 lemmas" count is correct as an object count. The ID range runs to 21.
- The registry ships a pre-built trace for THM-005, which is a Ch6 asset, not
  THM-004. Chapter 3's trace set piece uses THM-004 and must be built separately.
  Traces are generable mechanically from the dependency graph, so Figure 3.1 is
  buildable from data.

Appendix A reproduces the 28 theorems and lemmas only. The 200 propositions are
cited by ID and not reproduced in full.

---

## 11. Session handoff protocol

`HANDOFF.md` is the running session-to-session log. It carries the working state
that does not belong in this file: the active branch, what is committed and
pushed, the live open threads, and the standing reminders learned in recent
sessions. CLAUDE.md holds the durable rules; HANDOFF.md holds the perishable
state.

1. **At the start of every session, read `HANDOFF.md` before doing any work,**
   alongside this file. A SessionStart hook in `.claude/settings.json` prints it
   into context automatically, so it is in front of you already; read it rather
   than skipping past it.
2. **Before ending a session, update `HANDOFF.md` so it is accurate.** Refresh
   the last-updated date, the repository state (branch, what is pushed, whether
   `main` is behind), the chapter status, the open threads in priority order, and
   any standing reminder that changed. Then commit it. A handoff that lies about
   the branch or the sync state is worse than none, so verify the facts against
   `git status` and `status_check.py` rather than copying the previous entry.
3. **Keep the division of labor clean.** A durable rule or a closed decision
   graduates into CLAUDE.md or the decision log. Do not let HANDOFF.md accumulate
   settled rulings, and do not let CLAUDE.md drift into session bookkeeping.
