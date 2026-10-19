# Chapter 3 research, 2026-10-19 (Decision 87)

Found and read by a research pass in Claude's session (WebSearch and WebFetch).
"Verified" means the source was opened and the words seen. WebFetch passes a
page through an extractor; some long sentences came back in fragments and were
joined, so the external checker re-reads these before any goes into type.

## Key corrections

- K8 is FALSE as attributed: the 73% "AI costs exceeded original projections"
  figure is NOT in the FinOps Foundation's State of FinOps 2026 (full page
  searched). It appears only in secondary blogs. Never attribute it to the
  Foundation. (The chapters do not use it.)
- AT&T figures conflict by source and scope: savings "as much as 80%" (AMD
  newsroom), "as much as 90%" (AT&T blog, read by the Chapter 1 pass on an
  att.com copy), "up to 80%" (NYT), 56% for coding (The Information, unread);
  open-model share 20% in May, 40% now, maybe 60% (NYT), 40% to 70% (FT,
  unread), 25% to 70 to 80% (WSJ, unread). Never merge them.

## Verified (read)

V1. [supports] Sourcing, and allocation and routing.
Source: AMD Newsroom, "AAI 2026: Open Telco AI Optimizes Models, Infrastructure and Token Costs", July 23, 2026: https://newsroom.amd.com/news/aai-2026-att-open-telco-update/
Exact words: "AT&T processes an average of 45 billion tokens daily" "uses an intelligent gateway to match each task with an appropriate model." "Its cache-aware AI gateway processes an average of 45 billion tokens daily and has reduced AI costs by as much as 80%"

V2. [supports] Sourcing: changing providers on cost.
Source: New York Times (Eli Tan), "Corporate America is getting hooked on open-source AI", September 4, 2026, https://www.nytimes.com/2026/09/04/technology/open-source-ai-anthropic-openai.html ; read in the licensed reprint, The Star, September 7, 2026: https://www.thestar.com.my/tech/tech-news/2026/09/07/corporate-america-is-getting-hooked-on-open-source-ai
Exact words: "As AI costs skyrocketed, Andy Markus, the company's chief data and AI officer, looked for cheaper alternatives." "By May, open models accounted for 20% of AT&T's AI use." "That has since risen to 40% and may jump to 60% in the coming months, Markus said in an interview." "Closed models remain the best for heavy-duty tasks like coding and image and video generation" Airbnb and Deloitte named as also turning to open models.

V3. [supports Table 3.1 border, metering and attribution, value]
Source: FinOps Foundation, State of FinOps 2026: https://data.finops.org/ (read October 19, 2026)
Exact words: "98% of respondents now manage AI spend (up from 63% in 2025 and 31% in 2024)." AI challenges listed: "Visibility into AI costs", "Allocating AI costs to business units", "Determining AI value/ROI: investments are often exploratory, making returns hard to define early". "FinOps for AI emerges as the top forward-looking priority, outpacing traditional focus areas."

V4. [supports, qualified] Sourcing; spend driven by use, not price.
Source: Vercel, "Open weight takes 71.5% of tokens and 23% of spend" (AI Gateway Production Index), October 15, 2026: https://vercel.com/blog/ai-gateway-production-index-october-2026
Exact words: "Open-weight models now process more than seven in ten gateway tokens and account for nearly one in four dollars." "September's gateway spend was about 13 times December's, an increase of 1,180%, while the average price per token fell 47%." Caveat in the report: "Spending is estimated at published list prices; actual bills may differ."

V5. [cuts against, partly] "Spending is shifting from closed to open-weight models" (K7).
Source: Ramp, "Cracks in the AI Thesis" (AI Index), August 12, 2026: https://ramp.com/data/ai-index-august-2026
Exact words: "6.1% of businesses using AI are now using these platforms, up 0.2 points from last month." "Despite these competitive pressures that are driving down the cost of AI, American companies continue to ramp AI spend." "In July, the top 1% of businesses spent a median $7,400 per employee on AI."
Note: the open-weight shift is concentrated among heavy spenders, and shows more in tokens than in dollars.

