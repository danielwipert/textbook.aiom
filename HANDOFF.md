# Session handoff

Last updated: 2026-08-13. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session, alongside the voice and craft card.

## Repository state

Active working branch: `claude/textbook-website-design-h9nk9t`. **THREE COMMITS
AHEAD OF `main`, NOTHING BEHIND.** `git rev-list --left-right --count
origin/main...HEAD` reports `0 3`, checked after a fetch rather than assumed. The
three are the web edition proposal, Decisions 60 to 64 with the plan adopted, and
Phase W1. **NOT YET MERGED UP.** Merging is Dan's call: this is a new sub-project
rather than a chapter, and nothing on `main` depends on it.

The remote is clean and now holds two branches:

  main                                     the trunk, at 2b22b3f
  claude/textbook-website-design-h9nk9t    this one, +3, pushed

**THE 2026-08-12 STRANDING IS FULLY RESOLVED.** All three leftover branches named
in the previous handoff are gone from the remote. The durable lesson survives its
occasion and is repeated here because it will recur: **A DELETED BRANCH IS NOT
GONE WHILE A SESSION HOLDING IT IS STILL ALIVE.** A long-running container carries
a local ref and full push rights, so a push from an old session recreates what was
just deleted, and `git push --delete` returns 403 from this environment so Claude
cannot undo it. Close the sessions, then delete.

**THE WEB EDITION IS THE ACTIVE SUB-PROJECT.** Chapter 1 is locked and Chapter 2
is still the next DRAFTING target, but on 2026-08-13 Dan opened the web edition as
a parallel sub-project and it is where this branch's work is. Thread 8 below is the
live record.

**"MERGE MAIN UP" WAS ASKED FOR IN THIS CONTAINER ON 2026-08-12 AND THE ANSWER WAS
THE OPPOSITE DIRECTION.** `main` was EIGHTEEN commits ahead and this branch held
nothing `main` lacked, because the reconciliation session had already merged it.
Fast-forwarding `main` to the branch head, the phrase's usual meaning here, would
have been a no-op at best. The fetch-first rule and `git_hygiene.py` both caught it
before anything was pushed. This is the second consecutive session where the
inherited fast-forward assumption was false, so treat it as dead rather than as
unlucky.

Historical, from the 2026-08-12 reconciliation session:

**FOUR SESSIONS WORKED CHAPTER 1 BETWEEN 2026-08-10 AND 2026-08-12 WITHOUT SEEING
EACH OTHER, AND THE RESULT WAS THREE DISAGREEING RECORDS OF ONE CHAPTER.** Dan
ruled `claude/stage-7-explanation-sdsb38` the base, and this branch is the
reconciliation: `main` merged in first, then `stage-7` merged on top, with the
Stage 6 copy edits CE3 to CE6 layered over the Stage 7 fact-check narrowings FC2
to FC5. Nothing was discarded from either side.

**CLOSED 2026-08-12. `claude/stage-6-edits-rof1yb` IS MERGED AND ITS WORK IS IN
THIS TEXT.** It had held three commits nothing else contained: the Stage 6
closure at 9 of 13, the Stage 7 packet, SF11, and `factcheck_packet.py`. All are
now on `main`. Dan ruled option B: take everything, but leave the Stage 6 tick
OPEN, because the closure was made on 2026-08-10 and then stranded while two
sessions that could not see it applied four further copy edits. The closure text
is preserved verbatim in the checklist under a header reading RECORDED BUT NOT IN
FORCE. Re-closing Stage 6 is one character in the checklist and it is Dan's.

Worth keeping as a warning about handoffs rather than about branches:
`stage-7`'s HANDOFF asserted it REPLACED that branch. The git graph said
otherwise. Both branched from `e233c12`, and `stage-7` never contained those
three commits, so a handoff written in good faith sent the next reader past work
that was still stranded. **VERIFY A SUPERSESSION CLAIM WITH
`git merge-base --is-ancestor` BEFORE BELIEVING IT.** A branch is superseded when
the graph says so, never when a document says so.

**THE FAST-FORWARD ASSUMPTION THIS FILE CARRIED SINCE THE BEGINNING IS DEAD.**
Every entry before 2026-08-12 says `main` carries no commits of its own so every
merge is a clean fast-forward. Told "merge main up", the 2026-08-12 session ran
the fetch first and found `main` six commits AHEAD with one of its own
outstanding. A force would have destroyed two HANDOFF refreshes, two proof rounds
and 190 lines of checklist record. **"Merge main up" is a request to make the two
level, NOT a licence to force. If `git log origin/main ^HEAD` is non-empty, STOP
AND READ WHAT IS THERE.**

**USE `python3 git_hygiene.py` BEFORE EVERY MERGE AND EVERY SESSION CLOSE. DO NOT
HAND-ROLL THE SWEEP.** Ruled 2026-08-12 and written into CLAUDE.md section 9,
along with the rest of the git rules, because keeping the repository coherent is
Claude's job and it cost Dan a drafting session.

**THE HAND-ROLLED SWEEP THIS FILE USED TO CARRY WAS WRONG, AND ITS NUMBERS ARE
CORRECTED HERE.** It reported nine branches carrying 149 commits `main` did not
have. **That was a shallow-clone artifact.** The container clones with
`fetch --depth 50`, so an older branch's common ancestor sits beyond the
boundary, `git merge-base` fails, and `git rev-list origin/main..<branch>` counts
the branch's WHOLE history as unmerged. After `git fetch --unshallow`:

  claimed   9 branches, 149 commits stranded
  actual    3 branches,  24 commits stranded, and 13 branches FULLY MERGED

Four of the seven "dead" branches were fully merged the whole time. A sweep that
reports noise as danger is worse than no sweep, because it spends the reader's
trust. `git_hygiene.py` deepens before measuring, every run.

**BRANCH CLEANUP IS DONE. THE REPOSITORY IS THREE BRANCHES.** Dan deleted eleven
fully merged branches and then two of the three that carried unmerged work, all
on 2026-08-12, after every item worth keeping had been extracted onto `main`.
What remains:

  main                             the trunk
  claude/chapter-1-status-gli2c0   the 2026-08-12 working branch, level with main
  claude/chapter-1-handoff-review-sbkq2u   +3, STILL PRESENT, superseded

The third is a leftover rather than a decision: Dan ruled all three for deletion
and two went. It holds a reading copy, a copy-edit worksheet and its builder, all
Process v1 artifacts superseded by `copyedit_export.py`. Nothing in it is wanted.
Delete it whenever convenient. Recovery point if that judgment is ever wrong:
tip `68bc904`.

**THE TWO DELETED BRANCHES CARRIED UNMERGED COMMITS, so their tips are recorded
here rather than in a commit message that scrolls away:**

  chapter-1-prose-style-x0bzze  tip 84d6d04  +20  style guide, gate 15 and the
                                                  five house-style checks all
                                                  EXTRACTED first; vocabulary
                                                  ledger PRESERVED under archive/
  handoff-review-ownf6v         tip a52f95f  +1   copyedit_docx.py, ancestor of
                                                  copyedit_export.py

Unreachable objects survive on the remote for a window, and a recorded SHA is
what makes recovery a procedure rather than a hope: `git fetch origin <sha>`.

**THE NEAR MISS WORTH REMEMBERING.** The 2026-08-12 audit first called the
placed-vocabulary ledger "least urgent, possibly superseded". That was true when
written and false four hours later, because adopting the prose style guide the
same day made its section 2.4 live, and 2.4 only works across fifteen chapters if
something records which terms have already been placed. Deleting the branch would
have destroyed a live requirement four hours after adopting the policy that needs
it. **A SUPERSEDED VERDICT HAS A DATE ON IT. Re-check it against what the repo
adopted since, not against what it looked like when the verdict was written.**

**BRANCH DELETION IS BLOCKED FROM THE CLAUDE ENVIRONMENT AND IS DAN'S.**
`git push --delete` returns HTTP 403 for every branch, singly and in bulk; the
GitHub MCP server exposes `create_branch` with no delete counterpart; the proxy
reports no relay failures, so the remote is refusing rather than the transport
failing. Report the denial, do not route around it.

**CONCURRENT SESSIONS COLLIDE ON NAMES, TWICE OVER.** Both Stage 6 sessions
numbered findings from CE1, so one session's CE2 to CE5 are renumbered CE3 to CE6
with the mapping recorded in the checklist. Both also produced a file called
round 6. Number a finding or an artifact only after checking what the checklist
already owns.

**THE STRANDED-COMMIT LESSON, WHICH IS WHY `git_hygiene.py` EXISTS.** If a later
session finds the live text missing an edit this file claims, do not conclude it
was lost. Run `python3 git_hygiene.py --deep`, which deepens the shallow clone
first and lists every branch holding commits `main` does not have, plus the files
that live only on each. The hand-rolled version of that sweep used to be printed
here and was wrong; see the correction above.

Historical note from the third 2026-08-10 session, kept because the recovery
procedure above is drawn from it:

**A COMMIT WAS STRANDED ON THE PREVIOUS BRANCH AND NEARLY LOST.** Stage 6 CE1 was committed to
`claude/chapter-1-status-gli2c0` AFTER that branch had already been levelled with
`main`, so `main` never received it, and the next session cloned a container whose
live text did not contain the edit. The session opened believing Stage 6 edits
were in progress and found a clean tree, no pull requests, no issues, and no
returned proof. The edit was recovered by fast-forward, but only because every
branch was searched for commits `main` did not have, using the snippet above.

