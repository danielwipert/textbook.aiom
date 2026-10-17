# Chapter 3, Stage 3. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 3 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html`
RENDER         `Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/AIOM_Ch03_v2_Stage3_render.pdf`, FAILING a print gate on this file: overflow: [(6, 420.0, ' ')]; 1 definition callout(s) split across a page break; run place.py on this chapter.

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. This chapter carries 14 ruling(s) already
made and still in force, recorded in `AIOM_Claim_Ledger.md` and in the
register notes below. A checker who reaches one should say whether the
condition named in the note is now met, not restate the finding.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    20 keys defined, 18 cited. 2 orphan(s), 0 dangling.
                      orphans: gartner-aiops, kreuzberger-2023-mlops
  Citation markers    15 cited passages, every marker resolving to a key.
  Footnote build      24 footnote(s) generated. Gate 8 checks each sits on its calling page; its verdict on the shipped render is on the RENDER line above, where it is measured rather than assumed.
  Ruled-form check    14 ruling(s) in force for Ch03: 12 required, 16 forbidden,
                      1 by reading. `claimcheck.py` reports FAIL.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

CITES: `finops-2026-mission`

IN-CHAPTER GLOSS: The mission statement before and after the change.

### C2

CLAIM TEXT AS IT STANDS

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding was how far FinOps had expanded into AI spending: 98 percent of respondents now managed it, up from 31 percent two years earlier.

CITES: `finops-2026-state`, `finops-2026-state`

IN-CHAPTER GLOSS: Survey size and the cloud spending its respondents manage.

### C3

CLAIM TEXT AS IT STANDS

> FinOps was built to address a specific problem: cloud bills varied with use and arrived after capacity had been consumed. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all respondents to the Foundation’s survey were managing it.

CITES: `finops-definition-2024`, `finops-what-is`

IN-CHAPTER GLOSS: Cloud consumption as variable and tracked after the fact.

### C4

CLAIM TEXT AS IT STANDS

> Asked whether AI was providing value, one practitioner acknowledged the uncertainty. The report quoted the answer: “No one can answer that question yet.”

CITES: `finops-2026-state`

IN-CHAPTER GLOSS: Practitioner quotation as reproduced in the report.

### C5

CLAIM TEXT AS IT STANDS

> Chapter 1’s Cursor licenses show this check in practice. Two of the result’s conditions are that the buyer’s cost extends beyond the access price and that measurement makes resource use visible. After June 2025, each request drew down a twenty-dollar monthly credit at the model provider’s rate, and further use was priced at the same rates. Both conditions therefore held for a team on that plan. A manager who still budgeted the licenses as a fixed software expense was treating the access price as the full cost, even though the conditions showed otherwise. Checking those conditions could settle what confidence alone could not.

CITES: `truell-2025-pricing`

IN-CHAPTER GLOSS: The Cursor post describing the plan change of June 16, 2025, as cited in Chapter 1.

### C6

CLAIM TEXT AS IT STANDS

> In October 2025, Airbnb’s chief executive, Brian Chesky, said the company’s customer-service agent was built on 13 models from OpenAI, Google, Alibaba, and open-source providers. He said the company relied heavily on Alibaba’s Qwen models, which he called “very good” and “also fast and cheap.” He also said OpenAI’s tools for connecting its models to Airbnb’s systems were not yet ready to meet the company’s needs.

CITES: `airbnb-2025-qwen`

IN-CHAPTER GLOSS: The chief executive’s account of the models behind the agent.

### C7

CLAIM TEXT AS IT STANDS

> Pigment, a company that sells financial planning software, surveyed about 2,000 finance leaders in the United States, the United Kingdom, France, and Germany for a report released in October 2026. Eighty-three percent said consumption-based pricing had pushed their AI spending above expectations. Thirteen percent said they had stayed within budget, and the average overrun was about 27 percent. These figures describe the survey’s respondents and were reported by a vendor of planning software.

CITES: `pigment-2026-cfo-index`

IN-CHAPTER GLOSS: Survey size, overruns, and the share within budget.

### C8

CLAIM TEXT AS IT STANDS

