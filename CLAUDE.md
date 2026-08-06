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
5. **No decorative apparatus.** Signposting is done through the skeleton, not
   through prose. Do not tell the reader what the chapter is about to say before
   saying it.

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
| `AIOM_build.py` | Font staging, WeasyPrint render, fourteen QA gates, toolchain preflight. One command. |
| `AIOM_book.css` | The locked design system. |
| `place.py` | Definition-callout placement pass. See section 6. |
| `AIOM_Continuity_Ledger.md` | The G3 record: terms owned per chapter, forward references and whether paid, registry glosses, Northmoor figures, and the canonical Founding Questions and maturity stages. Appended at lock, never edited to make a gate pass. |
| `continuity.py` | Gate G3. Seven checks against the ledger. `--update` appends at Stage 9; `--pay N` marks promises kept. |
| `reopen.py` | Reopens a chapter at a stage: resets that step and everything after it, archives their findings in place rather than destroying them, and writes a dated reopen record. The mechanism CLAUDE.md section 8 always assumed and never had. |
| `renumber_stage_folders.py` | One-time Process v1 to v2 stage-folder migration. Run 2026-08-05 across all eighteen units. |
| `requirements.txt` | Pinned build toolchain. WeasyPrint line breaking and float placement move between releases, and gates 4 and 14 are sensitive to exactly that. |
| `AIOM_Design_QA_Spec_v1.md` | Gate-by-gate spec. Moves with `AIOM_build.py`. |
| `AIOM_Consolidated_Spec_v1.md` | The full pre-drafting specification. Authoritative. Markdown despite the earlier `.pdf` reference. |
| `AIOM_Voice_and_Craft_v1.md` | The positive voice standard: the four borrowed techniques, the guard, and the six craft criteria. Binds from Stage 0. Read before drafting. |
| `AIOM_Specification_Addendum_v1.0.docx` | Decisions 1 through 21 and the Addendum rulings. |
| `AIOM_Structure_v1.md` | Chapter structure and structural devices. |
| `AIOM_Exit_Competencies_v1.md` | The twenty-four competencies. Backward-design root. |
| `AIOM_Maturity_Model_v1.md` | Stage definitions. Ch13 craft. |
| `AIOM_Case_Bank_v1.md` | Cited cases with reuse policy. |
| `AIOM_Northmoor_Dataset_v1.md` | Capstone dataset design. |
| `AIOM_Workplan_v5.md` | Current workplan and per-chapter tracker. Supersedes v4, which is retired. |
| `AIOM_Validation_Matrix_v1.xlsx` | The 28-row Appendix A trace matrix. Working artifact, never book content. Distinct from the full 228-object registry, which lives in Drive. |
| `chapters/` | Chapter HTML sources. |
| `fonts/` | Committed fonts (IBM Plex Sans, Jost) plus their OFL licenses. `fonts/use/` holds the six faces the CSS loads, so rendering needs no network staging. |

When spec placeholders conflict with operative content, trust the operative
content: the maturity model, Stage definitions, and chapter assignments win over
placeholder glosses.

---

## 5. Build commands

```bash
pip install -r requirements.txt                  # once per session, first
apt-get update -qq && apt-get install -y poppler-utils
python3 AIOM_build.py chapters/AIOM_ch01.html    # render plus all QA gates
python3 AIOM_build.py chapters/AIOM_ch01.html --out build/Ch1.pdf
python3 place.py chapters/AIOM_ch01.html         # callout placement pass
python3 voicecheck.py chapters/AIOM_ch01.html    # Stage 4 mechanical plus craft metrics
python3 status_check.py                          # lifecycle status, authoritative
python3 reopen.py <checklist.md> --from "Stage 2" --reason "..."   # reopen
```

Fonts are committed under `fonts/`, so `--fonts` is not needed and the render
requires no network. The build exits 2 without running any gate if its toolchain
is missing.

System dependencies WeasyPrint requires: `libpango-1.0-0`, `libpangoft2-1.0-0`,
`libcairo2`, `libgdk-pixbuf-2.0-0`, `libffi-dev`, `shared-mime-info`.
Python: `weasyprint`, `pdfplumber`, `pdf2image`, `pillow`, `openpyxl`, `fonttools`.

