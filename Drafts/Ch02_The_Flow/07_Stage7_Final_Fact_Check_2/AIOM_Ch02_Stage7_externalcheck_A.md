# Chapter 2, Stage 7. External check A, as received.

Received 2026-08-30 from Dan. Recorded here as the check Dan rules on.
**Claude rules none of it.**

**NOTHING IS EDITED.** The response carried no em dash and no en dash, so unlike the
Stage 3 check it needed no punctuation alteration at all. No finding is reworded,
reordered, softened or summarized.

**THIS IS THE FIRST CHECK IN THE PROJECT WITH LIVE WEB ACCESS, and it says so in its
first line.** Every previous external check on this book, on both chapters, reported no
web access and reasoned from memory. This one opened Forbes, Fortune, the first-party
Rapid Response transcript, the Australian Government's full evaluation, Microsoft's
pricing announcement and the MIT report. That is a different KIND of evidence from
anything the project has had, and it is why four claims are contradicted rather than
carried.

**THE PACKET WAS NOT SUPPLIED TO IT, and the checker flags this itself at the end.**
It therefore could not see the twelve rulings in force or their REVERSES-IF conditions.
Claude ran that comparison afterwards and it is recorded in
`AIOM_Ch02_Stage7_rulings_to_make.md`, which is the file to read next.

---

# Chapter 2, Stage 7: External fact check A

**Live web access: YES.** I opened the cited Forbes and Fortune articles, the first-party Rapid Response transcript, the Australian Government's full trial evaluation, Microsoft's contemporaneous pricing announcement, the MIT NANDA report, and MIT's official NANDA page. The underlying *Information* article remained paywalled, so I do not treat claims available only through secondary retellings as independently confirmed by that primary account.

## Executive ruling

The chapter's central Uber facts are substantially sound: the budget was gone by April, the rollout began in December 2025 across roughly 5,000 engineers, and Andrew Macdonald's remark did refer specifically to Claude Code. The sentence giving a monthly cost range is not supported and should be corrected.

Problem P3 also rests on a real, accessible government evaluation, and most of its trial facts hold. Two material claims do not. The evaluation was jointly delivered by the DTA and Nous Group, not independent, and the report did not identify the two methodological limits in the way the problem says it did. It explicitly names several limitations, including self-assessed productivity. It does not identify the absence of a pre-trial work baseline as one of them.

The MIT passage is sound in substance, including the words "no measurable P&L impact." Its citation needs the four authors and the report's July 2025 date.

### Disposition

| Verdict | Count | Consequence |
| --- | ---: | --- |
| VERIFIED | 17 | May stand, with the qualifications recorded below |
| CONTRADICTED | 4 | Requires correction before lock |
| CANNOT CONFIRM | 3 | Requires narrower wording or a stronger source |
| MIXED | 1 | One clause is verified and one is contradicted |

The count treats compound claims separately where one clause passes and another fails.

## Priority findings: the five changed passages

### 1. Monthly spending range

**PDF sentence, page 2:** "Reported monthly spending ranged from several hundred to several thousand dollars, depending on how often each engineer used Claude Code and the complexity of the work."

**Checked against:** [Janakiram MSV, Forbes, May 17, 2026](https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/).

**Source language:** Forbes gives average monthly spending of "$150 to $250" and power-user spending of "$500 and $2,000."

**Verdict: CONTRADICTED.** The source supports neither endpoint in the PDF. The reported low end is below several hundred dollars, and the reported high end is $2,000, not several thousand dollars. The earlier wording "a few thousand" is also too high.

**Remedy:** "Reported monthly spending averaged $150 to $250 per engineer, while power users spent between $500 and $2,000."

The Forbes article says workflow choice can change invoices, but it does not expressly attribute the observed range to "the complexity of the work." If that causal explanation stays, it needs its own support.

### 2. What Macdonald could not connect to consumer features

**PDF sentence, page 3:** "Yet president and chief operating officer Andrew Macdonald said the company still could not connect its growing use of Claude Code to the consumer features it was producing."

