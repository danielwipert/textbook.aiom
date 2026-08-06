<!--
RECEIVED ARTIFACT. Chapter 1, Stage 3, source and fact check 1, external check 2
of 2. Delivered by Dan 2026-08-06. Produced outside the Claude system against
AIOM_Ch01_redraft.html as rendered for Stage 3. Independent of external check 1:
different prompt, different emphasis (source validity and citation mechanics
rather than claim-by-claim auditing), and a different corroboration set.

Stored with one mechanical normalization and no other change: two em dashes and
two en dashes in the checker's own connective prose were rewritten, so the file
does not breach the standing dash rules. No quoted source text was touched, and
no finding, wording, or footnote was altered. The verbatim original is
reproducible from the three substitutions recorded in the commit message.
-->

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Runa fact check on this textbook article like you are a New Yorker fact checker, focus on the source and their validty and how they are cited and claimed

The sourcing and citation apparatus in this chapter is unusually strong by textbook standards and broadly valid; the main risks are around how social media and news pieces are characterized, how composite episodes are framed, and whether the boundary between “reported” and “stipulated” is always obvious to a cold reader.

Below I’ll walk through this like a New Yorker checker: source-by-source, then by how those sources are used and flagged for you.

***

## Overall source architecture

The chapter ends with a self-contained source register: keys like `truell-2025-pricing`, `github-2026-usage`, etc., each with author/title, venue, date, URL, and a “note” field with prior raises and rulings.

From a fact-check perspective that’s a big plus:

- Every factual claim in the prose carries a key.
- Each key has an explicit durability assessment (`perishable` vs non-perishable).
- Social media and corporate blogs are treated as *perishable*, with notes about access dates and known discrepancies.
- There is a documented “two-path” standard for fragile items (e.g., Altman tweet + TechCrunch article).[^1]

Where this really helps is that the register itself already contains a lot of the fact-check work; you’re not re-deriving it from scratch, you’re checking whether the prose actually stays within what those notes say.

***

## Key episodes and their sources

### Cursor pricing change (June to July 2025)

**Claim in prose**

- June 16, 2025: Pro plan’s 500 external-model requests (Sonnet = 2) replaced with a 20-dollar monthly pool of frontier-model usage at underlying API rates; unlimited Tab and Auto.
- July 4, 2025: Michael Truell publishes an apology, explains the arithmetic, offers refunds between June 16 and July 4.
- TechCrunch is used only for his role/title and for corroborating user depletion.[^1]

**Sources**

- `truell-2025-pricing`: Cursor blog “Clarifying Our Pricing”, dated July 4, 2025.[^1]
- `techcrunch-2025-cursor-apology`: Maxwell Zeff, TechCrunch report, July 7, 2025.[^2][^3][^4][^5]

**Validity and use**

- The register note for `truell-2025-pricing` already captures the key facts and caveats: the 500-request allotment, Sonnet costing two, the new \$20 frontier pool, unlimited Tab and Auto, the “order of magnitude” line about hard requests, refunds, and the timeline.[^1]
- The note explicitly records and rejects TechCrunch’s “fast requests” gloss and the narrower “only auto mode unlimited” gloss; the prose follows Cursor’s primary terminology. That’s good discipline: vendor blog for mechanics, TechCrunch only for role and independent corroboration.
- The composite buyer story around Cursor is labelled as a composite employer (“buying organization is a composite”) and scoped to “the team’s heaviest users” rather than Pro users generally. That’s an important protection: otherwise “consumed in a matter of prompts” could be over-generalized beyond what the sources warrant.[^1]

From a checker’s standpoint: the sourcing is appropriate; the internal notes already guard against the two obvious distortions (fast vs “requests”, Auto-only vs Tab+Auto). You’d still want to re-open the Cursor blog and confirm that the “order of magnitude” and “vast majority don’t exhaust allowance” lines are quoted accurately, but the register makes that straightforward.[^3][^4][^5]

***