Two things follow. **Merge up before the branch is retired, not after the last
commit you happen to remember**, and **when a session reports work that is not in
the tree, search every branch before concluding it was lost.** Note also that
`origin/claude/stage-6-edits-rof1yb` did not exist on the remote at session start
while a local tracking ref for it did, so the first sync reading looked clean and
meant nothing. That is the THIRD instance of a worthless pre-fetch sync reading.

Historical note from the second session, kept because the reasoning still holds:
**`main` WAS MERGED UP AT THAT SESSION'S CLOSE and `main` and that branch were
LEVEL.** The branch started level with `main`, took four commits, and `main` was
fast-forwarded to the branch head. Every merge so far has been a clean
fast-forward, because `main` carries no commits of its own, and that was verified
before pushing rather than assumed: `git rev-list --left-right --count
origin/main...HEAD` reported `0 4`, and `git log origin/main ^HEAD` was empty,
which is what proves `main` is a strict ancestor. A specific SHA for the head is
deliberately not recorded here: it goes stale on the next commit.

**THE REMOTE-TRACKING REFS IN A FRESH CONTAINER CAN BE STALE. FETCH BEFORE YOU
DIAGNOSE SYNC STATE. THIS HAS NOW HAPPENED TWICE.** The container clones with
`fetch --depth 50` at setup. On 2026-08-09 that stored `origin/main` at `2090bcf`
while the real remote was eighteen commits further on at `95dc1f3`, and reading
the stale ref produced two false conclusions: that `main` was behind, and that
the 2026-08-08 entry's claim of a fast-forward was wrong. Both were incorrect.

**The second 2026-08-10 session hit the identical stale value.** A fresh
container again showed `origin/main` at `2090bcf`; `git fetch origin main` moved
it to the true head in one step. The ref was thirteen commits out of date and
would have made a level branch look far ahead. Two instances of the same stale
SHA is not coincidence, it is what the shallow clone stores, so treat any sync
reading taken before a fetch as worthless.

The lesson is not about that entry, it is about the tooling. `git log origin/main`
and `git rev-list origin/main...HEAD` both read the local tracking ref, and in this
environment that ref can be an old snapshot rather than the remote. Run
`git fetch origin main` first, then:

```
git fetch origin main                                   # ALWAYS FIRST
git status                                              # working tree
git rev-list --left-right --count origin/main...HEAD    # main behind / ahead
git log --oneline origin/main ^HEAD                     # empty = ff is safe
python3 status_check.py                                 # authoritative status
```

This is the same failure the repo has hit repeatedly in its own checks: a reading
that looks authoritative, taken from an input nobody re-derived. It cost a false
claim in a handoff, which is the one file that must not carry one. The 2026-08-10
session added a second instance of the same shape in a different place, a scope
claim in the Stage 5 record naming a page that had not been read; see the chapter
status below.

## Chapter 1 status: **LOCKED 2026-08-13, 13 of 13.** THE FIRST LOCKED CHAPTER

`status_check.py` reports 13/13 STATUS CONSISTENT. 25 pages, 7,069 words on the
Decision 33 measure, fifteen gates green against CSS v7.1, `voicecheck.py`
mechanically clean and house style clean on all five checks, G3 passing against a
populated ledger.

**WHAT LOCK MEANS FOR ANYONE OPENING THIS FILE NEXT: do not edit Chapter 1.** No
change without an explicit `reopen.py`, which re-runs every step from the one
owning the change. The full lock record, including what lock does NOT mean, is
under Stage 9 in the checklist and should be read before any reopen is considered.

**THE LEDGER NOW HOLDS A CHAPTER, WHICH CHANGES WHAT G3 DOES.** Eight owned terms,
five forward references to Chapters 2, 3, 4, 6 and 14, and one registry gloss for
THM-009. Until today G3 compared every chapter against an empty ledger and could
not fail. From Chapter 2 onward it can, and it will: those five forward references
are now promises a later chapter is held to, and "category error" plus seven other
terms may not be redefined.

**THE CRAFT BASELINE BAND IS IN FORCE FOR THE FIRST TIME**, set from the locked
text and written into `AIOM_Voice_and_Craft_v1.md` section 4. From 2026-08-05 until
today no chapter was read against a band, deliberately, because the earlier numbers
measured a chapter the copy edit had replaced. **Chapter 2 is the first chapter
read against one.** Two things in that block stop it being misused: the numbers are
advisory proxies and never thresholds, and the band contains a known flat stretch
at 1.1 that Stage 4 ruled a deliberate choice, so the mean is a description of what
shipped rather than a target.

**TWO ITEMS WERE OPEN AT LOCK AND STAY OPEN.** The "early May" preview-bill timing
in footnote 3, which external check 2 could reach only through secondary coverage
and which no Claude session can verify, and the THM-009 numbering question, which
is a Stage 2 or Stage 5 matter rather than a fact check. **A locked chapter with
two open items is an honest record; one claiming none would not be.**

Historical, and the record of how it got here:

**STAGE 6 IS CLOSED, ON DAN'S RULING OF 2026-08-12: "I have no more edits."**
Second closure of this step and the one in force. Fourteen copy edits raised, ruled
and applied, CE1 through CE14. It does NOT mean a further round is impossible:
Decision 24 places the step late so it runs on prose that has stopped moving, and
prose that moves again reopens it. The reversing condition stands, and a finding
from any later read enters as CE15.

**THE RECORD WAS FIVE FINDINGS SHORT WHEN THE RULING ARRIVED, AND WAS COMPLETED
BEFORE THE TICK.** CE10 to CE14 were in the live text with no entry in the
checklist, because the session that applied them ran concurrently with the
reconciliation and wrote its record into commit messages instead. Reconstructed
verbatim from `d19bf74` and `fceb220`; the chapter text was not touched. **CHECK A
STEP'S FINDINGS LIST AGAINST THE TEXT BEFORE TICKING IT, NOT AFTER.** A tick is a
claim about a record, and this record described a chapter five edits older than the
one on disk.

**THE PART 5 RULE 1 PROXY IN `voicecheck.py` IS DEFECTIVE AND ITS NUMBERS MUST NOT
BE QUOTED.** Recovered from the CE10 to CE12 record. It counts fronted adverbial
phrases as subject-verb separations, and a fronted adverbial is right-branching and
permitted, so both its baseline and its after-reading were measuring something the
rule does not cover. Fourth check in this repo to read authoritative while measuring
nothing. The sound measure moved: 40 long comma-fenced asides to 35. **This is
unfixed and is the one open defect in the ported house-style checks.**

Nothing downstream was invalidated by the tick: the last edit to the live text was
CE13 and CE14, and G2 was re-run after it.

**G2 PASSED ON THE RECONCILED TEXT, run from the top rather than carried forward.**
Fifteen gates, 25 pages, all twenty-five read at 150 dpi with the rasters deleted
and regenerated first so no page from the previous run could be read by mistake. No
new defect. Gate 15 ran against this chapter for the first time and reports zero
straight marks, which is independent confirmation by tooling that the PG2 fix
survived the reconciliation. Hyphenation with page turns included: 95 line ends,
zero inside a brand name, zero at a page turn.

**THE FIGURE GEOMETRY CHECK WAS WRONG ON ITS FIRST ATTEMPT, AND THIS IS THE THIRD
CHECK IN THIS REPO TO READ GREEN WHILE MEASURING NOTHING.** Pixel sampling with a
tolerance of 14 cannot separate `--amber-fig` #C0521A from `--amber` #B4551F, which
differ by 12 in red, so both matched every pixel and the check would have passed a
figure using the wrong token. It was re-run by taking dominant saturated colours
exactly. **WHEN A CHECK COMPARES COLOURS, MAKE THE TOLERANCE SMALLER THAN THE
DISTANCE BETWEEN THE TOKENS IT MUST TELL APART, OR MATCH EXACTLY.** It was caught by
noticing both tokens reported identical hit counts, which is impossible if they are
different colours, not by re-reading the code.

Historical, and the reason G2 was reopened at all:

**G2 HAD BEEN GREEN AGAINST PROSE THAT NO LONGER EXISTED.** It was passed 2026-08-11
against the pre-CE3 text. CE3 to CE6 were then ruled and applied on 2026-08-12 by the
reconciliation, the scoped re-run matrix sends a copy edit to G2, and no re-run was
made against the reconciled text. So `status_check.py` read 8 of 13 STATUS
CONSISTENT while a gate was green against prose that no longer existed. That is the
same shape as the 2026-08-08 reopen, and it happened again for the same structural
reason: a merge can invalidate a gate that neither side re-ran, because each side
was internally consistent. **AFTER ANY RECONCILIATION, RE-CHECK EVERY GATE TICK
AGAINST THE DATE OF THE LAST EDIT THAT COULD MOVE IT.** Nothing mechanical does
this today.

**EVERY G2 FROM NOW ON IS FIFTEEN GATES.** Gate 15, typographic marks, was added
2026-08-12, first ran against this chapter at the re-run above, and passed.

