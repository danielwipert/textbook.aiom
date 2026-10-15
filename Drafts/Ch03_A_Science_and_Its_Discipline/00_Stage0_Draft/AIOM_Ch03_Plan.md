# Chapter 3 plan, version 2: A Science and Its Discipline

Process v4, step 1 (Decision 77), for Dan's sitting 1: approve, or redirect.
Replaces the 2026-10-01 plan, which is in git history. It implements
**Decision 85** (2026-10-14), Dan's seven gates: the registry stays behind the
scenes; competency C4 becomes the discipline itself; four tight teaching
sections; one dated box of real reporting per function; the function audit as
the craft section; the full cycle runs again.

## The chapter in one line

AI Business Economics is the science; AI Operations Management is the discipline
that acts on it, through five functions, inside borders that separate it from
its neighbors. Competency C4, rewritten (decision 1 below). No anchor theorem and
no new panel. Closes Part I.

## Slots

| Slot | Content | Source or object |
|---|---|---|
| 1 Opening case | KEPT as locked and fact-checked: the FinOps Foundation's mission change, February 2026; the 2026 survey; the practitioner quotation | Verified at the 2026-10-13 fact check (finops-2026-mission, -state, -what-is, -definition-2024) |
| 2 Teaching body | **3.1 The science and the practice** (about 900 words): the business problem first; AI Business Economics as an ordered body of conditional claims; one short passage on how the book shows them (numbered panels such as Chapter 2's THM-004, each with a plain-English reading; the full statements are in Appendix A); how the two layers depend on each other; Figure 3.1, the two layers (the old Figure 3.2). **3.2 The five functions** (about 2,400): the definition of AI Operations Management, then each function in timeless prose followed by **one dated box of real reporting** (five boxes). **3.3 Where the discipline ends** (about 900): KEPT, the three subjects Chapter 1 set aside and Table 3.1, the four neighbors. **3.4 Five questions the discipline exists to answer** (about 700): KEPT, the Founding Questions verbatim | Dated boxes: candidates in `AIOM_Ch03_Redesign_examples.md`, all Grade C until read. Neighbors: the verified table sources |
| 3 Craft section | **The function audit**, six steps: (1) list the deployment's AI activities (Chapter 1's inventory); (2) for each, ask which question it answers and assign it to a function; (3) assign anything that answers a neighbor's question to that neighbor; (4) mark each function no activity performs; (5) name who performs each function, or "no one"; (6) state the first gap to close and the record it needs. Worked in full on one real deployment (decision 2) | Case per decision 2 |
| 4 Summary | The two layers; the five functions; the borders; the Founding Questions, unanswered | none |
| 5 Key terms | AI Business Economics; AI Operations Management; the five functions, each named; the value boundary; the Founding Questions; the function audit. Dropped: registry, theorem, lemma, proposition, certified claim, trace, dependency, condition, scope, non-claim, falsifying case, trace procedure | Inherited vocabulary for AI Business Economics terms |
| 6 Questions and problems | Discussion: the hardest border to defend (kept); a Founding Question in a CFO's language (kept); Chapter 2's flows mapped to the functions (kept); NEW, one dated box: what would the organization have to record to answer that function's question. Problems: **P1 worked** function audit; **P2 completion** audit, steps 4 to 6 open; **P3** an ownership dispute between FinOps and AI Operations Management over one named activity, argued in a page. Then the **Part I cumulative case, KEPT** (Klarna, February 2024 announcement only) | Cases per decision 2; Klarna verified 2026-10-13 |

**Removed:** the THM-004 trace (old 3.2) and Figure 3.1; how to read a formal
claim (old 3.3); the trace procedure; the dated registry-counts box; problems P1
and P2 on LEM-020 and THM-002; the four lemma and seven proposition citations.

**Continuity promises this chapter pays** (`AIOM_Continuity_Ledger.md`):
- Ch1 to Ch3: where each neighboring subject ends. Paid by 3.3, unchanged.
- Ch2 to Ch3: "As Chapter 3 explains, the theorem formalizes the economic
  consequence of the third flow's asymmetry; it does not establish the taxonomy
  itself." See decision 3.
- Ch2 to Ch3: Chapter 3 names the discipline that resolves the category error.
  Paid by 3.2.

**Promises it makes:** each Founding Question to its answering chapter; the
FinOps treaty to Chapter 14; the Klarna reveal to Chapter 6. **Withdrawn:** the
THM-008 trace in Chapter 7's assessment (C4 no longer asks for a trace).

**Ledgers, from the first lock:** Chapter 3's 14 claim-ledger rulings are
re-ruled at the new fact check (kept where the sentence survives, superseded
where it is cut); Chapter 3's continuity-ledger rows (16 terms, 21 forward
references, 13 glosses) are reconciled at the new lock, removing what the new
text no longer carries.

**Length:** 6,000 to 7,500 words (Decision 82). One figure, one table, five
dated boxes.

## Rulings at sitting 1, 2026-10-15 (all A)

1. C4 and Assessment 4 take the wording below; C4 moves to Group 2 (Doing).
2. Craft example: Lindy.ai. P1: Uber. P2: the Australian Copilot trial.
3. Chapter 2's THM-004 promise is kept by one or two sentences in 3.1.
4. Five key-term entries, one per function.

## Decisions as put to Dan at sitting 1

1. **The wording of C4 and Assessment 4.** Proposed C4: "Place an
   organization's AI work in the discipline: assign each activity to one of the
   five functions, name the functions no one performs, and tell AI Operations
   Management apart from FinOps, MLOps, AIOps and regulatory governance."
   Proposed Assessment 4: "Function audit on a cited real deployment not worked
   in the book: list its AI activities, assign each to a function or a
   neighboring discipline, mark the functions no one performs, and defend one
   contested border in a paragraph a CFO would accept." Also: C4 moves from
   Group 1 (thinking) to Group 2 (doing), or stays.
2. **Which real deployments carry the craft example, P1 and P2.** Candidates:
   Lindy.ai (small company, Anthropic bill above payroll, all traffic moved to
   DeepSeek, NPR, July 2026); Microsoft's Copilot routing to its own models
   (Bloomberg, July 2026); JPMorgan's stated AI value (2024 to 2025). A case used
   for a problem must not repeat a dated box.
3. **Chapter 2's promise about THM-004.** Keep one sentence in 3.1 that pays it,
   or leave it unpaid and amend Chapter 2 at the holistic review.
4. **The function names in the key terms**: five separate entries, or one entry
   naming all five.
