# AIOM Case Bank v1.0 (WORKING DOCUMENT)

Textbook: *AI Operations Management*. Documented, citable real-world material per the evidence policy (every empirical claim cited, formalized, or cut).
Compiled July 19, 2026 from first research pass. Status: working; gaps listed at end.

Source grades: A = primary/official document or top-tier press (TechCrunch, Fortune, CBC, Forbes staff, official provider docs). B = reliable trade press. C = vendor/SEO content (pointer only; never cite; chase to primary before use).
Rule: before print, every case cites its Grade A primary source directly.

## Chapter 2 shopping list: flow episodes

### CASE 2.1 [RULED IN 2026-08-21]: Uber exhausts its 2026 AI budget in four months (December 2025 - May 2026)

- What happened, per converging secondary coverage: Uber rolled out Anthropic's
  Claude Code across roughly 5,000 engineers from December 2025. Reported adoption
  ran from 32 per cent of engineers in February 2026 to 84 per cent classified as
  agentic coding users in March; by spring, reporting cites 95 per cent using AI
  tools monthly and roughly 70 per cent of committed code originating from those
  tools. Monthly API cost per engineer is reported in a range of $500 to $2,000.
  The company's entire 2026 AI budget was reported exhausted by April, four months
  into the year. CTO Praveen Neppalli Naga is reported as confirming the overrun to
  The Information; Fortune reports the COO questioning whether the spending was
  worth it. Uber's 2025 research and development spend is reported at $3.4 billion.
- **WHY IT IS A STRONG CHAPTER 2 OPENING: all three flows are visible in one named
  deployment, and they are visibly uneven.** The usage flow is measured and rising.
  The record flow existed in part, since a per-engineer monthly cost range was
  knowable, but it did not reach the model finance was planning against. The
  cost-and-value flow is unreconciled: **the organization knows precisely what it
  spent and cannot say what it was worth.** That is C3's asymmetry, all of the cost
  and an unknown fraction of the value, with a named company attached rather than a
  statistic.
- **HANDLE WITH CARE, AND THE FIGURE DISCIPLINE IS NOT YET SET.** Adoption
  percentages, the per-engineer cost range and the budget-exhaustion timing come
  from secondary reporting that paraphrases a paywalled primary. Reported figures
  vary in framing across outlets. **No figure here may enter prose until a fact
  check clears it**, and the ruling on which figures are load bearing has not been
  made. This is the shape that produced the 14-versus-15 per cent discipline note
  on CASE 6.4.
- **THE VENDOR CONFLICT IS RULED AND MITIGATED, 2026-08-21.** The tool is Claude
  Code and Claude drafts this book, so the chapter opens on the drafting vendor's
  own product. **Dan ruled the case in and ruled the mitigation: all prose is run
  by a second model to check for bias.** That is the same independence he already
  applies to the Stage 2 developmental read, the Stage 4 craft read and the two
  external fact checks. The second conflict, that Chapter 1 also opens on an AI
  coding assistant, was ruled acceptable because the failures differ in kind:
  Chapter 1 is a provider-side correction landing on a buyer, and this is a buyer's
  own consumption outrunning its records and its budget, which is the buyer-side
  spine the competency framework asks for.
- **WHAT THE BIAS CHECK MUST LOOK FOR, because a vague instruction finds nothing:**
  language that softens Anthropic's role or Uber's exposure, any implication that
  the overrun reflects well on the tool, any asymmetry between how this chapter
  treats Claude Code and how Chapter 1 treats Cursor, and the reverse failure of
  overcorrecting into criticism the sources do not support. C6 already forbids hero
  and villain framing in both directions; this is that guard applied where the
  drafter has an interest.
- Sources to chase, none yet read in full: The Information (primary, carries the
  CTO confirmation, paywalled); Fortune, 2026-05-26; Forbes, Janakiram MSV,
  2026-05-17; AI Magazine; DesignRush. **Grade C until a primary is read.**
- Placement: Chapter 2 opening case, proposed.
- **Provenance, and this line is the scope claim: found 2026-08-21 by WebSearch
  only. Claude read search-result summaries and NOT any article.** WebFetch and
  curl are blocked by the container's egress proxy, verified against fortune.com
  the same day. Nothing here has been verified against a primary by Claude, and
  Stages 3 and 7 remain external.