> DoiT, a company that sells cloud cost-management services, commissioned a survey of 500 finance leaders at organizations with at least 1,000 employees in the United States and the United Kingdom. Sapio Research conducted it in February 2026. Seventy-nine percent reported AI-related cost overruns in the previous twelve months. Asked who was accountable for AI spending, 55 percent named technology leadership and 53 percent named finance, meaning at least 8 percent named both.

CITES: `doit-2026-ai-spend`

IN-CHAPTER GLOSS: Survey size, overruns, and the split of accountability.

### C9

CLAIM TEXT AS IT STANDS

> In July 2026, Bloomberg reported that Microsoft had begun sending some prompts from Copilot in Excel and Outlook to its own MAI models instead of models from OpenAI and Anthropic, citing the cost of the outside models. Reports put the volume at tens of thousands of prompts a week. Routine tasks moved to the in-house models, while complex reasoning tasks could still go to the outside models. The company’s head of AI, Mustafa Suleyman, said its goal was to reduce and ultimately eliminate its payments to Anthropic.

CITES: `microsoft-2026-mai`

IN-CHAPTER GLOSS: The routing change, its scale, and the stated cost motive.

### C10

CLAIM TEXT AS IT STANDS

> In October 2025, JPMorgan Chase’s chief executive, Jamie Dimon, told Bloomberg Television that the bank spent about $2 billion a year on AI and received about the same in benefits: “We have shown that for $2 billion of expense, we have about $2 billion of benefit.” When later asked for updated figures, the bank’s chief financial officer put annual AI spending closer to $700 million and called the earlier figure “a little stale.” The same report said the benefits were not yet visible in the bank’s quarterly earnings. The published accounts do not say which costs, benefits, or period either figure covered.

CITES: `jpmorgan-2025-dimon`, `jpmorgan-cfo-ai-spend`

IN-CHAPTER GLOSS: The chief executive’s figures.

### C11

CLAIM TEXT AS IT STANDS

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. The distinction rests on what each was built to do, rather than what it intends to achieve. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The Foundation’s definition, which names business value.

### C12

CLAIM TEXT AS IT STANDS

> Lindy is a company of about 25 people that sells AI assistants for email and calendars. In 2026, its founder, Flo Crivello, said the company’s largest expense was the AI models it bought from Anthropic: “Like, more than payroll.” In June 2026, he announced that Lindy had moved all its traffic to DeepSeek V4, a model from a Chinese developer, and said the move would save millions of dollars. He called the switch “100x more work than we thought.” He said he would consider returning to Anthropic’s models if their prices fell and expected the company to keep spending more on AI than on payroll.

CITES: `npr-2026-lindy`, `cnbc-2026-lindy`

IN-CHAPTER GLOSS: The founder’s statements on cost, payroll, and the work of switching.

### C13

CLAIM TEXT AS IT STANDS

> Step 1. The reported activities are buying access to Claude Code; rolling it out to roughly 5,000 engineers from December 2025; setting an annual AI budget; tracking adoption, which reached 32 percent of the engineering organization in February and 84 percent in March; and totaling spending. Reported spending ranged from $150 to $250 a month for the average engineer and from $500 to $2,000 for the heaviest users. A sixth activity was asking about value. The president and chief operating officer said the company could not yet connect its growing use of the tool to the consumer features it was producing: “That link is not there yet.”

CITES: `uber-2026-budget`, `fortune-2026-uber-coo`

IN-CHAPTER GLOSS: Rollout, adoption, and the cost per engineer.

### C14

CLAIM TEXT AS IT STANDS

> Chapter 2’s problem P3 described the Australian Government’s whole-of-government trial of Microsoft 365 Copilot, which ran from January to June 2024. Around sixty agencies took part. Each agency nominated or approved the employees who would receive licenses, and the government issued several thousand. The product was priced per seat rather than by unit of use. The Digital Transformation Agency commissioned an evaluation, delivered it jointly with an external firm, and published the full report. Participants reported using the tool a few times a week or less and saving time when they used it. These were their own assessments, and the published methodology reports no objective measure of task time or output before the trial. Steps 1 to 3 are worked through below. Complete Steps 4 to 6.

