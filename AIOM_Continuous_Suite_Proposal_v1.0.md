> **STATUS: PROPOSED, NOT ADOPTED. AWAITING DAN'S RULING.**
>
> Companion to `AIOM_Process_v3_Proposal_v1.0.md`. If both are ruled in, this
> becomes **Decision 69** and the reorder becomes Decision 68; `AIOM_Workplan_v5.md`
> is the numbering authority and settles it either way. Nothing here binds until
> that ruling. Filed at the repository root because it is a live proposal, with the
> banner above so a root file does not read as adopted.

# The continuous suite: a passed step is a claim, and something should hold it

Author: Claude, 2026-08-19. Second of two proposals raised after Dan observed that
Chapter 1 spent most of its elapsed time in checks.

---

## 1. The finding

**The mechanical suite already exists, is already sequenced, and is wired to
exactly the chapters that need it least.**

`amend.py` runs the whole bundle in one pass: `claimcheck` for gate W14,
`voicecheck` mechanical, the print render with its fifteen gates on a temporary
copy at the repository root, and `web_build.py` with its seventeen. CLAUDE.md
puts that at thirty to forty-five seconds. It is the fastest complete statement of
whether a chapter is mechanically sound that this repository has.

It refuses to run on a chapter that is not locked. `amend.py` checks `is_locked`
at two points and exits. So the suite is available to a finished chapter, where
the text has stopped moving, and unavailable to a chapter being drafted, where it
moves every hour.

CI has the same shape, and the reason is structural rather than a missing
trigger. `.github/workflows/web.yml` does run on pull requests as well as on push
to `main`, but it builds with `web_build.py --site`, which resolves every chapter
through `snapshot.py` to its LAST LOCK rather than to the working tree. Gate W2
then refuses anything not at Stage 9. **So a pull request carrying a half-drafted
Chapter 2 is gated against the published Chapter 1**, and the text actually being
worked on is never examined. That is correct behaviour for a deploy pipeline,
whose job is the published site, and it means the deploy pipeline can never be the
place an in-flight chapter is checked.

## 2. What runs today, and when

| Check | Exists | Runs automatically | Runs on an in-flight chapter |
|---|---|---|---|
| Print render plus fifteen gates | Yes | No, at G2 by hand | No |
| `voicecheck` mechanical and house style | Yes | No, at Stage 4 by hand | No |
| W14 claim ledger | Yes | In CI, and in `amend.py` | No, CI reads the last lock |
| Web build plus seventeen gates | Yes | In CI | No, CI reads the last lock |
| `web_gates_selftest.py`, 108 controls | Yes | In CI | Not applicable |
| `status_check.py` consistency | Yes | No | No |

Every check in the left column is written, debugged and fast. The gap is entirely
in the two right-hand columns.

## 3. The defect

**A passed step is a claim about the chapter, and between checkpoints nothing
holds that claim true.**

When Stage 4 passes, the chapter is claiming that `voicecheck` is clean. When G2
passes, it is claiming fifteen gates are green. Those claims are recorded as ticks
and treated as facts by every later step. They are verified once, by hand, at the
moment the step is ticked, and then nothing re-tests them until a human notices
that the text has moved and reaches for `reopen.py`.

CLAUDE.md already states the principle: "A render that passed against older prose
has not passed." The scoped re-run matrix is the repair. What is missing is the
detection. Today a broken claim is found by a person remembering to look.

## 4. Evidence from Chapter 1

**The clearest case is in the 2026-08-08 reopen's own grounds**, which record that
`status_check.py` "reporting 8 of 13 had been false since round 1 landed." The
copy edit changed the chapter, five ticks stopped being true at that commit, and
the record went on asserting them until somebody worked it out. Nothing was
broken in the tooling. Nobody had asked it.

Three more, all from the record:

- **Pagination in this design is tightly coupled and a craft edit is not a local
  change.** A one-sentence reorder pushed footnotes off their calling pages eleven
  pages later, twice. That is the class of defect where the distance between the
  edit and the discovery is the whole cost, because by the time it surfaces the
  page has moved for several reasons at once.
