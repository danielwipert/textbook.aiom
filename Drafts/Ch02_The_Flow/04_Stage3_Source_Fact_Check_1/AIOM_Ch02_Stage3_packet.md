# Chapter 2, Stage 3. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 3 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch02_The_Flow/00_Stage0_Draft/AIOM_Ch02_draft.html`
RENDER         `Drafts/Ch02_The_Flow/04_Stage3_Source_Fact_Check_1/AIOM_Ch02_Stage3_render.pdf`, built this session, all fifteen gates green.

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. This chapter carries 8 ruling(s) already
made and still in force, recorded in `AIOM_Claim_Ledger.md` and in the
register notes below. A checker who reaches one should say whether the
condition named in the note is now met, not restate the finding.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    5 keys defined, 5 cited. 0 orphan(s), 0 dangling.
  Citation markers    7 cited passages, every marker resolving to a key.
  Footnote build      9 footnote(s) generated. Gate 8 checks each sits on its calling page and passed on the render above.
  Ruled-form check    8 ruling(s) in force for Ch02: 9 required, 8 forbidden,
                      1 by reading. `claimcheck.py` reports PASS.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> In April 2026, four months into the calendar year, press reporting indicates that Uber had spent the annual budget it had set for artificial intelligence. Nothing had broken. No contract had been renegotiated and no vendor had raised a price. The engineers were doing the work the company had asked them to do, with the tool the company had given them.

CITES: `uber-2026-budget`

IN-CHAPTER GLOSS: Reported timing of the budget exhaustion.

### C2

CLAIM TEXT AS IT STANDS

> The tool was Claude Code, an assistant that writes and edits software, and the company had begun rolling it out to roughly five thousand engineers in December 2025. Adoption moved quickly. By February, about a third of the engineering organization was using it. Within a further month it had reached a large majority.

CITES: `uber-2026-budget`, `uber-2026-adoption`

IN-CHAPTER GLOSS: Engineer count and rollout timing.

### C3

CLAIM TEXT AS IT STANDS

> By the measures an engineering organization normally applies, the rollout was going well. The tool was adopted and it was used heavily. Reporting indicates that by spring a large share of committed code had passed through it. Those measures establish adoption. They do not establish value, and the difference between the two is most of what this chapter is about.

CITES: `uber-2026-adoption`

IN-CHAPTER GLOSS: Reported share of committed code.

### C4

CLAIM TEXT AS IT STANDS

> What the engineers were consuming did not hold flat. Reported monthly costs ran from several hundred to a few thousand dollars per engineer, varying with how much each one worked and how hard the work was. The rate was not the surprise. Spending rose as adoption spread and as per-engineer consumption varied, and the commercial terms turned that variable consumption into variable cost.

CITES: `uber-2026-budget`

IN-CHAPTER GLOSS: Reported per-engineer monthly cost range.

### C5

CLAIM TEXT AS IT STANDS

> Two things about this episode are worth separating, because they are usually confused. The first is that the company could see what it was spending. The billing arrived and accumulated, and by April the total had reached the figure that had been set aside. The second is that the company could not say what it had received. The chief operating officer was publicly asking whether the spending had been worth it. That question suggests a documented return was unavailable, incomplete, or unpersuasive to senior leadership.

CITES: `fortune-2026-uber-coo`

IN-CHAPTER GLOSS: Reported executive commentary on whether the spending was justified.

### C6

CLAIM TEXT AS IT STANDS

> The pattern is not confined to one company. A 2025 study of enterprise deployments by MIT NANDA reported a striking gap. Ninety-five per cent of enterprise generative AI pilots delivered no measurable impact on profit and loss. A far higher share of organizations reported that they had piloted or deployed such tools. The figure attracted substantial methodological criticism after it circulated, and the study’s reported interview counts differ across accounts of it.

CITES: `mit-nanda-2025`, `mit-nanda-2025`

IN-CHAPTER GLOSS: Reported headline finding and adoption figures.

### C7

CLAIM TEXT AS IT STANDS

> Between January and June 2024 the Australian Government ran a whole-of-government trial of Microsoft 365 Copilot. Around sixty agencies took part. Each agency nominated the staff who would receive licences, and several thousand licences were issued. The licence is priced per seat rather than by unit of use. The Digital Transformation Agency commissioned an independent evaluation and published it in full. Participants reported using the tool a few times a week or less, and reported time savings from using it. The evaluation states two things about its own method: participants assessed the effects themselves, which may understate or overstate them, and no measure of the work existed from before the trial began.

CITES: `dta-copilot-2024`

IN-CHAPTER GLOSS: Trial period, participating agencies, licence allocation, and the evaluation’s statements about its own method.

---

## Part 2. Register entries, verbatim

### `dta-copilot-2024`

- **type**: report
- **title**: Evaluation of the whole-of-government trial of Microsoft 365 Copilot
- **container**: Australian Government Digital Transformation Agency
- **date**: 2024
- **perishable**: False
- **upgrade**: The published evaluation itself, which the Digital Transformation Agency released in full and which nobody on this project has read.

