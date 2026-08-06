# Session handoff

Last updated: 2026-08-06. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session, alongside the voice and craft card.

## Repository state

Active working branch: `claude/chapter-1-progress-fq0brc`, new on 2026-08-06 and
replacing `claude/prose-voice-style-gxjkgj`, which is fully merged into `main` and
is finished. Working tree clean, and the branch is pushed to origin.

**`main` is merged and synced as of 2026-08-06.** Dan approved the merge and
`main` was fast-forwarded to match this branch, with nothing to reconcile because
`main` still carries no commits of its own. It now reflects the whole body of
work through Chapter 1 Stage 3 passed: both external fact checks, all six
findings ruled, the three applied rulings, and the current render. A specific SHA
is deliberately not recorded here, because it goes stale on the next commit and a
handoff that lies about sync state is worse than none. Check it instead.

Keep them synced. When this branch advances, fast-forward `main` again before
ending the session.

Verify state any time with:

```
git status                                              # working tree
git rev-list --left-right --count origin/main...HEAD    # main behind / ahead
python3 status_check.py                                 # authoritative status
```

The 2026-08-06 session, in full: Chapter 1 status confirmed at 4/13; the Stage 2
text rendered as the Stage 3 fact-check input; CLAUDE.md section 10, this file,
and the Workplan brought back into line with the checklist, which all three had
lagged; both external fact checks received, filed, and reconciled; all six Stage
3 findings ruled, three of them applied, and the record written; the input
re-rendered; Stage 3 marked passed by Dan; Stage 4 run and passed, with five of
its six findings applied and the second-model check waived; and Stage 5 run and
passed, closing both carried layout defects and four tooling defects. The three
records were mirrored at each step.

Seven prose edits landed on the chapter this session: SF1, SF2, SF3 at Stage 3,
and NC1, NC2, NC3, NC5 at Stage 4. Stage 5 then moved one callout and changed no
prose. Chapter 1 went from 4/13 to 7/13, and its render went from twelve of
fourteen gates to all fourteen.

The 2026-08-05 session, oldest first: the voice and craft standard (Decision 52);
the craft-check hardening after the first read failed as verification; the re-run
process plus the reopen of Chapter 1 (Decision 53); the continuity ledger
(Decision 54); the Chapter 1 Stage 0 re-draft; G1; Stage 1 (Decision 55); the
Stage 2 pass; and the Stage 2 rulings applied.

## What now lives in the repo

**Specs and standards.** Consolidated Spec (amended 2026-08-05 at Ch1 Stage 1,
each amendment marked with its date and reason), Addendum, Structure, Exit
Competencies, Maturity Model, Case Bank (now carrying CASE 4.6 and CASE 6.4),
Northmoor Dataset design, Workplan v5, Validation Matrix, and
`AIOM_Voice_and_Craft_v1.md` (new 2026-08-05, at v1.1).

**Build and design.** `AIOM_book.css` v6.7 plus the audit-only rule,
`AIOM_DESIGN_SPEC` v6.8, `AIOM_Design_QA_Spec` (updated 2026-08-05 to the
fourteen-gate suite), `AIOM_build.py` (fourteen gates plus a toolchain
preflight), `place.py`, `cite_format.py`, `footnotes.py`, and pinned
`requirements.txt`.

**Stage 6 round trip (new 2026-08-06).** `copyedit_export.py` turns the chapter
HTML into a copy-editing `.docx` plus a manifest recording every block's span in
the source; `copyedit_import.py` maps the returned file back, applying only what
it can place unambiguously inside a block's own span and refusing the rest. The
`.docx` is a proof, never a second live text: Decision 50 still holds. The source
register is excluded from the export by design.

**Process tooling.** `status_check.py` (lifecycle status, authoritative),
`gen_checklists.py`, `voicecheck.py` (mechanical bans plus per-section craft
metrics), `reopen.py` (new), `continuity.py` (new, gate G3),
`AIOM_Continuity_Ledger.md` (new), and `renumber_stage_folders.py` (new,
one-time, already run).

**Content.** Fonts committed under `fonts/`, the Northmoor dataset under
`Northmoor/`, Chapter 1 artifacts under `Drafts/Ch01_The_Category_Error/`, and
`archive/` for superseded files.

## Chapter 1 status: 8 of 13, through G2

Reopened at Stage 0 on 2026-08-05 (Decision 53) and re-drafted the same day
against the craft standard. Passed: Stage 0, G1, Stage 1, Stage 2, all
2026-08-05, and Stages 3, 4, 5 and G2 on 2026-08-06. `status_check.py` reports
8/13, STATUS CONSISTENT. The chapter is 19 pages and ALL FOURTEEN GATES PASS,
with both manual checks performed at 150dpi. Every step Claude owns before lock
is now done.

**The live text is
`Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`**, 5,961
words against a 6,000 ceiling, 39 words of headroom. It supersedes the old Stage
4 render, which is history. Stage 3 changed three sentences in it; see thread 1.

What each step produced:

- **G1** caught a real breach. The re-draft had put the published QJE agent count
  5,172 into prose, where a 2026-07-29 ruling reserves it for Chapter 6 and
  requires "on the order of five thousand" in Chapter 1. Fixed. The fuller ruling
  lives in the chapter's own Decision 51 register, NOT in the shorter
  `AIOM_Source_Ledger.md` note.
