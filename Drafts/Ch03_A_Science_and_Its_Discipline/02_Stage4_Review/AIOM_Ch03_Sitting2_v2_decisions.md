# Chapter 3 (redesigned): Sitting 2 decisions

The second-model review (`AIOM_Ch03_Review_v2_secondmodel.md`, 21 findings) was
read against the chapter on 2026-10-17. All 21 quotes match the text exactly.
Claude's recommendation is given for each one; **Dan rules every finding**.

The findings fall into six groups, one gate each. Any item can be pulled from a
group ("A, but not S-11"). Every ruling is applied in one commit, then the
mechanical checks and the frequency sweep re-run.

Three of the proposed edits touch text kept from the first lock and already
fact-checked (S-2 opening case, S-9 Section 3.4, S-8 Klarna case). The whole
chapter goes through the fact check again anyway, so nothing is lost. One new
sentence (S-3) restates a Chapter 1 fact about Cursor and carries Chapter 1's
citation.

---

## Group 1. The audit method (S-1, S-4, S-14), all high or medium

**The problem.** The audit writes "no one" when a public record is merely
silent, so it diagnoses missing work from missing reporting (S-1). It treats
"all traffic to one model" as routing for Lindy, but treats "one tool for all
engineers" as sourcing for Uber, so a reader cannot find a stable rule (S-4).
P1 says that comparing spending with the budget needs team-level records, but
total spending can be compared with a total budget at once (S-14).

**Recommendation: accept all three, with one set of rules applied everywhere.**

1. **Three marks, not two.** Each function is marked *performed*, *partly
   performed*, or *not shown*. "Not named" replaces "no one" wherever the
   evidence is a public record.
2. **Sourcing versus routing.** Choosing what capacity to buy is sourcing, even
   when one model serves all the work. Allocation and routing begins only when a
   stated rule sends different work to different capacity, or decides what runs
   first.
3. **The first gap.** Close first the gap where the largest cost goes
   unwatched, starting with the records already held.

Proposed text:

- **Craft opening**: "...which of the five functions an organization performs
  for one deployment, and which no one performs." becomes "...and which the
  evidence does not show anyone performing."
- **Step 4**: "Mark each function as performed, partly performed, or not shown.
  A public record shows only what a company chose to report, so a function
  missing from it is not shown, not proven absent. Only an organization's own
  records can show that no one performs a function."
- **Step 5**: "For each function performed or partly performed, name who
  performs it. Write "not named" where the evidence names no one."
- **Step 6**: "State the first gap to close and the record that closing it
  requires. Close first the gap where the largest cost goes unwatched, starting
  with the records the organization already holds."
- **New paragraph after "Steps 2 and 4 do most of the work..."**: "Two rules
  keep the assignment consistent. Choosing what capacity to buy is sourcing,
  even when one model serves all the work. Allocation and routing begins only
  when a stated rule sends different work to different capacity or decides what
  runs first."
- **Lindy, step 2**: "Sending all traffic to one model is a routing rule, so
  allocation and routing is performed by a single decision." becomes "Sending
  all traffic to one model is part of that sourcing choice: no rule sends
  different work to different capacity."
- **Lindy, step 4**: "Metering and attribution is partly performed. Planning
  and budgeting, allocation and routing, and holding value to account are not
  shown. Nothing reported shows a forecast of consumption, a rule for which work
  runs where, or a measure of whether each customer's use pays for itself."
- **Lindy, step 5**: the sentence "A public record cannot show work a company
  does without announcing it, so "no one" here means "not shown."" is cut; step
  4 now carries it.
- **Lindy, closing**: "while the public record showed no one answering three of
  the five Founding Questions" becomes "while the public record showed no answer
  to three of the five Founding Questions and only part of an answer to a
  fourth."
- **P1 (Uber), step 4**: "Allocation and routing is not shown: nothing reported
  shows a rule for which work went to the tool or a limit on its heaviest users.
  Metering and attribution is partly performed: spending was totaled, but
  nothing reported assigns it to teams."
