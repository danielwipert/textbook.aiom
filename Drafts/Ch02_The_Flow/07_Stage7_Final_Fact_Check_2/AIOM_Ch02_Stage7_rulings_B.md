# Chapter 2, Stage 7. Check B, and what Dan has to rule.

Written 2026-08-30. **Claude rules none of it.** Every quote below was verified present in
the current chapter, and every claim was dated against the pre-copy-edit text to separate
what the copy edit introduced from what Stages 1 and 3 already examined.

**THE PAIR WORKED.** A read the sources and found four contradicted facts. B was given the
render and nothing else and found a different class entirely: **sentences that contradict
the chapter's own statements of what it does not know.** No source check can see that, and
no gate can either. They overlap on nothing.

---

## TIER 1. GLARING. Fix before anything else.

### B1. The chapter says it cannot know Uber's internal state, then states it. CRITICAL.

> "Public reporting does not establish whether Uber made the category error described in
> Chapter 1 ... **It does show that the deployment scaled before the company had a
> mechanism to control its cost or measure its return.**"

Two paragraphs later the chapter says the public account does not establish "what
consumption data Uber could see or when it became available, or whether the provider
offered spending limits or alerts that the company declined." **If that is unknown, the
company's lack of a control mechanism is unknown.** The sentence claims the thing the
limits paragraph disclaims.

**The copy edit made this worse.** It read "a deployment that scaled without a mechanism
able to govern its economics", which was already an internal-state claim; the new form is
more specific and more assertive.

**Proposed:** "It does show that nothing in the public account identifies a control that
changed the course of the spending, or a measure that connected the use to a return."

### B4 and B5. THE CRAFT DIAGNOSTIC FAILS ITS OWN FIRST TEST. CRITICAL, AND IT IS A RECURRENCE.

The chapter sets two tests: "First, the organization must be able to state the condition of
the flow **from a record it holds itself.**" The mapping then says:

> "**The record flow is also partly managed.** A per-engineer cost range was reported,
> which suggests that consumption was visible at some level of detail."

**A reported figure shows the number reached a journalist. It does not show Uber held a
record.** Section 2.2 draws exactly that line: the provider always keeps a record because
it must bill, and the buyer holds one only if it built one. **The diagnosis takes evidence
that satisfies neither test and returns "partly managed".**

**THIS IS THE DEFECT THE 2026-08-21 BIAS REVIEW ALREADY FOUND ONCE**, recorded in CLAUDE.md
as its most useful finding: that Chapter 2's craft diagnostic failed the test its own
section 2.2 sets, and that Claude had not seen it. **It was not fully closed, and a second
independent reader has now found it again.** That is the strongest signal in either check.

**It cascades to three places**, and a fix to one alone leaves the other two lying:

1. the craft mapping, above;
2. P1's setup, "finds two partly managed flows and a cost-and-value flow with only its cost
   half built";
3. P1's model answer, "a record flow available at some level of detail but without
   attribution, and a value half that was never built."

**Proposed, craft mapping:** "The record flow cannot be settled from the public account,
and the reason is the first of the two tests. A per-engineer cost range was reported, which
shows the figure existed somewhere. It does not show that Uber held it, because the
provider always keeps a record and the buyer holds one only if it built one. Nothing
reported shows that anyone attributed the consumption to teams or compared it with the
plan."

**Proposed, P1 setup:** "finds a partly managed usage flow, a record flow the public
account cannot settle, and a cost-and-value flow with only its cost half built."

**Proposed, P1 model answer:** "The mapping found a usage flow measured in people rather
than requests, a record flow the public account cannot settle, and no public evidence of a
built value half."

**THIS MAKES P1 BETTER, NOT WEAKER.** The honest answer to "what would a February review
have needed" is stronger when the chapter admits it cannot tell whether the record existed,
because that is the chapter's whole subject.

### B9. A quoted STATEMENT is called a "question" twice. CLEAN FACTUAL FIX.

The chapter quotes "That link is not there yet," he said. **Check A confirmed the statement
form against both Fortune and the transcript.** Two later sentences call it "the chief
operating officer's question". A third paraphrase widens it: "His statement suggests that
any documented return remained unavailable" is broader than a quote about the link between
Claude Code use and consumer features.

**Proposed:** "question" becomes "statement" in both later uses, and the paraphrase narrows
to "His statement says the link between that use and the consumer features was not yet
available to senior leadership."

### B10. "Appears unbuilt" in the craft section, "was never built" in P1.

The same fact at two strengths, and the stronger one is in the worked answer students copy.
**Covered by the P1 wording above.**

### B2 and B7 INVERTED. The limits sentence is too broad and contradicts two VERIFIED facts.