- **Stage 1** raised seven structural findings, all ruled (Decision 55). One
  changed an artifact: the case bank held no CASE 4.6 and no CASE 6.4 although
  the spec assigned both to Chapter 1, and both are now written in from
  already-cleared sources. Four amended the spec rather than the chapter. Two
  confirmed the chapter. Not one word of the chapter changed.
- **Stage 2** raised six findings. ND1 to ND4 were ruled and applied; ND5 and ND6
  closed with no action. Applying ND1 exposed a latent defect in gates 12 and 14,
  now fixed (see standing reminders).
- **Stage 3** ran two independent external checks on different prompts, which
  agreed on one finding out of six. SF1 to SF3 were applied, SF4 to SF6 closed
  with no chapter change. Every ruling is written into the chapter's own register
  note with the condition that would reverse it.
- **Stage 4** resolved all seven carried craft findings and raised six new, NC1
  to NC6, of which five are applied. It passed WITHOUT its second-model
  gut-check, which Dan ruled complete without.
- **Stage 5** closed both inherited layout defects and found four tooling
  defects doing it: one in gate 14 and three in `place.py`. No CSS changed and
  D0 stays closed.
- **G2** passed on a fresh build. It found the G2 box list itself was stale, a
  labelling inconsistency in the craft section that Stage 5 had missed (GD1,
  ruled and fixed), and a new coverage gap, G-I, where a floated callout can
  collide with a block panel and every gate still passes.

Carried items CD1 to CD7 are in the checklist and all are now closed. CD1 closed
at Stage 4 by a prose cut, CD6 at Stage 5 by placement, and CD7 as never having
been a defect at all.

## Open threads, in priority order

1. **Chapter 1 Stages 6, 7, and 8. DAN'S STEPS. Stage 6 is with Dan now.**

   Copy edit, final fact check 2, and the final read. Everything Claude owns
   before lock is done: the chapter is 19 pages, all fourteen gates pass, and both
   manual production checks were performed at 150dpi. The G2 render is committed
   at `Drafts/Ch01_The_Category_Error/07_G2_Production_Gate/AIOM_Ch1_G2.pdf`.

   **The Stage 6 proof was issued 2026-08-06** as
   `08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit.docx`, with its manifest beside it. When
   the edited file comes back, import it with
   `python3 copyedit_import.py <edited>.docx <manifest>.json <chapter>.html`,
   read the report, then re-run with `--apply`. It refuses anything it cannot
   place unambiguously; apply those by hand rather than loosening the tool. Then
   rebuild and re-run the gates, because a copy edit repaginates.

   **Before using the pair on any LATER chapter, round-trip the UNEDITED export
   and require zero reported changes.** That check found both bugs in the pair
   while it was being built, and neither was visible any other way.

   Two things to carry into those steps. Stage 7 is a source check and NO SOURCE
   HOST IS REACHABLE from a Claude session, so it is structurally external. And
   Stage 4 passed without its second-model gut-check, so if that read is ever run
   and disagrees, it enters as NC7 and reopens Stage 4.

   After them: **G3**, the continuity gate, which is Claude's and runs
   `continuity.py`. Then **Stage 9**, lock, also Claude's. Lock is not blocked.

   **An obligation booked for Stage 9, easy to lose:** when Chapter 1 locks,
   `continuity.py --update` must NOT record "flow" among the terms Chapter 1 owns.
   Chapter 2 owns it. Left unchecked, Chapter 2's proper definition registers as a
   redefinition and G3 fails Chapter 2 for a mis-logged ledger entry.

   **G2 passed 2026-08-06 and found three things worth carrying.** The G2 BOX LIST
   ITSELF WAS STALE: `gen_checklists.py` moved to a seventeen-box list on
   2026-08-05 but this chapter's checklist still had the old ten-box version,
   because `reopen.py` resets ticks and does not regenerate box text. After a
   reopen, check the box text against the generator, not only the ticks. GD1, a
   labelling inconsistency in the craft section's model inventory that Stage 5
   missed, was found by the manual raster review, ruled by Dan, and fixed by making
   all four steps inline bold, which also aligns the craft section with P2. And
   GAP G-I is new and open: a floated callout can collide with a following block
   panel, crushing a theorem panel's measure, while all fourteen gates pass. Until
   it closes, a chapter whose callout placement moves must have the affected pages
   READ, not merely gated.

2. **Remaining process hardening** (Dan approved, still to build):
   - `status_check.py` should verify that CLAUDE.md section 10 and the Workplan
     tracker agree with the checklist table. Those three have now been
     hand-mirrored across several sessions; the check would catch drift
     automatically.
   - Canonical `DECISIONS.md` with a status field per decision. Numbers are
     scattered across three files and now run to 55, with 47/48 flagged
     unverified.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout,
     though gate 11 now checks the panel directly.

3. **Chapter 2 (The Flow)** once the Chapter 1 re-draft has settled the craft
   standard in practice. Chapter 2 is the first chapter drafted under the
   standard from the start, so its Stage 0 acknowledgment box is a live
   requirement rather than a retrospective one.

4. **Decision 28**, Northmoor properties G, H, I. Gates the Ch9, Ch12, and Ch13
   problem sets only.

## Standing reminders

**Rules that bite.**

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
- Develop on `claude/chapter-1-progress-fq0brc`, then fast-forward `main` to match
  before ending the session. Do not push to any other branch without Dan's
  explicit say-so. The previous branch, `claude/prose-voice-style-gxjkgj`, is
  merged and finished; do not add to it.