**`gen_checklists.py` WAS EMITTING FOURTEEN GATE BOXES WHILE THE BUILD RAN FIFTEEN,
AND BOTH ARE FIXED.** A G2 pass could have been ticked without gate 15 ever being
recorded. This is the 2026-08-05 drift running the other way: then the checklist
claimed checks the build never performed, now the build performed one the checklist
did not list. Both produce a gate that reads green while nobody looked. G2 is now
eighteen boxes. Found only because CLAUDE.md requires checking box TEXT against the
generator after a reopen, since `reopen.py` resets ticks and does not regenerate
text.

**STAGE 7 IS OPEN. EXTERNAL CHECK 1 IS BACK AND ARCHIVED; FOUR OF ITS FIVE
PRECISION FLAGS ARE APPLIED.** Full record under Stage 7 in the checklist.

**STAGE 6 AND STAGE 7 BOTH HAVE WORK APPLIED, FROM TWO DIFFERENT SESSIONS THAT
DID NOT SEE EACH OTHER.** Both sets are now in one text.

  CE1 to CE6           Stage 6 copy edits, applied 2026-08-10 to 2026-08-12
  FC2, FC3, FC4, FC5   Stage 7 fact-check narrowings, applied 2026-08-11
  FC1                  OPEN, and half of it is decidable without a source
  CE7, CE8, CE9        raised and UNRULED, listed in the checklist

**FC1 IS THE ONE LIVE CHAPTER DEFECT AND IT IS VISIBLE ON PAGE 11.** The July 2025
dated box carries no date in its prose, and the paragraph after it opens "Eleven
days later", so the reader is asked to count eleven days from nothing they have
been given. That half needs no source. The other half does: the interval is
measured from the July 17 press report rather than from the encounter the report
dates to July 14. Of the two remedies offered, "eleven days after the first
reports" keeps the precision and supplies the antecedent; "two weeks later" blurs
both.

**BOTH PRODUCTION FLAGS WERE PHANTOMS, AND THE CAUSE IS PROCEDURAL: THE CHECKER
WAS GIVEN THE CHAPTER HTML RATHER THAN A RENDER.** Theorem 1's four antecedents
render intact on page 9 and P3's table is correct; the extraction dropped `<li>`
contents and collapsed empty cells leftward. Stage 3 fed PDFs and Stage 7 must too,
on every chapter. They carry no FC number, because they were disproved rather than
ruled. Note that the P3 flag would reproduce even against the PDF under naive text
extraction, since an empty cell contributes no text: it dies only to a read or to
the geometry.

**EXTERNAL CHECK 2, ON A DIFFERENT PROMPT, IS STILL OWED.** Stage 3 established
that two checks on different prompts beat one thorough check, and that the
disagreement between them is the value. One check is not the step.

**STAGE 6 HAS FOURTEEN EDITS APPLIED, CE1 TO CE14, AND THE CURRENT PROOF IS
ROUND 9.** Rounds 3 to 8 are superseded and must not be reviewed.

  `Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit_round9.docx`
  `Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit_round9.manifest.json`

  CE1        Category error key term rewritten in plain syntax
  CE2        "a round" cut from the craft section
  CE3        Meter relocation defined twice and differently; key term now verbatim
  CE4        number style mixed inside one sentence
  CE5, CE6   pronoun-antecedent faults
  CE7 to CE9 RAISED AND UNRULED, listed in the checklist
  CE10       the stacked-interrupter sentence the style guide itself cites
  CE11, CE12 two further interrupters, per style guide Part 5
  CE13       antithesis budget, and a genuine repetition it surfaced
  CE14       "the reader" removed from the teaching body

**CE3 IS THE FINDING WORTH CARRYING TO EVERY CHAPTER, AND IT IS NOW MECHANICAL.**
"Meter relocation" was defined twice, once as a body callout and once as a key
term, and the two did not match. The other three terms appearing in both places
were character for character identical, which is what showed this to be an
oversight. Gate 6 counts entries and header bands and read 8 and 8 throughout, and
it was a live G3 risk because `continuity.py` treats a verbatim restatement as not
a redefinition. **The check now runs in `voicecheck.py` as part of the house-style
block**, and its negative test reproduces CE3 exactly.

**CE13 IS THE ONE TO LEARN FROM, BECAUSE THE COUNT WAS NOT THE FINDING.** The
antithesis budget reported 4 against 3. Reading them showed two making the SAME
move one paragraph apart in 1.4: "not because no one is paying attention" and
"What is missing is not attention". A repetition a reader feels. The budget
surfaced it; the reading found it. The C6 guard that the cut clause was carrying
was verified present twice elsewhere in the same section BEFORE cutting.

**A REGISTER NOTE QUOTED THE SENTENCE CE11 CHANGED, AND WAS UPDATED IN THE SAME
COMMIT.** Sixth instance in this chapter of a record outliving the prose, and the
FIRST caught at the moment of the edit rather than three steps later. Before
editing any sentence, grep the register for it. That note is where SF8 to SF10
were found, precisely because it quotes the sentence.

**TWO EDITS ARE APPLIED, CE1 AND CE2, AND EACH ONE STALED THE OUTSTANDING PROOF.
THAT IS NOW A RULE RATHER THAN AN OBSERVATION: the re-export is part of applying
an edit, not a later step.** CE1 shortened the live text by 3 characters and
staled 64 spans; CE2 shortened it by 8 and staled 74.

**CE2, "a round" cut from the craft section.** Dan read "a round five thousand
agents" as a typo for "around". It was not one, and the answer went the opposite
way from the report: "a round" was correct, and "around" would have been WRONG,
because the paragraph performs exact arithmetic on the figure. That arithmetic was
verified rather than assumed and every quantity follows from 5,000 exactly. The
finding was the misreading rather than the grammar, since a reader who resolves
the phrase as "around" takes an approximate five thousand where the passage means
an exact one. "Stipulate" already carried the work, so the two words were cut.

**A FULL MECHANICAL SPELLING AND GRAMMAR PASS RAN WITH IT, AND ITS LIMIT IS THE
PART WORTH CARRYING.** `aspell` en_US over 7,181 words with the source register
excluded: zero spelling errors, and the doubled-word, article, split-word and
homophone checks all clean. It would NOT have caught "a round" had that been
wrong, because the phrase is two correctly spelled words in a grammatical
construction. The reader caught what the tooling could not, and the tooling then
proved the reader wrong. Neither was sufficient alone, which is the same shape as
gate 12 and DR7. Three recorded false positives, so they are not re-raised: "COST
COST USAGE USAGE" is Figure 1.2's two panels each carrying both axis labels,
`README` is the register's own key, and "a usage-based charge" is correct.

**CE1, the Category error key-term entry, rewritten in plain syntax.** Dan's
finding, ruled and applied. Two sentences at mean 25.5 words became four at mean
12.5, in genus and differentia form, with the semicolon splice gone. Meaning
unchanged and the same five propositions survive, which is what holds it in the
copy-edit row of the scoped re-run matrix, re-running G2 alone. Verified in a
fresh container rather than trusted from the commit message: fourteen gates pass,
25 pages held, `voicecheck.py` mechanically clean, Key terms improves from mean
18.2 to 15.9 words and from 14 to 19 percent short sentences.

**THE STANDING ROUND-TRIP CONTROL IS NECESSARY AND NOT SUFFICIENT. THIS IS THE
TRANSFERABLE FINDING OF THE SESSION AND IT BINDS EVERY LATER CHAPTER.** CLAUDE.md
requires the unedited export to round-trip at zero reported changes before either
Stage 6 tool is trusted. Round 3 PASSED that control at 221 blocks, zero edited,
zero applied, zero refused, while 64 of its spans were stale, because
`copyedit_import.py` compares the return against the manifest's own recorded text
and never against the live file. A manifest that has drifted from the chapter
still round-trips clean. The check that sees it compares each recorded span
against the current live text:

  round 3   spans correct 144/221   stale by exactly -3   64   other 12
  round 4   spans correct 209/221   stale                  0   other 12

The twelve are by design and identical in both rounds: six body paragraphs whose
span encloses a nested `<cite>`, and their six footnote blocks whose citation-key
marker the export excludes under Decision 51. Expect twelve; fail on a thirteenth.
Adding this to the Stage 6 procedure for Chapters 2 to 15 is NOT YET RULED.

The stale span was established as a usability problem and not a corruption risk by
READING the apply path, not by assuming. `copyedit_import.py` locates each edit
inside `frag = src[s0:e0]`, a real slice of the current file, so a located match
carries a true absolute offset even when the window is shifted, and it writes only
under `if a.apply and not problems and not refused`, so one refusal blocks the
whole write.

Superseded, from the second 2026-08-10 session:

221 blocks, exported from the live text against a fresh fourteen-gate render.
The `.manifest.json` beside it is what `copyedit_import.py` maps the return
through, so keep the pair together. Nothing in the folder before it is current:
round 2 was committed 2026-08-08 and twenty-one commits have touched the live
text since, so reviewing it would mean reviewing the text the Stage 2 re-run,
the Stage 3 restorations and the Stage 4 craft fixes all replaced. The unedited
export was round-tripped before the proof was handed over and reported 221
paragraphs against 221 blocks with zero edited, zero applied and zero refused,
which is the control CLAUDE.md requires before either Stage 6 tool is trusted on
a chapter. The live text hash was captured before and after to prove the dry run
mutated nothing.

The production render it was cropped from is `build/Ch1.pdf`, which is
gitignored and dies with the container. Rebuild it from the block in CLAUDE.md
section 5 if it is wanted again.

