# Session handoff

Last updated: 2026-08-14. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session, alongside the voice and craft card.

## Repository state

**THE POST-LOCK EDITING RUN IS OPEN. Dan is revising every paragraph of Chapter
1 and the process is CLAUDE.md section 8, "POST-LOCK (POST-LIVE) AUTHOR EDITS".**
Merged to `main` 2026-08-15 from
`claude/chapter-1-editing-versioning-tfixx1`, four commits, fast-forward. The
working protocol is four steps and Claude does not negotiate the prose: apply
verbatim to the one live text, run `amend.py Ch01 -m "..." --rule`, report one
line. The only thing raised unprompted is a NEW empirical claim with no source,
because standing rule 2 is not a lifecycle step and no gate reads it.

**THE LANDING PAGE HOOK IS NOW THE CHAPTER'S OWN SENTENCE, "Beneath every seat,
a meter was running."** Chapter 1 paragraph 2 verbatim apart from its opening
"But". This is gate W9a's rule applied to the one part of the page W9a does not
reach: the hero was the last place on the site still paraphrasing the book
rather than quoting it. The lede absorbed the old two-clause headline, so no
argument was lost. "Most organizations" lost its "Most", an unsourced quantity
of exactly the shape standing rule 2 governs inside the book. **`llms.txt`
needed no edit**, because its summary is extracted from the rendered hero.

**A HEADLINE'S LINE BREAK IS SET BY TYPE SIZE, NOT BY `text-wrap`, AND THE SWEEP
IS THE ONLY WAY TO KNOW.** The hook breaks at its comma from 360px up and goes
to three mid-clause lines at 320px. `text-wrap: balance` was ALREADY on the rule,
so the bad break was the balanced result; `text-wrap: pretty` was measured and is
a REGRESSION, dangling an "a" at 360, 390 and 430px, the widths that currently
work. The only lever that moves 320px is the clamp minimum, sharply: 1.95rem
still breaks badly, 1.85rem does not. **Dan ruled it left as is**, because that
minimum binds below about 845px, so it would shrink the headline on every phone
to fix the narrowest one, and a media query tuned to this sentence would need
re-deriving at every copy change. Booked here so it is not rediscovered.

**`--rule` WAS BUILT 2026-08-14 ON DAN'S RULING AND IS THE DEFAULT FOR THIS
RUN.** It retires whatever rulings an edit breaks in one pass, so the gate no
longer costs a round trip. It retires only what actually broke, from the same
evaluation W14 runs. Two fixes went in with it: `--dry-run` no longer writes the
ledger, and `amend.py` stopped printing a hardcoded web-gate count that had been
stale since W15.

**THE FIRST AMENDMENT OF THE RUN IS `da595e7`, AND IT DEMONSTRATED THE BLIND SPOT
RATHER THAN A RULE WORKING.** Dan's revision of the light-and-heavy-user
paragraph reintroduced the SF2 and SF8 continuation mechanism IN DIFFERENT WORDS.
W14 matched no forbidden string and stayed silent; it failed only on CE11, whose
required sentences were gone. SF2 and SF8 were retired by hand because `--rule`
could not have named them. **This is the third instance of that shape.** It is
the standing argument for reading the passage as well as running the gate, and it
is now recorded in CLAUDE.md section 8 rather than only here.

**A SELF-TEST CONTROL WAS ANCHORED ON PROSE AND THE EDIT KILLED IT.** The FC9
control injected after "The credit was consumed in a handful of prompts", which
`da595e7` deleted, so the injection became a no-op and the control tested
nothing. It asserted rather than passing, which is the design working. It now
injects at the first paragraph tag. **A FORBIDDEN control must never anchor on
prose carrying no ruling**; the REQUIRED controls are safe because each mutates
its own ruled sentence. Still 97 of 97.

**THE FULL TOOLCHAIN INSTALLS AND RUNS IN THIS CONTAINER, INCLUDING THE
BROWSER.** `pip install -r requirements.txt` plus `poppler-utils` and the Pango
and Cairo libraries. Contrary to the note below about the pinned browser, a
Chromium sits at `/opt/pw-browsers` and `web_build.py` globs it, so **W6, W15 and
W16b all RAN rather than skipping**: 20 widths clean, 33 links followed across 7
pages served over HTTP, Archivo confirmed on the page by measurement.

**ARCHIVO IS CONFIRMED ON THE PUBLISHED PAGE. Dan read the live Chapter 1
opening on 2026-08-14 and approved the face.** That closes the v0.5 to v0.6
sequence: the complaint was raised from a rendered page, the replacement was
chosen from a rendered specimen, and the result was confirmed on the deployed
site. **No step of it was settled by reading a description of a typeface**, which
is the rule the drawn marks already follow and which now has a second instance
behind it.

**MERGED TO MAIN 2026-08-14, CI GREEN, SITE DEPLOYED, BRANCH RETIRED.** `main` is
at `d411ec9`, the working tree is clean, the remote holds `main` alone and
`git_hygiene.py` reports nothing stranded. `status_check.py` reports Chapter 1 at
13 of 13, STATUS CONSISTENT. The branch deletion needed Dan again, for the third
time and by a third route; the rule is in Standing reminders and was not
relitigated.

**GATE W16 CLOSES THE TYPEFACE HOLE, 2026-08-14, RULED BY DAN THE SAME DAY IT WAS
BOOKED. THE WEB SUITE IS W1 THROUGH W16, SIXTEEN GATES, 97 SELF-TEST CONTROLS.**
Re-derived from build output, which is the standing rule for this count. W16a
reads each `@font-face` against the committed file, so it needs no browser and
always runs; W16b reads the served page; W16c reads figure labels. The verdict
line now says "W6, W15, W16b AND W16c NOT RUN", naming the parts rather than the
gate, because W16a did run.

**THE GATE FOUND THREE DEFECTS IN ITSELF BEFORE IT FOUND ANYTHING ELSE, AND EACH
IS A RULE.**

1. **It reported a 5.14 per cent phantom on the landing page.**
   `getComputedStyle().font` serializes to an EMPTY STRING in Chromium, so
   `span.style.font = cs.font` set nothing and the probe inherited the BODY's
   size rather than the paragraph's. It read correct on the chapter page, where
   those two sizes happen to be equal, and wrong on the landing page, where they
   are not. **Copy font properties one at a time; the shorthand is not reliable
   in either direction.**
2. **Deleting the font file made it print "SKIPPED, browser unavailable" while a
   browser sat there running.** The expected metrics were read inside the browser
   block, so the missing file raised and hit the catch-all. **A check whose setup
   can fail on the fault it hunts must have that setup outside the catch-all, or
   the fault reads as an absence.**
3. **The swapped-file control reported no failure, because the gate compared the
   build against itself.** Expected metrics came from the staged copy, which is
   the same file the browser loads, so any consistent substitution agreed with
   itself.

**AND THE FOURTH WAS FOUND BY CI, NOT BY THE CONTROLS: W16b WAS GREEN HERE AND
RED ON EVERY PAGE IN CI.** It compared a browser measurement against the font
file's own `hmtx` metrics, which answers two independent questions at once, which
face rendered and how the renderer measures it. The runner disagreed by about two
per cent in both directions and **could not be reproduced here, because the
pinned browser build will not download into this container**. The fix is a
division rather than a tolerance: a file is compared to a file, by SHA-256, in
W16a, and every W16b comparison now has both sides rendered in the same browser,
in the same page, at the same moment, so whatever the renderer does to one it
does to all of them. Its third leg is the page's own fallback chain with the
declared face removed, which is what absence looks like on that page and needs no
knowledge of which face a platform substitutes.

**THIS IS ALSO WHY THE FIX COULD BE PUSHED WITHOUT KNOWING WHICH WAY CI WOULD
GO.** Either the runner was rendering a fallback, in which case the new fallback
leg fails and says so plainly, or the old failure was an artifact of comparing a
rendering to a file, in which case it passes. It cannot hide the first case to
achieve the second, which is the only property that made it safe to ship while
main was red.

**CI ANSWERED IT: THE RUNNER RENDERS ARCHIVO.** The run is green, W16a, W16b and
W16c all ran there, 97 of 97 controls passed there, and the site deployed.
**That is a positive result and not a silence**, because the fallback leg is
what would have fired had the runner been substituting a face, and it is the one
leg that cannot be satisfied by a page rendering in the platform's font. So the
original red was the comparison, not the rendering.

**WHAT REMAINS UNEXPLAINED, RECORDED AS UNEXPLAINED: why that runner's browser
measured about two per cent away from the font file's own hmtx metrics** when
this container's measures within 0.165 per cent. Some shaping or advance
handling differs between the two Chromium builds. It no longer decides
anything, because no comparison in the gate crosses that boundary now, but it is
the reason the boundary must not be crossed again by a later check that wants a
convenient reference number.

**THE TOLERANCE IS 0.5 PER CENT AND THE OBVIOUS 1 PER CENT WOULD HAVE BEEN
USELESS.** Kerning moves a measured string at most 0.165 per cent from the font's
own metrics, which invites a round one per cent. **Liberation Sans, which is what
generic `sans-serif` resolves to on the build container, sets the probe 0.91 per
cent from Archivo**, so a one per cent band would have passed the single most
likely fallback of all. Measure the FALLBACK before setting the tolerance, not
only the kerning.

**Nine controls, and the first is the real defect**: Plex Sans Text at
usWeightClass 450 declared as font-weight 400, the thing that survived six phases
of green builds. The rest are the classes it implies, one per way a face can be
wrong. Two of them fired only after the gate was fixed, which is the controls
doing their job rather than confirming it.

**THE WEB BODY FACE IS ARCHIVO, CSS v0.6, RULED BY DAN 2026-08-14. Branch
`claude/chapter-text-font-uv7ywk`, MERGED to main 2026-08-14 and CI green.** v0.5 had made the roman
a true Regular 400 the day before, which fixed the weight and left the shape, and
the shape was the remaining objection: Plex is a technology company's
documentation face and reads as the default choice rather than a chosen one.

**THE FACE WAS CHOSEN FROM A RENDERED SPECIMEN, NOT FROM DESCRIPTIONS.** Seven
candidates were set in real Chapter 1 prose at the shipping conditions, with a
17px/20px toggle and a blind mode, and published as an artifact for Dan to read
at his own window size. **The tool is committed as `specimen.py`**, because the
rule it implements is now in CLAUDE.md and a rule with no implementation gets
rebuilt from scratch by the next session. This is the
drawn-marks rule applied to type: **render the sheet, do not reason about the
shapes.** Three candidates were ruled out before taste entered, on the weight
ladder: two carried no 600 and one had no static italic at all. A fourth took the
measure to 76 characters, past the top of the 45 to 75 band.

**FONT HOSTS ARE BLOCKED FROM THIS CONTAINER AND npm IS NOT.** The proxy answers
403 to CONNECT for `fonts.googleapis.com` and `raw.githubusercontent.com`, so the
OFL TTFs came from the `@expo-google-fonts/archivo` npm package, which ships the
upstream files and the licence unmodified. Worth remembering: the registry is
reachable for any Google Fonts family, which is the only font route that works
from here.

What changed, all of it web-only:

- Four Archivo 2.001 faces in `fonts/use/`, `fonts/OFL-Archivo.txt`, and
  `fonts/README.md` rewritten, since it was already one file stale and now has to
  carry the print-versus-web split.
- **`--body-face` is new and the family is named ONCE.** Three places consume it,
  two rules in `AIOM_web.css` and `web_build.tokenize_svg`. The URL-policy lesson
  applied before it could bite: a policy repeated in three places is wrong in two.
- **The chapter's SVG figures carry `font-family="Plex"` ten times, and
  `tokenize_svg` now remaps it** exactly as it remaps colours, to
  `var(--body-face)`. Without it every figure label would have stayed in the
  print face while the prose beside it moved. Attribute changes, no text changes,
  W1 unaffected, locked chapter untouched. **`var()` resolves in an SVG
  `font-family` presentation attribute**, checked in a browser, not assumed.
- One new self-test control, **88 now**. It is asserted directly rather than
  through a gate, because no gate can see a typeface substitution. It was proved
  by injecting three faults, remap disabled, remap unscoped, remap over-broad,
  and it fires on all three.

**VERIFIED, AND THE FIRST ATTEMPT AT THE VERIFICATION WAS ITSELF WRONG TWICE.**
The measurement selected `#chapter-text p`, which is the provenance line in Jost,
and reported a face and a measure belonging to neither the body nor the question.
The note sweep then reported "no floated notes" at every width including 1920,
because it looked for `.sidenote` and the class is `.note`. Both were rewritten to
name what they selected and print it. **A check that reads green while measuring
nothing is still this repository's signature failure, and it produced two in one
session.** What holds after the fixes: body renders Archivo 400 at 17px/1440 and
20px/1920; the probe sets at 3310.9px against Plex Regular's 3388.3px, so the
face genuinely loaded; the measure is 72.7 characters at every width; six notes
float above 1420px and go inline at 1420 and below, none off the edge at any of
21 widths; all fifteen web gates pass with W1 identical at 43,204 chars; 88/88
self-test controls; and the print build passes its fifteen gates with `pdffonts`
showing five faces, none of them Archivo.

**TWO DEAD RAIL ANCHORS, FIXED 2026-08-13, AND THE GATE THAT CALLED THEM LIVE.**
Dan clicked the Craft section link in the navigation rail and nothing happened.
Opening case was dead the same way and nobody had clicked it. Both had been dead
since Phase W1, through every green build since.

`add_anchors` wrote the slot id before the LAST CHARACTER of the pattern match.
Three of the six `SLOTS` patterns match a bare opening tag, so that was right
for them; the other two match a whole element, because matching the label text
is the only way to tell one slot label from another, and for those it produced
`</p id="slot-craft-section">`. An attribute on a CLOSING tag, which every
parser discards, so the id was in the file and never in the DOM. It cuts at the
first `>` now, correct for both shapes.

**THE GATE IS THE LARGER HALF. W4b counted ids with a regex**, which matches
inside a closing tag, so two anchors no browser could see counted as live
targets, and W4c took that same set and reported that every internal link
resolved. Both readers parse now, through `AnchorCollector`, and the gate also
fails when an id is in the markup but on no element. Chapter reader and page
reader were changed together, or the landing page would keep the defect the
chapter is protected from. **A regex answers whether text is present; it cannot
answer whether an element exists.**

**A LINK IS VERIFIED BY FOLLOWING IT, AND NOTHING HERE EVER HAD.** The fix was
checked by driving a browser through all twelve rail links and asserting where
each lands. Roughly fifteen lines of Playwright, and the only method that would
have caught this. Do it after any navigation change. The self-test control
reproduces the real malformed markup rather than an invented fault, so the suite
is now **75 controls**.

**THIS IS THE SECOND DEFECT IN TWO DAYS THAT NO GATE COULD SEE AND A PERSON
FOUND BY USING THE SITE**, after the body roman being half a step heavy through
six phases. Neither is a gap in a particular gate. Both are the same gap: **the
suite measures the artifact and never exercises it.** W1 compares text, W3 scans
marks, W4 matches strings, W6 measures layout, and nothing clicked.

