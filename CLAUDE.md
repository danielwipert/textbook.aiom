# CLAUDE.md

Project context for *AI Operations Management*. Read this before touching anything
in this repository. **This file holds the rules. The reasoning and the incident
behind each one are in `LESSONS.md`**, which is read before any tooling work and
whenever a check behaves oddly, not before every drafting session (Decision 80).
The full text of this file as it stood before that cut is
`archive/CLAUDE_to_2026-09-30.md`.

---

## 1. What this is

A founding academic textbook establishing AI Operations Management as a discipline.
Fifteen chapters, four parts. Print-quality PDF produced through a WeasyPrint
pipeline in this repo, and a website from the same source.

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
   rule under stress. A build gate enforces it, and it also fails en dashes: a
   number range sets with a hyphen (`889-942`), and the register stores it so.
2. **Every empirical claim is cited to a real source, rewritten as a formal
   conditional, or cut.** No third option. Never invent a citation, a statistic,
   or a source. If the claim cannot be sourced, cut it and say so. A sentence
   saying how often organizations do something is an empirical claim
   (Decision 78).
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
   The panel is CHECKED, not trusted: `chapter_check.py` fails a chapter that
   renders an object which does not exist, is not certified, or carries a name
   the registry does not carry (section 9).
5. **No decorative apparatus.** Signposting is done through the skeleton, not
   through prose. Do not tell the reader what the chapter is about to say before
   saying it.
6. **Theorem statement form.** A registry conditional carrying more than two
   antecedents is set as a structured conditional, never as running prose: scope
   boundary first, before the word "if"; antecedents enumerated in lower-case
   roman, one per line; consequent on its own line opening with "then". Render
   registry shorthand into full parallel English, and never change the logic. No
   antecedent added, dropped, merged, split, weakened, or strengthened. Full rule
   in `AIOM_DESIGN_SPEC.md` section 5; Decision 56.

### Voice: Concrete Management Prose

**THE ONE PROSE STANDARD IS `AIOM_Prose_Standard_v2.0.md`. READ IT BEFORE
DRAFTING.** Decision 71. It is the only place prose rules live; the v1 files and
Consolidated Spec B.2 are pointers to it. The rules that bite:

- **Business reality first, abstraction second.** Begin a paragraph with its main
  business claim. Keep the actor visible. One main idea per sentence. Ordinary
  business language unless a technical term adds a real distinction.
  "Magisterial" is retired as a register and is never an instruction.
- **A coined term arrives AFTER the mechanism it names**, never before it.
- **Not neutral about the argument, completely neutral about individual actors.**
  Derive provider behavior, do not scold it.
- **Third person** in body prose. Second person sparingly in craft sections and
  discussion questions.
- **No contractions** in body prose (permitted in case dialogue and discussion
  questions). **No exclamation points. No rhetorical questions** in body prose;
  genuine management questions set in a list are permitted.
- **No hedging** ("perhaps", "some argue"). **Accurate qualification is not
  hedging**: the standard's section 13 rules the distinction.
- **No comma splices and no run-on sentences** (section 21). Ration the
  interrupter: never separate a subject from its verb by more than about three
  words, never stack two in one sentence (section 15).
- **Fifty-year rule:** body prose is timeless. Perishable specifics are
  quarantined in dated cases.

### Craft: the seven criteria

They bind at drafting time and are graded at the review, one finding per
criterion, from section 26 of the standard. They appear verbatim as sub-boxes in
every checklist and `status_check.py` fails a passed step with one left open.

- **C1. Concrete particular.** Every abstraction carrying argumentative weight is
  anchored to a named, specific instance.
- **C2. Context and stakes.** Every mechanism states the conditions that made it
  available and what it settles, not only what it does.
- **C3. Claim first.** Findings lead, qualifications subordinate, no throat
  clearing.
- **C4. Deliberate rhythm.** Sentence length varies. No long stretch at a uniform
  length.
- **C5. Paragraph close.** End on the load-bearing clause, not a trailing
  qualifier.
- **C6. The guard holds in both directions.** No hero or villain framing, no
  populist register, no character-driven causation where a structural account is
  available, and no false sophistication.
