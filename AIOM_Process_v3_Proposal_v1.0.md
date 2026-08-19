> **STATUS: PROPOSED, NOT ADOPTED. AWAITING DAN'S RULING.**
>
> If ruled in, this becomes **Decision 68** in `AIOM_Workplan_v5.md`, which is the
> decision-numbering authority, and Process v2 becomes Process v3. Nothing in this
> file binds until that ruling. It is filed at the repository root rather than in
> `archive/` because it is a live proposal awaiting a decision, and the banner
> above is what stops a root file reading as adopted.

# Process v3: the production-side steps run on frozen text

Author: Claude, 2026-08-19. Raised after Dan observed that Chapter 1 spent most of
its elapsed time in checks rather than in drafting and design.

---

## 1. The finding

Dan's observation is correct about the ratio and wrong about the cause. The cost
was not in running the gates. It was in re-running the human steps behind them,
and the re-runs were scheduled by the step order rather than caused by bad luck.

Measured on Chapter 1, from the repository rather than from memory:

| Measure | Number |
|---|---|
| Commits total | 231 |
| Commits touching the live chapter text | 47 |
| Commits touching tooling (`.py`) | 60 |
| Commits touching records and checklists | 186 |
| Words of chapter (Decision 33 measure, per `status_check.py`) | 7,069 |
| Words of record in the chapter checklist | 51,374 |
| Record-to-chapter ratio | 7.3 to 1 |
| Findings raised (DE, SF, FC, CE, PG, DR) | 55 |
| Reopens | 8 |
| Lines of checklist owned by Stage 6 alone | 1,006 |

The mechanical suite is not the expense. CLAUDE.md section 8 puts the whole
amendment-path suite, which is W14 plus `voicecheck` mechanical plus the print
render with fifteen gates plus the web build with seventeen, at thirty to
forty-five seconds. That figure is the repository's and was not re-measured here,
because this container has no print toolchain installed.

## 2. The defect, stated precisely

**Gate G2, the most expensive step in the process, runs at position 8 of 13, and
three text-changing steps are scheduled after it.**

Stage 6 copy edit, Stage 7 final fact check 2, and any ruling that follows either
one all move the rendered text. The scoped re-run matrix then correctly sends the
chapter back through G2. That is not a failure of the matrix. The matrix is
working exactly as designed, repairing a sequencing problem that the step order
creates on every chapter.

G2 costs what it costs because sixteen of its eighteen boxes are mechanical and
two are marked MANUAL: figure geometry read against a raster by eye, and a
rasterized page-level visual review. Gaps G-I and G-II add more reading, because
both require a chapter whose pagination or callout placement moves to be read
rather than merely gated. Every reopen of G2 re-incurred all of that.

## 3. What it cost on Chapter 1

All eight reopens, classified by cause:

| # | Date | Reset from | Cause | Class |
|---|---|---|---|---|
| 1 | 2026-08-05 | Stage 0 | Chapter drafted before the craft standard existed | One-time, cannot recur |
| 2 | 2026-08-06 | Stage 5 | Decision 56, theorem form, CSS v6.8 | Design-system churn |
| 3 | 2026-08-07 | Stage 5 | Decision 57, DR2 and DR3, CSS v6.9 | Design-system churn |
| 4 | 2026-08-08 | Stage 2 | Copy edit rounds 1 to 3 rewrote the chapter | **Late text change** |
| 5 | 2026-08-11 | Gate G2 | FC2 to FC5 from external check 1 | **Late text change** |
| 6 | 2026-08-12 | Gate G2 | Copy edits CE3 to CE6 applied after G2 passed | **Late text change** |
| 7 | 2026-08-12 | Gate G2 | FC8 and FC9 from external check 2 | **Late text change** |
| 8 | 2026-08-13 | Gate G2 | Citation format change in shared tooling | **Late text change** |

Reopen 1 is unrepeatable: Chapter 2 drafts under a standard that now exists.
Reopens 2 and 3 were design-system churn, and the system has been locked at v7.1
since. **Reopens 4 through 8 are one defect occurring five times, and every one of
them re-ran G2.**

The Stage 6 evidence is the sharpest form of it. Decision 24 places the copy edit
late so that it runs on prose that has stopped moving. On Chapter 1, round 1 alone
changed 59 of 155 blocks, grew body prose by 25 per cent, and took the chapter
from 20 pages to 26. The copy edit was not running on prose that had stopped
moving. It was the thing that moved it.

## 4. Options

**Option A. No change.** Accept the rework and rely on the re-run matrix.
Honest, and it is what Chapter 1 did. It books five reopens per chapter across
fourteen remaining chapters as the expected cost of the design.

