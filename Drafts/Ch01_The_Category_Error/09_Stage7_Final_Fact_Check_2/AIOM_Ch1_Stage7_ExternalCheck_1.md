# Stage 7, final fact check 2. External check 1

Received: 2026-08-11. Commissioned by Dan on a New Yorker fact-checker prompt.
Checker had source access. Claude does not, so the source verifications below are
recorded as received and are not independently confirmed in this repo.

**ARTIFACT READ: the chapter HTML, not a render.** This is the cause of both
production flags below, and both are phantoms. See
`AIOM_Ch1_Stage7_Render_Verification.md` in this folder.

**EM DASHES NORMALIZED.** The report as received carried em dashes. They are
replaced here with commas, colons, or parentheses, on the precedent already set
in the chapter source register for `techcrunch-2025-anthropic-tightening`, whose
published headline carries an em dash removed to satisfy the voice gate. No
wording is otherwise altered, and no finding is softened.

---

## Verdict as received

The chapter's factual spine holds. Every dated vendor action, every figure, and
every attribution tested verified against the cited primary source, and the
two-path sourcing standard (first-party plus named-byline reportage) is doing real
work. No fabricated or misdated events found. Five precision flags, two of them
instances of the "ruled narrowing lost in a copy edit" failure mode the register
itself warns about, plus two production flags where the file as rendered appeared
to be missing content.

## What checked out

| Claim in chapter | Verification as received |
| :-- | :-- |
| Cursor Pro was $20/developer/month in spring 2025; on June 16, 2025 the 500-requests-per-month allowance for external models (Sonnet counting double) became a $20 frontier-model credit drawn at API rates | Cursor's own post confirms the June 16 date, the 500-request limit with Sonnet models costing two, and "$20 of frontier model usage per month at API pricing"; TechCrunch corroborates the $20 Pro price and June 16 update |
| July 4, 2025: Truell apologized, promised refunds for transition charges; "less than three weeks" after June 16 | Cursor's timeline dates the apology post July 4 and offers refunds for unexpected usage between June 16 and July 4; TechCrunch places the apology on a Friday, and July 4, 2025 was a Friday. 18 days is under three weeks |
| Michael Truell is chief executive of Anysphere, Cursor's maker | TechCrunch: "Anysphere CEO Michael Truell". The register correctly notes his role is not stated on the Cursor post itself, which is good attribution discipline |
| June 18, 2025: GitHub put monthly premium-request allowances into effect, two days after Cursor | The changelog is dated 2025-06-18 and says allowances are "now in effect, now enforced". Date arithmetic correct |
| June 1, 2026: all Copilot plans moved from premium requests to GitHub AI Credits consumed on token usage at published API rates; base prices unchanged; every plan includes an allotment; announced April 27, 2026; preview bill in early May | GitHub's announcement confirms each element, and the April 27 announcement date is independently corroborated |
| January 28, 2026 earnings call: Copilot paid subscriber count and year-over-year growth, four months before the June 1 change | Microsoft's own transcript dates the call Wednesday, January 28, 2026, and the sentence appears in the coding (GitHub Copilot) paragraph exactly as the register records. Jan 28 to June 1 is four months and four days, so "four months before" is fair |
| January 2025: Altman said OpenAI was losing money on the $200 ChatGPT Pro plan because usage exceeded expectations, and that he personally chose the price | TechCrunch, dated January 5, 2025, carries both, quoting "I personally chose the price". The register's timezone note on the X post (Jan 5 US, Jan 6 UTC) is consistent with TechCrunch's same-day Sunday report |
| July 2025: Claude Code subscribers hit tighter limits without notice; many unaware limits existed; Anthropic confirmed reports but not a change; on July 28 it announced two weekly caps (one overall, one Opus 4) atop existing five-hour limits, effective August 28; Max subscribers can buy more at standard API rates | Brandom's July 17 report supports the no-notice tightening, user unawareness, and Anthropic's non-confirmation; Zeff's July 28 report supports the two weekly caps, the five-hour limits continuing, the August 28 effective date, and Max overage at API rates |
| Brynjolfsson, Li and Raymond, "Generative AI at Work," QJE 140(2): 889 to 942, 2025, DOI 10.1093/qje/qjae044; "on the order of five thousand agents" | Exact match on authors, journal, volume, issue, pages, and DOI. The published agent count is consistent with "on the order of five thousand", and the chapter properly stipulates that the event architecture and volumes are its own exercise, not the study's |
| Craft-section arithmetic: 5,000 agents x 40 contacts x 6 replies x 21 days | 25.2M generations + 25.2M retrievals + 4.2M close operations = 54.6M events/month; divided by 5,000 seats = 10,920, fairly stated as "about 10,900". Math checks |