- **Chapter 1's pagination moved four times on 2026-08-10 alone.**
- **Straight quotation marks shipped in every generated footnote past fourteen
  green gates**, and the fix for them introduced a doubled comma that the same
  fourteen gates then passed twice. Gate 15 closed the first half. Neither half
  was visible at the time because nothing was running between checkpoints.

## 5. The design: the chapter's own checklist decides what binds

The naive version of this proposal fails immediately, and the objection is section
7. The version worth ruling on is this one.

**The runner reads the chapter's checklist, asks which steps have passed, and
enforces exactly the checks those steps own.** Nothing more.

| Step passed | What the suite then holds green |
|---|---|
| Gate G1 | Structural checks: six slots in order, provenance line, `lang="en-US"` |
| Stage 4 | `voicecheck` mechanical and the five house-style checks |
| Stage 5 and Gate G2 | The print render and its fifteen gates |
| Stage 3 or Stage 7 | W14, the claim ledger |
| Gate G3 | `continuity.py`, the seven ledger checks |

A chapter halfway through Stage 0 has passed nothing, so nothing binds and the
suite reports without failing. A chapter that has passed G2 fails the build the
moment an edit breaks one of the fifteen gates, and the failure names the step
whose tick just became false.

**This makes the continuous suite an enforcement of the scoped re-run matrix
rather than a new gate.** It adds no standard. It holds the standards already
ruled, at the commit that breaks them, instead of at the next time a human looks.

Under this design the 2026-08-08 case is caught automatically: copy edit round 1
lands, five ticks become false, CI fails naming Stages 2, 3, 4, 5 and G2, and the
reopen happens that hour rather than being reconstructed later.

## 6. Where it runs

**Option 1. CI on every branch.** Cannot be skipped, needs no local toolchain, and
the runner already knows how to install everything, because `web.yml` installs the
pinned requirements, `poppler-utils` and a pinned Chromium today. Cost is
asynchronous minutes rather than seconds: the last five successful runs on `main`
took between 2:07 and 3:10 end to end, including all of that installation.

**Option 2. A local `pre-commit` hook.** Rejected. A fresh container has neither
the Python dependencies nor poppler, which was true again in this session, so the
hook fails until somebody installs the toolchain and the natural response is
`--no-verify`. A check that trains the operator to bypass it is worse than no
check. Hooks also live outside version control unless `core.hooksPath` is set, so
the repository cannot guarantee the hook exists.

**Option 3. By convention, run by Claude at each edit.** This is what happens
today, and it is the thing that failed. A convention is a claim nobody checks, and
this repository has a documented history of records asserting checks that were
never performed.

**Recommended: Option 1 for enforcement, plus the same runner available locally
for fast feedback before committing.** One implementation, two callers.

## 7. The serious objection, and the answer

**An in-flight chapter will fail these gates by design, and a suite that is red
for the whole drafting period trains everyone to ignore it.** A half-drafted
chapter has no provenance line and no six slots. If red is the normal state, red
stops carrying information, which is precisely the failure mode this repository
keeps recording under a different name.

The section 5 design is the answer, and it is why the design is not optional.
Nothing binds until the chapter itself claims it. Red is never the normal state,
because the suite only ever asserts what the chapter's own checklist already
asserts. A red build means a tick is currently lying, which is always worth
stopping for.

## 8. What cannot run continuously must be reported, never claimed

Two of G2's eighteen boxes are marked MANUAL: figure geometry read against a
raster, and the rasterized page-level visual review. Gaps G-I and G-II add more
reading, because a chapter whose pagination or callout placement moves has to be
read rather than gated.

**The runner must never tick these and must not stay silent about them.** When
text moves under a passed G2, it should re-run the sixteen mechanical boxes and
print a warning naming the two manual boxes as now stale, following the precedent
already set by the snapshot divergence warning: report, do not fail, because
failing would demand a human read on every keystroke.

This is the honest limit of the proposal. It reduces what a G2 re-run costs, from
eighteen boxes to two, and it cannot reduce it to zero.

## 9. One implementation, not two

The bundle must be **extracted** from `amend.py` into a runner that both callers
use, never reimplemented beside it.

