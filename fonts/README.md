# fonts

The book's two type families, committed so a render needs no network font
staging. `AIOM_build.py --fonts` fetches these from GitHub and Google, but the
Jost source and the Google Fonts CDN are blocked by some proxy policies; keeping
the files here means the build can skip staging and render directly.

## What is here

`use/` holds the six faces the CSS loads by `@font-face`:

| File | Family, weight | PostScript name |
|---|---|---|
| `IBMPlexSans-Text.ttf` | IBM Plex Sans, Text (body) | IBMPlexSans-Text |
| `IBMPlexSans-Medium.ttf` | IBM Plex Sans, Medium | IBMPlexSans-Medm |
| `IBMPlexSans-SemiBold.ttf` | IBM Plex Sans, SemiBold | IBMPlexSans-SmBld |
| `IBMPlexSans-Italic.ttf` | IBM Plex Sans, Italic | IBMPlexSans-Italic |
| `Jost-Medium.ttf` | Jost, Medium (500) | Jost-Medium |
| `Jost-SemiBold.ttf` | Jost, SemiBold (600) | Jost-SemiBold |

The CSS declares the families as `Plex` and `Jost`, so WeasyPrint names the
embedded subsets from the CSS family and weight, not from the PostScript names
above. That is why the QA gate 5 face check passes with these files.

## Licenses

Both families are under the SIL Open Font License 1.1, included here:

- `OFL-IBMPlexSans.txt`: Copyright IBM Corp., Reserved Font Name "Plex". From the
  `ibm-plex-sans` release on GitHub.
- `OFL-Jost.txt`: Copyright The Jost Project Authors. From the Jost distribution.

## Sources

- IBM Plex Sans: the `@ibm/plex-sans` GitHub release, `fonts/complete/ttf/`.
- Jost: the official Jost distribution `static/` weights (Medium and SemiBold).
  The variable font instances to the same weights, but the static files carry
  correct per-weight names, so they are used directly.