**GATE W15 CLOSES IT, ruled by Dan the same day.** It loads every emitted page,
clears the hash, clicks every internal link and measures where the target lands,
AND serves the tree over HTTP at the prefix it deploys to, failing on any
subresource 404. 33 links across 7 pages. **The suite is now W1 through W15,
FIFTEEN gates, with 80 self-test controls**, derived from build output rather
than copied forward, which is the standing rule for it.

**THE HTTP HALF CAME FROM DAN ASKING WHETHER CLAUDE CAN ACTUALLY VIEW THE SITE.
It cannot, and asking found a second live defect.** The published URL is
unreachable here: the proxy answers 403 to CONNECT for `danielwipert.github.io`,
logged by name. Every browser check before that had loaded the build from
`file://`, the same artifact CI publishes but not the same CONFIGURATION.
Serving at `/textbook.aiom/` exposed the 404 page linking its stylesheet as
`/assets/aiom_web.css`, which on a project site points at the root of the USER
site: the live 404 was unstyled with every link leading out of the book. It was
the only root-absolute path in the build, and 404 is the one page that cannot
use a relative one, since Pages serves it for any missing address at any depth.
`--base-path` supplies the prefix and CI derives it from the repository name.

W15 is the SECOND optional gate, since it needs the same headless browser W6
does. `--no-browser` skips both and the verdict line reads "W6 AND W15 NOT RUN".
CI installs the browser, so both run there.

**Two details inside W15 are load bearing and must survive any rewrite.** The
hash is cleared before each click, because clicking a link whose hash is already
current is a no-op in every browser, and without that a second visit to an
anchor reports the previous landing as a fresh pass. And a target at the foot of
the document cannot reach the top of the window, so arrival is accepted when the
page is at its end and the target is on screen; without that exception the last
anchor on every page fails forever, which is how a gate gets switched off.

Its three controls are the real defect and the two it implies. **Two of the
three are invisible to every other gate**: an anchor on an element that is
`display:none`, and a click swallowed by a handler. That is what makes W15 a
gate rather than a duplicate of W4's hardened parse.

**LLMS.TXT AND ONE URL POLICY, 2026-08-13. ON `main`.** `/llms.txt` publishes
the llmstxt.org map of the site: an H1 name, a blockquote summary, then H2
sections of links, in markdown. **It quotes the site and writes nothing new**,
taking its summary from the landing page's own hero, extracted from the rendered
index rather than retyped, so the two cannot drift. The chapter list comes from
what actually locked and built, the counts from the transformed body, the part
names from the structure document.

**IT WITHHOLDS WHAT EVERY OTHER PAGE WITHHOLDS**: no chapter "Big idea",
"Competency" or "Anchor theorem" line, because CLAUDE.md section 9 rules that
later chapters withhold deliberately and **a file addressed to a machine is not
an exemption from that**, and no register note, which W9b enforces everywhere.

**WRITING IT FOUND THE 404 DEFECT IN TWO MORE EMITTERS.** With no domain ruled
the sitemap emitted `/ch01/` and robots.txt pointed at `/sitemap.xml`, both of
which address the root of the USER site when served at `/textbook.aiom/`. Three
emitters had answered the same question separately and two had it wrong.
`site_url(base_url, base_path, path)` is now the single answer, verified across
all four shapes.

**GATE W10 RESOLVES EVERY ADDRESS IN `llms.txt` AND `sitemap.xml` BACK TO A
FILE**, fails one that escapes the deploy prefix, checks a fragment is a real
anchor on its target, and checks the chapters listed are exactly the chapters
built. W15 cannot cover either file: it drives a browser over emitted HTML and
neither is one. W3 runs over `llms.txt` too. **87 controls now.**

**`llms-full.txt` IS UNRULED AND WAS DELIBERATELY NOT BUILT.** It would publish
the whole book as one scrapeable document, which is a different decision from
publishing a map of it, and it belongs with the domain ruling.

**THE WEBSITE-EDITS SESSION, CLOSED 2026-08-13. Everything is on `main` and
there is nothing else anywhere.** It was closed and reopened several times as
Dan kept finding things, and every count written inside it went stale each time,
so the numbers here are DERIVED at the final close rather than remembered:
**19 commits, of which 8 changed the site or the build and 11 are records.**
Check the git log rather than trusting a number in prose. The remote holds ONE
branch, `main`, for the first time in this project's history. `git_hygiene.py` reports nothing
stranded and no branch safe to delete, the tree is clean, local and remote are
`0 0`, and `status_check.py` reports Chapter 1 locked at 13 of 13, STATUS
CONSISTENT. **No work sits on a branch. There is nothing to merge up.**

**Eight changes shipped and NOT ONE TOUCHED THE CHAPTER TEXT**, so no lifecycle
step moved and no amendment was needed. That is the point of the presentation
layer being a separate file, and it is the first session about this chapter that
cost the lifecycle nothing.

Three to the reading surface: the v0.4 reading scale, the v0.5 body roman, and
term linking. One to the toolchain: **`playwright` is pinned**, and the
workflow's bare `pip install playwright`, which ran after the requirements
install and would have overridden it, is gone. Four to correctness: the two dead
rail anchors and the two gates that had called them live, **gate W15**, the live
404 page plus W15's HTTP half, and **`llms.txt`** with the one URL policy it
forced. All eight are described below.

**THE SUITE ENDED AT FIFTEEN GATES AND 87 CONTROLS**, up from fourteen and 74.
W15 is the only check in either suite that EXERCISES the site rather than
measuring it, and W10's address resolution is the only one that follows a link
outside an HTML page.

**THE PATTERN IS WORTH MORE THAN ANY OF THE EIGHT. Six began by checking
something the repository already asserted, and the assertion was wrong every
time.** The column was 71 characters where the stylesheet said 66. The body
roman was weight 450 where the CSS said 400. The section 17 breakpoint sum had
been missing a whole term since Phase W2, covered by a cushion nobody had
reasoned about. Two gates agreed that a rail link resolved when it went
nowhere. Every page was believed to load its stylesheet, and the 404 page never
had. The sitemap and robots.txt each stated an address for this site that
pointed outside it. **None of those was findable by reading the code, because
the code asserted the wrong thing in each case.**

They were found by rendering the page, measuring the result, clicking the link,
and serving the tree at the address it actually deploys to. That is the lesson
the drawn spot marks and the hyphenation scan had already taught elsewhere,
arriving three more times in one session.

**THE GENERALISED FORM, AND THE ONE TO CARRY INTO CHAPTER 2: this project's
checks measure artifacts and rarely exercise them.** Both defects a human found
this session had survived six phases of green builds. W15 closes the navigation
and the subresource half of that gap. Nothing yet closes typography, which is
how the body roman sat half a step heavy through the same six phases, and no
gate is proposed for it because the line changes about once a year.

**WHAT CLAUDE CAN AND CANNOT SEE OF THE SITE, since it decided two findings.**
It CAN render, click, measure and serve the built tree in real headless
Chromium, which is the artifact CI publishes from the same commit. It CANNOT
load the published URL: the egress proxy answers 403 to CONNECT for
`danielwipert.github.io`, logged by name. **So nothing between CI and the reader
is checkable here**: a failed deploy, Pages caching, or a settings change. That
last mile is Dan's.

**Next session starts on `main` and starts on CHAPTER 2**, unless Dan brings
more website edits, in which case the rhythm that worked was: change, gates,
self-test, render a sheet at the size it ships at, commit with the reasoning in
the message, then update the three documents.

**TERM LINKING, 2026-08-13. ON `main`.** A bolded key term in the chapter text
is now a link to the definition callout that owns it. Built by
`web_build.link_terms()`, which gives each callout and key-term entry an id and
wraps the matching bold runs: attributes and an element, no text, so gate W1a
still reports the web prose character-identical to print at 43,204 chars. **The
chapter HTML is shared with print and is never edited for this.**

**THE MATCH IS ON THE TERM, NEVER ON THE TAG**, because bold does two jobs here.
Five of Chapter 1's nineteen bold runs name a defined term; the other fourteen
are the craft section's worksheet labels ("Meter:", "Step 3. The meter.") and two
pieces of ordinary emphasis. Matching folds case, collapses whitespace and drops
ONE leading article. **Trailing punctuation is deliberately not stripped**: it
would let "Meter:" match a term named Meter and turn a form field into a link. A
term with no callout still links, to its key-term entry, because otherwise four
bolded terms are links and a fifth identical-looking one is not.

**GATE W8a CAUGHT A REAL BUG IN THIS CHANGE AND THE NEAR MISS IS THE LESSON.**
Giving every `.kt` block an id broke two patterns expecting the tag to close
immediately. Widening one to `<div class="kt"[ >]` LOOKED equivalent and was not:
`find_spans` returns the text after the opener MATCH, so the rest of the tag
stayed inside the block and W8a reported all eight terms as differing from the
ledger. It is `[^>]*>` in both places now, and the two must move together,
because the drift failure is the opposite one and it is SILENT: an opener
demanding an immediate `>` matches nothing and W8a compares an empty set and
passes. Fourth time a hand-rolled pattern over this file's nested markup has
been the defect.

The build prints the term-link count and warns on zero, because rewording a term
would delete every link with no gate failing.

**Open: the dark-theme landing tint moves only 4 to 8 levels** and may be too
subtle. It is the shared `:target` device, so changing it changes the sidenote,
the glossary row and the sources entry too. And only Chapter 1 has exercised the
matching rules; Chapter 2 is their first real test.

**THE BODY ROMAN, `AIOM_web.css` v0.5, 2026-08-13. ON `main`.** Dan read the
chapter at 1920 in Chrome and said the type felt heavy, and that the weight
seemed to change with the window. **THE WEIGHT NEVER CHANGED**: computed
`font-weight` is 400 at every width and nothing varies it. What v0.4 made fluid
is the SIZE, and the same face set larger reads heavier. The symptom was
reported accurately and the mechanism named was the wrong one, which is a shape
worth expecting: measure before agreeing or disagreeing.

Chasing it found a defect older than v0.4. The body roman was
`IBMPlexSans-Text.ttf`, `usWeightClass` 450, declared as `font-weight: 400`
since v0.1, so web body prose had always been half a step heavier than it
announced, and the italic beside it is a true 400, so **the roman and its own
italic had never matched**. Neither fact is visible in the CSS, which says 400
in both places. It took reading the font's OS/2 table. The web roman is now
`IBMPlexSans-Regular.ttf`, Plex 3.005, the same release as every other face in
`fonts/use/`. Print keeps Text and is unchanged.

**NO GATE IN EITHER SUITE COULD HAVE CAUGHT THIS AND NONE CAN CATCH ITS
RETURN.** A face substitution changes no text, so W1's equivalence holds
perfectly, and print gate 5 inspects the faces embedded in the PDF rather than
the weight a web stylesheet declares. Six phases of green builds passed over it.
No gate is proposed, deliberately, but the hole is recorded in CLAUDE.md and in
plan section 16.

**VERIFY A FONT SWAP BY MEASURING A STRING, NEVER BY LOOKING**, because a face
that fails to load renders identically to one that changed nothing. Text sets
the 77-character probe at 723.34px and Regular at 716.59px; the built page
reports the second. The measure survives at 71 characters, a 0.9 per cent move,
so the section 17 arithmetic is untouched. The PRINT build was re-run for the
same reason, since "print is unaffected" was a claim: all fifteen print gates
pass and gate 5 reports no unexpected face, proving the new file is embedded
nowhere in the book. `web_build.py` globs `fonts/use/*.ttf`, so a web-only face
must still be a TTF and still sits in the directory print reads from.

**If the page ever reads a shade LIGHT, the answer is not to go back.** Nudge
`--ink` darker: perceived weight is partly contrast and there is ample AA
headroom above the W13 floor.

**THE READING SCALE, `AIOM_web.css` v0.4, 2026-08-13. MERGED TO `main` AND
LEVEL.** Dan asked why Chapter 1's text column ran so thin on the site. It does
not, and the first answer given was wrong because it reasoned from the CSS
instead of rendering the page. Measured in a browser against the chapter's own
prose in its own face, the column is **71 characters**, near the top of the 45 to
75 band; the stylesheet had claimed 66 since v0.2, which was the half-em rule of
thumb rather than a measurement. Mobile measures 49 characters at 390px and
needed nothing at all.

What reads as thin is the ratio, not the measure: before v0.4 the column held 28
per cent of a 1920px window. **Only three things can move it, the measure, the
type size, and the alignment rule.** Capping the reading area cannot, because a
centred child of a centred container lands in the same place at every cap, and
the variant built to test that rendered pixel-identical to the build it was meant
to improve.

v0.4 buys presence with type size instead: the root is
`clamp(17px, 8px + 0.625vw, 20px)`, so the column grows from 544px to 640px while
holding 71 characters and spending no readability. Below 1440px nothing moves,
and phones stay at 16px. `--note` narrows to 14rem and `--rail` does NOT: the
first attempt narrowed both and wrapped the contents rail, and the rail is
content while the note track is clearance. The breakpoint lands at **1420px**,
below the 1440px it was, so a 1440px window GAINS margin notes.

**THE SECTION 17 SUM WAS WRONG AND HAD BEEN SINCE PHASE W2.** It gave 1411px
while omitting the `.reading` padding, a whole term, and it never showed because
the media query sat at 1440px and a 29px cushion nobody had reasoned about
covered the gap. That is worse than the 1240px breakpoint it replaced: a
breakpoint set by eye announces itself as a guess, while a sum that is off by a
term and lands inside its own safety margin reads as rigour until a token moves.
Re-derived in rem, since the fluid root makes every term scale together.

**THE DEFECT THIS AREA PRODUCES CANNOT BE A GATE.** A floated note hanging past
the window edge does not make the page scroll, so W6 is blind to it, and it is
exactly what the 1240px breakpoint shipped. Verified instead by sweeping 24
widths from 1400px to 2560px and comparing each floated note's right edge with
the viewport. Re-run that after any change to `--note`, `--note-gap`, `--measure`,
`--rail`, `.reading`'s padding, or either stop of the clamp. The script is not
committed; it is about fifteen lines of Playwright and is quicker to rewrite than
to find.

Three commits, fast-forwarded to `main` from `claude/website-edits-upsmk4`.
Verified in this order before anything was pushed: `git_hygiene.py` first
(CLAUDE.md section 9 rule 1), then a fetch, then `git log origin/main ^HEAD`
empty. Fourteen web gates pass with W6 RUN rather than skipped, 74 of 74
self-test controls behave, and `status_check.py` reports Chapter 1 at 13 of 13.
CLAUDE.md and `AIOM_Web_Edition_Plan_v1.0.md` both carry the corrected
arithmetic; the plan gains section 15.

**ONE OPTION IS BOOKED AND UNRULED: the margin could be filled rather than
reserved.** Chapter 1 calls six notes across 6,853 words, so the side track is
empty for almost the whole chapter, and the layout is built for a book with heavy
marginalia that the book does not yet have. Moving figure captions or key-term
glosses into the margin would make the space read as designed rather than as
leftover. It is a decision about Chapters 2 to 15, not about CSS, and it is the
only option that answers Dan's original complaint without touching a
measurement.

