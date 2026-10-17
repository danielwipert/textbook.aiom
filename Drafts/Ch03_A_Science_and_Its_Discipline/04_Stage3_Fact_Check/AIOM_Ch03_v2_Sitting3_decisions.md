# Chapter 3 (redesigned): Sitting 3, fact-check decisions

Two external checks, 2026-10-17, read against the live text the same day:

- **Check A** (`AIOM_Ch03_v2_Stage3_externalcheck_A.md`) had web access and returned
  55 findings: 35 verified, 9 partly supported, 3 contradicted, 8 cannot confirm.
- **Check B** (`AIOM_Ch03_v2_Stage3_externalcheck_B.md`) read only the render and
  returned 19 findings.

Every remedy below was judged separately from its finding. Where a checker's
wording would break a house rule or claim something new, Claude's wording is
given instead and the difference is said. **Dan rules every group**; any item can
be pulled ("A, but not A-46"). All rulings are applied in one commit, then the
register notes and `AIOM_Claim_Ledger.md` are written from the chapter's new
sentences.

Six gates: 1. Contradicted, 2. Narrowings, 3. Unconfirmed Lindy items,
4. Small accuracy fixes, 5. Findings recommended for no change, 6. The ledger.

---

## Group 1. The three contradictions (A-21, A-26 with A-52, A-45)

**Recommendation: accept all three.**

**A-21, JPMorgan.** "A little stale" described the CFO's own $700 million figure,
not Dimon's $2 billion. The CFO is Jeremy Barnum; the report is dated October 13,
2026.

- The box's date line "Dated: October 2025, with a later update" becomes
  "Dated: October 2025 and October 2026".
- "When later asked for updated figures, the bank's chief financial officer put
  annual AI spending closer to $700 million and called the earlier figure "a
  little stale." The same report said the benefits were not yet visible in the
  bank's quarterly earnings." becomes "In October 2026, the bank's chief
  financial officer, Jeremy Barnum, put annual AI spending closer to $700
  million, while calling that estimate "a little stale at this point." He said
  the benefits were not yet observable in the bank's quarterly earnings."

**A-26 and A-52, Lindy.** Lindy's own technical post says most managed-agent
traffic moved to DeepSeek and selected uses stayed on Anthropic's Sonnet. So
"all traffic" is wrong, and the worked audit's "no rule for which work runs
where" is wrong too: keeping some work on one model and moving the rest is
exactly the routing rule the chapter teaches. The audit is reworked to match (this
also settles B-4 and B-10). Lindy's post becomes a new source,
`lindy-2026-migration`, which check A read.

- **Box** (date line "Dated: June to July 2026"): "Lindy is a company of more
  than two dozen people that sells AI assistants for email and calendars. In
  2026, Flo Crivello, who leads the company, said its largest expense was the AI
  models it bought from Anthropic: "Like, more than payroll." In June 2026, he
  announced a move to DeepSeek V4, a model from a Chinese developer, and said it
  would save millions of dollars. Lindy's own technical account says most of its
  managed-agent traffic moved, while selected uses stayed on Anthropic's Sonnet
  model." (The three unconfirmed sentences are in Group 3.)
- **Step 1**: "The record shows four activities: running the assistants that
  customers use; choosing a model provider; knowing the total cost of the models
  well enough to compare it with payroll; and moving most traffic to one model
  while keeping selected uses on another."
- **Step 2**: "Choosing a provider answers the sourcing question. Keeping selected
  uses on Sonnet while the rest moves to DeepSeek sends different work to
  different capacity, so allocation and routing is partly performed: the sources
  describe the split, not the rule behind it. Knowing the total cost answers part
  of the metering and attribution question, but the sources do not show that cost
  assigned to customers or products."
- **Step 4**: "Metering and attribution, and allocation and routing, are partly
  performed. Planning and budgeting and holding value to account are not shown.
  The cited sources contain no forecast of consumption and no measure of whether
  each customer's use pays for itself."
- **Step 5**: "Crivello performs sourcing in public. The sources cited here name
  no one responsible for the other functions." (Also settles A-55.)
- **Closing paragraph**: "Using six steps and a few public facts, the audit
  examined a company moving most of its AI work to a new model, a move its leader
  explained by cost. The public record provided no answer to two of the five
  Founding Questions and only part of an answer to two others. Whether the
  sourcing decision was sound depends on the new model's quality and the cost of
  the move, which the record does not show. The audit also identifies what the
  switch alone could not establish: which customers account for the company's
  new costs."
- Step 6 stays as it is.

