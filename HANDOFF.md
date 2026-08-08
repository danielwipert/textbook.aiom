# Session handoff

Last updated: 2026-08-08 (third entry, session close). Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session, alongside the voice and craft card.

## Repository state

Active working branch: `claude/stage-6-craft-section-r1q9tj`, new on 2026-08-08 and
replacing `claude/textbook-opening-rewrite-ac7yst`. Working tree clean and pushed
to origin.

**`main` was fast-forwarded to this branch at the end of the 2026-08-08 session,
on Dan's ruling**, as it was at the end of the session before it. Each merge has
been a clean fast-forward, because `main` carries no commits of its own. A specific
SHA is deliberately not recorded here: it goes stale on the next commit, and a
handoff that lies about sync state is worse than none. Check it instead.

Verify state any time with:

```
git status                                              # working tree
git rev-list --left-right --count origin/main...HEAD    # main behind / ahead
python3 status_check.py                                 # authoritative status, but see below
```

**THE 2026-08-08 SESSION, IN FULL.** Dan returned the Stage 6 copy edit. It changed
59 of 155 blocks and grew body prose 25 percent, so it is a re-voicing rather than a
copy edit, and Dan ruled it the new live text while keeping the chapter in Stage 6
for further rounds. `copyedit_import.py` could not land it, refusing 162 spans, so
it was applied by span substitution against the manifest
(`08_Stage6_Copy_Edit/apply_round1.py`, guarded so it cannot run twice). Two
standing-rule collisions were ruled: the theorem panel keeps its Decision 56 form
and its four registry antecedents, and the five diagnostic questions in 1.4 are set
as five short paragraphs rather than a new list class. Then `BLOCK_RE` was fixed,
`copyedit_import.py` was taught to refuse edits to registry-bound blocks, and the
round-2 proof was exported and verified. Rounds 2 and 3 came back and were applied,
six rulings Q1 to Q6 were made and applied, the chapter was reopened at Stage 2,
CSS went to v7.0, and Chapter 1 finished the day at 25 pages with ALL FOURTEEN
GATES PASSING and a clean `voicecheck.py`.

**The 2026-08-06 evening session, for context.** The opening case and two teaching
passages were rewritten at Dan's direction and handed back in chat rather than
applied. Those chat rewrites are now MOOT: the round-1 copy edit rewrote the same
passages and is in the live text, so do not go looking for them. The theorem
statement form was ruled (Decision 56) and applied to THM-009. Chapter 1 was
reopened at Stage 5 three times and re-passed each time. The superseded fork was
deleted. Stage 5 and G2 were re-run in full, raising five findings that no gate saw;
Dan ruled DR2 and DR3, which became Decision 57 and took CSS to v6.9.

**One error worth carrying, because the guard against it already existed and was
not used.** Decision 56 was first applied to
`06_Stage5_Design_Review/AIOM_Ch01_Stage4_FINAL.html`, a superseded fork, not to
the live text. It was caught only when this file was opened to be updated, which
is exactly what CLAUDE.md section 11 says to read FIRST. The fork had diverged by
roughly 150 lines. It has since been deleted, so the trap is gone for Chapter 1,
but the lesson is general: read HANDOFF.md before touching a chapter file, and
confirm the live-text path before editing, not after.

## What now lives in the repo

**Specs and standards.** Consolidated Spec (amended 2026-08-05 at Ch1 Stage 1,
each amendment marked with its date and reason), Addendum, Structure, Exit
Competencies, Maturity Model, Case Bank (now carrying CASE 4.6 and CASE 6.4),
Northmoor Dataset design, Workplan v5, Validation Matrix, and
`AIOM_Voice_and_Craft_v1.md` (new 2026-08-05, at v1.1).