### GitHub Copilot usage-based billing (June 1, 2026) and scale

**Claims in prose**

- June 18, 2025: act one, premium requests begin carrying separate charge; recorded on GitHub Changelog.[^1]
- April 27, 2026 announcement; June 1, 2026 transition to GitHub AI Credits metered in tokens at each model’s published API rate.[^1]
- Exceptions: annual Pro/Pro+ stay on premium-request billing until term expiry; completions and Next Edit Suggestions free; monthly credit allowance; base subscription prices unchanged.[^6][^7][^8][^9][^1]
- “Across every plan” is asserted as a breadth contrast with Cursor.
- January 28, 2026 Microsoft earnings call: “over 4.7 million paid Copilot subscribers, up 75 percent year-over-year.”[^1]

**Sources**

- `github-2025-premium`: GitHub Changelog entry “Update to GitHub Copilot Consumptive Billing Experience”, June 18, 2025.[^1]
- `github-2026-usage`: GitHub blog “GitHub Copilot Is Moving to Usage-Based Billing”, April 27, 2026.[^7][^8][^9][^6][^1]
- `microsoft-2026-q2`: Microsoft FY26 Q2 earnings call transcript.[^1]

**Validity and use**

- The usage-based billing description (credits, token-based metering, unaffected base seat prices, exceptions) matches multiple public summaries and GitHub/Microsoft’s own artifacts.[^8][^9][^6][^7]
- The register note for `github-2026-usage` confirms that:
    - The post is dated April 27 for a June 1 transition.
    - It explicitly states “all GitHub Copilot plans” transition to usage-based billing, which underwrites “across every plan.”[^9][^7][^1]
    - Exceptions (annual Pro/Pro+, completions and Next Edit Suggestions, monthly allowance, unchanged subscription prices) are verified against the post.
- The Microsoft call transcript is used narrowly: “over 4.7 million” and “up 75% year-over-year.” The note clarifies that this is a *quarter-end* figure (through Dec 31, 2025), not the base at the June 1 transition. The prose now reflects that sequencing (“four months before the change”), which cures a prior overreach.[^1]
- Importantly, the register explicitly forbids a previously inferred “Copilot is the most widely adopted coding assistant” rank claim as unsourceable. That’s an example of a good internal correction: the chapter is now anchored on the numbers and growth rate, not on unsourced superlatives.[^1]

A New Yorker checker would still re-open the April 27 GitHub blog and the Q2 transcript to confirm wording/figures, but there is no obvious inflation or mischaracterization here; breadth (“across all plans”), exceptions, and timing are all grounded in first-party text plus consistent third-party descriptions.[^7][^8][^9]

***

### Anthropic / Claude Code usage limits (July to August 2025)

**Claims in prose**

- Mid-July: subscribers encounter tightened usage limits, no advance announcement, many unaware limits applied at all; Anthropic acknowledges reports but does not confirm a change in limits.[^1]
- July 28: Anthropic announces two new weekly caps stacked on top of existing five-hour limits; effective August 28; highest tier Max can buy extra usage at standard API rates.[^10][^11][^12][^1]

**Sources**

- `anthropic-2025-limits`: Anthropic post on X announcing new weekly rate limits, July 28, 2025.[^1]
- `techcrunch-2025-anthropic-limits`: Maxwell Zeff, TechCrunch on new weekly limits and stacking behavior, July 28, 2025.[^12][^10][^1]
- `techcrunch-2025-anthropic-tightening`: Russell Brandom, TechCrunch on users experiencing stricter limits without notice, July 17, 2025.[^11][^13][^1]

**Validity and use**