CITES: `microsoft-2024-copilot-pricing`, `dta-copilot-2024`

IN-CHAPTER GLOSS: Per-seat pricing of the product.

### C15

CLAIM TEXT AS IT STANDS

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. Klarna also reported that customers resolved their questions in under two minutes during that month, compared with eleven minutes previously. It estimated that the assistant would improve its profit by $40 million in 2024.

CITES: `klarna-2024-assistant`

IN-CHAPTER GLOSS: All figures in this case are the company’s own, as announced.

---

## Part 2. Register entries, verbatim

### `airbnb-2025-qwen`

- **type**: news
- **title**: Airbnb CEO Brian Chesky says OpenAI’s tools are not ready, relies on Alibaba’s Qwen
- **container**: Fortune
- **date**: 2025-10-21
- **url**: https://fortune.com/2025/10/21/brian-chesky-openai-tools-not-ready
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage (Fortune, South China Morning Post, Bloomberg interview behind both) gives: the agent is built on 13 models from OpenAI, Alibaba, Google and open-source providers; Airbnb relies heavily on Qwen, which Chesky called ‘very good’ and ‘also fast and cheap’; OpenAI’s integration tools were not ‘quite ready’. Check A must confirm each, the date, and the exact quotations; the Bloomberg interview is the primary. The chapter does not use the later House inquiry.


### `cnbc-2026-lindy`

- **type**: news
- **title**: OpenAI and Anthropic face new AI reality as users shift from ‘tokenmaxxing’ to efficiency
- **container**: CNBC
- **date**: 2026-06-26
- **url**: https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage gives: Lindy is a roughly 25-person company; Crivello expects the switch to save millions within months; he still expects to spend more on AI than on payroll. Check A must confirm each.


### `doit-2026-ai-spend`

- **type**: web
- **authors**: {"org": "DoiT"}
- **title**: Why 79% of Enterprises Overspent on AI in 2026
- **container**: DoiT blog
- **date**: 2026
- **url**: https://www.doit.com/blog/ai-spending-survey
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage gives: commissioned by DoiT, conducted by Sapio Research, February 2026; 500 finance leaders at US and UK organizations with 1,000 or more employees; 79 percent reported AI-related cost overruns in the previous twelve months; accountability split, technology 55 percent and finance 53 percent. Check A must confirm each, and the survey dates. A 36 percent ‘unclear attribution’ figure seen in secondary coverage is NOT used: no primary was found for it.


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

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE REPORT HAS NOW BEEN READ AND THE GRADE C IS DISCHARGED. Of the four things this note called load bearing, TWO HELD AND TWO FAILED. Held: the licence is priced per seat rather than by unit of use (now also carried by microsoft-2024-copilot-pricing, since this report does not state the contrast), and agencies nominated participants (the chapter now says ’nominated or approved’, because Appendix B records a self-nomination route as well). FAILED 1, THE EVALUATION IS NOT INDEPENDENT: Appendix B says it was ’jointly delivered by the DTA and Nous’. This note asked Stage 3 to record whether Nous appears on the face of the report, and it does. The word ’independent’ is cut from BOTH sentences that carried it, which sit far apart, and FQ5 is amended in the claim ledger because one of them was its REQUIRED text. FAILED 2, THE REPORT NAMES FIVE LIMITS, NOT TWO: representativeness, positive selection bias, inconsistent rollout, evaluation fatigue and self-assessment. Only self-assessment was one of the chapter’s two. THE ABSENCE OF A PRE-TRIAL WORK BASELINE IS NOT ONE OF THE REPORT’S LIMITATIONS: it ran a pre-use survey that baselined sentiment and confidence rather than task time or output. The chapter was presenting its own inference as the report’s statement, which is Chapter 1’s FC9 shape. The sentence is split so the report’s finding and the chapter’s inference are visibly different things. THE COUNTS WERE RIGHT TO LEAVE LOOSE. Around sixty agencies holds, and the official record reports 7,600 staff, 5,765 licences and 7,769 licences in three places, so ’several thousand’ should NOT be replaced by a precise count until the agency resolves its own discrepancy. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch on 2026-08-22 for problem P3, after Dan ruled at Chapter 2 Stage 1 that competency C2 needs a mapping exercise on a cited real deployment and that the constructed insurer would not serve. Claude read search result summaries and did NOT read the evaluation, any article about it, or any agency page: WebFetch and curl are blocked by the container egress proxy. Grade C. THE SECONDARY COVERAGE DISAGREES WITH ITSELF ON EVERY COUNT, which is why the problem states none of them precisely. Agency counts of 56, almost 60 and more than 60 all appear; participant and licence counts of more than 5,000, 5,765, nearly 6,000 and 7,600 all appear. The problem says ’around sixty agencies’ and ’several thousand licences’ deliberately, so that a corrected count does not invalidate the exercise. WHAT IS LOAD BEARING IS NOT A COUNT. The problem rests on four things: that the licence is priced per seat rather than by unit of use, that agencies nominated their own participants, that an independent evaluation was commissioned and published, and that the evaluation stated both that participants self-assessed the effects and that no pre-trial measure of the work existed. STAGE 3 MUST CONFIRM THOSE FOUR AND MAY LEAVE THE COUNTS ALONE. It should also settle the publication date, which is recorded here as the year only because no source read gave a day, and record whether the evaluation is attributed to Nous Group on its face, since secondary coverage names that firm as the evaluator. ACCESS DATE NOT REQUIRED: a fixed published report, the same convention applied to mit-nanda-2025.


