# Chapter 1, Stage 3. Claim inventory and source packet

Generated from the live text for the Stage 3 source and fact check. Two external
checks run against this packet plus the render, on different prompts, per the
practice established 2026-08-06.

LIVE TEXT      `Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`
RENDER         `AIOM_Ch1_Stage3_FactCheck_Input_v3.pdf`, 25 pages, built this session,
               all fourteen gates green.

WHAT THIS IS. Every passage in the chapter that carries a citation marker, with
the keys it cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for the
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. Findings SF1 through SF6 were ruled
2026-08-06 and their rulings are recorded in the register notes below. A checker
who reaches one of them should say whether the condition named in the note is
now met, not restate the finding. SF6, archive capture and second paths, is
closed on Decisions 30 and 48 and has now been raised four times.

MECHANICAL CHECKS ALREADY RUN THIS SESSION, so they need not be repeated:

  Register closure    11 keys defined, 11 cited. Zero orphans, zero dangling.
  Citation markers    6 cited passages, every marker resolving to a register key.
  Footnote build      6 footnotes generated, all falling on their calling page (gate 8).

---

## Part 1. Cited passages, in document order

### C1. Two subscriptions, one correction

CLAIM TEXT AS IT STANDS

> On July 4, less than three weeks after the change, Michael Truell, chief executive of Anysphere, the company behind Cursor, apologized and promised refunds for charges incurred during the transition. His explanation reduced the dispute to arithmetic. The newest models consumed far more tokens on long-horizon tasks than a flat monthly price could cover. Cursor had been paying the difference, but the difference had become too expensive to absorb.

CITES: `truell-2025-pricing`, `techcrunch-2025-cursor-apology`

IN-CHAPTER GLOSS: The Cursor post describes the change of June 16 and the clarification of June 30. The TechCrunch report carries Truell’s role and title.

### C2. Two subscriptions, one correction

CLAIM TEXT AS IT STANDS

> Microsoft’s scale changed how the pricing correction arrived, but not whether the underlying economics required it. On January 28, 2026, four months before that change, the company told investors on its earnings call that Copilot had passed 4.7 million paid subscribers and was growing 75 percent year over year. If a provider can fund the gap between a flat price and the cost of the resource that price buys, then it controls the timing and the form of the correction. That control is what buys advance notice, a published schedule, and tooling that shows customers the effect before it lands. If a provider cannot fund the gap, the gap sets the timing instead. Scale made the correction orderly. It did not make the variable cost disappear.

CITES: `github-2025-premium`, `github-2026-usage`, `microsoft-2026-q2`

IN-CHAPTER GLOSS: The Microsoft earnings call carries the subscriber figure and the growth rate.

### C3. Two subscriptions, one correction

CLAIM TEXT AS IT STANDS

> From the buyer’s side, the two pricing corrections looked very different. Cursor changed its plan without warning, then apologized and issued refunds after customers objected. GitHub announced its change in advance, published a schedule, and gave customers tools to preview the effect on their bills. The execution differed. The economic correction was the same.

CITES: `github-2025-premium`, `github-2026-usage`

IN-CHAPTER GLOSS: Act one sits on the GitHub Changelog, dated June 18, 2025. Act two was announced April 27, 2026, with a preview bill experience launched in early May ahead of the June 1 transition.

### C4. Two subscriptions, one correction

CLAIM TEXT AS IT STANDS

> OpenAI provided an early example. Chief executive Sam Altman said publicly that the company was losing money on its two-hundred-dollar Pro subscriptions because customers were consuming more computing resources than the monthly price covered. He also acknowledged that he had personally set the price. The problem was not the price of access. Actual consumption had exceeded the assumption built into it.

CITES: `altman-2025-pro`, `techcrunch-2025-altman-pro`

IN-CHAPTER GLOSS: The TechCrunch report reproduces both statements.

### C5. Two subscriptions, one correction

