# AI Operations Management: Textbook Workplan
Owner: Dan (Chorus AI Systems)
Last updated: 2026-08-02 (v5; currency sweep to Process v2 status)
Status legend: [x] done · [~] in progress · [ ] not started

---

## What changed in v5
v5 exists because seventeen rulings from the 2026-07-27 design session lived
only in a conversation. That was a single point of failure. This file absorbs
them.

Base: `AIOM_Workplan_v4.md`, carried forward in full. Nothing in v4 was found
to be wrong. Items were closed, not corrected.

Added or changed in v5:
1. **D0 is closed.** Design finalization is complete. Chapter locks are
   unblocked on the design side. CSS at v6.8, design spec at v6.8 plus three
   addenda.
2. **The chapter lifecycle is replaced.** v4's seven-stage lifecycle is
   superseded by the twelve-step process ruled on 2026-07-27, which separates
   gates from passes. See the reconstruction flag below.
3. **Decisions 29 through 41 recorded**, plus 40a. Decision 24 closed.
   Decisions 34 and 35 recorded as moot.
4. Chapter 1 status updated: renders complete at 18 pages, all ten QA gates
   passing. G1 had failed on source archiving only; Decision 48 later repealed
   the archival checks, so that blocker is retired.
5. Source handling recorded as built: one book-wide register, scripted capture,
   generated citations, Chicago 17 notes and bibliography.
6. Two manuscript fact corrections logged.
7. Restart procedure recorded, because the container does not persist.

Unchanged and still open: **Decision 28**, the Northmoor property gap.

Superseded: `AIOM_Workplan_v4.md`. Delete it. One live workplan at a time.

---

## Where we are (snapshot)
Pre-drafting closeout is complete (M2, CB2, M3 all done). Design finalization
is complete (D0 closed). The design system was tested on the three things it
had never been tested on: Figure 1.2 renders, the craft section typesets using
the model-answer treatment that section 7 of the spec predicted, and a
full-length chapter paginates without defect.

Chapter 1 was reopened at Stage 0 (2026-08-05, Decision 53), re-drafted against
the voice and craft standard, and reopened again at Stage 5 (2026-08-06,
Decision 56). It is now 6 of 13: Stage 0, G1, Stage 1, and Stage 2 all passed
2026-08-05, and Stages 3 and 4 passed 2026-08-06 and survive the second reopen.
Stage 5 and G2 had passed and are reset, because the theorem statement form
re-set THM-009 and the CSS moved to v6.8, so the design review ran against a
panel that no longer exists. The theorem's logic did not change, which is why
Stage 3 stands and the reopen point is Stage 5. The current render is 19 pages
and ALL FOURTEEN GATES PASS, with page 7 read at 150dpi; both manual production
checks owe a full-document pass in the re-run. Stage 5 and G2 are Claude's and
are the next work. The superseded Stage 5 and G2 between them found five tooling
defects and one new coverage gap, each of which had made a check report success
on a chapter that was not in the state the check described.

The editorial process now exists as a defined thing rather than an intention.

Chapter 2 drafting is unblocked and can run in parallel with Chapter 1's
editorial passes.

Dataset name: Northmoor is final (Decision 23). One open question on its
property coverage: see Decision 28.

---

## Milestone tracker

| ID | Milestone                          | Status | Blocks        |
|----|------------------------------------|--------|---------------|
| M1 | Consolidated Spec review           | [x]    | -             |
| M2 | Registry integration + validation  | [x]    | cleared       |
| CB2| Case-bank research pass 2          | [x]    | cleared       |
| M3 | Northmoor numerical build          | [x]    | cleared (see D28) |
| D0 | Design finalization (lock the system) | [x] | cleared       |
| D1 | Chapter drafts (Ch1 to Ch15)       | [~]    | -             |
| D2 | Front matter and appendices        | [ ]    | -             |
| P1 | Production, QA, delivery           | [ ]    | -             |

---

## Immediate queue (in order)
1. **Chapter 1 Stage 5 and G2, re-run.** Claude's steps, reset by the 2026-08-06
   reopen at Stage 5 (Decision 56). The design review must be performed against
   the re-set THM-009 panel and CSS v6.8, and G2's two MANUAL checks owe a
   full-document raster pass rather than the single page already read. Then Dan's
   Stages 6, 7, and 8, which may run in one sitting: copy edit, final fact check
   2, final read. Then G3 and Stage 9 lock, both Claude's. Note Stage 4 passed
   without its second-model gut-check, so the craft verdict and the baseline band
   the remaining chapters are read against are not independently verified, and
   Stage 7 is structurally external because no source host is reachable from a
   Claude session.