**Build and design.** `AIOM_book.css` v7.0 plus the audit-only rule
(`AIOM_DESIGN_SPEC` is still written to v6.9 and OWES a v7.0 update: the CSS moved
on 2026-08-08 and the design spec has not caught up), `AIOM_Design_QA_Spec` (updated 2026-08-05 to the
fourteen-gate suite), `AIOM_build.py` (fourteen gates plus a toolchain
preflight), `place.py`, `cite_format.py`, `footnotes.py`, and pinned
`requirements.txt`.

**Stage 6 round trip (new 2026-08-06, extended 2026-08-08).**
`copyedit_export.py` turns the chapter HTML into a copy-editing `.docx` plus a
manifest recording every block's span in the source; `copyedit_import.py` maps the
returned file back, applying only what it can place unambiguously inside a block's
own span and refusing the rest. The `.docx` is a proof, never a second live text:
Decision 50 still holds. The source register is excluded from the export by design.
Since 2026-08-08 the exporter also carries `<li>`, so a theorem panel travels as
labelled THEOREM SCOPE, THEOREM ANTECEDENT and THEOREM CONSEQUENT blocks marked
`registry verbatim, do not edit`, and the importer REFUSES any edit to them.
`08_Stage6_Copy_Edit/apply_round1.py` is a third, one-shot pass, kept as the record
of how the round-1 return was applied when the importer could not land it.

**Process tooling.** `status_check.py` (lifecycle status, authoritative),
`gen_checklists.py`, `voicecheck.py` (mechanical bans plus per-section craft
metrics), `reopen.py` (new), `continuity.py` (new, gate G3),
`AIOM_Continuity_Ledger.md` (new), and `renumber_stage_folders.py` (new,
one-time, already run).

**Content.** Fonts committed under `fonts/`, the Northmoor dataset under
`Northmoor/`, Chapter 1 artifacts under `Drafts/Ch01_The_Category_Error/`, and
`archive/` for superseded files.

## Chapter 1 status: 3 of 13, reopened at Stage 2, ALL FOURTEEN GATES PASS

`status_check.py` reports 3 of 13, STATUS CONSISTENT, and that number is honest.
It is LOW because the chapter was reopened at Stage 2 on 2026-08-08, not because
the chapter is in poor shape: it is 25 pages, all fourteen gates pass, and
`voicecheck.py` mechanical passes. Stage 2 is the next step and it is Claude's.

**Three copy-edit rounds happened on 2026-08-08 and the chapter is much better
for them.** Round 1 was a re-voicing rather than a copy edit, 59 of 155 blocks,
and Dan ruled it the new live text. Rounds 2 and 3 were real copy edits, the last
at 13 blocks and 34 spans with zero refusals. The esoteric register and the long
periodic sentences are gone.

Body prose across the rounds: words 5,241 to about 6,500, paragraphs 63 to 129,
mean sentence 18.3 to about 15, sentences of 35 words or more 19 to 3. Sentence
length VARIANCE FELL, stdev 10.5 to about 6.9. The long tail is gone, which was
the point, but the prose now clusters at 12 to 18 words, and a long run at one
length is the other half of what C4 prohibits. Any further round should widen
range rather than shorten. Stage 4 will have to rule on this when it re-runs.

**The reopen was ruled deliberately and the copy edit is not closed by it.**
Stage 6 sits after every step the reopen reset, so another round may be taken at
any time. Nothing is waiting on Claude except Stage 2.

Six rulings were made and applied on 2026-08-08, all recorded under Stage 6 in
`AIOM_Ch01_Checklist_v6.md` with their reasoning and their verification:

  Q1  the five diagnostic questions in 1.4 stay as third-person questions,
      marked `p.diagnostic` and exempted from the question-mark ban only
  Q2  the unsourced Microsoft comparison became a formal conditional
  Q3  P1 retitled "Five hundred seats, one meter"; the spec still says CIO memo
      and that divergence is deliberate
  Q4  the book converted to typographic quotes, `typographic_quotes.py` added
  Q5  reopen at Stage 2
  Q6  the two failing gates, FIRST RULED to be booked and left red, then
      REVERSED the same day when Dan asked whether they could be fixed. They
      could. See below.