This repository's signature failure is two artifacts of one thing that silently
disagree, which is why gate W1 exists, why the URL policy was collapsed into
`site_url` after three emitters answered it separately and two were wrong, and why
`--body-face` names the family once. A second copy of the mechanical suite,
drifting against `amend.py`'s copy, would be that failure in the one place whose
whole job is detecting it.

Concretely: `amend.py` keeps its behaviour and calls the runner. The runner gains
the ability to work on an unlocked chapter, which the web half already supports
through `web_build.py --preview`, documented as an unlocked, noindex, local build.

## 10. Implementation surface

| File | Change |
|---|---|
| New `chapter_check.py` | The runner. The mechanical half of `amend.py` lifted out, plus the section 5 step-to-check mapping read from the checklist |
| `amend.py` | Calls the runner instead of carrying its own copy. No behaviour change |
| New `.github/workflows/chapter.yml` | Runs the suite on push to any branch, over every chapter under `Drafts/`. A separate workflow rather than an extension of `web.yml`, because that one builds the published snapshot by design and must keep doing so |
| `web_build.py` | None. `--preview` already covers the unlocked case |
| `status_check.py` | None. It already parses the checklist and reports each step's status |
| `CLAUDE.md` section 5 and 6 | Document the runner and what binds when |

The print half needs the copy-to-root dance that CLAUDE.md section 5 describes,
because `AIOM_build.py` sets `base_url` to the input file's own directory.
`amend.py` already does exactly this with a temporary file it removes afterwards,
so the runner inherits a solved problem rather than solving it again.

## 11. Risks, and the condition that would reverse this

**Risk 1. CI minutes on every branch push.** The repository is public, so Actions
minutes are free, and three minutes is the measured cost. A path filter on
`Drafts/**`, the stylesheets and the Python files would trim runs that cannot
change any outcome.

**Risk 2. A flaky or environment-dependent check makes the suite untrustworthy.**
This has a precedent worth naming: W16b was green locally and red on every page in
CI, because it compared a browser measurement against a font file's own metrics.
The fix was structural rather than a loosened tolerance. Any check that behaves
differently on the runner than here must be fixed the same way and not tolerated
as noise, or Risk 2 becomes the section 7 failure by a slower route.

**Risk 3. The suite becomes the standard.** A green continuous suite is evidence
about what the gates measure and about nothing else. CLAUDE.md says this in four
places and it does not stop being true because the check runs more often. The
suite must not be allowed to substitute for the reading passes, and the manual
boxes in section 8 are where that pressure will show up first.

**Reversal condition.** If the suite produces failures that are routinely
overridden rather than fixed, the step-to-check mapping in section 5 is wrong and
should be re-derived from what each step actually claims, not loosened check by
check.

## 12. What this does not fix

- **It does not reduce how often the expensive steps re-run.** That is the other
  proposal. This one reduces what each run costs and shortens the distance between
  introducing a defect and finding it. The two are complementary and the reorder is
  the larger effect.
- **It does not read anything.** Every judgment stage stays exactly where it is.
- **It cannot see the W14 blind spot.** A withdrawn claim restated in different
  words matches no forbidden string, and running that check more often does not
  give it eyes.
- **It does not close gaps G-I or G-II**, and section 8 is the reason.
- **The print suite still has no negative controls.** Running a check that measures
  nothing more frequently produces more confident silence, not more evidence. Three
  print gates have been caught reading green while measuring nothing, and
  `web_gates_selftest.py` has no print counterpart. **If this proposal is adopted,
  that omission gets worse rather than better**, which is an argument for building
  the print controls alongside it rather than afterwards.

## 13. The decision requested

Rule one of:

- **Adopt, as specified**, meaning the section 5 checklist-driven design, CI on
  every branch, the runner extracted from `amend.py` rather than duplicated, and
  the manual boxes reported stale rather than ticked. **Recommended.**
- **Adopt the runner only**, with no CI wiring, so Claude has one command instead
  of four and enforcement stays a convention.
- **Decline**, and the mechanical checks continue to run at checkpoints by hand.

If it is adopted, the honest sequencing note is that it pairs with the print
negative controls in section 12, and that Chapter 2 is the first chapter that
could run under it from Stage 0.