### `finops-2026-mission`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: A One Word Change: How the FinOps Community Made Our Mission Evolution Inevitable
- **date**: 2026-02-19
- **url**: https://www.finops.org/insights/mission-update/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). REPLACES the Yahoo Finance syndication cited at Stage 0 (A-4): the Foundation’s own announcement is the better source. VERIFIED: February 2026, a one-word change from ‘advancing the people who manage the value of cloud’ to ‘advancing the people who manage the value of technology’, released with the State of FinOps 2026 figures. RULING, Dan, sitting 3, A-1 and B-30: the chapter quoted the wording without ‘the value of’; both statements are now quoted exactly. REVERSES-IF: the Foundation’s page is changed to give a different wording.


### `finops-2026-state`

- **type**: report
- **authors**: {"org": "FinOps Foundation"}
- **title**: State of FinOps 2026
- **date**: 2026-02-19
- **url**: https://data.finops.org/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). VERIFIED (A-2, A-5): ‘1,192 respondents’, ‘$83bn+ in annual cloud spend’, and ‘98% of respondents now manage AI spend (up from 63% in 2025 and 31% in 2024)’, so 31 percent is the 2024 figure for the same measure. The quotation is in the report itself: ‘As one practitioner framed it: “Is your AI providing value? No one can answer that question yet.”’ RULINGS, Dan, sitting 3: A-3 the sentence now reads ‘Its central finding concerned the expansion of FinOps into AI spending.’ (the report makes AI central but does not state the discipline’s history); B-10 ‘nearly all of the survey’s respondents’, and the gloss ‘Share of respondents’; B-9 one practitioner’s remark is not generalized to practitioners; B-2 the provenance banner now says the figures were checked against the report. REVERSES-IF: the report is revised, or a later reading finds the quotation outside the report body.


### `finops-definition-2024`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: 2024 Changes to the Definition of Cloud FinOps
- **url**: https://www.finops.org/insights/changes-to-finops-definition/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: ADDED AT SITTING 3 (A-6). Found and read by external check A with live web access: the page describes cloud’s ‘variable consumption tracked after the fact’. RULING, Dan: the opening case’s ‘cloud computing let engineers buy capacity with a few lines of code, but the bills arrived after they had used it’ had no source for its first half and now reads ‘cloud consumption varied with use, and the bills arrived after capacity had been used.’ Section 3.5 matches (B-12). REVERSES-IF: a source describing provisioning by code is cited.


