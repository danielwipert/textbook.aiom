"""cite_format.py

Turns AIOM source-block entries into footnote text.

Style: Chicago notes-bibliography, note form. Full citation at the foot of the
page carrying the claim, per the ruling recorded in AIOM_book.css section 3.
The back-of-book bibliography remains the aggregated list.

url_policy controls whether the URL appears in the footnote:
    "full"   full URL in the note
    "none"   no URL in the note; it lives in the bibliography only
"""

MONTHS = ("January February March April May June July August September "
          "October November December").split()

PLATFORMS = {"x.com": "X", "twitter.com": "X", "bsky.app": "Bluesky",
             "linkedin.com": "LinkedIn"}


def _date(iso):
    """ISO date to Chicago long form. Year-only input passes through."""
    if not iso:
        return ""
    parts = str(iso).split("-")
    if len(parts) == 1:
        return parts[0]
    y, m = parts[0], int(parts[1])
    if len(parts) == 2:
        return f"{MONTHS[m - 1]} {y}"
    return f"{MONTHS[m - 1]} {int(parts[2])}, {y}"


def _one_author(a):
    if "org" in a:
        name = a["org"]
    else:
        name = f'{a.get("given", "")} {a.get("family", "")}'.strip()
    if a.get("handle"):
        name = f'{name} ({a["handle"]})'
    return name


def _authors(authors):
    """Note form: first name first, no inversion. Chicago uses 'and'."""
    names = [_one_author(a) for a in (authors or [])]
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + f", and {names[-1]}"


def _platform(url):
    for dom, name in PLATFORMS.items():
        if dom in (url or ""):
            return name
    return None


def _description(title):
    """Social posts have no titles. A description sits unquoted and lowercase."""
    t = (title or "").strip()
    if t[:4].lower() == "post":
        return "post" + t[4:]
    return t[:1].lower() + t[1:] if t else t


def _join(parts):
    """Join citation parts, respecting punctuation a part already carries.

    Chicago puts the comma inside the closing quotation mark, so a title part
    arrives as '“Title,”' and must not receive a second comma. Both quote forms
    are tested: the ASCII pair is no longer emitted, but keying this test on one
    form is what silently doubled the comma when the quotes were corrected.
    """
    out = ""
    for p in (x for x in parts if x):
        if not out:
            out = p
        elif out.rstrip().endswith((',”', ',"', ",", ".")):
            out += " " + p
        else:
            out += ", " + p
    return out


def format_note(entry, url_policy="full"):
    """Return the footnote text for one source entry, without terminal period."""
    t = entry.get("type", "web")
    parts = [_authors(entry.get("authors"))]

    if t == "social":
        desc = _description(entry.get("title"))
        plat = _platform(entry.get("url"))
        # The description usually already names the platform. Do not repeat it.
        if plat and plat.lower() not in desc.lower():
            desc = f"{desc}, {plat}"
        parts.append(desc)
    else:
        if entry.get("title"):
            # Typographic quotes, not ASCII. Chicago sets a title in curly
            # marks, and body prose already uses them, so a straight mark in a
            # note reads as a typewriter artifact next to the prose above it.
            parts.append(f'“{entry["title"]},”')
        if entry.get("container"):
            # An article's year parenthetical attaches to the journal name
            # with no intervening comma.
            if t == "article":
                yr = _date(entry.get("date"))
                parts.append(f'<i>{entry["container"]}</i>'
                             + (f" ({yr})" if yr else ""))
            else:
                parts.append(f'<i>{entry["container"]}</i>')

    if t != "article":
        d = _date(entry.get("date"))
        if d:
            parts.append(d)

    if entry.get("perishable") and entry.get("accessed"):
        parts.append(f'accessed {_date(entry["accessed"])}')

    if url_policy == "full":
        if entry.get("doi"):
            parts.append(f'<span class="url">https://doi.org/{entry["doi"]}</span>')
        elif entry.get("url"):
            parts.append(f'<span class="url">{entry["url"]}</span>')

    return _join(parts)


def format_footnote(keys, sources, gloss="", url_policy="full"):
    """Assemble a full footnote from one or more source keys plus a gloss."""
    notes = [format_note(sources[k], url_policy) for k in keys if k in sources]
    text = "; ".join(notes)
    if text and not text.endswith("."):
        text += "."
    if gloss:
        g = gloss.strip().rstrip(".")
        if g:
            # Glosses are used verbatim. Capitalisation is an editorial
            # property of the gloss text, not something to infer here.
            text += " " + g + "."
    return text
