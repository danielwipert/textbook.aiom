# Chapter 3, Stage 3. Registry passages checked against the pinned registry

Checked 2026-10-13 by Claude against `danielwipert/dag.aiom` at commit
`9d7ee504dfebdac70b5fbb8087177946e4cc4cdd`, the version pinned in
`AIOM_Registry_Manifest.json`. The external checkers cannot reach the registry,
so the twelve passages citing `aibe-registry-2026` (packet C5 to C11, C13 to
C16) are checked here instead, from the registry's own files: statements, scope
conditions and exclusions in `registry/*.jsonl`, edges in `edges/edges.jsonl`,
certification rules in `scripts/validate.py`, counts and certification in the
manifest. This is a comparison of the chapter with the registry, not a check of
the registry against the world.

## Result: one finding for sitting 3, everything else matches

**R-1. "The registry records every claim's non-claims." (Section 3.3, packet
C9.)** Two claims carry an empty exclusions field: LEM-015 and THM-003. Both are
UNCERTIFIED (blocker: review_status provisional), and the book renders and cites
only certified claims. Every certified proposition, lemma and theorem has its
non-claims recorded. Proposed remedy: "The registry records every certified
claim's non-claims." The sentence predates the author pass. For Dan to rule.

## What matches

| Packet | Chapter says | Registry |
|---|---|---|
| C5 | Certified when every dependency is certified and the argument meets fixed conditions; computed by the validator, not entered | `validate.py`: certified iff local rules pass and every parent is certified (fixpoint) |
| C5 | Validator checks dependencies recorded and certified, no loops, every EMPIRICAL claim has evidence, reviewer signed off on current wording | Rules 3 to 5, rule 6 (cycles), rule 7 (only nodes flagged empirical need an evidence edge), review-signoff plus statement digest. The author pass's "empirical" is MORE accurate than the old "every claim" |
| C6 | PROP-043, PROP-053, PROP-085 quoted | Verbatim match, all three |
| C6 | LEM-020 combines those three with four further propositions and LEM-002 | LEM-020 edges: PROP-032, 039, 041, 042, 043, 053, 085, LEM-002, all Required |
| C7 | 413 objects: 140, 35, 201, 21, 11, 5; 1,777 links; 397 certified | Manifest counts identical; certified 140+34+194+20+9+0 = 397 |
| C8 | THM-004 scope: one deployment and its measurement boundary; applies when an organization seeks economic control over the resulting cost | Scope condition and statement agree |
| C9 | THM-004 does not establish that governance delivers control, is costless, the scale at which it binds, or the size of the exposure | Exclusions state each |
| C10, C15 | LEM-020 does not establish mechanisms are automatically effective, or that visibility alone determines the right policy or price | Exclusions: "automatically effective"; "optimal policy or pricing" |
| C11, C16 | LEM-021 name and statement quoted | Verbatim match |
| C13 | LEM-020 scope: reliable visibility and authority to apply mechanisms | Scope condition agrees |
| C14 | LEM-002 and its condition (record detailed enough for the relevant person to observe the activity); PROP-032, 039, 041, 042, 043, 053, 085 paraphrased | Each paraphrase agrees with its statement; LEM-002 scope: "sufficient granularity to be observed by the relevant actor" |
| C16 | THM-002 has four dependencies; LEM-006 and LEM-021 required, LEM-002 and LEM-020 contextual | Edges agree exactly |
| Panel | THM-004 panel: scope, antecedents (i) to (iv), consequent | Matches the registry statement; no antecedent added, dropped or changed |