2. **Chapter 2 drafting.** Can run in parallel once the Chapter 1 re-draft has
   settled the craft standard in practice.
3. **Decision 28 ruling.** Northmoor properties G, H, I. Not urgent: it gates
   Ch9, Ch12, and Ch13 problem sets, not Ch2.

Closed since v5: the G1 contradiction on Chapter 1 (cleared 2026-07-29 after
Decision 48 repealed the archival checks) and source capture (retired by Decision
48; G1 dropped to ten checks, a source now needs a verified primary, an access
date, and two independent fact checks).

---

## Chapter lifecycle

The authoritative lifecycle is CLAUDE.md section 8 (Process v2, 2026-08-01): ten
stages (0 through 9) plus three gates, with the developmental edit at Stage 2,
the scoped re-run matrix, and the v1-to-v2 stage mapping. This file does not keep
a second copy; that duplication is what drifts. Status is single-sourced in each
chapter's checklist and printed by `status_check.py`.

Chapter 1 was reopened at Stage 0 (2026-08-05, Decision 53) and again at Stage 5
(2026-08-06, Decision 56); 6 of the thirteen steps are passed. `reopen.py`
performed both resets, archiving each step's findings in place rather than
destroying them. Stage folders across all eighteen units were migrated to
Process v2 numbering on 2026-08-05, so a folder name no longer disagrees with
the live process.

- Copy-edit placement is revisited at Chapter 4 (Decision 24). If line edits are
  being churned by structural changes, move it earlier then, not before.
- Fifteen self-contained checklists exist, one per chapter (Decision 32).
- No process document and no book-wide rollup (Decision 32).
- Chapter 1 is not Locked until every step above is complete.
- **Chapter 1's live text is
  `Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`.** A
  superseded fork, `06_Stage5_Design_Review/AIOM_Ch01_Stage4_FINAL.html`, is still
  in the tree and has diverged by roughly 150 lines. Decision 56 was applied to
  the fork first and had to be reverted and re-applied. "One live text per
  chapter, supersede and delete, never fork" is the standing rule; the delete has
  not happened and is Dan's call.

---

## Per-chapter status

Decision 32 rules out a rollup, so this is a status line per chapter rather
than a twelve-column grid. The detail lives in each chapter's own checklist.
If a twelve-column grid in this file would read as the forbidden rollup, say so
and it comes out.

| Ch  | Title                          | Step reached | Notes |
|-----|--------------------------------|--------------|-------|
| 1   | The Category Error             | Stage 5 next | Reopened at Stage 0 on 2026-08-05 (Decision 53) and re-drafted the same day against the craft standard, then reopened again at Stage 5 on 2026-08-06 (Decision 56). Now 6 of 13: Stages 0 to 2 and G1 passed 2026-08-05; Stages 3 and 4 passed 2026-08-06 and survive the second reopen. Stage 5 and G2 had passed and are reset, because the theorem statement form changed THM-009 and the CSS moved to v6.8, so the design review ran on a panel that no longer exists. The theorem logic is unchanged, so Stage 3 stands. Current render is 19 pages with all fourteen gates passing and page 7 read at 150dpi; both MANUAL checks still owe a full-document pass. Earlier record: Stage 3 ran two independent external checks which agreed on one finding of six. Stage 4 resolved all seven carried craft findings and raised six new, five applied, but passed without its second-model gut-check. The superseded Stage 5 closed CD6 and found CD7 was never real; the superseded G2 found the box list stale, fixed a craft-section labelling inconsistency, and opened gap G-I. Next: Claude re-runs Stage 5 and G2, then Dan takes Stages 6, 7, 8. |
| 2   | The Flow                       | not started  | Unblocked. Next to draft. |
| 3   | A Science and Its Discipline   | not started  | Build the THM-004 trace. |
| 4   | The Playing Field              | not started  | Decision 24 revisited here. |
| 5   | The Anatomy of Cost            | not started  | |
| 6   | The Nature of Value            | not started  | CB2 value statements ready. |
| 7   | Sourcing                       | not started  | |
| 8   | Metering                       | not started  | |
| 9   | Attribution                    | not started  | See Decision 28. |
| 10  | Planning and Budgeting         | not started  | |
| 11  | Allocation and Routing         | not started  | |
| 12  | The Value Boundary             | not started  | See Decision 28. |
| 13  | Diagnosis and Maturity         | not started  | T0 packet ready. See Decision 28. |
| 14  | The Organized Buyer            | not started  | CB2 FinOps data ready. |
| 15  | Standing Up the Discipline     | not started  | Final exam. |