**Option B. Move Gate G2 to after Stage 7.** The minimal reorder. Production
becomes the last gate before G3, so it runs once on text nothing further will
move. This eliminates reopens 5 through 8 outright and the G2 portion of reopen 4.

**Option C. Move Stage 5 and Gate G2 to after Stage 7.** Option B, plus the design
review, on the reasoning that both are reads of a rendered page and both are
invalidated by exactly the same event. **Recommended, for the reasons in section
5.**

**Option D. Move the Stage 6 copy edit earlier instead, ahead of Stage 5.**
Rejected. It puts the copy edit ahead of both fact checks, which are the other
source of late text change, so it fixes one of the two inputs. It also reorders a
stage rather than a gate, which forces stage renumbering and a v2-to-v3 mapping
table for reading dated records. Process v2 already paid that price once and
CLAUDE.md section 8 still carries the mapping.

**Option E. Absorb late findings through `amend.py` after lock.** Rejected as a
substitute, correct as what it already is. The amendment path exists for
post-lock author edits, where Dan's edit is approved by definition. A Stage 7
fact-check finding is a lifecycle step, not an author edit, and routing it through
an amendment would mean locking a chapter whose final fact check had never been
verified against a render.

## 5. Recommendation: Option C

Move Stage 5 and Gate G2 to sit after Stage 7. Recommended over Option B on the
Chapter 1 evidence about what Stage 5 findings actually are.

**Every Stage 5 finding on Chapter 1 was fixed in CSS or in markup, and not one of
them was fixed by rewriting a sentence.** The Stage 5 pass in force, dated
2026-08-10, raised exactly two findings, DR6 and DR7, both line-end breaks falling
inside proper nouns, one of them across the page 11 to 12 turn, and both were
ruled as Decision 58, the `.nb` class. The superseded run before it raised a
stranded craft head group, model-answer paragraphs running together, and a
one-row table spill, which became Decision 56a and CSS v6.9. Two further findings
under that run turned out to be a phantom produced by a defect in gate 14 and
three defects in `place.py`, which are tooling rather than chapter defects.

Note that the DR numbering was reused across the two runs, so these are cited by
what they were rather than by a count.

CLAUDE.md already rules the consequence: "Rewording is not a fix for a break. A
break is a property of the measure, not of the sentence, so it returns at the next
reflow." A design review performed before the copy edit is therefore reading a
pagination that the copy edit is about to destroy. That is the same defect as
running G2 early, and it should be fixed in the same move rather than left to be
rediscovered on Chapter 3.

## 6. The step table, before and after

Process v2, in force today:

| Pos | Step | Name | Owner |
|---|---|---|---|
| 1 | Stage 0 | Draft | C |
| 2 | G1 | Structural gate | C |
| 3 | Stage 1 | Content review | D |
| 4 | Stage 2 | Developmental edit | C |
| 5 | Stage 3 | Source and fact check 1 | D |
| 6 | Stage 4 | Voice and craft check | C |
| 7 | **Stage 5** | **Design review** | C |
| 8 | **G2** | **Production gate** | C |
| 9 | Stage 6 | Copy edit | D |
| 10 | Stage 7 | Final fact check 2 | D |
| 11 | G3 | Continuity gate | C |
| 12 | Stage 8 | Final read | D |
| 13 | Stage 9 | Locked | C |

Process v3, proposed:

| Pos | Step | Name | Owner |
|---|---|---|---|
| 1 | Stage 0 | Draft | C |
| 2 | G1 | Structural gate | C |
| 3 | Stage 1 | Content review | D |
| 4 | Stage 2 | Developmental edit | C |
| 5 | Stage 3 | Source and fact check 1 | D |
| 6 | Stage 4 | Voice and craft check | C |
| 7 | Stage 6 | Copy edit | D |
| 8 | Stage 7 | Final fact check 2 | D |
| 9 | **Stage 5** | **Design review** | C |
| 10 | **G2** | **Production gate** | C |
| 11 | G3 | Continuity gate | C |
| 12 | Stage 8 | Final read | D |
| 13 | Stage 9 | Locked | C |

The three gates now sit where each can be run once: G1 before Dan reads anything,
G2 and G3 after the text has stopped moving, and Stage 8 is Dan's final read of a
chapter that every check has already cleared.

## 7. What does NOT change, and this is the point