### `finops-what-is`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: What is FinOps?
- **url**: https://www.finops.org/introduction/what-is-finops/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). VERIFIED (A-7): ‘FinOps is an operational framework and cultural practice which maximizes the business value of technology ... and creates financial accountability through collaboration between engineering, finance, and business teams.’ The page names AI among technology categories (A-8) and describes ‘a strong heritage in managing cloud cost and usage’ (A-13). RULINGS, Dan, sitting 3: B-11 Table 3.1’s purpose cell now carries the value purpose as well as accountability; A-13 the table’s ‘built around cloud billing’ is now ‘grew from managing cloud cost and usage’; A-8 ‘the hardest to define’ is the book’s judgment and stays. REVERSES-IF: the Foundation changes its definition.


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

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. CHECK A OPENED THE ARTICLE AND THE FIRST-PARTY TRANSCRIPT BEHIND IT. The quotation ’That link is not there yet’ is confirmed in both, and the remark refers to Claude Code specifically rather than to AI spending generally, which the Stage 6 copy edit had narrowed it to and which was flagged for this step as a risk. It is cleared. THE UPGRADE THIS ENTRY ASKED FOR IS NOW TAKEN and lives at rapidresponse-2026-macdonald. One unresolved nuance, recorded rather than acted on: Fortune calls it the 2026 AI coding-tools budget while Forbes and Macdonald use the broader ’AI budget’, and the chapter follows Forbes. PRIOR NOTE, KEPT AS HISTORY: VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS B1 TO B3 OF THE VERIFICATION SHEET, ALL PASS. The speaker is Andrew Macdonald, Uber’s PRESIDENT AND CHIEF OPERATING OFFICER, and the chapter said only ‘chief operating officer’ until this ruling; both sentences carrying the title were corrected the same day. THE VENUE IS THE RAPID RESPONSE PODCAST, which Fortune reports: the article is therefore SECONDARY to a recorded interview, and that is the level the chapter cites. MACDONALD’S WORDS, QUOTED HERE BECAUSE A NOTE THAT QUOTES THE SENTENCE IS WHAT CAUGHT SF7 AND SF11: he said it is hard to draw a connection between the company’s rising use of Claude Code and innovations meant to serve consumers. ‘That link is not there yet. Maybe implicitly there’s more that is getting shipped, but it’s very hard to draw a line between one of those stats and “Okay now we’re actually producing like 25% more useful consumer features.”’ B2 PASSES ON DAN’S READING that he questions the value of the spend repeatedly in the interview, not on this quotation alone. REVERSES IF the interview is shown to postdate or otherwise not bear on the April budget exhaustion, or if the title changes again. RULED THE SAME DAY: DAN CHOSE THE DIRECT QUOTATION AND THE NAME. The paraphrase was supported and stood, and the quoted words are narrower and stronger, namely that the link between usage and consumer value cannot be drawn, which is the cost-value asymmetry in the executive’s own words. The opening case now names him in Chapter 1’s form, title then full name then ‘said publicly that’, and carries ‘That link is not there yet,’ he said. THIS IS THE BOOK’S FIRST DIRECT QUOTATION IN BODY PROSE; Chapter 1 names Sam Altman and quotes nobody. THE SHORT LINE WAS CHOSEN OVER THE LONGER ONE DELIBERATELY: the longer quotation carries three contractions, body prose bans them, and the opening case is not a voiced block, so quoting it would have failed Stage 4 mechanical. The 2.6 back-reference is unchanged and is supported by B2. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Supports the claim that a senior executive publicly questioned whether the spending was justified. THE CHAPTER’S ARGUMENT LEANS ON THIS MORE THAN ON ANY FIGURE, because the executive’s question is the evidence that the value half of the flow was unbuilt. If Stage 3 cannot confirm it, the paragraph and problem P1 both need rework rather than a looser number.


### `jpmorgan-2025-dimon`

- **type**: news
- **title**: JPMorgan’s Dimon says AI cost savings now match money spent
- **container**: Bloomberg, via Yahoo Finance
- **date**: 2025-10-07
- **url**: https://finance.yahoo.com/news/jpmorgan-dimon-says-ai-cost-160516333.html
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage of a Bloomberg Television interview gives the quotation ‘We have shown that for $2 billion of expense, we have about $2 billion of benefit.’ Fortune’s report is dated October 8, 2025, so the interview is placed on October 7, 2025. Check A must confirm the date and the quotation.