NOTE, verbatim:

> UNVERIFIED. Found by WebSearch on 2026-08-22 for problem P3, after Dan ruled at Chapter 2 Stage 1 that competency C2 needs a mapping exercise on a cited real deployment and that the constructed insurer would not serve. Claude read search result summaries and did NOT read the evaluation, any article about it, or any agency page: WebFetch and curl are blocked by the container egress proxy. Grade C. THE SECONDARY COVERAGE DISAGREES WITH ITSELF ON EVERY COUNT, which is why the problem states none of them precisely. Agency counts of 56, almost 60 and more than 60 all appear; participant and licence counts of more than 5,000, 5,765, nearly 6,000 and 7,600 all appear. The problem says ’around sixty agencies’ and ’several thousand licences’ deliberately, so that a corrected count does not invalidate the exercise. WHAT IS LOAD BEARING IS NOT A COUNT. The problem rests on four things: that the licence is priced per seat rather than by unit of use, that agencies nominated their own participants, that an independent evaluation was commissioned and published, and that the evaluation stated both that participants self-assessed the effects and that no pre-trial measure of the work existed. STAGE 3 MUST CONFIRM THOSE FOUR AND MAY LEAVE THE COUNTS ALONE. It should also settle the publication date, which is recorded here as the year only because no source read gave a day, and record whether the evaluation is attributed to Nous Group on its face, since secondary coverage names that firm as the evaluator. ACCESS DATE NOT REQUIRED: a fixed published report, the same convention applied to mit-nanda-2025.


### `fortune-2026-uber-coo`

- **type**: news
- **title**: Uber burned through its entire 2026 AI budget in four months
- **container**: Fortune
- **date**: 2026-05-26
- **url**: https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/
- **perishable**: True
- **accessed**: 2026-08-21
- **upgrade**: Direct quotation of the executive, with venue and date.

NOTE, verbatim:

> UNVERIFIED. Supports the claim that a senior executive publicly questioned whether the spending was justified. THE CHAPTER’S ARGUMENT LEANS ON THIS MORE THAN ON ANY FIGURE, because the executive’s question is the evidence that the value half of the flow was unbuilt. If Stage 3 cannot confirm it, the paragraph and problem P1 both need rework rather than a looser number.


### `mit-nanda-2025`

- **type**: report
- **title**: The GenAI Divide: State of AI in Business 2025
- **container**: MIT NANDA
- **date**: 2025-08
- **perishable**: False
- **upgrade**: The report PDF itself, which the case bank records as not yet obtained.

NOTE, verbatim:

> UNVERIFIED, and carried from CASE 6.2 in the case bank rather than from new research. Ruled into the Chapter 2 teaching body by Dan on 2026-08-21. HANDLE WITH CARE per the bank: the ninety-five per cent figure circulated widely and drew methodological criticism, and reported interview counts vary across accounts. The chapter states the criticism once, plainly, per the straight-spine evidence policy, and rests its argument on the phrase ’no measurable impact’ rather than on the figure’s precision. Stage 3 should obtain the report and confirm the wording of the headline finding. ACCESS DATE NOT REQUIRED: the report is non-perishable, and the Chapter 1 convention is that a fixed document cited by a stable identifier needs no access date. What it still needs is its location, which the case bank records as not yet obtained. Stage 3 task.


### `uber-2026-adoption`

- **type**: news
- **title**: Reported adoption for the Uber engineering rollout
- **container**: Multiple secondary outlets
- **date**: 2026-05
- **perishable**: True
- **upgrade**: A single named source for the adoption percentages, ideally the primary.

NOTE, verbatim:

> PERCENTAGES WITHDRAWN 2026-08-21 ON DAN’S RULING, and the fallback wording is now what the chapter says. The February and March adoption percentages appeared across several outlets with consistent values and no consistent attribution, which is the signature of one upstream source being repeated rather than of corroboration. G1 could not clear an access date for an entry with no locatable source, so the figures came out instead of the citation being invented. THE CHAPTER NOW SAYS ‘about a third’ and ‘a large majority’, and the share of committed code is characterized rather than quantified. No access date applies because no single document is cited. REVERSING CONDITION: a named source carrying the adoption percentages, read and dated, would license restoring them as figures. Until then the qualitative form is the claim.


### `uber-2026-budget`

- **type**: news
- **authors**: MSV Janakiram
- **title**: Uber burns its 2026 AI budget in four months on Claude Code
- **container**: Forbes
- **date**: 2026-05-17
- **url**: https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/
- **perishable**: True
- **accessed**: 2026-08-21
- **upgrade**: The Information’s original report, which carries the CTO confirmation. Paywalled.

NOTE, verbatim:

> UNVERIFIED. Found by WebSearch 2026-08-21; the article itself has not been read by Claude, and the container cannot fetch it. Carries the budget exhaustion timing, the engineer count, the rollout date, and the per-engineer monthly cost range. Grade C until a primary is read. The chapter states the cost range as ’several hundred to a few thousand dollars’ rather than as exact bounds, deliberately, so that a corrected figure does not invalidate the sentence.

