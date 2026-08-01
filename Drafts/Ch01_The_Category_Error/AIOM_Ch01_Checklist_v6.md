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

## Process v2 numbering

This chapter was drafted under Process v1 and renumbered to Process v2 on
2026-08-01. The section headers below use v2 numbers. Dated findings and the
chapter's HTML source block keep their original v1 labels; read them through the
CLAUDE.md section 8 mapping (v1 Stage 2 fact check is v2 Stage 3, v1 Stage 3
voice is v2 Stage 4, v1 Stage 4 design is v2 Stage 5, and so on). The
developmental edit, new in v2, is Stage 2.

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

Status: [x]        Date cleared: 2026-07-29

> Mechanical. Runs before Dan sees the chapter, so no reading time is spent on a draft with a defect a script could find.

- [x] All six slots present, in order, correctly headed
- [x] Opening case carries a provenance line under its title
- [x] Every exit competency assigned to this chapter is addressed
- [x] Every registry ID cited resolves against Locked Registry v1.3
- [x] Tier rules hold: one theorem callout, lemmas by ID, propositions by ID
- [x] Every empirical claim carries a citation
- [x] Source upgrade checked: most durable available form selected
- ~~Every perishable source captured to the Wayback Machine~~ REPEALED, D48
- ~~Every source filed in the local dark archive, named to the citation~~ REPEALED, D48
- [x] Every register entry carries original URL and access date
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

~~G1 CLOSED 2026-07-28. All ten checks pass. Draft v2, 5,669 words.~~

STRUCK 2026-07-28. That line was true against a ten-item gate. The gate now has
fourteen items: Decisions 39, 40, 40a, and 41 appended four archiving checks
after the line was written. Chapter 1 has never been run against those four.
The Perma.cc wording in the checkbox above was also superseded by Decision 40a
and has been reworded. G1 remains FAILED, on archiving only.

VERIFIED 2026-07-28 by `python3 sources.py check` against AIOM_sources.json:

    7 sources in the register
    1 ready, 6 blocked
    G1 cannot pass for any chapter citing a blocked source

Nothing has been captured. The `sources_archive/` directory does not exist. The
only ready source is brynjolfsson-2025-genai, which is marked non-perishable
and carries a DOI, so it needs no capture. Every other source is blocked:

- Five have no canonical URL at all: altman-2025-pro, anthropic-2025-limits,
  github-2025-premium, github-2026-usage, microsoft-2026-q2. All five also carry
  a pending upgrade note.
- truell-2025-pricing has its URL but no Wayback link, no local copy, and no
  access date.

FURTHER DEFECT FOUND 2026-07-28, larger than the checkbox contradiction. The
chapter is not wired to the register. AIOM_ch01.html contains zero
`<cite src="...">` tags. It carries five hand-written `<span class="fn">`
footnotes and one hand-written `<section class="sources">`, which are the output
form that `sources.py build` generates, not the input form it consumes.
Consequences:

1. Decision 41, generated citations, is not in force for this chapter. The
   apparatus was built but Chapter 1 never adopted it.
2. Running `sources.py build AIOM_ch01.html` now would resolve zero citations
   and append a second sources section, duplicating the one already there.
3. The citations are a divergent second copy of the register. This is the same
   failure mode as proof v14 against draft v2, and it will produce the same
   result if left.
4. The chapter asserts "Accessed July 28, 2026" six times. Per the capture
   worksheet, those dates record verification against the live record, not
   capture. The register overstates what has been done.

SOURCE WORK COMPLETED 2026-07-28. Wiring done and upgrades resolved.

Wiring: the chapter now carries five `<cite src="...">` tags resolving nine
citations. The hand-written footnotes and the hand-written sources section are
deleted. `sources.py build` generates both. The six false "Accessed July 28,
2026" claims disappeared on their own, because the register holds no access
dates. Nothing had to be remembered.

Register grew from 7 sources to 9. Two second paths were added under the
Decision 40 two-path standard.

Upgrades, all resolved:

- altman-2025-pro. Canonical post found. Snowflake ID decoded to settle the
  date: posted 2025-01-05 19:11 US Pacific, which is 2025-01-06 03:11 UTC. The
  book's January 5 is correct in US time and matches TechCrunch's same-day "on
  Sunday" report, but X displays January 6 outside the Americas. Recorded in the
  register so a fact checker explains it rather than "corrects" it. Second path
  added.
