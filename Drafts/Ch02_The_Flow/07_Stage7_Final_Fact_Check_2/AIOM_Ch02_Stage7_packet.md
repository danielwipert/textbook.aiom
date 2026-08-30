# Chapter 2, Stage 7. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 7 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch02_The_Flow/00_Stage0_Draft/AIOM_Ch02_draft.html`
RENDER         `Drafts/Ch02_The_Flow/07_Stage7_Final_Fact_Check_2/AIOM_Ch02_Stage7_render.pdf`, FAILING a print gate on this file: footnotes not on the page of their call: [(2, ['5']), (3, ['5'])].

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. This chapter carries 12 ruling(s) already
made and still in force, recorded in `AIOM_Claim_Ledger.md` and in the
register notes below. A checker who reaches one should say whether the
condition named in the note is now met, not restate the finding.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    5 keys defined, 5 cited. 0 orphan(s), 0 dangling.
  Citation markers    7 cited passages, every marker resolving to a key.
  Footnote build      9 footnote(s) generated. Gate 8 checks each sits on its calling page; its verdict on the shipped render is on the RENDER line above, where it is measured rather than assumed.
  Ruled-form check    12 ruling(s) in force for Ch02: 14 required, 16 forbidden,
                      4 by reading. `claimcheck.py` reports PASS.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> By April 2026, just four months into the year, Uber had already exhausted its annual AI budget. Nothing had broken. No contract had been renegotiated, and no vendor had raised its prices. Engineers were simply doing the work the company had asked them to do by using the tools it had given them.

CITES: `uber-2026-budget`

IN-CHAPTER GLOSS: Reported timing of the budget exhaustion.

### C2

CLAIM TEXT AS IT STANDS

> The tool was Claude Code, an AI assistant that writes and edits software. Uber had begun rolling it out to roughly 5,000 engineers in December 2025. Adoption was rapid. By February, about a third of the engineering organization was using it. A month later, usage had spread to a large majority.

CITES: `uber-2026-budget`, `uber-2026-adoption`

IN-CHAPTER GLOSS: Engineer count and rollout timing.

### C3

CLAIM TEXT AS IT STANDS

> By the usual measures, the rollout looked like a success. Engineers adopted the tool quickly and used it heavily. Press reports indicated that by spring, a large share of committed code had passed through it. But those measures establish adoption, not value. That distinction is central to this chapter.

CITES: `uber-2026-adoption`

IN-CHAPTER GLOSS: Characterized rather than quantified, for the same reason.

### C4

CLAIM TEXT AS IT STANDS

> The cost per engineer, however, was not fixed. Reported monthly spending ranged from several hundred to several thousand dollars, depending on how often each engineer used Claude Code and the complexity of the work. The price had not changed. Uber was paying for consumption, so wider adoption and heavier use drove spending higher.

CITES: `uber-2026-budget`

IN-CHAPTER GLOSS: Reported per-engineer monthly cost range.

### C5

CLAIM TEXT AS IT STANDS

> This episode turns on a distinction that is easy to miss. Uber could see what it was spending, but it could not say what that spending had produced. The charges accumulated until they consumed the annual budget in April. Yet president and chief operating officer Andrew Macdonald said the company still could not connect its growing use of Claude Code to the consumer features it was producing. “That link is not there yet,” he said. His statement suggests that any documented return remained unavailable, incomplete, or unconvincing to senior leadership.

CITES: `fortune-2026-uber-coo`

IN-CHAPTER GLOSS: Reported executive commentary on whether the spending was justified.

### C6

CLAIM TEXT AS IT STANDS

> The pattern is not confined to one company. A 2025 MIT NANDA study of enterprise deployments reported a striking gap: 95 percent of enterprise generative AI pilots produced no measurable impact on profit and loss, even though a far larger share of organizations reported piloting or deploying such tools. The headline drew substantial methodological criticism after it circulated, and published accounts of the study report different interview counts.

CITES: `mit-nanda-2025`, `mit-nanda-2025`

IN-CHAPTER GLOSS: Reported headline finding and adoption figures.

### C7

CLAIM TEXT AS IT STANDS