CLAIM TEXT AS IT STANDS

> Eleven days later, the company announced two new weekly usage caps in addition to its existing five-hour limits. The caps would take effect the following month for every subscriber, regardless of renewal date. Customers on the highest-priced plan could continue using Claude Code beyond those limits by purchasing additional usage at standard API rates. The subscription price remained intact, but the amount of consumption included within it now had a clearer boundary.

CITES: `anthropic-2025-limits`, `techcrunch-2025-anthropic-limits`, `techcrunch-2025-anthropic-tightening`

IN-CHAPTER GLOSS: The announcement set two weekly caps, effective August 28, 2025, in addition to five-hour limits that were already in force and had been tightened on July 17, 2025.

### C6. The consumption-event inventory

CLAIM TEXT AS IT STANDS

> Consider a customer-support organization that has deployed a generative AI assistant across its contact center. For each incoming customer message, the assistant drafts a suggested reply that the agent may edit and send; the assistant draws on a knowledge base and on the conversation so far. The deployment covers a large agent population, on the order of five thousand agents, and the organization currently accounts for it as a per-seat tool.

CITES: `brynjolfsson-2025-genai`

IN-CHAPTER GLOSS: The study supplies the setting and the scale of the agent population. The event architecture and the volumes used below are stipulated for this exercise and are not reported by the study. It returns in Chapter 6 as the book’s anchor case on realized value.

---

## Part 2. Register entries, alphabetical

### `altman-2025-pro`

Cited in 1 passage.

- AUTHORS: Altman, Sam
- TITLE: Post on X on ChatGPT Pro subscription economics
- DATE: 2025-01-05
- URL: https://x.com/sama/status/1876104315296968813
- PERISHABLE: True
- ACCESSED: 2026-07-28
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Posted 2025-01-05 19:11 US Pacific, which is 2025-01-06 03:11 UTC. X displays 'January 6, 2025' to viewers outside the Americas. The book dates it January 5, 2025, matching US time and TechCrunch's same-day 'on Sunday' report. Flag for fact check so the UTC display is not read as an error. Second path: techcrunch-2025-altman-pro. SUPERLATIVE CUT 2026-08-06 (Stage 3, SF1, raised independently by both external checks). The sentence formerly opened 'The chief executive of the largest provider'. Neither this post nor techcrunch-2025-altman-pro establishes 'largest', and no metric was named, so the descriptor was unsourceable on the standing rule. Ruled: name the firm instead. The sentence now reads 'OpenAI's chief executive, Sam Altman, stated publicly', naming the person as well as the firm, which matches the Truell treatment in the opening case. The superlative must not return in any form, including 'one of the largest', which asserts a market position on no stated metric and hedges. What the two sources do carry, and all they carry, is that the company was losing money on the two-hundred-dollar Pro tier because subscribers used it more than the price assumed, and that Altman set the price himself. Do not generalize that to OpenAI's subscriptions as a whole.

### `anthropic-2025-limits`

Cited in 1 passage.

- AUTHORS: Anthropic
- TITLE: post on X announcing new weekly rate limits for Claude Pro and Max
- DATE: 2025-07-28
- URL: https://x.com/AnthropicAI/status/1949898502688903593
- PERISHABLE: True
- ACCESSED: 2026-07-28
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Announced 2025-07-28 by email to subscribers and by this post; effective 2025-08-28. The X post is the canonical public form. The chapter's clause about limits already in force and tightened earlier in July rests on techcrunch-2025-anthropic-tightening, added 2026-07-29, and secondarily on techcrunch-2025-anthropic-limits, not on this post.

### `brynjolfsson-2025-genai`

Cited in 1 passage.