- anthropic-2025-limits. Canonical form is the X post, not a web page. Type
  changed from web to social, which also removes the duplicated "Anthropic,
  ... Anthropic" in the rendered note. Second path added, and it is not
  optional: the chapter's clause about limits introduced quietly earlier in July
  rests on it, not on the X post. That clause was previously uncited.
- github-2025-premium. Resolved differently from the worksheet, which called
  for a permalinked docs.github.com revision. A docs page describes the current
  state; the claim is about a change on a date. The GitHub Changelog entry of
  June 18, 2025 is the right artifact, and it matches the chapter's original
  footnote wording, "premium-request billing changelog".
- github-2026-usage. Canonical github.blog permalink found. No repo revision
  exists, since it is a blog post rather than a docs page. The worksheet's
  permalink advice applies to neither GitHub entry.
- microsoft-2026-q2. See Decision 46.

DECISION 46 (2026-07-28). Microsoft's IR transcript is accepted as the primary
source for the 4.7 million figure. The filing upgrade is not available: the
figure appears only in spoken remarks, the FY26 Q2 press release carries no
Copilot subscriber count, so the 8-K exhibit will not either, and Microsoft does
not break out product-level subscriber counts in the 10-Q. The transcript is a
first-party disclosure published by the party holding the data. Perishable, so
capture governs durability.

CORRECTION TO MY OWN WORK. The TechCrunch Altman piece was initially filed under
a byline inferred from TechCrunch's usual AI author. It was not verified. Both
TechCrunch entries are now filed to the publication, with a register note to
fill the author in at capture and not to guess it.

CARRIED TO STAGE 2. Nadella said "over 4.7 million"; the chapter says "reported
at 4.7 million", which understates.

CARRIED TO THE sources.py FIX LIST. Footnotes 3 and 4 render "post on x" and
"chatgpt pro" in lowercase. `note()` calls `ttl.lower()` on social titles. The
bug is in the code and cannot be fixed from the register.

~~REMAINING FOR G1: capture only.~~ STRUCK 2026-07-29 by Decision 48. Capture
is repealed. The `sources.py capture` step is retired and the blocking
condition in `sources.py check` must be narrowed accordingly. See the fix list.

G1 CLOSED 2026-07-29 against the ten-check gate as amended by Decision 48.
The gate was failed on the four archiving checks and on nothing else. Two of
those checks are repealed, one is satisfied already (upgrades were resolved
2026-07-28), and the fourth is satisfied once the access-date field alone is
required. No prose or structural defect remains outstanding at this gate.

Source pass completed. All five sources verified against the live record and
replaced with full citations. Three corrections were required:

CORRECTION 1 (fact error). The opening case attributed Cursor's repricing to the
upstream cost of serving heavy users. Truell's stated reason was different:
newer models spend more tokens per request on longer-horizon tasks, and Cursor
had been absorbing the difference. Corrected. The chapter's argument is
unaffected and arguably strengthened, since per-request intensity is a cleaner
instance of consumption economics than user skew.

CORRECTION 2 (attribution). The 4.7 million subscriber figure was cited to
GitHub. It is a Microsoft disclosure, from the FY26 Q2 earnings call of
January 28, 2026, four months before the June 1, 2026 billing transition.
Reattributed, with the gap noted in the bibliography.

CORRECTION 3 (dates). Vague dates pinned throughout: Cursor June 16 and July 4,
2025; Copilot June 18, 2025 and June 1, 2026; Altman January 5, 2025; Anthropic
announced July 28, 2025, effective August 28, 2025.

FLAG FOR STAGE 2. The QJE paper reports 5,172 agents and a 15 percent
productivity gain in the published version, against 5,179 and 14 percent in the
NBER working paper. The book must cite the published figures consistently. This
matters most at Ch6, where the study is the anchor case.

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

Status: [x]        Date cleared: 2026-07-29

> Is this the right chapter, not is it true. Read against the outline and the competency map. Structural findings only, no line edits.

Findings:

STAGE 1 PASSED 2026-07-29, against AIOM_ch01.html, read against Consolidated
Spec Part D.1 and the competency map. Run jointly, Dan ruling.

CONFORMS. All ten spec obligations for Chapter 1 are met:
- Six slots present and correctly ordered.
- Slot 1 pairs Cases 4.3 and 4.6 from the buyer's seat, opens on the surprise
  bill, closes on the purchase question. The pairing does the work Decision 1
  assigned it, preempting the "one badly run startup" dismissal.