**G2 found PG1, now Decision 59: the book sets `lang="en-US"`, never `lang="en"`.**
In Pyphen, which WeasyPrint hyphenates through, `en` is an ALIAS FOR en_GB, so a
Chicago-styled American book was breaking on British points ("organiz-ation" for
"or-ga-ni-za-tion"). Five of 88 line-end breaks sat at points en_US would not
choose. THERE IS NO CSS LEVER: it is a per-document attribute, so EVERY NEW
CHAPTER MUST CARRY IT, and one that omits it hyphenates British silently with no
gate reporting it. After the fix: 25 pages held, zero non-American breaks, zero
proper nouns broken, and line-end breaks rise 88 to 95, which is a gain because
more legal points mean better spacing in a justified measure.

**A FALSE SCOPE CLAIM WAS WRITTEN INTO THE STAGE 5 RECORD, BY CLAUDE, AND IS
CORRECTED IN PLACE.** It said ten pages were rasterized and read. Nine were. Page
1 was never rasterized and page 4 was rasterized and never opened, and page 4 is
exactly where PG1 sat until G2's full 25-page read found it. Fifth instance in
this repo of a check claimed in a record that was not performed, and the first
authored here rather than inherited. WRITE A SCOPE CLAIM FROM WHAT WAS DONE, NEVER
FROM WHAT WAS INTENDED. G2's own scope statement is written that way and names
which pages were read on which render.

**Stage 5 found two defects by reading that no gate can see, now Decision 58 and
CSS v7.1.** DR6, "ChatGPT" breaking as ChatG-PT in the narrow column beside a
floated callout; DR7, "GitHub" breaking as Git-Hub ACROSS THE PAGE 11 TO 12 TURN.
A new `.nb` class switches hyphenation off for a proper noun and 34 brand
occurrences are wrapped. After the fix, 88 hyphenated line ends and zero of them
inside a proper noun.

**The method is the transferable part.** DR6 came from a raster and only raised
the question; every hyphenated line end in the chapter was then scanned against
its proper nouns, which found DR7 and proved the list complete at two. Eyeing 25
pages finds the first and misses the second, because a break at a page foot reads
as an ordinary hyphen until the page turns. Rewording was rejected on the gate 12
precedent: a break is a property of the measure, not of the sentence.

**A CSS change re-runs Stage 5 and G2 for every chapter,** and this Stage 5 pass
IS that re-run, taken against v7.1. It was taken now deliberately, while Chapter 1
was the only chapter in flight and the cost was one chapter rather than five.

**The design spec debt is paid.** It read v6.9 while the CSS shipped v7.0. It now
carries section 16 for v7.0, section 17 for v7.1 and Decision 58, and section 18
for Decision 59, with its header at v7.1.

**FIVE STALE MIRRORS WERE FOUND AND FIXED ON ONE DAY, FOUR OF THEM IN THE
WORKPLAN.** Its tracker row still said "Stage 6 next, 8 of 13, 20-page render";
its snapshot said the same; its lifecycle paragraph said 6 of 13; its queue named
a finished step. CLAUDE.md's counts were the fifth. Each was true when written and
false within two days. CLAUDE.md and this file are mirrors too. `status_check.py`
is the only source, and the standing item to have it verify the mirrors
mechanically is now the most valuable unbuilt piece of process tooling in the
repo.

**Stage 4 closed with its second-model gut-check still open**, on Dan's ruling and
the precedent of Stage 2 and the archived Stage 4. Six findings, one per criterion:
NC1, NC2, NC3 and NC5 applied, NC4 and NC6 recorded with no edit. Read the "WHAT
THIS TICK MEANS" paragraph under Stage 4 in the checklist before treating it as
more. A finding from the verification prompt enters as NC7 and reopens the step.

**NO CRAFT BASELINE BAND IS IN FORCE, and that is deliberate.** The band recorded
2026-08-06 measures a chapter the copy edit replaced: 17.4 mean and 10.1 stdev
against a current 14.5 and 6.3, with the long tail gone entirely. The standard
makes Chapter 1 the band later chapters are read against, so the stale numbers
would have graded Chapter 2 against a text that no longer exists. Dan ruled the
reset deferred to Stage 9, taken from the locked text. Booked as a Stage 9 pending
action, and the archived block is annotated in place.

**Pagination is coupled tightly enough that a craft edit is not a local change.**
NC5 was a one-sentence reorder inside 1.2. It failed the build twice: once by
splitting "Figure 1.2" across a page turn, and both times by adding a line that
pushed footnotes 5 and 6 off their calling pages ELEVEN PAGES LATER. Build after
any craft edit, and attribute a new gate failure by rebuilding the committed state
rather than assuming the edit caused it, which is how that one was pinned.

**Stage 3 was cleared 2026-08-10 on Dan's executive ruling** that the 2026-08-06
external checks carry it, rather than by running a fresh pair. Read the "WHAT
THIS TICK MEANS" paragraph under Stage 3 in the checklist before treating the
tick as more than it is. A finding from any later external check enters as SF11
and reopens the step.

The packet built for the checks that were passed is still filed in
`04_Stage3_Source_Fact_Check_1/` and is current against the live text:

  AIOM_Ch1_Stage3_FactCheck_Input_v3.pdf   the current render, 25 pages, built
                                           from the live text, fourteen gates
                                           green. The v1 and v2 renders are kept
                                           because a finding is only meaningful
                                           against the text that produced it,
                                           and v2 earned its keep this session.
  AIOM_Ch1_Stage3_Claim_Inventory.md       every cited passage paired with the
                                           register entry behind each key, each
                                           note verbatim.

### What the 2026-08-12 stage-7 container did, AFTER the reconciliation

A second session was still running on `claude/stage-7-explanation-sdsb38` while the
reconciliation below happened, and could not see it. Its Stage 7 and G2 work is
already in `main`; what follows is only what it did after merging `main` in.

1. **Ran G2 to completion on the pre-reconciliation text.** Fourteen gates, figure
   geometry by pixel sampling, and all twenty-five pages read at 150 dpi. It found
   PG2, straight quotation marks in every generated footnote, and then PG2a, a
   doubled comma its own fix introduced through `_join` keying on the ASCII quote.
   Both are fixed in `cite_format.py` and both are in `main`.
2. **Cut CLAUDE.md section 10 from 323 lines to 194**, to durable rules only, and
   graduated six duplicated standing reminders out of this file into it. Every
   retained item was checked to still resolve, and two existed nowhere else: Gap
   G-II and the `AIOM_Source_Ledger.md` pointer.
3. **Told to "merge main up", found `main` eighteen ahead instead.** See the
   repository state above.
4. **Corrected the gate 15 claim, reopened G2, and fixed `gen_checklists.py`.** See
   the chapter status above. This is the one commit `main` does not yet have.

**THE CONNECTING THREAD IS THAT GATE 15 EXISTS BECAUSE OF PG2, AND NEITHER SESSION
KNEW ABOUT THE OTHER.** This container found straight quotes by reading pages; the
reconciliation recovered a typographic-marks gate stranded since 2026-08-05. Two
sessions solved the same defect the same day by different routes, one by hand and
one by tooling. That is the cost of concurrency stated precisely: not wrong work,
duplicated work.

### What the 2026-08-12 reconciliation session did

**Almost none of it was drafting, and that was the point.** Dan ruled mid-session
that keeping the repository coherent is Claude's job, not his, after spending his
time managing files instead of writing. The rules that came out of it are
CLAUDE.md section 9.

**Reconciled four sessions into one history.** `main` was six commits AHEAD with
one of its own outstanding, the first time it was not a strict ancestor. Two
sessions had edited the same chapter, colliding on finding labels (two CE2s) and
artifact names (two round 6 files). Resolved by real merges on Dan's ruling that
`stage-7-explanation` was the base, with nothing discarded from either side. Both
content conflicts turned out to be two correct fixes to one sentence.

**Cleaned git from sixteen branches to three**, and built `git_hygiene.py` so it
does not happen again. The audit corrected its own premise: the hand-rolled sweep
reported nine branches and 149 stranded commits, which was a SHALLOW CLONE
ARTIFACT. The true figure was three branches and 24 commits, with thirteen
branches already fully merged.

**Recovered a week of stranded standards work**, which turned out to be the most
valuable thing found all day: the prose style guide, gate 15, and five
house-style checks, all written 2026-08-05 and never merged.

**Stage 6, eleven edits applied: CE3 to CE6, CE10 to CE14.** Three came from the
recovered style guide's Part 5, one of them the sentence the guide itself cites
as its example and which had survived every step since being named.

**Four checks in this repo were found to be wrong or newly built this day**, and
that is the running theme. Gate 15 closed the punctuation gap. Five house-style
checks were ported, each with a negative test. And TWO CHECKS WRITTEN IN THIS
SESSION WERE THEMSELVES DEFECTIVE and were caught before their numbers were
believed: a span check that reported a freshly written manifest as 6 of 221, and
a Part 5 proxy whose three "violations" were all fronted adverbials rather than
subject-verb splits. Both were reported as wrong rather than quietly re-run.

### What the 2026-08-11 session did

Archived Stage 7 external check 1, applied four of its findings, and re-ran G2,
which failed, was fixed, and passed. Four commits. Advanced no step to passed
except G2, which is where it started.