- AUTHORS: Brynjolfsson, Erik; Li, Danielle; Raymond, Lindsey
- TITLE: Generative AI at Work
- CONTAINER: Quarterly Journal of Economics
- VOLUME: 140
- ISSUE: 2
- PAGES: 889-942
- DATE: 2025
- DOI: 10.1093/qje/qjae044
- URL: https://doi.org/10.1093/qje/qjae044
- PERISHABLE: False
- ACCESSED: 
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> NOTE ADDED 2026-07-29 (Stage 2, contact-center misattribution). This entry previously carried no note despite drawing four raises across three fact-check rounds. WHAT THE STUDY SUPPLIES to Chapter 1: the setting, a customer-support contact center with a generative AI assistant, and the scale of the agent population. WHAT IT DOES NOT SUPPLY: the event architecture. The retrieval calls, the conversation-close tagging, and the per-token metering in the worked inventory are stipulated for the exercise and are not described by the study. Ruled 2026-07-29: the worked example is labelled a stylized application by a provenance line under the craft-section title rather than bound to the study's parameters, on the reasoning that a precise agent count above a stipulated inventory would falsely signal that the whole inventory is reported. Chapter 1 therefore says on the order of five thousand agents and states no productivity figure at all. FIGURES, FOR CHAPTER 6 WHERE THE STUDY IS REPORTED RATHER THAN ADAPTED: use the published QJE figures, 5,172 agents and a 15 percent average increase in issues resolved per hour. The widely circulated 14 percent and 5,179 figures come from the 2023 NBER working paper and must not be used anywhere in the book. Non-perishable: cited by DOI, so no access date is required.

### `github-2025-premium`

Cited in 2 passages.

- AUTHORS: GitHub
- TITLE: Update to GitHub Copilot Consumptive Billing Experience
- CONTAINER: GitHub Changelog
- DATE: 2025-06-18
- URL: https://github.blog/changelog/2025-06-18-update-to-github-copilot-consumptive-billing-experience/
- PERISHABLE: True
- ACCESSED: 2026-07-28
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Upgrade RESOLVED differently from the worksheet. The worksheet called for a permalinked docs.github.com revision. A dated changelog entry is the better artifact for a dated claim: a docs page describes the current state, a changelog records the change on the day it happened. This also matches the chapter's own footnote wording, 'premium-request billing changelog'. CLAIM NARROWED 2026-08-06 (Stage 3, SF3). The chapter formerly said GitHub 'began billing premium requests that had previously carried no separate charge'. External check 1 raised that this changelog documents the change, not the arrangement preceding it, and a dated changelog cannot establish a prior billing state it does not describe. External check 2 restated the original claim as sound, so the two checks disagreed and the narrower reading was ruled controlling. The sentence now says GitHub 'began enforcing monthly premium-request allowances and letting customers pay for usage beyond them', which is exactly what this entry carries: allowances enforced, and a paid overage limit available to customers. The act one, act two structure survives the narrowing. Do not restore the prior-state contrast without a pre-2025-06-18 GitHub pricing or documentation artifact that describes the earlier arrangement in its own words.

### `github-2026-usage`

Cited in 2 passages.

- AUTHORS: GitHub
- TITLE: GitHub Copilot Is Moving to Usage-Based Billing
- CONTAINER: The GitHub Blog
- DATE: 2026-04-27
- URL: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Announced 2026-04-27, effective 2026-06-01. Confirms the chapter's claim: premium request units replaced by GitHub AI Credits consumed on token usage, including input, output, and cached tokens, at each model's published API rate. No repo revision exists for this one; it is a github.blog post, not a docs page. EXCEPTIONS VERIFIED 2026-07-29 against the same post, in answer to five independent fact-check raises: annual Pro and Pro+ subscribers remain on premium-request pricing until their terms expire; code completions and Next Edit Suggestions remain included and consume no credits; every plan retains a monthly credit allowance; base subscription prices are unchanged. The chapter therefore does not claim premium requests were retired entirely, and any raise to that effect has already been answered. ADVANCE NOTICE VERIFIED 2026-07-29 (Stage 2, item A4): the post is dated 2026-04-27 for a 2026-06-01 effective date, roughly five weeks ahead, and states that to help customers prepare GitHub was launching a preview bill experience in early May, giving users and admins visibility into projected costs before the transition, reachable from the Billing Overview page. Act one carries its own advance record in github-2025-premium, a dated GitHub Changelog entry. The chapter therefore does not describe either step as quiet. ALL PLANS VERIFIED 2026-07-29 (Stage 2, item B2): the post states that all GitHub Copilot plans transition to usage-based billing on June 1, 2026, which is the basis for the chapter's phrase across all of its plans. That phrase replaced an inferred claim about millions of accounts. The breadth contrast the chapter draws is sourced on both sides: Cursor's own timeline records that the June 16 change altered the Pro plan and left Teams plans unchanged, while this transition covered every Copilot plan. Separately noted for later chapters: the transition did draw substantial developer backlash in late May and early June 2026, so advance notice should not be read as smooth reception.