- 1.1 delivers the software access model and the manages-versus-operates
  mismatch. 1.2 defines the consumption event and runs the anatomy, with
  Figures 1.1 and 1.2 at first exposure. 1.3 states the objection at full
  strength, answers it by meter relocation, and carries the THM-009 callout.
  1.4 delivers the supply-chain analogy, the absent discipline, and the stakes.
  1.5 is one paragraph, borders deferred to Ch3.
- Slot 3 runs the four-step inventory worked on the QJE contact-center
  deployment, planting the Ch6 anchor two chapters early as designed.
- Slot 4 is one paragraph in can-now-do form, not a recap.
- Slot 5 carries exactly the seven terms the spec names.
- Slot 6 carries three discussion questions in self-explanation register, plus
  P1 worked memo, P2 worked inventory, P3 completion.
- Competency C1 served. THM-009 is the only chapter-anchoring callout.
  Assessment 1 prepared by 1.1 to 1.3 plus P1; assessment 7 seeded.

ONE ITEM RULED. See Decision 49.

NO STRUCTURAL DEFECT FOUND. Stage 1 raised no rework. Three findings arose that
belong to Stage 2 and are carried, not counted against this stage.

---

## Stage 2. Developmental edit

Owner: Claude

Status: [~]        Date cleared: 

> Teaching quality, held early so its line edits do not churn fact check, voice, design, and production. Clarity, pacing, cognitive load, example fitness, transitions, and whether the argument carries the target reader without a stall. Claude runs a fresh critical pass; Dan gut-checks with a second model and rules.

Findings:

Added under Process v2 (2026-08-01). Chapter 1 predates this stage and is being
run retroactively. Claude ran the developmental pass 2026-08-01; findings below
AWAIT Dan's second-model gut-check and ruling. Nothing is applied. Any edit Dan
approves re-runs only its downstream steps per the scoped re-run matrix.

WHAT IS STRONG. The argument arc is clean (two vendors, category error, the two
economic models, the objection answered, what follows, borders). The steel and
goods-flow analogy is apt and on brand. Worked examples earn their place,
especially the CIO memo reply. Backward design is met: 1.1 to 1.3 plus P1 deliver
C1. The notes below lift the chapter from correct to maximally well taught.

FINDINGS, PRIORITIZED (for Dan to rule item by item):

D1 (HIGH). Section 1.4 carries too many distinct moves in about eight
paragraphs: the steel analogy, an informal five questions, the absent-discipline
point, three absences, inheritance not negligence, scale, and stakes. Two
enumerated lists (five questions, three absences) sit two paragraphs apart and
can blur. Recommend signposting the through-line or splitting 1.4.

D2 (HIGH). The seat-versus-event cost curves (now Figure 1.2) are the chapter's
big-idea visual (cost flat versus cost as area under use), but they land at the
end of 1.2 after the anatomy, while the big idea is stated in 1.1. Pedagogy
commitment is one strong figure per big idea at first exposure. Consider
anchoring the seat-versus-event contrast nearer 1.1. Interacts with the figure
order set 2026-08-01, so a judgment call, not a redo.

D3 (MEDIUM). The opening front-loads vendor mechanics (request counts, Sonnet
counting as two, the twenty-dollar pool, exact dates) before the reader has the
consumption-event frame. Consider lightening the opener to the shape of the
correction and letting Ch4 carry the granular numbers. Tension: the opener is a
dated case, where specifics are allowed, so a judgment call.

D4 (MEDIUM). The informal five questions in 1.4 are the same five posed formally
as the Founding Questions in Ch3. This may be deliberate withholding, which the
standing rules protect, or an accidental near-duplicate. Dan rules which; if
intentional, leave it, if not, a light this-book-will-return signal helps.

D5 (MEDIUM). The what-a-theorem-means aside in 1.3 interrupts the meter-relocation
momentum (necessary, first theorem in the book). Consider tightening it or
repositioning so the argument does not brake for a definitional aside.

D6 (LOW). Seven key terms is a heavy vocabulary load for a first chapter; confirm
each is load-bearing (likely locked by spec).

NEXT: Dan gut-checks with a second model, rules which findings to action. D1 and
D2 most affect how well the chapter teaches. On a ruling, Claude drafts the
specific edits for approval, then re-runs the downstream steps each edit touches.