- **P1, step 5**: "writes "no one" against that comparison" becomes "writes
  "not named" against that comparison."
- **P1, step 6**: "The first gap is a monthly comparison of total consumption
  with the plan. The spending totals already reported make that comparison
  possible without a new record. Recording consumption by team comes next, to
  show where a deviation came from."
- **P2, step 4**: "Mark each function as performed, partly performed, or not
  shown." (The per-seat sentence stays.) **Step 5**: "Write "not named" where
  the facts name no owner."
- **Summary and the key term "Function audit"**: "marks the functions no one
  performs" becomes "marks each function performed, partly performed, or not
  shown."

---

## Group 2. The border with FinOps (S-2, S-13), both high

**The problem.** The opening case says "A neighboring discipline cannot supply
either on its behalf." That is a categorical claim the chapter does not prove
(S-2). P3 asks the reader to split a contested decision between FinOps and AI
Operations Management, but the chapter never works one (S-13). This matters
because Assessment 4 asks for exactly that judgment.

**Recommendation: accept both.**

- **Opening case**: "A neighboring discipline cannot supply either on its
  behalf." becomes "This book sets out both."
- **Section 3.3, a new paragraph after the FinOps paragraph** (constructed, and
  labeled so): "Until Chapter 14 draws the full border, a provisional rule
  settles most cases. An activity belongs to FinOps when it answers a question
  about the bill, and to AI Operations Management when it answers a Founding
  Question about the work the consumption served. Consider a constructed case.
  A company's monthly AI invoice arrives at three times its forecast.
  Reconciling the invoice against the contract and charging it to cost centers
  answers a question about the bill, so it sits with FinOps. Tracing the
  increase to the workflow whose requests grew, and deciding whether that
  workflow's output justifies its new cost, answers the third and fifth Founding
  Questions, so it sits with AI Operations Management. Both draw on the same
  record. Evidence that the FinOps team already traces consumption to work would
  move the second activity across the border."

P3's annual-contract dispute stays as the independent problem, as the reviewer
asks.

---

## Group 3. Making the science concrete (S-3 with S-15, S-21, S-16)

**The problem.** Section 3.1 says that a stated condition lets managers settle
a disagreement, but it never shows that happening (S-3, S-15). Section 3.2
opens on medicine and engineering before any business fact (S-21). The budget
sentence credits the budget with a job that the comparison actually does
(S-16).

**Recommendation: accept all three.**

- **S-3 and S-15, a new paragraph in 3.1 after "That is what lets two managers
  who disagree find the fact that would settle the question."**, built from
  Chapter 1's own fact-checked case, citing Chapter 1's Cursor source: "Chapter
  1's Cursor licenses show the check at work. Two of the result's conditions
  are that the buyer's cost extends beyond the access price and that
  measurement makes resource use visible. After June 2025, each request drew
  down a credit at the model provider's rate, so both conditions held for a team
  on that plan. A manager who still budgeted the licenses as a fixed software
  expense was relying on a price the conditions said no longer described the
  cost. Two conditions settled what confidence could not."
- **S-21, the opening of 3.2**: "Knowledge alone does not change what an
  organization does. Medicine draws on physiology, but clinicians treat patients
  by applying that knowledge. Engineering draws on physics, but engineers build
  bridges using codes and procedures. In each case, a practice connects the
  knowledge to the result through its own methods, roles, and standards."
  becomes "A manager can know that consumption drives cost and still have no
  forecast of next month's use, no owner for the bill, and no record of which
  team used what. Knowledge alone does not change what an organization does. A
  practice connects knowledge to results through its own methods, roles, and
  standards, as clinical practice does for physiology and engineering codes do
  for physics."
- **S-16, planning and budgeting**: "A budget is a commitment made in advance
  that makes deviations visible as they happen, before the money is gone."
  becomes "A budget is a commitment made in advance. When someone compares it
  with recorded consumption as the period runs, a deviation shows before the
  money is gone."

