> **STATUS: PARTLY RULED.** D-A to D-F RULED YES 2026-09-30 as Decisions 75 to 80.
> D-G is proposed and not ruled; nothing else in this file is in force until Dan rules it. If adopted it becomes Decisions 75 onward in `AIOM_Workplan_v5.md`,
> which is the numbering authority. The standing rules in CLAUDE.md section 2 are
> untouched by every proposal below.

# Process v4: one week per chapter

Author: Claude, 2026-09-30. Raised by Dan: "It's taking a month to do a chapter. It
should take a week. I want to be thorough and conservative on sources and language,
but this is moving way too slow." The target is at least a 50 per cent cut.

---

## 1. Where the time actually went

Measured from the repository on Chapter 2, the first chapter run under Process v3.
Chapter 1 shows the same pattern at a larger scale.

| Measure | Chapter 2 |
|---|---|
| Opened to locked | 252 hours (08-21 to 08-31) |
| Hours with nobody working, waiting between sessions | about 154 (61 per cent) |
| Separate sittings where Dan had to rule or act | about 18 |
| Decisions Dan ruled | about 60 |
| Claude sessions | 6, each loading about 82,000 tokens of CLAUDE.md and HANDOFF.md first |
| Blocks the copy edit changed | 104 of 195 (Chapter 1: 59 of 155) |
| Times the frequency-claim sweep ran | 5, and it is still booked as unfinished |
| Fact checks | 2, and the first checker could not read sources, so the second redid it |
| Tool defects fixed in the middle of the chapter | about 15 |
| Second-model packages built | 4 (one never sent) |
| Checklist length against chapter length | 29,254 words against 7,453 (3.9 to 1) |
| Commits touching only markdown records, whole project | 49 per cent |
| Commits touching chapter text, whole project | 22 per cent |

**The finding.** Claude's working time on Chapter 2 was about five active days. The
rest was the chapter waiting for the next round trip with Dan, and each round trip
reopened work that an earlier step had already done. The process is slow because it
has too many hand-offs and it checks the same text before and after the text changes.
It is not slow because any single check is slow.

Seven causes, largest first:

1. **Too many hand-offs.** About 18 sittings for one chapter. Every sitting is a gap
   of a day or more, and three gaps alone cost 154 hours (48, 80 and 26 hours).
2. **The copy edit is really Dan's rewrite, and it comes too late.** It changed more
   than half the chapter, after fact check 1, the voice check and the developmental
   edit had all been run. So those steps checked text that no longer exists, and the
   copy edit brought in new voice violations, two reverted fact-check rulings and a
   new unsourced claim.
3. **Two fact checks, and the first one could not do the job.** The Stage 3 checker
   had no web access, so real source verification slid to Stage 7, which reversed
   several Stage 3 rulings. Stage 3's work was mostly thrown away.
4. **Three separate review passes (Stages 1, 2, 4), each with its own second-model
   package and its own ruling sitting.** They read the same draft for overlapping
   things. Stage 1 turned into a 15-decision working session.
5. **Tools were built and fixed during the chapter.** About a third of the Chapter 2
   commits are tooling. Every tool fix mid-chapter means a rebuild, a re-check and a
   record.
6. **The same sweep ran five times.** The "organizations usually do X" claims were
   swept at Stages 1, 4, 6 and 7 and still not finished, because no single step owns
   them.
7. **Record-keeping overhead.** Each session reads about 82,000 tokens of rules and
   history before it starts. HANDOFF.md is 3,300 lines and repeats itself. Every
   defect becomes a new capitalised paragraph in CLAUDE.md. A finding costs more to
   record than to fix.

---

## 2. The proposal: seven steps, four sittings for Dan

The thirteen steps become seven. Every check that exists today still runs. What
changes is **when** it runs (once, on the text that ships) and **how many times Dan
is interrupted** (four, down from about eighteen).

| # | Step | Who | Replaces | Dan's time |
|---|---|---|---|---|
| 1 | **Plan** | C, Dan approves | new | Sitting 1: 20 minutes |
| 2 | **Draft, self-checked** | C | Stage 0, G1 | none |
| 3 | **Review** | C plus one second model | Stages 1, 2, 4 | Sitting 2: one batch of rulings |
| 4 | **Author pass** | D | Stage 6, and most of Stage 8 | Dan's own pass, in Word |
| 5 | **Fact check** | D, external, once | Stages 3 and 7 | Sitting 3: one batch of rulings |
| 6 | **Production** | C | Stage 5, G2, G3 | none |
| 7 | **Sign-off and lock** | D, then C | Stage 8, Stage 9 | Sitting 4: 15 minutes |