> Between January and June 2024, the Australian Government ran a whole-of-government trial of Microsoft 365 Copilot. Around sixty agencies participated. Each agency nominated the employees who would receive licences, and the government issued several thousand licences. The product was priced per seat rather than by unit of use. The Digital Transformation Agency commissioned an independent evaluation and published it in full. Participants reported using the tool a few times a week or less and saving time when they used it. The evaluation identified two limits in its method: participants assessed the effects themselves, which could understate or overstate them, and no measure of the work existed from before the trial.

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
- **accessed**: 2026-08-29
- **upgrade**: Direct quotation of the executive, with venue and date.

NOTE, verbatim:

> VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS B1 TO B3 OF THE VERIFICATION SHEET, ALL PASS. The speaker is Andrew Macdonald, Uber’s PRESIDENT AND CHIEF OPERATING OFFICER, and the chapter said only ‘chief operating officer’ until this ruling; both sentences carrying the title were corrected the same day. THE VENUE IS THE RAPID RESPONSE PODCAST, which Fortune reports: the article is therefore SECONDARY to a recorded interview, and that is the level the chapter cites. MACDONALD’S WORDS, QUOTED HERE BECAUSE A NOTE THAT QUOTES THE SENTENCE IS WHAT CAUGHT SF7 AND SF11: he said it is hard to draw a connection between the company’s rising use of Claude Code and innovations meant to serve consumers. ‘That link is not there yet. Maybe implicitly there’s more that is getting shipped, but it’s very hard to draw a line between one of those stats and “Okay now we’re actually producing like 25% more useful consumer features.”’ B2 PASSES ON DAN’S READING that he questions the value of the spend repeatedly in the interview, not on this quotation alone. REVERSES IF the interview is shown to postdate or otherwise not bear on the April budget exhaustion, or if the title changes again. RULED THE SAME DAY: DAN CHOSE THE DIRECT QUOTATION AND THE NAME. The paraphrase was supported and stood, and the quoted words are narrower and stronger, namely that the link between usage and consumer value cannot be drawn, which is the cost-value asymmetry in the executive’s own words. The opening case now names him in Chapter 1’s form, title then full name then ‘said publicly that’, and carries ‘That link is not there yet,’ he said. THIS IS THE BOOK’S FIRST DIRECT QUOTATION IN BODY PROSE; Chapter 1 names Sam Altman and quotes nobody. THE SHORT LINE WAS CHOSEN OVER THE LONGER ONE DELIBERATELY: the longer quotation carries three contractions, body prose bans them, and the opening case is not a voiced block, so quoting it would have failed Stage 4 mechanical. The 2.6 back-reference is unchanged and is supported by B2. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Supports the claim that a senior executive publicly questioned whether the spending was justified. THE CHAPTER’S ARGUMENT LEANS ON THIS MORE THAN ON ANY FIGURE, because the executive’s question is the evidence that the value half of the flow was unbuilt. If Stage 3 cannot confirm it, the paragraph and problem P1 both need rework rather than a looser number.


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
- **accessed**: 2026-08-29
- **upgrade**: The Information’s original report, which carries the CTO confirmation. Paywalled.

NOTE, verbatim:

> VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS A1 TO A6 OF THE VERIFICATION SHEET, ALL PASS. That covers the budget exhaustion and its April timing, that no contract was renegotiated and no vendor raised a price, the roughly five thousand engineers from December 2025, the per-engineer monthly cost range, the attribution of the variation to workload, and the usage-based commercial terms. A2 AND A5 WERE CHECKED SEPARATELY FROM THE FIGURES AND BOTH HOLD, which matters because each could have been the chapter’s inference rather than the article’s statement, and that is the shape of Chapter 1’s FC9. STILL SECONDARY. The chapter’s cost range remains deliberately loose, and the upgrade is unchanged: The Information’s original report carries the CTO confirmation and is paywalled. Verifying Forbes establishes that the reporting says what the chapter says it says, not that the underlying facts hold. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch 2026-08-21; the article itself has not been read by Claude, and the container cannot fetch it. Carries the budget exhaustion timing, the engineer count, the rollout date, and the per-engineer monthly cost range. Grade C until a primary is read. The chapter states the cost range as ’several hundred to a few thousand dollars’ rather than as exact bounds, deliberately, so that a corrected figure does not invalidate the sentence.