---

## 6. QA gates and their remedies

The suite is fourteen gates. Full detail in `AIOM_Design_QA_Spec_v1.md`. The ones
that fail most often:

- **Gate 1, horizontal overflow.** 428.4pt odd pages, 417.6pt even, 1.5pt
  tolerance. Catches unbreakable strings, oversized SVG text, table cells that
  will not wrap.
- **Gate 2, em and en dashes.** Fails on any `U+2014` or `U+2013`. Note this is
  stricter than the standing rule, which bans em dashes only. Open question Q2.
- **Gate 4, definition callout splits.** Fails a callout sitting flush at the top
  margin, the signature of one that broke across a page. **Remedy: run
  `place.py`.** Do not try to fix this in CSS. WeasyPrint 69 ignores
  `break-inside: avoid` on floated elements.
- **Gate 5, font faces.** Expected set only. Catches a missing `@font-face`, an
  unstaged font falling back to a system face, and stray faces inside SVG.
- **Gate 7, provenance line.** Page 1 must carry the 7pt amber semibold line
  beneath the opening case title.

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

---

## 10. Current state

**Chapter 1 was reopened at Stage 0 on 2026-08-05 and is now 7 of 13.** Stage 0
(re-draft), G1 (structural gate), Stage 1 (content review), and Stage 2
(developmental edit) all passed 2026-08-05; Stage 3 (source and fact check 1),
Stage 4 (voice and craft check), and Stage 5 (design review) passed 2026-08-06.
`status_check.py` reports 7/13 with STATUS CONSISTENT. Stage 5 (design review) also passed 2026-08-06, taking the
chapter to 7 of 13 and producing its first fully green render: all fourteen
gates pass on 19 pages. G2, the production gate, is next and is Claude's.

**Stage 4 passed without its second-model gut-check**, which Dan ruled complete
without it. The craft verdict on Chapter 1 therefore rests on one read by the
model that drafted the chapter and wrote the standard it grades against, with the
adversarial method and the per-section table as the only correctives. This
matters past Chapter 1: the baseline band that Chapters 2 to 15 are read against
comes from that read, and Chapter 1 is the exemplar the other fourteen are
drafted against. The verification prompt is still in the chapter checklist and
can be run at any time; a finding it raises enters as NC7 and reopens Stage 4. The prior record is not
lost: every step's findings are archived in place in the checklist, marked
superseded, because they state what was examined and how it was ruled and the
re-run should not have to rediscover that.

**Stage 3 established two things worth carrying to every later chapter.** First,
run two external checks on different prompts rather than one thorough check. The
2026-08-06 pair agreed on one finding out of six: check 2 confirmed a passage
check 1 had raised, and check 1 caught a sourcing gap check 2 restated as sound.
The disagreement is the value. Second, judge a proposed remedy separately from
the finding it answers. Check 1 was right that a superlative was unsourced and
proposed hedging language the voice rules prohibit; check 2 was right that
durability rests on access dates and proposed second source paths below the floor
already in force. Both findings survived and neither fix did.

**No source host is reachable from the Claude environment**, verified 2026-08-06
against six of them, so Stages 3 and 7 are structurally external rather than
external by preference. Claude can rule on whether prose stays inside what a
register note says. Claude cannot verify the note against the source, and must
not offer to.

