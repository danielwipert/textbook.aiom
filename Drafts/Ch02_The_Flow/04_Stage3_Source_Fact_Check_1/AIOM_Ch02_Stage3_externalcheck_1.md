# Chapter 2 Stage 3: external fact check 1

Received 2026-08-29 from Dan. Recorded here as the check Dan rules on.
**Claude rules none of it.**

**THE ONLY ALTERATION IS PUNCTUATION AND IT CHANGES NO WORD.** The response was
written with em dashes. Standing rule 1 bans them in every file in this repository,
so each has been replaced by a full stop, a comma, a colon or a pair of parentheses
at the same break. Nothing else is edited: no finding is reworded, reordered,
softened or summarized, the reviewer's own labels stand as written, and their
transcription slips ("accound", "acound", "footote") are left as received.

**THE RESPONSE ARRIVED DUPLICATED**, the same text twice, and is recorded once.

**THE REVIEWER HAD NO WEB ACCESS AND SAYS SO IN ITS FIRST LINE.** That is the single
most important fact about this check and it governs how every finding below is
ruled. See Claude's assessment, which follows the review in its own section.

---

## The review as received

Here's my fact-checking overview. One honesty note up front that I owe you: I don't
have live web access in this environment, no browser, no lookup tool, so I can't open
Forbes, Fortune, or the MIT document the way a New Yorker fact checker would at a
terminal. What I can do is check the chapter against (a) the primary documents I do
hold, and (b) my own knowledge of the public record, clearly separating "corroborated"
from "can't confirm." Here's where it lands.

**1. The Australian DTA / Microsoft 365 Copilot trial: VERIFIED, passes.**
This is the chapter's strongest source, and it holds up. The Australian Government did
run a whole-of-government Copilot trial in the first half of 2024, through the Digital
Transformation Agency; around sixty agencies took part; several thousand licences were
issued; pricing was per seat; and the DTA commissioned and published an independent
evaluation [1]. The evaluation did rely on participants self-assessing effects and did
acknowledge there was no pre-trial work baseline [1]. Every substantive claim in
Problem P3 matches the public record. If the book's sourcing were all at this level,
I'd clear it today.

**2. The Uber / Claude Code episode: PLAUSIBLE, but UNVERIFIABLE from my side.**
This is the opening case and the crux of the chapter, and it's the part I cannot
certify. The general shape is consistent with real reporting on Uber's Claude Code
usage. Uber genuinely has been one of Anthropic's largest coding-assistant customers,
and its AI spend has been a documented leadership concern. But every specific
load-bearing detail here (the 2026 AI budget exhausted by April, the roughly five
thousand engineers from December 2025, the per-engineer monthly cost range, the COO
publicly asking whether it was worth it) is dated 2025 to 2026, after my own
knowledge, and rests on the paywalled primary accound via Forbes and Fortune [1]. The
dates are internally consistent, which is necessary but not sufficient. This claim
must be carried as "pending verification," which is exactly what the book's own stamp
says [1].

**3. The MIT "GenAI Divide" 95% figure: SUSPICIOUS AS CITED, correctly hedged in the
text.**
The figure (95% of enterprise GenAI pilots with no measurable P&L impact) matches a
real, heavily discussed 2025 report finding, and the chapter is right that it
attracted substantial methodological criticism and that reported interview counts
conflict [1]. Good handling in the prose: it uses "no measurable impact" as an
observability claim, not a value claim [1]. But the citation itself is suspect. "The
GenAI Divide: State of AI in Business 2025, MIT NANDA" [1] is malformed enough (the
all-caps fused "NANDA") to raise the question of whether it's a placeholder or a
mangled name. That footnote needs the primary document produced with a real author
line before the number can be relied on.