---

## Group 4. Sentence-level accuracy (S-5, S-8, S-9, S-10, S-11, S-20)

**Recommendation: accept all six as below.** The reviewer also suggested an
interpretive sentence inside every dated box. Claude recommends against that:
the boxes report and the body prose interprets, which keeps the boxes factual
for the fact check.

- **S-5, the DoiT box sits loosely on attribution.** Keep the box, and add one
  sentence to the body paragraph before it, after "Only the organization can
  supply the second...": "Without that record, no one can say whose work caused
  a cost, so responsibility for it can sit with several groups at once." The box
  then shows the split.
- **S-8, the Klarna case asks for detail the announcement lacks.** "Identify the
  consumption events described in the announcement and where each would be
  metered." becomes "Identify the consumption events the announcement implies
  and where each would be metered, marking what the announcement reports and
  what you assume." The Chapter 6 reveal is untouched.
- **S-9, Section 3.4 rejects provider records outright.** "It can always produce
  an answer by asking the provider, estimating, or repeating the business case,
  but none of those methods produces knowledge the organization holds and can
  check." becomes "It can always produce an answer by asking the provider,
  estimating, or repeating the business case. Such an answer counts only when
  the organization keeps the evidence behind it and can check it: a provider's
  figures reconciled against its own, or an estimate with its assumptions
  written down."
- **S-10, an invoice does not always meter.** "A provider's invoice supplies the
  first part in total." becomes "An invoice priced by use supplies the first
  part in total. An invoice priced by seat supplies neither part."
- **S-11, the busiest month need not raise the return.** "So does an evaluation
  that measures the busiest month instead of the whole quarter." becomes "So can
  an evaluation that measures only its best month instead of the whole quarter."
- **S-20, "sourcing done well" outruns the evidence.** "The switch itself was
  sourcing done well." becomes "The switch was a sourcing decision made on cost.
  Whether it was made well depends on the new model's quality and the cost of the
  move, which the record shows only in part."

---

## Group 5. Leftovers and structure (S-6, S-7, S-12, S-19)

**Recommendation: accept all four.**

- **S-6, the summary brings back the registry.** Cut "The claims are kept in a
  registry and linked by dependency. This book renders and cites only certified
  claims." This was missed in the redesign.
- **S-7, the fifth function has no key-term entry**, against your own sitting 1
  ruling 4. Add "**Holding value to account.** The function that judges, at a
  value boundary set before spending begins, whether a deployment pays for
  itself, and names one person responsible for knowing." Cut the last sentence
  of the "Value boundary" entry.
- **S-12 and S-19, two overview paragraphs in 3.2.** The first repeats the
  definition box; the second ends on book organization. Merge them into one
  paragraph that keeps the category-error link (a continuity promise to Chapter
  2) and closes on the consequence: "Chapter 1 described the problem as a
  category error. Wherever that chapter's conditions hold, AI Operations
  Management addresses the error by managing AI as a resource the organization
  consumes. The discipline has five functions that follow AI capacity through
  the organization: buying it, planning its use, recording and assigning
  consumption, routing it to work, and judging the value it returns. Each
  function is a capability an organization either has or lacks. An organization
  that lacks one does not stop consuming. It consumes without that function's
  answer." (The chapter numbers stay in 3.4, and the figure caption keeps "all
  taught in Part III".)

---

## Group 6. Marked deliberate by the reviewer (S-17, S-18)

**Recommendation: no change to either.**

- **S-17**: the THM-004 paragraph opens on an announcement. It carries Chapter
  2's continuity promise and its locked gloss. The reviewer agrees it is a
  deliberate compromise.
- **S-18**: the five Founding Questions repeat a fixed pattern. They are kept
  verbatim on purpose, and the repetition helps the reader find them again.

---

## Effect on length

The accepted edits add about 350 words net, putting the chapter near 6,000. The
new words come from teaching gaps the review found, as the G1 ruling foresaw.