### `jpmorgan-cfo-ai-spend`

- **type**: news
- **title**: JPMorgan CEO Dimon warns customers of ‘liability transfer’ with AI
- **container**: Banking Dive
- **url**: https://www.bankingdive.com/news/jpmorgan-dimon-ai-agents-bank-customers-liability-transfer/832870/
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search summary of this article gives: asked for updated figures, the bank’s CFO put annual AI spending closer to $700 million, calling the earlier figure ‘a little stale’; AI benefits were not yet observable in quarterly earnings. The date and the CFO’s name were not visible in the summary. Check A must confirm all of it; if the article does not carry it, the box’s second half is cut.


### `klarna-2024-assistant`

- **type**: web
- **authors**: {"org": "Klarna"}
- **title**: Klarna AI assistant handles two-thirds of customer service chats in its first month
- **date**: 2024-02-27
- **url**: https://www.prnewswire.com/news-releases/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month-302072740.html
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). URL changed to the PR Newswire copy of the release, which is the copy check A read. VERIFIED (A-11): ‘2.3 million conversations’, ‘two-thirds’, ‘700 full-time agents’, ‘less than 2 mins compared to 11 mins previously’, ‘$40 million USD in profit improvement to Klarna in 2024’, dated February 27, 2024. RULINGS, Dan, sitting 3: A-12 ‘built on OpenAI’s models’ is now ‘powered by OpenAI’, the release’s words; B-28 the resolution time is attributed to the company; B-29 the case tasks work from the announcement alone. PROTECT THE CHAPTER 6 REVEAL: the case uses this announcement only and must not cite or allude to any later reporting. REVERSES-IF: none expected; the release is fixed.


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

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. ADDED BECAUSE THE DTA EVALUATION DOES NOT ESTABLISH THE PRICING CONTRAST. It records agencies purchasing licences; it does not state that the product is priced per seat rather than by unit of use, which is the sentence problem P3 rests on. Microsoft’s own announcement prices it at $30 per user per month, which settles it. Check A raised the gap and it is closed here rather than by leaving one source carrying two claims.


### `microsoft-2026-mai`

- **type**: news
- **title**: Microsoft begins replacing third-party AI models with its own in Office apps
- **container**: Redmond Magazine
- **date**: 2026-07-09
- **url**: https://redmondmag.com/articles/2026/07/09/microsoft-begins-replacing-third-party-ai-models.aspx
- **perishable**: True
- **accessed**: 2026-10-15
- **upgrade**: The Bloomberg report of July 7, 2026, which the coverage cites.

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage of a Bloomberg report (July 7, 2026) gives: Microsoft routes some Excel and Outlook Copilot prompts to its in-house MAI models instead of OpenAI and Anthropic models, to cut cost; tens of thousands of prompts a week (one source says 10K+); routine tasks to MAI, complex reasoning still to frontier models; Suleyman: the goal is to ‘reduce and ultimately eliminate’ what Microsoft pays Anthropic. The chapter paraphrases the Suleyman remark because the coverage quotes it with an em dash. Check A must confirm each against Bloomberg.


### `npr-2026-lindy`

- **type**: news
- **title**: American AI is expensive. Some startups are turning to cheap Chinese models
- **container**: NPR
- **date**: 2026-07-15
- **url**: https://www.npr.org/2026/07/15/nx-s1-5886476/startups-cheap-chinese-ai-models
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage gives: Crivello, ‘By far, our No. 1 expense was Anthropic ... Like, more than payroll’; Lindy moved 100 percent of its traffic to DeepSeek V4, announced in June 2026; ‘100x more work than we thought’; open to returning to Claude if prices fall. Check A must confirm each quotation and which outlet carries it, and the month of the announcement.


### `pigment-2026-cfo-index`

- **type**: report
- **authors**: {"org": "Pigment"}
- **title**: CFO Index, Q3 2026
- **date**: 2026-10-07
- **url**: https://www.pigment.com/reports/cfo-index/q3-2026
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage of the report and its press release gives: about 2,000 finance leaders in the US, UK, France and Germany; 83 percent say consumption-based costs pushed spending above expectations; 13 percent stayed within budget; average overrun about 27 percent; released October 7, 2026. Check A must confirm each against the report. Vendor survey: the box says so.