D1 RULED AND RESOLVED 2026-08-01. Dan ruled: signpost and tighten, no split. The
section is correct and in band on length; the defect is enumeration blur and move
density, not length. Three edits applied to AIOM_Ch01_Stage4_FINAL.html, the
authoritative source:

- EDIT 1 (signpost), 1.4 paragraph 2. The five questions are now named as the
  same five practices recast, so the reader reads a concrete-then-abstract pairing
  rather than two independent lists. "The same five practices, stated in timeless
  form, are not techniques belonging to manufacturing. They are the questions ..."
- EDIT 2 (tighten), 1.4 paragraph 3. The third full re-enumeration of the five
  ("no practice yet sources ... plans ... records ... allocates ... holds") is
  compressed to "no practice yet assembles them under one vocabulary and one
  owner." The assembly and one-owner payoff is preserved; about 25 words drop.
- EDIT 3 (signpost), 1.4 paragraph 5. The three absences now open with "The
  failure to answer those questions is not abstract," bridging the five-to-three
  count shift as symptom of cause rather than a fresh list.

The five is now enumerated once in full (as practices), recast once as questions
with the link made explicit, and referred back to thereafter. The steel texture
in paragraph 1 is untouched.

D4 TOUCH NOTED. EDIT 1 moves the numeral "five" one paragraph earlier than it
previously appeared (paragraph 3 already said "the five questions"). This lightly
sharpens the tie to Ch3's five Founding Questions, which is D4's territory. If D4
is later ruled accidental, revisit this word.

DOWNSTREAM RE-RUNS (scoped re-run matrix, body prose edit):
- Stage 4 voice: RE-RAN 2026-08-01, PASS. voicecheck.py clean (0 em dashes, 0
  contractions, 0 stray question marks, 0 first or second person in body prose).
- Stage 5 design: RE-RAN 2026-08-01 on the post-D1 render, PASS. Callouts intact,
  figures on page 6 (section 1.2) untouched; first-pass visual review of pages 9
  to 11 shows no widows, orphans, or stranded heads, and the 1.4 head is well
  seated.
- G2 production: RE-RAN 2026-08-01, PASS. Full eleven-check suite green on the
  19-page re-render (page count unchanged).
- Stage 3 fact check (Dan): RULED PASS 2026-08-01 by Dan. Body prose changed but
  no empirical claim, citation, number, or figure changed, so the fact-checkable
  surface is untouched and the 2026-07-29 pass holds.

Stage 2 remains in progress: D2 through D6 await ruling.

---

## Stage 3. Source and fact check 1

Owner: Dan

Status: [x]        Date cleared: 2026-07-29

> Every empirical claim traced to primary source. Runs before voice and design so corrections do not churn later polish.

Findings:

STAGE 2 PASSED 2026-07-29, run by Dan against AIOM_ch01.html. The fact-check
record lives in the chapter's own source block (Decision 51): every source
verified live on its access date, bylines and dates confirmed by direct fetch,
and the raises resolved are logged there as items A2 to A7 and B1, B2 (for
example the Microsoft 4.7 million and 75 percent figures pinned to the Nadella
sentence, the Anthropic July 17 tightening given its own primary, the Cursor
date held at July 4, and the GitHub exceptions and all-plans scope verified).

The current Stage 4 render differs from that fact-checked draft only by the
Figure 1.1 and 1.2 reorder and reference fix, which is layout and touches no
prose, citation, or fact. Verified by diff 2026-08-01: the two files are
byte-identical outside those figure lines, so Stage 2 holds against the current
version.

---

## Stage 4. Voice check

Owner: Claude

Status: [x]        Date cleared: 2026-07-28

> Magisterial register: third person, no contractions, no em dashes, no rhetorical questions outside discussion prompts, no hedging. Also checks over-explanation below the reader baseline and under-explanation above it.

Findings:

STAGE 3 PASSED 2026-07-28, against AIOM_ch01.html. Run with voicecheck.py.

MECHANICAL, all clean on re-run after edits:
- Em dashes: 0.
- Contractions: 0.
- Question marks: 0 in the entire file, so no rhetorical questions arise.
- First or second person in unmarked body prose: 0.
- Hedging: one instance, "often read as" in discussion question 2. It reports
  how the episodes are commonly read rather than softening a claim of the
  book's. Not hedging. No change.

CARRIED ITEM FROM G1, RESOLVED. The contraction reported at line 149 of the
markdown draft inside quoted speech does not exist in the HTML. The CIO reply
runs "I am not asking," "we did not plan," "does not exist" throughout.
Verified against the HTML only. If the markdown draft is still live it may
still carry it, which is a further argument for the deletion Decision 36
already directs.