**NOTE FOR THE NEXT SESSION: `playwright` IS NOT IN `requirements.txt`.** Gate W6
and the width sweep both need it, and it had to be pip-installed by hand. The
container's Chromium is at
`/opt/pw-browsers/chromium-1194/chrome-linux/chrome` and the pip version expects
a newer build, so `p.chromium.launch()` fails and `executable_path` must be
passed explicitly. Worth pinning, which would also stop W6 silently reporting
SKIPPED in a fresh container.

**EDITING A LOCKED CHAPTER IS SOLVED END TO END, 2026-08-13. This is the headline
and it is what unblocks everything else.** Dan is an iterative writer who will be
revising Chapter 1 forever, and until today every edit to it cost a trip through
a thirteen-step lifecycle and held CI red for the duration. Three pieces, built
in the order Dan ruled, each independent of the others.

1. **SAFE. Gate W14, claim preservation, reads `AIOM_Claim_Ledger.md`** and fails
   the build when a ruled sentence goes missing or a withdrawn one returns. It is
   the only gate in either suite that reads MEANING, and it exists because five
   recorded incidents changed meaning while every date and figure stayed intact,
   so nothing mechanical could see them. Verified against all six historical
   reverts rather than invented faults.
2. **DECOUPLED. `snapshot.py` publishes each chapter's LAST LOCK, never the
   working tree.** Reopen Chapter 1, leave it open for a week, push freely: the
   site keeps serving the lock SILENTLY and CI stays green. Before this, a reopen
   failed the whole site build with "no locked chapter found".
3. **FAST. `amend.py` edits a locked chapter in one command,** about twenty
   seconds, reopening nothing. Dan's edit is approved by definition and
   supersedes. Only the mechanical gates run, and `--supersede` retires a
   fact-check ruling he overturns.

**THE WEB SUITE IS NOW FOURTEEN GATES, W1 THROUGH W14, WITH 74 NEGATIVE
CONTROLS.** Re-derive both from build output rather than copying them forward:
the count in this file was wrong for five phases before anyone checked it.

**THE DESIGN ACCENT PASS ALSO LANDED, 2026-08-13.** Dan's brief was "New Yorker
meets Comptoir des Cotonniers", accents not an overhaul. Paper grain on the
ground, a department rule on `.eyebrow`, and nine spot marks drawn as INSTRUMENTS
rather than jokes, because C6 rules out the New Yorker's wit even as the book
borrows its technique. **Marks are chrome only, ruled by Dan and enforced by gate
W4g**, which was needed because W1 cannot see a mark: an SVG carries no text, so
text equivalence with print stays perfect while a reading page fills with
ornament. `AIOM_book.css` is untouched throughout, so print is unaffected.

**THE REPOSITORY IS PUBLIC AND THE SITE IS LIVE, 2026-08-13. HISTORY WAS
REWRITTEN THAT DAY AND EVERY SHA WRITTEN BEFORE IT IS DEAD.** Any commit hash in
an entry below this one refers to the pre-rewrite history and will not resolve.
The tree is unchanged apart from the removals recorded here; only the hashes
moved.

`main` is at the rewritten tip and carries the LICENSE. 182 commits, down from
183 because one became empty when its only content was purged. The remote held
`main` and `claude/book-website-privacy-check-ewd96o` and nothing else at the
time this was written; that second branch was deleted by Dan on 2026-08-13.

**WHAT WAS REMOVED, AND WHY IT IS NOT A SECRETS INCIDENT.** A sweep before going
public found NO secrets: no keys, tokens, credentials, emails, phone numbers or
internal hosts, in the tree or across all 183 commits, and every document's
metadata carries only its generator name. What it found was material that should
not be published even though none of it is secret. Ten files were purged from
all history with `git-filter-repo` and force-pushed:

- Four Northmoor files that gave away the Part III problem sets.
  `northmoor_answer_keys.md` is the worked solutions, `northmoor_checks.py`
  prints them when run, `northmoor_emit.py` builds the answer text inline, and
  `northmoor_gen.py` carries the engineered causes as named constants, so
  reading it alone hands over Property B. Dan holds copies outside the repo.
  **THE GENERATOR IS GONE FROM THE REPO, SO THE DATASET CANNOT BE REBUILT HERE.**
  `northmoor_construction_note.md` still names it and the seed, which stays true
  as a statement of how the data was made.
- Six superseded Chapter 1 drafts that stated withdrawn claims as the book's own
  assertion: the three files in `archive/`, and the three that sat beside the
  live text. Removing those three leaves `00_Stage0_Draft/` holding exactly one
  file, which is what Decision 50 always required.

**THE LOCKED CHAPTER'S BODY PROSE WAS CLEAN AND WAS VERIFIED SO, NOT ASSUMED.**
The five withdrawn sentences were pulled out of the register notes and grepped
across every artifact including PDFs and `.docx`. All five appear in
`AIOM_Ch01_redraft.html` only inside its register notes, never in the prose,
confirmed by splitting the file at the Decision 51 boundary. The stage artifacts
that still carry them are kept deliberately: a file under `08_Stage6_Copy_Edit`
named round4 reads as a working proof rather than as the book, and the claim
inventories and checklist are the record of the withdrawal doing its job.

**FOUR BRANCHES WERE DELETED AND ONE CARRIED WORK, ABANDONED ON DAN'S RULING.**
`chapter-1-status-gli2c0`, `stage-7-explanation-sdsb38` and
`textbook-website-design-h9nk9t` were fully merged. `chapter-1-handoff-review-sbkq2u`
held three commits `main` did not have, last touched 2026-08-05: a reading-copy
PDF, a copy-edit worksheet and `build_copyedit_worksheet.py`, all written into
Process v1 folder names that the v2 renumbering retired, and all superseded by
the `copyedit_export.py` and `copyedit_import.py` pair. Dan ruled abandon.

**CLAUDE COULD NOT DELETE BRANCHES AND THIS WILL RECUR.** The session's git
credentials permit push and force-push but return 403 on any ref deletion. Force
-push was proven on Claude's own branch before `main` was touched, rather than
assumed. Branch deletion is Dan's to do, in the GitHub UI or from his own
terminal, and a session that needs it should ask early rather than discover it
mid-rewrite.

**A PRE-REWRITE BUNDLE OF ALL 183 COMMITS WAS TAKEN AND IS ALREADY GONE.** It
lived in the container scratchpad, which is reclaimed with the container. The
remote is now the only copy of anything.

Verified after the rewrite rather than claimed: zero hits for all ten paths
across the full history OF A FRESH CLONE rather than of the working copy,
`status_check.py` at 13 of 13, all web gates passing, every
self-test controls behaving, and `git_hygiene.py` reporting nothing stranded.

The record of the pre-rewrite state follows and its hashes are dead.

**MERGED TO `main` AND LEVEL, 2026-08-13.** `main` carries the whole web edition,
twelve commits, fast-forwarded from `claude/textbook-website-design-h9nk9t`,
which was then levelled back onto `main` so nothing sits on the branch alone. No
commit SHA is pinned here: the commit that writes this line moves `main` past any
SHA it could name, and a stale hash in a handoff is worse than none. Verified rather than assumed, in this
order and before anything was pushed: `git_hygiene.py` first (CLAUDE.md section 9
rule 1), then a fetch, then `git log origin/main ^HEAD` empty, then
`git merge-base --is-ancestor` confirming `main` was a strict ancestor. After the
push, `git rev-list --left-right --count origin/main...<branch>` reports `0 0`.
The build, the self-test and `status_check.py` were all re-run ON `main` after
the merge: the gates pass, the controls behave, Chapter 1 reports 13
of 13.

`claude/textbook-website-design-h9nk9t` is now FULLY MERGED and safe to delete.

**A CLAIM IN THIS FILE WAS WRONG AND IT WAS WRITTEN THIS SESSION.** The previous
revision said "the remote is clean and now holds two branches" and "the 2026-08-12
stranding is FULLY RESOLVED, all three leftover branches are gone from the
remote." Neither was true. It was written from intention rather than from a
sweep, which is the exact failure CLAUDE.md section 10 records under "write a
scope claim from what was done, never from what was intended", and it is the
sixth instance in this repository. `git_hygiene.py`, run at session close as the
rule requires, found four branches:

  main                                     the trunk, carries everything
  claude/textbook-website-design-h9nk9t    LEVEL with main, safe to delete
  claude/chapter-1-status-gli2c0           fully merged, safe to delete
  claude/stage-7-explanation-sdsb38        fully merged, safe to delete
  claude/chapter-1-handoff-review-sbkq2u   +3, NOT merged, ruled superseded

Deletion is Dan's: `git push --delete` returns 403 from this environment.

**THE ONE BRANCH `main` DOES NOT HAVE, AND WHAT IS ACTUALLY ON IT.**
`claude/chapter-1-handoff-review-sbkq2u` carries three commits from 2026-08-05,
inspected rather than guessed at: a Chapter 1 reading-copy PDF, a copy-edit
worksheet `.docx` and its manifest, a HANDOFF revision, and
`build_copyedit_worksheet.py` at 304 lines. That script is the Process v1
predecessor of `copyedit_export.py` and `copyedit_import.py`, both of which are at
the repository root and have since round-tripped a real chapter. The branch was
already ruled superseded and marked for deletion. It was NOT merged here, and
that is a deliberate choice rather than an oversight. Recovery tip is `68bc904` if
the worksheet script is ever wanted.

**THE DURABLE LESSON, repeated because it will recur: A DELETED BRANCH IS NOT
GONE WHILE A SESSION HOLDING IT IS STILL ALIVE.** A long-running container carries
a local ref and full push rights, so a push from an old session recreates what was
just deleted. Close the sessions, then delete.

**THE WEB EDITION IS COMPLETE THROUGH PHASE W6 AND IS ON `main`.** Chapter 2 is
the next DRAFTING target and is unblocked. Thread 8 below is the live record of
the web sub-project.

## Chapter 1 status: **LOCKED 2026-08-13, 13 of 13.** THE FIRST LOCKED CHAPTER

`status_check.py` reports 13/13 STATUS CONSISTENT. 25 pages, 7,069 words on the
Decision 33 measure, fifteen gates green against CSS v7.1, `voicecheck.py`
mechanically clean and house style clean on all five checks, G3 passing against a
populated ledger.

**WHAT LOCK MEANS FOR ANYONE OPENING THIS FILE NEXT: do not edit Chapter 1.** No
change without an explicit `reopen.py`, which re-runs every step from the one
owning the change. The full lock record, including what lock does NOT mean, is
under Stage 9 in the checklist and should be read before any reopen is considered.

**THE LEDGER NOW HOLDS A CHAPTER, WHICH CHANGES WHAT G3 DOES.** Eight owned terms,
five forward references to Chapters 2, 3, 4, 6 and 14, and one registry gloss for
THM-009. Until today G3 compared every chapter against an empty ledger and could
not fail. From Chapter 2 onward it can, and it will: those five forward references
are now promises a later chapter is held to, and "category error" plus seven other
terms may not be redefined.

**THE CRAFT BASELINE BAND IS IN FORCE FOR THE FIRST TIME**, set from the locked
text and written into `AIOM_Voice_and_Craft_v1.md` section 4. From 2026-08-05 until
today no chapter was read against a band, deliberately, because the earlier numbers
measured a chapter the copy edit had replaced. **Chapter 2 is the first chapter
read against one.** Two things in that block stop it being misused: the numbers are
advisory proxies and never thresholds, and the band contains a known flat stretch
at 1.1 that Stage 4 ruled a deliberate choice, so the mean is a description of what
shipped rather than a target.

**TWO ITEMS WERE OPEN AT LOCK AND STAY OPEN.** The "early May" preview-bill timing
in footnote 3, which external check 2 could reach only through secondary coverage
and which no Claude session can verify, and the THM-009 numbering question, which
is a Stage 2 or Stage 5 matter rather than a fact check. **A locked chapter with
two open items is an honest record; one claiming none would not be.**

Historical, and the record of how it got here:

**STAGE 6 IS CLOSED, ON DAN'S RULING OF 2026-08-12: "I have no more edits."**
Second closure of this step and the one in force. Fourteen copy edits raised, ruled
and applied, CE1 through CE14. It does NOT mean a further round is impossible:
Decision 24 places the step late so it runs on prose that has stopped moving, and
prose that moves again reopens it. The reversing condition stands, and a finding
from any later read enters as CE15.

**THE RECORD WAS FIVE FINDINGS SHORT WHEN THE RULING ARRIVED, AND WAS COMPLETED
BEFORE THE TICK.** CE10 to CE14 were in the live text with no entry in the
checklist, because the session that applied them ran concurrently with the
reconciliation and wrote its record into commit messages instead. Reconstructed
verbatim from `d19bf74` and `fceb220`; the chapter text was not touched. **CHECK A
STEP'S FINDINGS LIST AGAINST THE TEXT BEFORE TICKING IT, NOT AFTER.** A tick is a
claim about a record, and this record described a chapter five edits older than the
one on disk.

**THE PART 5 RULE 1 PROXY IN `voicecheck.py` IS DEFECTIVE AND ITS NUMBERS MUST NOT
BE QUOTED.** Recovered from the CE10 to CE12 record. It counts fronted adverbial
phrases as subject-verb separations, and a fronted adverbial is right-branching and
permitted, so both its baseline and its after-reading were measuring something the
rule does not cover. Fourth check in this repo to read authoritative while measuring
nothing. The sound measure moved: 40 long comma-fenced asides to 35. **This is
unfixed and is the one open defect in the ported house-style checks.**

Nothing downstream was invalidated by the tick: the last edit to the live text was
CE13 and CE14, and G2 was re-run after it.

**G2 PASSED ON THE RECONCILED TEXT, run from the top rather than carried forward.**
Fifteen gates, 25 pages, all twenty-five read at 150 dpi with the rasters deleted
and regenerated first so no page from the previous run could be read by mistake. No
new defect. Gate 15 ran against this chapter for the first time and reports zero
straight marks, which is independent confirmation by tooling that the PG2 fix
survived the reconciliation. Hyphenation with page turns included: 95 line ends,
zero inside a brand name, zero at a page turn.

**THE FIGURE GEOMETRY CHECK WAS WRONG ON ITS FIRST ATTEMPT, AND THIS IS THE THIRD
CHECK IN THIS REPO TO READ GREEN WHILE MEASURING NOTHING.** Pixel sampling with a
tolerance of 14 cannot separate `--amber-fig` #C0521A from `--amber` #B4551F, which
differ by 12 in red, so both matched every pixel and the check would have passed a
figure using the wrong token. It was re-run by taking dominant saturated colours
exactly. **WHEN A CHECK COMPARES COLOURS, MAKE THE TOLERANCE SMALLER THAN THE
DISTANCE BETWEEN THE TOKENS IT MUST TELL APART, OR MATCH EXACTLY.** It was caught by
noticing both tokens reported identical hit counts, which is impossible if they are
different colours, not by re-reading the code.

