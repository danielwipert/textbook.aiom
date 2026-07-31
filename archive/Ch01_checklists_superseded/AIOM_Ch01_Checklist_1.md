# Chapter 1: The Category Error

Editorial checklist.

Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

Stages run in order. A chapter is not Locked until every stage above has
passed. Stages 5, 6, and 7 are all external and may be run in one sitting.
Stage 1 may not be batched with them: it runs early or it is worthless.

Gates are mechanical and stop the chapter where it stands. Passes are judgment.

Standing rules at every stage: no em dashes; every empirical claim cited or
cut; six-slot skeleton without exception; theorems are the only chapter
anchoring callouts.

---

## Stage 0. Draft

Owner: Claude

Status: [x]        Date cleared: 2026-07-28

> Against the chapter outline and the fixed six-slot skeleton. Sources archived at drafting time.

Findings:

Draft complete, 4,557 words, 167 lines.

---

## Gate G1. Structural gate

Owner: Claude

Status: [!]        Date cleared: 

> Mechanical. Runs before Dan sees the chapter, so no reading time is spent on a draft with a defect a script could find.

- [x] All six slots present, in order, correctly headed
- [x] Opening case carries a provenance line under its title
- [x] Every exit competency assigned to this chapter is addressed
- [x] Every registry ID cited resolves against Locked Registry v1.3
- [x] Tier rules hold: one theorem callout, lemmas by ID, propositions by ID
- [ ] Every empirical claim carries a citation; every source archived
- [x] Every Slot 5 key term appears defined in the body
- [x] Zero em dashes
- [x] Word count inside the chapter target band
- [x] Gloss-less lemmas carry a book-authored gloss, marked as such

Findings:

G1 FAILED on 3 of 10. Verified 2026-07-28 against the draft and Registry v1.3.

PASS
- Six slots present and correctly ordered, plus a working sources appendix.
- Competency C1 addressed: 1.1, 1.2, and 1.3 map to it directly.
- THM-009 resolves. Quoted text matches the registry formal_statement verbatim.
- Tier rules hold: exactly one theorem callout, no lemmas or propositions cited.
- Zero em dashes across the whole file.
- No gloss-less lemma cited, so no gloss required.

FAIL 1. No provenance line under the opening case title. The draft carries a
status note under the chapter title instead. Provenance lines under opening case
titles are a locked design element.

FAIL 2. Sources cited but not archived. All five carry the marker "Primary
source to be archived at citation pass; chase-list item." Archiving was
explicitly deferred at drafting. It has to close before stage 2.

FAIL 3. Key term "Meter relocation" is defined in Slot 5 but the phrase never
appears in the body. Section 1.3 argues the concept without naming it. Either
name it in 1.3 or drop it from the register.

RESOLVED 2026-07-28 in draft v2 (AIOM_Ch1_draft_v2.md):
- Provenance line added under the opening case title.
- "Meter relocation" now named in 1.3; key term no longer orphaned.
- Section 1.4 expanded to the spec outline: supply-chain analogy in its timeless
  form, the three absences, absence as inheritance rather than negligence, scale
  as what ends the arrangement, and the stakes. Word count 4,557 to 5,216.
- Decision 33 sets Ch1 and Ch2 at 5,000 to 6,000 words. 5,216 is in band.
- Re-verified: zero em dashes, all seven key terms present in body.

STILL OPEN. Source archiving. G1 cannot close until the five sources are
captured. Stage 2 cannot run without them.

CARRIED TO STAGE 1 (Dan). Spec 1.3 calls for the OpenAI Pro and Anthropic
episodes as dated case boxes (Cases 4.1 and 4.2). Draft runs both as inline
prose. Case-box treatment is formally introduced in Ch6, so whether Ch1 uses the
device is a content and design question, not a G1 failure.

CARRIED TO STAGE 3 (voice). One contraction survives at line 149, inside quoted
speech attributed to a board member. Quoted speech is arguably outside the
body-prose rule. Needs a voice-check ruling.



---

## Stage 1. Content review

Owner: Dan

Status: [ ]        Date cleared: 

> Is this the right chapter, not is it true. Read against the outline and the competency map. Structural findings only, no line edits.

Findings:

---

## Stage 2. Source and fact check 1

Owner: Dan

Status: [ ]        Date cleared: 

> Every empirical claim traced to primary source. Runs before voice and design so corrections do not churn later polish.

Findings:

---

## Stage 3. Voice check

Owner: Claude

Status: [ ]        Date cleared: 

> Magisterial register: third person, no contractions, no em dashes, no rhetorical questions outside discussion prompts, no hedging. Also checks over-explanation below the reader baseline and under-explanation above it.

Findings:

---

## Stage 4. Design review

Owner: Claude

Status: [ ]        Date cleared: 

> Blocked until D0 closes. Layout, figures, typography, running heads, callout placement, key-term register, against the locked design system.

Findings:

---

## Gate G2. Production gate

Owner: Claude

Status: [ ]        Date cleared: 

> Mechanical, run on the rendered PDF.

- [ ] Renders under WeasyPrint without error or warning
- [ ] Zero overflow: all character bounds inside the text block
- [ ] Running heads correct and correctly sided on every page
- [ ] All figures present, numbered, captioned, referenced in text
- [ ] Figure geometry validated by pixel sampling
- [ ] Callout placement correct: no splits, ordering correct after place.py
- [ ] Footnotes on correct pages, numbering sequential and unbroken
- [ ] Key-term register renders with correct rule and tint alternation
- [ ] No widows, no orphans, no section head stranded at a page foot
- [ ] Rasterized visual sample reviewed at page level

Findings:

---

## Stage 5. Copy edit

Owner: Dan

Status: [ ]        Date cleared: 

> Line level, on prose that has stopped moving. Decision 24 places this late. Revisit the placement after Chapter 4.

Findings:

---

## Stage 6. Final fact check 2

Owner: Dan

Status: [ ]        Date cleared: 

> Narrower than stage 2. Targets what changed since it, confirming nothing broke in revision.

Findings:

---

## Gate G3. Continuity gate

Owner: Claude

Status: [ ]        Date cleared: 

> Mechanical, against the running continuity ledger. Catches chapter to chapter drift here rather than at manuscript integration, where the fix would mean reopening a locked chapter.

- [ ] No term redefined that an earlier chapter already owns
- [ ] Every forward reference assigned to this chapter is paid
- [ ] Every forward reference this chapter makes is logged
- [ ] Northmoor figures diffed against generator output
- [ ] Registry IDs logged; recurring glosses worded identically
- [ ] Maturity ladder language consistent with the locked five-stage model
- [ ] Founding Question references match the canonical table exactly
- [ ] Ledger updated on lock

Findings:

---

## Stage 7. Final read

Owner: Dan

Status: [ ]        Date cleared: 

> The chapter read whole, typeset, at reading pace, in one sitting. Pass or fail on the whole, per Decision 30. No lists of small fixes. A failure names one structural reason and the chapter returns to the stage that owns it.

Findings:

---

## Stage 8. Locked

Owner: Claude

Status: [ ]        Date cleared: 

> Frozen. Continuity ledger committed. No change without an explicit reopen, which re-runs every stage from the one that owns the change.

Findings:

---

## Chapter notes

Open items, deferrals, and anything a later chapter needs to know.