**A-45, the Australian trial.** Problem P2 calls the evaluation "independent".
It was jointly delivered by the Digital Transformation Agency and Nous Group, and
Chapter 2's fact check removed that word for exactly this reason. Claude
reintroduced it when drafting P2. "commissioning an independent evaluation"
becomes "commissioning an evaluation delivered jointly with an outside firm".

---

## Group 2. Narrowings: true, but the sentence claims more (A-3, A-16 with B-18, A-23, A-38 with B-2, A-46)

**Recommendation: accept all five.**

- **A-3, Airbnb.** Chesky was talking about putting Airbnb's app inside ChatGPT,
  not about connecting OpenAI's models to Airbnb's systems. "He also said
  OpenAI's tools for connecting its models to Airbnb's systems were not yet ready
  to meet the company's needs." becomes "He also said OpenAI's tools for making
  Airbnb's app available inside ChatGPT were not yet ready."
- **A-16 and B-18, Microsoft.** The routine-versus-complex split is a general
  explanation in the trade report, not a documented rule. "Reports put the volume
  at tens of thousands of prompts a week. Routine tasks moved to the in-house
  models, while complex reasoning tasks could still go to the outside models."
  becomes "Bloomberg put the volume at tens of thousands of prompts a week. The
  reporting did not say how the tasks that moved were chosen."
- **A-23, JPMorgan.** The reports do give annual figures. "The published accounts
  do not say which costs, benefits, or period either figure covered." becomes
  "The reports give annual figures but do not say which costs and benefits each
  figure includes."
- **A-38 and B-2, Cursor (Section 3.1).** Tab and Auto stayed unlimited, the change
  was to the individual Pro plan, and a plan only makes the conditions possible:
  they hold for a developer who uses frontier models past the credit. "After June
  2025, each request drew down a twenty-dollar monthly credit at the model
  provider's rate, and further use was priced at the same rates. Both conditions
  therefore held for a team on that plan." becomes "From June 16, 2025, the
  individual Pro plan included twenty dollars a month of frontier-model use at the
  model provider's rates, and further use was priced at the same rates. For a
  developer whose frontier-model use ran past that credit, both conditions held."
  The "priced, not billed" ruling from Chapter 1 is kept. Chapter 1's own wording
  goes on the list for the Chapters 1 to 3 review, as already noted.
- **A-46, the Australian trial.** "Weekly or less" describes most survey
  respondents, not every participant; about a third reported daily use.
  "Participants reported using the tool a few times a week or less and saving
  time when they used it." becomes "Most participants who answered the survey
  after the trial reported using the tool a few times a week or less, and
  respondents reported saving time when they used it." This sentence came from
  Chapter 2's problem P3, so Chapter 2's wording joins the Chapters 1 to 3 review
  list.

---

## Group 3. Lindy items no one could confirm (A-28, A-29, A-30, A-31, A-24, A-25)

The "100x more work" quotation, the willingness to return to Anthropic, the
expectation of spending more on AI than on payroll, and the April start date
could not be read in any source. Standing rule 2: cite, make conditional, or cut.

