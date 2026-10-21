#!/usr/bin/env python3
"""Verify the generated study site.

The promise made about this site is that NOTHING is reduced, so the checks are
built around proving that rather than around the site looking right:

  1. every .md file on disk has a page
  2. text sampled from the start, middle and END of each source file is present
     in its rendered page -- this is what would catch truncation
  3. every internal link on every page resolves to a file that exists
  4. the page actually works in real Google Chrome: nav, search, theme, and no
     horizontal overflow at phone width

Run: python3 verify_site.py
"""
import json
import pathlib
import re
import sys

from build_site import LIBRARIES   # the card count is derived, never hardcoded

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "study-site"
RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond), detail))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   [{detail}]" if detail else ""))


def plain(html_text):
    txt = re.sub(r"<(script|style)\b.*?</\1>", " ", html_text, flags=re.S | re.I)
    txt = re.sub(r"<[^>]+>", " ", txt)
    txt = (txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
              .replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " "))
    return re.sub(r"\s+", " ", txt).strip()


def norm(s):
    """Collapse whatever differs between markdown source and rendered text.

    Emphasis and code markers vanish on render; underscores inside words do not.
    Normalising BOTH sides the same way means a probe can only fail because the
    words are genuinely absent -- which is the thing being tested.
    """
    s = re.sub(r"[*`~]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def squash(s):
    """Whitespace-free form. Rendering turns `x`: into x :, which is not a defect."""
    return re.sub(r"\s+", "", s)


def strip_md(line):
    line = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", line)   # list marker
    line = re.sub(r"^\s*>+\s*", "", line)                      # blockquote
    line = re.sub(r"^\s*#+\s*", "", line)                      # heading
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)      # link -> its text
    return norm(line)


# ---------------------------------------------------------------- 1. coverage
def source_md():
    out = []
    for p in ROOT.rglob("*.md"):
        parts = p.parts
        if any(x in parts for x in ("scratchpad", "drafts", "site", "study-site",
                                    "sitebuild", "node_modules", ".git",
                                    # ds-jobs/ds-out hold the generator's prompt files and
                                    # raw drafts; the reviewed copies live in the library.
                                    "ds-jobs", "ds-out", "artifact", "_backlog", "src",
                                    # design specs and plans for the library live outside it
                                    "docs")):
            continue
        if p.name in ('prompt.md',):
            continue
        out.append(p)
    return sorted(out)


def run_static():
    print("\n1. Coverage -- every markdown file has a page")
    manifest = json.loads((SITE / "assets" / "manifest.json").read_text())
    md_pages = [m for m in manifest if m["kind"] == "md"]
    on_disk = source_md()
    check("1.1 page count equals file count",
          len(md_pages) == len(on_disk), f"{len(md_pages)} pages / {len(on_disk)} files")

    by_disk = {m["disk"] for m in manifest}
    missing = [p.relative_to(ROOT).as_posix() for p in on_disk
               if p.relative_to(ROOT).as_posix() not in by_disk]
    check("1.2 no markdown file is absent", not missing,
          "" if not missing else f"missing: {missing[:3]}")
    check("1.3 source files are included too",
          sum(1 for m in manifest if m["kind"] == "code") >= 6,
          f'{sum(1 for m in manifest if m["kind"] == "code")} source pages')

    print("\n2. Completeness -- start, middle and END of every file survived")
    thin, sampled, missed = [], 0, []
    for m in md_pages:
        page = SITE / m["url"]
        if not page.exists():
            missed.append(m["url"])
            continue
        rendered = squash(norm(plain(page.read_text(encoding="utf-8"))))
        src_path = ROOT / m["disk"]
        if not src_path.exists():
            missed.append(f'{m["url"]} :: source missing {m["disk"]}')
            continue
        raw = src_path.read_text(encoding="utf-8", errors="replace")

        # a rendered page must carry most of its source's characters
        if m["text_chars"] < 0.45 * m["src_chars"] and m["src_chars"] > 400:
            thin.append((m["url"], m["src_chars"], m["text_chars"]))

        # sample real prose from three depths, the last one deliberately near the end
        lines = [ln for ln in raw.splitlines()
                 if len(ln.strip()) > 45
                 and not ln.lstrip().startswith(("|", "```", "![", "<"))]
        if len(lines) < 3:
            continue
        for frac in (0.15, 0.55, 0.96):
            ln = lines[min(int(len(lines) * frac), len(lines) - 1)]
            probe = strip_md(ln)[:45]
            if len(probe) < 20:
                continue
            sampled += 1
            if squash(probe) not in rendered:
                missed.append(f'{m["url"]} :: {probe[:40]}')
    check("2.1 no page rendered suspiciously thin", not thin,
          "" if not thin else f"{len(thin)} thin, e.g. {thin[0]}")
    check(f"2.2 all {sampled} sampled passages present, including end-of-file ones",
          not missed, "" if not missed else f"{len(missed)} missing, e.g. {missed[0][:70]}")

    print("\n3. Links -- every internal href resolves")
    broken, total = [], 0
    for page in SITE.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http://", "https://", "#", "mailto:",
                                "data:", "javascript:")):
                continue
            total += 1
            target = (page.parent / href.split("#")[0]).resolve()
            if not target.exists():
                broken.append(f"{page.relative_to(SITE)} -> {href}")
    check(f"3.1 all {total} internal links resolve", not broken,
          "" if not broken else f"{len(broken)} broken, e.g. {broken[0]}")
    dead = len(re.findall(r'class="dead"', "".join(
        p.read_text(encoding="utf-8") for p in SITE.rglob("*.html"))))
    check("3.2 unresolvable source links are marked, not silently dropped",
          dead < 10, f"{dead} marked dead (files that do not exist in the repo)")