Historical, and the reason G2 was reopened at all:

**G2 HAD BEEN GREEN AGAINST PROSE THAT NO LONGER EXISTED.** It was passed 2026-08-11
against the pre-CE3 text. CE3 to CE6 were then ruled and applied on 2026-08-12 by the
reconciliation, the scoped re-run matrix sends a copy edit to G2, and no re-run was
made against the reconciled text. So `status_check.py` read 8 of 13 STATUS
CONSISTENT while a gate was green against prose that no longer existed. That is the
same shape as the 2026-08-08 reopen, and it happened again for the same structural
reason: a merge can invalidate a gate that neither side re-ran, because each side
was internally consistent. **AFTER ANY RECONCILIATION, RE-CHECK EVERY GATE TICK
AGAINST THE DATE OF THE LAST EDIT THAT COULD MOVE IT.** Nothing mechanical does
this today.

**EVERY G2 FROM NOW ON IS FIFTEEN GATES.** Gate 15, typographic marks, was added
2026-08-12, first ran against this chapter at the re-run above, and passed.

**`gen_checklists.py` WAS EMITTING FOURTEEN GATE BOXES WHILE THE BUILD RAN FIFTEEN,
AND BOTH ARE FIXED.** A G2 pass could have been ticked without gate 15 ever being
recorded. This is the 2026-08-05 drift running the other way: then the checklist
claimed checks the build never performed, now the build performed one the checklist
did not list. Both produce a gate that reads green while nobody looked. G2 is now
eighteen boxes. Found only because CLAUDE.md requires checking box TEXT against the
generator after a reopen, since `reopen.py` resets ticks and does not regenerate
text.

**STAGE 7 IS OPEN. EXTERNAL CHECK 1 IS BACK AND ARCHIVED; FOUR OF ITS FIVE
PRECISION FLAGS ARE APPLIED.** Full record under Stage 7 in the checklist.

**STAGE 6 AND STAGE 7 BOTH HAVE WORK APPLIED, FROM TWO DIFFERENT SESSIONS THAT
DID NOT SEE EACH OTHER.** Both sets are now in one text.

  CE1 to CE6           Stage 6 copy edits, applied 2026-08-10 to 2026-08-12
  FC2, FC3, FC4, FC5   Stage 7 fact-check narrowings, applied 2026-08-11
  FC1                  OPEN, and half of it is decidable without a source
  CE7, CE8, CE9        raised and UNRULED, listed in the checklist

**FC1 IS THE ONE LIVE CHAPTER DEFECT AND IT IS VISIBLE ON PAGE 11.** The July 2025
dated box carries no date in its prose, and the paragraph after it opens "Eleven
days later", so the reader is asked to count eleven days from nothing they have
been given. That half needs no source. The other half does: the interval is
measured from the July 17 press report rather than from the encounter the report
dates to July 14. Of the two remedies offered, "eleven days after the first
reports" keeps the precision and supplies the antecedent; "two weeks later" blurs
both.

**BOTH PRODUCTION FLAGS WERE PHANTOMS, AND THE CAUSE IS PROCEDURAL: THE CHECKER
WAS GIVEN THE CHAPTER HTML RATHER THAN A RENDER.** Theorem 1's four antecedents
render intact on page 9 and P3's table is correct; the extraction dropped `<li>`
contents and collapsed empty cells leftward. Stage 3 fed PDFs and Stage 7 must too,
on every chapter. They carry no FC number, because they were disproved rather than
ruled. Note that the P3 flag would reproduce even against the PDF under naive text
extraction, since an empty cell contributes no text: it dies only to a read or to
the geometry.

**EXTERNAL CHECK 2, ON A DIFFERENT PROMPT, IS STILL OWED.** Stage 3 established
that two checks on different prompts beat one thorough check, and that the
disagreement between them is the value. One check is not the step.

**STAGE 6 HAS FOURTEEN EDITS APPLIED, CE1 TO CE14, AND THE CURRENT PROOF IS
ROUND 9.** Rounds 3 to 8 are superseded and must not be reviewed.

  `Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit_round9.docx`
  `Drafts/Ch01_The_Category_Error/08_Stage6_Copy_Edit/AIOM_Ch1_CopyEdit_round9.manifest.json`

  CE1        Category error key term rewritten in plain syntax
  CE2        "a round" cut from the craft section
  CE3        Meter relocation defined twice and differently; key term now verbatim
  CE4        number style mixed inside one sentence
  CE5, CE6   pronoun-antecedent faults
  CE7 to CE9 RAISED AND UNRULED, listed in the checklist
  CE10       the stacked-interrupter sentence the style guide itself cites
  CE11, CE12 two further interrupters, per style guide Part 5
  CE13       antithesis budget, and a genuine repetition it surfaced
  CE14       "the reader" removed from the teaching body

**CE3 IS THE FINDING WORTH CARRYING TO EVERY CHAPTER, AND IT IS NOW MECHANICAL.**
"Meter relocation" was defined twice, once as a body callout and once as a key
term, and the two did not match. The other three terms appearing in both places
were character for character identical, which is what showed this to be an
oversight. Gate 6 counts entries and header bands and read 8 and 8 throughout, and
it was a live G3 risk because `continuity.py` treats a verbatim restatement as not
a redefinition. **The check now runs in `voicecheck.py` as part of the house-style
block**, and its negative test reproduces CE3 exactly.

**CE13 IS THE ONE TO LEARN FROM, BECAUSE THE COUNT WAS NOT THE FINDING.** The
antithesis budget reported 4 against 3. Reading them showed two making the SAME
move one paragraph apart in 1.4: "not because no one is paying attention" and
"What is missing is not attention". A repetition a reader feels. The budget
surfaced it; the reading found it. The C6 guard that the cut clause was carrying
was verified present twice elsewhere in the same section BEFORE cutting.

**A REGISTER NOTE QUOTED THE SENTENCE CE11 CHANGED, AND WAS UPDATED IN THE SAME
COMMIT.** Sixth instance in this chapter of a record outliving the prose, and the
FIRST caught at the moment of the edit rather than three steps later. Before
editing any sentence, grep the register for it. That note is where SF8 to SF10
were found, precisely because it quotes the sentence.

**TWO EDITS ARE APPLIED, CE1 AND CE2, AND EACH ONE STALED THE OUTSTANDING PROOF.
THAT IS NOW A RULE RATHER THAN AN OBSERVATION: the re-export is part of applying
an edit, not a later step.** CE1 shortened the live text by 3 characters and
staled 64 spans; CE2 shortened it by 8 and staled 74.

**CE2, "a round" cut from the craft section.** Dan read "a round five thousand
agents" as a typo for "around". It was not one, and the answer went the opposite
way from the report: "a round" was correct, and "around" would have been WRONG,
because the paragraph performs exact arithmetic on the figure. That arithmetic was
verified rather than assumed and every quantity follows from 5,000 exactly. The
finding was the misreading rather than the grammar, since a reader who resolves
the phrase as "around" takes an approximate five thousand where the passage means
an exact one. "Stipulate" already carried the work, so the two words were cut.

**A FULL MECHANICAL SPELLING AND GRAMMAR PASS RAN WITH IT, AND ITS LIMIT IS THE
PART WORTH CARRYING.** `aspell` en_US over 7,181 words with the source register
excluded: zero spelling errors, and the doubled-word, article, split-word and
homophone checks all clean. It would NOT have caught "a round" had that been
wrong, because the phrase is two correctly spelled words in a grammatical
construction. The reader caught what the tooling could not, and the tooling then
proved the reader wrong. Neither was sufficient alone, which is the same shape as
gate 12 and DR7. Three recorded false positives, so they are not re-raised: "COST
COST USAGE USAGE" is Figure 1.2's two panels each carrying both axis labels,
`README` is the register's own key, and "a usage-based charge" is correct.

**CE1, the Category error key-term entry, rewritten in plain syntax.** Dan's
finding, ruled and applied. Two sentences at mean 25.5 words became four at mean
12.5, in genus and differentia form, with the semicolon splice gone. Meaning
unchanged and the same five propositions survive, which is what holds it in the
copy-edit row of the scoped re-run matrix, re-running G2 alone. Verified in a
fresh container rather than trusted from the commit message: fourteen gates pass,
25 pages held, `voicecheck.py` mechanically clean, Key terms improves from mean
18.2 to 15.9 words and from 14 to 19 percent short sentences.

**THE STANDING ROUND-TRIP CONTROL IS NECESSARY AND NOT SUFFICIENT. THIS IS THE
TRANSFERABLE FINDING OF THE SESSION AND IT BINDS EVERY LATER CHAPTER.** CLAUDE.md
requires the unedited export to round-trip at zero reported changes before either
Stage 6 tool is trusted. Round 3 PASSED that control at 221 blocks, zero edited,
zero applied, zero refused, while 64 of its spans were stale, because
`copyedit_import.py` compares the return against the manifest's own recorded text
and never against the live file. A manifest that has drifted from the chapter
still round-trips clean. The check that sees it compares each recorded span
against the current live text:

  round 3   spans correct 144/221   stale by exactly -3   64   other 12
  round 4   spans correct 209/221   stale                  0   other 12

The twelve are by design and identical in both rounds: six body paragraphs whose
span encloses a nested `<cite>`, and their six footnote blocks whose citation-key
marker the export excludes under Decision 51. Expect twelve; fail on a thirteenth.
Adding this to the Stage 6 procedure for Chapters 2 to 15 is NOT YET RULED.

The stale span was established as a usability problem and not a corruption risk by
READING the apply path, not by assuming. `copyedit_import.py` locates each edit
inside `frag = src[s0:e0]`, a real slice of the current file, so a located match
carries a true absolute offset even when the window is shifted, and it writes only
under `if a.apply and not problems and not refused`, so one refusal blocks the
whole write.

Superseded, from the second 2026-08-10 session:

221 blocks, exported from the live text against a fresh fourteen-gate render.
The `.manifest.json` beside it is what `copyedit_import.py` maps the return
through, so keep the pair together. Nothing in the folder before it is current:
round 2 was committed 2026-08-08 and twenty-one commits have touched the live
text since, so reviewing it would mean reviewing the text the Stage 2 re-run,
the Stage 3 restorations and the Stage 4 craft fixes all replaced. The unedited
export was round-tripped before the proof was handed over and reported 221
paragraphs against 221 blocks with zero edited, zero applied and zero refused,
which is the control CLAUDE.md requires before either Stage 6 tool is trusted on
a chapter. The live text hash was captured before and after to prove the dry run
mutated nothing.

The production render it was cropped from is `build/Ch1.pdf`, which is
gitignored and dies with the container. Rebuild it from the block in CLAUDE.md
section 5 if it is wanted again.

**G2 found PG1, now Decision 59: the book sets `lang="en-US"`, never `lang="en"`.**
In Pyphen, which WeasyPrint hyphenates through, `en` is an ALIAS FOR en_GB, so a
Chicago-styled American book was breaking on British points ("organiz-ation" for
"or-ga-ni-za-tion"). Five of 88 line-end breaks sat at points en_US would not
choose. THERE IS NO CSS LEVER: it is a per-document attribute, so EVERY NEW
CHAPTER MUST CARRY IT, and one that omits it hyphenates British silently with no
gate reporting it. After the fix: 25 pages held, zero non-American breaks, zero
proper nouns broken, and line-end breaks rise 88 to 95, which is a gain because
more legal points mean better spacing in a justified measure.

**A FALSE SCOPE CLAIM WAS WRITTEN INTO THE STAGE 5 RECORD, BY CLAUDE, AND IS
CORRECTED IN PLACE.** It said ten pages were rasterized and read. Nine were. Page
1 was never rasterized and page 4 was rasterized and never opened, and page 4 is
exactly where PG1 sat until G2's full 25-page read found it. Fifth instance in
this repo of a check claimed in a record that was not performed, and the first
authored here rather than inherited. WRITE A SCOPE CLAIM FROM WHAT WAS DONE, NEVER
FROM WHAT WAS INTENDED. G2's own scope statement is written that way and names
which pages were read on which render.

**Stage 5 found two defects by reading that no gate can see, now Decision 58 and
CSS v7.1.** DR6, "ChatGPT" breaking as ChatG-PT in the narrow column beside a
floated callout; DR7, "GitHub" breaking as Git-Hub ACROSS THE PAGE 11 TO 12 TURN.
A new `.nb` class switches hyphenation off for a proper noun and 34 brand
occurrences are wrapped. After the fix, 88 hyphenated line ends and zero of them
inside a proper noun.

**The method is the transferable part.** DR6 came from a raster and only raised
the question; every hyphenated line end in the chapter was then scanned against
its proper nouns, which found DR7 and proved the list complete at two. Eyeing 25
pages finds the first and misses the second, because a break at a page foot reads
as an ordinary hyphen until the page turns. Rewording was rejected on the gate 12
precedent: a break is a property of the measure, not of the sentence.

**A CSS change re-runs Stage 5 and G2 for every chapter,** and this Stage 5 pass
IS that re-run, taken against v7.1. It was taken now deliberately, while Chapter 1
was the only chapter in flight and the cost was one chapter rather than five.

**The design spec debt is paid.** It read v6.9 while the CSS shipped v7.0. It now
carries section 16 for v7.0, section 17 for v7.1 and Decision 58, and section 18
for Decision 59, with its header at v7.1.

**FIVE STALE MIRRORS WERE FOUND AND FIXED ON ONE DAY, FOUR OF THEM IN THE
WORKPLAN.** Its tracker row still said "Stage 6 next, 8 of 13, 20-page render";
its snapshot said the same; its lifecycle paragraph said 6 of 13; its queue named
a finished step. CLAUDE.md's counts were the fifth. Each was true when written and
false within two days. CLAUDE.md and this file are mirrors too. `status_check.py`
is the only source, and the standing item to have it verify the mirrors
mechanically is now the most valuable unbuilt piece of process tooling in the
repo.

**Stage 4 closed with its second-model gut-check still open**, on Dan's ruling and
the precedent of Stage 2 and the archived Stage 4. Six findings, one per criterion:
NC1, NC2, NC3 and NC5 applied, NC4 and NC6 recorded with no edit. Read the "WHAT
THIS TICK MEANS" paragraph under Stage 4 in the checklist before treating it as
more. A finding from the verification prompt enters as NC7 and reopens the step.

**NO CRAFT BASELINE BAND IS IN FORCE, and that is deliberate.** The band recorded
2026-08-06 measures a chapter the copy edit replaced: 17.4 mean and 10.1 stdev
against a current 14.5 and 6.3, with the long tail gone entirely. The standard
makes Chapter 1 the band later chapters are read against, so the stale numbers
would have graded Chapter 2 against a text that no longer exists. Dan ruled the
reset deferred to Stage 9, taken from the locked text. Booked as a Stage 9 pending
action, and the archived block is annotated in place.

**Pagination is coupled tightly enough that a craft edit is not a local change.**
NC5 was a one-sentence reorder inside 1.2. It failed the build twice: once by
splitting "Figure 1.2" across a page turn, and both times by adding a line that
pushed footnotes 5 and 6 off their calling pages ELEVEN PAGES LATER. Build after
any craft edit, and attribute a new gate failure by rebuilding the committed state
rather than assuming the edit caused it, which is how that one was pinned.

