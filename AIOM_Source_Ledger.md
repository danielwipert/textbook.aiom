# AIOM Source Ledger
Owner: Dan (Chorus AI Systems)
Policy: Decision 29 as amended by Decision 30. Append-only. One entry per
source, written when a chapter closes. Never edited after FC2 clears, except
to add a later chapter to the "Used in" line.

Decision 30: no archive snapshots. A source is sufficiently sourced when it
is cited to a primary, verified live on the accessed date, and cleared by
two independent fact checks. The accessed date is recorded so a later reader
can locate a snapshot independently if one exists.

Purpose: prevent cross-chapter drift on repeat sources, avoid re-verifying
a source already cleared, and assemble the bibliography mechanically.

Verification legend: FC1 (first independent check, external) ·
FC2 (second independent check against the source, external)

---

## S-001 · Altman, OpenAI Pro losses
Author: Sam Altman · Publisher: X (@sama) · Date: 2025-01-05
URL: https://x.com/sama · Accessed: 2026-07-29
Corroborating Grade A: Fortune, 2025-01-07 (Quiroz-Gutierrez)
Supports: flat-rate pricing mispriced by the provider itself; usage exceeded
the assumption the price was set against.
Used in: Ch1 (1.3, flat-rate objection). Scheduled: Ch4 opening case.
Verification: FC1 [ ] · FC2 [ ]
Note: the X timestamp renders as January 6 in some time zones. The post is
Sunday, January 5, 2025 US time. Use "January 2025" in body prose.

## S-002 · Anthropic, Claude Code weekly rate limits
Author: Anthropic (corporate) · Publisher: subscriber email and X
Date: 2025-07-28 announced, 2025-08-28 effective
Corroborating Grade A: TechCrunch, 2025-07-28 (Zeff)
URL: https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/
Accessed: 2026-07-29
Supports: the provider mechanism menu (rolling window, weekly caps, per-model
caps, metered overflow at API rates).
Used in: Ch1 (1.3). Scheduled: Ch4 teaching body, Ch11 opening case.
Verification: FC1 [ ] · FC2 [ ]
Note: SEQUENCE MATTERS. The unannounced mid-cycle tightening is July 17,
2025, a separate and earlier event. The July 28 announcement carried thirty
days notice. Do not describe the July 28 action as unannounced or mid-cycle.

## S-003 · Brynjolfsson, Li & Raymond, Generative AI at Work
Publisher: The Quarterly Journal of Economics, 140(2), 889-942
Date: 2025-05 (advance access 2025-02-04) · DOI: 10.1093/qje/qjae044
Accessed: 2026-07-29
Supports: a real, described deployment for the consumption-event inventory;
later, realized value with a stated boundary.
Used in: Ch1 (craft worked example). Scheduled: Ch6 anchor case.
Verification: FC1 [ ] · FC2 [ ]
Note: CITE THE PUBLISHED FIGURES. QJE: 5,172 agents, 15 percent average
increase in issues resolved per hour. The widely circulated 14 percent and
5,179 figures are from the 2023 NBER working paper and must not be used.

## S-004 · GitHub, premium request billing begins
Publisher: GitHub Docs (request-based billing, legacy)
Date: 2025-06-18 (billing start date for paid plans on GitHub.com)
URL: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/copilot-requests
Accessed: 2026-07-29
Supports: act one of the Copilot migration, the capping of request types that
had been effectively unlimited.
Used in: Ch1 (opening case). Scheduled: Ch10 (mid-life billing-model change).
Verification: FC1 [ ] · FC2 [ ]
Note: perishable. The page is already marked legacy and will likely be
retired now that credits are live. Capture the snapshot.

## S-005 · GitHub, move to usage-based billing
Author: Mario Rodriguez (Chief Product Officer, GitHub)
Publisher: The GitHub Blog · Date: 2026-04-27 announced, 2026-06-01 effective
URL: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
Accessed: 2026-07-29
Supports: act two, the retirement of premium request units for GitHub AI
Credits metered on input, output, and cached tokens at published per-model
API rates; base plan prices unchanged.
Used in: Ch1 (opening case). Scheduled: Ch4, Ch10.
Verification: FC1 [ ] · FC2 [ ]
Note: HIGH VALUE. Under "Why we're making this change" the provider states,
in its own voice, that a brief chat and a multi-hour autonomous session can
cost the user the same, and that the request model is no longer sustainable.
That is the book's thesis stated by the provider. Consider quoting directly.
Note also: this act was announced publicly six weeks ahead by the CPO, with a
preview-bill tool. It was not quiet.

## S-006 · Microsoft, GitHub Copilot paid subscriber count
Publisher: Microsoft Investor Relations, FY26 Q2 earnings call
Date: 2026-01-28
URL: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
Accessed: 2026-07-29 · Transcript published on the IR event page
Supports: the scale of the affected base. Nadella, in the coding remarks:
more than 4.7 million paid Copilot subscribers, up 75 percent year over year.
Used in: Ch1 (opening case).
Verification: FC1 [ ] · FC2 [ ]
Note: the figure is a January 2026 disclosure. The June 2026 migration base
was larger and is not published. Date the figure in prose; do not attach it
to the migration date.

## S-007 · Truell, Cursor pricing
Author: Michael Truell (CEO, Anysphere) · Publisher: Cursor blog
Date: 2025-07-04 (apology and explanation); 2025-06-16 (original change)
URL: https://cursor.com/blog/june-2025-pricing
Companion: https://cursor.com/blog/new-tier
Accessed: 2026-07-29 (both)
Supports: an application vendor converting flat pricing to metered pricing
under its own upstream variable cost; cost pass-through down the AI supply
chain; buyer-side planning failure when the correction lands mid-subscription.
Used in: Ch1 (opening case). Scheduled: Ch4 teaching body, Ch7.
Verification: FC1 [ ] · FC2 [ ]
Note: STATED CAUSE. Truell's reason is per-request cost dispersion, that new
models spend more tokens on longer-horizon tasks and the hardest requests
cost an order of magnitude more than simple ones, while most users' costs
stayed roughly constant. It is not a claim about heavy users in aggregate.
The post also gives median coverage under the new plan at roughly 225 Sonnet
4 requests, and states that the vast majority of Pro users do not exhaust it.

Note: the same call is an asset for later chapters. Nadella states that the
key metric Microsoft optimizes for is tokens per watt per dollar, and Hood
describes allocating scarce GPU capacity across first-party Copilot usage,
R&D, and Azure demand. A hyperscaler denominating its own optimization
problem in tokens is Ch4 and Ch5 material. Flagged, not yet claimed.