Cumulative cases (Part I, II, III) run the same lifecycle when drafted.

---

## Decisions log

Decisions 1 through 21 live in the Consolidated Spec and its Addendum.
Decisions 22 onward live here.

- **Decision 22.** Founding Questions canonical wording: Section 6 wording,
  leading "And" dropped from Q5. Five questions locked. (A parallel session
  labeled this same ruling "Option B"; the substance is identical. Decision 22
  is the canonical label.)
- **Decision 23.** Northmoor confirmed as the final dataset name.
- **Decision 24. RULED.** Copy edit sits late, at stage 5, after voice and
  design. Revisit at Chapter 4. Rationale: line edits are not churned by
  structural changes.
- **Decision 25.** The axiom layer. The book describes the definition and axiom
  layers accurately in Chapter 3 and reproduces down to the proposition layer
  only. The axiom source files are not loaded into the project. Chapter 3's
  trace set piece terminates at proposition nodes with a pointer to the fuller
  apparatus.
- **Decision 26.** Founding Question numbering. Manifesto numbering is
  retained. Part III resolves the questions out of numerical order (1, 3, 3, 2,
  4, 5 across Ch7 to Ch12), taught as a feature in the Part III introduction.
  Renumbering was rejected.
- **Decision 27.** The nine unassigned lemmas are assigned as prose-level
  grounding, cited by ID where they carry the argument. Tier architecture
  unchanged: theorems remain the only chapter-anchoring callouts, eight,
  one-to-one. Ch9, Ch10, and Ch11 gain formal grounding they previously lacked.
- **Decision 28. OPEN.** Northmoor property coverage. Decision 18 in the
  Specification Addendum extended the property list from A-through-F to
  A-through-I, adding property G (an unreconcilable invoice residual within a
  seeded band), property H (a workflow whose value column is structurally
  absent), and property I (a disputed attribution basis where two bases each
  survive challenge). The M3 build asserts A through F only. Options: (a) extend
  the generator and answer keys to G, H, I; (b) implement G, H, I as authored
  artifacts outside the generator; (c) amend Decision 18. Recommendation:
  option (a) or (b), because G, H, and I are the properties whose answer keys
  grade reasoning rather than answer-matching, and they feed Ch9, Ch12, and
  Ch13. Awaiting ruling. Carried open since v4.
- **Decision 29.** Content review is its own pass, at stage 1. It is not folded
  into the fact check.
- **Decision 30.** A final read of the rendered chapter, judged pass or fail on
  the whole rather than line by line.
- **Decision 31.** A running continuity ledger is maintained across chapters and
  checked at G3.
- **Decision 32. AMENDED.** Per-chapter checklist only. No process document and
  no book-wide rollup.
- **Decision 33.** Word bands are set. Chapters 1 and 2 run 5,000 to 6,000
  words.
- **Decision 34. MOOT.** Margins were already correct. No change.
- **Decision 35. MOOT.** The theorem panel is a block, so `break-inside: avoid`
  holds it. No workaround needed.
- **Decision 36.** Draft v2 is authoritative over proof v14. Two divergent texts
  is the failure mode to avoid; delete the loser.
- **Decision 37.** Figure fills use `--tint-fig`. Figures never use apparatus
  tints.
- **Decision 38.** The chapter source register is classed as apparatus, not a
  seventh slot. The six-slot skeleton is intact.
- **Decision 39.** Chicago 17, notes and bibliography, with access dates.
- **Decision 40.** Source standard: upgrade to the most durable primary; a
  social-post-only claim gets a second independent path. The source-upgrade half
  survives; the archival-capture half is repealed by Decision 48.
- **Decision 40a.** Perma.cc is out. Moot under Decision 48, which drops capture
  entirely.
- **Decision 41.** One book-wide source register, generated citations. The
  scripted-capture step is retired by Decision 48.
- **Decision 48 (2026-07-29).** No capture. A source is sufficiently sourced when
  cited to a verified primary, checked live on the access date, and cleared by
  two independent fact checks. Repeals the archival capture of Decisions 39, 40,
  and 40a; the Decision 40 source-upgrade standard survives. Gate G1 drops from
  fourteen checks to ten.