- **C7. Business reality first.** No paragraph opens on a framework where a
  business statement is available.

`voicecheck.py` prints advisory craft metrics beside the mechanical bans. They are
proxies, never a threshold. C2, C6 and C7 are enforced only by reading. The band
measured from locked Chapter 1 is in the standard's section 27.

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

## 4. Chapter lifecycle: Process v4

Adopted 2026-09-30, Decisions 75 to 81, from Chapter 3 onward. Evidence and
reasoning: `AIOM_Process_v4_Proposal_v1.0.md`. **The target is one week per
chapter, and the cost it attacks is hand-offs and re-checking changed text, not
the checks themselves.** Chapter 1 stays under Process v2 and Chapter 2 under v3;
a completed unit keeps the process it was completed under.

| v4 step | Checklist label | Owner | Dan |
|---|---|---|---|
| 1 Plan | Stage 0 | C | Sitting 1: approve the one-page plan |
| 2 Draft, self-checked | Stage 0, Gate G1 | C | none |
| 3 Review | Stage 4 | C, second model | Sitting 2: rule one list |
| 4 Author pass | Stage 6 | D | his rewrite, in Word |
| 5 Fact check | Stage 3 | D, external | Sitting 3: rule A and B |
| 6 Production | Stage 5, Gate G2, Gate G3 | C | none |
| 7 Sign-off and lock | Stage 8, Stage 9 | D, then C | Sitting 4 |

**The labels are kept from v3 on purpose** so every tool binds unchanged:
`chapter_check.py` binds W14 to Stage 3, voicecheck to Stage 4, the print render
to Stage 5, the web build to G2, continuity to G3, and the registry to G1; the lock
is Stage 9. The checklist order, not the number, is the order, and `reopen.py`
reads it from the checklist.

- **Plan (Decision 77).** One page before drafting: opening case and source,
  sections, craft artifact, registry objects, continuity promises, a source for
  every intended claim. Dan approves it.
- **Draft (Decision 78).** Claude runs every mechanical check before anyone
  reads: G1, `voicecheck.py`, `registry.py --check`, `continuity.py`,
  `chapter_check.py`, and `freqsweep.py`, whose whole list is cleared (cited,
  conditional, or cut, or kept as qualification for Dan) before the review.
- **Review (Decision 77).** One pass for structure (against
  `AIOM_Structure_v1.md` and `AIOM_Exit_Competencies_v1.md`), teaching quality,
  and voice and craft. ONE second-model package carries the three as separate
  sections and reads without Claude's findings, because a chapter judged by the
  model that drafted it is self-marking. Read adversarially: quote the WEAKEST
  evidence for each competency and criterion. **Dan rules every finding; Claude
  rules none.**
- **Author pass (Decision 75).** Dan's rewrite, through `copyedit_export.py` and
  `copyedit_import.py`. The unedited export must round-trip at zero changes
  before the pair is trusted on a chapter. The importer applies only what it can
  place unambiguously and prints the rest. After import, the mechanical checks
  and `freqsweep.py` re-run.
- **Fact check (Decision 76).** Once, on a fresh RENDER of the post-author-pass
  text, never the HTML. Two checks in parallel on different prompts: A reads the
  sources, B reads only the render. **The checker must have web access.** Judge a
  proposed remedy separately from the finding. Write every ruling into the
  register note with the condition that would reverse it, and into
  `AIOM_Claim_Ledger.md`, from the CHAPTER's sentence, never the note's.
- **Production.** Stage 5 design review (rasterize and read every page), G2, G3,
  once, after the text is final. Never run early.
- **Sign-off.** Render plus a diff since the author pass. Dan approves the whole
  or names one structural reason.

**Working rules for the process (Decisions 79 and 81).**

- **Four sittings, each with its package BUILT BEFOREHAND.** Rulings are batched
  and applied in one commit.
- **One line per finding** in the checklist: ID, what, ruling, commit. Reasoning
  goes in the commit message.
- **Tooling is frozen while a chapter is in flight.** A defect goes on the
  fix-between-chapters list in HANDOFF.md. Fix at once only what BLOCKS: a gate
  failing a correct chapter, a tool damaging text, a check hiding a real defect.
