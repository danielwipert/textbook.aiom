#!/usr/bin/env python3
"""One-time migration of the Chapter 1 draft into enriched markdown."""
import re, sys

src = open(sys.argv[1], encoding="utf-8").read()

# > **FIGURE 1.1. Caption.** description...
def fig(m):
    num, cap, desc = m.group(1), m.group(2).strip(), m.group(3).strip()
    return f"::: figure {num}\ncaption: {cap}\nsrc:\n\n{desc}\n:::"
src = re.sub(r"^> \*\*FIGURE ([\d.]+)\. (.+?)\*\* (.+)$", fig, src, flags=re.M)

# > **THM-009. Title.**  /  >  /  > *statement*
def obj(m):
    oid, title, stmt = m.group(1), m.group(2).strip(), m.group(3).strip()
    kind = {"THM": "theorem", "LEM": "lemma", "PROP": "proposition"}[oid.split("-")[0]]
    return f"::: {kind} {oid}\n{title}\n\n{stmt}\n:::"
src = re.sub(r"^> \*\*((?:THM|LEM|PROP)-\d+)\. (.+?)\*\*\n>\n> \*(.+?)\*$",
             obj, src, flags=re.M)

# **P1 (worked). The CIO memo.** body  +  the *Model reply.* paragraph
def prob(m):
    label, note, title, body, reply = m.groups()
    head = f"{title.strip().rstrip(".")}{' (worked)' if note else ''}"
    return (f"::: problem {label}\n{head}\n\n{body.strip()}\n\n"
            f"*Model reply.*{reply.strip()[len('*Model reply.*'):] if False else ''}"
            f"\n{reply.strip()}\n:::")
src = re.sub(
    r"^\*\*(P\d+)( \(worked\))?\. (.+?)\*\* (.+?)\n\n(\*Model reply\.\*.+?)$",
    prob, src, flags=re.M | re.S)

open(sys.argv[2], "w", encoding="utf-8").write(src)
print(f"wrote {sys.argv[2]}")