**Checked against:** [Fortune, May 26, 2026](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/) and the [first-party Rapid Response transcript](https://mastersofscale.com/ubers-swerve-on-gas-prices-hotels-a-driverless-future/).

**Source language:** The transcript asks what moved above the line because "25% of our code commits were via Claude Code last quarter."

**Verdict: VERIFIED.** The surrounding discussion concerns AI use and token consumption generally, but the concrete statistic Macdonald tests against consumer output is explicitly Claude Code. Fortune's paraphrase is faithful.

### 3. Budget exhaustion, date, and verb

**PDF sentence, page 1:** "By April 2026, just four months into the year, Uber had already exhausted its annual AI budget."

**Checked against:** [Forbes](https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/), [Fortune](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/), and the [Rapid Response transcript](https://mastersofscale.com/ubers-swerve-on-gas-prices-hotels-a-driverless-future/).

**Source language:** Forbes says Uber "exhausted its entire 2026 artificial intelligence budget by April."

**Verdict: VERIFIED.** "Exhausted" and "by April" are directly supported by the cited Forbes source. The first-party transcript is consistent and may place the disclosure earlier, around mid-March, although Macdonald marks that recollection as approximate. One precision point remains: Fortune calls it the 2026 AI coding-tools budget, while Forbes and Macdonald use the broader "AI budget."

### 4. "Tools" in the plural

**PDF sentence, page 1:** "Engineers were simply doing the work the company had asked them to do by using the tools it had given them."

**Checked against:** the same Forbes and Fortune accounts and the first-party transcript.

**Source language:** The reporting names Claude Code as the tool tied to the overrun. Fortune also refers generically to an AI coding-tools budget and total AI-tool usage, without identifying a second tool that caused the overrun.

**Verdict: CANNOT CONFIRM.** The public sources establish that Uber used multiple AI systems more broadly, but the cited opening case identifies one named tool, Claude Code, as the driver of this episode. The plural implies evidentiary breadth the sources do not supply.

**Remedy:** "Engineers were simply doing the work the company had asked them to do by using the tool it had given them."

### 5. "The evaluation identified two limits"

**PDF sentence, pages 24-25:** "The evaluation identified two limits in its method: participants assessed the effects themselves, which could understate or overstate them, and no measure of the work existed from before the trial."

**Checked against:** [DTA full report, executive summary](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/executive-summary-glossary), [Appendix B: Methodology](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/appendix-b), and the [productivity section](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/productivity).

**Source language:** Appendix B labels five categories under "Limitations" and expressly says productivity impacts relied on participant self-assessment.

**Verdict: CONTRADICTED.** The report does not identify only two limitations. It lists representativeness, positive selection bias, inconsistent rollout, evaluation fatigue, and self-assessment. The report does not name the absence of a pre-trial work baseline as a limitation. It did conduct a pre-use survey, but that survey primarily baselined sentiment and confidence, not objective task time or output.

**Remedy:** "The evaluation identified several limits in its method. Its productivity findings relied on participants' self-assessments, which could understate or overstate the effects. The published methodology reports no objective pre-trial measure of task time or output."

This preserves the instructional point while distinguishing the report's own finding from an inference drawn from its disclosed method.

## Australian DTA trial

### 6. Trial period

**PDF sentence, page 24:** "Between January and June 2024, the Australian Government ran a whole-of-government trial of Microsoft 365 Copilot."

**Checked against:** [DTA announcement](https://www.dta.gov.au/articles/evaluation-whole-government-trial-generative-ai-now-available) and [Appendix B](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/appendix-b).

**Source language:** The methodology table gives "1 January" through "30 June" as the trial period.

**Verdict: VERIFIED.** Evaluation activity continued into July and report preparation into August, but the trial itself ran January 1 through June 30, 2024.

### 7. Number of participating agencies

**PDF sentence, page 24:** "Around sixty agencies participated."

**Checked against:** [DTA announcement](https://www.dta.gov.au/articles/evaluation-whole-government-trial-generative-ai-now-available) and [Appendix A](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/appendix-a).

**Source language:** The public announcement says "60+ government agencies"; Appendix A says almost 60.

**Verdict: VERIFIED.** "Around sixty" is the right level of precision because the government's own pages do not use one consistent formulation.

### 8. Number of licences

**PDF sentence, page 24:** "The government issued several thousand licences."

**Checked against:** the DTA announcement, full-report executive summary, and Appendix A.

**Source language:** The three official locations report more than 7,600 staff, more than 5,765 licences, and more than 7,769 licences, respectively.

**Verdict: VERIFIED.** Every official count supports "several thousand." The underlying official record is internally inconsistent, however. The chapter should not replace its generic wording with a precise count until DTA resolves the discrepancy.

### 9. Recipient nomination

**PDF sentence, page 24:** "Each agency nominated the employees who would receive licences."

**Checked against:** [full-report executive summary](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/executive-summary-glossary) and [Appendix B](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/appendix-b).

**Source language:** The executive summary says agencies nominated staff for licences. Appendix B adds that participants self-nominated or were identified by agencies.

**Verdict: VERIFIED.** The sentence accurately describes the allocation mechanism, although it omits the participant self-nomination route. "Agencies nominated or approved the staff who received licences" would capture both accounts more safely.

### 10. Seat pricing

**PDF sentence, page 24:** "The product was priced per seat rather than by unit of use."

**Checked against:** [DTA Appendix A](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/appendix-a) and Microsoft's [January 2024 commercial announcement](https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/).

**Source language:** DTA describes agencies purchasing licences; Microsoft priced the product at $30 per user per month.

**Verdict: VERIFIED.** The fact is correct. The DTA evaluation alone does not state the contrast with unit-of-use pricing, so the sentence needs a Microsoft pricing citation as well as the DTA citation.

### 11. Independent evaluation

**PDF sentence, page 24:** "The Digital Transformation Agency commissioned an independent evaluation and published it in full."

**Checked against:** the full-report executive summary and Appendix B.

**Source language:** Appendix B says the evaluation was "jointly delivered by the DTA and Nous."

**Verdict: CONTRADICTED.** Nous Group was engaged to assist, analyze data, conduct interviews and focus groups, and develop the report. DTA designed the evaluation plan and data collection method, and a government steering committee endorsed the final reports. That is an externally assisted joint evaluation, not an independent evaluation.

**Remedy:** "The Digital Transformation Agency engaged Nous Group to assist with the evaluation and published the full report."

### 12. Publication in full

**PDF sentence:** Same sentence as Finding 11.

**Checked against:** the [DTA trial landing page](https://www.digital.gov.au/initiatives/copilot-trial) and [full report](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full).

**Source language:** The landing page identifies separate summary and full reports and describes the latter as detailed analysis with data tables and methodology.

**Verdict: VERIFIED.** The full report is publicly accessible as a set of linked HTML pages rather than a single PDF.

### 13. Frequency of use

**PDF sentence, page 24:** "Participants reported using the tool a few times a week or less and saving time when they used it."

**Checked against:** [employee-related outcomes](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/employee-related-outcomes) and [productivity](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/productivity).

**Source language:** The frequency table reports 1 percent not at all, 21 percent a few times monthly, and 46 percent a few times weekly.

**Verdict: VERIFIED.** Sixty-eight percent used Copilot a few times a week or less. The time-savings clause is also supported as a participant-reported or perceived result, not as an independently timed result.

### 14. Participant self-assessment

**PDF sentence, pages 24-25:** "Participants assessed the effects themselves, which could understate or overstate them."

**Checked against:** Appendix B.

**Source language:** The report says self-assessment may understate or overstate impacts, particularly estimated time savings.

**Verdict: VERIFIED.** This is an explicit limitation in the report.

### 15. No pre-trial measure of the work

**PDF sentence, page 25:** "No measure of the work existed from before the trial."

**Checked against:** Appendix B and the productivity section.

**Source language:** The disclosed method includes pre-use, pulse, and post-use surveys, but only three questions were repeated for before-and-after comparison, focused on sentiment and confidence.

**Verdict: CANNOT CONFIRM.** The report does not say that no prior work measure existed. It also does not disclose an objective pre-trial baseline for task time, output volume, or output quality. The defensible claim is about what the published methodology reports, not about what did or did not exist anywhere in the agencies.

**Remedy:** "The published methodology reports no objective pre-trial measure of task time or output."

### 16. Document identity, author attribution, and location

**PDF footnote 9:** "Evaluation of the whole-of-government trial of Microsoft 365 Copilot," Australian Government Digital Transformation Agency, 2024.

**Verdict: VERIFIED WITH A REQUIRED ATTRIBUTION UPDATE.**

- **Title:** *Evaluation of the whole-of-government trial of Microsoft 365 Copilot*.
- **Author attribution:** No conventional personal byline appears. The report says it was jointly delivered by the Digital Transformation Agency and Nous Group.
- **Location:** [Australian Government, digital.gov.au, full report](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full).
- **Recommended citation:** Digital Transformation Agency and Nous Group, *Evaluation of the Whole-of-Government Trial of Microsoft 365 Copilot: Full Report* (Australian Government, 2024).

## MIT NANDA report

### 17. Headline finding

**PDF sentence, page 13:** "A 2025 MIT NANDA study of enterprise deployments reported a striking gap: 95 percent of enterprise generative AI pilots produced no measurable impact on profit and loss."

**Checked against:** [*The GenAI Divide: State of AI in Business 2025*](https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf), a mirror of the report formerly distributed through NANDA's official access form, and [MIT's official NANDA page](https://www.media.mit.edu/groups/nanda/overview/).

**Source language:** The executive summary says the vast majority remained stuck with "no measurable P&L impact."

**Verdict: VERIFIED IN SUBSTANCE.** The report directly supports the 95-to-5 split and the absence of measurable P&L impact. Its units shift between organizations, integrated pilots, and custom enterprise AI tools. The PDF sentence presents those as one clean population. That is acceptable as a headline paraphrase but less exact than the report.

**More exact remedy:** "The report found that only 5 percent of integrated AI pilots were extracting millions in value, while the remainder showed no measurable P&L impact."

### 18. Whether "no measurable impact" is the report's own phrase

**PDF sentence, page 13:** "The methodological dispute does not need to be settled for the finding to illustrate the problem, because the crucial phrase is no measurable impact."

**Verdict: VERIFIED.** The report itself uses "no measurable P&L impact." The chapter's expansion of P&L to "profit and loss" is accurate.

### 19. Author line

**PDF footnotes 7 and 8:** The citation names only the title and MIT NANDA.

**Checked against:** the report cover.

**Verdict: CONTRADICTED AS CITATION METADATA.** The author line is Aditya Challapally, Chris Pease, Ramesh Raskar, and Pradyumna Chari. A press-ready citation should name them.

### 20. Publishing body and date

**PDF footnotes 7 and 8:** "MIT NANDA, August 2025."

**Checked against:** the report cover, notes page, and MIT's official NANDA page.

**Verdict: PARTLY VERIFIED, PARTLY CONTRADICTED.** "MIT NANDA" appears on the cover and is a defensible short imprint. The notes call the work preliminary findings from Project NANDA, and MIT identifies NANDA as a Media Lab project. "Project NANDA, MIT Media Lab" is the clearer institutional form. The report is dated **July 2025**, not August 2025. August was the public-news cycle, not the report date printed on the document.

**Recommended citation:** Aditya Challapally, Chris Pease, Ramesh Raskar, and Pradyumna Chari, *The GenAI Divide: State of AI in Business 2025* (Project NANDA, MIT Media Lab, July 2025), preliminary findings.

## Remaining Forbes and Fortune attributions

### 21. Engineer count and rollout date

**PDF sentence, page 1:** "Uber had begun rolling it out to roughly 5,000 engineers in December 2025."

**Checked against:** Forbes.

**Source language:** Forbes reports a December 2025 rollout across roughly 5,000 engineers.

**Verdict: VERIFIED AGAINST THE CITED SECONDARY SOURCE.** The underlying *Information* article could not be read without a subscription, so the primary account remains unconfirmed in this session.

### 22. Adoption in February and March

**PDF sentence, page 1:** "By February, about a third of the engineering organization was using it. A month later, usage had spread to a large majority."

**Checked against:** Forbes.

**Source language:** Forbes reports adoption rising from 32 percent in February to 84 percent in March.

**Verdict: VERIFIED.** The chapter's characterization is accurate. Footnote 3 should identify an actual source rather than "Multiple secondary outlets" if the book's standard is document-level verification.

### 23. Share of committed code

**PDF sentence, page 1:** "Press reports indicated that by spring, a large share of committed code had passed through it."

**Checked against:** Forbes and the first-party transcript.

**Source language:** Macdonald refers to 25 percent of code commits via Claude Code in the prior quarter; Forbes reports a higher AI-assisted share but notes varying definitions.

**Verdict: VERIFIED IN SUBSTANCE.** "A large share" is supported, but "passed through" has no stable technical definition. If the number matters pedagogically, use the first-party 25 percent formulation and define whether it means assisted, generated, or committed without human intervention.

### 24. Direct quotation

**PDF sentence, page 3:** "'That link is not there yet,' he said."

**Checked against:** Fortune and the first-party transcript.

**Source language:** Fortune prints "That link is not there yet" and the transcript preserves the same words in the Claude Code discussion.

**Verdict: VERIFIED.** The excerpt is accurate. The spoken version continues with "right?", but omitting that tag does not change the meaning.

### 25. Forbes author name in the footnotes

**PDF footnotes 1, 2, and 5:** "MSV Janakiram."

**Checked against:** the Forbes byline.

**Verdict: CANNOT CONFIRM AS CURRENTLY STYLED.** Forbes displays the byline as "Janakiram MSV." The book should follow the author's published form unless its citation system has separately verified which element is the family name.

## Required corrections before chapter lock

1. Replace the monthly cost range with the exact Forbes figures.
2. Revert "tools" to singular unless a source identifying multiple contributing tools is added.
3. Replace "independent evaluation" with "evaluation jointly delivered by the DTA and Nous Group" or equivalent.
4. Replace "identified two limits" with wording that separates the report's explicit self-assessment limitation from the chapter's inference about the absence of an objective work baseline.
5. Add a Microsoft source for the per-user pricing claim.
6. Add the four MIT report authors and change August 2025 to July 2025.
7. Name actual sources in footnotes 3 and 4. "Multiple secondary outlets" is not a document a later checker can reopen.
8. Attribute the DTA full report jointly to DTA and Nous Group.

## Source-access limitation

The expected `AIOM_Ch02_Stage7_packet.md` was not supplied. I therefore could not see the source-register notes, prior rulings, or `REVERSES-IF` conditions. I did not knowingly reopen a ruled finding, but I cannot certify compliance with that instruction without the packet. The underlying *Information* account was also paywalled. Findings 21 through 23 verify what the cited accessible sources say, not the inaccessible original reporting behind them.