- **Gates are not passes.** A gate is mechanical and stops the chapter where it
  stands; a pass is judgment.
- **A passed step is a claim, and `chapter_check.py` holds it** (Decision 69).
  It fails only on checks owned by a ticked step, runs on every push in
  `chapter.yml`, and red means a tick is lying.
- **Status lives in the checklist checkbox.** `status_check.py` prints it and is
  the authority; HANDOFF.md and the Workplan mirror it.
- A reopen (`reopen.py --from <step>`) resets that step and everything after it
  in checklist order, archiving findings in place. It resets by position, not by
  the matrix below, so check what it cleared. After a reopen, check box TEXT
  against the generator, not only the ticks.

**Scoped re-run matrix, v4 labels.** An edit re-runs only what it can break.

| Edit class | Re-runs | Leaves intact |
|---|---|---|
| Body prose (claim or teaching) after the review | Review for the changed passages, fact check if a claim changed, voicecheck, Stage 5, G2 | G1 unless a slot moves |
| Citation or source only | Fact check, G2 | review, design |
| Figure order, geometry or number | Stage 5, G2 | review, fact check |
| Copy edit (typo, punctuation, no meaning change) | G2 | everything else |
| CSS or design system | Stage 5 and G2, every chapter | review, fact check |
| Voice or craft standard change | Review, every chapter not yet locked | fact check, design, G2 unless prose changes |
| Structural (slot added, removed, reordered) | G1, then every downstream step | nothing |

### After lock: the amendment path

Dan is the author and final editor. An edit he makes to a locked chapter is
approved by definition and runs through `amend.py`, which reopens nothing: the
chapter never leaves Stage 9. It runs the mechanical half only (W14, voicecheck,
print render and fifteen gates, web build) and reports before committing;
`--force` commits anyway on Dan's authority. **Batch edits: the cost is per run.**
The checklist is touched on every amendment, which is what advances the published
snapshot. A fact-check ruling Dan overturns is SUPERSEDED (`--supersede ID
"reason"`, or `--rule` for exactly what the edit broke), never bypassed. `--rule`
cannot see a withdrawn claim restated in new words. An amendment adding a NEW
empirical claim still needs a source, and that is the one thing Claude raises
unprompted.

**Editing-run protocol.** Dan sends prose; Claude applies it VERBATIM to the one
live text (previous wording comes from `git show`, never a second file); runs
`python3 amend.py ChNN -m "what changed" --rule`; reports ONE line. No proposed
alternatives, no second opinion on the writing.

---

## 5. How to work here

- **Present decisions one at a time**, with options, a recommendation, and the
  reasoning. Do not proceed past an unruled decision.
- **Structure before content.**
- **Verify programmatically before delivering.** Never report a build clean
  without running the gates.
- **Single attempts over retries.** Token waste is flagged explicitly.
- **Protect pedagogical surprises.** Later chapters withhold things deliberately.
- **Real cited evidence over constructed material,** every time it is available.
- **Write a scope claim from what was done, never from what was intended.**

### Git hygiene is Claude's job, not Dan's

1. **Run `python3 git_hygiene.py` BEFORE any merge and BEFORE closing a
   session.** It deepens the shallow clone first; never hand-roll the sweep,
   because a shallow clone counts merged branches as stranded.
2. **"Merge main up" means make the two level, never force.** Fetch first; if
   `git log origin/main ^HEAD` is non-empty, stop and read it.
3. **Merge up BEFORE a branch is retired.**
4. **One session, one branch, and say so in HANDOFF.** Check what the checklist
   already owns before numbering a finding or an artifact.
5. **Delete a branch once `git_hygiene.py` lists it as merged.** Remote deletion
   fails from the container with a 403; Dan runs it (HANDOFF reminders).
6. **A HANDOFF correction goes straight to `main`** (Dan, 2026-08-24). This
   licenses the handoff file and nothing else.

---

## 6. Build commands