FOUR JUDGMENT ITEMS RAISED AND RULED. Decisions 42 to 45.

Decision 42. Voiced material. Body prose is third person. First or second
person is permitted only in material marked as voiced, either by a block class
(model, dq, problem) or by enclosing quotation marks. Applied: the flat-rate
objection in 1.3 now takes quotation marks. Quotation marks were preferred over
recasting to third person because the paragraph's stated purpose is to put the
objection at full strength, which third person would drain. Standing rule for
all fifteen chapters.

Decision 43. Reader address. Second person is permitted in discussion questions
and problems. "The reader" holds everywhere else. NO EDIT REQUIRED. On
re-examination the chapter was already consistent: all three discussion
questions and all three problems use imperative address, and questions 1 and 3
additionally use a second-person possessive where they refer to the reader's
own organization. Question 2 needs no such possessive. The inconsistency
reported at the time of the ruling was not real.

Decision 44. Definition restatement. A definition given in a definition aside
is not restated verbatim in body prose; the body names the term instead.
Applied: the consumption-event definition appeared verbatim three times (aside,
body, Key Terms) where access price and software access model each appeared
once with a naming sentence in prose. The body restatement is cut to "That unit
is the consumption event." Now two occurrences, both apparatus, matching the
other two definitions.

Decision 45. Token gloss. "Token" carried substantial load from the opening
case onward and was never explained. A short appositive gloss is added at the
anatomy paragraph in 1.2, where the concept starts doing work, rather than at
the opening case where it is incidental: "the units into which a model divides
the text it reads and writes." Conditional on the preface not assuming the term.
The preface does not yet exist. See chapter notes.

WORD COUNT after edits: 5,362 by HTML text extraction. In band per Decision 33.
Note this counts differently from the 5,669 recorded for markdown draft v2. Both
are in band; the delta is extraction method, not text loss.

CONSEQUENCE. These are prose edits, so Stage 4 and Gate G2 revert to not run.

---

## Stage 5. Design review

Owner: Claude

Status: [x]        Date cleared: 2026-08-01

> Blocked until D0 closes. Layout, figures, typography, running heads, callout placement, key-term register, against the locked design system.

Findings:

Passed provisionally 2026-07-28. REVERTED to not run on the same date, because
Stage 3 made prose edits in sections 1.2 and 1.3. A design review that passed
against superseded prose has not passed. Re-run after the render.

Re-run 2026-07-31 on the Stage 4 render (AIOM_Ch01_Stage4), per Dan: design
review passed.

REVERTED again 2026-07-31, same day, by the Figure 1.2 reference fix. The two
section 1.2 figures were reordered (anatomy becomes Figure 1.1, seat and event
becomes Figure 1.2) so both are referenced in figure order. That is a figure and
prose edit, so Stage 4 and G2 revert and must re-run against the next render.

Re-run 2026-08-01 on the re-render carrying the figure fix: design review
passes. The two section 1.2 figures now appear and are referenced in order
(anatomy is Figure 1.1, seat and event is Figure 1.2), callouts are intact, and
the mechanical gates confirm the layout under G2 below.

---

## Gate G2. Production gate

Owner: Claude

Status: [x]        Date cleared: 2026-08-01

> Mechanical, run on the rendered PDF.

- [x] Renders under WeasyPrint without error or warning
- [x] Zero overflow: all character bounds inside the text block
- [x] Running heads correct and correctly sided on every page
- [x] All figures present, numbered, captioned, referenced in text
- [x] Figure geometry validated by pixel sampling (gap G-B; first-pass visual review 2026-08-01, p6 figures correct and in order; Dan final sign-off)
- [x] Callout placement correct: no splits, ordering correct after place.py
- [x] Footnotes on correct pages, numbering sequential and unbroken
- [x] Key-term register renders with correct rule and tint alternation
- [x] No widows, no orphans, no section head stranded at a page foot (gap G-D; first-pass visual review 2026-08-01, none seen; Dan final sign-off)
- [x] Rasterized visual sample reviewed at page level (19 pages rasterized and reviewed 2026-08-01, first pass by Claude)

Findings:

Passed provisionally 2026-07-28. REVERTED to not run on the same date, for the
same reason as Stage 4.