**No stage is renamed and no stage is renumbered.** Stage 5 is still Stage 5 and
Stage 6 is still Stage 6. Only the position of two steps moves. A dated record
saying "Stage 5" means the same step before and after this ruling, so **Process v3
needs no mapping table of the kind CLAUDE.md section 8 carries for Process v1 to
v2.** That is the reason to move the gate rather than the copy edit.

**Chapter 1 does not migrate.** It is locked under Process v2 and its record keeps
v2 ordering, exactly as v1 records keep their v1 numbers. Chapter 2 would be the
first chapter run under v3.

**The scoped re-run matrix is unchanged, row for row.** Every edit class still
re-runs what it can invalidate. What changes is how many completed steps sit
downstream of the steps most likely to move text, and therefore how often the
matrix bites.

## 8. Implementation surface

Verified against the code rather than estimated:

| File | Change | Size |
|---|---|---|
| `reopen.py` | `ORDER` list, reorder two entries | One line |
| `gen_checklists.py` | `STAGES` list, move two tuples | Two blocks moved |
| Stage folders, eighteen units | Renumber prefixes | Mechanical migration, precedent is `renumber_stage_folders.py` |
| `CLAUDE.md` section 8 | Step table, sequencing rules, a v3 note | Prose |
| `AIOM_Workplan_v5.md` | Decision 68 | Prose |
| `status_check.py` | **None.** It derives step order from the checklist headings and validates no hardcoded sequence | Zero |

**The folder migration touches no tool path.** The only stage folder any tool
resolves by name is `00_Stage0_Draft`, in `web_build.py`, `amend.py`,
`specimen.py` and `web_gates_selftest.py`, and Stage 0 does not move. This was
checked by grep across every `.py` in the repository, and the single other hit is
a historical apply script living inside Chapter 1's own copy-edit folder.

**Stage 6 keeps the render it needs.** `copyedit_export.py` takes `--pdf` as a
path to a production render and does not read gate status, so a render produced
for the copy-edit proof satisfies it whether or not G2 has run. The dependency is
on the renderer, not on the gate, which is what makes this reorder possible at
all.

## 9. Risks, and the condition that would reverse this

**Risk 1. A design or production defect is found later in the run than it is
today.** Real, and partly mitigated by the second proposal in the process review,
which is to run the mechanical suite continuously on any in-flight chapter rather
than only at named checkpoints. Under that pairing, mechanical defects surface at
the commit that introduces them and only the judgment-level page read moves late.
Adopting v3 without the continuous suite is weaker than adopting both.

**Risk 2. A late design finding that requires a CSS change re-runs Stage 5 and G2
for every chapter under the matrix.** This is true today and is not made worse by
the reorder, but it is made later, and later is more expensive when fourteen
chapters exist. This argues for the design system staying locked at v7.1, which is
already the standing position.

**Risk 3. The copy edit now reads a chapter no design review has passed.** Chapter
1 says this costs little, because the copy edit runs on a `.docx` proof that
carries blocks and cropped figures rather than the page design. It is the risk to
watch on the first chapter run under v3.

**Reversal condition.** If the first chapter run under Process v3 produces Stage 5
findings that require prose changes rather than CSS or tooling changes, then the
design read belongs before the copy edit after all, and Option B is the fallback:
move G2 alone and return Stage 5 to position 7.

## 10. What this does not fix

Stated so that adopting it is not mistaken for solving the whole problem.

- **The external round trips.** Stages 1, 3, 6, 7 and 8 are Dan's, and Stages 3
  and 7 are structurally external because no source host is reachable from the
  Claude environment. Five of thirteen steps wait on a human and each wait is a
  session boundary.
- **The 7.3 to 1 record ratio.** A separate proposal: a fixed short form per
  finding, with prose reserved for findings that need argument.
- **The manual reads.** Gaps G-I and G-II still require pages to be read whenever
  pagination or callout placement moves. This proposal makes them happen once
  instead of five times. It does not automate them.
- **The W14 blind spot.** A withdrawn claim restated in different words matches no
  forbidden string, which is how SF2 returned as SF8 and returned a third time on
  2026-08-14. No reordering touches that.
- **The check-the-check tax.** Three print gates have been found reading green
  while measuring nothing. The print suite still has no negative controls of the
  kind `web_gates_selftest.py` provides for the web suite.

## 11. The decision requested

Rule one of:

- **Option C**, recommended: move Stage 5 and Gate G2 to after Stage 7, adopt
  Process v3, and run Chapter 2 under it.
- **Option B**: move Gate G2 only, leaving the design review at position 7.
- **Option A**: no change, and the five-reopen pattern is booked as expected cost.

If C or B is ruled, the implementation is the six rows in section 8 and Chapter 2
starts under the new order.