```bash
pip install -r requirements.txt                  # once per session, first
apt-get update -qq && apt-get install -y poppler-utils
python -m playwright install --with-deps chromium   # only for W6, W15, W16b/c

LIVE=Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html

# The whole mechanical suite on any chapter. The one command after any edit.
python3 chapter_check.py Ch01          # or --all; --no-print skips the render
python3 status_check.py                # lifecycle status, authoritative
python3 voicecheck.py "$LIVE"          # voice bans plus craft metrics
python3 freqsweep.py "$LIVE"           # frequency claims to dispose of
python3 gen_checklists.py 3            # a v4 checklist for Chapter 3

# Print render plus the fifteen gates. Build from the REPO ROOT on a copy: the
# base_url is the HTML's own directory, so building in place loses the CSS and
# fonts. Create build/ first.
mkdir -p build && cp "$LIVE" _ch_build.html
python3 AIOM_build.py _ch_build.html --out build/Ch.pdf
rm -f _ch_build.html _ch_build.print.html

# Callout placement (gate 4 remedy). REWRITES the live file in place, needs
# AIOM_book.css and fonts/ symlinked beside it, and leaves a .bak to delete.
python3 place.py "$LIVE"

# Web edition. Site build, and the self-tests after any change to a builder.
python3 web_build.py --site
python3 web_gates_selftest.py ; python3 print_gates_selftest.py

# Author pass round trip. Without --apply the importer is a dry run.
python3 copyedit_export.py "$LIVE" --pdf build/Ch.pdf --out <name>
python3 copyedit_import.py <name>.docx <name>.manifest.json "$LIVE"

python3 reopen.py <checklist.md> --from "Stage 4" --reason "..."
python3 amend.py Ch01 -m "what changed" --rule
```

Fonts are committed under `fonts/`, so rendering needs no network. The build exits
2 without running any gate if its toolchain is missing, and a gate that did not
run is not a gate that passed. The web build without poppler prints `W17 SKIPPED`
and names the skip in its verdict line. Toolchain versions are pinned in
`requirements.txt` because line breaking and float placement move between
releases.

---

## 7. Gates: what they miss and how to fix them

Fifteen print gates (`AIOM_build.py`, spec in `AIOM_Design_QA_Spec_v1.md`) and
seventeen web gates, W1 to W17 (`web_build.py`). A gate is one number; lettered
parts are parts. Re-derive counts from tool output, never copy them forward.

- **Gate 4, a split definition callout: run `place.py`.** Never fix it in CSS;
  WeasyPrint ignores `break-inside: avoid` on floats.
- **Gate 12 passes illegible figures.** A FIGURE IS JUDGED ON THE PAGE: rasterize
  it and look at the size it ships at.
- **No gate measures page fill.** `AIOM_build.py` prints pages leaving over 110pt
  unused as an advisory. **The remedy for a figure that will not fit is to move
  its anchor LATER, not earlier.** Build the candidates and measure.
- **No gate reads a doubled comma, a splice, or any punctuation beyond dashes
  and straight quotes.** A green suite is evidence about what the gates measure
  and nothing else.
- **Three MANUAL items in every G2:** figure geometry against a raster, the
  rasterized page-level read, and figure legibility.
- **Gap G-I:** a floated callout can collide with a block panel unseen. **Gap
  G-II:** gate 14 cannot see a stranded head GROUP. When pagination moves, READ
  the affected pages and slot openings.
- **Pagination is tightly coupled.** A one-sentence edit can push footnotes off
  their pages eleven pages later. Build after any edit and attribute a new failure
  by rebuilding the committed state.
- **Rewording is not a fix for a break.** A break belongs to the measure.
- **DR3a is an accepted cost:** a short page before a whole inventory table.
- **Every gate has a negative control** (`web_gates_selftest.py`,
  `print_gates_selftest.py`). A control must name the gate that fails, and the
  unmutated chapter is the control's own control.
- **`source_html` is not optional when calling `AIOM_build.qa()`.**

---

## 8. What every chapter must carry

- **`lang="en-US"`, never `lang="en"`** (Decision 59): `en` hyphenates British.
- **`.nb` on proper nouns** (Decision 58), so none breaks at a line end.
- **One live text per chapter, in `00_Stage0_Draft/`. Supersede and delete,
  never fork** (Decision 50). Check the path before every edit.