### Step 1. Plan (Claude, then Dan approves once)

Claude writes a one-page plan before drafting: the opening case and its source, the
teaching sections, the craft artifact, the registry objects the chapter renders, the
forward promises it pays or makes, and a **source list for every empirical claim the
chapter intends to make**. Dan approves or redirects in one sitting.

*Why:* Stage 1's structural questions are cheapest before a word is drafted. Most of
Chapter 2's fifteen Stage 1 decisions were questions a plan would have settled.

### Step 2. Draft, self-checked (Claude, no hand-off)

Claude drafts, then runs everything mechanical before anyone sees it: G1 structure,
`voicecheck.py`, `registry.py --check`, `continuity.py`, `chapter_check.py`, and a
**frequency-claim sweep that the draft step now owns**. Every sentence saying what
organizations "usually", "commonly", "often" or "almost always" do is either cited,
rewritten as a formal conditional, or cut, exactly as standing rule 2 requires. A
short script lists every such sentence so the sweep is complete rather than
remembered.

*Why:* this is the only way the sweep stops running five times. One step owns it.

### Step 3. Review (Claude plus one second model, one ruling sitting)

One review pass replaces three. Claude reads the draft once against three things:
structure (the old Stage 1 test against the Structure and Exit Competencies files),
teaching quality (the old Stage 2), and voice and craft (the old Stage 4, the seven
criteria). **One** second-model package covers all three, with one prompt. Claude
applies every fix that is not a judgment call, and hands Dan **one list** of the
decisions that are his, each with a recommendation. Dan rules the list in one
sitting.

*Why:* the three passes read the same draft for overlapping things and each needed
its own package, extract and sitting. Independence is kept: the second model still
reads without Claude's findings.

### Step 4. Author pass (Dan)

Dan does his rewrite **here**, in Word, through the existing `copyedit_export.py`
and `copyedit_import.py` round trip. This is the step that changed 104 of 195 blocks
on Chapter 2. Moving it before the fact check means the fact check, the voice
mechanics and the design review all run on the text Dan actually wants.

After import, Claude re-runs the mechanical checks (voice bans, W14 claim ledger,
frequency sweep script) on the changed blocks only and reports anything they catch.
A later typo fix is still a copy edit and re-runs only G2.

*Why:* this is the single biggest saving. Every step after this one now checks
final text, so nothing is checked twice.

### Step 5. Fact check (external, once, with web access)

One external fact check on the **rendered PDF of the post-author-pass text**, run as
**two parallel checks on different prompts**, which is the rule already in force:
check A reads the sources, check B reads only the render. The checker **must have web
access**. Chapter 2's Stage 7 proved an external checker can read sources, and Stage
3's checker could not, which is why Stage 3's work was thrown away.

Claude builds the packet with `factcheck_packet.py`, Dan runs both checks, and Dan
rules the combined findings in one sitting. Rulings are written into the register
notes and the claim ledger as now.

**This is not less conservative. It is more.** Today the first fact check reads text
the copy edit then rewrites, so its rulings can be reverted and nobody sees it (SF8,
SF9, SF10, FC2). Checking once, on final text, with a checker that can read, closes
that hole. W14 still guards the rulings afterwards.

### Step 6. Production (Claude, one session)

Design review (the page raster read), G2 and G3, run once, after the text is final.
Pagination is fixed once instead of at Stages 2, 3 and 4 as on Chapter 2. **Stage 5
is never run early**, which on Chapter 2 made it run twice.

### Step 7. Sign-off and lock (Dan, 15 minutes)

Claude sends Dan the render plus a short diff of everything that changed since his
author pass (usually fact-check fixes and design fixes). Dan approves, and Claude
locks. The full read-through that Stage 8 was is folded into Step 4, because that is
when Dan is already reading every block.

---

## 3. Supporting changes that make the week possible

These are not steps. They are the overhead cuts.