DEFECT FOUND AT STAGE 3, to be fixed before G2 re-runs. Figure 1.2 is never
referenced in body prose. The caption is present and correctly numbered, and
the figure renders, but no sentence points the reader at it. Figure 1.1 is
referenced correctly in the closing paragraph of 1.2. The checkbox "All figures
present, numbered, captioned, referenced in text" was marked passed on the
provisional run and should not have been. Fix: add a reference to Figure 1.2,
most naturally in the anatomy paragraph of 1.2 that the figure illustrates.

RESOLVED IN SOURCE 2026-07-31, pending re-render. Rather than only add a
reference, the two section 1.2 figures were reordered so they appear and are
referenced in figure order. The anatomy figure is now Figure 1.1, referenced in
the anatomy paragraph it illustrates; the seat-and-event figure is now Figure
1.2, referenced in the closing paragraph of 1.2. Both figures are now referenced
in body prose, in order. G2 confirms this against the next render.

PASSED 2026-08-01 on the re-render (19 pages). AIOM_build.py ran the full
automated suite and all eleven checks passed: right-margin overflow 0; em and en
dashes 0; heads and folios present and correctly sided; definition callout
splits 0 (place.py not needed); font faces the six expected only; key terms 7
fields and 7 header bands; opening-case provenance present; footnotes 6 called
and all on the calling page; dated evidence boxes 2 labelled and 2 hairline rules
at 2px; problem labels 3 all with their title; theorem panel intact.

One CSS fix was required to reach this pass: the committed v6.7 CSS lacked a rule
to hide the audit source block (Decision 51 apparatus, marked class="audit-only"
by the build), so the raw JSON block rendered as monospace and overflowed. A
rule "#aiom-sources, .audit-only { display: none; }" was added to AIOM_book.css.
The committed CSS predates Decision 51. Ruled 2026-08-01: the committed CSS
(v6.7 plus this audit-only rule) is the working version of record; no external
CSS reconciliation is pending.

The three items outside the automated suite were given a first-pass visual review
2026-08-01 against the 19 rasterized pages: figure geometry is correct (the two
section 1.2 figures render cleanly and in order on page 6), and no widows,
orphans, or stranded heads were seen. Final visual sign-off remains Dan's. The
chapter is 19 pages, up from the prior 18; the added figure reference and the
page footnotes shifted pagination.

---

## Stage 6. Copy edit

Owner: Dan

Status: [ ]        Date cleared: 

> Line level, on prose that has stopped moving. Decision 24 places this late. Revisit the placement after Chapter 4.

Findings:

---

## Stage 7. Final fact check 2

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

## Stage 8. Final read

Owner: Dan

Status: [ ]        Date cleared: 

> The chapter read whole, typeset, at reading pace, in one sitting. Pass or fail on the whole, per Decision 30. No lists of small fixes. A failure names one structural reason and the chapter returns to the stage that owns it.

Findings:

---

## Stage 9. Locked

Owner: Claude

Status: [ ]        Date cleared: 

> Frozen. Continuity ledger committed. No change without an explicit reopen, which re-runs every stage from the one that owns the change.

Findings:

---

## Chapter notes

Open items, deferrals, and anything a later chapter needs to know.

~~OPEN, UNRULED. G1's marker and G1's findings contradict each other.~~
RESOLVED 2026-07-29 by Decision 48. The contradiction was real and the reading
recorded here was correct: G1 was failed on the archiving checks only. Decision
48 repeals those checks, so the contradiction dissolves rather than being
adjudicated. The struck "G1 CLOSED 2026-07-28" line stays struck, because it
was written against a ten-check gate that is not the ten-check gate now in
force. The current closure is dated 2026-07-29 and stands on its own.

~~OPEN. Source count discrepancy.~~ RESOLVED 2026-07-29. The register holds
nine sources after the two second paths added 2026-07-28 under Decision 40's
two-path standard. The "five sources" figure predates the wiring pass and the
"seven" figure predates the second paths. Nine is current. NOTE: Decision 40 is
repealed by Decision 48 as to capture, but its two-path standard is not
disturbed. Confirm that reading at Stage 2.

CARRIED TO STAGE 2. The QJE paper reports 5,172 agents and a 15 percent
productivity gain in the published version, against 5,179 and 14 percent in the
NBER working paper. The book cites the published figures consistently. Matters
most at Ch6, where the study is the anchor case.