V6. [supports] Sourcing from several providers, matching models to tasks.
Source: Microsoft 365 Blog (Charles Lamanna), "Expanding model choice in Microsoft 365 Copilot", September 24, 2025: https://www.microsoft.com/en-us/microsoft-365/blog/2025/09/24/expanding-model-choice-in-microsoft-365-copilot/
Exact words: "you can even mix which models are used for specialized tasks from Anthropic, OpenAI, or any of the models in the Azure Model Catalog."

V7. [supports, with a teaching caveat] Holding value to account: a target set in advance and reported against.
Source: IBM, 3Q25 earnings prepared remarks, 8-K Exhibit 99.1, October 2025: https://www.sec.gov/Archives/edgar/data/51143/000005114325000063/ibm_ex991.htm
Exact words (Arvind Krishna, joined from two fragments): "In 2023, we set out on a goal to achieve $2.0 billion of productivity savings and today we are well ahead of that, with an expectation of $4.5 billion of annual run rate savings exiting this year."
Caveat: the boundary is unstated (AI plus automation, gross savings).

## Pull list (major outlet, not readable here)

P1. Financial Times, US companies turning to open-weight models, about September 27, 2026: https://www.ft.com/content/d9de4776-1fc9-4f2b-aaaf-9961c35d8acd . Reportedly: AT&T 40% toward 70%; Markus, cost "extremely important" at 45 billion tokens a day; Tinder's CTO Vinay Kuruvila, spend from about $1m a year in January to about $10m by July, routing some staff queries to open models; PNC, CH Robinson, Siemens named.
P2. Wall Street Journal, AT&T open models, about August 20, 2026, URL not found. Reportedly: 25% open, savings 80% to 90% on targeted applications, target 70% to 80%.
P3. The Information, "AT&T is Using Open Source Models to Curb Anthropic Bills", about August 21, 2026: https://www.theinformation.com/newsletters/applied-ai/t-using-open-source-models-curb-anthropic-bills . Reportedly: AT&T plans to hold employee spending on Anthropic and OpenAI flat by shifting to open models.
P4. The Information (Laura Bratton), "Why Anthropic Costs Are Unpredictable", about May 2026: https://www.theinformation.com/newsletters/applied-ai/anthropic-costs-unpredictable . ServiceNow; the "AI Control Tower" internal use is unconfirmed.
P5. The Information, Meta curbs employee AI usage as costs reach billions, about June 12, 2026: https://www.theinformation.com/articles/tokenminimizing-meta-moves-to-curb-employee-ai-usage-as-ai-costs-reach-billions . Correction to K5: budgets come in 2027, per-employee caps not yet in force.
P6. The Information, "Meta's AI Incubator Is Developing an OpenRouter Rival to Cut Coding Costs", July 2026: https://www.theinformation.com/articles/metas-ai-incubator-developing-openrouter-rival-cut-coding-costs . Reportedly: a router scoring request difficulty; Meta paying top-model prices for every coding request.
P7. Financial Times, Amazon retires the "Kirorank" AI usage leaderboard, about late May 2026, URL not found. Reportedly: "never intended to promote the use of AI for usage's sake".
P8. Wall Street Journal, Johnson and Johnson narrows its generative AI strategy, about April 2025, URL not found. Reportedly: about 900 use cases, 10% to 15% delivered about 80% of the value.
P9. Bloomberg, Match Group slows hiring to pay for AI tools, about May 2026, URL not found. Its Q1 2026 earnings call would verify.

## Searched but not usable

AT&T blog on about.att.com (403 here; Dan can open https://about.att.com/blogs/2026/the-tokenomics-equation.html ); AT&T Q2 2026 call (nothing on AI cost); trade press on AT&T (TM Forum gives 40 billion tokens a day, conflicting); Atlassian AI wallets (Guardian, trade press); Mavvrik survey (vendor); self-hosting hidden costs (vendor posts only); Decagon CEO framing (TechCrunch); Shopify Q1 2026 call (not read).