**CSS is at v7.0.** `p { widows: 2; orphans: 3 }`, plus `.dated p + p` and
`.summary p + p` at 6pt. The design system is no longer locked at v6.9 and every
chapter inherits this. **`AIOM_DESIGN_SPEC` still says v6.9 and owes a v7.0
update.** `AIOM_Design_QA_Spec_v1.md` IS current: G-J rewritten and G-K closed.

**Gate 8's underlying WeasyPrint behaviour is NOT fixed and is not understood.**
The widows setting is good typography on its own merits and was ruled on that
basis; clearing gate 8 was a side effect of repagination. It must NOT be expected
to repeat on Chapters 2 to 15. If gate 8 fails on a later chapter, gap G-J is
where the diagnosis starts, and it records what has already been ruled out:
`footnote-policy: line` is load-bearing, `footnote-policy: block` does nothing,
call position is irrelevant, and there is no minimal repro.

## Still true from before the copy edit

**The live text is
`Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`.** It is
the only chapter HTML for Chapter 1 outside clearly-superseded early stage folders.
Check this path before editing, every time.

**Chapter 1's history to the copy edit.** Reopened at Stage 0 on 2026-08-05
(Decision 53) and re-drafted the same day, then reopened at Stage 5 three times on
2026-08-06 and re-passed each time. Passed: Stage 0, G1, Stage 1, Stage 2, all
2026-08-05; Stages 3 and 4 on 2026-08-06; Stage 5 and G2 re-passed 2026-08-06
against CSS v6.9, on a 20-page render with all fourteen gates green. Every one of
those passes now predates the copy edit, which is why the chapter was reopened at
Stage 2 and why `status_check.py` reads 3 of 13.

**Decision 56, theorem statement form, is applied and survived the copy edit.**
THM-009 is set as a structured conditional: scope boundary first, four antecedents
enumerated in lower-case roman, consequent on its own line. The round-1 return
rebuilt it from an older paraphrase and dropped one registry antecedent; Dan ruled
the Decision 56 panel and the registry antecedents kept. Page number has moved with
the repagination.

**Decision 57 closed all five Stage 5 findings.** DR1 (craft head group stranded
at the foot of page 12) and DR5 (Figure 1.1 using `--amber` instead of
`--amber-fig`) were fixed first. DR2 (`.model p + p` unset, so model-answer
paragraphs ran flush) and DR3 (`table.inv` breaking, spilling one row onto a blank
final page) were ruled by Dan and applied. DR4, hyphenation at three consecutive
hyphenated line ends on four pages, is at Chicago's limit and took no action.
DR3a is an accepted cost: holding the table whole leaves a short page, and
`break-before: avoid` was tried and rejected because WeasyPrint binds it to the
preceding line box rather than the preceding block, splitting a paragraph across
the spread. All five were found on the pre-copy-edit pagination. DR2's ruling
was EXTENDED on 2026-08-08 to `.dated p + p` and `.summary p + p`, which the copy
edit split into several paragraphs each and which then set them flush for exactly
the reason DR2 identified in `.model`. That was found by READING THE PAGE, not by a
gate: no gate measures paragraph separation inside a block. Stage 5 still owes a
fresh read when it re-runs, now on 25 pages.

## Open threads, in priority order