**TWO OF THE THREE DEFECTS FOUND THIS SESSION WERE IN SHARED PRODUCTION TOOLING,
NOT IN CHAPTER 1, so all fifteen chapters have them fixed before the second is
drafted.** That is the argument for finding them on the exemplar.

**PG2, straight quotation marks in every generated footnote.** All six footnotes
set their source titles in ASCII quotes while body prose used typographic ones, and
both were visible within nine pages of each other: the objection at the head of 1.3
on page 8 read with a proper pair, footnote 1 on page 2 with typewriter marks. In a
Chicago-styled book at university-press standard that is a production defect.
Counted in the rendered text, not inferred from source: 22 straight quotes against
exactly one typographic pair. `cite_format.py:105` now emits curly marks. No gate
sees this; gate 2 tests em and en dashes only.

**PG2a, WHICH THE FIX INTRODUCED AND THE RE-READ CAUGHT. THIS IS THE FINDING OF
THE SESSION.** Applying PG2 doubled the comma in every footnote: `“Clarifying Our
Pricing,”,`. Chicago puts the comma inside the closing mark, so `_join` suppressed
the separator by testing `endswith((',"', ",", "."))`, keyed on the ASCII quote; a
title ending `,”` matched nothing and took a second comma. Both forms are now
tested and the docstring says why.

**All fourteen gates passed the doubled comma twice**, on the build that introduced
it and the build that removed it, because nothing mechanical in this repo reads
punctuation. It was visible on page 2 the moment the page was opened. A one-line
change to shared tooling is exactly the kind that feels too small to re-verify, and
it silently broke a second thing inside the same six footnotes it was correcting.

**THE PAGE READ WAS STOPPED MID-WAY ON THE FAILING RUN, DELIBERATELY, AND THAT
REASONING IS WHY PG2a WAS CAUGHT.** Curly quotes are not the width of straight
ones, so the remedy reflows the footnote blocks and can move the pages carrying
them: a read taken before the fix is invalidated by the fix. Eleven pages were read
and recorded as eleven, then superseded. The final read is all twenty-five pages on
the final render, with the rasters deleted and regenerated between runs so no stale
page could be read.

**FC2 IS A DRAFTING ATTRACTOR, NOT A CLOSED INCIDENT.** It is the same defect as
SF8, made a second time about a second vendor: the copy edit reaches for "the
vendor began charging" because it is shorter than "began enforcing allowances and
offered a paid overage". Both sources are scheduled for reuse in Chapters 4 and 11.

**THE RULED-SENTENCE SWEEP SHOULD BECOME A GATE, AND IT HAS NOW FAILED ONCE BY
BEING RUN BY HAND.** Every ruled sentence quoted in the register was compared
against body prose with the register block excluded so the notes cannot self-match.
Four exist; three were present and only SF3 was absent, so the 2026-08-10 repair
caught SF8, SF9 and SF10 and missed exactly one. About fifteen lines, and it
generalizes to all fifteen chapters. Its limit, stated so it is not overtrusted: it
sees only claims that were once ruled with a quoted sentence. FC3, FC4 and FC5 are
prose drifting broader than a register note on claims never ruled, and nothing
mechanical will find those.

### What the SECOND 2026-08-10 session did

Advanced no step, and that is correct: every step Claude owns before lock was
already done, so the work was preparing Dan's next step and clearing repo debt.
Four commits.

1. **The Stage 6 proof, round 3**, described under the chapter status above.
2. **`python-docx` pinned in `requirements.txt`.** `copyedit_export.py` and
   `copyedit_import.py` both import it and it had never been pinned, so the
   export died with `ModuleNotFoundError` in a fresh container. Pinned at 1.2.0,
   the version that produced the clean round trip. Note the near-contradiction
   the comment now heads off: CLAUDE.md section 7 says python-docx FAILS on this
   repo's `.docx` files, which is true of the spec files, since those carry the
   extension and are plain markdown. The Stage 6 proof is a real `.docx`.
3. **`aiom_md.py` deleted, on Dan's ruling.** It parsed `AIOM_chNN.md` into
   semantic HTML, which was the pipeline before Decision 50 made the chapter HTML
   the single source of truth, and its docstring still asserted the overturned
   premise. Verified dead across every file type before removal: zero references
   to `aiom_md` or `parse_chapter` anywhere, and the only markdown chapter source
   ever written is already filed as
   `archive/AIOM_ch01_markdown_noncanonical.md`. The companion artifact had been
   archived and the parser had not. It carried the repo's only two other unpinned
   imports, `markdown_it` and `mdit_py_plugins`, which went with it rather than
   being pinned.
4. **CLAUDE.md's `chapters/` paths fixed.** The repository map listed
   `chapters/` as "Chapter HTML sources" and all four build commands in section 5
   invoked `chapters/AIOM_ch01.html`. That directory has never existed, so a
   fresh session following section 5 verbatim got a file-not-found on its first
   render.

**THE PATTERN ACROSS THREE OF THE FOUR IS THE ONE THIS REPO KEEPS FINDING, in a
new place.** The dependency gap, the dead module and the wrong paths all sat in
territory no gate covers. The fourteen gates cover the render path and they were
green throughout; Stage 6 is a Word round trip and CLAUDE.md is prose, and
neither is exercised by anything. Each defect read as fine right up to the moment
someone tried to use it. This is the same shape as the gates that were claimed
but never performed before 2026-08-05, and as the five stale mirrors of the first
2026-08-10 session, and it is the standing argument for the unbuilt
`status_check.py` mirror verification in thread 4.

**Section 5 was rewritten rather than path-corrected, because a corrected path
would not have been enough.** There is no chapter path that works for every tool:
the build must NOT run on the live text, since `base_url` is the HTML's own
directory and building in place loses the design system, and `place.py` MUST run
on the live text, since it rewrites the file it is given. The block now carries
that reason, a `LIVE` variable, the Stage 6 pair, and four hazards that were
previously only in this file or in nobody's notes: create `build/` first or the
render raises `FileNotFoundError`, delete the `.print.html` sibling, omitting
`--out` writes a fourth file beside the input, and `place.py` leaves an
ungitignored `.bak`. The documented block was then run verbatim to prove it
works. The `place.py` symlink requirement is the ONE line in it transcribed from
this file rather than re-verified, because running `place.py` would rewrite a
live text that has passed G2.

### What the FIRST 2026-08-10 session did

Cleared TWO steps, Stage 3 and Stage 4, raising ten findings between them.