B flags "No contract had been renegotiated, and no vendor had raised its prices" and "Uber
was paying for consumption" as unsupported. **B is wrong about the evidence and right about
the contradiction.** Both are Stage 3 verified: rows A2 and A6, passed by Dan, and A6 is
"the usage-based commercial terms". **B could not know that, because it was given no
packet by design.**

So the fix runs the other way. The limits sentence says the public account does not
establish "what the contract priced", which sweeps in the pricing BASIS that is verified.

**Proposed:** "The public account does not establish the contract's specific terms, what
consumption data Uber could see or when it became available, or whether the provider
offered spending limits or alerts that the company declined."

---

## TIER 2. FIVE UNSOURCED GENERALIZATIONS THE COPY EDIT INTRODUCED.

Each was checked against the pre-copy-edit text. **In every one, a sentence that made no
population claim acquired one.** Standing rule 2 allows a citation, a recast, or a cut, and
none of these is cited.

| # | Now | Was | Proposed |
|---|---|---|---|
| B12 | "By the **usual measures**, the rollout looked like a success." | no equivalent | "By adoption measures, the rollout looked like a success." |
| B18 | "Once the organization marks the project delivered, **managers stop revisiting** the business case." | no equivalent | "Once the organization marks the project delivered, nothing requires anyone to revisit the business case." |
| B20 | "In practice, the records **usually** sit in one of three places." | "It lives in one of three places." | "In practice, the records sit in one of three places." |
| B22 | "**It usually rises as the deployment expands** and can be reported without..." | "It can be presented without..." | "It can be reported without anyone defining what the deployment was supposed to improve." |
| B24 | "**Most of the work** required to manage the flows must occur before a deployment scales." | no equivalent | "The work required to manage the flows is easiest before a deployment scales." |

**B22 is the one Claude already flagged to Dan at Stage 6** as the single new unsourced
claim the copy edit added. B found it independently.

---

## TIER 3. THE FQ8 SHAPE, IN A SENTENCE FQ8 DID NOT COVER.

> "In a first-year deployment, the mapping **commonly finds** a healthy usage flow, an
> absent record flow, and a cost-and-value flow with only its cost half built."

**FQ8's ledger entry says there cannot be an observational base for what this mapping
finds**, because the three-flow mapping is this book's own construct, introduced on the page
before, so no organization has run it. Stage 3 withdrew "Two failure modes recur when
organizations run this mapping on themselves" for exactly that reason, and the Stage 6 copy
edit brought it back as "Two common errors", which was repaired this week.

**This is a third instance of the same claim, in a sentence none of that touched.** It is
pre-existing, so Stage 1 and Stage 3 both passed over it.

**Proposed:** "In a first-year deployment, the mapping can find a healthy usage flow, an
absent record flow, and a cost-and-value flow with only its cost half built."

---

## TIER 4. TWELVE PRE-EXISTING CLAIMS. THIS IS A SCOPE DECISION, NOT A FIX.

B applies standing rule 2 strictly and finds about a dozen more claims about what
organizations usually, commonly, normally or almost always do. **Every one predates the
copy edit**, so Stage 1's frequency sweep and Stage 3's fact check both saw them and
neither withdrew them.

**Some are defensible on the record and should NOT be reopened:**

- **"Organizations skip the record flow most often for structural reasons" is RULED CLEAN.**
  Stage 1 cleared it explicitly as its sixth candidate, on the ground that section 2.5
  derives it, and FQ4's REVERSES-IF records that. **Do not reopen it.**
- **"The provider always keeps a record because it must produce a bill" is a DERIVATION,
  not a population claim**, and it is inherited from Chapter 1. Changing it is a continuity
  question for G3, not a Stage 7 fix. B's observation that P3's per-seat licence has no unit
  meter is sharp, but the chapter's justification is billing AND capacity management, and
  capacity management holds under per-seat.
- **"The rarest of the three because ..."** carries its own derivation in the same sentence.

**Others are genuine unsourced population claims with no derivation attached**, notably
"Organizations fund most AI deployments as projects", "project funding usually leads to an
annual review", "the ordinary case in the first year of a deployment", and "the record flow
is the one organizations almost always build last".

**THE REAL QUESTION IS NOT THESE TWELVE SENTENCES. It is that Stage 1 listed five
candidates and cleared a sixth, and a reader with no packet found roughly a dozen more of
the same shape.** That is evidence about the SWEEP rather than about any one sentence, and
it will repeat on Chapter 3 unless the sweep changes.

**Claude's recommendation: do not do these piecemeal at Stage 7.** Tiers 1 to 3 are
contradictions and new damage and belong to this step. Tier 4 is a deliberate pass over one
class of claim across the whole chapter, and doing half of it now leaves the chapter
inconsistent in a way that reads as arbitrary. **Book it as its own pass, with the Chapter
3 process change beside it.**