**Stage 3 was cleared 2026-08-10 on Dan's executive ruling** that the 2026-08-06
external checks carry it, rather than by running a fresh pair. Read the "WHAT
THIS TICK MEANS" paragraph under Stage 3 in the checklist before treating the
tick as more than it is. A finding from any later external check enters as SF11
and reopens the step.

The packet built for the checks that were passed is still filed in
`04_Stage3_Source_Fact_Check_1/` and is current against the live text:

  AIOM_Ch1_Stage3_FactCheck_Input_v3.pdf   the current render, 25 pages, built
                                           from the live text, fourteen gates
                                           green. The v1 and v2 renders are kept
                                           because a finding is only meaningful
                                           against the text that produced it,
                                           and v2 earned its keep this session.
  AIOM_Ch1_Stage3_Claim_Inventory.md       every cited passage paired with the
                                           register entry behind each key, each
                                           note verbatim.

### What the 2026-08-12 stage-7 container did, AFTER the reconciliation

A second session was still running on `claude/stage-7-explanation-sdsb38` while the
reconciliation below happened, and could not see it. Its Stage 7 and G2 work is
already in `main`; what follows is only what it did after merging `main` in.

1. **Ran G2 to completion on the pre-reconciliation text.** Fourteen gates, figure
   geometry by pixel sampling, and all twenty-five pages read at 150 dpi. It found
   PG2, straight quotation marks in every generated footnote, and then PG2a, a
   doubled comma its own fix introduced through `_join` keying on the ASCII quote.
   Both are fixed in `cite_format.py` and both are in `main`.
2. **Cut CLAUDE.md section 10 from 323 lines to 194**, to durable rules only, and
   graduated six duplicated standing reminders out of this file into it. Every
   retained item was checked to still resolve, and two existed nowhere else: Gap
   G-II and the `AIOM_Source_Ledger.md` pointer.
3. **Told to "merge main up", found `main` eighteen ahead instead.** See the
   repository state above.
4. **Corrected the gate 15 claim, reopened G2, and fixed `gen_checklists.py`.** See
   the chapter status above. This is the one commit `main` does not yet have.

**THE CONNECTING THREAD IS THAT GATE 15 EXISTS BECAUSE OF PG2, AND NEITHER SESSION
KNEW ABOUT THE OTHER.** This container found straight quotes by reading pages; the
reconciliation recovered a typographic-marks gate stranded since 2026-08-05. Two
sessions solved the same defect the same day by different routes, one by hand and
one by tooling. That is the cost of concurrency stated precisely: not wrong work,
duplicated work.

### What the 2026-08-12 reconciliation session did

**Almost none of it was drafting, and that was the point.** Dan ruled mid-session
that keeping the repository coherent is Claude's job, not his, after spending his
time managing files instead of writing. The rules that came out of it are
CLAUDE.md section 9.

**Reconciled four sessions into one history.** `main` was six commits AHEAD with
one of its own outstanding, the first time it was not a strict ancestor. Two
sessions had edited the same chapter, colliding on finding labels (two CE2s) and
artifact names (two round 6 files). Resolved by real merges on Dan's ruling that
`stage-7-explanation` was the base, with nothing discarded from either side. Both
content conflicts turned out to be two correct fixes to one sentence.

**Cleaned git from sixteen branches to three**, and built `git_hygiene.py` so it
does not happen again. The audit corrected its own premise: the hand-rolled sweep
reported nine branches and 149 stranded commits, which was a SHALLOW CLONE
ARTIFACT. The true figure was three branches and 24 commits, with thirteen
branches already fully merged.

**Recovered a week of stranded standards work**, which turned out to be the most
valuable thing found all day: the prose style guide, gate 15, and five
house-style checks, all written 2026-08-05 and never merged.

**Stage 6, eleven edits applied: CE3 to CE6, CE10 to CE14.** Three came from the
recovered style guide's Part 5, one of them the sentence the guide itself cites
as its example and which had survived every step since being named.

**Four checks in this repo were found to be wrong or newly built this day**, and
that is the running theme. Gate 15 closed the punctuation gap. Five house-style
checks were ported, each with a negative test. And TWO CHECKS WRITTEN IN THIS
SESSION WERE THEMSELVES DEFECTIVE and were caught before their numbers were
believed: a span check that reported a freshly written manifest as 6 of 221, and
a Part 5 proxy whose three "violations" were all fronted adverbials rather than
subject-verb splits. Both were reported as wrong rather than quietly re-run.

### What the 2026-08-11 session did

Archived Stage 7 external check 1, applied four of its findings, and re-ran G2,
which failed, was fixed, and passed. Four commits. Advanced no step to passed
except G2, which is where it started.

**TWO OF THE THREE DEFECTS FOUND THIS SESSION WERE IN SHARED PRODUCTION TOOLING,
NOT IN CHAPTER 1, so all fifteen chapters have them fixed before the second is
drafted.** That is the argument for finding them on the exemplar.

**PG2, straight quotation marks in every generated footnote.** All six footnotes
set their source titles in ASCII quotes while body prose used typographic ones, and
both were visible within nine pages of each other: the objection at the head of 1.3
on page 8 read with a proper pair, footnote 1 on page 2 with typewriter marks. In a
Chicago-styled book at university-press standard that is a production defect.
Counted in the rendered text, not inferred from source: 22 straight quotes against
exactly one typographic pair. `cite_format.py:105` now emits curly marks. No gate
sees this; gate 2 tests em and en dashes only.

**PG2a, WHICH THE FIX INTRODUCED AND THE RE-READ CAUGHT. THIS IS THE FINDING OF
THE SESSION.** Applying PG2 doubled the comma in every footnote: `“Clarifying Our
Pricing,”,`. Chicago puts the comma inside the closing mark, so `_join` suppressed
the separator by testing `endswith((',"', ",", "."))`, keyed on the ASCII quote; a
title ending `,”` matched nothing and took a second comma. Both forms are now
tested and the docstring says why.

**All fourteen gates passed the doubled comma twice**, on the build that introduced
it and the build that removed it, because nothing mechanical in this repo reads
punctuation. It was visible on page 2 the moment the page was opened. A one-line
change to shared tooling is exactly the kind that feels too small to re-verify, and
it silently broke a second thing inside the same six footnotes it was correcting.

**THE PAGE READ WAS STOPPED MID-WAY ON THE FAILING RUN, DELIBERATELY, AND THAT
REASONING IS WHY PG2a WAS CAUGHT.** Curly quotes are not the width of straight
ones, so the remedy reflows the footnote blocks and can move the pages carrying
them: a read taken before the fix is invalidated by the fix. Eleven pages were read
and recorded as eleven, then superseded. The final read is all twenty-five pages on
the final render, with the rasters deleted and regenerated between runs so no stale
page could be read.

**FC2 IS A DRAFTING ATTRACTOR, NOT A CLOSED INCIDENT.** It is the same defect as
SF8, made a second time about a second vendor: the copy edit reaches for "the
vendor began charging" because it is shorter than "began enforcing allowances and
offered a paid overage". Both sources are scheduled for reuse in Chapters 4 and 11.

**THE RULED-SENTENCE SWEEP SHOULD BECOME A GATE, AND IT HAS NOW FAILED ONCE BY
BEING RUN BY HAND.** Every ruled sentence quoted in the register was compared
against body prose with the register block excluded so the notes cannot self-match.
Four exist; three were present and only SF3 was absent, so the 2026-08-10 repair
caught SF8, SF9 and SF10 and missed exactly one. About fifteen lines, and it
generalizes to all fifteen chapters. Its limit, stated so it is not overtrusted: it
sees only claims that were once ruled with a quoted sentence. FC3, FC4 and FC5 are
prose drifting broader than a register note on claims never ruled, and nothing
mechanical will find those.

### What the SECOND 2026-08-10 session did

Advanced no step, and that is correct: every step Claude owns before lock was
already done, so the work was preparing Dan's next step and clearing repo debt.
Four commits.

1. **The Stage 6 proof, round 3**, described under the chapter status above.
2. **`python-docx` pinned in `requirements.txt`.** `copyedit_export.py` and
   `copyedit_import.py` both import it and it had never been pinned, so the
   export died with `ModuleNotFoundError` in a fresh container. Pinned at 1.2.0,
   the version that produced the clean round trip. Note the near-contradiction
   the comment now heads off: CLAUDE.md section 7 says python-docx FAILS on this
   repo's `.docx` files, which is true of the spec files, since those carry the
   extension and are plain markdown. The Stage 6 proof is a real `.docx`.
3. **`aiom_md.py` deleted, on Dan's ruling.** It parsed `AIOM_chNN.md` into
   semantic HTML, which was the pipeline before Decision 50 made the chapter HTML
   the single source of truth, and its docstring still asserted the overturned
   premise. Verified dead across every file type before removal: zero references
   to `aiom_md` or `parse_chapter` anywhere, and the only markdown chapter source
   ever written is already filed as
   `archive/AIOM_ch01_markdown_noncanonical.md`. The companion artifact had been
   archived and the parser had not. It carried the repo's only two other unpinned
   imports, `markdown_it` and `mdit_py_plugins`, which went with it rather than
   being pinned.
4. **CLAUDE.md's `chapters/` paths fixed.** The repository map listed
   `chapters/` as "Chapter HTML sources" and all four build commands in section 5
   invoked `chapters/AIOM_ch01.html`. That directory has never existed, so a
   fresh session following section 5 verbatim got a file-not-found on its first
   render.

**THE PATTERN ACROSS THREE OF THE FOUR IS THE ONE THIS REPO KEEPS FINDING, in a
new place.** The dependency gap, the dead module and the wrong paths all sat in
territory no gate covers. The fourteen gates cover the render path and they were
green throughout; Stage 6 is a Word round trip and CLAUDE.md is prose, and
neither is exercised by anything. Each defect read as fine right up to the moment
someone tried to use it. This is the same shape as the gates that were claimed
but never performed before 2026-08-05, and as the five stale mirrors of the first
2026-08-10 session, and it is the standing argument for the unbuilt
`status_check.py` mirror verification in thread 4.

**Section 5 was rewritten rather than path-corrected, because a corrected path
would not have been enough.** There is no chapter path that works for every tool:
the build must NOT run on the live text, since `base_url` is the HTML's own
directory and building in place loses the design system, and `place.py` MUST run
on the live text, since it rewrites the file it is given. The block now carries
that reason, a `LIVE` variable, the Stage 6 pair, and four hazards that were
previously only in this file or in nobody's notes: create `build/` first or the
render raises `FileNotFoundError`, delete the `.print.html` sibling, omitting
`--out` writes a fourth file beside the input, and `place.py` leaves an
ungitignored `.bak`. The documented block was then run verbatim to prove it
works. The `place.py` symlink requirement is the ONE line in it transcribed from
this file rather than re-verified, because running `place.py` would rewrite a
live text that has passed G2.

### What the FIRST 2026-08-10 session did

Cleared TWO steps, Stage 3 and Stage 4, raising ten findings between them.

