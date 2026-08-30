# Chapter 2, Stage 7. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 7 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch02_The_Flow/00_Stage0_Draft/AIOM_Ch02_draft.html`
RENDER         `Drafts/Ch02_The_Flow/07_Stage7_Final_Fact_Check_2/AIOM_Ch02_Stage7_render.pdf`, all fifteen print gates pass on this file, run here.

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. This chapter carries 10 ruling(s) already
made and still in force, recorded in `AIOM_Claim_Ledger.md` and in the
register notes below. A checker who reaches one should say whether the
condition named in the note is now met, not restate the finding.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    6 keys defined, 6 cited. 0 orphan(s), 0 dangling.
  Citation markers    7 cited passages, every marker resolving to a key.
  Footnote build      10 footnote(s) generated. Gate 8 checks each sits on its calling page; its verdict on the shipped render is on the RENDER line above, where it is measured rather than assumed.
  Ruled-form check    10 ruling(s) in force for Ch02: 12 required, 15 forbidden,
                      3 by reading. `claimcheck.py` reports PASS.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> By April 2026, just four months into the year, Uber had already exhausted its annual AI budget. Nothing had broken. No contract had been renegotiated, and no vendor had raised its prices. Engineers were simply doing the work the company had asked them to do by using the tool it had given them.

CITES: `uber-2026-budget`

IN-CHAPTER GLOSS: Reported timing of the budget exhaustion.

### C2

CLAIM TEXT AS IT STANDS

> The tool was Claude Code, an AI assistant that writes and edits software. Uber had begun rolling it out to roughly 5,000 engineers in December 2025. Adoption was rapid. By February, 32 percent of the engineering organization was using it. By March, that share had reached 84 percent.

CITES: `uber-2026-budget`, `uber-2026-budget`

IN-CHAPTER GLOSS: Engineer count and rollout timing.

### C3

CLAIM TEXT AS IT STANDS

> By the usual measures, the rollout looked like a success. Engineers adopted the tool quickly and used it heavily. Macdonald said that a quarter of the company’s code commits in the previous quarter had come through Claude Code. But those measures establish adoption, not value. That distinction is central to this chapter.

CITES: `rapidresponse-2026-macdonald`

IN-CHAPTER GLOSS: Share of code commits, in the executive’s own words.

### C4

CLAIM TEXT AS IT STANDS

> The cost per engineer, however, was not fixed. Reported monthly spending ran from $150 to $250 for the average engineer and from $500 to $2,000 for the heaviest users. The price had not changed. Uber was paying for consumption, so wider adoption and heavier use drove spending higher.

CITES: `uber-2026-budget`

IN-CHAPTER GLOSS: Reported per-engineer monthly cost figures, verified against the article at Stage 7.

### C5

CLAIM TEXT AS IT STANDS

> This episode turns on a distinction that is easy to miss. Uber could see what it was spending, but it could not say what that spending had produced. The charges accumulated until they consumed the annual budget in April. Yet president and chief operating officer Andrew Macdonald said the company still could not connect its growing use of Claude Code to the consumer features it was producing. “That link is not there yet,” he said. His statement suggests that any documented return remained unavailable, incomplete, or unconvincing to senior leadership.

CITES: `fortune-2026-uber-coo`

IN-CHAPTER GLOSS: Reported executive commentary on whether the spending was justified.

### C6

CLAIM TEXT AS IT STANDS

> The pattern is not confined to one company. A 2025 MIT NANDA study of enterprise deployments reported a striking gap: 95 percent of integrated enterprise AI pilots produced no measurable impact on profit and loss, even though a far larger share of organizations reported piloting or deploying such tools. The headline drew substantial methodological criticism after it circulated, and published accounts of the study report different interview counts.

CITES: `mit-nanda-2025`, `mit-nanda-2025`

IN-CHAPTER GLOSS: Reported headline finding and adoption figures.

### C7

CLAIM TEXT AS IT STANDS

> Between January and June 2024, the Australian Government ran a whole-of-government trial of Microsoft 365 Copilot. Around sixty agencies participated. Each agency nominated or approved the employees who would receive licences, and the government issued several thousand licences. The product was priced per seat rather than by unit of use. The Digital Transformation Agency commissioned the evaluation, delivered it jointly with an external firm, and published the full report. Participants reported using the tool a few times a week or less and saving time when they used it. The evaluation named five limits in its method, one of which is that participants assessed the effects themselves, which could understate or overstate them. Its published methodology reports no objective measure of task time or output from before the trial.

CITES: `microsoft-2024-copilot-pricing`, `dta-copilot-2024`