- **Every figure referenced in text and read on the page.**
- **A figure from a cited study is checked against the in-chapter Decision 51
  register**, which can carry rulings the source ledger lacks.

---

## 9. Sourcing, registry, and continuity

- **WebSearch works; WebFetch and curl do not reach sources from this
  container.** Claude can find candidates, and cannot read a primary, verify a
  quotation or check a figure. **The fact check is therefore external**, and an
  external checker CAN read. A case found by search is filed at Grade C with a
  provenance line saying no article was read.
- **Feed an external check a render, never HTML.** HTML extraction produced both
  phantom flags on Chapter 1's first check.
- **A ruled claim narrowing does not survive an edit on its own.** W14 and
  `AIOM_Claim_Ledger.md` hold it; quote the sentence a fix adds.
- **The registry is `dag.aiom`, pinned in `AIOM_Registry_Manifest.json`**
  (Decision 72): 413 objects. The bundle is never committed; the manifest carries
  hashes and no statements. **The book renders and cites CERTIFIED objects
  only.** `registry.py --check` runs under G1. LEM-015 is uncertified and skipped.
  Appendix A reproduces the certified theorems and lemmas; uncertified ones are
  listed by ID with blockers.
- **The continuity ledger is gate G3** (`continuity.py`, seven checks),
  appended at lock with `--update`, promises paid with `--pay N`, never edited to
  make a gate pass.
- **Open: Decision 28**, Northmoor properties G, H, I, gating the Chapter 9, 12
  and 13 problem sets.

---

## 10. The web edition

Plan in `AIOM_Web_Edition_Plan_v1.0.md`, Decisions 60 to 67 and 70. Domain
`aioperationsmanagement.ai`, served at the root from `main` by GitHub Pages.

- **The web is a second PRESENTATION, never a second text.** W1 requires web body
  text character-identical to print. Figures and bold terms are transformed by
  adding attributes, never text, and the locked chapter is never edited for the
  web.
- **What publishes is each chapter's LAST LOCK**, resolved by `snapshot.py` from
  the checklist history, never the working tree. **CI needs `fetch-depth: 0`.**
- **Only locked chapters publish** (W2). Each publishes its typeset PDF, gated by
  W17.
- **Never read `archive/AIOM_ch01_markdown_noncanonical.md` for prose.** It is
  pre-fact-check.
- **The register `note` field is never published** (W9b). **The landing page
  quotes the book and never paraphrases it** (W9a).
- **No analytics and no CDN** (W11). Fonts are self-hosted.
- **Marks are chrome only, never in a chapter** (W4g), and each means something.
- **Print palette values are the values of record**; the web carries WCAG AA
  derivatives, and W13 enforces the floor in both themes.
- **The web body face is Archivo; print keeps Plex Sans Text.** Verify a face by
  measuring a string, never by looking (W16).
- **A breakpoint is arithmetic.** Re-derive the section 17 sum in `AIOM_web.css`,
  enumerating every term, after touching its tokens or the type clamp, then sweep
  widths for notes off the edge, which no gate sees.
- **A link is verified by following it** (W15, over HTTP at the deploy prefix).

---

## 11. Rules for writing a check

The recurring failure here is a check that reads green while measuring nothing.
Each rule below has its incident in `LESSONS.md`.

- **A green suite is evidence about what the gates measure and nothing else.**
- **Give every new check a negative control that names the owning gate.**
- **Compare two things prepared the same way.** A file to a file, a rendering to
  a rendering, an extraction to an extraction under the same rule.
- **A check that reports SKIPPED on its own fault is switched off by it.** Keep
  setup that can fail outside the catch-all.
- **Decide what a check does at a page boundary.** Join pages in reading order.
- **Use the balanced scanner `find_spans`, never a non-greedy regex over nested
  elements; collect ids by parsing start tags, never by regex.**
- **Handle `span.nb` before the generic tag rule in any extractor.**
- **A one-line change to shared tooling is a reflow.** Rebuild and re-read what
  it touches; a check whose input a fix could move is re-run after the fix.