### CASE 2.2 [RULED IN 2026-08-22]: The Australian Government whole-of-government trial of Microsoft 365 Copilot (January - June 2024)

- What happened, per converging secondary coverage: the Australian Government ran
  a six-month whole-of-government trial of Microsoft 365 Copilot from January to
  June 2024. Around sixty agencies took part, each nominating the staff who would
  receive licences, and several thousand licences were issued. The licence is
  priced per seat rather than by unit of use. The Digital Transformation Agency
  commissioned an independent evaluation, reported as conducted by Nous Group, and
  published it in full. Participants reported using the tool a few times a week or
  less and reported time savings from using it. The evaluation states that
  participants assessed the effects themselves, which may understate or overstate
  them, and that no measure of the work existed from before the trial began.
- **WHY IT EARNS A PLACE BESIDE CASE 2.1: it inverts the Uber shape.** Uber teaches
  a deployment that never built the value half at all. This teaches a deployment
  that commissioned independent evaluators to build it after the fact and still
  could not settle the question, because the apparatus has to exist before the
  deployment rather than after it. That is the craft section's retailer lesson with
  a real name attached. The per-seat licence also puts Chapter 1's meter relocation
  in front of the reader inside a real deployment, which discussion question 4
  already asks about.
- **THE COUNTS ARE NOT LOAD BEARING AND THE PROBLEM STATES NONE OF THEM
  PRECISELY.** Secondary coverage disagrees with itself on every count: agency
  counts of 56, almost 60 and more than 60 all appear, and participant or licence
  counts of more than 5,000, 5,765, nearly 6,000 and 7,600 all appear. The chapter
  says "around sixty agencies" and "several thousand licences" deliberately, so a
  corrected count does not invalidate the exercise. **Four claims are load bearing
  and Stage 3 must confirm exactly those:** that the licence is priced per seat
  rather than by unit of use; that agencies nominated their own participants; that
  an independent evaluation was commissioned and published in full; and that the
  evaluation stated both the self-assessment limitation and the absence of a
  pre-trial measure.
- Sources to chase, none yet read: the published evaluation itself (primary,
  Digital Transformation Agency, digital.gov.au); the DTA release announcing it;
  the separate Treasury evaluation of its own Copilot trial; secondary coverage in
  The Mandarin and ARN. **Grade C until a primary is read.** The publication date
  is recorded as the year only, because no source read gave a day.
- Placement: Chapter 2, problem P3, the independent three-flow mapping. **Ruled in
  by Dan on 2026-08-22 at Chapter 2 Stage 1**, on finding S1-2: competency C2's
  assessment specifies a mapping on a cited real deployment, the constructed
  insurer that first filled P3 did not satisfy it, and no already-banked case was
  free to take the slot.
- **Provenance, and this line is the scope claim: found 2026-08-22 by WebSearch
  only. Claude read search-result summaries and NOT the evaluation, any article
  about it, or any agency page.** WebFetch and curl are blocked by the container's
  egress proxy. Stages 3 and 7 remain external.


## Chapter 4 shopping list: provider mechanism episodes (the playing field)

### CASE 4.1: OpenAI loses money on flat-rate Pro subscriptions (January 2025)
- What happened: CEO Sam Altman publicly stated OpenAI was losing money on its $200/month ChatGPT Pro plan because "people use it much more than we expected," adding "I personally chose the price and thought we would make some money." Pro had launched in December 2024 with near-unlimited access.
- What it documents: fixed revenue against variable cost, mispriced by the provider itself; the usage distribution problem under flat rates. This is the C5 stylized-model assessment made real: the provider's own CEO conceding the mismatch.
- Sources: Altman post on X (primary, Jan 5-6 2025); Fortune; ITPro. Grade A.
- Placement: Ch4 opening case candidate (strongest option); also cited in Ch1 (flat-rate objection).