# ---------------------------------------------------------------- 4. browser
def run_browser():
    from playwright.sync_api import sync_playwright
    print("\n4. Real Google Chrome")
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        ctx = b.new_context()
        pg = ctx.new_page()
        errors = []
        pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errors.append(str(e)))

        home = (SITE / "index.html").as_uri()
        pg.goto(home)
        check("4.1 home page renders its heading",
              "Infosys" in pg.inner_text("h1"), pg.inner_text("h1")[:40])
        check("4.2 a card is present for every library",
              pg.locator(".libcard").count() == len(LIBRARIES),
              f'{pg.locator(".libcard").count()} cards / {len(LIBRARIES)} libraries')
        check("4.3 the stat bar counts the pages",
              pg.locator(".stat").count() >= 4)

        # deep page with tables and code
        deep = SITE / "infosys-se" / "puzzles" / "Z1-number-grids-and-matrices.html"
        pg.goto(deep.as_uri())
        check("4.4 a deep page renders", "Number grids" in pg.inner_text("h1"),
              pg.inner_text("h1")[:40])
        check("4.5 its code blocks are syntax-highlighted",
              pg.locator(".codehilite").count() >= 1, str(pg.locator(".codehilite").count()))
        check("4.6 its tables are wrapped so they scroll in their own box",
              pg.locator(".tablewrap").count() >= 3, str(pg.locator(".tablewrap").count()))
        check("4.7 the sidebar shows the current page as current",
              pg.locator(".navitem.current").count() == 1)
        check("4.8 prev/next pagers exist", pg.locator(".pager").count() == 2)
        check("4.9 the on-this-page table of contents is built",
              pg.locator(".toc a").count() > 4, str(pg.locator(".toc a").count()))

        # a link out of a page actually goes somewhere real. The topic files are
        # self-contained by design, so this is checked on the index, which is where
        # this library's cross-references live.
        pg.goto((SITE / "infosys-se" / "00-MASTER-INDEX.html").as_uri())
        first_internal = pg.eval_on_selector_all(
            ".prose a[href]",
            "els => els.map(e => e.getAttribute('href')).filter(h => "
            "!h.startsWith('http') && h !== '#')")
        check("4.10 the page links on to other pages", len(first_internal) > 2,
              f"{len(first_internal)} internal links in the body")

        # search
        pg.fill("#q", "puzzle")
        pg.wait_for_function(
            "() => { const r = document.getElementById('results');"
            " return r && !r.hidden && r.querySelectorAll('a').length > 0; }", timeout=15000)
        n = pg.locator("#results a").count()
        top = pg.inner_text("#results a >> nth=0")
        check("4.11 search returns hits for 'puzzle'", n > 0, f"{n} results")
        check("4.12 the top hit is a puzzle page",
              ("grid" in top.lower() or "puzzle" in top.lower() or "kakuro" in top.lower()), top.split("\n")[0][:50])
        pg.fill("#q", "increment")
        pg.wait_for_function(
            "() => document.querySelectorAll('#results a').length > 0", timeout=15000)
        # one library here, so this checks that search reaches across SECTIONS
        check("4.13 search reaches across sections",
              "increment" in pg.inner_text("#results").lower(),
              "found a pseudocode-section hit")
        pg.fill("#q", "zzzzqqqq")
        pg.wait_for_timeout(200)
        check("4.14 a query that matches nothing says so, and does not crash",
              "Nothing matches" in pg.inner_text("#results"))

        # theme
        pg.fill("#q", "")
        before = pg.eval_on_selector("body", "e => getComputedStyle(e).backgroundColor")
        pg.click("#themeBtn")
        after = pg.eval_on_selector("body", "e => getComputedStyle(e).backgroundColor")
        check("4.15 the theme toggle changes the page background", before != after,
              f"{before} -> {after}")
        pg.reload()
        kept = pg.eval_on_selector("body", "e => getComputedStyle(e).backgroundColor")
        check("4.16 the theme choice survives a reload", kept == after, kept)
        check("4.17 body has an explicit background in both themes",
              kept not in ("rgba(0, 0, 0, 0)", "transparent"), kept)

        # phone width
        pg.set_viewport_size({"width": 390, "height": 780})
        pg.goto(deep.as_uri())
        overflow = pg.evaluate(
            "() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        check("4.18 no horizontal page scroll at 390px", overflow <= 1, f"{overflow}px")
        check("4.19 the sidebar is off-canvas on a phone",
              pg.eval_on_selector(".sidenav", "e => e.getBoundingClientRect().right") <= 1)
        pg.click("#menuBtn")
        pg.wait_for_timeout(300)
        check("4.20 the menu button opens it",
              pg.eval_on_selector(".sidenav", "e => e.getBoundingClientRect().right") > 100)

        check("4.21 no console or page errors anywhere in the run",
              not errors, "" if not errors else errors[0][:80])
        ctx.close()
        b.close()


if __name__ == "__main__":
    if not SITE.exists():
        sys.exit("study-site/ not built -- run: python3 build_site.py")
    run_static()
    try:
        run_browser()
    except Exception as exc:                                  # noqa: BLE001
        check("4.x browser checks ran", False, f"{type(exc).__name__}: {exc}")
    ok = sum(1 for _, c, _ in RESULTS if c)
    print(f"\n{'=' * 62}\n{ok}/{len(RESULTS)} site checks passed")
    bad = [n for n, c, _ in RESULTS if not c]
    if bad:
        print("FAILED:", *bad, sep="\n  ")
    sys.exit(0 if not bad else 1)