1. **Chapter 1 Stage 2, the developmental edit. CLAUDE'S, AND IT IS NEXT.**

   Nothing blocks it. The chapter is 25 pages with all fourteen gates green and a
   clean `voicecheck.py`. Stage 2 interrogates clarity, pacing, cognitive load,
   example fitness, transitions, and whether the argument carries the target
   reader without a stall. Dan gut-checks with a second model. After it: Stage 3
   (Dan, external, two checks on different prompts), Stage 4, Stage 5, G2.

   Carry into Stage 4: the rhythm finding above. Round 1 removed the long tail
   and also removed range. The advisory metric to watch is the longest uniform
   run, which `voicecheck.py` prints.

   **A further copy-edit round is still available** and does not conflict with
   any of this. The round-3 manifest is stale by several blocks after rulings Q2
   to Q4 and the v7.0 repagination, so a new round means a fresh export.

   **`copyedit_import.py` still drops untagged continuation paragraphs**, so a
   split paragraph loses everything after its first line. Rounds 2 and 3 carried
   no splits so it did not bite, but round 1 did and had to be applied by
   `08_Stage6_Copy_Edit/apply_round1.py` instead. Unfixed.

   **THREE EXPORTER AND IMPORTER BUGS WERE FIXED on 2026-08-08 and the third
   carries the widest lesson.** `BLOCK_RE` did not match `li`, so THM-009's four
   antecedents had never appeared in any proof, which is why the round-1 return
   rebuilt the theorem from a paraphrase and dropped a registry antecedent. The
   importer read a leading `(...)` on ANY tag line as the sources group, so the
   `(a) `, `(b) `, `(c) ` openers round 1 introduced in P2 would have been
   silently deleted. And `strip()` replaced every tag with a space, so
   `<b>access price</b>.` reached the proof as `access price .`

   THE UNEDITED ROUND TRIP CANNOT SEE THE THIRD KIND. The artifact is symmetric:
   export and import agree with each other and both differ from the page. The
   round trip proves the pair is self-consistent, not that it reads the page
   correctly. When a new inline construct appears, compare extracted text against
   the RENDERED text as well.

   The importer now REFUSES any edit to a registry-bound block (theorem scope,
   antecedents, consequent, statement), which travel labelled
   `registry verbatim, do not edit`.

2. **Chapter 1 Stages 7 and 8. DAN'S STEPS.**

   They come AFTER the copy-edit rounds close and after the re-runs those rounds
   owe. Do not start Stage 7 against text that is still moving.

   **The G2 render committed at
   `Drafts/Ch01_The_Category_Error/07_G2_Production_Gate/AIOM_Ch1_G2.pdf` is the
   20-page v6.9 render and is now HISTORICAL.** It is the render the design review
   and the production gate passed, and the chapter is 25 pages against CSS v7.0.
   Do not read it as the current state.

   **Measure proof staleness, do not assume it.** The round-1 proof was described
   here as predating "every Decision 57 change". Measured, it was stale by ONE
   block, the theorem: Decision 57 was a CSS change and moved no block text. Diff
   manifest block text against a fresh `copyedit_export.extract()` rather than
   listing decisions since the export.

   **Before using the export and import pair on any LATER chapter, round-trip the
   UNEDITED export and require zero reported changes.** It has now caught four
   bugs across three sessions, and not one of them was visible any other way. On
   2026-08-08 it caught an importer bug that would have silently deleted the "(a) "
   "(b) " "(c) " openers from three paragraphs of Chapter 1's P2.

   Two things to carry into these steps. Stage 7 is a source check and NO SOURCE
   HOST IS REACHABLE from a Claude session, so it is structurally external. And
   Stage 4 passed without its second-model gut-check, so if that read is ever run
   and disagrees, it enters as NC7 and reopens Stage 4.

   After them: **G3**, the continuity gate, which is Claude's and runs
   `continuity.py`. Then **Stage 9**, lock, also Claude's. Lock is not blocked.

   **An obligation booked for Stage 9, easy to lose:** when Chapter 1 locks,
   `continuity.py --update` must NOT record "flow" among the terms Chapter 1 owns.
   Chapter 2 owns it. Left unchecked, Chapter 2's proper definition registers as a
   redefinition and G3 fails Chapter 2 for a mis-logged ledger entry.

   **The Stage 5 and G2 re-runs of 2026-08-06 found five things and no gate saw
   any of them.** All five are closed; see the chapter status above. The one to
   carry forward is GAP G-II, below. The earlier G2 findings still stand: the G2
   BOX LIST ITSELF WAS STALE: `gen_checklists.py` moved to a seventeen-box list on
   2026-08-05 but this chapter's checklist still had the old ten-box version,
   because `reopen.py` resets ticks and does not regenerate box text. After a
   reopen, check the box text against the generator, not only the ticks. GD1, a
   labelling inconsistency in the craft section's model inventory that Stage 5
   missed, was found by the manual raster review, ruled by Dan, and fixed by making
   all four steps inline bold, which also aligns the craft section with P2. And
   GAP G-I is open: a floated callout can collide with a following block panel,
   crushing a theorem panel's measure, while all fourteen gates pass. Until it
   closes, a chapter whose callout placement moves must have the affected pages
   READ, not merely gated.

   **GAP G-II is new, open, and the most important thing in this file.** Gate 14
   cannot see a stranded head GROUP. It tests whether a HEAD is the last block on
   a page, so any non-head block trailing the group hides the defect completely.
   Decision 56a put `break-after: avoid` on `.slot-label` alone; that bound the
   label to its title, left the provenance line last, and gate 14 then reported
   ZERO stranded heads while all three head lines sat orphaned at the foot of page
   12. A partial fix that silences the check is worse than no fix, because it
   turns a visible defect into an invisible one. v6.8 chains the rule through
   `h2.case-title` and `p.provenance`, so the book is held off this defect by CSS
   rather than by the check. Until gate 14 treats a run of head-like blocks as one
   unit, a chapter whose pagination moves must have its SLOT OPENINGS read, not
   merely gated.

