# Chapter 3, Sitting 3: fact-check rulings

Built 2026-10-13 from three inputs, all in this folder:

- `AIOM_Ch03_Stage3_externalcheck_A.md`: check A, the sources. **WEB ACCESS: yes.**
  13 findings: 6 VERIFIED, 6 PARTLY SUPPORTED, 1 CANNOT CONFIRM (Gartner blocks
  retrieval; corroborated through Cisco). Nothing CONTRADICTED.
- `AIOM_Ch03_Stage3_externalcheck_B.md`: check B, the render only. 36 findings.
- `AIOM_Ch03_Stage3_registry_check.md`: Claude against the pinned registry. R-1.

**Dan rules every item. Claude recommends and rules none.** Each finding was
judged separately from its proposed remedy. Where Claude checked a B finding
against the registry, the evidence is given. "Keep" means no change to the text.

**Re-run cost.** Groups 1 and 2 are claim and citation edits: fact check closes
on them, then voicecheck, Stage 5 and G2. Group 3 edits teaching prose after
the review, so the scoped matrix re-runs the review for those passages only.

Three gates, one per group: A accept every recommendation in the group, B go
through the group item by item, C apply only what a source or the registry
contradicts and keep the rest.

---

## Group 1. Sources (check A, and B findings on the same sentences)