### CASE 4.2: Anthropic imposes weekly rate limits on Claude Code (July-August 2025)
- What happened: After Claude Code users ran the tool "continuously in the background, 24/7" and some resold account access, Anthropic announced weekly rate limits effective August 28, 2025 for Pro ($20) and Max ($100/$200) subscribers, on top of existing 5-hour rolling limits; overall weekly cap plus a separate cap for the top model; overflow purchasable at standard API rates; company said <5% of subscribers affected.
- Precursor mini-episode: on ~July 17, 2025, Anthropic tightened limits WITHOUT announcement; users discovered via "Claude usage limit reached" errors and suspected downgrades (TechCrunch, July 17, 2025).
- What it documents: the full mechanism menu live in one episode: limits, tiers, per-model caps, priority-by-plan, metered overflow; and (precursor) that corrections arrive on the provider's terms, sometimes without notice. The precursor empirically grounds Ch11's constraint scenario (mid-quarter limit change).
- Sources: TechCrunch (July 28, 2025); TechCrunch (July 17, 2025); Anthropic email/X announcement (primary). Grade A.
- Placement: Ch4 teaching body; Ch11 constraint-scenario grounding.

### CASE 4.3: Cursor repricing: flat allotment to usage-based, and the apology (June-July 2025)
- What happened: On June 16, 2025 Anysphere changed Cursor Pro from 500 fast requests + unlimited slow requests to $20 of usage billed at API rates; users exhausted allowances in a few prompts on expensive models and incurred surprise overage charges; CEO Michael Truell apologized ("we didn't handle this pricing rollout well") and refunded surprised users. Stated cause: newer models cost more to serve; company signed multi-year deals with OpenAI, Anthropic, Google, xAI.
- What it documents: the middle of the value chain (an AI application vendor) forced to convert flat pricing to metered pricing by its own upstream variable costs; cost pass-through cascading down the AI supply chain; the buyer-side planning failure when the correction arrives mid-subscription.
- Sources: TechCrunch (July 7, 2025); Truell blog post (primary). Grade A.
- Placement: Ch4 teaching body; also Ch1 (the flat-rate objection's real-world refutation).

### CASE 4.4: The priced mechanism menu: OpenAI service tiers (documented current state)
- What happened / state: OpenAI operates four processing tiers: Standard (default), Priority (premium per-token price for faster, more consistent performance, invoked per-request via service_tier="priority"), Flex (~50% discount, variable latency, may return 429 Resource Unavailable), Batch (~50% discount, 24-hour turnaround), plus Scale (committed throughput, 30-day minimum, 99.9% SLA).
- What it documents: allocation and priority pricing as a shipped product surface, not a prediction; and, for Ch11, the buyer's side of tier economics (routing work classes across price/latency tiers is literally supported by the provider's own API parameter).
- Sources: OpenAI official pricing/docs pages (primary). Grade A. Perishable: re-verify all specifics at drafting time; quarantine in dated case per fifty-year rule.
- Placement: Ch4 (mechanism menu evidence); Ch11 craft section (routing against real tier structures).