### `microsoft-2026-q2`

Cited in 1 passage.

- AUTHORS: Microsoft Corporation
- TITLE: FY26 Second Quarter Earnings Call
- DATE: 2026-01-28
- URL: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> DECISION 46 (2026-07-28): Microsoft's own IR transcript is accepted as the primary source. The figure is a first-party disclosure by the party that holds the data, published by that party. A filing upgrade is not available: the 4.7 million figure appears only in spoken remarks, the FY26 Q2 press release carries no Copilot subscriber count, and Microsoft does not break out product-level subscriber counts in the 10-Q. Perishable, so capture governs durability. Verified wording, Nadella: 'all up now we have over 4.7 million paid Copilot subscribers, up 75% year-over-year', stated in the coding paragraph, so GitHub Copilot. FLAG CLEARED 2026-07-29 (Stage 2, item A2): the chapter now reads 'over 4.7 million', attributes the figure to the January 28, 2026 call, and states that it precedes the 2026-06-01 billing transition by four months. The figure measures the quarter ended 2025-12-31 and is not a measurement of the paid base at transition. The prose no longer asserts otherwise. GROWTH RATE PROMOTED 2026-07-29 (Stage 2, item B1): the chapter now also carries the 75 percent year-over-year figure from the same verbatim sentence, which replaced an unsourceable claim that Copilot was the most widely adopted AI coding assistant in the world. That rank claim had no adoption metric and no comparative source; it has been cut and must not return. Both the 4.7 million and the 75 percent come from the one Nadella sentence recorded above, so they stand or fall together. DATE ANCHOR DRIFTED AND IS RESTORED 2026-08-10 (Stage 3, SF7). The A2 entry above was accurate when it was written and had stopped being so, which is why it is left standing and dated rather than edited. The chapter had been generalized to read 'In January 2026, four months before that change', so the four-month interval rested on a date the sentence did not name: read as the month at large the interval runs to five, and it is four only from the 2026-01-28 call. The anchor is restored and the sentence now reads 'On January 28, 2026, four months before that change, the company told investors on its earnings call that Copilot had passed 4.7 million paid subscribers and was growing 75 percent year over year.' One further correction to A2, recorded because its claim is exactly what outlived the prose it described: the chapter reads 'had passed 4.7 million', which carries the same quantity as Nadella's 'over 4.7 million' but is not that phrase verbatim. The figure, the growth rate, and the four-month relation are otherwise unchanged. What would reverse this: an IR listing or transcript dating the FY26 Q2 call to a day other than 2026-01-28, which would break the interval as well as the anchor.

### `techcrunch-2025-altman-pro`

Cited in 1 passage.