- **Decision 42.** Voiced material. Body prose is third person. First or second
  person is permitted only in material marked as voiced, either by a block class
  (`model`, `dq`, `problem`) or by enclosing quotation marks. Ruled at Ch1
  Stage 3.
- **Decision 43.** Reader address. Second person is permitted in discussion
  questions and problems. "The reader" holds everywhere else.
- **Decision 44.** Definition restatement. A definition given in a definition
  aside is not restated verbatim in body prose. The body names the term instead.
- **Decision 45.** Token gloss. "Token" carries a short appositive gloss at
  first substantive use in Ch1 section 1.2. Revisit when the preface
  reader-assumptions subsection is written.

- **Decision 46.** Microsoft's IR transcript is accepted as the primary source
  for the GitHub Copilot subscriber figure. A filing upgrade is not available:
  the figure appears only in spoken remarks, the earnings press release carries
  no subscriber count, and Microsoft does not break out product-level
  subscriber counts in the 10-Q. Standing principle: a first-party disclosure
  published by the party that holds the data is a primary source, and where no
  filing carries it, capture governs durability rather than a stronger form.

- **Decision 52. RULED 2026-08-05.** The voice standard gains a positive half.
  `AIOM_Voice_and_Craft_v1.md` extracts four transferable techniques from named
  exemplars (the concrete particular from Michael Lewis, context and stakes from
  James Lardner, sentence economy from the Financial Times, paragraph
  architecture from The New Yorker), carries an explicit guard against the
  registers those exemplars arrive with, and reduces to six criteria C1 through
  C6. Enforcement is four-layered, all four ruled together: the criteria are
  sub-checkboxes under Stage 4 so `status_check.py` fails a Stage 4 marked passed
  with one left open; the standard binds from Stage 0 at drafting time, with a
  Stage 0 acknowledgment box; `voicecheck.py` prints advisory craft metrics
  proxying C1, C3, C4, and C5, permanently advisory and never a threshold; and
  worked before-and-after exemplars are carried in the standard file, drawn from
  Chapter 1. Stage 4 is renamed the voice and craft check. Rationale: the
  standing rules were entirely prohibitive, and prose can break none of them and
  still be dead on the page. C2 and C6 have no mechanical proxy and are enforced
  by reading alone, which is stated rather than papered over.

- **Decision 53. RULED 2026-08-05.** Chapter 1 is reopened at Stage 0 and fully
  re-drafted, rather than patched, because it was drafted before the craft
  standard existed and is the exemplar fourteen further chapters are drafted
  against. The re-draft is also the proving run for Process v2 end to end.
  Supporting process, built the same day: `reopen.py`, so a reopen resets steps
  and archives findings instead of destroying them; the Process v1 to v2
  stage-folder migration across all eighteen units; gates 12, 13, and 14 in
  AIOM_build.py, closing the three checks the G2 checklist had claimed for
  months while performing none of them; a toolchain preflight and pinned
  requirements.txt, since a gate that did not run is not a gate that passed; and
  a G2 checklist mirroring the fourteen printed gates one for one, with the two
  genuinely manual checks labelled manual. Gate 14 found a real defect on its
  first run that the eleven-gate suite had passed.

- **Decision 54. BUILT 2026-08-05.** The continuity ledger exists:
  `AIOM_Continuity_Ledger.md` as the record and `continuity.py` as gate G3, with
  all seven checks the checklist names. The ledger carries terms owned per
  chapter, forward references and whether paid, registry glosses, Northmoor
  figures, and the canonical Founding Questions and maturity stages parsed from
  the ledger itself rather than hard-coded. Policy: entries are appended at
  Stage 9 on lock, never at draft time; the ledger is the authority and is never
  edited to make a gate pass; registry glosses are written by hand, and the
  placeholder fails the gate deliberately. Verified end to end against the
  superseded Chapter 1 render. Lock is no longer blocked for any chapter.

- **Decision 55. RULED 2026-08-05, Chapter 1 Stage 1.** Seven structural
  findings ruled, four of which amend the Consolidated Spec's Ch1 outline rather
  than the chapter. (S1) The case bank held no CASE 4.6 and no CASE 6.4 although
  the spec assigned both to Ch1; both are now written into AIOM_Case_Bank_v1.md
  from sources already cleared through the Ch1 register, with provenance lines
  saying so and no new research. CASE 6.4 carries the QJE figure discipline and
  the 2026-07-29 stipulation ruling, so a later chapter meets both rules from the
  bank. (S2) Figure numbering stands as the chapter has it, anatomy at 1.1, and
  the spec is amended. (S3) The opening case closes on the category error stated
  rather than the spec's question, since the standing rule forbids rhetorical
  questions in body prose; general principle ruled, whatever is more effective
  inside the chapter wins on educational and style grounds. (S4) A fourth
  discussion question is accepted, added to answer craft finding F7. (S5) P2 no
  longer needs a CITED deployment: the evidence policy governs empirical claims,
  not exercise scaffolding. (S6) FinOps stays out of Ch1; Ch14 owns the named
  engagement. (S7) The 2026-07-29 agent-count ruling stands unchanged. No word of
  the chapter changed, so no downstream step was invalidated.