**Stage 4, six findings, one per criterion.** NC1, the chapter never named its own
title concept: "category error" appeared once, in the first words of the summary,
and nowhere in the opening case or in 1.1 to 1.5. That breached Consolidated Spec
line 565, wording that is itself the product of ruling S3. Applied, and it is now
the eighth key term. NC2, 1.1 gave a thin cause ("simply because AI arrives in the
same commercial packaging") for what 1.4 explains properly as inheritance; the
clause is cut and the argued account keeps its arrival. NC3, 1.3 opened on "A
buyer may object", which is "one might say" with the noun changed; the ruled 2026-
08-06 form is restored. NC4, 1.1 is the flattest prose in the chapter, ruled a
deliberate choice with no edit because the standard forbids adding a sentence for
cadence and both candidate repairs were worse than the condition. NC5, two
paragraphs closed on a pointer; 1.2 reordered, 1.5 ruled to stand. NC6, the guard
holds, recorded with no edit, both archived watch items unchanged.

**The regression check that opened Stage 4 is worth repeating on every chapter.**
Because SF8 to SF10 had just shown that a ruled form does not survive a copy edit,
the applied craft fixes were checked the same way BEFORE the read began. NC1 to
NC3 and F2 to F3 all survived, and two apparent regressions turned out to be false
alarms from rewording. Reading rather than trusting the string match is what
distinguished them, and a grep alone would have raised two findings that were not
there.

**Stage 3: the packet, and four findings.**

**SF8, SF9, SF10, and the reason the ruling to pass was checked before it was
ticked.** Dan ruled that the two external checks would be passed because the fact
checks had already run on 2026-08-06. Before ticking, the current text was diffed
against `AIOM_Ch1_Stage3_FactCheck_Input_v2.pdf`, the artifact those checks
actually audited. The diff supported the ruling on values: eighteen checkable
atoms, zero added, zero altered, so a fresh pair would have re-verified an
unchanged value surface. It also found that the sentences carrying those values
had all been rewritten by the 2026-08-08 copy edit, and that three had regressed
to forms Stage 3 had specifically ruled out.

  SF8   the SF2 mechanism claim was back: "Once the credit ran out, Cursor billed
        each additional request at API rates", against a register note that says
        in as many words not to restore a mechanism claim without a new passage
  SF9   the depletion claim had lost its scoping to the case team and become a
        general claim about "Heavy users" that the primary contradicts
  SF10  the Altman sentence had acquired a compute mechanism the register records
        the sources as not carrying

Ruled: restore all three from the register wording. Applied, and verified by the
same check that caught them: five banned forms absent, four ruled forms present,
value surface still eighteen atoms with zero added and zero gone.

**THE FINDING THAT GENERALIZES, and it is the real output of this session. A
ruled claim narrowing does not survive a copy edit on its own, and nothing
mechanical sees it go.** Every date and figure stayed intact through all three
regressions, so no gate and no check on values could detect them. They were
recoverable only because each register note quoted the exact ruled SENTENCE,
which made the regression greppable and diffable against the audited render.
With DE2 and SF7 this is the fourth instance of the shape. Two consequences, one
of them still unruled:

1. Quoting the sentence a fix adds is a control, not a convenience. See the
   unruled standing practice below, which this converts from housekeeping into
   the thing that saved the step.
2. A chapter whose fact check predates a copy edit should be diffed against the
   audited artifact before that fact check is credited. Run here by hand; it
   should probably be tooling.

**SF7, ruled by Dan and applied earlier in the same session. DE7 came due and did
not check out.** Stage 2
flagged DE7 forward on the grounds that the temporal relation had gone from vague
to explicit, and an explicit claim is checkable in a way the vague one was not.
It failed on two counts. The prose read "In January 2026, four months before that
change", and read as the month at large the interval to the 2026-06-01 transition
runs to five; it is four only from the 2026-01-28 call, which the sentence did not
name. Worse, the `microsoft-2026-q2` note had recorded since 2026-07-29 that the
chapter "attributes the figure to the January 28, 2026 call". It did not, and the
string appeared zero times in body prose. The date was generalized after item A2
was written, most probably in the copy edit, and the note went on asserting the
stronger form.

Ruled: name the date. The sentence now reads "On January 28, 2026, four months
before that change, ...", so the interval verifies from the sentence itself. The
register note was corrected in the same change, which was required whichever way
the prose was ruled. A2 is left standing and dated because it was accurate when
written; the drift, the restoration, and the reversing condition are appended
beneath it.

SF7 is the same shape as SF8 to SF10 seen from the other side. There the prose
drifted away from a ruled form; here the RECORD outlived the prose it described.
Both were catchable only because something quoted the actual sentence.

**Mechanical checks banked** and recorded on the packet's first page: the
register closes both ways, 11 keys defined and 11 cited, zero orphans and zero
dangling; every cite marker resolves; six footnotes all fall on their calling
page.

### What the 2026-08-09 session did

Ran the Stage 2 re-run end to end. Nine findings raised, nine ruled by Dan one at
a time, seven applied to the chapter. Full record with reasoning and verification
is under Stage 2 in `AIOM_Ch01_Checklist_v6.md`.

  DE1  the resource consumption model is now named in the teaching body, in 1.2,
       instead of first appearing in the summary
  DE2  the bridge from the five questions to the three failures, restored. It was
       D1 EDIT 3, ruled 2026-08-01, silently lost in the re-draft and copy edit
  DE3  duplicate causal sentence cut from the opening case
  DE4  theorem antecedent (iv) glossed, so all four are now in plain English
  DE5  the chapter hands off to Chapter 2 once, in the summary, not twice
  DE6  Decision 33 amended to 6,500 to 7,500 with the measure named
  DE7  the Microsoft paragraph names its own date anchor
  DE8  the four-activity clause cut from the consumption-event paragraph
  DE9  theorem panel untouched, gloss split in two, restating paragraph cut

Chapter 7,102 to 7,034 words, 25 pages throughout, all fourteen gates green at
every step.

**Stage 2 was closed with its second-model gut-check still open**, on Dan's
ruling and on the precedent of the archived pass. The tick means the step ran and
every finding was ruled. It does not mean independent verification happened. The
prompt is in the checklist; a stall it finds enters as DE10 and reopens Stage 2.

### Three outputs of that session that are not chapter edits

1. **Gate 12 had a second silent defect and it is fixed.** It counted in-text
   figure references LINE BY LINE, so a reference that wrapped was invisible.
   Applying DE1 moved a line break and the gate failed a chapter whose prose
   names the figure in the sentence beside it. It also dropped any body-size line
   OPENING with a figure label, counting it as neither caption nor reference.
   References are now counted on the joined page text with captions subtracted
   one for one. A NEGATIVE TEST WAS RUN and the fixed gate still fails when the
   reference is genuinely absent.
2. **Standing rule 4a in CLAUDE.md**, from Dan's ruling at DE9: the registry is
   the third rail, and the book is an interpretation of it. A panel rendering a
   registry object is never paraphrased into plainer words. When a statement
   reads as technical, the remedy is the prose beside it, never the statement.
3. **Decision 33 is computable.** It named a band and no measure, and Chapter 1
   produced four defensible counts, two of which put it on opposite sides of the
   band. The measure is now the whole rendered chapter less the source register
   and SVG labels, and `voicecheck.py` prints it as the first craft metric.

### Open observations carried out of Stage 2

- **Page 16 is short by about 1.7 inches** after DE5 pushed the craft-section
  head group to page 17. Read, not gated: the head group is whole and page 16
  ends on a complete paragraph. Carried to Stage 5 as an observation, not booked
  as a defect. Same shape as DR3a.
- **DE7 was flagged for Stage 3. CLOSED 2026-08-10 as SF7**, and the flag was
  worth writing: the explicit claim it created was checkable, and it failed.
- **A standing practice was proposed and is NOT yet ruled:** when a developmental
  or craft fix is applied, record the SENTENCE it adds, in quotation marks, not
  only the reason. DE2 exists because a ruled fix was silently reverted and
  nothing saw it, and it was recoverable only because D1's archived entry
  happened to quote the sentence. A sentence is greppable; a reason is not.
  **SF7 is a second argument for it, from the other direction:** there the RECORD
  outlived the prose, and the drift was visible only because the note quoted what
  it had ruled. Ruling this in would have caught SF7 at the copy edit instead of
  three steps later.

## What lives in the repo

**Specs and standards.** Consolidated Spec, Addendum, Structure, Exit
Competencies, Maturity Model, Case Bank, Northmoor Dataset design, Workplan v5
(Decision 33 amended 2026-08-09), Validation Matrix, and
`AIOM_Voice_and_Craft_v1.md` at v1.1.

**Build and design.** `AIOM_book.css` **v7.1**, `AIOM_DESIGN_SPEC` **v7.1**,
`AIOM_Design_QA_Spec` (current), `AIOM_build.py` (fourteen gates plus toolchain
preflight, gate 12 fixed 2026-08-09), `place.py`, `cite_format.py` (quote handling
fixed 2026-08-11, PG2 and PG2a), `footnotes.py`, pinned `requirements.txt`. **The design-spec debt is PAID.** It
had been written to v6.9 while the CSS shipped v7.0; on 2026-08-10 it gained
section 16 for v7.0 (widows and orphans, and Decision 57's DR2 extended to
`.dated` and `.summary`), section 17 for v7.1 (Decision 58, `.nb` for proper
nouns), and section 18 for Decision 59 (`lang="en-US"`, which is a per-document
attribute and not a CSS rule).

**Stage 6 round trip.** `copyedit_export.py` and `copyedit_import.py`, plus
`08_Stage6_Copy_Edit/apply_round1.py` as the record of how round 1 was applied
when the importer could not land it. The `.docx` is a proof, never a second live
text (Decision 50). Both tools need `python-docx`, pinned in
`requirements.txt` since 2026-08-10. `aiom_md.py` was DELETED that day; if a
record mentions it, it is gone and Decision 50 is why.

**Process tooling.** `status_check.py`, `gen_checklists.py`, `voicecheck.py`
(Decision 33 measure, plus the five prose style guide Part 8 house-style checks
since 2026-08-12; `--voice-only` suppresses that half for Stage 4 work in
progress), `reopen.py`, `continuity.py` (G3), `AIOM_Continuity_Ledger.md`,
`typographic_quotes.py`, `renumber_stage_folders.py`, and **`git_hygiene.py`,
which is run BEFORE every merge and every session close** (CLAUDE.md section 9).

**The prose standard is TWO files and they divide cleanly.**
`AIOM_Voice_and_Craft_v1.md` governs the six craft criteria C1 to C6;
`AIOM_Prose_Style_Guide_v1.md` governs the reader model, altitude, sentence-level
craft, the drafting protocol and the house style sheet. Read both before
drafting. **Part 5 of the guide is the answer to prose that reads denser than its
ideas**, which is the most common complaint about this book's drafts.

**The QA suite is FIFTEEN gates**, not fourteen. Gate 15, typographic marks, was
added 2026-08-12 and closes the gap where no gate read punctuation.

## Open threads, in priority order

**LIVE THREADS AS OF 2026-08-13, in order: 8 (the web edition), 6 (Chapter 2),
5 (process hardening), 3 (design gaps), 7 (Decision 28).** Everything else below is
closed and kept as record. The numbering is left alone deliberately: these numbers
are cited in commit messages and in the checklist, and renumbering would break
those references for cosmetic tidiness. **THE WEB EDITION IS THE WORK ON THIS
BRANCH. CHAPTER 2 REMAINS THE NEXT DRAFTING TARGET AND IS UNBLOCKED.**

8. **LIVE. The web edition, opened 2026-08-13.** Dan asked for the book to exist
   as a website, with `messyjobs.ai` as the inspiration. Plan in
   `AIOM_Web_Edition_Plan_v1.0.md`, rulings as Decisions 60 to 64 in the Workplan,
   durable rules mirrored into CLAUDE.md section 10.

   **What the uploaded `Web Version/` folder turned out to be, because this is the
   finding that shaped everything after it.** Four files. Two were byte-identical
   to files already in the repo. The third, `aiom_md.py`, was deleted on
   2026-08-10 on Dan's ruling. The fourth, `AIOM_ch01.md`, is byte-identical to
   `archive/AIOM_ch01_markdown_noncanonical.md` and is a PRE-FACT-CHECK draft
   carrying the SF2 continuation mechanism, the FC9 absorbed-cost inference, and
   the forbidden word "introduced". Building a public site from it would have
   shipped claims Dan ruled out, with every date and figure intact so nothing
   mechanical would have seen it. The archive README now names all three.

   **Phase W0 (decisions) CLOSED. Phase W1 (pipeline and gates) BUILT AND GREEN.**
   `web_build.py`, `AIOM_web.css`, `web_templates/`, `web_gates_selftest.py`.
   Chapter 1 reports 43,204 characters of prose identical to print and six
   footnotes identical. Build it with:

       python3 web_build.py Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html

   **RUN `web_gates_selftest.py` AFTER ANY CHANGE TO `web_build.py`.** On its first
   run five of twenty-five negative controls did not fire, four of them because
   gate W3's fault was injected into `<title>`, which the extractor skips. The gate
   had been reporting green on faults it had never seen. It also surfaced a real
   defect: the web note extractor had been written as a non-greedy regex twenty
   lines after the print scanner was written to avoid exactly that.

   **Phase W2, the reader design, is BUILT AND GREEN.** Slot rail with reading
   metadata, sidenotes in the margin, tightened apparatus, keyboard layer, motion.
   Gate W6 was added in W2: a twenty-width overflow sweep, the web analogue of
   print gate 1. It is the ONLY optional gate, because it needs a headless
   browser, and it reports SKIPPED plus "W6 NOT RUN" on the verdict line rather
   than passing quietly. It found the P3 inventory table forcing the whole
   document to scroll sideways below 390px. Twenty-nine negative controls now.

   **A RESPONSIVE BREAKPOINT HERE IS ARITHMETIC.** A margin note needs
   `--note + --note-gap` of side track and the side track is
   `(viewport - --rail - --measure) / 2`, so notes fit only from 1411px up. It had
   been set by eye at 1240px, leaving a 170px band where notes ran off the window.
   Redo the sum if any of those four tokens changes.

   **Phase W3, the front door, is BUILT AND GREEN.** Landing page, whole-book
   navigation rail, `book_structure.py`, and gate W7. EIGHT gates now, and
   thirty-four negative controls.

   **THREE RULES CAME OUT OF W3 AND THEY BIND LATER PHASES.** (1) Gate W7 guards
   the joint where the book could split in two: a chapter's title comes from its
   locked HTML, the navigation's comes from `AIOM_Structure_v1.md`, and nothing
   else would notice them disagreeing. (2) A gate handed one page is evidence
   about one page: W3 and W5 had only ever seen the chapter, so the landing page
   was ungated and shipped four straight apostrophes. `gate_pages()` now covers
   every emitted page, and a new page must be added there. (3) Planning prose is
   not publishable prose: only the FIRST SENTENCE of a part's Purpose line is
   published, and no chapter's "Big idea" line is published at all.

   **Decision W-F, ruled 2026-08-13: the web keeps IBM Plex Sans.** Dan supplied
   screenshots of `messyjobs.ai` and its structure was adopted, its typography and
   palette were not.

   **THE LANDING PAGE COPY IS DRAFT AND NEEDS DAN'S RULING.** Hero, lede and
   editions section are written from ruled material but are not themselves ruled.
   Part descriptions are one-sentence placeholders.

   **Phase W4, the reference layer and search, is BUILT AND GREEN.** Glossary,
   per-chapter sources, object index, promises between chapters, client-side
   search. `ledger.py` reads the continuity ledger as data. NINE gates, and
   thirty-eight negative controls.

   **GATE W8 GUARDS THE REFERENCE LAYER AGAINST THE CHAPTER.** W8a requires the
   ledger's definition of a term to be character-identical to the chapter's
   key-term text. A definition is exactly the text that can be reworded with no
   date or figure changing, which is the shape that reverted four times on
   Chapter 1.

   **THREE THINGS TO CARRY.** (1) `find_spans(doc, opener, tag)` is the balanced
   scanner and it takes a tag; a non-greedy regex over nested elements has now
   been the defect three times in `web_build.py`. (2) The reference layer is
   generated from records already enforced elsewhere, never scraped from the
   rendered chapter. (3) The sources page is where URLs live, built with
   `url_policy="full"`; the chapter page matches print so gate W1 stays exact.

   **Phase W5, deploy, is next.**

   **STILL BLOCKED AND IT IS NOT A CODE PROBLEM: `messyjobs.ai` is refused by the
   container's egress proxy** (`gateway answered 403 to CONNECT`, confirmed against
   the proxy status endpoint; a text-extraction proxy was blocked the same way).
   No part of the plan or the design derives from that site. Closing it needs one
   of: the domain allowlisted in the environment, screenshots from Dan, or a
   sentence on what appealed. Ask again before W2 is called finished.

