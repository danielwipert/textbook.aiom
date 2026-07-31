#!/usr/bin/env python3
"""
sources.py  |  one tool for the book-wide source register

Chapters cite by key. Footnotes and chapter source registers are both generated
from AIOM_sources.json, so a source cited in three chapters cannot appear three
different ways, and an access date cannot disagree with itself.

FOUR COMMANDS

  python3 sources.py check
      Report every source: what is missing, what needs upgrading, what is
      captured. Run this any time.

  python3 sources.py capture
      Capture every perishable source to the Wayback Machine and to the local
      dark archive, then write the archive links and access dates back into
      the register. Needs live network.

  python3 sources.py build AIOM_ch01.html
      Resolve <cite> tags into footnotes, append the chapter source register,
      and write AIOM_ch01.built.html for AIOM_build.py to render.

  python3 sources.py add
      Walk through adding one source, so you never hand-edit the JSON.

CITING IN A CHAPTER

    ... and the flat price had to go.<cite src="truell-2025-pricing">describing
    the change of June 16</cite></p>

  The text inside the tag is an optional gloss appended to the footnote. Leave
  it empty for a bare citation: <cite src="truell-2025-pricing"></cite>
"""

import argparse
import json
import os
import re
import shutil
import sys
import urllib.request
from datetime import date

REGISTER = "AIOM_sources.json"
ARCHIVE_DIR = "sources_archive"
SPN = "https://web.archive.org/save/"
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


# ---------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------

def load():
    with open(REGISTER) as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if not k.startswith("_")}, data