IN-CHAPTER GLOSS: Per-seat pricing for the product, from the vendor’s own announcement.

---

## Part 2. Register entries, verbatim

### `dta-copilot-2024`

- **type**: report
- **authors**: {"org": "Digital Transformation Agency"}, {"org": "Nous Group"}
- **title**: Evaluation of the whole-of-government trial of Microsoft 365 Copilot
- **container**: Australian Government Digital Transformation Agency
- **date**: 2024
- **url**: https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full
- **perishable**: False
- **upgrade**: The published evaluation itself, which the Digital Transformation Agency released in full and which nobody on this project has read.

NOTE, verbatim:

> STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE REPORT HAS NOW BEEN READ AND THE GRADE C IS DISCHARGED. Of the four things this note called load bearing, TWO HELD AND TWO FAILED. Held: the licence is priced per seat rather than by unit of use (now also carried by microsoft-2024-copilot-pricing, since this report does not state the contrast), and agencies nominated participants (the chapter now says ’nominated or approved’, because Appendix B records a self-nomination route as well). FAILED 1, THE EVALUATION IS NOT INDEPENDENT: Appendix B says it was ’jointly delivered by the DTA and Nous’. This note asked Stage 3 to record whether Nous appears on the face of the report, and it does. The word ’independent’ is cut from BOTH sentences that carried it, which sit far apart, and FQ5 is amended in the claim ledger because one of them was its REQUIRED text. FAILED 2, THE REPORT NAMES FIVE LIMITS, NOT TWO: representativeness, positive selection bias, inconsistent rollout, evaluation fatigue and self-assessment. Only self-assessment was one of the chapter’s two. THE ABSENCE OF A PRE-TRIAL WORK BASELINE IS NOT ONE OF THE REPORT’S LIMITATIONS: it ran a pre-use survey that baselined sentiment and confidence rather than task time or output. The chapter was presenting its own inference as the report’s statement, which is Chapter 1’s FC9 shape. The sentence is split so the report’s finding and the chapter’s inference are visibly different things. THE COUNTS WERE RIGHT TO LEAVE LOOSE. Around sixty agencies holds, and the official record reports 7,600 staff, 5,765 licences and 7,769 licences in three places, so ’several thousand’ should NOT be replaced by a precise count until the agency resolves its own discrepancy. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch on 2026-08-22 for problem P3, after Dan ruled at Chapter 2 Stage 1 that competency C2 needs a mapping exercise on a cited real deployment and that the constructed insurer would not serve. Claude read search result summaries and did NOT read the evaluation, any article about it, or any agency page: WebFetch and curl are blocked by the container egress proxy. Grade C. THE SECONDARY COVERAGE DISAGREES WITH ITSELF ON EVERY COUNT, which is why the problem states none of them precisely. Agency counts of 56, almost 60 and more than 60 all appear; participant and licence counts of more than 5,000, 5,765, nearly 6,000 and 7,600 all appear. The problem says ’around sixty agencies’ and ’several thousand licences’ deliberately, so that a corrected count does not invalidate the exercise. WHAT IS LOAD BEARING IS NOT A COUNT. The problem rests on four things: that the licence is priced per seat rather than by unit of use, that agencies nominated their own participants, that an independent evaluation was commissioned and published, and that the evaluation stated both that participants self-assessed the effects and that no pre-trial measure of the work existed. STAGE 3 MUST CONFIRM THOSE FOUR AND MAY LEAVE THE COUNTS ALONE. It should also settle the publication date, which is recorded here as the year only because no source read gave a day, and record whether the evaluation is attributed to Nous Group on its face, since secondary coverage names that firm as the evaluator. ACCESS DATE NOT REQUIRED: a fixed published report, the same convention applied to mit-nanda-2025.


### `fortune-2026-uber-coo`

- **type**: news
- **title**: Uber burned through its entire 2026 AI budget in four months
- **container**: Fortune
- **date**: 2026-05-26
- **url**: https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/
- **perishable**: True
- **accessed**: 2026-08-30
- **upgrade**: Taken 2026-08-30. See rapidresponse-2026-macdonald.

NOTE, verbatim:

> STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. CHECK A OPENED THE ARTICLE AND THE FIRST-PARTY TRANSCRIPT BEHIND IT. The quotation ’That link is not there yet’ is confirmed in both, and the remark refers to Claude Code specifically rather than to AI spending generally, which the Stage 6 copy edit had narrowed it to and which was flagged for this step as a risk. It is cleared. THE UPGRADE THIS ENTRY ASKED FOR IS NOW TAKEN and lives at rapidresponse-2026-macdonald. One unresolved nuance, recorded rather than acted on: Fortune calls it the 2026 AI coding-tools budget while Forbes and Macdonald use the broader ’AI budget’, and the chapter follows Forbes. PRIOR NOTE, KEPT AS HISTORY: VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS B1 TO B3 OF THE VERIFICATION SHEET, ALL PASS. The speaker is Andrew Macdonald, Uber’s PRESIDENT AND CHIEF OPERATING OFFICER, and the chapter said only ‘chief operating officer’ until this ruling; both sentences carrying the title were corrected the same day. THE VENUE IS THE RAPID RESPONSE PODCAST, which Fortune reports: the article is therefore SECONDARY to a recorded interview, and that is the level the chapter cites. MACDONALD’S WORDS, QUOTED HERE BECAUSE A NOTE THAT QUOTES THE SENTENCE IS WHAT CAUGHT SF7 AND SF11: he said it is hard to draw a connection between the company’s rising use of Claude Code and innovations meant to serve consumers. ‘That link is not there yet. Maybe implicitly there’s more that is getting shipped, but it’s very hard to draw a line between one of those stats and “Okay now we’re actually producing like 25% more useful consumer features.”’ B2 PASSES ON DAN’S READING that he questions the value of the spend repeatedly in the interview, not on this quotation alone. REVERSES IF the interview is shown to postdate or otherwise not bear on the April budget exhaustion, or if the title changes again. RULED THE SAME DAY: DAN CHOSE THE DIRECT QUOTATION AND THE NAME. The paraphrase was supported and stood, and the quoted words are narrower and stronger, namely that the link between usage and consumer value cannot be drawn, which is the cost-value asymmetry in the executive’s own words. The opening case now names him in Chapter 1’s form, title then full name then ‘said publicly that’, and carries ‘That link is not there yet,’ he said. THIS IS THE BOOK’S FIRST DIRECT QUOTATION IN BODY PROSE; Chapter 1 names Sam Altman and quotes nobody. THE SHORT LINE WAS CHOSEN OVER THE LONGER ONE DELIBERATELY: the longer quotation carries three contractions, body prose bans them, and the opening case is not a voiced block, so quoting it would have failed Stage 4 mechanical. The 2.6 back-reference is unchanged and is supported by B2. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Supports the claim that a senior executive publicly questioned whether the spending was justified. THE CHAPTER’S ARGUMENT LEANS ON THIS MORE THAN ON ANY FIGURE, because the executive’s question is the evidence that the value half of the flow was unbuilt. If Stage 3 cannot confirm it, the paragraph and problem P1 both need rework rather than a looser number.


### `microsoft-2024-copilot-pricing`

- **type**: web
- **authors**: {"org": "Microsoft"}
- **title**: Expanding Copilot for Microsoft 365 to businesses of all sizes
- **container**: Microsoft 365 Blog
- **date**: 2024-01-15
- **url**: https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/
- **accessed**: 2026-08-30
- **upgrade**: Nothing outstanding. This is the vendor’s own announcement.

NOTE, verbatim:

> STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. ADDED BECAUSE THE DTA EVALUATION DOES NOT ESTABLISH THE PRICING CONTRAST. It records agencies purchasing licences; it does not state that the product is priced per seat rather than by unit of use, which is the sentence problem P3 rests on. Microsoft’s own announcement prices it at $30 per user per month, which settles it. Check A raised the gap and it is closed here rather than by leaving one source carrying two claims.


### `mit-nanda-2025`

- **type**: report
- **authors**: Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari
- **title**: The GenAI Divide: State of AI in Business 2025
- **container**: MIT NANDA
- **date**: 2025-07
- **perishable**: False
- **upgrade**: An institutional location: MIT Media Lab or Project NANDA’s own distribution. A third-party mirror is refused, ruled by Dan 2026-08-30.

NOTE, verbatim:

> STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. AUTHORS AND DATE CORRECTED. The four authors are named on the cover and the register carried none. THE REPORT IS DATED JULY 2025, NOT AUGUST: August was the news cycle, and the chapter’s dated evidence box moves with it. The headline wording is confirmed: the report’s own phrase is ’no measurable P&L impact’, which the chapter expands accurately to profit and loss, and the 95 per cent is over INTEGRATED pilots, which the chapter now says. THE LOCATION IS STILL ABSENT AND THAT IS A RULING, NOT AN OMISSION. Dan ruled on 2026-08-30 that the only location check A could produce, a copy hosted on a consulting firm’s website, is REFUSED: a third-party mirror can vanish and confers no authority, and this entry is better carrying an honest gap than a citation that looks solid and is not. The upgrade is unchanged and is now specific. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED, and carried from CASE 6.2 in the case bank rather than from new research. Ruled into the Chapter 2 teaching body by Dan on 2026-08-21. HANDLE WITH CARE per the bank: the ninety-five per cent figure circulated widely and drew methodological criticism, and reported interview counts vary across accounts. The chapter states the criticism once, plainly, per the straight-spine evidence policy, and rests its argument on the phrase ’no measurable impact’ rather than on the figure’s precision. Stage 3 should obtain the report and confirm the wording of the headline finding. ACCESS DATE NOT REQUIRED: the report is non-perishable, and the Chapter 1 convention is that a fixed document cited by a stable identifier needs no access date. What it still needs is its location, which the case bank records as not yet obtained. Stage 3 task.


