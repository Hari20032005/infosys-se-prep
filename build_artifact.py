#!/usr/bin/env python3
"""Pack the built study-site into a single-page app that can be published.

study-site/ is 271 separate HTML files, which is more files than an artifact can
hold. This takes the SAME pages, in the SAME order, and re-packs them as:

    artifact/index.html          the shell: nav, search, router, theme
    artifact/content/<lib>.js    every rendered article body, one file per library
    artifact/assets/fulltext.js  plain text of every page, for search

Nothing is summarised or trimmed: the article bodies are the exact HTML that
build_site.py already rendered and verify_site.py already checked.

    python3 build_site.py && python3 build_artifact.py
"""
import json
import pathlib
import re
import shutil

from build_site import LIBRARIES, discover, title_of

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "study-site"
OUT = ROOT / "artifact"

ARTICLE_RE = re.compile(r'<article class="prose">(.*?)</article>', re.S)


def article_of(url):
    """The rendered body of one built page, exactly as it is on the static site."""
    f = SITE / url
    m = ARTICLE_RE.search(f.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"no article body in {f}")
    return m.group(1).strip()


def to_hash_links(body):
    """Static site links (../../lib/page.html) become in-app routes (#/lib/page)."""
    def fix(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        frag = ""
        if "#" in href:
            href, frag = href.split("#", 1)
            frag = "#" + frag
        href = re.sub(r"^(\.\./)+", "", href)
        if href.endswith(".html"):
            return 'href="#/%s%s"' % (href[:-5], frag)
        return m.group(0)
    return re.sub(r'href="([^"]+)"', fix, body)


def plain(html_text):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html_text, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                 ("&quot;", '"'), ("&#39;", "'")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


# A non-ASCII byte in the shell renders as mojibake wherever the charset is not
# declared, which has already bitten this project once. The shell is therefore
# written as pure ASCII: typographic characters in the CSS and markup are
# transliterated, and everything inside the script becomes a \uXXXX escape.
TRANSLIT = {
    "\u2014": "--", "\u2013": "-", "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"', "\u2026": "...", "\u00b7": "*",
    "\u00a0": " ",
}


def asciify(shell):
    head, sep, tail = shell.partition("<script>")
    if not sep:
        raise SystemExit("shell has no <script> block")
    for ch, rep in TRANSLIT.items():
        head = head.replace(ch, rep)
    stray = sorted({c for c in head if ord(c) > 127})
    if stray:
        raise SystemExit(f"shell head still has non-ASCII: {stray!r} -- extend TRANSLIT")
    tail = "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in tail)
    return head + sep + tail


def main():
    pages, by_lib = discover()
    titles = {p["url"]: title_of(p) for p in pages}

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "content").mkdir(parents=True)
    (OUT / "assets").mkdir(parents=True)

    nav, fulltext, total = [], [], 0
    for lib in LIBRARIES:
        slug = lib["slug"]
        entries = by_lib.get(slug) or []
        if not entries:
            continue
        bundle = {}
        for e in entries:
            body = to_hash_links(article_of(e["url"]))
            key = e["url"][:-5]                      # drop .html
            bundle[key] = body
            nav.append({"u": key, "t": titles[e["url"]], "l": slug,
                        "s": e["section_name"], "k": e["kind"]})
            fulltext.append({"u": key, "x": plain(body)})
        js = "window.APREP_PUT('%s',%s);" % (
            slug, json.dumps(bundle, ensure_ascii=True, separators=(",", ":")))
        f = OUT / "content" / f"{slug}.js"
        f.write_text(js, encoding="ascii")
        total += f.stat().st_size
        print(f"  {slug:<12} {len(entries):>4} pages  {f.stat().st_size/1e6:>6.2f} MB")

    ft = OUT / "assets" / "fulltext.js"
    ft.write_text("window.APREP_FT=%s;" % json.dumps(
        fulltext, ensure_ascii=True, separators=(",", ":")), encoding="ascii")
    print(f"  fulltext     {len(fulltext):>4} pages  {ft.stat().st_size/1e6:>6.2f} MB")

    libs = [{"slug": l["slug"], "name": l["name"], "short": l["short"],
             "blurb": l["blurb"], "n": len(by_lib.get(l["slug"]) or [])}
            for l in LIBRARIES if by_lib.get(l["slug"])]

    css = (SITE / "assets" / "style.css").read_text(encoding="utf-8")
    shell = (ROOT / "artifact_shell.html").read_text(encoding="utf-8")
    shell = shell.replace("/*SITE_CSS*/", css)
    shell = shell.replace("/*NAV_JSON*/", json.dumps(
        nav, ensure_ascii=True, separators=(",", ":")))
    shell = shell.replace("/*LIBS_JSON*/", json.dumps(
        libs, ensure_ascii=True, separators=(",", ":")))
    shell = asciify(shell)
    (OUT / "index.html").write_text(shell, encoding="ascii")

    print(f"\n  index.html   {(OUT / 'index.html').stat().st_size/1e6:>6.2f} MB")
    print(f"  {len(nav)} pages packed, {total/1e6:.2f} MB of content")


if __name__ == "__main__":
    main()