def save(full):
    with open(REGISTER, "w") as f:
        json.dump(full, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------------------
# formatting
# ---------------------------------------------------------------------------

def fmt_date(iso):
    """2025-07-04 -> July 4, 2025.  2025-07 -> July 2025.  2025 -> 2025."""
    if not iso:
        return ""
    parts = iso.split("-")
    if len(parts) == 1:
        return parts[0]
    month = MONTHS[int(parts[1]) - 1]
    if len(parts) == 2:
        return f"{month} {parts[0]}"
    return f"{month} {int(parts[2])}, {parts[0]}"


def names(authors, style):
    """style 'bib' gives Family, Given for the first author. 'note' gives natural order."""
    out = []
    for i, a in enumerate(authors):
        if "org" in a:
            out.append(a["org"])
            continue
        fam, giv = a.get("family", ""), a.get("given", "")
        if style == "bib" and i == 0:
            name = f"{fam}, {giv}".strip().rstrip(",")
        else:
            name = f"{giv} {fam}".strip()
        if a.get("handle"):
            name += f" ({a['handle']})"
        out.append(name)
    if len(out) == 1:
        return out[0]
    if len(out) == 2:
        return f"{out[0]} and {out[1]}"
    return ", ".join(out[:-1]) + ", and " + out[-1]


def note(src, gloss=""):
    """Chicago full note form, for the page footnote. Kept short by design."""
    t, who, ttl = src["type"], names(src["authors"], "note"), src["title"]
    d = fmt_date(src.get("date", ""))
    if t == "article":
        base = (f'{who}, "{ttl}," {src["container"]} {src.get("volume","")}, '
                f'no. {src.get("issue","")} ({src["date"]}): {src.get("pages","")}')
    elif t == "blog":
        base = f'{who}, "{ttl}," {src["container"]} (blog), {d}'
    elif t == "web":
        base = f'{who}, "{ttl}," {src["container"]}, {d}'
    elif t == "social":
        base = f"{who}, {ttl.lower()}, {d}"
    else:
        base = f'{who}, "{ttl}," {d}'
    base = re.sub(r"\s+", " ", base).strip()
    return f"{base}, {gloss.strip()}." if gloss.strip() else base + "."


def bib(src):
    """Chicago bibliography entry for the chapter source register."""
    t, who, ttl = src["type"], names(src["authors"], "bib"), src["title"]
    d = fmt_date(src.get("date", ""))
    if t == "article":
        s = (f'{who}. "{ttl}." <i>{src["container"]}</i> {src.get("volume","")}, '
             f'no. {src.get("issue","")} ({src["date"]}): {src.get("pages","")}.')
    elif t == "blog":
        s = f'{who}. "{ttl}." <i>{src["container"]}</i> (blog), {d}.'
    elif t == "web":
        s = f'{who}. "{ttl}." {src["container"]}, {d}.'
    elif t == "social":
        s = f"{who}. {ttl}, {d}."
    else:
        s = f'{who}. "{ttl}." {d}.'
    if src.get("url"):
        s += f' {src["url"]}.'
    if src.get("wayback"):
        s += f' Archived at {src["wayback"]}.'
    if src.get("accessed"):
        s += f' Accessed {fmt_date(src["accessed"])}.'
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------------------
# check
# ---------------------------------------------------------------------------

def cmd_check(args):
    srcs, _ = load()
    ready = blocked = 0
    print(f"{len(srcs)} sources in the register\n")
    for key in sorted(srcs):
        s = srcs[key]
        problems = []
        if not s.get("url"):
            problems.append("no URL")
        if s.get("upgrade"):
            problems.append("upgrade pending")
        if s.get("perishable"):
            if not s.get("wayback"):
                problems.append("not captured to Wayback")
            if not s.get("local"):
                problems.append("no local copy")
            if not s.get("accessed"):
                problems.append("no access date")
        if problems:
            blocked += 1
            print(f"  BLOCKED  {key}")
            for p in problems:
                print(f"           - {p}")
        else:
            ready += 1
            print(f"  ready    {key}")
    print(f"\n{ready} ready, {blocked} blocked.")
    print("G1 cannot pass for any chapter citing a blocked source."
          if blocked else "All sources meet the archival standard.")
    return 0 if not blocked else 1


# ---------------------------------------------------------------------------
# capture
# ---------------------------------------------------------------------------

def capture_one(url, key):
    """Wayback Save Page Now, then a local copy. Returns (wayback_url, local_file)."""
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    wb = ""
    try:
        req = urllib.request.Request(SPN + url,
                                     headers={"User-Agent": "AIOM-source-capture"})
        with urllib.request.urlopen(req, timeout=120) as r:
            final = r.geturl()
            body = r.read()
        if "/web/" in final:
            wb = final
        local = os.path.join(ARCHIVE_DIR, f"{key}.html")
        with open(local, "wb") as f:
            f.write(body)
        return wb, local
    except Exception as e:
        print(f"    capture failed: {e}")
        return "", ""


def cmd_capture(args):
    srcs, full = load()
    today = date.today().isoformat()
    done = 0
    for key in sorted(srcs):
        s = srcs[key]
        if not s.get("perishable") or not s.get("url"):
            continue
        if s.get("wayback") and not args.force:
            continue
        print(f"  capturing {key} ...")
        wb, local = capture_one(s["url"], key)
        if wb or local:
            full[key]["wayback"] = wb or full[key].get("wayback", "")
            full[key]["local"] = local or full[key].get("local", "")
            full[key]["accessed"] = today
            done += 1
            print(f"    wayback: {wb or 'FAILED'}")
    save(full)
    print(f"\ncaptured {done}. Run 'check' to see what remains.")
    return 0


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------

CITE = re.compile(r'<cite\s+src="([^"]+)"\s*>(.*?)</cite>', re.S)


def cmd_build(args):
    srcs, _ = load()
    html = open(args.html).read()
    used, missing = [], []

    def repl(m):
        keys = [k.strip() for k in m.group(1).split(";") if k.strip()]
        gloss = m.group(2)
        bad = [k for k in keys if k not in srcs]
        if bad:
            missing.extend(bad)
            return m.group(0)
        for k in keys:
            if k not in used:
                used.append(k)
        # several sources in one note are separated by semicolons; the gloss,
        # if any, attaches to the last of them
        parts = [note(srcs[k]).rstrip(".") for k in keys[:-1]]
        parts.append(note(srcs[keys[-1]], gloss).rstrip("."))
        return f'<span class="fn">{"; ".join(parts)}.</span>'

    out = CITE.sub(repl, html)
    if missing:
        print("ERROR: keys not in the register: " + ", ".join(sorted(set(missing))))
        return 1

    if used:
        entries = "\n".join(f"<p>{bib(srcs[k])}</p>" for k in sorted(used))
        block = f'\n<section class="sources">\n<p class="slot-label">Sources</p>\n{entries}\n</section>\n'
        out = out.replace("\n</body>", block + "\n</body>", 1)

    dest = args.html.replace(".html", ".built.html")
    open(dest, "w").write(out)
    print(f"resolved {len(used)} citations -> {dest}")
    blocked = [k for k in used if srcs[k].get("perishable")
               and not srcs[k].get("wayback")]
    if blocked:
        print(f"WARNING: {len(blocked)} cited source(s) not yet captured: "
              + ", ".join(blocked))
        print("This chapter cannot pass G1 until they are.")
    return 0


# ---------------------------------------------------------------------------
# add
# ---------------------------------------------------------------------------

def cmd_add(args):
    srcs, full = load()
    def ask(q, default=""):
        v = input(f"  {q}" + (f" [{default}]" if default else "") + ": ").strip()
        return v or default
    print("Add a source. Blank to skip an optional field.\n")
    key = ask("key, e.g. truell-2025-pricing")
    if not key or key in full:
        print("  need a new unique key")
        return 1
    t = ask("type (article/blog/web/social/report)", "web")
    org = ask("organisation, if the author is one")
    authors = [{"org": org}] if org else []
    while not authors or ask("another author? y/n", "n") == "y":
        fam = ask("  author family name")
        if not fam:
            break
        authors.append({"family": fam, "given": ask("  author given name"),
                        **({"handle": h} if (h := ask("  handle, social only")) else {})})
    entry = {"type": t, "authors": authors, "title": ask("title"),
             "date": ask("date, ISO"), "url": ask("url"),
             "perishable": ask("perishable? y/n", "y") == "y",
             "wayback": "", "local": "", "accessed": "",
             "upgrade": ask("upgrade note, blank if settled") or None}
    for f in ("container", "volume", "issue", "pages", "doi"):
        if (v := ask(f"{f}, optional")):
            entry[f] = v
    full[key] = entry
    save(full)
    print(f"\nadded {key}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    c = sub.add_parser("capture"); c.add_argument("--force", action="store_true")
    b = sub.add_parser("build"); b.add_argument("html")
    sub.add_parser("add")
    a = ap.parse_args()
    sys.exit({"check": cmd_check, "capture": cmd_capture,
              "build": cmd_build, "add": cmd_add}[a.cmd](a))