Grounds for the reopen. Chapter 1 was drafted before the voice and craft standard
existed (Decision 52), so its prose was never written against C1 through C6. The
Stage 4 craft read found seven findings, including a systematic C5 failure (four
paragraphs closing on a cross-reference) and the weakest C4 unit in the book (the
summary, at twice the chapter's mean sentence length with zero short sentences).
Chapter 1 is the exemplar the other fourteen chapters are drafted against, so it
is re-drafted rather than patched, and the re-draft doubles as the proving run for
Process v2 end to end.

What the reopen inherits, as carried items for the re-draft:

- The seven craft findings and two watch items, archived under Stage 4.
- **A real production defect found by new gate 14 on its first run**: the "Craft
  section" slot label stranded alone at the foot of page 12, with the section it
  labels opening on page 13. The eleven-gate suite passed this render. The
  fourteen-gate suite fails it. CLOSED 2026-08-06 at Stage 4, not at Stage 5:
  applying craft finding NC2 cut two sentences from 1.4, the pagination moved,
  and gate 14 now reports zero stranded heads on a 19-page chapter. The gate
  found a real defect the older suite passed, and the defect outlived a full
  re-draft and every Stage 3 edit before a two-sentence craft cut removed it. The
  other three defects, one gate 4 callout split and a widow and an orphan on page
  16, did not move with it and remain Stage 5 work.
- The nine verified sources in `AIOM_Source_Ledger.md`, which the re-draft should
  reuse rather than re-verify, subject to Dan's Stage 3 re-run.
- The Stage 2 developmental rulings D1 through D6 and the four voice rulings
  (Decisions 42 to 45), all still standing as rules even though the steps reset.

Three things the re-run has already proved. G1 caught a real breach of a standing
source ruling in the re-draft: the published QJE agent count had been put into
prose, where a 2026-07-29 ruling reserves it for Chapter 6. The fuller ruling
lives in the chapter's own Decision 51 register, not in the shorter
`AIOM_Source_Ledger.md` note, so read the in-chapter register before using a
figure from a cited study. Stage 1 ruled seven structural findings without
changing one word of the chapter, so no downstream step was invalidated, which is
what the scoped re-run matrix exists to produce. And Stage 2 found six
developmental findings of which four were applied as ND1 through ND4, landing
those line edits before fact check, voice, design, and production rather than
churning them afterward, which is the whole reason Process v2 moved the
developmental edit early.

Process built 2026-08-05 to make the re-run safe and repeatable across fifteen
chapters: `reopen.py`; the Process v1 to v2 stage-folder migration across all
eighteen units (162 folders renamed, 18 developmental-edit folders created);
gates 12, 13, and 14; the toolchain preflight and `requirements.txt`; and a G2
checklist that now mirrors the fourteen printed gates one for one, with the two
genuinely manual checks labelled as manual.

**The continuity ledger is built (2026-08-05).** `AIOM_Continuity_Ledger.md`
holds the record and `continuity.py` is gate G3, running all seven checks the
checklist names. Verified end to end against the superseded Chapter 1 render: it
found the six forward references, detected unpaid promises when run as a later
chapter, recognised a term restated verbatim as not a redefinition, and failed on
a placeholder registry gloss rather than passing it. The ledger currently holds
no entries, which is correct: entries are appended at Stage 9, and no chapter has
locked. Lock is no longer blocked.

Design finalization is complete (D0 closed, 2026-07-28). The design system is
locked: CSS at v6.7, design spec at v6.8 plus three addenda. The registry is
validated: 228 objects load (200 propositions, 20 lemmas, 8 theorems), eight
book-mapped theorem IDs resolve, zero dangling references in the dependency
graph.

Chapter 2 ("The Flow") is the immediate next drafting target and is unblocked.
Chapters 3 through 15 follow in sequence. Front and back matter come after the
manuscript.

One decision still open: **Decision 28**, the Northmoor property gap. The M3
build asserts properties A through F; Decision 18 in the Addendum extended the
list to A through I. G, H, and I remain unbuilt. This gates the Ch9, Ch12, and
Ch13 problem sets, not Ch2.

Registry flags to carry into the appendix build (Phase 3, Appendix A):

- LEM-015 is retired. Skip it explicitly. IDs run LEM-001 through LEM-021 with
  LEM-015 absent.
- The "20 lemmas" count is correct as an object count. The ID range runs to 21.
- The registry ships a pre-built trace for THM-005, which is a Ch6 asset, not
  THM-004. Chapter 3's trace set piece uses THM-004 and must be built
  separately. Traces are generable mechanically from the dependency graph, so
  Figure 3.1 is buildable from data.

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
