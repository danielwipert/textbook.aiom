<!--
RECEIVED ARTIFACT. Chapter 1, Stage 3, source and fact check 1, external check 1
of 2. Delivered by Dan 2026-08-06. Produced outside the Claude system against
AIOM_Ch01_redraft.html as rendered for Stage 3.

Stored with one mechanical normalization and no other change: five em dashes in
the checker's own connective prose were rewritten to commas and parentheses, so
the file does not breach the standing no-em-dash rule. No quoted source text was
touched, and no finding, wording, or footnote was altered. The verbatim original
is reproducible from the three substitutions recorded in the commit message.
-->

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I want you to fact-check this textbook article, specifically the sources and what they are claiming. Pretend you are fact checker at New Yorker

I audited the chapter as a fact-checker would: separating **documented facts**, claims that are directionally supported but overstated, and claims that are really the author’s analytic framework rather than externally verifiable reporting. The source spine is generally strong, but several sentences need tightening before publication.[^1]

## Overall verdict

The dated vendor episodes are mostly accurate and well sourced through primary vendor posts, Microsoft’s earnings transcript, reputable reporting, and a peer-reviewed study. The chief vulnerabilities are not fabricated citations; they are **overbroad inferences**, a few imprecise formulations, and a fragile source-preservation policy.[^2][^3][^4][^5][^6]


| Finding | Assessment | Editorial action |
| :-- | :-- | :-- |
| Cursor’s June 2025 pricing revision and July 4 apology/refunds | Confirmed, with one material wording issue | Revise automatic-billing language |
| GitHub’s 2025 premium-request enforcement | Mostly supported | Do not say the June 18 post itself proves requests had previously carried “no separate charge” |
| GitHub’s June 2026 credit transition | Confirmed | Keep; unusually well documented |
| Microsoft’s 4.7m paid Copilot subscribers, up 75% YoY | Confirmed | Keep the careful time qualification |
| Altman/ChatGPT Pro episode | Core claim confirmed | Delete “largest provider” unless defined and independently sourced |
| Anthropic/Claude Code limits | Carefully and mostly accurately presented | Keep attribution to user reports where Anthropic did not confirm a change |
| Contact-center study | Strong and accurately limited in the revised prose | Keep the stipulation labels prominent |
| Chapter’s general “theorem” and categorical economics | Not source-verified empirical fact | Label as the author’s model/argument, qualify absolutes |

## Confirmed reporting

- **Cursor:** Its own July 4 post says Pro moved from a 500-request monthly limit for external models, with Sonnet counting as two requests, to \$20 of frontier-model use at API pricing; it also says Tab and Auto use are unlimited and offers refunds for unexpected charges between June 16 and July 4. It explicitly attributes the shift to long-horizon requests that can consume far more tokens.  TechCrunch independently reported user complaints that some users exhausted the new allowance after only a few prompts, and identifies Michael Truell as Anysphere’s CEO.[^7][^2]
- **GitHub Copilot:** The June 18, 2025 changelog confirms that monthly premium-request allowances were being enforced and that customers could set a paid overage limit.  GitHub’s April 2026 announcement clearly supports the later transition: all plans moved to AI Credits on June 1, token use, including input, output, and cached tokens, was to be charged at published model API rates, and annual Pro/Pro+ subscribers had a temporary exception. It also confirms unchanged base prices, included completions/Next Edit Suggestions, monthly credits, and the early-May preview bill.[^3][^4]
- **Scale claim:** Microsoft’s January 28, 2026 earnings transcript says GitHub Copilot had “over 4.7 million paid Copilot subscribers, up 75% year-over-year.” The chapter correctly dates the figure to four months before the June billing transition rather than claiming it was the subscriber total on the transition date.[^5]
- **Claude Code:** Contemporary TechCrunch reporting supports the July 17 reports of unexpectedly restrictive limits and absent advance notice, while also recording that Anthropic did not confirm a limit change. The July 28 report confirms two weekly limits were added to the existing five-hour limits, effective August 28, and that Max subscribers could purchase additional usage at standard API rates.[^8][^9]
- **Contact-center study:** The published QJE article studied 5,172 customer-support agents using a GPT-3-based conversational assistant. It reports a 15% average improvement in issues resolved per hour and describes real-time suggested responses plus links to internal documentation. The chapter properly says its retrieval architecture, event counts, and pricing mechanics are *stipulated* rather than findings of that study.[^6]


