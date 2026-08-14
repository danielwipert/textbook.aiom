# fonts

The book's type families, committed so a render needs no network font staging.
`AIOM_build.py --fonts` fetches these from GitHub and Google, but the Jost source
and the Google Fonts CDN are blocked by some proxy policies; keeping the files
here means the build can skip staging and render directly. The web build has no
staging path at all: `web_build.py` globs `use/*.ttf` and copies what it finds
into `assets/fonts/`, so a face must be a TTF and must live here to ship.

## What is here

`use/` holds the faces the two stylesheets load by `@font-face`. **Print and web
do not load the same body family, and that divergence is deliberate.** Print is
locked at CSS v7.1 and a change there re-runs Stage 5 and G2 on every chapter;
the web is free to correct for a backlit screen, which it already does for colour.

| File | Family, weight | Loaded by |
|---|---|---|
| `Archivo-Regular.ttf` | Archivo, Regular (400) | web body |
| `Archivo-Italic.ttf` | Archivo, Italic (400) | web body |
| `Archivo-Medium.ttf` | Archivo, Medium (500) | web body |
| `Archivo-SemiBold.ttf` | Archivo, SemiBold (600) | web body |
| `IBMPlexSans-Text.ttf` | IBM Plex Sans, Text (450) | print body |
| `IBMPlexSans-Regular.ttf` | IBM Plex Sans, Regular (400) | nothing, see below |
| `IBMPlexSans-Medium.ttf` | IBM Plex Sans, Medium (500) | print |
| `IBMPlexSans-SemiBold.ttf` | IBM Plex Sans, SemiBold (600) | print |
| `IBMPlexSans-Italic.ttf` | IBM Plex Sans, Italic (400) | print |
| `Jost-Medium.ttf` | Jost, Medium (500) | print and web display |
| `Jost-SemiBold.ttf` | Jost, SemiBold (600) | print and web display |

`IBMPlexSans-Regular.ttf` was added at web v0.5 to give the web a true Regular
roman, and web v0.6 moved the web to Archivo three days later. Nothing loads it
now. It is kept rather than deleted because the two stylesheets share this
directory and the file costs nothing unloaded, and because deleting a face is the
kind of change that is discovered at the next render rather than at the commit.

Each stylesheet declares its families under its own name, so WeasyPrint names the
embedded subsets from the CSS family and weight rather than from the PostScript
names. That is why the QA gate 5 face check passes with these files, and gate 5
is also what proves the web-only faces are embedded nowhere in the print PDF: it
lists exactly five faces, none of them Archivo.

## Licenses

All three families are under the SIL Open Font License 1.1, included here:

- `OFL-IBMPlexSans.txt`: Copyright IBM Corp., Reserved Font Name "Plex". From the
  `ibm-plex-sans` release on GitHub.
- `OFL-Jost.txt`: Copyright The Jost Project Authors. From the Jost distribution.
- `OFL-Archivo.txt`: Copyright The Archivo Project Authors, Omnibus-Type. Shipped
  with the family.

## Sources

- IBM Plex Sans: the `@ibm/plex-sans` GitHub release, `fonts/complete/ttf/`.
- Jost: the official Jost distribution `static/` weights (Medium and SemiBold).
  The variable font instances to the same weights, but the static files carry
  correct per-weight names, so they are used directly.
- Archivo 2.001: the static instances as distributed on Google Fonts. Font hosts
  are blocked from the build container, so they were taken from the
  `@expo-google-fonts/archivo` npm package, which ships the upstream TTFs and the
  OFL unmodified. All four are one release, which is the standard web v0.5 set:
  mixing releases of a family is how a roman and its own italic stop matching.