**Stage 4, six findings, one per criterion.** NC1, the chapter never named its own
title concept: "category error" appeared once, in the first words of the summary,
and nowhere in the opening case or in 1.1 to 1.5. That breached Consolidated Spec
line 565, wording that is itself the product of ruling S3. Applied, and it is now
the eighth key term. NC2, 1.1 gave a thin cause ("simply because AI arrives in the
same commercial packaging") for what 1.4 explains properly as inheritance; the
clause is cut and the argued account keeps its arrival. NC3, 1.3 opened on "A
buyer may object", which is "one might say" with the noun changed; the ruled 2026-
08-06 form is restored. NC4, 1.1 is the flattest prose in the chapter, ruled a
deliberate choice with no edit because the standard forbids adding a sentence for
cadence and both candidate repairs were worse than the condition. NC5, two
paragraphs closed on a pointer; 1.2 reordered, 1.5 ruled to stand. NC6, the guard
holds, recorded with no edit, both archived watch items unchanged.

**The regression check that opened Stage 4 is worth repeating on every chapter.**
Because SF8 to SF10 had just shown that a ruled form does not survive a copy edit,
the applied craft fixes were checked the same way BEFORE the read began. NC1 to
NC3 and F2 to F3 all survived, and two apparent regressions turned out to be false
alarms from rewording. Reading rather than trusting the string match is what
distinguished them, and a grep alone would have raised two findings that were not
there.

**Stage 3: the packet, and four findings.**

**SF8, SF9, SF10, and the reason the ruling to pass was checked before it was
ticked.** Dan ruled that the two external checks would be passed because the fact
checks had already run on 2026-08-06. Before ticking, the current text was diffed
against `AIOM_Ch1_Stage3_FactCheck_Input_v2.pdf`, the artifact those checks
actually audited. The diff supported the ruling on values: eighteen checkable
atoms, zero added, zero altered, so a fresh pair would have re-verified an
unchanged value surface. It also found that the sentences carrying those values
had all been rewritten by the 2026-08-08 copy edit, and that three had regressed
to forms Stage 3 had specifically ruled out.

  SF8   the SF2 mechanism claim was back: "Once the credit ran out, Cursor billed
        each additional request at API rates", against a register note that says
        in as many words not to restore a mechanism claim without a new passage
  SF9   the depletion claim had lost its scoping to the case team and become a
        general claim about "Heavy users" that the primary contradicts
  SF10  the Altman sentence had acquired a compute mechanism the register records
        the sources as not carrying

Ruled: restore all three from the register wording. Applied, and verified by the
same check that caught them: five banned forms absent, four ruled forms present,
value surface still eighteen atoms with zero added and zero gone.

**THE FINDING THAT GENERALIZES, and it is the real output of this session. A
ruled claim narrowing does not survive a copy edit on its own, and nothing
mechanical sees it go.** Every date and figure stayed intact through all three
regressions, so no gate and no check on values could detect them. They were
recoverable only because each register note quoted the exact ruled SENTENCE,
which made the regression greppable and diffable against the audited render.
With DE2 and SF7 this is the fourth instance of the shape. Two consequences, one
of them still unruled:

1. Quoting the sentence a fix adds is a control, not a convenience. See the
   unruled standing practice below, which this converts from housekeeping into
   the thing that saved the step.
2. A chapter whose fact check predates a copy edit should be diffed against the
   audited artifact before that fact check is credited. Run here by hand; it
   should probably be tooling.

**SF7, ruled by Dan and applied earlier in the same session. DE7 came due and did
not check out.** Stage 2
flagged DE7 forward on the grounds that the temporal relation had gone from vague
to explicit, and an explicit claim is checkable in a way the vague one was not.
It failed on two counts. The prose read "In January 2026, four months before that
change", and read as the month at large the interval to the 2026-06-01 transition
runs to five; it is four only from the 2026-01-28 call, which the sentence did not
name. Worse, the `microsoft-2026-q2` note had recorded since 2026-07-29 that the
chapter "attributes the figure to the January 28, 2026 call". It did not, and the
string appeared zero times in body prose. The date was generalized after item A2
was written, most probably in the copy edit, and the note went on asserting the
stronger form.

Ruled: name the date. The sentence now reads "On January 28, 2026, four months
before that change, ...", so the interval verifies from the sentence itself. The
register note was corrected in the same change, which was required whichever way
the prose was ruled. A2 is left standing and dated because it was accurate when
written; the drift, the restoration, and the reversing condition are appended
beneath it.

SF7 is the same shape as SF8 to SF10 seen from the other side. There the prose
drifted away from a ruled form; here the RECORD outlived the prose it described.
Both were catchable only because something quoted the actual sentence.

**Mechanical checks banked** and recorded on the packet's first page: the
register closes both ways, 11 keys defined and 11 cited, zero orphans and zero
dangling; every cite marker resolves; six footnotes all fall on their calling
page.

### What the 2026-08-09 session did

Ran the Stage 2 re-run end to end. Nine findings raised, nine ruled by Dan one at
a time, seven applied to the chapter. Full record with reasoning and verification
is under Stage 2 in `AIOM_Ch01_Checklist_v6.md`.

  DE1  the resource consumption model is now named in the teaching body, in 1.2,
       instead of first appearing in the summary
  DE2  the bridge from the five questions to the three failures, restored. It was
       D1 EDIT 3, ruled 2026-08-01, silently lost in the re-draft and copy edit
  DE3  duplicate causal sentence cut from the opening case
  DE4  theorem antecedent (iv) glossed, so all four are now in plain English
  DE5  the chapter hands off to Chapter 2 once, in the summary, not twice
  DE6  Decision 33 amended to 6,500 to 7,500 with the measure named
  DE7  the Microsoft paragraph names its own date anchor
  DE8  the four-activity clause cut from the consumption-event paragraph
  DE9  theorem panel untouched, gloss split in two, restating paragraph cut

Chapter 7,102 to 7,034 words, 25 pages throughout, all fourteen gates green at
every step.

**Stage 2 was closed with its second-model gut-check still open**, on Dan's
ruling and on the precedent of the archived pass. The tick means the step ran and
every finding was ruled. It does not mean independent verification happened. The
prompt is in the checklist; a stall it finds enters as DE10 and reopens Stage 2.

### Three outputs of that session that are not chapter edits

1. **Gate 12 had a second silent defect and it is fixed.** It counted in-text
   figure references LINE BY LINE, so a reference that wrapped was invisible.
   Applying DE1 moved a line break and the gate failed a chapter whose prose
   names the figure in the sentence beside it. It also dropped any body-size line
   OPENING with a figure label, counting it as neither caption nor reference.
   References are now counted on the joined page text with captions subtracted
   one for one. A NEGATIVE TEST WAS RUN and the fixed gate still fails when the
   reference is genuinely absent.
2. **Standing rule 4a in CLAUDE.md**, from Dan's ruling at DE9: the registry is
   the third rail, and the book is an interpretation of it. A panel rendering a
   registry object is never paraphrased into plainer words. When a statement
   reads as technical, the remedy is the prose beside it, never the statement.
3. **Decision 33 is computable.** It named a band and no measure, and Chapter 1
   produced four defensible counts, two of which put it on opposite sides of the
   band. The measure is now the whole rendered chapter less the source register
   and SVG labels, and `voicecheck.py` prints it as the first craft metric.

### Open observations carried out of Stage 2

- **Page 16 is short by about 1.7 inches** after DE5 pushed the craft-section
  head group to page 17. Read, not gated: the head group is whole and page 16
  ends on a complete paragraph. Carried to Stage 5 as an observation, not booked
  as a defect. Same shape as DR3a.
- **DE7 was flagged for Stage 3. CLOSED 2026-08-10 as SF7**, and the flag was
  worth writing: the explicit claim it created was checkable, and it failed.
- **A standing practice was proposed and is NOT yet ruled:** when a developmental
  or craft fix is applied, record the SENTENCE it adds, in quotation marks, not
  only the reason. DE2 exists because a ruled fix was silently reverted and
  nothing saw it, and it was recoverable only because D1's archived entry
  happened to quote the sentence. A sentence is greppable; a reason is not.
  **SF7 is a second argument for it, from the other direction:** there the RECORD
  outlived the prose, and the drift was visible only because the note quoted what
  it had ruled. Ruling this in would have caught SF7 at the copy edit instead of
  three steps later.

## What lives in the repo

**Specs and standards.** Consolidated Spec, Addendum, Structure, Exit
Competencies, Maturity Model, Case Bank, Northmoor Dataset design, Workplan v5
(Decision 33 amended 2026-08-09), Validation Matrix, and
`AIOM_Voice_and_Craft_v1.md` at v1.1.

**Build and design.** `AIOM_book.css` **v7.1**, `AIOM_DESIGN_SPEC` **v7.1**,
`AIOM_Design_QA_Spec` (current), `AIOM_build.py` (fourteen gates plus toolchain
preflight, gate 12 fixed 2026-08-09), `place.py`, `cite_format.py` (quote handling
fixed 2026-08-11, PG2 and PG2a), `footnotes.py`, pinned `requirements.txt`. **The design-spec debt is PAID.** It
had been written to v6.9 while the CSS shipped v7.0; on 2026-08-10 it gained
section 16 for v7.0 (widows and orphans, and Decision 57's DR2 extended to
`.dated` and `.summary`), section 17 for v7.1 (Decision 58, `.nb` for proper
nouns), and section 18 for Decision 59 (`lang="en-US"`, which is a per-document
attribute and not a CSS rule).

**Stage 6 round trip.** `copyedit_export.py` and `copyedit_import.py`, plus
`08_Stage6_Copy_Edit/apply_round1.py` as the record of how round 1 was applied
when the importer could not land it. The `.docx` is a proof, never a second live
text (Decision 50). Both tools need `python-docx`, pinned in
`requirements.txt` since 2026-08-10. `aiom_md.py` was DELETED that day; if a
record mentions it, it is gone and Decision 50 is why.

**Process tooling.** `status_check.py`, `gen_checklists.py`, `voicecheck.py`
(Decision 33 measure, plus the five prose style guide Part 8 house-style checks
since 2026-08-12; `--voice-only` suppresses that half for Stage 4 work in
progress), `reopen.py`, `continuity.py` (G3), `AIOM_Continuity_Ledger.md`,
`typographic_quotes.py`, `renumber_stage_folders.py`, and **`git_hygiene.py`,
which is run BEFORE every merge and every session close** (CLAUDE.md section 9).

**The prose standard is TWO files and they divide cleanly.**
`AIOM_Voice_and_Craft_v1.md` governs the six craft criteria C1 to C6;
`AIOM_Prose_Style_Guide_v1.md` governs the reader model, altitude, sentence-level
craft, the drafting protocol and the house style sheet. Read both before
drafting. **Part 5 of the guide is the answer to prose that reads denser than its
ideas**, which is the most common complaint about this book's drafts.

**The QA suite is FIFTEEN gates**, not fourteen. Gate 15, typographic marks, was
added 2026-08-12 and closes the gap where no gate read punctuation.

## Open threads, in priority order

**LIVE THREADS AS OF THE 2026-08-14 SESSION CLOSE, in order: 6 (CHAPTER 2, now
the work, unblocked, and the only thing anyone is waiting on), 8 (the web
edition, LIVE and waiting on Dan for a domain and the author band), 10 (the
Northmoor CSVs, for the Part III build), 5 (process hardening), 3 (design gaps),
7 (Decision 28). Thread 9 closed the day it opened and so did item (e) below.
THE POST-LOCK EDITING PROBLEM IS SOLVED and needs no thread: see the top of
Repository state.**

**NOTHING IN THE WEB EDITION IS OUTSTANDING AS OF THIS CLOSE.** The typeface
question that ran for two days is settled and confirmed on the published page,
and the hole it exposed is now gate W16. **CHAPTER 2 IS THE WORK.** Before
drafting it, read `AIOM_Voice_and_Craft_v1.md` and `AIOM_Prose_Style_Guide_v1.md`
rather than consulting them at Stage 4, which is what CLAUDE.md section 2
requires and what the craft standard binding from Stage 0 means.

**AND CHAPTER 2 HAS NO BAND TO BE READ AGAINST YET.** The craft baseline reset is
a Stage 9 pending action on Chapter 1, deferred by Dan so it comes from the
locked text, and Chapter 1 has been locked since 2026-08-13. It is available to
take whenever he wants it. Until it is taken, a chapter is read against the six
criteria themselves and against no numbers.

**Five small items are booked by the website-edits sessions and none blocks
anything.** They belong to thread 8.

- **(a) The dark-theme `:target` landing tint moves only 4 to 8 levels** and may
  be too subtle. It is shared with the sidenote, the glossary row and the
  sources entry, so changing it changes all four.
- **(b) The term-linking match rules have been exercised against Chapter 1
  only.** Chapter 2 is the first real test of the leading-article rule and the
  trailing-punctuation refusal.
- **(d) `llms-full.txt` is unruled.** The llmstxt.org convention has a companion
  carrying the entire text as one plain file. It publishes the whole book as a
  single scrapeable document, which is a different decision from publishing a
  map of it, and it belongs with the domain ruling rather than ahead of it.
- **(c) A CUSTOM DOMAIN WILL BREAK THE 404 PAGE IN THE OTHER DIRECTION.**
  `--base-path` is derived in CI from the repository name, which is right for a
  Pages project site at `/textbook.aiom/`. The day a domain is ruled and the
  site serves at the root, that prefix must become EMPTY or the 404 page starts
  reaching for `/textbook.aiom/assets/` on a host that has no such path. The
  workflow comment says so at the line that sets it. **Gate W15 catches it**,
  because it serves at whatever prefix the build was given, so this fails loudly
  rather than shipping. Ruled at the same time as the domain, not before.
- **(e) CLOSED THE DAY IT OPENED, 2026-08-14. A gate over the served page's body
  face is now W16.** It was booked as unbuilt and unruled that morning and Dan
  ruled it built that afternoon. See the top of Repository state.

**The unpinned `playwright` was booked here and CLOSED on 2026-08-13**: it is
now `playwright==1.62.0` in `requirements.txt`, and `.github/workflows/web.yml`
no longer runs a bare `pip install playwright` that silently overrode the
toolchain. Pinning the library pins the rendering engine, since
`playwright install chromium` fetches the build matching the installed version.
The browser binary is still a separate fetch, because pip does not carry it.
Everything else below is
closed and kept as record. The numbering is left alone deliberately: these numbers
are cited in commit messages and in the checklist, and renumbering would break
those references for cosmetic tidiness. **THE WEB EDITION IS BUILT THROUGH PHASE
W6 AND MERGED TO `main`. CHAPTER 2 IS NOW THE WORK.**

9. **CLOSED 2026-08-13, same day it was found. The case bank's withdrawn claim is
   fixed and the bank now carries the ruling that governs it.**

   `AIOM_Case_Bank_v1.md`, in CASE 4.6, asserted flatly that GitHub "began billing
   premium requests that had previously carried no separate charge." That is the
   exact sentence SF3 narrowed on 2026-08-06, because the changelog documents the
   change rather than the arrangement preceding it. The case bank is not a
   superseded draft. It is a live working document, and CLAUDE.md schedules that
   source for reuse in Chapters 4 and 11, so the next chapter to draft from it
   would have inherited the unsupported form.

   **THE FIX WAS COPIED FROM THE REGISTER NOTE, NOT COMPOSED.** Act one now reads
   that GitHub "began enforcing monthly premium-request allowances for Copilot and
   letting customers pay for usage beyond them", which was verified to be the
   chapter's own current sentence before it was carried across, rather than
   reconstructed from the note's description of it.

   **THE BANK NOW CARRIES A `Claim ruling:` LINE, AND THAT LINE IS THE REAL FIX.**
   It records what was narrowed, that the two external checks disagreed and the
   narrower reading was ruled controlling, and the REVERSAL CONDITION: no
   restoration of the prior-state contrast without a pre-2025-06-18 GitHub pricing
   or documentation artifact describing the earlier arrangement in its own words.
   The bank had no convention for recording a ruling before this; it has one now,
   and the next entry to take a fact-check finding should use it.

   **WHY IT SURVIVED SEVENTY DAYS: the ruling was written into the Ch1 register
   note and never propagated to the source document.** CLAUDE.md already requires
   writing a ruling back into the register note, and that was done. Nothing
   required propagating it to the case bank, and nothing mechanical reads the case
   bank, so a privacy sweep is what found it. A sweep of the other four withdrawn
   sentences across every live working document came back clean, so this was the
   only instance, but the propagation gap itself is not closed by fixing one entry.

   **THIS IS THE FIFTH INSTANCE OF A SHAPE CLAUDE.md ALREADY CALLS A DRAFTING
   ATTRACTOR.** SF8, SF9 and SF10 were reverted during a copy edit with every date
   and figure intact, FC2 repeated it on a second vendor, and this is the same
   thing surviving in the source document rather than in the prose. It was found
   by a privacy sweep rather than by any check, which is the point: nothing
   mechanical looks at the case bank.

   Fixing it is a case-bank edit, not a chapter edit, so it re-runs nothing.

10. **FOUR OF THE SIX NORTHMOOR CSVs CARRY WORKED RESULTS RATHER THAN RAW
   INPUTS. Booked 2026-08-13 for the Part III build session.**

   `budget_vs_actual.csv` has `variance_pct` and `anomaly`, `routing.csv` has
   `saving_vs_frontier`, `routing_scenarios.csv` has `option_B_cost`, and
   `capstone_netting.csv` is the netting worked line by line. Only
   `raw_events.csv` and `multiprovider_export.csv` are pure inputs.

   This is probably deliberate design rather than leakage, since the Ch13
   diagnostic packet and the Ch15 CFO briefing are supposed to show figures, and
   these files were left in place on that reasoning when the answer keys were
   purged. **NOBODY HAS ACTUALLY RULED WHICH ARE STUDENT INPUTS AND WHICH ARE
   WORKED EXHIBITS**, and deleting the wrong ones would break Part III. That
   ruling belongs to whoever builds the Part III problem sets, and it now has to
   be made without the generator, which is no longer in the repository.

8. **BUILT THROUGH W6 AND ON `main`, 2026-08-13. Waiting on Dan for three
   things, none of which Claude can supply.** The web edition, opened the same
   day.

   **LIVE AS OF 2026-08-13 at `https://danielwipert.github.io/textbook.aiom/`.**
   The repository is public, Pages is on with the source set to GitHub Actions,
   and run 5 of the `web` workflow deployed the rewritten `main` with both jobs
   green. **GATE W6 GENUINELY RAN IN CI**, printing its twenty-width sweep with
   its negative control firing, which is the one thing worth checking on a CI
   run here. The published artifact is `ch01/`, the landing page, glossary,
   search, sources, objects, sitemap, robots, 404 and the six self-hosted fonts:
   one chapter, because W2 refuses everything not at Stage 9.

   **DAN CONFIRMED THE SITE RENDERS, 2026-08-13.** That confirmation is the only
   evidence of it, and it should stay that way in the record rather than being
   upgraded later into something Claude checked.

   **CLAUDE HAS NEVER LOADED THE LIVE SITE AND CANNOT.** The container's egress
   proxy blocks `github.io`, for `curl` and `WebFetch` alike. Every other
   statement here about the deployment comes from the workflow logs and the
   deploy API rather than from a page anyone fetched, and a later session will
   hit the same wall: **a claim about how the site LOOKS can only come from Dan.**
   The gates are what Claude can speak to, and they cover the artifact, not its
   appearance in a browser.

   **WHAT DAN OWES, in the order it blocks things:**
   - **THE DOMAIN.** `--base-url` writes the CNAME and makes the sitemap
     absolute. Unset today, so no hostname is invented and the sitemap emits
     site-relative paths that become absolute the moment one is supplied. The
     site is live without it on the github.io address.
   - **DONE 2026-08-13: the README.** Written after Dan ruled the three questions
     it turned on: no argument restated (only a link, since nothing gates a
     README and a paraphrase of the book's claim would sit unchecked on a public
     surface), name and affiliation only, and the one-locked-chapter state stated
     as a property of gate W2 rather than as an apology.
   - **The author band: real biography and a portrait.** It currently carries a
     name, an organization and the method, because that is all this repository
     states and nothing about the author was invented. The monogram is a
     typographic placeholder standing in for a photograph. NOTE it is also one of
     only two bands left deliberately unmarked in the accent pass, the hero being
     the other, because each already carries its own object.

   **TWO FINDINGS DAN SHOULD SEE:**
   - **The print palette fails WCAG AA.** Five foreground tokens fall below the
     4.5:1 floor against paper and its tints, `--folio` worst at 2.38:1. Print has
     no WCAG floor, so `AIOM_book.css` IS UNTOUCHED and those remain the values of
     record; `AIOM_web.css` carries text derivatives darkened by the minimum
     needed. The numbers are in `AIOM_web.css` section 2 and plan section 14.
   - **The stale fork is GONE, closed 2026-08-13.** `DRAFT-AIOM_ch01.html` was
     purged from all history in the pre-public rewrite, along with the two
     superseded markdown drafts beside it, so `00_Stage0_Draft/` now holds
     exactly one file. The `LIVE_EXCLUDE` guard in `web_build.py` STAYS and its
     comment was corrected to say why: the hazard is structural, and the next
     chapter can reintroduce it.

   The original opening record follows. Dan asked for the book to exist
   as a website, with `messyjobs.ai` as the inspiration. Plan in
   `AIOM_Web_Edition_Plan_v1.0.md`, rulings as Decisions 60 to 64 in the Workplan,
   durable rules mirrored into CLAUDE.md section 10.

   **What the uploaded `Web Version/` folder turned out to be, because this is the
   finding that shaped everything after it.** Four files. Two were byte-identical
   to files already in the repo. The third, `aiom_md.py`, was deleted on
   2026-08-10 on Dan's ruling. The fourth, `AIOM_ch01.md`, is byte-identical to
   `archive/AIOM_ch01_markdown_noncanonical.md` and is a PRE-FACT-CHECK draft
   carrying the SF2 continuation mechanism, the FC9 absorbed-cost inference, and
   the forbidden word "introduced". Building a public site from it would have
   shipped claims Dan ruled out, with every date and figure intact so nothing
   mechanical would have seen it. The archive README now names all three.

   **Phase W0 (decisions) CLOSED. Phase W1 (pipeline and gates) BUILT AND GREEN.**
   `web_build.py`, `AIOM_web.css`, `web_templates/`, `web_gates_selftest.py`.
   Chapter 1 reports 43,204 characters of prose identical to print and six
   footnotes identical. Build it with:

       python3 web_build.py Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html

   **RUN `web_gates_selftest.py` AFTER ANY CHANGE TO `web_build.py`.** On its first
   run five of twenty-five negative controls did not fire, four of them because
   gate W3's fault was injected into `<title>`, which the extractor skips. The gate
   had been reporting green on faults it had never seen. It also surfaced a real
   defect: the web note extractor had been written as a non-greedy regex twenty
   lines after the print scanner was written to avoid exactly that.

   **Phase W2, the reader design, is BUILT AND GREEN.** Slot rail with reading
   metadata, sidenotes in the margin, tightened apparatus, keyboard layer, motion.
   Gate W6 was added in W2: a twenty-width overflow sweep, the web analogue of
   print gate 1. It is the ONLY optional gate, because it needs a headless
   browser, and it reports SKIPPED plus "W6 NOT RUN" on the verdict line rather
   than passing quietly. It found the P3 inventory table forcing the whole
   document to scroll sideways below 390px. Twenty-nine negative controls now.

   **A RESPONSIVE BREAKPOINT HERE IS ARITHMETIC.** A margin note needs
   `--note + --note-gap` of side track and the side track is
   `(viewport - --rail - --measure) / 2`, so notes fit only from 1411px up. It had
   been set by eye at 1240px, leaving a 170px band where notes ran off the window.
   Redo the sum if any of those four tokens changes.

   **Phase W3, the front door, is BUILT AND GREEN.** Landing page, whole-book
   navigation rail, `book_structure.py`, and gate W7. SEVEN gates now, and
   thirty-four negative controls.

   **THREE RULES CAME OUT OF W3 AND THEY BIND LATER PHASES.** (1) Gate W7 guards
   the joint where the book could split in two: a chapter's title comes from its
   locked HTML, the navigation's comes from `AIOM_Structure_v1.md`, and nothing
   else would notice them disagreeing. (2) A gate handed one page is evidence
   about one page: W3 and W5 had only ever seen the chapter, so the landing page
   was ungated and shipped four straight apostrophes. `gate_pages()` now covers
   every emitted page, and a new page must be added there. (3) Planning prose is
   not publishable prose: only the FIRST SENTENCE of a part's Purpose line is
   published, and no chapter's "Big idea" line is published at all.

   **Decision W-F, ruled 2026-08-13: the web keeps IBM Plex Sans.** Dan supplied
   screenshots of `messyjobs.ai` and its structure was adopted, its typography and
   palette were not.

   **THE LANDING PAGE COPY IS DRAFT AND NEEDS DAN'S RULING.** Hero, lede and
   editions section are written from ruled material but are not themselves ruled.
   Part descriptions are one-sentence placeholders.

   **Phase W4, the reference layer and search, is BUILT AND GREEN.** Glossary,
   per-chapter sources, object index, promises between chapters, client-side
   search. `ledger.py` reads the continuity ledger as data. EIGHT gates, and
   thirty-eight negative controls.

   **GATE W8 GUARDS THE REFERENCE LAYER AGAINST THE CHAPTER.** W8a requires the
   ledger's definition of a term to be character-identical to the chapter's
   key-term text. A definition is exactly the text that can be reworded with no
   date or figure changing, which is the shape that reverted four times on
   Chapter 1.

   **THREE THINGS TO CARRY.** (1) `find_spans(doc, opener, tag)` is the balanced
   scanner and it takes a tag; a non-greedy regex over nested elements has now
   been the defect three times in `web_build.py`. (2) The reference layer is
   generated from records already enforced elsewhere, never scraped from the
   rendered chapter. (3) The sources page is where URLs live, built with
   `url_policy="full"`; the chapter page matches print so gate W1 stays exact.

   **THE LANDING PAGE WAS REBUILT 2026-08-13 after an editorial review.** Dan
   asked for a publisher-grade critique and the verdict was that the front door
   was inert: no author, no images, one value repeated four times, incompleteness
   advertised twice, and the book's three best assets (the figures, the formal
   spine, the sourcing discipline) invisible until a reader was already reading.
   All seven items were taken. The page now runs argument, proof, evidence,
   author, contents, conversion, with a LIVE draggable model in the hero and one
   inverted navy band carrying the theorem verbatim.

   **TWO NEW GATES, AND W9b IS THE IMPORTANT ONE.** W9a requires the theorem and
   the specimen paragraph on the landing page to be verbatim from the chapter.
   W9b forbids the register's `note` field from appearing on ANY published page:
   those notes carry fact-check finding IDs and verbatim quotations of sentences
   the book CUT, so a first draft of the specimen band came within one build of
   publishing retracted claims on the most public surface in the project. Gate W3
   caught it only through stray apostrophes, which is luck. Nine gates now,
   forty-four negative controls.

   **Phase W5, the site build and deploy, is BUILT.** `web_build.py --site`
   discovers every locked chapter and builds the whole site, plus sitemap,
   robots.txt, 404 and CNAME. `.github/workflows/web.yml` builds, gates, runs the
   self-test and publishes to GitHub Pages from `main`. TEN gates, forty-nine
   negative controls.

   **A STALE FORK IS STILL SITTING IN CHAPTER 1'S LIVE-TEXT FOLDER.**
   `Drafts/Ch01_The_Category_Error/00_Stage0_Draft/DRAFT-AIOM_ch01.html` carries
   `lang="en"` and no source register. It is the Decision 50 hazard exactly.
   Discovery excludes it by name and prints that it did so on every build, but an
   exclusion rule is a guard and not a fix. **Deleting it is Dan's call and it
   should be made.**

   **CI INSTALLS A HEADLESS BROWSER ON PURPOSE**, so gate W6 actually runs. A CI
   job running `--no-browser` would be a green tick on a suite with a known hole.

   **HOST AND ANALYTICS ARE RULED, 2026-08-13: Decisions 65 and 66.** GitHub
   Pages, published from `main`. No analytics, and gate W11 now enforces it:
   every subresource must be same-origin, so no analytics script, no CDN
   stylesheet and no remote image can be added without failing the build.
   Outbound anchor links stay legal, because the sources page exists to link out.

   **Phase W6, dark mode and the figure token pass, is BUILT AND GREEN.**
   THIRTEEN gates, sixty-one negative controls. `AIOM_web.css` v0.3. The suite
   later reached FOURTEEN gates and 74 controls on the same day, through W14
   (claim preservation) and W4g (no spot mark on a chapter page).

   **THE PRINT PALETTE FAILS WCAG AA AND THE WEB CORRECTS IT.** Five foreground
   tokens fail against paper and its tints, `--folio` worst at 2.38:1. Print has
   no WCAG floor, so `AIOM_book.css` IS UNTOUCHED and the print values remain the
   values of record; `AIOM_web.css` carries web text derivatives darkened by the
   minimum needed. Only `--folio` moves visibly. **This is worth Dan's attention
   as a finding, not just an implementation detail.**

   **CHAPTER FIGURES ARE RETOKENIZED ON THE WAY TO THE WEB**, never in the
   chapter, by `tokenize_svg()`. It adds attributes and no text, so gate W1 is
   unaffected, and the locked chapter is untouched.

   **GATE W13 SPENT ITS FIRST RUN MEASURING NOTHING**, because its regex captured
   `--folio` while every lookup used `folio`. The self-test control caught it, and
   the fixed gate immediately found a real defect: the theorem panel's roman
   numerals were 2.19:1 on the navy band in LIGHT mode. That is the fifth time in
   this sub-project that a control has caught a gate rather than a page.

   **ONE THING IS STILL OUTSTANDING AND IT IS DAN'S: THE DOMAIN.** `--base-url`
   is unset, so no hostname is invented and the sitemap emits site-relative paths
   that become absolute the moment one is supplied. Nothing else blocks a deploy.

   **STILL BLOCKED AND IT IS NOT A CODE PROBLEM: `messyjobs.ai` is refused by the
   container's egress proxy** (`gateway answered 403 to CONNECT`, confirmed against
   the proxy status endpoint; a text-extraction proxy was blocked the same way).
   No part of the plan or the design derives from that site. Closing it needs one
   of: the domain allowlisted in the environment, screenshots from Dan, or a
   sentence on what appealed. Ask again before W2 is called finished.