### CASE 4.6: GitHub Copilot dismantles flat pricing in two acts (June 2025 - June 2026)
- What happened: Act one, June 18, 2025: GitHub began enforcing monthly premium-request allowances for Copilot and letting customers pay for usage beyond them. Act two, announced April 27, 2026 and effective June 1, 2026: standard billing moved from premium requests to GitHub AI Credits denominated in tokens (input, output, and cached), priced at each model's published API rate. The transition carried stated exceptions: annual Pro and Pro+ subscribers remained on premium-request pricing until their terms expired, code completions and Next Edit Suggestions stayed included and consumed no credits, every plan retained a monthly credit allowance, and base subscription prices did not change. A preview bill experience launched in early May 2026 ahead of the transition. On its January 28, 2026 earnings call, four months before act two, Microsoft reported over 4.7 million paid Copilot subscribers, up 75 percent year over year.
- What it documents: the same correction as Case 4.3 reached by the opposite method and at far larger scale. Where Cursor corrected retroactively under public pressure with an apology and refunds, GitHub corrected on a published schedule, announced in advance, supported by tooling, across every plan. Paired with 4.3 the two convert anecdote into pattern and preempt the "one badly run startup" dismissal, which is exactly the work Ch1's opening case needs. The stated exceptions matter pedagogically: they show a repricing that is neither punitive nor disguised, so the structural account survives without any villain.
- Sources: GitHub Changelog, June 18, 2025 (primary, dated to the day of the change); The GitHub Blog, April 27, 2026 (primary); Microsoft FY26 Q2 earnings call, January 28, 2026 (primary, first-party disclosure per Decision 46). Grade A. Perishable: all three carry access dates in the Ch1 source register.
- Claim ruling: act one is NARROWED and the narrow form above is the only one cleared for reuse. Ruled 2026-08-06 at Ch1 Stage 3 (SF3). The entry formerly read that GitHub "began billing premium requests that had previously carried no separate charge". External check 1 raised that the changelog documents the change rather than the arrangement preceding it, and a dated changelog cannot establish a prior billing state it does not describe; external check 2 restated the original as sound, the two disagreed, and the narrower reading was ruled controlling. What the source carries is allowances enforced and a paid overage available, which is what the sentence now says. The act one, act two structure survives the narrowing. REVERSAL CONDITION: do not restore the prior-state contrast without a pre-2025-06-18 GitHub pricing or documentation artifact that describes the earlier arrangement in its own words.
- Placement: Ch1 opening case, paired with 4.3 (in use). Candidate for Ch4 teaching body.
- Provenance: added 2026-08-05 at Chapter 1 Stage 1, on Dan's ruling. The Consolidated Spec assigned "Case 4.6" to Ch1 Slot 1 but the bank held no such entry. Written from sources already cleared through the Ch1 register and its fact check, not from new research. Act one carried the pre-SF3 wording from that date until 2026-08-13, when a pre-public sweep found it: the ruling had been written into the Ch1 register note and never propagated here, which is why the bank now carries a Claim ruling line at all.

## Chapter 6 shopping list: value, productivity, ROI statements