- The July 17 “tightening without telling users” narrative is precisely the sort of thing TechCrunch is good for: reporting user experiences and an off-the-record acknowledgment of performance issues; the register explicitly cautions that Anthropic never confirms a *change in limits*, only slower response times, and the prose carefully attributes tightening to what subscribers encountered, not to a company statement.[^13][^11][^1]
- The July 28 TechCrunch piece and Anthropic’s own X post confirm the structured weekly limits, the August 28 effective date, stacking on top of existing five-hour limits, and the Max-plan ability to buy extra usage at standard API rates.[^10][^12][^1]
- The register explicitly warns against reading “quietly introduced” in the July 28 TechCrunch text as implying limits didn’t exist before; Brandom’s July 17 article establishes earlier tiered limits. The prose corresponds: “limits already governing their plans abruptly tightened” rather than “introduced.”[^1]

From a fact-check vantage: this is careful use of tech reporting and social media. You’re not over-claiming (no assertion that Anthropic admitted changing limits), and you correctly separate “subscriber reports” from “company statements.”

***

### Altman / ChatGPT Pro economics (January 2025)

**Claim in prose**

- CEO of largest provider publicly says the company is losing money on its \$200 Pro subscriptions because subscribers use them more than the price assumed; adds that he set the price himself.[^1]

**Sources**

- `altman-2025-pro`: Altman’s X post, January 5/6 2025.[^1]
- `techcrunch-2025-altman-pro`: TechCrunch article quoting the tweet, dated January 5 in US framing.[^1]

**Validity and use**

- The register notes already capture the time-zone ambiguity (tweet is dated January 6 UTC, January 5 Pacific; TechCrunch describes it as “on Sunday” and dates the piece accordingly). You’ve locked the book to the US time convention, which is fine as long as that choice is explicit, and the note flags it for you.[^1]
- The TechCrunch article reproduces both statements (losing money, personally chose the price) and links the exact status URL in the source.[^1]

Risk here is minimal: the claim is quoted directly and backed by two paths, one of them first-party; the main checker action is to make sure you don’t drift into broader generalization (e.g., “OpenAI is losing money on all subscriptions” vs the specific Pro tier).

***

### Brynjolfsson et al. “Generative AI at Work” adaptation

**Use in the chapter**

- The craft-section contact-center example cites `brynjolfsson-2025-genai` for the existence of a customer-support contact center with generative AI and the scale (“on the order of five thousand agents”), but explicitly labels the event architecture and volumes as stipulated for the exercise.[^1]

**Source**

- `brynjolfsson-2025-genai`: QJE paper with 5,172 agents and 15% average productivity uplift.[^1]

**Validity and use**

- The register shows you’ve already wrestled with prior misuses: earlier drafts evidently pulled “5,179” and “14%” from the NBER working paper and over-specified the example; the note now mandates using only the QJE figures in Chapter 6 and never importing the working-paper numbers.[^1]
- In this chapter, you’ve responded by:
    - Using scale language (“on the order of five thousand agents”) rather than an exact count.
    - Labeling all event-architecture details and token volumes as stipulated, not reported.[^1]

This is exactly how you should use a real study in a stylized worked example: anchor setting and scale in the study, but make the boundary between “their data” and “your hypothetical” very explicit. From a checker’s standpoint, the main job is making sure that boundary remains obvious in any retelling (e.g., in teaching notes or slides) and that no one later edits in the QJE numbers in this chapter in a way that suggests the event inventory is empirically measured.

***

## Social vs institutional sources and burden of proof

### Social media (X posts) and corporate blogs

- Altman’s and Anthropic’s X posts, and Cursor’s and GitHub’s own blogs, are all marked `perishable: true`. That’s appropriate: these are first-party statements about policy and economics, but they are web pages that can change or disappear.[^1]
- The notes emphasize capture and access dates rather than archive snapshots (per “Decision 48 repealed archive capture”; as a checker you might consider whether adding archive URLs would improve reproducibility, but that’s a tooling decision, not a validity one).[^1]
- For high-stakes claims (Altman losing money on Pro, Cursor absorbing an order-of-magnitude difference on hard requests), you’ve layered in second-path reporting from TechCrunch that reproduces the key statements and provides independent context.[^5][^2][^1]

That’s structurally solid: social/media first-party for the quote, tech journalism as corroboration.