00. **CLOSED 2026-08-12. The prose style guide is adopted and its checks are
    running.** Three items were recovered from `chapter-1-prose-style-x0bzze`,
    stranded there since 2026-08-05. Dan ruled option B: adopt the guide, retire
    its duplicated Part 6 to a pointer, then port the checks separately.

    - **`AIOM_Prose_Style_Guide_v1.md` is on `main` at v1.6.** Part 6 duplicated
      `AIOM_Voice_and_Craft_v1.md` and is now a pointer to it. **The two files
      divide as stated in CLAUDE.md section 2**: the craft file governs C1 to C6,
      the guide governs everything else about prose. Part 9 was rewritten because
      the original described a repository that never existed.
    - **The typographic check is gate 15 in `AIOM_build.py`**, verified by
      negative test.
    - **The five Part 8 house-style checks are in `voicecheck.py`**, ported one
      at a time because the branch script was 262 lines and this one is 470.
      Each verified by negative test; one reproduces CE3 exactly.
    - **STILL UNRULED, BUT NO LONGER AT RISK: the placed-vocabulary ledger.**
      Preserved at `archive/AIOM_Placed_Vocabulary_Ledger_unadopted.md` before
      its branch was deleted. Filed in `archive/` rather than the root because a
      file at the root reads as adopted and Dan has not ruled it in.
      **IT IS PROBABLY A LIVE REQUIREMENT.** Style guide section 2.4 places
      inherited vocabulary once and never re-explains it, which only works across
      fifteen chapters if something records what has already been placed. This is
      that something, and **Chapter 2 is the first chapter that needs it.** Check
      whether `AIOM_Continuity_Ledger.md` already covers the ground, and whether
      the two should merge, before ruling.

    **THE ADOPTION PAID FOR ITSELF WITHIN THE HOUR.** The guide's Part 5 rule 2
    cites one sentence as its example of stacked interrupters, and that sentence
    was still in the opening case, having survived a developmental edit, a voice
    pass, a design review, a production gate and two copy-edit rounds since it
    was named on 2026-08-05. It is CE10. The ported checks then raised CE13 and
    CE14 with no human read involved.

0. **CLOSED 2026-08-10. Dan ruled it in, and `factcheck_packet.py` is now at the
   repo root.** The packet is judged worth having on every chapter: Stages 3 and 7
   each need one, so fifteen chapters need thirty. The argument was the history.
   The Stage 3 packet was built by a throwaway script in a session scratchpad and
   died with its container, and the Stage 7 packet four hours later rebuilt the
   same work from nothing.

1. **CLOSED 2026-08-12. G2 was re-run and passed at fifteen gates.** Reopened
   because the 2026-08-11 pass was taken against the pre-CE3 text. Full record
   under Gate G2 in the checklist. Three things from it that bind the next G2 on
   any chapter:

   - **Delete and regenerate the rasters before a page read.** A page read taken
     against a stale raster is worse than none, and this chapter has now had two
     runs whose renders differ only in places a reader would not suspect.
   - **A colour check needs a tolerance smaller than the distance between the
     tokens it must separate.** The figure geometry check first reported identical
     hit counts for two different colours, which is impossible, and would have
     passed a figure using the wrong token.
   - **Gaps G-I and G-II still mean callout placement and slot openings must be
     READ whenever pagination moves.** It moved again with the copy edits.