- **Decision 56. RULED 2026-08-06.** Theorem statement form. A registry
  conditional carrying more than two antecedents is set as a structured
  conditional in the panel, never as running prose: scope boundary first, before
  the word "if"; antecedents enumerated in lower-case roman, one per line,
  semicolon-closed, "and" before the last; consequent on its own line opening
  with "then" and carrying the registry's negation. Antecedents are set in
  parallel grammar and full English, so elided articles are restored and a
  dangling disjunct is attached to the noun it modifies. The logic is untouchable:
  no antecedent may be added, dropped, merged, split, weakened, or strengthened,
  and the consequent may not be restated in the chapter's vocabulary. The registry
  statement is the authority, the panel is a faithful rendering, and the ID in the
  panel label is what a reader follows to the verbatim form. Rationale: THM-009 as
  drafted was a single sixty-word sentence with four conjoined antecedents and its
  scope clause trailing the negation, so the reader had to finish the statement and
  then retroactively re-scope it. The form is ruled now, at one theorem, rather than
  after the remaining seven are set. Spec: AIOM_DESIGN_SPEC.md section 5. CSS to
  v6.8: `.theorem .cond`, `ol.ante`, `li .mk`, `.conseq`. The dependency chain stays
  out of the panel, because Chapter 3 owns the trace set piece.

- **Decision 56a. RULED 2026-08-06.** `.slot-label` gains `break-after: avoid`.
  `h3.section` and `.problems-sec .slot-label` already carried the rule and the
  base slot label did not, which is why the craft-section label could strand at a
  page foot. It stranded once at Ch1 gate 14's first run, was cleared by cutting
  two sentences of prose at Stage 4, and returned the moment the theorem panel
  changed height. A defect whose only remedy is shaving prose until the page breaks
  elsewhere is a CSS defect, not a prose defect. Ch1 now reports zero stranded heads
  with the prose untouched.

Also settled, not numbered: theorem panels are labeled "Theorem n" while prose
cites registry IDs.

---

## Design system of record (D0 closed)

State: CSS at v6.8. Design spec at v6.8 plus three addenda.

What D0 proved, being the three things the system had never been tested on:
1. Figure 1.2 renders.
2. The craft section typesets using the model-answer treatment, as section 7 of
   the spec predicted.
3. A full-length chapter paginates without defect.

Standing design rules carried out of D0:
- `--tint-fig` for figure fills. Figures never use apparatus tints
  (Decision 37).
- The chapter source register is apparatus, not a slot (Decision 38).
- Theorem panels are labeled "Theorem n"; prose cites registry IDs.
- Margins are as specified; the earlier concern was unfounded (Decision 34).
- The theorem panel is a block and `break-inside: avoid` holds it
  (Decision 35). This does not generalize: WeasyPrint 69 still ignores
  `break-inside: avoid` on floated elements, which is what `place.py` exists
  for.

---

## Source apparatus (built)

- One book-wide source register: `AIOM_sources.json`.
- Citations are generated, not hand-written.
- Capture: retired by Decision 48. No snapshots are filed.
- Style: Chicago 17, notes and bibliography, with access dates (Decision 39).
- Archival standard: repealed by Decision 48. A source is sufficiently sourced
  when cited to a verified primary with an access date and cleared by two
  independent fact checks. The capture requirement of Decisions 40 and 40a is
  withdrawn; the Decision 40 source-upgrade standard survives.

Chapter 1 source state (resolved 2026-07-29, G1 cleared):
- The register carries nine sources, each cited to a verified primary and checked
  live on its access date.
- The three upgrades are done: the Microsoft 4.7 million figure is sourced to the
  FY26 Q2 earnings call (Decision 46, no filing carries it), the GitHub claim to
  the dated changelog entry, and the Altman post carries a second independent path.
- Capture is retired (Decision 48), so no snapshots are filed.

---