**4. The adoption footnotes: FAIL, and internally contradicted.**
Footnotes 3 and 4 cite "Multiple secondary outlets, May 2026": no outlet named, no
URL, no page [1]. That's not a citation; it's a placeholder. And there's a genuine
internal contradiction a fact checker has to flag: the body prints "about a third" of
the engineering organization by February and "a large majority" a month later [1],
while footote 3 annotates the same adoption as "reported, not quantified" [1]. You
cannot print specific percentages and annotate them as unquantified without a
reconciling note explaining where the numbers came from.

**5. Self-regulation quality: GOOD, unusually so.**
Credit where due: the chapter discloses its own pending-verification status [1],
labels its worked example as stipulated rather than real [1], says outright it asserts
nothing about how much value any deployment produces [1], and hedges the COO claim
with "suggests" and "the public acound does not establish" [1]. That's better sourcing
discipline than most published work shows. It just means the authors already know the
exposure is in the Uber case, not the argument.

**Bottom line:** Two of the chapter's four sourced claims are unverifiable as cited,
one citation is malformed, and the adoption notes are self-contradicted. The DTA trial
is the one clean pass. My verdict stands as delivered: I would not clear this to press
until the Forbes and Fortune pieces are produced, footnotes 3 and 4 are given real
outlets, and the "roughly a third" vs. "not quantified" conflict is resolved [1]. The
argument survives; the evidence needs work, and the book helpfully says so itself [1].

---

## Claude's assessment. This is Claude's, not the reviewer's, and Dan rules all of it.

**THIS CHECK CANNOT CLEAR STAGE 3, AND THE REVIEWER SAYS SO IN ITS FIRST LINE.** It
had no web access, which puts it in exactly the position Claude is in and which
CLAUDE.md calls structurally external for that reason. It read no primary. Two of its
five findings do not survive contact with the artifact; three do, and all three are
fixable without reading anything.

### REJECTED. S3-R1, the DTA trial is NOT verified, and accepting this would be the most expensive error available here.

The reviewer marks the DTA trial "VERIFIED, passes" and offers "around sixty agencies
took part; several thousand licences were issued; pricing was per seat". **The chapter
says, in P3: "Around sixty agencies took part", "several thousand licences were
issued", and "The licence is priced per seat rather than by unit of use."** The
reviewer read those sentences and then reported that its recollection agrees with
them. That is corroboration by a model with no source access, and it is circular.

**This is the confirmatory shape this project has already been burned by.** Chapter
1's first craft review returned "meets all six criteria, no findings" and was
withdrawn as confirmatory. The register note for `dta-copilot-2024` records the
opposite of convergence: **"THE SECONDARY COVERAGE DISAGREES WITH ITSELF ON EVERY
COUNT"**, with agency counts of 56, almost 60 and more than 60 all appearing. A
confident "around sixty" from an unsourced recollection is the signature of one
upstream number repeated, which is the exact reasoning on which Dan withdrew the
adoption percentages on 2026-08-21.

The entry stays Grade C and UNVERIFIED. Nobody has read the evaluation.

### WITHDRAWN 2026-08-29, THE SAME DAY IT WAS RAISED. S3-R2 WAS CLAUDE'S ERROR, NOT THE REVIEWER'S.

**The rejection is withdrawn in full. The reviewer was right.** Findings 2 and 5 say
the chapter discloses its own pending-verification status, and it does. **The
provenance line on page 1 reads: "Dated: December 2025 to May 2026. Figures and dates
are drawn from press reporting of a paywalled primary account and are pending source
verification. See the source register."**

**THE REJECTION RESTED ON A GREP FOR THE WRONG STRING.** It searched the render for
"pending verification" and for "unverified", and the chapter says "pending SOURCE
verification". One intervening word, zero matches, and a confident "no such stamp
exists in the book" written on top of it. **This is the failure this repository
documents more than any other: a check that reads green while measuring something
other than what it claims**, and it is worse here than in the tooling, because the
output was not a gate but a ruling handed to Dan.