2. **CLOSED 2026-08-13. Chapter 1 is LOCKED.** Stage 6 closed 2026-08-12, Stage 7
   and Stage 8 closed 2026-08-13 on Dan's rulings, G3 passed and Stage 9 locked the
   chapter. Two items were open at lock and remain so, named under the chapter
   status above. The Stage 6 proof round 9 and the Stage 7 packet are kept as
   artifacts of their steps, not as live work.

3. **Gaps G-I and G-II are not closed, and bind any future design work.** Both require a chapter whose
   pagination or callout placement moves to be READ rather than gated, and this
   chapter's pagination moved four times on 2026-08-10. Gate 14 still cannot see a
   stranded head GROUP, and a floated callout can still collide with a block panel
   unseen.

4. **CLOSED 2026-08-13. G3 and Stage 9 are done, and all three booked pending
   actions were discharged.** The craft band is set from the locked text, "category
   error" is logged as a Chapter 1 owned term on Dan's ruling, and "flow" is absent
   from the ledger, which turned out to be structurally impossible rather than
   narrowly avoided: `continuity.py` reads the key-term register, never prose. The
   THM-009 gloss was written by hand, because `--update` writes a placeholder
   deliberately and leaving it would make check 4 compare later chapters against
   nothing.

5. **Remaining process hardening** (Dan approved, still to build):
   - **The ruled-sentence sweep as a gate.** About fifteen lines: compare every
     sentence a register note quotes as ruled against body prose, with the register
     block excluded so the notes cannot self-match. It has already failed once by
     being run by hand, missing SF3 on 2026-08-10 and surfacing it as FC2 a day
     later through an external check. Read the limit in the 2026-08-11 section
     before treating it as complete coverage.
   - **Teach gate 14 about head GROUPS**, closing gap G-II. Highest value: the
     defect it misses has appeared twice on the same page of the same chapter,
     and the second time the gate reported clean.
   - **`status_check.py` should verify CLAUDE.md section 10 and the Workplan
     against the checklist. THIS IS NOW THE HIGHEST-VALUE UNBUILT ITEM HERE.** All
     are hand-mirrored, and 2026-08-10 alone found FIVE stale mirrors: the
     Workplan's tracker row, snapshot, lifecycle paragraph and queue, plus
     CLAUDE.md's counts. Each was true when written and false within two days.
   - Canonical `DECISIONS.md` with a status field. Numbers run to **59** across
     several files, with 47/48 flagged unverified. 58 (`.nb`, proper nouns) and 59
     (`lang="en-US"`) were both added 2026-08-10 and live in the design spec.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout.
   - `copyedit_import.py` still drops untagged continuation paragraphs, so a
     split paragraph loses everything after its first line. Unfixed.
   - `place.py` writes a `.bak` beside the chapter, which puts a second chapter
     HTML in the live-text directory and is not gitignored. Delete it after every
     run until the tool is changed.

6. **Chapter 2 (The Flow). THIS IS THE NEXT WORK, and it is the first chapter
   drafted under the full standard.** Word band 6,500 to 7,500 (Decision 33,
   amended 2026-08-09), counted as the whole rendered chapter less the source
   register and SVG labels; `voicecheck.py` prints the number.

   **WHAT CHAPTER 2 INHERITS THAT CHAPTER 1 NEVER HAD:**

   - **A craft baseline band in force**, set from the locked Chapter 1 and written
     into `AIOM_Voice_and_Craft_v1.md` section 4. Chapter 2 is the first chapter
     read against one. Read the two guards in that block before using it.
   - **A ledger that can fail G3.** Eight owned terms may not be redefined, and
     five forward promises are recorded. Chapter 2 owns "flow" and must define it;
     Chapter 1 deliberately does not.
   - **Both prose standards, dividing cleanly.** `AIOM_Voice_and_Craft_v1.md` for
     C1 to C6, `AIOM_Prose_Style_Guide_v1.md` for everything else, and **Part 5 is
     the answer to prose that reads denser than its ideas.** Read both BEFORE
     drafting, not at Stage 4.
   - **Fifteen gates**, including gate 15 for typographic marks, and a citation
     formatter that emits volume, issue and pages with a hyphenated range.

   **TWO THINGS IT MUST CARRY FROM DAY ONE:** `<html lang="en-US">` (Decision 59;
   there is no CSS lever and no gate reports its absence) and `.nb` on proper nouns
   (Decision 58).

   **THE PROVING QUESTION FOR CHAPTER 2 IS WHETHER THE STANDARD PAYS.** Chapter 1
   was drafted before the craft standard existed and was re-drafted against it,
   which cost a full reopen from Stage 0. Chapter 2 is the first chapter to have
   the standard from Stage 0. If it still needs a Stage 4 rewrite, the standard is
   not doing the work at drafting time and that is worth knowing early.

7. **Decision 28**, Northmoor properties G, H, I. Gates Ch9, Ch12, Ch13 problem
   sets only.

## Standing reminders

**Rules that bite.**

- **CLAUDE CANNOT DELETE A REMOTE BRANCH FROM THIS CONTAINER, AND SECTION 9 RULE
  6 THEREFORE NEEDS DAN.** The egress proxy denies ref DELETION specifically:
  `git push origin --delete` returns `RPC failed; HTTP 403` on
  `git-receive-pack`, and `DELETE /repos/.../git/refs/heads/...` on the REST API
  returns 403, while ordinary pushes to the same remote succeed. The proxy
  README rules 403s as organization policy, to be reported rather than routed
  around. **Do not spend attempts on this.** Report the branch name and let Dan
  run the one-liner. Confirmed twice on 2026-08-13, on two different branches,
  by two different routes: it is the operation that is denied, not the
  credential or the syntax. **THE LOCAL BRANCH CAN STILL BE DELETED**, and
  should be, so `git branch --list` does not disagree with the remote. Nothing
  is outstanding as of the 2026-08-14 session close: Dan deleted
  `claude/chapter-text-font-uv7ywk` when asked and the remote holds `main` alone.
  **Confirmed a third time on 2026-08-14**, where the git delete refspec reported
  "the remote end hung up unexpectedly" and the REST ref delete answered 403
  "Write access to this GitHub API path is not permitted through this proxy". The
  reconnected GitHub MCP server offers `create_branch` and no delete, so that
  route is closed too. **Run `git fetch --prune` after Dan confirms**, or the
  local tracking ref outlives the branch it tracks. This matters because the
  2026-08-12 stranding was made hard to see by thirteen merged and undeleted
  branches, so the cleanup rule is real even though Claude cannot execute it.
  **The working pattern that settled this: Claude finishes, verifies fully
  merged, deletes the local branch, and hands Dan the one-liner.**
- **A LOCAL `main` CAN BE STALE IN A WAY EVERY SECTION 9 CHECK MISSES.** On
  2026-08-13 `git merge --ff-only` refused with 69 and 193 divergent commits
  after `git_hygiene.py`, a fetch, `git log origin/main ^HEAD` and
  `merge-base --is-ancestor` had ALL passed. Nothing was wrong: local `main`
  still pointed at `2090bcf` from 2026-08-06, the dead pre-rewrite history from
  the `git-filter-repo` force-push, and every one of those checks measures
  against `origin/main` rather than the local pointer. Confirm the old tip is
  contained in no remote branch (`git branch -r --contains main`), tag it, then
  `git reset --hard origin/main` before the fast-forward.

- **TO EDIT A LOCKED CHAPTER, USE `amend.py`. Do not reopen it.** A reopen is for
  producing a chapter; an amendment is for changing one that exists.
  `python3 amend.py Ch01 -m "what changed"` runs the mechanical gates, appends
  the record, re-commits, and the chapter never leaves Stage 9. Add
  `--supersede ID "reason"` if the edit deliberately overturns a fact-check
  ruling, which retires it in `AIOM_Claim_Ledger.md` rather than switching W14
  off.
- **THE AMENDMENT MUST TOUCH THE CHECKLIST OR THE SITE SERVES STALE TEXT.**
  `snapshot.py` resolves what publishes as the newest commit whose CHECKLIST
  reported Stage 9. `amend.py` handles this; a hand edit to the chapter HTML
  alone does NOT, and the build will print a WARNING naming that chapter.
- **WHAT PUBLISHES IS THE LAST LOCK, NOT THE WORKING TREE.** Editing Chapter 1
  has no effect on the live site until it re-locks. This is deliberate and Dan
  ruled it silent: no revision banner, no reader-visible state.
  `--from-worktree` previews edits in flight and CI never uses it.
- **CI NEEDS `fetch-depth: 0`.** At the default depth of 1 the walk over
  checklist commits sees nothing, every chapter resolves to never-locked, and the
  build fails. It looks exactly like a speed optimization someone should remove.
- **A DRAWN MARK IS JUDGED AT THE SIZE IT SHIPS AT.** Render the contact sheet at
  2.35rem, not at display size. Three of the nine marks were redrawn on that
  basis and one took three attempts.

- **The build and `place.py` want the chapter in DIFFERENT places, and CLAUDE.md
  section 5 now carries the runnable form.** Do not reconstruct it from memory
  here. In short: `AIOM_build.py` sets `base_url` to the HTML's own directory, so
  building in place under `Drafts/` drops the design system and reports dozens of
  false defects, and the fix is to copy the live text to the repo root, build
  there, and delete the copy and its `.print.html` sibling. `place.py` is the
  opposite case and runs ON the live text path, from the repo root, with
  `AIOM_book.css` and `fonts/` symlinked beside it, because it rewrites the file
  it is given. This bullet graduated into CLAUDE.md on 2026-08-10 per the section
  11 division of labor; it stays here only as the pointer.
- **A green gate suite is not a read page.** With all fourteen gates passing,
  reading found flush paragraphs in the summary and a dated box (2026-08-08),
  confirmed three moved-page cases (2026-08-09), and found straight quotes in every
  footnote and then a doubled comma introduced by their fix (2026-08-11). No gate
  measures paragraph separation inside a block, and none reads punctuation at all.
- **When a check and the prose disagree, fix whichever is actually wrong, and say
  which.** Gate 12 on 2026-08-09 is the cleanest case: rewording the sentence so
  the reference did not wrap would have passed the gate and left every later
  chapter exposed.
- **Read the archived rulings before writing findings.** Two of the nine Stage 2
  findings exist only because that was done: DE2 recovered a ruled fix that had
  been lost, and DE3 was framed as a different finding on rewritten text rather
  than as reopening D3.
- **Read the decision text before proposing an edit that touches it.** DE9 was
  first raised claiming Decision 56 does not constrain the panel's vocabulary. It
  does. Had that gone unchecked, the ruling would have breached it.
- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4.

**Graduated into CLAUDE.md section 10 on 2026-08-11, and deliberately not restated
here.** They were duplicated in both files, and a mirror is the failure this repo
has already paid for repeatedly. Read them there, not from memory:

- a one-line change to shared tooling is not too small to re-verify, because a
  glyph-width change is a reflow
- a check over rendered pages must decide explicitly what it does at a page
  boundary, or it passes the defect it exists to catch
- one live text per chapter, the chapter HTML is it, supersede and delete and never
  fork (Decision 50)
- read the in-chapter Decision 51 register before using a figure from a cited
  study, because it can carry rulings the summary ledger does not
- write every fact-check ruling back into the register note, with the condition
  that would reverse it
- judge a proposed remedy separately from the finding it answers

- **`reopen.py` RESETS BY POSITION IN THE LIFECYCLE, NOT BY THE SCOPED RE-RUN
  MATRIX, AND IT IS UNFIXED.** A reopen at a late step clears every step after it in
  the step order, including ones the matrix would leave intact. On 2026-08-13 two
  citation-lane G2 reopens silently cleared Dan's ruled Stage 6 closure, and the
  loss was invisible until a passed Stage 7 appeared above an open Stage 6. **CHECK
  THE STEPS BELOW A REOPEN POINT AGAINST THE MATRIX BEFORE ACCEPTING THE RESET.**
- **THE PART 5 RULE 1 PROXY IN `voicecheck.py` IS DEFECTIVE. DO NOT QUOTE ITS
  NUMBERS.** It counts fronted adverbial phrases as subject-verb separations, and a
  fronted adverbial is right-branching and permitted, so both its baseline and its
  after-reading measure something the rule does not cover. Unfixed, and the one open
  defect in the ported house-style checks. The sound measure beside it, long
  comma-fenced asides, does work.
- **A COLOUR CHECK NEEDS A TOLERANCE SMALLER THAN THE DISTANCE BETWEEN THE TOKENS
  IT MUST SEPARATE, or an exact match.** The figure geometry check first reported
  identical hit counts for `--amber-fig` and `--amber`, which differ by 12 in red,
  under a tolerance of 14. Two different colours cannot both match every pixel; that
  impossibility is what exposed it, not re-reading the code.
- **DATES IN RECORDS COME FROM THE COMMIT CLOCK, NOT FROM MEMORY.** A session
  crossing midnight UTC wrote several records a day old on 2026-08-13. `reopen.py`
  auto-dated correctly throughout; only hand-typed dates were wrong. This matters
  because the standing control is to re-check every gate tick against the date of
  the last edit that could move it, and that control is worthless if dates drift.

**Tooling facts learned the hard way.**

- **THE DESIGN MIRRORS ITS MARGINS.** Main text starts at x0 68.4 on odd pages,
  57.6 on even. Any new geometry check must derive the edge per page or it will
  read green while measuring nothing.
- The PRINT QA suite is FIFTEEN gates, 1 through 15, and the WEB suite is also
  FIFTEEN, W1 through W15, since W15 (in-page navigation) was added 2026-08-13.
  Both numbers were wrong in this file earlier that day: this line said fourteen
  for print, which went stale when gate 15 was added on 2026-08-12, and the web
  counts ran one high for five phases before that. THE WEB NUMBER HAS NOW GONE
  STALE TWICE FOR TWO DIFFERENT REASONS, once by miscounting sub-letters and
  once by a gate being added, which is why the rule is to derive it. A
  gate is one number, never one check, so sub-lettered checks like `W8a` are
  parts of a gate. Re-derive both from build output rather than copying them
  forward. Three checks written in this repo have been
  wrong in a way that read as green, and gate 12 has now been wrong twice. Every
  one was found by changing the input, never by re-reading the code. Treat a
  green gate on unchanged input as weak evidence.
- A fresh session has neither the Python deps nor poppler. `pip install -r
  requirements.txt`, then `apt-get update -qq && apt-get install -y
  poppler-utils`. The build exits 2 without them. The 403s from unrelated
  third-party PPAs during that apt-get are harmless.
- **NO SOURCE HOST IS REACHABLE FROM THIS ENVIRONMENT.** Verified 2026-08-06
  against six hosts; all fail CONNECT with a gateway 403 recorded as a policy
  denial. Do not offer to check a primary. Do not treat a register note as a
  substitute for one either; say which it is.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN. Report
  policy denials, do not route around them.
- To reopen a chapter use `reopen.py`, never `gen_checklists.py --force`. After a
  reopen, check the box TEXT against the generator, not only the ticks.
- Stage folders are on Process v2 numbering across all eighteen units.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- Rasterize for visual review with `pdftoppm -png -r 150`.