## Manuscript corrections of record

Logged so they are not silently reintroduced by a later edit.

1. **Cursor repricing.** Previously attributed to heavy-user cost. Truell's
   stated reason was rising tokens per request on long-horizon tasks.
   Corrected.
2. **The 4.7 million figure.** Previously attributed to GitHub. It is a
   Microsoft disclosure. Corrected.
3. Dates pinned throughout Chapter 1.

---

## Decision 27 assignments (reference)
| Lemma | Chapter gained | What it grounds |
|-------|----------------|-----------------|
| LEM-011 | Ch9 | Recorded token activity becomes measurable usage |
| LEM-001 | Ch10 | Usage growth increases cost exposure |
| LEM-003, LEM-004 | Ch11 | Rule-based differentiated treatment; capacity constraints require allocation |
| LEM-010 | Ch7 | Model substitution constrained by adequacy and switching cost |
| LEM-018 | Ch5 | Pilot cost structure is not deployment cost structure |
| LEM-013 | Ch4 | Deployment architecture influences economics |
| LEM-014 | Ch5, Ch7 | Resource requirement differences produce cost-exposure differences |
| LEM-005 | Ch2 | Production is operated, not merely accessed |
| LEM-017 | Ch7, Ch12 | Workflow integration creates scoped operational dependency |

---

## Canonical Founding Questions (locked, Decision 22)

| # | Question | Function | Answered in | Maturity stage |
|---|----------|----------|-------------|----------------|
| 1 | Are you paying for capability you do not need, or starving work that needs more? | Sourcing | Ch7 | Governed |
| 2 | What do you expect the AI flow to consume next period, and how will you know when it deviates? | Planning and budgeting | Ch10 | Governed |
| 3 | Who consumed what last month, in service of which work? | Metering and attribution | Ch8, Ch9 | Visible, then Attributed |
| 4 | When capacity is constrained, who decides what runs first, and by what rule? | Allocation | Ch11 | Governed |
| 5 | Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing? | Value boundary | Ch12 | Accountable |

Structural device: posed at the end of Ch3, resolved once each across Ch7 to
Ch12, instrumentalized as the diagnostic in Ch13, re-asked as the ninety-day
plan's targets in Ch15.

---

## Registry facts of record (verified against Registry v1.3)

- 228 objects: 200 propositions, 20 lemmas, 8 theorems.
- All eight book-mapped theorem IDs resolve. One-to-one, no orphans, no gaps.
- Appendix A scope confirmed at 28 objects.
- Dependency graph integrity verified: every internal proposition and lemma
  reference resolves. Zero dangling references.
- Keystones: **LEM-006** (buyer total cost extends beyond access price)
  underpins six theorems; **LEM-021** (ROI evaluation requires measurement
  boundary) and **LEM-002** (measurement enables visibility) underpin five each.
  These three carry the most structural load in the book.
- **LEM-015 does not exist.** IDs run LEM-001 to LEM-021 with 015 absent.
  Nothing references it. Retired, not lost.
- Axioms AX-001 to AX-035 (34 distinct) are cited as dependencies but live in
  separate canonical source files, per the workbook's own reader guide.
  Boundary set by Decision 25.
- **11 of 20 lemmas have no registry plain statement**, only a formal
  statement: LEM-002, 004, 006, 007, 008, 009, 012, 016, 019, 020, 021.
  Appendix A's verbatim reproduction is safe because all 28 have formal
  statements. Prose citation of these 11 requires a plain-language gloss
  written at drafting and marked as book-authored, not registry text.
- The workbook ships a worked recursive trace for THM-005 (`02_TRACE_EXAMPLE`),
  which is a Ch6 asset. The Ch3 trace set piece uses THM-004 and must be built
  separately. Traces for any theorem can be generated mechanically from the
  dependency graph, so Figure 3.1 is buildable from data.
- Registry grounding reaches Ch1 through Ch13 after Decision 27. Ch14 and Ch15
  carry none by design: both are Part IV institutional chapters that reprise
  established claims rather than establish new ones. Record in the method note
  so it reads as decided rather than overlooked.

Reference artifact: `AIOM_Validation_Matrix_v1.xlsx` (28 rows; exact statement,
scope conditions, dependent chapters and figures, revision trigger, plus a
Legend sheet). Working artifact only. Never book content. Keep in Drive and in
project knowledge; the Decision 27 assignments exist nowhere else.

---