00. **CLOSED 2026-08-12. The prose style guide is adopted and its checks are
    running.** Three items were recovered from `chapter-1-prose-style-x0bzze`,
    stranded there since 2026-08-05. Dan ruled option B: adopt the guide, retire
    its duplicated Part 6 to a pointer, then port the checks separately.

    - **`AIOM_Prose_Style_Guide_v1.md` is on `main` at v1.6.** Part 6 duplicated
      `AIOM_Voice_and_Craft_v1.md` and is now a pointer to it. **The two files
      divide as stated in CLAUDE.md section 2**: the craft file governs C1 to C6,
      the guide governs everything else about prose. Part 9 was rewritten because
      the original described a repository that never existed.
    - **The typographic check is gate 15 in `AIOM_build.py`**, verified by
      negative test.
    - **The five Part 8 house-style checks are in `voicecheck.py`**, ported one
      at a time because the branch script was 262 lines and this one is 470.
      Each verified by negative test; one reproduces CE3 exactly.
    - **STILL UNRULED, BUT NO LONGER AT RISK: the placed-vocabulary ledger.**
      Preserved at `archive/AIOM_Placed_Vocabulary_Ledger_unadopted.md` before
      its branch was deleted. Filed in `archive/` rather than the root because a
      file at the root reads as adopted and Dan has not ruled it in.
      **IT IS PROBABLY A LIVE REQUIREMENT.** Style guide section 2.4 places
      inherited vocabulary once and never re-explains it, which only works across
      fifteen chapters if something records what has already been placed. This is
      that something, and **Chapter 2 is the first chapter that needs it.** Check
      whether `AIOM_Continuity_Ledger.md` already covers the ground, and whether
      the two should merge, before ruling.

    **THE ADOPTION PAID FOR ITSELF WITHIN THE HOUR.** The guide's Part 5 rule 2
    cites one sentence as its example of stacked interrupters, and that sentence
    was still in the opening case, having survived a developmental edit, a voice
    pass, a design review, a production gate and two copy-edit rounds since it
    was named on 2026-08-05. It is CE10. The ported checks then raised CE13 and
    CE14 with no human read involved.

0. **CLOSED 2026-08-10. Dan ruled it in, and `factcheck_packet.py` is now at the
   repo root.** The packet is judged worth having on every chapter: Stages 3 and 7
   each need one, so fifteen chapters need thirty. The argument was the history.
   The Stage 3 packet was built by a throwaway script in a session scratchpad and
   died with its container, and the Stage 7 packet four hours later rebuilt the
   same work from nothing.

1. **CLOSED 2026-08-12. G2 was re-run and passed at fifteen gates.** Reopened
   because the 2026-08-11 pass was taken against the pre-CE3 text. Full record
   under Gate G2 in the checklist. Three things from it that bind the next G2 on
   any chapter:

   - **Delete and regenerate the rasters before a page read.** A page read taken
     against a stale raster is worse than none, and this chapter has now had two
     runs whose renders differ only in places a reader would not suspect.
   - **A colour check needs a tolerance smaller than the distance between the
     tokens it must separate.** The figure geometry check first reported identical
     hit counts for two different colours, which is impossible, and would have
     passed a figure using the wrong token.
   - **Gaps G-I and G-II still mean callout placement and slot openings must be
     READ whenever pagination moves.** It moved again with the copy edits.

2. **CLOSED 2026-08-13. Chapter 1 is LOCKED.** Stage 6 closed 2026-08-12, Stage 7
   and Stage 8 closed 2026-08-13 on Dan's rulings, G3 passed and Stage 9 locked the
   chapter. Two items were open at lock and remain so, named under the chapter
   status above. The Stage 6 proof round 9 and the Stage 7 packet are kept as
   artifacts of their steps, not as live work.

3. **Gaps G-I and G-II are not closed, and bind any future design work.** Both require a chapter whose
   pagination or callout placement moves to be READ rather than gated, and this
   chapter's pagination moved four times on 2026-08-10. Gate 14 still cannot see a
   stranded head GROUP, and a floated callout can still collide with a block panel
   unseen.

4. **CLOSED 2026-08-13. G3 and Stage 9 are done, and all three booked pending
   actions were discharged.** The craft band is set from the locked text, "category
   error" is logged as a Chapter 1 owned term on Dan's ruling, and "flow" is absent
   from the ledger, which turned out to be structurally impossible rather than
   narrowly avoided: `continuity.py` reads the key-term register, never prose. The
   THM-009 gloss was written by hand, because `--update` writes a placeholder
   deliberately and leaving it would make check 4 compare later chapters against
   nothing.