3. **Remaining process hardening** (Dan approved, still to build):
   - `status_check.py` should verify that CLAUDE.md section 10 and the Workplan
     tracker agree with the checklist table. Those three have now been
     hand-mirrored across several sessions; the check would catch drift
     automatically.
   - Canonical `DECISIONS.md` with a status field per decision. Numbers are
     scattered across three files and now run to 57, with 47/48 flagged
     unverified.
   - **Teach gate 14 about head GROUPS**, closing gap G-II, so the book is not
     held off a stranded slot opening by CSS alone. This is the highest-value
     item in this list: the defect it misses has now appeared twice on the same
     page of the same chapter, and the second time the gate reported clean.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout,
     though gate 11 now checks the panel directly.

4. **Chapter 2 (The Flow)** once the Chapter 1 re-draft has settled the craft
   standard in practice. Chapter 2 is the first chapter drafted under the
   standard from the start, so its Stage 0 acknowledgment box is a live
   requirement rather than a retrospective one.

5. **Decision 28**, Northmoor properties G, H, I. Gates the Ch9, Ch12, and Ch13
   problem sets only.

## Standing reminders

**Rules that bite.**

- **Building a chapter that lives under `Drafts/` needs `AIOM_book.css` and
  `fonts/` symlinked beside it.** `AIOM_build.py` sets WeasyPrint's `base_url` to
  the HTML file's own directory, and the CSS is committed only at the repo root, so
  a fresh container renders the chapter with DejaVu fallbacks and reports nonsense:
  no folios, no key-term bands, no theorem panel, gates 5, 7, 12 and 13 all failing
  at once. That signature means the stylesheet did not load, not that the chapter
  broke. Fix with `ln -sfn "$PWD/AIOM_book.css" <stage dir>/` and the same for
  `fonts`, then delete them before committing. CLAUDE.md section 5 shows the build
  command against `chapters/AIOM_ch01.html`; that directory does not exist.