### CASE 6.1: Klarna: the claim and the correction (February 2024 - May 2025)
- The claim: In February 2024, Klarna, jointly with OpenAI, announced its AI assistant handled 2.3M conversations in month one, two-thirds of customer-service chats, equivalent (by Klarna's estimate) to the work of 700 full-time agents, resolution time down from 11 minutes to under 2, projected $40M profit improvement for 2024. Company-reported figures announced jointly with the vendor supplying the model.
- The correction: In May 2025, CEO Sebastian Siemiatkowski told Bloomberg the cost-cutting drive had gone too far, produced "lower quality," and Klarna began recruiting human agents (an "Uber-type" flexible model) so customers could always reach a human. Headcount decline (roughly 5,000 toward 3,000-3,500 across the period) came substantially through attrition and a hiring freeze, complicating the "700 replaced" framing.
- What it documents: nearly every distinction Ch6 teaches in one episode: claimed vs realized value; vendor-joint self-reported figures; the boundary problem (what period, what outcomes, which confounds); productivity claim vs ROI; and the netting that was never published. Deliberate design echo: the Northmoor capstone (C18) is structurally a miniature Klarna with the netting actually performed.
- Sources: Klarna/OpenAI announcement Feb 2024 (primary); Bloomberg interview May 2025 (primary); CNBC on headcount; Forbes. Grade A. (Note: many secondary retellings are sloppy; cite primaries only.)
- Placement: Ch6 opening case (strongest option); referenced again in Ch12.

### CASE 6.2: MIT NANDA "The GenAI Divide: State of AI in Business 2025" (August 2025)
- What it says: Based on interviews with executives, employee surveys, and analysis of ~300 public AI deployments, the report found 95% of enterprise GenAI pilots delivered no measurable P&L impact; ~5% achieved rapid value; >80% of organizations had piloted tools while ~40% reported deployment, mainly boosting individual productivity rather than measurable enterprise outcomes; budgets skewed to sales/marketing while better returns sat in back-office functions; and a "shadow AI economy" with personal-tool use in the large majority of firms.
- Handle with care: the 95% figure went viral and drew methodological criticism; reported methodology descriptions vary across outlets (52 vs 150 interviews). Use the report's own text, state its method plainly, and cite the criticism's existence per the straight-spine policy (state limitation once, no hedging).
- What it documents: the unknown-value-fraction claim (C3) at market scale: high adoption, unmeasured transformation; also budget misallocation and shadow usage.
- Sources: MIT NANDA report (primary; obtain the PDF); Fortune interview with lead author Aditya Challapally. Grade A with noted caveats.
- Placement: Ch2 or Ch6 teaching body; candidate for Ch3 discussion questions (have students critique the study's boundary discipline: a beautiful self-referential exercise).

### CASE 6.3: [GAP] Classifiable value statements needed, and the requirement GREW on 2026-08-21

- **The count was six. Decision 74 raises what the set must COVER rather than
  simply its size.** C3's spot-the-error moved into C6's sort-and-repair, so the
  cited statements must now include at least one each of claimed-as-realized,
  netting-against-access-price, and adoption-as-value, alongside the
  claimed/realized/productivity/measurement/ROI classification the assessment
  already required.
- **NETTING-AGAINST-ACCESS-PRICE IS THE HARD ONE TO SOURCE and it is not a value
  error.** It is a cost error: a return set against the subscription price while
  the consumption cost is ignored. A statement exhibiting it has to name a price
  and a benefit in the same breath, which is rarer in public sources than a bare
  productivity claim.
- This gap was already the thinnest supply in the bank, and Chapter 2 has since
  taken CASE 6.2, which was dual-placed for Chapter 2 or Chapter 6. **Chapter 6's
  case supply should be built before Chapter 6 is drafted, not during.**
- **A CANDIDATE WAS FOUND AND DELIBERATELY WITHHELD FROM CHAPTER 2, 2026-08-22.**
  Pennsylvania ran a twelve-month pilot of ChatGPT Enterprise across 175 employees
  in fourteen agencies and published a report in March 2025. The reported headline
  is an average of 95 minutes saved per day, restated publicly by the governor as
  eight hours a week. **That is a self-reported productivity claim published as a
  value figure, which is exactly what this gap is short of.** It surfaced while
  searching for a Chapter 2 mapping case and was passed over for that purpose on
  the reasoning that Chapter 2 would spend it on one flow-mapping exercise and
  Chapter 6 would lose its clearest specimen. **Grade C, found by WebSearch, no
  report and no article read.** It also carries a second usable statement, a
  reported reduction of thirty days in onboarding time.
- The C6 sort-and-repair assessment needs ~8 short real statements spanning the classification set (claimed value, realized value, productivity claim, productivity measurement, ROI claim). Have: Klarna (multiple statements), MIT-quoted executive lines. Need: earnings-call and press-release specimens from large deployers. Research pass 2 targets: major-bank AI value claims, big-tech Copilot seat claims, consultancy ROI multipliers (e.g., IDC/Microsoft "$3.7x" genre), retailer/airline deployment claims.

### CASE 6.4: Generative AI at work: the contact-center deployment (QJE, 2025)
- What it is: Brynjolfsson, Li, and Raymond, "Generative AI at Work," Quarterly Journal of Economics 140(2), 889-942, DOI 10.1093/qje/qjae044. A customer-support contact center deploying a generative AI assistant that drafts suggested replies for agents, drawing on a knowledge base and the conversation so far. Published figures: 5,172 agents, and a 15 percent average increase in issues resolved per hour.
- FIGURE DISCIPLINE, LOAD-BEARING: the widely circulated 14 percent and 5,179 figures come from the 2023 NBER working paper and must not be used anywhere in the book. Cite the published QJE figures only.
- What it documents: for Ch1, a real described deployment whose shape carries the consumption-event inventory, at a scale where the seat count and the event count visibly separate. For Ch6, realized value with a stated boundary, where the study is reported rather than adapted.
- WHAT IT DOES NOT SUPPLY: the event architecture. Retrieval calls, conversation-close tagging, per-token metering, and all volume assumptions in the Ch1 worked inventory are stipulated for that exercise and are not described by the study. Ruled 2026-07-29: Ch1 labels the worked example a stylized application by a provenance line rather than binding it to the study's parameters, says "on the order of five thousand agents," and states no productivity figure at all, on the reasoning that a precise count above a stipulated inventory would falsely signal that the whole inventory is reported. The precise 5,172 belongs to Ch6, where the study is reported. Re-affirmed at Ch1 Stage 1, 2026-08-05.
- Sources: QJE 140(2), 889-942, cited by DOI (primary). Grade A. Non-perishable: cited by DOI, so no access date is required.
- Placement: Ch1 craft section, the consumption-event inventory (in use). Ch6 anchor case on realized value.
- Provenance: added 2026-08-05 at Chapter 1 Stage 1, on Dan's ruling. The Consolidated Spec assigned "Case 6.4" to Ch1 Slot 3 but the bank held no such entry. Written from the source already cleared through the Ch1 register and its fact check, not from new research.

## Chapter 5 shopping list: cost anatomy episodes

### CASE 5.1: Air Canada chatbot liability: Moffatt v. Air Canada (February 2024)
- What happened: Air Canada's website chatbot told a passenger he could apply for bereavement fares retroactively within 90 days; actual policy forbade retroactive claims. The BC Civil Resolution Tribunal found negligent misrepresentation, rejected Air Canada's argument that the chatbot was "a separate legal entity responsible for its own actions" ("a remarkable submission"), found the airline "did not take reasonable care to ensure its chatbot was accurate," and awarded C$812.02 (C$650.88 fare difference + interest + fees).
- What it documents: the error-cost category of the TCO ledger with a court-quantified number; error exposure scales with deployment (PROP-156-160 territory); also governance cost rationale.
- Sources: CBC News (Feb 2024); Tribunal decision text (primary); American Bar Association note; Forbes. Grade A.
- Placement: Ch5 teaching body (error and governance cost categories); alternative Ch5 opening case.

### CASE 5.2: Shadow AI and the invisible flow (2023-2026 pattern, multiple sources)
- Documented pattern: IBM's 2025 Cost of a Data Breach Report found breaches involving shadow AI averaged $670,000 MORE than other incidents, with 97% of breached organizations lacking AI access controls; an IDC 2025 survey found 56% of employees using unauthorized AI tools vs 23% using organization-governed tools; the Samsung 2023 episode (engineers pasting source code and internal material into a public chatbot within a month, prompting a ban, later reversed toward an internal tool) is the canonical incident.
- What it documents: the record flow's absence has a price; unmetered activity is invisible to the management boundary (THM-010 territory); motivates Ch8's coverage test and shadow-usage estimate. Northmoor's designer/marketer shadow usage mirrors this pattern.
- Sources: IBM Cost of a Data Breach 2025 (primary; obtain report); IDC survey (chase primary); Samsung episode (contemporaneous 2023 reporting; chase primary). Grade A for IBM; B pending primaries for the rest.
- Placement: Ch8 opening case or teaching body.

## Cross-cutting notes

- PERISHABILITY: every price, tier name, and limit above is perishable. Per the fifty-year rule, all appear only inside dated case studies ("In July 2025, ..."), never in body prose.
- PRIMARY-SOURCE CHASE LIST before print: Altman X post; Anthropic announcement; Truell blog post; Klarna Feb 2024 press release; Bloomberg May 2025 interview; MIT NANDA report PDF; BC CRT decision text (2024 BCCRT 149); IBM CoDB 2025 report; IDC survey; Samsung 2023 contemporaneous reporting; OpenAI docs snapshots (archive on capture date).
- BALANCE FLAG: current bank skews cautionary. The book needs at least one well-documented POSITIVE value-realization case (a deployment with an honest published boundary and surviving number) or reviewers will read the discipline as pessimism rather than measurement. Research pass 2 priority.

## Research pass 2 targets (open)

1. Six more classifiable value statements for the C6 sort-and-repair set (earnings calls, press releases).
2. One or more documented positive ROI/value cases with real boundaries.
3. Opening-case candidates for chapters without one: Ch1, Ch2, Ch3, Ch7, Ch9, Ch10, Ch13, Ch14, Ch15.
4. FinOps Foundation: current framework text and State of FinOps survey data on AI spend (Ch14 boundary treaty; engage by name).
5. Token-price volatility evidence (OpenRouter or equivalent) to support or replace the manifesto's PMT claim.
6. Model deprecation/forced-migration episodes for Ch7 switching economics.
7. Verify the "Northmoor" trade-name collision check (logged from dataset session).

## Status

Structure document open item 4: IN PROGRESS (pass 1 complete, pass 2 targets defined).
