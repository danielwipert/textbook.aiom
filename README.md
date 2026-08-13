# AI Operations Management

The source repository for a founding academic textbook establishing AI
Operations Management as a discipline. Fifteen chapters in four parts, written
to university press standard, and built from this repository into two artifacts:
a print-quality PDF and a website.

The book itself is on the website. This repository is where it is made.

## Read it

**https://danielwipert.github.io/textbook.aiom/**

The site is the reading surface. Nothing here is a substitute for it, and the
argument is not restated in this file.

## What state this is in

**Chapter 1 is locked. The other fourteen are not written yet.**

That is why the site publishes one chapter. Publication is not an editorial
choice made per chapter: a chapter reaches the site only after it passes all
thirteen steps of the lifecycle and is marked Locked, and gate W2 fails the
build for any chapter `status_check.py` does not report at that stage. A chapter
in progress builds to a local preview that carries `noindex` and that CI never
publishes.

`status_check.py` is the only authority on where a chapter stands:

```bash
python3 status_check.py
```

This file deliberately does not carry a chapter count. A number written here
would be a second answer to a question the repository already answers in one
place, and it would be wrong the day Chapter 2 locks.

## Licensing, which is not uniform

**Read `LICENSE` before reusing anything. Two different licenses apply, and
which one you are under depends on the file.**

- **The manuscript and all book content are ALL RIGHTS RESERVED.** The chapter
  text, the drafts, the constructed dataset, the specifications, the stylesheets
  and the site templates. No license is granted. Brief quotation with attribution
  is fine, as ordinary scholarly practice allows. Reproduction, redistribution,
  adaptation, translation and use as training data are not.
- **The build and QA tooling is MIT.** The Python at the repository root and the
  CI configuration. Reuse it freely.
- **The fonts are SIL OFL 1.1.** IBM Plex Sans and Jost, with their license texts
  committed beside them in `fonts/`.

This repository is public so the site can be built and served from it. Public
visibility is not a grant of any right in the text.

## Building

Both artifacts descend from the same locked chapter HTML. That is the point of
the arrangement rather than an implementation detail: a second renderer is a
machine for producing two versions of one chapter that silently disagree, and
gate W1 exists to make text equivalence a checked property rather than an
intention.

```bash
pip install -r requirements.txt
apt-get install -y poppler-utils        # the print gates rasterize pages
```

**The print PDF and its fifteen gates.** The build sets `base_url` to the input
file's own directory, so it must run from the repository root against a copy
rather than in place, or it loses the stylesheet and the fonts:

```bash
LIVE=Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html
mkdir -p build
cp "$LIVE" _ch01_build.html
python3 AIOM_build.py _ch01_build.html --out build/Ch1.pdf
rm -f _ch01_build.html _ch01_build.print.html
```

**The website and its gates, W1 through W14:**

```bash
python3 web_build.py --site --out build/web
python3 web_gates_selftest.py           # negative controls for every web gate
```

The build refuses to start without its toolchain and exits 2 rather than
skipping gates, because a gate that did not run is not a gate that passed. One
gate is optional and says so loudly: W6 needs a headless browser, and it prints
`SKIPPED` and appends `W6 NOT RUN` to the verdict rather than passing quietly.
CI installs a browser so it actually runs there.

`web_gates_selftest.py` is worth explaining, because it is the least obvious
piece of this repository. It injects one fault at a time and asserts that the
gate which owns that fault fails. On its first run, five of its controls did not
fire, and every one of those was a fault in the control rather than in the gate.
Without the controls, a green gate suite would have been evidence of nothing.

Everything runs on every push through `.github/workflows/web.yml`, which
publishes to GitHub Pages from `main`.

## What lives where

`CLAUDE.md` section 4 carries the repository map and is kept current. It is not
duplicated here, for the same reason the chapter count is not.

In short: build and QA tooling at the root, chapter working directories under
`Drafts/`, the constructed dataset under `Northmoor/`, superseded files under
`archive/`, and the specifications, ledgers and standards as the `AIOM_*.md`
files at the root.

## Author

Daniel S. Wipert, Chorus AI Systems.