- **A green gate suite is not a read page, and 2026-08-08 proved it again.** With
  all fourteen gates passing, reading the pages found the chapter summary and a
  dated evidence box setting their paragraphs completely flush. No gate measures
  paragraph separation inside a block. Gaps G-I and G-II already say a chapter
  whose pagination moves must be READ; the sharper version is that the read finds
  things the gates were never built to see, so do it after every pagination move,
  not only when a gap warns you.

- **When a check and the prose disagree, fix whichever is actually wrong, and say
  which.** On 2026-08-08 gate 14 reported two widows: one real, one a phantom the
  check could not distinguish from a one-line paragraph. The prose was right and
  the check was wrong, so the check was given the source HTML rather than the
  prose being bent. The opposite call was made on the question-mark ban the same
  day: the rule was right in general, so the exception was made explicit in the
  source with `p.diagnostic` rather than the ban being loosened.

- **Do not conclude "structural" from one lever.** Gate 8's footnote failures were
  booked as an unfixable renderer defect after four prose perturbations failed to
  move them. Prose length was simply the wrong lever; `widows` and `orphans` moved
  them immediately. The booked entry G-J had to be rewritten the same day. Before
  recording something as impossible, name the levers not yet tried.

- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4. Craft
  caught at Stage 4 is a rewrite; craft applied at Stage 0 is free. A SessionStart
  hook prints the six-criterion card into context alongside this file.
- The chapter HTML is the single source of truth (Decision 50). Edit it directly;
  never fork a chapter into a second live text.
- Source register notes inside a chapter's own Decision 51 block can carry
  rulings that `AIOM_Source_Ledger.md`'s summary does not. G1 caught a breach
  this way. Read the in-chapter note before using a figure from a cited study.