- AUTHORS: Wiggers, Kyle
- TITLE: OpenAI Is Losing Money on Its Pricey ChatGPT Pro Plan, CEO Sam Altman Says
- CONTAINER: TechCrunch
- DATE: 2025-01-05
- URL: https://techcrunch.com/2025/01/05/openai-is-losing-money-on-its-pricey-chatgpt-pro-plan-ceo-sam-altman-says
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Second independent path for altman-2025-pro, per the Decision 40 two-path standard. BYLINE VERIFIED 2026-07-29 by direct fetch: Kyle Wiggers, then TechCrunch AI Editor; article:published_time 2025-01-06T04:39:16Z, displayed 8:39 PM PST January 5, 2025. Reproduces both statements and links the exact status URL used in altman-2025-pro. Quotes Altman: 'I personally chose the price, and thought we would make some money.' Frames the remark as made 'on Sunday', corroborating the January 5 US dating.

### `techcrunch-2025-anthropic-limits`

Cited in 1 passage.

- AUTHORS: Zeff, Maxwell
- TITLE: Anthropic Unveils New Rate Limits to Curb Claude Code Power Users
- CONTAINER: TechCrunch
- DATE: 2025-07-28
- URL: https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Carries the fact the X post does not: Anthropic had quietly introduced Claude Code rate limits weeks earlier, linking its own report of 2025-07-17. CAUTION on that wording: Zeff writes 'quietly introduced', but the linked July 17 report, now carried here as techcrunch-2025-anthropic-tightening, establishes that tiered limits already existed and were tightened. The chapter says tightened for that reason. Do not restore 'introduced' on the strength of this note. BYLINE VERIFIED 2026-07-29 by direct fetch: Maxwell Zeff, Senior AI Reporter; published 2025-07-28T19:21:15Z, 12:21 PM PDT. Also confirms the existing five-hour limits remained in force, that two new weekly limits were added (one overall, one specific to Opus 4), effective August 28, and that Max subscribers could buy additional usage at standard API rates.

### `techcrunch-2025-anthropic-tightening`

Cited in 1 passage.

- AUTHORS: Brandom, Russell
- TITLE: Anthropic Tightens Usage Limits for Claude Code Without Telling Users
- CONTAINER: TechCrunch
- DATE: 2025-07-17
- URL: https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Added 2026-07-29 (Stage 2, item A3) to remove a second-hand dependency: the July 17 tightening previously reached the chapter only through techcrunch-2025-anthropic-limits linking back to this report, which is second-hand inside a single outlet. VERIFIED 2026-07-29 by direct fetch. Byline Russell Brandom, AI Editor, confirmed in the visible byline and in meta-author and parsely-author; published 2025-07-17T21:04:34Z, displayed 2:04 PM PDT July 17, 2025. CAUTION: the page also carries a stale sailthru.author field naming Connie Loizos, a CMS artifact; do not cite her. Establishes that tiered limits already existed before July (Max at twenty times Pro, Pro at five times free), that resets came within hours, that subscribers received no advance notice, and that many were unaware limits applied at all. Anthropic's representative confirmed the reports but spoke only of slower response times and declined to confirm a change in limits, which is why the chapter attributes the tightening to what subscribers encountered rather than to a company action the company acknowledged. Source title normalized: the published headline carries an em dash before the word Without, removed here to satisfy the voice gate.

### `techcrunch-2025-cursor-apology`

Cited in 1 passage.