Note on the QJE row: the published agent count is reserved for Chapter 6 by the
2026-07-29 ruling and is deliberately not restated here. G1 caught it once already
in Chapter 1 prose.

## Flags as received

**1. "Eleven days later" measures from the press report, not the encounter
(medium).** The chapter says Claude Code customers encountered tighter limits and
that "eleven days later" Anthropic announced the weekly caps. July 17 to July 28
is eleven days, but July 17 is the date of the TechCrunch *report*; the report
itself says users were hit "since Monday morning" of that week, and Monday was
July 14. The register note "tightened on July 17, 2025" inherits the same drift.
The encounter-to-announcement interval is at least fourteen days. Suggest "two
weeks later" or "eleven days after the first reports."

**2. The GitHub act-one sentence has drifted past its own ruled narrowing
(medium).** The chapter reads: GitHub "began charging Copilot customers for
premium requests that exceeded a monthly allowance". The changelog says allowances
were "now enforced" and that paying beyond them required setting a spending limit
whose default was $0, so overage was opt-in, not automatic. The register's SF3
ruling records the narrowed sentence as "began enforcing monthly premium-request
allowances and letting customers pay for usage beyond them", which the current
prose no longer matches. This is the same regression pattern documented in
SF8/SF9. Restore the ruled wording.

**3. "Annual subscribers kept their existing terms until their subscriptions
expired" (low-medium).** GitHub's post says annual Pro/Pro+ users stay on
premium-request pricing until expiry, but also that "model multipliers will
increase on June 1, for annual plan subscribers only". One term did change for
them. Suggest "kept premium-request pricing until their subscriptions expired," or
add the multiplier exception.

**4. "For every subscriber, regardless of renewal date" (low).** Zeff supports
that the caps apply to all Pro and Max subscribers from August 28. "Regardless of
renewal date" is a reasonable inference but appears in neither cited source. Since
the clause exists to sharpen the contrast with GitHub's annual carve-out, either
source it or trim to "for all Pro and Max subscribers."

**5. "Customers on the highest-priced plan" (low).** The source says "Max
subscribers", and Max spans two price points ($100 and $200). "Max-plan
subscribers" is the supported form.

## Production flags as received, BOTH SINCE DISPROVED

- **Theorem 1's conditions are missing from the file as rendered.** The text reads
  "if:" followed immediately by "then that AI use is a resource-consuming
  operating activity," yet later prose references "the fourth condition". Confirm
  the numbered condition list survived the HTML build.
- **Problem P3's table appears misaligned.** As rendered, the resource-driver text
  sits under the "Event type" header and the trailing column is empty. If the
  intended student-blank column is "Event type," verify the empty cells are
  actually in the first column of the source HTML.

Both are artifacts of HTML text extraction, not defects. Disproved against the
render on 2026-08-11; see the verification memo in this folder.

## Checker's notes as received

The source register is unusually strong practice: perishability flags with access
dates, the two-path standard for load-bearing claims, and dated ruling notes that
quote the ruled sentence are what made the two regressions above detectable at
all. Two items could not be verified to the primary: the two X posts (Altman's and
Anthropic's), reached only through their named second paths, and the CMS-metadata
cautions in the register (for example the stale sailthru.author field), which are
not visible in extracted page text. Both are acceptable as documented, given the
register's own durability rules. Nothing in the chapter requires a correction of
substance; the flags above are precision work, not structural problems.

## Sources cited by the checker

1. https://cursor.com/blog/june-2025-pricing
2. https://techcrunch.com/2025/07/07/cursor-apologizes-for-unclear-pricing-changes-that-upset-users/
3. https://github.blog/changelog/2025-06-18-update-to-github-copilot-consumptive-billing-experience/
4. https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
5. https://www.insight.com/en_US/content-and-resources/blog/github-is-moving-to-usage-based-billing-heres-what-you-need-to-know.html
6. https://lanternstudios.com/insights/blog/github-copilot-billing-change-faq/
7. https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
8. https://techcrunch.com/2025/01/05/openai-is-losing-money-on-its-pricey-chatgpt-pro-plan-ceo-sam-altman-says
9. https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/
10. https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/
11. https://doi.org/10.1093/qje/qjae044
12. https://ideas.repec.org/a/oup/qjecon/v140y2025i2p889-942..html
13. AIOM_Ch01_redraft.html (the artifact read, and the cause of both production flags)
14. https://academic.oup.com/qje/article/140/2/889/7990658

Items 5, 6, 15 through 24 in the original list are third-party explainers,
preprints, community discussions, and social posts. Decision 48 and SF6 have
already ruled that class out as a sourcing path, so they are not carried here.