- **Write every fact-check ruling back into the register note, with the condition
  that would reverse it.** Stage 3 on 2026-08-06 closed two raises that earlier
  rounds had already answered, and closed a third, SF6, for at least the third
  time. The notes that carried their history ("has been rejected once and should
  be rejected again", "must not return") are what made those closures fast. A
  ruling recorded only in the checklist is a ruling the next checker will raise
  again.
- **A second check is worth running even when the first was thorough, and the
  two disagreeing is the useful part.** The 2026-08-06 pair agreed on one finding
  out of six. Check 2 confirmed a passage check 1 raised, and check 1 caught a
  sourcing gap check 2 restated as sound. Run them on different prompts.
- **Not every proposed remedy is an improvement.** External check 1 proposed
  hedging language the voice rules prohibit, and check 2 proposed second source
  paths below the floor already in force. Evaluate the remedy separately from the
  finding: the finding can be right and the fix still wrong.

**How to read and check.**

- Read Stage 4 ADVERSARIALLY: quote the weakest passage per criterion rather than
  asking whether the criterion is met. The confirmatory version produced a false
  all-clear on Chapter 1. Read the per-section table, never the chapter average
  alone: the average concealed a summary running at twice the chapter's mean
  sentence length, and later concealed a section regression during the re-draft.
- The craft standard was generalized partly from Chapter 1, so it cannot fail
  Chapter 1 on its own. Judge against the named exemplars and the criteria as
  stated. A reusable second-model prompt sits in the Chapter 1 checklist under
  Stage 4, and another under Stage 2.
- `voicecheck.py` craft metrics are proxies and permanently advisory. Do not turn
  them into thresholds: the trailing-qualifier proxy over-reports, flagging three
  strong causal closes in Chapter 1 as weak. C2 and C6 have no proxy at all.

**Tooling facts learned the hard way.**

- **THE DESIGN MIRRORS ITS MARGINS.** The main text column starts at x0 68.4 on
  odd pages and 57.6 on even. Gates 12 and 14 originally hard-coded a single left
  edge and were silently blind on half the book; fixed 2026-08-05 to derive the
  edge per page. Any new geometry check must do the same or it will read green
  while measuring nothing.
- The QA suite is FOURTEEN gates, not eleven. Gates 12, 13, and 14 were added
  2026-08-05, closing three checks the G2 checklist had claimed for months while
  `AIOM_build.py` performed none of them. The G2 checklist now mirrors the printed
  gates one for one, with the two genuinely manual checks labelled MANUAL.
- Three checks in this chapter's re-run were wrong in a way that read as green.
  Every one was a check written in this repo, and every one surfaced by changing
  the input rather than by re-reading the code. Treat a green gate on unchanged
  input as weak evidence.
- A fresh session has neither the Python build deps nor poppler. Run `pip install
  -r requirements.txt` (pinned) and `apt-get update -qq && apt-get install -y
  poppler-utils`. The build REFUSES to start without them and exits 2. A gate that
  did not run is not a gate that passed. The 403s from unrelated third-party PPAs
  during that apt-get are harmless.
- The continuity ledger exists: `AIOM_Continuity_Ledger.md` plus `continuity.py`
  (G3, seven checks). It holds no entries, which is correct: entries append at
  Stage 9 and no chapter has locked. The ledger is the authority; never edit it to
  make a gate pass. Registry glosses are written by hand, and the placeholder
  deliberately fails the gate.
- To reopen a chapter use `reopen.py`, never `gen_checklists.py --force`. The
  latter destroys ticks and writes to `checklists/` rather than the chapter
  folder, which would fork a live checklist. Do not run `gen_checklists.py` in the
  repo root without cleaning up after it; generate to a scratch directory.
- Stage folders are on Process v2 numbering across all eighteen units. Voice is
  `05_Stage4_Voice_And_Craft_Check`, design is `06_Stage5_Design_Review`. Do not
  trust older paths in dated records.
- Build from a repo-root copy: copy the LIVE text
  (`Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`) to
  repo root, run `python3 AIOM_build.py <copy>.html --out <target>.pdf`, then
  remove the copy. Rasterize for visual review with `pdftoppm -png -r 150`.
  Building in place instead of from a root copy does not merely misrender, it
  renders a chapter that is not the book: the CSS link and the fonts resolve
  against the HTML's own directory, so the whole design system drops out and the
  gates report dozens of false defects (no folios, no running heads, DejaVu
  fallback faces, no provenance line). Two side effects to clean up after a build:
  `AIOM_build.py` writes `<name>.print.html` next to its input, and `.gitignore`
  only covers that file when the name begins with an underscore. Name the root
  copy `_ch01_build.html` and both files fall under the ignore rule.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- **NO SOURCE HOST IS REACHABLE FROM THIS ENVIRONMENT, so Stages 3 and 7 are
  structurally external, not external by preference.** Tested 2026-08-06:
  `cursor.com`, `techcrunch.com`, `github.blog`, `www.microsoft.com`, `doi.org`,
  and `x.com` all fail CONNECT with a gateway 403, recorded by the proxy as
  "policy denial". That is the network policy, not a bot block at the origin and
  not a TLS fault, so there is nothing to fix and nothing to work around. Verify
  with `curl -sS "$HTTPS_PROXY/__agentproxy/status"`, which lists recent relay
  failures by host. The practical consequence: Claude can rule on whether a
  chapter claim stays inside what a register note says, and cannot verify the
  note against the source. Do not offer to check a primary. Do not treat a
  register note as a substitute for one either; say which it is.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN; do not
  route around policy denials, report them.
- Develop on `claude/textbook-opening-rewrite-ac7yst`, then fast-forward `main` to
  match before ending the session. Both were synced at the close of 2026-08-06.
  Do not push to any other branch without Dan's explicit say-so. The earlier branches
  `claude/chapter-1-progress-fq0brc` and `claude/prose-voice-style-gxjkgj` are
  finished; do not add to them.
- **Confirm the live-text path before editing a chapter, not after.** This session
  applied a ruling to a superseded fork and had to revert it. HANDOFF.md names the
  live text; read it first, which is what CLAUDE.md section 11 already required.