- AUTHORS: Zeff, Maxwell
- TITLE: Cursor Apologizes for Unclear Pricing Changes That Upset Users
- CONTAINER: TechCrunch
- DATE: 2025-07-07
- URL: https://techcrunch.com/2025/07/07/cursor-apologizes-for-unclear-pricing-changes-that-upset-users/
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> Added 2026-07-29 (Stage 2, item A7). Carries the one fact truell-2025-pricing does not: Truell's role. The piece describes him as the CEO of Anysphere, the company behind Cursor, and quotes him as Anysphere CEO Michael Truell. VERIFIED 2026-07-29 by direct fetch. Byline Maxwell Zeff, Senior AI Reporter, confirmed in the visible byline and in meta-author, parsely-author, and sailthru.author; published 2025-07-07T22:57:09Z, 3:57 PM PDT July 7, 2025. Independently corroborates the June 16 change and the apology from outside the vendor, and places the apology on a Friday, consistent with July 4, 2025. TWO DISCREPANCIES RECORDED SO THEY ARE NOT MISTAKEN FOR CORRECTIONS. First, this piece glosses the old allotment as 500 fast responses; that phrase is TechCrunch's, not Cursor's, and the chapter follows the primary, which says 500 requests per month against external models with Sonnet models costing two. Do not reintroduce 'fast requests' from this source. Second, this piece states that only auto mode offers unlimited usage, whereas Cursor's own post lists unlimited usage of Tab and of models in Auto. The primary governs, so the chapter says Tab and Auto. Do not narrow it to Auto on the strength of this source. Also supports the chapter's depletion sentence directly: it reports that many users ran out of requests quickly under the new plan, in some cases after just a few prompts when using Anthropic's newer Claude models, which is reportage rather than inference.

### `truell-2025-pricing`

Cited in 1 passage.

- AUTHORS: Truell, Michael
- TITLE: Clarifying Our Pricing
- CONTAINER: Cursor
- DATE: 2025-07-04
- URL: https://cursor.com/blog/june-2025-pricing
- PERISHABLE: True
- ACCESSED: 2026-07-29
- UPGRADE: none, settled

REGISTER NOTE, verbatim:

> NOTE ADDED 2026-07-29 (Stage 2, items A5, A6, A7). This entry previously carried no note despite being the most load-bearing source in the chapter. Verified by direct reading on the access date. DATE: July 4, 2025, stated on the page and corroborated by the post's own timeline, which reads June 16 for the original change, June 30 for a clarity revision to that post and the pricing page, and July 4 for the apology. Three fact-check rounds have proposed July 3; all three are wrong. Do not change it. REQUEST ARITHMETIC: for external models Cursor had previously charged by request count, with a limit of 500 requests per month and Sonnet models costing two requests, which is why the chapter says five hundred requests against external models rather than 'fast requests'. The phrase 'fast requests' is TechCrunch's gloss, not Cursor's term, and must not be reintroduced. NEW PLAN TERMS: unlimited use of Tab and of models in Auto, 20 dollars of frontier model usage per month at API pricing, and the option to purchase more at cost. ORDER OF MAGNITUDE: the post states verbatim that although most users' costs stayed fairly constant, the hardest requests cost an order of magnitude more than simple ones. A raise calling this unsupported has been rejected once and should be rejected again. COVERAGE: the post gives median Pro coverage as roughly 225 Sonnet 4 requests and states that the vast majority of Pro users do not exhaust the allowance, so the chapter's depletion sentence is scoped to a labelled composite team's heaviest users on long-horizon frontier work, not to Pro users generally. REFUNDS: offered for unexpected usage between June 16 and July 4, 2025. BYLINE: the post is bylined Michael Truell with no role stated on the page; his role as chief executive of Anysphere rests on techcrunch-2025-cursor-apology, not on this post. CLAIM NARROWED 2026-08-06 (Stage 3, SF2). The chapter formerly said the allowance was consumed 'after which usage continued to bill against real rates', which asserts that billing continued automatically. This entry does not establish that. What it establishes is the price of further use: twenty dollars of frontier-model usage per month at API pricing, with the option to purchase more at cost. Whether continuation was the default or required usage-based pricing or a spend limit to have been enabled is not settled here, and no Claude session can reach the post to settle it. RULED by Dan: state the price and assert no mechanism. The sentence now reads 'after which additional usage was priced at the same rates'. Do not restore a mechanism claim without a passage from this post that describes the default billing behaviour on exhaustion. The sentence that follows, that charges arrived which no one had planned for, is scoped to the labelled composite team and is separately supported by the refund offer for unexpected usage between June 16 and July 4, 2025.