## Corrections needed

### 1. Cursor: automatic billing is too strong

**Current:** “after which usage continued to bill against real rates.”

The primary source says customers could enable a spend limit to pay for additional use at cost; the contemporaneous report says unexpected charges occurred when users exceeded the allowance without setting a spend limit. That is not identical to inevitable, automatic continuation for every user.[^2][^7]

**Safer replacement:**
> “after which users could purchase or authorize additional frontier-model usage at cost.”

### 2. GitHub: “previously carried no separate charge” needs evidence

**Current:** “it began billing premium requests that had previously carried no separate charge.”

The June 18 changelog establishes that allowances became enforced and paid overage became available. It does **not**, by itself, establish the full prior billing arrangement in the wording used.[^3]

**Safer replacement:**
> “it began enforcing monthly premium-request allowances and enabled paid overage for usage beyond them.”

If the author wants the stronger historical contrast, cite a pre-June 18 GitHub pricing or documentation page that explicitly describes the previous arrangement.

### 3. Altman: “largest provider” is unsupported

**Current:** “The chief executive of the largest provider…”

The cited reporting confirms that Altman said OpenAI was losing money on the \$200/month ChatGPT Pro plan because users consumed more than expected, and that he set the price himself. It does not establish “largest,” and the relevant metric (revenue, users, inference volume, or market share) is unspecified.[^10]

**Replacement:**
> “OpenAI’s chief executive stated publicly…”

### 4. Several absolutes need qualification

These are the passages most likely to draw a rigorous fact-check challenge:

- “The marginal cost of an additional use… is the central fact.”
- “The event is… the only candidate the provider’s meter actually records.”
- “In the ordinary case it is held by the provider, and the buyer never sees it at all.”
- “No assembled discipline governs it.”
- “The correction arrives on the provider’s schedule.”

They may express the book’s thesis, but they are not established by the cited episodes. Enterprise buyers can often receive usage dashboards, APIs, exports, logs, budget controls, or self-hosted telemetry; vendors can also maintain flat plans, change contracts at renewal, or impose caps rather than reprice. GitHub’s own 2026 announcement, for example, emphasizes preview billing, budget controls, and pooled usage, not merely a hidden meter imposed on passive buyers.[^4]

**Editorial fix:** replace universals with “often,” “typically,” “in many managed-service arrangements,” or explicitly introduce these as the author’s proposed analytic model.

## Source-method concerns

The chapter’s source register is meticulous, but its preservation policy is not publication-grade. It says that archive capture was repealed and that durability “rests on the access date”; an access date merely says someone viewed a page, not what the page contained or whether it later changed.[^1]

For every load-bearing web source, retain:

- A local PDF or HTML capture with retrieval timestamp.
- An archived permalink where permitted.
- Exact quotations and page/transcript locations in a verification ledger.
- A backup source for vendor posts and social posts.

This matters particularly for the two X posts. The underlying claims are independently corroborated by TechCrunch, but social posts should not be the sole durable source for a textbook proposition.[^8][^10]

## Non-source editorial notes

- The chapter’s opening “mid-size company” is labeled a composite, which is good. Keep that label visually conspicuous; its details should never read as reported events.[^1]
- The “theorem” nomenclature risks sounding like an externally established empirical theorem. If it is a formal result within the book’s own defined system, say so at first reference and avoid allowing the Cursor/Copilot cases to appear to prove it.
- The document-review exercise table appears structurally broken: its first column is labeled “Event type,” but the rows begin with resource-driver text. That is an editorial/layout error, not a sourcing issue.[^1]

**Bottom line:** publishable after a targeted line edit. The factual case studies survive scrutiny; the prose should make a cleaner distinction between what the sources show and what the author infers from them.

<div align="center">⁂</div>

[^1]: AIOM_Ch01_redraft-1.html

[^2]: https://cursor.com/blog/june-2025-pricing

[^3]: https://github.blog/changelog/2025-06-18-update-to-github-copilot-consumptive-billing-experience/

[^4]: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/

[^5]: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2

[^6]: https://doi.org/10.1093/qje/qjae044

[^7]: https://techcrunch.com/2025/07/07/cursor-apologizes-for-unclear-pricing-changes-that-upset-users/

[^8]: https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/

[^9]: https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/

[^10]: https://techcrunch.com/2025/01/05/openai-is-losing-money-on-its-pricey-chatgpt-pro-plan-ceo-sam-altman-says