| ID | Finding | Recommendation |
|---|---|---|
| A-1, B-30 | Mission wording is "the value of cloud" / "the value of technology", not "cloud value" / "technology value". B: neither statement is quoted, so "replaced one word" cannot be checked by a reader. | **Accept.** Quote both: "For years, it had described its purpose as \"advancing the people who manage the value of cloud.\" The new statement replaced one word: \"advancing the people who manage the value of technology.\"" Keep "changed" (A's "updated" is not needed). |
| A-4 | Better source for the mission change: the Foundation's own announcement, "A One Word Change: How the FinOps Community Made Our Mission Evolution Inevitable", finops.org/insights/mission-update/, February 19, 2026. | **Accept.** Replace the Yahoo Finance syndication in `finops-2026-mission`. |
| A-2, A-5 | VERIFIED: 1,192 respondents, $83bn+, 98 percent, 31 percent is 2024 and the same measure; the quotation is in the report, from a practitioner, answering whether AI provides value. | **Record as verified.** Update the register notes. |
| A-5, B-2 | B: body and footnotes say the authors read the report, while the provenance banner says nothing was checked against it. A has now checked it. | **Fix the banner, not the body.** New banner: "Dated: February 2026. Figures and the quotation checked against the Foundation's report and announcement, October 2026." Reject B's remedy (it weakens sentences A verified). |
| A-3 | "Its central finding concerned work the discipline had not originally been created to do": the report makes AI central but does not state the history. | **Accept A's remedy:** "Its central finding concerned the expansion of FinOps into AI spending." |
| B-10 | "nearly all of them" generalizes 1,192 respondents to all practitioners. Footnote 3 says "practitioners". | **Accept, narrowed:** "...and by 2026 nearly all of the survey's respondents were managing it." Footnote 3 gloss: "Share of respondents managing AI spend, 2026 survey against 2024 survey." Reject B's second change (A confirmed the same measure across years). |
| A-6, B-12 | "a few lines of code" is not in any source; the source supports "variable consumption tracked after the fact". B: 3.5 moves "after use" from the problem into the discipline. | **Accept, narrowed:** opening case: "FinOps was built to address a specific problem: cloud consumption varied with use, and the bills arrived after capacity had been used." Cite the Foundation's "2024 Changes to the Definition of Cloud FinOps" (new register entry). 3.5, B's remedy: "FinOps was built to make cloud spending accountable when bills arrived after capacity had been used." |
| A-7, A-8, B-11 | Definition VERIFIED. B: one page cited for three accounts, and the table cell omits the value purpose 3.5 attributes to it. "Cloud cost management ... expanded into work no discipline was designed to govern" (also B-20). | **Accept.** Table cell: "Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams". Opening case: "FinOps is a capable neighboring discipline that has expanded into work it was not built to govern: the economics of an organization's AI consumption." A-8's "hardest to define" is the book's judgment: keep. |
| A-13, B-9 | Table cell "built around cloud billing" is less precise than the source; one remark is generalized to practitioners in three places. | **Accept, narrowed.** Table: "It grew from managing cloud cost and usage. Its 2026 report quotes a practitioner saying that no one can yet answer whether AI is providing value". Opening case: "The report also carried one practitioner's statement of what remained unknown." and "The quotation names the gap Chapters 1 and 2 described, in the words of someone asked to close it." |
| A-9, B-36 | Gartner glossary blocked; Cisco reproduces Gartner's wording and says Gartner coined the term. Gloss "the originating definition" rests on that secondary claim. | **Accept.** Table cell, closer to the source: "Applying big data and machine learning to automate IT operations, including event correlation, anomaly detection, and causality determination". Gloss: "Gartner's definition of AIOps." Register stays Grade C, note records the Cisco corroboration. |
| A-10 | Kreuzberger 2023: paraphrase and bibliography VERIFIED. | **Record as verified.** |
| A-11, B-28 | Klarna: every figure VERIFIED against the February 27, 2024 release. B: the resolution time is the only figure stated flat. | **Accept B-28:** "The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously." |
| A-12 | "built on OpenAI's models": the release says "powered by OpenAI". | **Accept:** "an AI assistant powered by OpenAI." |
| B-29 | Case tasks say "public record" though the case says "work from this announcement alone"; the metering task asks for a fact the announcement does not give. | **Accept, narrowed:** "whether the announcement provides an answer from the organization's own records", and "Identify the consumption events described in the announcement and where each would be metered." |

## Group 2. What the registry says (B findings, checked against dag.aiom 9d7ee50)

| ID | Finding | Registry evidence | Recommendation |
|---|---|---|---|
| R-1, B-15 | "The registry records every claim's non-claims." | LEM-015 and THM-003 have none; both uncertified. The three-flows non-claim in 3.3 comes from the book. | **Accept:** "The registry records the non-claims of every certified claim. The record is not exhaustive: the exclusion of Chapter 2's three flows comes from this book, not from the registry." |
| B-4 | "397 of the 413 were certified" lets a reader infer no theorem was certified. | Certified: 9 of 11 theorems, 20 of 21 lemmas. | **Accept:** "...and 397 of the 413 were certified, including 9 of the 11 theorems and 20 of the 21 lemmas." |
| B-14 | "no one enters it manually" while one check is a human sign-off. | Status is computed; sign-off and evidence are inputs. | **Accept, narrowed:** "The registry's validator computes that status at each version; no one enters the status by hand." |
| B-17 | "start at any theorem" and "trace any claim to the lemma level using the book alone" overreach. | Appendix A holds certified theorems and lemmas only. | **Accept:** "start at any certified theorem" and "trace any certified theorem to the lemma level using the book alone." |
| B-18 | "no conclusion rests on circular reasoning": the check sees recorded links only. | 1,776 dependency edges, zero cycles. | **Accept, narrowed:** "no conclusion rests on a circular chain of recorded support." Keep the "map" sentence (true). |
| B-25 | "A disagreement over a specific proposition can be settled." | Certification does not test truth (3.1). | **Accept B's remedy:** "A disagreement over a specific proposition concerns one stated claim, so the two sides can name the fact that would decide it." |
| B-13 | 3.4 and Key terms attribute to LEM-021 a boundary per deployment, a named owner, set before spending. | LEM-021 says none of the three. | **Accept B's remedy:** "LEM-021 requires a defined boundary whenever return is evaluated. This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary." Key terms entry narrowed to match. |
| B-21 | P2 step 6 says "the cost is not understated"; THM-002 claims a risk. | Statement: "creates underestimation risk". | **Accept B's remedy** for steps 3 and 6. |
| B-23 | P1, the worked model, states no scope although procedure step 2 says "State its scope". | LEM-020 scope: reliable visibility and authority. | **Accept B's remedy** (scope added to P1 step 2). |
| B-22 | P1 calls LEM-002's requirement a "condition"; it is a scope condition. Also asks the craft section to add LEM-002's limit. | LEM-002's requirement is its scope_condition. | **Accept P1 wording only:** "Its scope adds a requirement: ...". Keep the craft section (a new teaching addition). |
| B-7 | 3.3: an uninstrumented deployment can meet all four conditions. Craft: a team outside LEM-020's scope is outside the theorem. | THM-004's scope has no authority condition; the conditions are capability claims, so 3.3 is right. | **Accept, narrowing the craft section:** cut "and the theorem says nothing about it" and the sentence "Like the pilot ... coverage." Keep "The support for THM-004's third condition therefore does not extend to that team. The trace reveals a limit not stated in the theorem's own wording." |
| B-19 | Flat-fee branch reads as assuming the conclusion. | | **Accept B's remedy:** "A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, the contract is a falsifying case only if the organization controls the costs beyond the fee without measuring them." |
| B-24 | Registry names say more than their statements ("Creates Incentives", "Is Underestimated"). | Names are registry-verbatim (rule 4a: never edited). | **Accept the gloss, not a name change.** Procedure step 1 adds: "A claim's name is a label; only its statement says what the claim establishes." |
| B-6 | "the only route to managing that exposure" claims necessity from enabling lemmas. | THM-004 proof step 5 says "the only route" verbatim. | **Keep.** The sentence reports the recorded proof. |
| B-8 | "Costs ... grow with scale" overstates LEM-016's "may increase". | Proof step 1: exposure "grows with deployment". | **Keep.** The sentence reports the recorded proof. |
| B-5 | The pilot "fails the first condition" by assertion. | THM-004 scope: deployment "expanded from isolated or pilot use into repeated operating contexts". | **Keep.** The registry names pilot use as outside. |
| B-16 | "THM-004 formalizes the economic consequence of the third flow's asymmetry" reads as the theorem covering the flows. | Wording is locked Chapter 2's, paid as a G3 promise; 3.3 says the flows are the book's. | **Keep.** Changing it reopens a continuity promise. |

## Group 3. The book's claims about itself (B findings, teaching prose)

| ID | Finding | Recommendation |
|---|---|---|
| B-1 | Figure 3.2 caption "states what is true about consuming AI" and 3.6 "Part II establishes what is true" contradict 3.1 "checks the structure ... not its truth". B's FIX FIRST. | **Accept for the caption and 3.6:** caption "AI Business Economics states conditional claims about consuming AI and records what each one rests on." 3.6: "Part II presents the certified claims the functions rest on, ...". Keep the opening case's "a body of knowledge about what is true" (it defines a science, not certification). |
| B-3 | "The registry supports each result the book teaches": flows, functions and Founding Questions are not registry results. | **Accept, narrowed** (3.1 and summary): "The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis." |
| B-27 | "management based on them fails, however carefully managers carry it out" is absolute. | **Accept B's remedy** (3.1 and 3.4): "careful execution does not repair the decisions built on them." |
| B-31 | 3.4 describes the practice as what organizations already do. | **Accept:** "An organization that practices it buys AI capacity, ..." |
| B-32 | "resolves it by managing AI as a resource" drops Chapter 1's conditions. | **Accept:** "addresses it by managing AI as a resource the organization consumes wherever Chapter 1's conditions hold." |
| B-33 | Rate-limit example unlabelled and overstated ("whenever the other is busy"). | **Accept B's remedy** (labelled constructed; waiting when combined demand exceeds the limit). |
| B-34 | "begins with that call" puts sourcing outside the discipline. | **Accept:** "AI Operations Management begins where a model is a service an organization can buy and call." |
| B-35 | "The most costly misreading" compares costs the chapter never measured. (Kept at 2b as a frequency-sweep hit; this is a new ground.) | **Accept, narrowed:** "A costly misreading confuses necessary with sufficient." |
| B-26 | "five questions that an organization cannot answer without the discipline." | **Accept for 3.6:** "AI Operations Management exists to answer five questions from an organization's own records." Keep 3.5 ("Only the discipline can determine ..."), which states the book's thesis. |
| B-20 | "Until both exist, the practitioner's question ... remains unanswered." | **Keep.** It states the book's argument, not a fact; the "no discipline was designed" clause is fixed under B-11. |

## Not raised as findings

B's coverage notes list fifteen more sentences it judged definitional or modal
and did not rank. No action recommended.

## After the rulings

Applied in one commit. Each ruling goes into its register note with the
condition that would reverse it, and into `AIOM_Claim_Ledger.md` from the
chapter's sentence. Then: voicecheck, freqsweep, chapter_check, and (for
Group 3) a review of the changed passages; then Stage 5, G2, G3, sign-off.