## Phase 0: Foundation (DONE)
- [x] Stage 1: exit competencies (24) locked
- [x] Stage 2: course architecture locked
- [x] Stage 3: chapter structure locked (15 chapters, 4 parts)
- [x] Theorem map (8 theorems, one-to-one) locked
- [x] Coverage map (all 24 competencies placed)
- [x] Maturity model designed (Unmanaged, Visible, Attributed, Governed, Accountable)
- [x] Northmoor dataset design locked (one company, two moments)
- [x] Chapter-level outlines for all 15 chapters (Consolidated Spec, Part D)
- [x] Case bank pass 1 complete
- [x] Consolidated Spec v1.0 compiled
- [x] Addendum v1.0 ruled (M1 closed)

---

## Phase 1: Pre-drafting closeout (COMPLETE)

### M2: Registry integration + validation matrix [x]
- [x] Load founding paper and Registry v1.3 into the project
- [x] Fill the REGISTRY PULL items (Founding Questions exact wording; Decision 22)
- [x] Build validation matrix: all 28 Appendix A objects traced to ID
- [x] Confirm Appendix A scope (the 28 theorems and lemmas, verbatim)

Registry flags to carry into the Appendix A build (Phase 3):
- LEM-015 is absent from the ID sequence; skip it explicitly.
- The "20 lemmas" count is correct as an object count, but IDs run to LEM-021.
- The registry ships a worked trace for THM-005 (Ch6 asset), not THM-004 (Ch3
  trace set piece per Decision 3); the THM-004 trace must be built separately.

Documentation follow-ups (not blocking):
- [ ] Replace Consolidated Spec section B.5's placeholder gloss with the
      canonical five-question table above. The placeholder had Questions 2 and
      3 swapped relative to the manifesto.
- [ ] Mark the Part H `[REGISTRY PULL]` open items resolved.
- [ ] Upload `AIOM_Validation_Matrix_v1.xlsx` to project knowledge.

### CB2: Case-bank research pass 2 [x]
- [x] Six more classifiable value statements for the Ch6 sort-and-repair set
- [x] Positive value case with real boundaries (Brynjolfsson, Li, Raymond QJE
  2025; METR developer RCT arc as counterweight)
- [x] Opening cases for chapters that were missing one
- [x] FinOps Foundation framework text + State of FinOps 2026
- [x] Token-price volatility corrected (same-model cross-provider ~3x to 4x;
  cross-model spread is the 10x to 50x figure; keep separate in Ch2 and Ch5)
- [x] Model deprecation and forced-migration episodes (Ch7 switching
  economics). Now also formally grounded by LEM-010 per Decision 27.
- [~] Northmoor trade-name check (disclaimer written; collision check is a
  pre-print gate, not a drafting gate)

### M3: Northmoor numerical build [x]
- [x] Confirm final dataset name (Northmoor; Decision 23)
- [x] Seeded Python generator (properties A to F asserted; all pass)
- [x] Emit outputs (raw events, half-cleaned export, budget/actuals, task-class
  and tier tables plus scenarios, capstone netting, T0 diagnostic packet, keys)
- [x] Construction note written
- [ ] **Properties G, H, I per Decision 18. See open Decision 28.**

Gate cleared: Part III (Ch7 to Ch12), Ch13, and Ch15 are unblocked for
drafting. Decision 28 affects Ch9, Ch12, and Ch13 problem sets specifically.

---

## Phase 2: Drafting

### D0: Design finalization [x] CLOSED 2026-07-28
- [x] Review the Ch1 design proof and list what to change
- [x] Rule each open design question (one at a time, per protocol)
- [x] Rebuild the affected assets (CSS, figure templates, running heads)
- [x] Re-render Ch1 as the confirmed design proof
- [x] Lock the design system; record the decision

