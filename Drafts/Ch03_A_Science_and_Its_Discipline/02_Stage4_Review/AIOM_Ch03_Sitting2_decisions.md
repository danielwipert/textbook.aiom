# Chapter 3, sitting 2: one decision list (Decision 77)

Built 2026-10-01. The independent review raised 44 findings (R-1 to R-44, in
`AIOM_Ch03_Review_claude_findings.md`). **Claude applied every finding that was a
standing-rule breach, a factual or fidelity error, or a defect with a plain fix:**
R-1, R-3 to R-8, R-11, R-13, R-17, R-18, R-21 to R-24, R-26, R-28 to R-33, R-35 to
R-37, R-39 to R-43, and the wording half of R-15. R-12 and R-38 were resolved by
those edits. R-19, R-20 and R-44 were noise. The second-model review (the prompt in
this folder) has not run yet; its findings join this list when it returns.

**What is left is yours.** Each has a recommendation. "All recommendations" is a
valid answer.

| # | Finding | Decision | Recommendation |
|---|---|---|---|
| 1 | G1-1, R-19 | Decision 33 sets a word band only for Chapters 1 and 2 (6,500 to 7,500). Chapter 3 is now 6,364. | **Set the band for Chapters 3 to 15 at 6,000 to 7,500.** Decision 33's own text says the band was moved to fit what Chapters 1 and 2 became, not to a target. Your author pass may add length; padding to reach a floor would not help. |
| 2 | R-2 | C4 asks a reader to trace a theorem they have not seen, but the chapter never says where to read the registry. Appendix A will carry theorems and lemmas only (Decision 72), so a reader cannot go below lemma level unaided. | **Tell me whether the `dag.aiom` registry will be public.** If yes, 3.1 names it. If no, 3.1 says that Appendix A reaches lemma level and propositions are cited by ID, and the assessment on THM-008 supplies the propositions. |
| 3 | R-16 | Problem P1 traces LEM-020, not THM-004 as the plan said, because the craft section already works THM-004 in full. | **Accept.** A second worked trace, on a lemma, is the model assessment 4 needs. |
| 4 | R-15 | A fourth discussion question (matching flows to functions) goes beyond the plan's three. | **Keep.** It is the interleaving question, the same device Chapter 2 uses. |
| 5 | R-9 | "Without it, the other functions have nothing to work from" (3.4) starts an argument about function order that the Part III introduction owns. | **Cut the sentence.** |
| 6 | R-10 | The Founding Questions run in function order, and their answering chapters run 7, 10, 8 and 9, 11, 12. | **Add one clause:** "Part III takes them in a different order, for reasons given there." |
| 7 | R-14 | The Klarna case says "do not use anything published afterward", which hints there is something to find and partly spends Chapter 6's reveal. | **Change to "Work from this announcement alone."** |
| 8 | R-25 | Four lemma IDs and names arrive in prose before Figure 3.1. | **Leave to the production step**, where figure anchors are measured, not reasoned about. |
| 9 | R-27 | 3.1 defines five kinds of registry object before any example. | **Keep.** Section 3.2 instantiates each one within a page. |
| 10 | R-34 | The five function paragraphs share one template. | **Keep the parallel openings.** The fix added an instance to three of them, so their lengths now vary. |
| 11 | D3, D10 | The frequency sweep lists 16 sentences. None states how often organizations do something: they are logic, importance, structure, or inside problems. | **Keep all 16.** |

Separately, and not part of Chapter 3's list: **Chapter 2's THM-004 panel does not
render the registry statement** (Chapter 3 checklist D9). That fix is a Chapter 2
amendment and is put to you on its own.