### `rapidresponse-2026-macdonald`

- **type**: interview
- **authors**: Andrew Macdonald
- **title**: Uber’s swerve on gas prices, hotels, a driverless future
- **container**: Rapid Response, Masters of Scale
- **date**: 2026-05
- **url**: https://mastersofscale.com/ubers-swerve-on-gas-prices-hotels-a-driverless-future/
- **accessed**: 2026-08-30
- **upgrade**: Nothing outstanding. This is the primary.

NOTE, verbatim:

> STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE FIRST-PARTY VENUE, and it is the upgrade fortune-2026-uber-coo asked for by name: ’Direct quotation of the executive, with venue and date.’ Check A read the transcript and confirms both the quotation and the figure the chapter now carries, a quarter of code commits in the previous quarter through Claude Code. THE CHAPTER PREVIOUSLY SAID ’a large share of committed code had passed through it’, which check A flagged because ’passed through’ has no stable technical definition: it does not distinguish assisted from generated from committed without human review. The first-party formulation is used instead. The spoken quotation continues with ’right?’, which is dropped as a spoken tag without changing the meaning.


### `uber-2026-budget`

- **type**: news
- **authors**: Janakiram MSV
- **title**: Uber burns its 2026 AI budget in four months on Claude Code
- **container**: Forbes
- **date**: 2026-05-17
- **url**: https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/
- **perishable**: True
- **accessed**: 2026-08-30
- **upgrade**: The Information’s original report, which carries the CTO confirmation. Paywalled.

NOTE, verbatim:

> STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE COST RANGE WAS WRONG AND STAGE 3 PASSED IT. The article gives an average of $150 to $250 and heavy-user spending of $500 to $2,000. The chapter said ’several hundred to several thousand’ and, before the Stage 6 copy edit, ’a few thousand’: BOTH endpoints were unsupported in both forms, so the copy edit did not cause this. The looseness was deliberate, recorded here as protection against a corrected figure, and it concealed the error from every checker who could not read the article. THE RATIONALE FOR LOOSENESS IS RETIRED and the chapter now carries the exact figures, which the fifty-year rule permits because the opening case is dated. THE COMPLEXITY CLAUSE IS CUT: the article does not attribute the range to the complexity of the work, and the workload mechanism is already carried by the two sentences after it. THE ADOPTION PERCENTAGES NOW LIVE HERE, 32 per cent in February and 84 per cent in March, which retires uber-2026-adoption and with it rulings S3-1 and S3-2. BYLINE CORRECTED to its published form, Janakiram MSV, which the register had inverted. STILL SECONDARY, and the upgrade is unchanged: The Information’s original carries the CTO confirmation and stayed paywalled to check A as well. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS A1 TO A6 OF THE VERIFICATION SHEET, ALL PASS. That covers the budget exhaustion and its April timing, that no contract was renegotiated and no vendor raised a price, the roughly five thousand engineers from December 2025, the per-engineer monthly cost range, the attribution of the variation to workload, and the usage-based commercial terms. A2 AND A5 WERE CHECKED SEPARATELY FROM THE FIGURES AND BOTH HOLD, which matters because each could have been the chapter’s inference rather than the article’s statement, and that is the shape of Chapter 1’s FC9. STILL SECONDARY. The chapter’s cost range remains deliberately loose, and the upgrade is unchanged: The Information’s original report carries the CTO confirmation and is paywalled. Verifying Forbes establishes that the reporting says what the chapter says it says, not that the underlying facts hold. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch 2026-08-21; the article itself has not been read by Claude, and the container cannot fetch it. Carries the budget exhaustion timing, the engineer count, the rollout date, and the per-engineer monthly cost range. Grade C until a primary is read. The chapter states the cost range as ’several hundred to a few thousand dollars’ rather than as exact bounds, deliberately, so that a corrected figure does not invalidate the sentence.