**S1. Tool freeze during a chapter.** No new gates, no tool rewrites, while a chapter
is in flight. A tool defect found mid-chapter goes on a short list and is fixed
between chapters, unless it blocks the chapter. Chapter 2 fixed about 15 tools in
flight.

**S2. HANDOFF.md becomes one page.** Current state only: branch, chapter, current
step, open decisions for Dan, next action. Target under 150 lines. The 3,300 lines of
history move to `archive/HANDOFF_history_to_2026-08-31.md`, where they are kept and
not auto-loaded.

**S3. CLAUDE.md becomes the rules, not the history.** The standing rules, the
process, the build commands and the repository map stay. The "rules that came from a
check being wrong" narratives, which are most of its 1,664 lines, move to a
`LESSONS.md` that is read when working on tooling, not at the start of every
drafting session. Target: CLAUDE.md under 400 lines. **No rule is deleted, only
moved.** Also fix the session-start hook, which still prints the retired v1 voice
card instead of the v2.0 standard.

**S4. One line per finding in the checklist.** Finding ID, what, ruling, commit. The
reasoning goes in the commit message. Chapter 2's checklist was 3.9 times the length
of the chapter.

**S5. Batch Dan's rulings, never one commit per ruling.** Dan rules a list; Claude
applies the list in one commit.

**S6. Claude prepares the next package before the sitting, not after.** The 80-hour
gap on Chapter 2 was spent waiting for a second-model package that had not been
built yet.

---

## 4. The week, day by day

| Day | Work | Dan |
|---|---|---|
| 1 | Plan, Dan approves; Claude drafts and self-checks | Sitting 1 (20 min) |
| 2 | Review pass and second model; decision list to Dan | Sitting 2 (rulings) |
| 3 to 4 | Dan's author pass in Word; Claude imports and re-checks | Author pass |
| 5 | Fact check A and B, both external; Dan rules | Sitting 3 (rulings) |
| 6 | Production: design review, G2, G3 | none |
| 7 | Sign-off and lock | Sitting 4 (15 min) |

The week holds only if each sitting happens within a day of the package being ready.
Hand-off gaps are the one cost Claude cannot cut.

---

## 5. What does NOT change

- Every standing rule in CLAUDE.md section 2, including no em dashes, every claim
  cited or conditional or cut, the six-slot skeleton, and the registry rules.
- Every mechanical gate: fifteen print, seventeen web, W14, G3, registry check.
- Two external fact checks on different prompts, now run in parallel on final text.
- An independent second-model read. There is one, not three.
- Locked Chapters 1 and 2 keep the process they were locked under, as Chapter 1 kept
  Process v2. The amendment path in CLAUDE.md section 8 is unchanged.

## 6. Risks, and what would reverse this

- **Risk: one review pass misses what three would have caught.** Mitigation: the
  single second-model package covers all three questions, and the mechanical checks
  run after every change. **Reverse if** Chapter 3's fact check or sign-off finds a
  structural problem that the old Stage 1 test would have caught.
- **Risk: Dan's author pass introduces claims that need sources.** This is already
  true today. Now the fact check runs after it, so it is caught once instead of
  slipping through.
- **Risk: the tool freeze leaves a real defect in place for a chapter.** Blocking
  defects are still fixed immediately. Only improvements wait.

## 7. Decisions for Dan, in order

Each is independent. The first four carry most of the saving.

1. **D-A. RULED YES 2026-09-30, Decision 75.** Move Dan's rewrite (the copy edit) to Step 4, before the fact check.
2. **D-B. RULED YES 2026-09-30, Decision 76.** Merge the two fact checks into one external check, A and B in parallel,
   with web access, on the post-author-pass render.
3. **D-C. RULED YES 2026-09-30, Decision 77.** Merge Stages 1, 2 and 4 into one review pass with one second-model
   package and one ruling sitting. Add the one-page plan as Step 1.
4. **D-D. RULED YES 2026-09-30, Decision 78.** Draft step owns the frequency-claim sweep, backed by a listing script.
5. **D-E. RULED YES 2026-09-30, Decision 79.** Tool freeze while a chapter is in flight.
6. **D-F. RULED YES 2026-09-30, Decision 80.** Shrink HANDOFF.md to one page and CLAUDE.md to the rules, moving history
   to archive files. Nothing deleted.
7. **D-G.** One line per finding; batched rulings; packages built before the sitting.
