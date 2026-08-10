# Session handoff

Last updated: 2026-08-10, at the close of the THIRD session that day. Read this
plus CLAUDE.md before starting work, and update this file before ending the
session. The protocol is CLAUDE.md section 11. A SessionStart hook
(`.claude/settings.json`) prints this file into context automatically at the
start of every session, alongside the voice and craft card.

## Repository state

Active working branch: `claude/stage-6-edits-rof1yb`, new in the THIRD 2026-08-10
session. It replaces `claude/chapter-1-status-gli2c0`. **DO NOT ADD TO THAT
BRANCH, AND READ THE NEXT PARAGRAPH BEFORE ASSUMING IT IS FINISHED.**

**`main` WAS MERGED UP ON DAN'S INSTRUCTION AND `main` AND THIS BRANCH ARE
LEVEL.** The branch took five commits and `main` was fast-forwarded to the branch
head. Verified immediately before pushing rather than trusted from a reading taken
earlier in the session: `git rev-list --left-right --count origin/main...HEAD`
reported `0 5`, `git log origin/main ^HEAD` was empty, and
`git merge-base --is-ancestor origin/main HEAD` confirmed `main` was a strict
ancestor. A specific SHA is deliberately not recorded here, because it goes stale
on the next commit.

**A COMMIT WAS STRANDED ON THE PREVIOUS BRANCH AND NEARLY LOST, WHICH IS THE MAIN
LESSON OF THIS SESSION.** Stage 6 CE1 was committed to
`claude/chapter-1-status-gli2c0` AFTER that branch had already been levelled with
`main`, so `main` never received it, and the next session cloned a container whose
live text did not contain the edit. The session opened believing Stage 6 edits
were in progress and found a clean tree, no pull requests, no issues, and no
returned proof. The edit was recovered by fast-forward, but only because every
branch was searched for commits `main` did not have:

```
git fetch --all --prune
for b in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin); do
  n=$(git rev-list --count origin/main..$b); [ "$n" != 0 ] && echo "$b +$n"; done
```

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

## Chapter 1 status: 8 of 13, EVERY STEP CLAUDE OWNS BEFORE LOCK IS DONE

25 pages, 7,062 words, CSS v7.1, `voicecheck.py` mechanically clean,
`status_check.py` reports 8/13 STATUS CONSISTENT. Stages 3, 4, 5 and G2 all
cleared 2026-08-10.

**Dan's Stages 6, 7 and 8 are next and may run in one sitting.** Then G3 and
Stage 9, both Claude's.

**STAGE 6 IS UNDER WAY. ONE EDIT IS APPLIED, CE1, AND THE CURRENT PROOF IS ROUND
4.** Chapter is 7,066 words after CE1. Full record under Stage 6 in the checklist.

  `Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit_round4.docx`
  `Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit_round4.manifest.json`

**ROUND 3 IS SUPERSEDED AND MUST NOT BE REVIEWED.** Its `.docx` still displays the
pre-CE1 Category error definition, and 64 of its 221 spans went stale when CE1
shortened the live text by three characters. It is kept as the artifact of its
step, not deleted.

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
preflight, gate 12 fixed 2026-08-09), `place.py`, `cite_format.py`,
`footnotes.py`, pinned `requirements.txt`. **The design-spec debt is PAID.** It
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
(now prints the Decision 33 measure), `reopen.py`, `continuity.py` (G3),
`AIOM_Continuity_Ledger.md`, `typographic_quotes.py`, `renumber_stage_folders.py`.

## Open threads, in priority order

0. **UNRULED DECISION, cheap and it blocks nothing.** The Stage 3 packet was
   generated by a throwaway script in the session scratchpad, so it is not
   reproducible for Chapters 2 to 15. It should become `factcheck_packet.py` at
   the repo root if the packet is judged worth having every chapter. Dan has not
   ruled. Until he does, regenerating the Chapter 1 packet means rewriting the
   script.

1. **Chapter 1 Stages 6, 7 and 8. DAN'S, AND THEY MAY RUN IN ONE SITTING.** Copy
   edit, final fact check 2, final read. **STAGE 6 IS UNDER WAY: CE1 IS APPLIED
   AND THE CURRENT PROOF IS ROUND 4**, exported from the post-CE1 live text with
   both the round trip and the span check banked. Open
   `AIOM_Ch1_CopyEdit_round4.docx`, edit in Word, return it, and import through
   `copyedit_import.py` with the round-4 manifest. **DO NOT USE ROUND 3.** Stage 7
   is structurally external. THREE THINGS TO CARRY INTO THE ROUND:

   - **Any edit that changes the live text invalidates the current proof.** CE1
     shortened it by three characters and staled 64 spans. Re-export after
     applying a round, and run the span check rather than relying on the round
     trip, which cannot see staleness.

   - **Diff the return against the ruled sentences before crediting it.** Three
     ruled Stage 3 narrowings and one ruled Stage 4 fix were silently reverted
     by the LAST copy edit, and nothing mechanical saw any of them: every date
     and figure survived intact. The quoted sentences are in the register notes
     and the checklist. This is the single highest-risk moment left in the
     chapter, because Stage 6 is the step that caused the reopen.
   - **The theorem panel blocks export but the importer refuses edits to them.**
     That is standing rule 4a working as designed. If a panel line reads badly
     the remedy is the prose beside it, never the panel.

2. **Gaps G-I and G-II are not closed, and bind any future design work.** Both require a chapter whose
   pagination or callout placement moves to be READ rather than gated, and this
   chapter's pagination moved four times on 2026-08-10. Gate 14 still cannot see a
   stranded head GROUP, and a floated callout can still collide with a block panel
   unseen.

3. **G3 and Stage 9, both Claude's, after Dan's three steps.** Stage 9 carries a
   BOOKED PENDING-ACTIONS LIST in the checklist, because these are owed at lock and
   are easy to lose: re-set the craft baseline band from the locked text (NOTHING
   READS AGAINST A BAND UNTIL THIS IS DONE); do NOT let `continuity.py --update`
   record "flow" among Chapter 1's terms, since Chapter 2 owns it and a mis-logged
   entry would fail G3 on Chapter 2; and check whether "category error" should be
   logged as a Chapter 1 term, since it became the eighth key term on 2026-08-10,
   after the ledger design was written.

4. **Remaining process hardening** (Dan approved, still to build):
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

5. **Chapter 2 (The Flow).** Drafts against the amended band, 6,500 to 7,500, and
   is the first chapter written under the craft standard from Stage 0, so its
   acknowledgment box is a live requirement rather than a retrospective one. TWO
   THINGS IT MUST CARRY FROM DAY ONE: `<html lang="en-US">` (Decision 59; there is
   no CSS lever and no gate reports its absence) and `.nb` on proper nouns
   (Decision 58). And it is read against NO craft band until Stage 9 re-sets one
   from the locked Chapter 1.

6. **Decision 28**, Northmoor properties G, H, I. Gates Ch9, Ch12, Ch13 problem
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
  reading found flush paragraphs in the summary and a dated box (2026-08-08) and
  confirmed three moved-page cases (2026-08-09). No gate measures paragraph
  separation inside a block.
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
- The chapter HTML is the single source of truth (Decision 50). Never fork.
- Source register notes inside a chapter's own Decision 51 block can carry
  rulings the summary ledger does not. Read them before using a figure.
- **Write every fact-check ruling back into the register note, with the condition
  that would reverse it.** A ruling recorded only in the checklist is a ruling
  the next checker will raise again.
- **Not every proposed remedy is an improvement.** Evaluate the remedy separately
  from the finding.

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