- **When a check and the prose disagree, fix whichever is wrong and say which.**
- **A second chapter is a test instrument.** Expect each new chapter to expose
  checks that only ever saw one.

---

## 12. Repository map

| Path | What it is |
|---|---|
| `AIOM_build.py`, `AIOM_book.css` | Print render and its fifteen gates; the locked design system (v7.1). |
| `web_build.py`, `AIOM_web.css`, `web_templates/` | Web edition, seventeen gates, per-chapter PDF. Chrome lives outside `<article id="chapter-text">`. |
| `chapter_check.py` | The mechanical suite on any chapter; what CI runs (`chapter.yml`). |
| `status_check.py`, `gen_checklists.py`, `reopen.py` | Checklist status, generation (v4), reopen. |
| `amend.py`, `snapshot.py` | Post-lock edits; what publishes. |
| `voicecheck.py`, `freqsweep.py`, `claimcheck.py` | Voice bans and metrics; frequency claims; gate W14. |
| `continuity.py`, `ledger.py` | Gate G3; the ledger as data. |
| `registry.py` | Registry manifest, inherited vocabulary, object checks. |
| `footnotes.py`, `cite_format.py`, `place.py` | Citations to notes; callout placement. |
| `copyedit_export.py`, `copyedit_import.py` | The author pass round trip. |
| `factcheck_packet.py`, `prose_extract.py` | Fact-check packet; second-model reading text. |
| `web_gates_selftest.py`, `print_gates_selftest.py` | Negative controls. |
| `git_hygiene.py`, `specimen.py`, `book_structure.py` | Branch sweep; type specimen; parts and chapters from the structure doc. |
| `renumber_stage_folders*.py` | One-time folder migrations (v2, v3, v4). |
| `AIOM_Prose_Standard_v2.0.md` | THE prose standard. |
| `AIOM_Process_v4_Proposal_v1.0.md` | The process in force and why. |
| `AIOM_Workplan_v5.md` | Tracker and **the decision-numbering authority**. Decisions run to 81. |
| `AIOM_Consolidated_Spec_v1.md`, `AIOM_Structure_v1.md`, `AIOM_Exit_Competencies_v1.md` | Specification, structure, the twenty-four competencies. |
| `AIOM_DESIGN_SPEC.md`, `AIOM_Design_QA_Spec_v1.md` | Design spec; gate spec. |
| `AIOM_Continuity_Ledger.md`, `AIOM_Claim_Ledger.md`, `AIOM_Source_Ledger.md` | G3 record; W14 record; sources. |
| `AIOM_Registry_Manifest.json`, `AIOM_Inherited_Vocabulary.md` | Pinned registry; generated vocabulary. |
| `AIOM_Case_Bank_v1.md`, `AIOM_Maturity_Model_v1.md`, `AIOM_Northmoor_Dataset_v1.md` | Cases; maturity stages; capstone data. |
| `Drafts/ChNN_<Name>/` | One per chapter plus `Case_Part_I` to `III`; live text in `00_Stage0_Draft/`; see `Drafts/README.md`. |
| `LESSONS.md` | The reasoning and incidents behind these rules. |
| `archive/` | Superseded files, including the full old HANDOFF and CLAUDE. |

When spec placeholders conflict with operative content, trust the operative
content. The `.docx` spec files are plain markdown: use `grep`, not `python-docx`.
Load the registry `.xlsx` with `openpyxl` and `data_only=True`. In CSS `content:`
strings use literal UTF-8, not hex escapes.

---

## 13. Session handoff protocol

`HANDOFF.md` is ONE PAGE of current state (Decision 80): branch, chapter, step,
what waits on Dan, the fix-between-chapters list, next action. A SessionStart hook
prints it.

1. **At the start of every session, read `HANDOFF.md`** alongside this file.
2. **Before ending a session, update it** from `git status` and
   `status_check.py`, not from the previous entry, and keep it under 150 lines.
3. **Keep the division clean.** A durable rule graduates into this file in one
   line, its story into `LESSONS.md`. A closed item is deleted from HANDOFF, not
   kept.