### Tech journalism (TechCrunch primarily)

- TechCrunch is used to:
    - Provide role/title for Truell and context for user backlash around Cursor pricing.[^2][^1]
    - Describe user experience and lack of communication around Anthropic’s tightening.[^11][^13][^1]
    - Spell out the detailed weekly caps and stacking behavior for Claude Code limits.[^12][^10][^1]
    - Provide second-path confirmation/scheduling for Altman’s tweet.[^1]
- The notes show a healthy skepticism: you explicitly ignore TechCrunch’s “fast requests” terminology and “quietly introduced” framing where they conflict with primary evidence, and you record byline metadata quirks (e.g., stale `sailthru.author` fields) so they aren’t misread as multiple authors.[^1]

That’s what you want from a New Yorker-style checker: respect tech journalism as reportage, but treat vendor communications and verbatim quotes as primary, and be explicit when you accept or decline a journalist’s interpretive language.

### Institutional / academic sources

- Microsoft IR transcript is treated as primary for Copilot subscriber counts and growth. The note explains why a filing upgrade is not available (figure appears only in spoken remarks). That’s a reasonable compromise.[^1]
- The Brynjolfsson QJE article is treated as non-perishable, cited by DOI, with notes carefully distinguishing journal figures from working-paper ones.[^1]

Again, this is textbook-appropriate: IR transcripts and peer-reviewed articles are heavy anchors; tech blogs and social posts are light but acceptable when used carefully.

***

## Citation mechanics in the prose

A New Yorker checker will look not just at whether claims have sources, but whether the citations make the scope of each source clear.

This chapter generally does that well:

- Cursor section: “The Cursor post describes the change of June 16 and the clarification of June 30. The TechCrunch report carries Truell’s role and title.” That line explicitly allocates facts between sources.[^1]
- Copilot section: “The Microsoft earnings call carries the subscriber figure and the growth rate.” Again, explicit attribution.[^1]
- Anthropic section: “The announcement set two weekly caps effective August 28, 2025, added to five-hour limits already in force and tightened on July 17, 2025.” The register notes map those pieces to Anthropic’s X post and the two TechCrunch articles.[^10][^11][^12][^1]

There are a few places where, as a checker, I’d keep an eye on scope creep:

- The phrase “the largest provider” in the Altman episode: it’s plausible that OpenAI is the largest by some measure, but that specific characterization is not directly supported by `techcrunch-2025-altman-pro`. You’d want to confirm whether you have a separate adoption/market-share source for that description or soften it (“one of the largest providers”).[^1]
- The initial framing “two widely used AI coding subscriptions” for Cursor and Copilot. Copilot “widely used” is grounded in the subscriber base; Cursor’s degree of “widely used” is more anecdotal, and you’re relying on aggregated backlash reporting and the existence of Pro/Teams tiers. The term is probably fine for a textbook, but a New Yorker checker might ask for either a usage/adoption metric or slightly more guarded language here.[^4][^14][^3][^5]

***

## Reported vs stipulated and composite claims

The chapter is very self-conscious about separating empirical claims from structural ones:

- Worked examples (contact center, coding assistant, document review) have explicit stipulation language: “volumes used below are stipulated for this exercise and are not reported by the study,” “event architecture and volume assumptions stipulated for this exercise and labelled where used.”[^1]
- The Cursor buyer is a composite organization; the prose repeats that twice (opening “the buying organization is a composite,” later “labelled composite team’s heaviest users” in the register).[^1]
- The central theorem (THM-009) is clearly labelled as a theorem proved within the book’s system rather than an empirical generalization from the cited episodes.[^1]

This is doing the work a checker would otherwise have to insist on: your structural claims (“AI use is resource consumption…”) are not sold as empirically universal law; they’re contingent on the antecedents and anchored by clearly specific episodes.

***

## Where I’d push or tighten

If I were marking this up for publication with New Yorker-level standards, most of my notes would be at the margin, not the core claims:

1. **“Largest provider” language.**
Confirm you have a concrete adoption or revenue basis for calling OpenAI “the largest provider”; if not, soften the phrasing or add a source for that descriptor.[^1]
2. **Cursor “charges arrived that no one had planned for.”**
The TechCrunch article supports “many users ran out of requests quickly” and user upset; Cursor’s blog supports that hard requests cost an order-of-magnitude more and that Pro users generally don’t exhaust the allowance.[^5][^2][^1]
Your composite story extrapolates that into “charges arrived that no one had planned for” for a mid-size team. That’s plausible, but it’s still hypothetical. Because you already label the buyer as a composite, you’re probably safe; just don’t let later drafts inadvertently turn that into a claim about a named real company.
3. **“Widely used” descriptors.**
For Copilot, “widely used” is fine given 4.7M paid subscribers; for Cursor, you might either provide some adoption evidence (press coverage, plan breakdowns, enterprise tiers) or shift to “popular among developers” or “used by many teams” to avoid implying a specific market position you don’t document.[^14][^3][^4][^5]
4. **Archival robustness.**
You’ve explicitly chosen not to rely on archive captures; that’s acceptable, but your durability strategy then rests entirely on access dates. For the most load-bearing perishable sources (Cursor blog, GitHub blog, Anthropic posts, key TechCrunch pieces), consider adding a second durable path where available (e.g., GitHub Community discussions and third-party “billing change” explainers that restate the original announcements).[^6][^8][^9][^7]

None of these are “this claim is wrong”; they’re “this claim is right but the way it’s *framed* could be misread as stronger than the sources actually support.”

***

## Bottom line

On the New Yorker-checker axis, meaning clear mapping from claim to source, two-path corroboration where needed, explicit handling of fragile web artifacts, and an honest boundary between reported and stipulated, the chapter is in good shape.

Your main ongoing tasks as an author/editor are:

- Keep the prose aligned with the scope each source actually supports (especially for adjectives like “largest” or “widely used”).
- Preserve and maintain the source register notes; they’re doing a lot of the verification work and are crucial for future checking.
- Continue to flag composite and stylized examples so readers never accidentally treat them as direct empirical findings.

If you’d like, I can go line-by-line through the opening case and mark each sentence with the specific source(s) that support it and where, if anywhere, you’re leaning on inference rather than citation.
<span style="display:none">[^15][^16]</span>

<div align="center">⁂</div>

[^1]: AIOM_Ch01_redraft-1.html

[^2]: https://www.reddit.com/r/programming/comments/1lu8eyb/cursor_pay_more_get_less_and_dont_ask_how_it_works/

[^3]: https://www.vantage.sh/blog/cursor-pricing-explained

[^4]: https://www.eesel.ai/blog/cursor-pricing

[^5]: https://www.finout.io/blog/what-happened-to-cursor-pricing-2026-guide-5-cost-cutting-tips

[^6]: https://github.com/orgs/community/discussions/192948

[^7]: https://www.directionsonmicrosoft.com/github-copilot-to-move-to-usage-based-pricing-in-june/

[^8]: https://lanternstudios.com/insights/blog/github-copilot-billing-change-faq/

[^9]: https://www.gapvelocity.ai/blog/github-copilots-new-usage-based-billing-what-changed-why-developers-are-upset-and-what-it-means

[^10]: https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/

[^11]: https://www.techzine.eu/news/applications/133177/anthropic-unexpectedly-restricts-use-of-claude-code/

[^12]: https://explainx.ai/blog/claude-usage-limits-2026-timeline-explained

[^13]: https://www.reddit.com/r/ClaudeAI/comments/1m2tu85/techcrunch_anthropic_tightens_usage_limits_for/

[^14]: https://flexprice.io/blog/cursor-pricing-guide

[^15]: https://github.com/orgs/community/discussions/197089

[^16]: https://www.linkedin.com/posts/techcrunch_anthropic-tightens-usage-limits-for-claude-activity-7351719624343814146-KyiI