### Drafting (chapter by chapter)
Protocol: one editorial decision at a time, ruled before proceeding. Every
chapter uses the fixed six-slot skeleton, no exceptions, and runs the full
lifecycle above. Per-chapter registry grounding is in the validation matrix.
Word band: 5,000 to 6,000 for Ch1 and Ch2 (Decision 33).
- [~] Ch1  The Category Error        (renders at 19 pages; through G2, Dan's Stage 6 to 8 remain)
- [ ] Ch2  The Flow                  (next; unblocked)
- [ ] Ch3  A Science and Its Discipline   (M2 ready; build THM-004 trace)
- [ ] Part I cumulative case
- [ ] Ch4  The Playing Field          (revisit Decision 24 here)
- [ ] Ch5  The Anatomy of Cost
- [ ] Ch6  The Nature of Value        (CB2 value statements ready)
- [ ] Part II cumulative case
- [ ] Ch7  Sourcing                   (M3 ready)
- [ ] Ch8  Metering                   (M3 ready)
- [ ] Ch9  Attribution                (M3 ready; see Decision 28)
- [ ] Ch10 Planning and Budgeting     (M3 ready)
- [ ] Ch11 Allocation and Routing     (M3 ready)
- [ ] Ch12 The Value Boundary         (M3 ready; see Decision 28)
- [ ] Part III cumulative case
- [ ] Ch13 Diagnosis and Maturity     (M3 diagnostic packet ready; see D28)
- [ ] Ch14 The Organized Buyer        (CB2 FinOps data ready)
- [ ] Ch15 Standing Up the Discipline (final exam; M3 ready)

Standing drafting tasks:
- [ ] Write plain-language glosses for the 11 lemmas lacking them, at the
      chapter where each is first cited. Mark every gloss as book-authored,
      never as registry text.
- [ ] Maintain the continuity ledger across chapters (Decision 31).

---

## Phase 3: Front and back matter
- [ ] Appendix A: 28 theorems and lemmas, verbatim (skip LEM-015, IDs run to
  LEM-021, build the THM-004 trace separately)
- [ ] Glossary (aggregated key terms from all chapters)
- [ ] Method note (include: LEM-015 retirement; the 20-lemma count against a
  21-wide ID range; the axiom-layer boundary per Decision 25; Ch14 and Ch15
  carrying no registry grounding by design)
- [ ] Index
- [ ] Bibliography, generated from the source register (Decisions 39 and 41)
- [ ] Front matter (title, preface, founding-document framing, 14-week course map)

Front and back matter clear the same lifecycle where a fact check applies
(Appendix A, method note, glossary).

---

## Phase 4: Production, QA, delivery
- [x] Render pipeline built (WeasyPrint, AIOM_book.css, AIOM_build.py, place.py
  for callout placement, fourteen-check QA suite, toolchain preflight)
- [x] Design system locked (D0)
- [ ] Validate all figures before render
- [ ] Programmatic QA (pdfplumber overflow and header checks; zero em dashes)
- [ ] Rasterized visual QA (pdf2image pixel sampling)
- [ ] Northmoor trade-name collision check (pre-print gate)
- [ ] Final PDF delivery to /mnt/user-data/outputs/

---

## Working files and restart procedure

The repository is version-controlled and is the source of truth. Work is
committed and pushed to the working branch each session, with `main` kept in
sync; nothing is downloaded or re-uploaded by hand. A fresh session clones the
repo, so the file set is already present.

Build environment and commands live in CLAUDE.md section 5; the perishable
per-session state (active branch, what is pushed, and the standing environment
reminders) lives in HANDOFF.md. This file keeps no second copy of either, since
duplication is what drifts. In particular: the fonts are committed under
`fonts/`, so `AIOM_build.py --fonts` is not run; poppler-utils installs per
session for gate 9; and a chapter builds from a repo-root copy of its stage HTML
because of the CSS-adjacency wrinkle.

File handling rules:
- The chapter HTML is the single source of truth (Decision 50). Edit it directly;
  the built HTML and PDF are generated. Do not write chapter prose to markdown,
  and never fork a chapter into a second live text. Two divergent texts is the
  exact failure the v14 episode produced.

---

## Standing rules (do not violate)
- No em dashes anywhere. Rewrite with commas, colons, periods, parentheses.
- Every empirical claim cited or cut.
- The six craft criteria in AIOM_Voice_and_Craft_v1.md bind from Stage 0, at
  drafting time, and are verified at Stage 4. Read the file before drafting.
- Fixed six-slot skeleton in all 15 chapters, no exceptions. The source
  register is apparatus, not a slot.
- Registry justifies the book; it does not organize it.
- Theorems are the only chapter-anchoring callouts. Eight, one-to-one.
  Lemmas are prose-cited by ID. Propositions are cited by ID only.
- Theorem statement form (Decision 56): more than two antecedents means scope
  first, antecedents enumerated, consequent on its own line. Render the registry
  into readable English; never change its logic.
- No chapter is Locked until it clears the full lifecycle.
- One live workplan at a time. Supersede and delete; never fork.
- One live text per chapter. Supersede and delete; never fork.
- Verify currency before reporting. A file in front of you is not necessarily
  the current file. Check the version before drawing a conclusion from it.

END OF WORKPLAN v5.