~~CARRIED TO STAGE 1 (Dan). Spec 1.3 calls for the OpenAI Pro and Anthropic
episodes as dated case boxes.~~ RESOLVED 2026-07-29 by Decision 49. The premise
was also partly wrong as recorded: the episodes are not inline prose. They are
already dated blocks with a date label and cite wiring.

CARRIED TO THE PREFACE. Decision 45 added a token gloss in 1.2 on the condition
that the preface does not already assume the term. The preface does not yet
exist. When the reader-assumptions subsection is written, check for redundancy
against this gloss.

CARRIED TO STAGE 5. Page range in the Brynjolfsson, Li, and Raymond entry is
set with a hyphen (889-942). Chicago 17 takes an en dash. Copy-edit item, not a
voice item.

FOR CH2. Chapter 1 closes by promising that Chapter 2 takes the atomic unit
defined here and asks what becomes visible when many events are seen together.
Chapter 2 also owes LEM-005 per Decision 27, production is operated rather than
merely accessed. The summary's stated handoff is "seeing the deployment as flows
rather than events."

DECISION 47 (2026-07-29). Sourcing is chapter-local. Each chapter carries its
own source list, resolved and closed when the chapter locks rather than deferred
to a pre-print pass. The book-wide primary-source chase list in Consolidated
Spec Part H is struck. Rationale: chapters are drafted weeks apart, and a
deferred book-wide list cannot survive that cadence. The register remains the
single store; chapter-local means the work closes per chapter, not that each
chapter keeps a separate register.

DECISION 48 (2026-07-29). No capture. A source is sufficiently sourced when it
is cited to a primary, verified live on the accessed date, and cleared by two
independent fact checks against that source. Wayback capture and the local dark
archive are repealed.

  REPEALS: Decision 39, Decision 40 as to capture and local archiving, and
  Decision 40a in full. Decision 40's two-path standard survives; confirm.
  AMENDS: Gate G1 from fourteen checks to ten.
  AMENDS: the internal A/B/C source grading is retired. One operative rule
  survives, that an aggregator or vendor page is never cited, only the primary
  it points to.
  CODE CONSEQUENCE: `sources.py check` currently blocks on three fields,
  Wayback link, local copy, and access date. It must block on access date only.
  Until that change lands, `check` will report false blocks. On the fix list.

  KNOWN COST, ACCEPTED. Accessed dates now carry the whole durability burden.
  A reader in 2040 holding a citation to a Cursor blog post or a GitHub docs
  page already marked legacy will find a dead link. Normal for academic books
  and no reviewer will fault it. Record it plainly in the method note: web
  sources were verified live at drafting and were not archived.

DECISION NUMBERING WARNING. 47 and 48 were assigned against a log whose highest
seen entry is 46. If any session landed a decision above 46, renumber before
this file is treated as authoritative.

CARRIED TO STAGE 2, STATUS UNKNOWN. Nadella said "over 4.7 million"; the
chapter reportedly says "reported at 4.7 million", which understates. A fix was
applied 2026-07-29 but only to a markdown fork, not to AIOM_ch01.html. Treat as
UNFIXED until verified against the HTML.

FORK WARNING, 2026-07-29. A markdown draft v2, a standalone Ch1 source list,
and a markdown source ledger were generated this date from stale project
knowledge. All three are divergent second copies of AIOM_ch01.html and
AIOM_sources.json. Discard them.

RESOLVED 2026-07-29. The three uncertain items were checked against the live
HTML. All three are real and all three survive in the chapter. See the Stage 2
carried items below.

DECISION 49 (2026-07-29). The dated block stands; the spec is amended. Chapter 1
keeps the OpenAI Pro and Anthropic episodes as `div.dated` blocks with a date
label and cite wiring. They are not promoted to case boxes.

  REASONING. The case box's defining feature is its evidence-taxonomy tag, and
  the taxonomy is introduced in Ch6. An untagged box in Ch1 imitates the device
  without being it; a tagged box forward-references vocabulary the reader meets
  five chapters later. The two blocks are also not cases: they run forty-five
  and forty-seven words against the spec's two-to-three-page definition, and
  Ch1 already has its case in the Cursor and Copilot pairing, which Decision 1
  built to be the chapter's evidentiary center of gravity. A third case-like
  object would dilute it. Importing the device early would additionally oblige
  Ch2 through Ch5 to use it, or leave Ch1 an orphan.

  SPEC AMENDMENT REQUIRED. Consolidated Spec Part D.1, Chapter 1, section 1.3
  reads "Evidence in dated case boxes." Amend to "Evidence in dated blocks."
  The collision between that wording and Ch6's tagged case box is what sent
  this item to Stage 1 in the first place; leaving it will re-fire at every
  future read of Part D.1 against a draft. Amend once, in Drive, and resync.

  SCOPE. Ch1 only as to placement. The naming fix is book-wide vocabulary.