**What the original rejection got right is only that the packet also carries
"UNVERIFIED" and "Grade C".** That is true and irrelevant: the reviewer did not use
either phrase about the chapter, and the phrase it did use is in the book, on page 1,
in the amber provenance line gate 7 exists to guarantee.

**The rest of finding 5 stands too, and was never in dispute**: the worked example is
labelled stipulated, section 2.8 says outright that the chapter asserts nothing about
how much value a deployment produces, and the executive sentence is qualified.

**S3-R1, the DTA rejection, is unaffected.** Its reasoning is independent of this one
and still holds: that finding is a model with no source access reporting that its
recollection agrees with three sentences it had just read.

### ACCEPTED. S3-1, footnote 3 contradicts the sentence it annotates. Cheap, and needs no source.

Footnote 3 reads: **"Reported adoption, not quantified. See the register."** The
sentence it annotates reads: **"By February, about a third of the engineering
organization was using it. Within a further month it had reached a large majority."**

"About a third" is a quantity. The gloss says the adoption is not quantified. Both
cannot stand. **The reviewer overstates it slightly**, since the chapter prints no
percentage and "about a third" is a characterization, but the contradiction in wording
is real and a copy editor or a press checker will stop at it every time.

The gloss is what is wrong, not the sentence: Dan withdrew the PERCENTAGES on
2026-08-21 and "not quantified" was written to mean "no percentage is given here". It
should say what it means.

### ACCEPTED. S3-2, footnotes 3 and 4 name no outlet, and that is a ruling Dan already made pointing the other way.

The reviewer calls "Multiple secondary outlets, May 2026" a placeholder rather than a
citation. **As a bibliographic entry that is correct**, and a university press would
not set it.

**But the absence is deliberate and is Dan's own ruling.** The register records that
the February and March percentages "appeared across several outlets with consistent
values and no consistent attribution, which is the signature of one upstream source
being repeated rather than of corroboration", and that the figures came out rather
than a citation being invented. Standing rule 2 has no option for citing a source you
cannot name.

So the question this finding really raises is not "name the outlets". It is **whether
a footnote should exist at all where no document is being cited.** Three options, and
this is Dan's:

- **(a) Drop the citation markers.** The two sentences become uncited characterizations
  of reported adoption. Honest, and it removes the placeholder a press checker objects
  to. Costs the reader any pointer at all.
- **(b) Name the outlets actually seen.** Requires reading them, so it is external work
  and cannot be done here.
- **(c) Keep the markers and reword the gloss** so it says plainly that no single
  source could be attributed and why. Keeps the pointer, drops the false promise of a
  citation, and is the option that pairs with S3-1.

### ACCEPTED, WITH THE REMEDY ALREADY BOOKED. S3-3, the MIT NANDA container is thin.

The reviewer flags "MIT NANDA" as possibly a placeholder or a mangled name, and asks
for a real author line. **The reaction is fair and it is what the register already
says the entry needs**: its `upgrade` field reads "The report PDF itself, which the
case bank records as not yet obtained", and its note instructs Stage 3 to obtain the
report and confirm the wording of the headline finding.

Nothing to fix here without the document. The finding's value is that an independent
reader stopped at the same place the register already marks.

### The reviewer's own bottom line is the right one and it is unchanged by any of the above.

It would not clear this to press until the Forbes and Fortune pieces are produced.
**Neither would Claude, and neither does the register.** `fortune-2026-uber-coo`
remains the entry the chapter's argument leans on hardest, and its note already says
that if Stage 3 cannot confirm it, the paragraph and problem P1 need rework rather
than a looser number.

### What this check did NOT do, stated so the next one is not asked for the same thing.

It read no primary, so it moved no entry off Grade C. **Run a second external check on
a different prompt**, per CLAUDE.md: Chapter 1's pair agreed on one finding out of six
and the disagreement was the value. A second check with the same absence of web access
will produce the same class of result, so the useful second check is one with source
access, or a human at a terminal with the two articles open.