### `truell-2025-pricing`

- **type**: blog
- **authors**: Michael Truell
- **title**: Clarifying Our Pricing
- **container**: Cursor
- **date**: 2025-07-04
- **url**: https://cursor.com/blog/june-2025-pricing
- **perishable**: True
- **accessed**: 2026-07-29

NOTE, verbatim:

> FROM CHAPTER 1, verified there (note follows). Chapter 3 uses it for the plan change only, in the ruled form: further use was PRICED at the same rates; no billing mechanism is asserted (SF2, SF8). NOTE ADDED 2026-07-29 (Stage 2, items A5, A6, A7). This entry previously carried no note despite being the most load-bearing source in the chapter. Verified by direct reading on the access date. DATE: July 4, 2025, stated on the page and corroborated by the post's own timeline, which reads June 16 for the original change, June 30 for a clarity revision to that post and the pricing page, and July 4 for the apology. Three fact-check rounds have proposed July 3; all three are wrong. Do not change it. REQUEST ARITHMETIC: for external models Cursor had previously charged by request count, with a limit of 500 requests per month and Sonnet models costing two requests, which is why the chapter says five hundred requests against external models rather than 'fast requests'. The phrase 'fast requests' is TechCrunch's gloss, not Cursor's term, and must not be reintroduced. NEW PLAN TERMS: unlimited use of Tab and of models in Auto, 20 dollars of frontier model usage per month at API pricing, and the option to purchase more at cost. ORDER OF MAGNITUDE: the post states verbatim that although most users' costs stayed fairly constant, the hardest requests cost an order of magnitude more than simple ones. A raise calling this unsupported has been rejected once and should be rejected again. COVERAGE: the post gives median Pro coverage as roughly 225 Sonnet 4 requests and states that the vast majority of Pro users do not exhaust the allowance, so the chapter's depletion sentence is scoped to a labelled composite team's heaviest users on long-horizon frontier work, not to Pro users generally. REFUNDS: offered for unexpected usage between June 16 and July 4, 2025. BYLINE: the post is bylined Michael Truell with no role stated on the page; his role as chief executive of Anysphere rests on techcrunch-2025-cursor-apology, not on this post. CLAIM NARROWED 2026-08-06 (Stage 3, SF2). The chapter formerly said the allowance was consumed 'after which usage continued to bill against real rates', which asserts that billing continued automatically. This entry does not establish that. What it establishes is the price of further use: twenty dollars of frontier-model usage per month at API pricing, with the option to purchase more at cost. Whether continuation was the default or required usage-based pricing or a spend limit to have been enabled is not settled here, and no Claude session can reach the post to settle it. RULED by Dan: state the price and assert no mechanism. The sentence now reads 'after which additional usage was priced at the same rates'. Do not restore a mechanism claim without a passage from this post that describes the default billing behaviour on exhaustion. The sentence that follows, that charges arrived which no one had planned for, is scoped to the labelled composite team and is separately supported by the refund offer for unexpected usage between June 16 and July 4, 2025. MECHANISM AND SCOPE BOTH REGRESSED AND ARE RESTORED 2026-08-10 (Stage 3, SF8 and SF9). The Stage 6 copy-edit rounds of 2026-08-08 rewrote this paragraph and undid both rulings while leaving every date and figure intact, so no check on values could see it. SF8: the chapter had come to read 'Once the credit ran out, Cursor billed each additional request at API rates', which is the automatic-continuation mechanism the SF2 ruling removed, restored in different words and with no new passage from the post to support it. SF9: the depletion claim had been generalized from the case team to 'Heavy users', dropping the scoping the COVERAGE entry above exists to require, since the post states that the vast majority of Pro users do not exhaust the allowance. The sentence read, as ruled on 2026-08-10, 'For the team's heaviest users, the people getting the most value, the credit was consumed in a handful of prompts, after which additional usage was priced at the same rates.' Both halves were the ruled form. UPDATED 2026-08-12 (CE11). That sentence was restructured to remove a mid-clause interrupter, per prose style guide Part 5 rule 3, and now reads 'The credit was consumed in a handful of prompts for the team's heaviest users, the people getting the most value. Additional usage was then priced at the same rates.' THE SF9 SCOPING SURVIVES: the depletion is still scoped to the team's heaviest users and is still not a claim about Pro users generally, which is the whole point of the COVERAGE entry above. Only the clause order changed; no value, date or claim moved. Recorded here rather than left to a later checker because this note's quotation of the exact sentence is what caught SF8 to SF10, and a quotation that silently goes stale is the failure SF7 and SF11 already are. What would reverse SF8 is unchanged and stated above: a passage from this post describing the default billing behaviour on exhaustion. What would reverse SF9: a passage scoping exhaustion to Pro users generally, which this post contradicts. CARRY TO EVERY LATER CHAPTER: a ruled claim narrowing does not survive a copy edit on its own. This one was recoverable only because the ruled sentence was quoted here and could be diffed against the render the external checks audited. CLAIM CUT 2026-08-13 (Stage 7, external check 2, FC9). The chapter formerly closed the paragraph with 'Cursor had been paying the difference, but the difference had become too expensive to absorb.' This entry does not carry it: the words absorb, paying the difference and too expensive appear nowhere in this note, and what the post supplies is the order-of-magnitude spread between hardest and simple requests plus the statement that most users' costs stayed fairly constant. The sentence was an inferred economic mechanism presented as Truell's explanation, which is the SF2 shape a second time. Cut. The supported sentence before it now carries the point alone: 'The newest models consumed far more tokens on long-horizon tasks than a flat monthly price could cover.' REVERSING CONDITION: a passage in which Cursor states it had been absorbing the difference would license restoring it.


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

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE COST RANGE WAS WRONG AND STAGE 3 PASSED IT. The article gives an average of $150 to $250 and heavy-user spending of $500 to $2,000. The chapter said ’several hundred to several thousand’ and, before the Stage 6 copy edit, ’a few thousand’: BOTH endpoints were unsupported in both forms, so the copy edit did not cause this. The looseness was deliberate, recorded here as protection against a corrected figure, and it concealed the error from every checker who could not read the article. THE RATIONALE FOR LOOSENESS IS RETIRED and the chapter now carries the exact figures, which the fifty-year rule permits because the opening case is dated. THE COMPLEXITY CLAUSE IS CUT: the article does not attribute the range to the complexity of the work, and the workload mechanism is already carried by the two sentences after it. THE ADOPTION PERCENTAGES NOW LIVE HERE, 32 per cent in February and 84 per cent in March, which retires uber-2026-adoption and with it rulings S3-1 and S3-2. BYLINE CORRECTED to its published form, Janakiram MSV, which the register had inverted. STILL SECONDARY, and the upgrade is unchanged: The Information’s original carries the CTO confirmation and stayed paywalled to check A as well. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS A1 TO A6 OF THE VERIFICATION SHEET, ALL PASS. That covers the budget exhaustion and its April timing, that no contract was renegotiated and no vendor raised a price, the roughly five thousand engineers from December 2025, the per-engineer monthly cost range, the attribution of the variation to workload, and the usage-based commercial terms. A2 AND A5 WERE CHECKED SEPARATELY FROM THE FIGURES AND BOTH HOLD, which matters because each could have been the chapter’s inference rather than the article’s statement, and that is the shape of Chapter 1’s FC9. STILL SECONDARY. The chapter’s cost range remains deliberately loose, and the upgrade is unchanged: The Information’s original report carries the CTO confirmation and is paywalled. Verifying Forbes establishes that the reporting says what the chapter says it says, not that the underlying facts hold. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch 2026-08-21; the article itself has not been read by Claude, and the container cannot fetch it. Carries the budget exhaustion timing, the engineer count, the rollout date, and the per-engineer monthly cost range. Grade C until a primary is read. The chapter states the cost range as ’several hundred to a few thousand dollars’ rather than as exact bounds, deliberately, so that a corrected figure does not invalidate the sentence.