5. **Remaining process hardening** (Dan approved, still to build):
   - **The ruled-sentence sweep as a gate.** About fifteen lines: compare every
     sentence a register note quotes as ruled against body prose, with the register
     block excluded so the notes cannot self-match. It has already failed once by
     being run by hand, missing SF3 on 2026-08-10 and surfacing it as FC2 a day
     later through an external check. Read the limit in the 2026-08-11 section
     before treating it as complete coverage.
   - **Teach gate 14 about head GROUPS**, closing gap G-II. Highest value: the
     defect it misses has appeared twice on the same page of the same chapter,
     and the second time the gate reported clean.
   - **`status_check.py` should verify CLAUDE.md section 10 and the Workplan
     against the checklist. THIS IS NOW THE HIGHEST-VALUE UNBUILT ITEM HERE.** All
     are hand-mirrored, and 2026-08-10 alone found FIVE stale mirrors: the
     Workplan's tracker row, snapshot, lifecycle paragraph and queue, plus
     CLAUDE.md's counts. Each was true when written and false within two days.
   - Canonical `DECISIONS.md` with a status field. Numbers run to **59** across
     several files, with 47/48 flagged unverified. 58 (`.nb`, proper nouns) and 59
     (`lang="en-US"`) were both added 2026-08-10 and live in the design spec.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout.
   - `copyedit_import.py` still drops untagged continuation paragraphs, so a
     split paragraph loses everything after its first line. Unfixed.
   - `place.py` writes a `.bak` beside the chapter, which puts a second chapter
     HTML in the live-text directory and is not gitignored. Delete it after every
     run until the tool is changed.

6. **Chapter 2 (The Flow). THIS IS THE NEXT WORK, and it is the first chapter
   drafted under the full standard.** Word band 6,500 to 7,500 (Decision 33,
   amended 2026-08-09), counted as the whole rendered chapter less the source
   register and SVG labels; `voicecheck.py` prints the number.

   **WHAT CHAPTER 2 INHERITS THAT CHAPTER 1 NEVER HAD:**

   - **A craft baseline band in force**, set from the locked Chapter 1 and written
     into `AIOM_Voice_and_Craft_v1.md` section 4. Chapter 2 is the first chapter
     read against one. Read the two guards in that block before using it.
   - **A ledger that can fail G3.** Eight owned terms may not be redefined, and
     five forward promises are recorded. Chapter 2 owns "flow" and must define it;
     Chapter 1 deliberately does not.
   - **Both prose standards, dividing cleanly.** `AIOM_Voice_and_Craft_v1.md` for
     C1 to C6, `AIOM_Prose_Style_Guide_v1.md` for everything else, and **Part 5 is
     the answer to prose that reads denser than its ideas.** Read both BEFORE
     drafting, not at Stage 4.
   - **Fifteen gates**, including gate 15 for typographic marks, and a citation
     formatter that emits volume, issue and pages with a hyphenated range.

   **TWO THINGS IT MUST CARRY FROM DAY ONE:** `<html lang="en-US">` (Decision 59;
   there is no CSS lever and no gate reports its absence) and `.nb` on proper nouns
   (Decision 58).

   **THE PROVING QUESTION FOR CHAPTER 2 IS WHETHER THE STANDARD PAYS.** Chapter 1
   was drafted before the craft standard existed and was re-drafted against it,
   which cost a full reopen from Stage 0. Chapter 2 is the first chapter to have
   the standard from Stage 0. If it still needs a Stage 4 rewrite, the standard is
   not doing the work at drafting time and that is worth knowing early.

7. **Decision 28**, Northmoor properties G, H, I. Gates Ch9, Ch12, Ch13 problem
   sets only.

## Standing reminders

**Rules that bite.**

- **The build and `place.py` want the chapter in DIFFERENT places, and CLAUDE.md
  section 5 now carries the runnable form.** Do not reconstruct it from memory
  here. In short: `AIOM_build.py` sets `base_url` to the HTML's own directory, so
  building in place under `Drafts/` drops the design system and reports dozens of
  false defects, and the fix is to copy the live text to the repo root, build
  there, and delete the copy and its `.print.html` sibling. `place.py` is the
  opposite case and runs ON the live text path, from the repo root, with
  `AIOM_book.css` and `fonts/` symlinked beside it, because it rewrites the file
  it is given. This bullet graduated into CLAUDE.md on 2026-08-10 per the section
  11 division of labor; it stays here only as the pointer.
- **A green gate suite is not a read page.** With all fourteen gates passing,
  reading found flush paragraphs in the summary and a dated box (2026-08-08),
  confirmed three moved-page cases (2026-08-09), and found straight quotes in every
  footnote and then a doubled comma introduced by their fix (2026-08-11). No gate
  measures paragraph separation inside a block, and none reads punctuation at all.
- **When a check and the prose disagree, fix whichever is actually wrong, and say
  which.** Gate 12 on 2026-08-09 is the cleanest case: rewording the sentence so
  the reference did not wrap would have passed the gate and left every later
  chapter exposed.
- **Read the archived rulings before writing findings.** Two of the nine Stage 2
  findings exist only because that was done: DE2 recovered a ruled fix that had
  been lost, and DE3 was framed as a different finding on rewritten text rather
  than as reopening D3.
- **Read the decision text before proposing an edit that touches it.** DE9 was
  first raised claiming Decision 56 does not constrain the panel's vocabulary. It
  does. Had that gone unchecked, the ruling would have breached it.
- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4.

**Graduated into CLAUDE.md section 10 on 2026-08-11, and deliberately not restated
here.** They were duplicated in both files, and a mirror is the failure this repo
has already paid for repeatedly. Read them there, not from memory:

- a one-line change to shared tooling is not too small to re-verify, because a
  glyph-width change is a reflow
- a check over rendered pages must decide explicitly what it does at a page
  boundary, or it passes the defect it exists to catch
- one live text per chapter, the chapter HTML is it, supersede and delete and never
  fork (Decision 50)
- read the in-chapter Decision 51 register before using a figure from a cited
  study, because it can carry rulings the summary ledger does not
- write every fact-check ruling back into the register note, with the condition
  that would reverse it
- judge a proposed remedy separately from the finding it answers

- **`reopen.py` RESETS BY POSITION IN THE LIFECYCLE, NOT BY THE SCOPED RE-RUN
  MATRIX, AND IT IS UNFIXED.** A reopen at a late step clears every step after it in
  the step order, including ones the matrix would leave intact. On 2026-08-13 two
  citation-lane G2 reopens silently cleared Dan's ruled Stage 6 closure, and the
  loss was invisible until a passed Stage 7 appeared above an open Stage 6. **CHECK
  THE STEPS BELOW A REOPEN POINT AGAINST THE MATRIX BEFORE ACCEPTING THE RESET.**
- **THE PART 5 RULE 1 PROXY IN `voicecheck.py` IS DEFECTIVE. DO NOT QUOTE ITS
  NUMBERS.** It counts fronted adverbial phrases as subject-verb separations, and a
  fronted adverbial is right-branching and permitted, so both its baseline and its
  after-reading measure something the rule does not cover. Unfixed, and the one open
  defect in the ported house-style checks. The sound measure beside it, long
  comma-fenced asides, does work.
- **A COLOUR CHECK NEEDS A TOLERANCE SMALLER THAN THE DISTANCE BETWEEN THE TOKENS
  IT MUST SEPARATE, or an exact match.** The figure geometry check first reported
  identical hit counts for `--amber-fig` and `--amber`, which differ by 12 in red,
  under a tolerance of 14. Two different colours cannot both match every pixel; that
  impossibility is what exposed it, not re-reading the code.
- **DATES IN RECORDS COME FROM THE COMMIT CLOCK, NOT FROM MEMORY.** A session
  crossing midnight UTC wrote several records a day old on 2026-08-13. `reopen.py`
  auto-dated correctly throughout; only hand-typed dates were wrong. This matters
  because the standing control is to re-check every gate tick against the date of
  the last edit that could move it, and that control is worthless if dates drift.

**Tooling facts learned the hard way.**

- **THE DESIGN MIRRORS ITS MARGINS.** Main text starts at x0 68.4 on odd pages,
  57.6 on even. Any new geometry check must derive the edge per page or it will
  read green while measuring nothing.
- The QA suite is FOURTEEN gates. Three checks written in this repo have been
  wrong in a way that read as green, and gate 12 has now been wrong twice. Every
  one was found by changing the input, never by re-reading the code. Treat a
  green gate on unchanged input as weak evidence.
- A fresh session has neither the Python deps nor poppler. `pip install -r
  requirements.txt`, then `apt-get update -qq && apt-get install -y
  poppler-utils`. The build exits 2 without them. The 403s from unrelated
  third-party PPAs during that apt-get are harmless.
- **NO SOURCE HOST IS REACHABLE FROM THIS ENVIRONMENT.** Verified 2026-08-06
  against six hosts; all fail CONNECT with a gateway 403 recorded as a policy
  denial. Do not offer to check a primary. Do not treat a register note as a
  substitute for one either; say which it is.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN. Report
  policy denials, do not route around them.
- To reopen a chapter use `reopen.py`, never `gen_checklists.py --force`. After a
  reopen, check the box TEXT against the generator, not only the ticks.
- Stage folders are on Process v2 numbering across all eighteen units.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- Rasterize for visual review with `pdftoppm -png -r 150`.