**A. Cut all four, and use the confirmed wording for size and role** *(recommended)*
The box keeps only what check A read (Group 1's box text). "About 25 people"
becomes "more than two dozen people", NPR's figure. "Its founder" becomes "who
leads the company", because NPR calls Lindy "his startup" and no source read
gives the title. The CNBC source is then cited by nothing and leaves the
register.

**B. Keep them as Grade C, marked unconfirmed in the register**
This is faster, but the chapter then prints statements no one has read.

**C. Send them to a second checker before ruling**
This costs another round trip for one box.

---

## Group 4. Small accuracy fixes (A-13, A-53, A-54, B-1, B-3, B-11, B-12, B-15, B-16)

**Recommendation: accept all nine.**

- **A-13, DoiT.** "at least 8 percent named both" assumes a multi-answer question
  that no source shows. Cut ", meaning at least 8 percent named both". The two
  figures still sum past 100.
- **B-11, DoiT.** "in the previous twelve months" becomes "in the twelve months
  before the survey". Also update the register to the live page's title, author
  and date (A-9).
- **B-12, Pigment.** "and the average overrun was about 27 percent" becomes "and
  the report put the average overrun at about 27 percent". Check B wanted the
  base stated as well, but no source read gives it, so the fix only attributes
  the figure to the report.
- **A-53, FinOps in 3.3.** Add the citation `finops-definition-2024` to "FinOps was
  built to make cloud spending accountable when bills arrived after capacity had
  been used." No words change.
- **A-54, invoices.** "A usage-based invoice supplies an aggregate count; a
  seat-based invoice supplies neither consumption counts nor attribution."
  becomes "An invoice priced by use can supply an aggregate count; an invoice that
  reports only seats and charges supplies neither consumption counts nor
  attribution."
- **B-1, the allocation rule.** Check B is right that P2 calls choosing seat
  holders "allocation" while the craft section's rule does not cover it. Its
  remedy, moving it to sourcing, contradicts the chapter's own definition
  ("Allocation decides who goes first when capacity is insufficient for
  everyone"). Claude's fix widens the rule instead. The rule's last sentence
  becomes "The allocation and routing function begins only when a stated rule
  sends different work to different sources of capacity, decides what runs first,
  or decides which users receive capacity and which do not." P2 step 2 becomes
  "Choosing which employees receive a license is allocation: agency nomination
  decided which users received capacity and which did not." Uber stays
  consistent, because it gave the tool to every engineer.
- **B-3, Table 3.1.** The FinOps row's last cell has no citation. "Its 2026 report
  quotes a practitioner saying that no one can yet answer whether AI is providing
  value" becomes "Its 2026 report quotes one practitioner saying that no one can
  yet answer whether AI is providing value", cited to `finops-2026-state`.
- **B-15, Klarna.** "had handled 2.3 million conversations, accounting for
  two-thirds of its customer-service chats" becomes "had handled 2.3 million
  conversations in that month, accounting for two-thirds of its customer-service
  chats". It stays the company's own figure, and the Chapter 6 reveal is
  untouched.
- **B-16, Uber (P1 step 5).** "Engineering ran the rollout, and someone set the
  budget. The public account does not identify anyone who compared spending with
  that budget before it ran out, so the audit records "not named" for that task."
  becomes "Engineering ran the rollout. The public account names no one who set
  the budget or compared spending with it before it ran out, so the audit records
  "not named" for both."

---

## Group 5. Findings recommended for no change (B-5, B-6, B-7, B-8, B-9, B-13, B-14, B-17, B-19; A-4, A-49)

**Recommendation: no change, for the reason given.**

- **B-5, B-9, the FinOps survey's scope.** The sentences already say "98 percent
  of respondents" and "nearly all respondents to the Foundation's survey", and
  check A verified both (A-34, A-37).
- **B-6, FinOps's purpose in 3.3.** This is the Foundation's current definition,
  verified (A-51).
- **B-7, B-8, the boxes next to the fifth and fourth functions.** Check B worried
  that readers would take the JPMorgan and Microsoft boxes as examples of the
  functions being performed. Groups 1 and 2 already make each box say what is
  missing (no reconciled costs; no stated rule).
- **B-13, Airbnb's requirements.** Group 2's fix removes the connection-tools
  point from the box, so no conflict remains.
- **B-14, Uber's cost ranges.** P1 never asks the reader to multiply them out.
- **B-17, "can always produce an answer".** This states what is possible, not how
  often anyone does it. It is your author-pass wording.
- **B-19.** Check B itself found nothing wrong here.
- **A-4, the Airbnb interview's name.** The Bloomberg report and its date were
  read; the chapter does not name the program.
- **A-49, Gartner's AIOps definition.** The table matches Cisco's reproduction of
  Gartner's wording, and the earlier ruling's reversal condition is not met.

---

## Group 6. The claim ledger and the register

**Recommendation: accept.**

- **Re-rule FC3-A3, FC3-A6 and FC3-B10** to your author-pass sentences. Check A
  verified each new wording and found that none restores what the old ruling
  banned (A-34, A-35, A-37). The new REQUIRED text is the chapter's sentence; the
  FORBIDDEN text stays.
- **Supersede FC3-R1, FC3-B4, FC3-B13 and FC3-B21.** Their sentences were cut in
  the redesign.
- **New rulings** for the narrowings in Groups 1 to 4 that a later edit could undo:
  "a little stale" (JPMorgan), "most of its managed-agent traffic" (Lindy),
  "delivered jointly with an outside firm" (Australian trial), and "priced at the
  same rates" (Cursor).
- **Register**: record check A's reading, URL and date on every source it read.
  Add `lindy-2026-migration`, drop `cnbc-2026-lindy`, and correct the DoiT and
  JPMorgan entries.

---

## Effect

About 30 sentences change, and the chapter stays near 6,000 words. After the
commit: claimcheck must pass with the new ledger, then voicecheck, the frequency
sweep, continuity and chapter_check re-run. Production (Stage 5, G2, G3) follows.