CARRIED TO STAGE 2, THREE ITEMS, all verified present in AIOM_ch01.html on
2026-07-29:

1. "Two quiet steps." The chapter describes GitHub's second act as quiet. It
   was announced on 2026-04-27 by GitHub's Chief Product Officer on the company
   blog, six weeks before it took effect, with a preview-bill tool shipped in
   advance. The apology-versus-no-apology contrast the sentence wants survives
   without the word. Note that "quietly" is used accurately elsewhere, in the
   cite note on the Anthropic block, where the July 17 tightening genuinely
   carried no announcement.

2. "Reported at 4.7 million." Nadella said "over 4.7 million." The chapter
   understates. Previously carried, still unfixed, now confirmed against the
   HTML rather than a fork.

3. Anthropic sequence in the second dated block. The block reads that Anthropic
   "introduced usage limits ... and then announced weekly caps." The five-hour
   rolling limits predate July; 17 July was a tightening of limits already in
   force, not an introduction. The cite note on the same block states the
   sequence correctly, so the block contradicts its own footnote.

AVAILABLE, NOT A DEFECT. The GitHub announcement states in the provider's own
voice that under the retiring model a brief chat question and a multi-hour
autonomous session could cost the user the same, and that the arrangement was
no longer sustainable. The chapter does not use it. This is a provider stating
the chapter's thesis in the first person, which is stronger evidence than the
book's own restatement of it. Content decision, not a correction. Raise at
Stage 2 or leave to Stage 5.

DECISION 50 (2026-07-29). Version control. AIOM_ch01.html is the single source
of truth for Chapter 1, and the same rule holds for every chapter.

  1. HTML IS AUTHORITATIVE. Markdown drafts are scaffolding. Once a chapter
     reaches HTML with cite wiring, every prior markdown is dead and is
     deleted, not archived. Decision 36 already said this and was not
     enforced; it is now a gate condition.
  2. NO VERSION NUMBER IS REUSED ACROSS FORMATS. The HTML carries the version
     and the PDF inherits it: AIOM_ch01_v19.html renders AIOM_Ch1_v19.pdf. If
     those two numbers disagree, stop and reconcile before any stage runs.
  3. CLAUDE DOES NOT WRITE CHAPTER PROSE TO MARKDOWN. Proposed prose goes in
     chat or as a patch against the HTML, never as a file that could be
     mistaken for a draft.
  4. FINGERPRINT BY HASH, NOT WORD COUNT. This chapter reads as 5,116, 5,362,
     or 5,437 words depending on extraction method. Three numbers, one
     chapter. Record the SHA-256 prefix when citing a version.

  ESTABLISHED 2026-07-29 BY HASH. Three distinct artifacts existed, not two
  competing versions of the prose:
    b6815af1de07  draft_v1.md            4,557w  dead ancestor
    4460505bc580  "draft_v2".md          4,736w  CLAUDE FORK, delete on sight
    335af891e698  AIOM_ch01.html         5,116w  LIVE
  The three markdown uploads were byte-identical to each other and to the fork
  generated 2026-07-29 from draft_v1. The two HTML uploads were byte-identical.
  Body prose in the PDF matches the HTML; the apparent sentence-level diff is
  hyphenation and running heads.

  ROOT CAUSE: filename collision. A legitimate AIOM_Ch1_draft_v2.md (5,216w,
  the 1.4 expansion) existed and was superseded into the HTML. Claude then
  generated a different file from draft_v1 and gave it the same version number.
  One version number, two lineages. That file is what reached the fact
  checkers, which voided a large share of their findings.

PDF v18 IS STALE. Superseded 2026-07-29. Its bibliography carries seven entries
and no TechCrunch; the HTML register carries nine sources with two-path
citations on altman-2025-pro and anthropic-2025-limits. v18 therefore predates
the source pass of 2026-07-28. Consequences:
  - Any design or production review conducted against v18 is void. Stage 4 and
    G2 were already reverted to not run, so no gate is affected.
  - A re-render is required before Stage 4 and G2 can run. Next render is v19.
  - The v18 footnotes also lack the second paths, so footnote numbering and
    content will change at re-render.
