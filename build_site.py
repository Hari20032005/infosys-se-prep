#!/usr/bin/env python3
"""Build the study website from every markdown file in the four prep libraries.

Nothing is summarised, trimmed or reformatted: each .md file becomes one page
carrying its full rendered content. Java, SQL and HTML source files are included
as read-only source pages so the solutions are readable on the site too.

    python3 build_site.py     ->  study-site/

No network access, no build step for the reader: open study-site/index.html.
"""
import html
import json
import os
import pathlib
import re
import sys

import markdown
from pygments.formatters import HtmlFormatter

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "study-site"   # NOT site/ -- another builder (sitebuild/) owns that

# ---------------------------------------------------------------- libraries

LIBRARIES = [
    {
        "dir": "infosys-prep-library",
        "slug": "infosys-se",
        "name": "Infosys \u2014 Systems Engineer",
        "short": "Infosys SE",
        "blurb": "Seven timed sections, 60 questions in 120 minutes: reasoning, maths, verbal, pseudocode, number puzzles, grammar and an essay. A cut-off in every section. No coding, no calculator.",
    },
]


# Section display names, in reading order. Anything unlisted lands in "More".
SECTION_ORDER = [
    ("", "Start here"),
    ("core-course", "Core Course: start here"),
    ("aptitude", "Aptitude \u2014 from zero"),
    ("topics", "Topic files"),
    ("puzzles", "Numerical puzzles"),
    ("pseudocode", "Pseudocode"),
    ("question-banks", "Question banks & mock"),
    ("interview", "Interview"),
    ("research", "Evidence & method"),
    ("data", "Data & verifiers"),
]

SECTION_RANK = {k: i for i, (k, _) in enumerate(SECTION_ORDER)}
SECTION_NAME = dict(SECTION_ORDER)

SKIP_DIRS = {"scratchpad", "drafts", "__pycache__", ".git", "node_modules",
             "site", "study-site", "sitebuild", "src"}
CODE_SUFFIXES = {".java": "java", ".sql": "sql", ".html": "html", ".json": "json",
                 ".py": "python", ".csv": "csv", ".js": "javascript", ".css": "css"}
MD_EXT = [
    "tables", "fenced_code", "codehilite", "toc", "attr_list",
    "sane_lists", "md_in_html", "footnotes",
]
MD_CFG = {"codehilite": {"guess_lang": False}, "toc": {"anchorlink": False}}


def natural_key(p: str):
    """Sort 00-, 01-, 02-, 10-, 90- the way a human reads them."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p)]


def discover():
    """Every page on the site, in reading order, grouped by library and section."""
    pages, by_lib = [], {}
    for lib in LIBRARIES:
        libdir = (ROOT / lib["dir"]).resolve()
        if not libdir.is_dir():
            continue
        found = []
        if lib.get("globs"):
            for pat in lib["globs"]:
                for src in sorted(libdir.glob(pat)):
                    if not src.is_file():
                        continue
                    rel = src.relative_to(libdir)
                    rel_dir = rel.parent.as_posix()
                    rel_dir = "" if rel_dir == "." else rel_dir
                    kind = "md" if src.suffix.lower() == ".md" else "code"
                    found.append((rel_dir, rel, src, kind))
            found.sort(key=lambda t: (t[0], natural_key(t[1].name)))
            entries = []
            for rel_dir, rel, src, kind in found:
                url = f"{lib['slug']}/{rel.with_suffix('.html').as_posix()}"
                page = {
                    "lib": lib["slug"], "lib_name": lib["name"], "lib_short": lib["short"],
                    "section": rel_dir,
                    "section_name": "The briefs" if not rel_dir else "Raw evidence",
                    "src": src, "rel": rel.as_posix(), "url": url, "kind": kind,
                }
                entries.append(page)
                pages.append(page)
            by_lib[lib["slug"]] = entries
            continue
        for dirpath, dirnames, filenames in os.walk(libdir):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
            rel_dir = pathlib.Path(dirpath).relative_to(libdir).as_posix()
            rel_dir = "" if rel_dir == "." else rel_dir
            for fn in filenames:
                suffix = pathlib.Path(fn).suffix.lower()
                if suffix == ".md":
                    kind = "md"
                elif suffix in CODE_SUFFIXES:
                    if fn.startswith("."):
                        continue
                    kind = "code"
                else:
                    continue
                src = pathlib.Path(dirpath) / fn
                rel = src.relative_to(libdir)
                found.append((rel_dir, rel, src, kind))

        found.sort(key=lambda t: (
            SECTION_RANK.get(t[0], 500 + len(t[0])),
            t[0],
            natural_key(t[1].name),
        ))
        entries = []
        for rel_dir, rel, src, kind in found:
            url = f"{lib['slug']}/{rel.with_suffix('.html').as_posix()}"
            page = {
                "lib": lib["slug"], "lib_name": lib["name"], "lib_short": lib["short"],
                "section": rel_dir, "section_name": SECTION_NAME.get(rel_dir) or (
                    rel_dir.replace("/", " / ") if rel_dir else "Start here"),
                "src": src, "rel": rel.as_posix(), "url": url, "kind": kind,
            }
            entries.append(page)
            pages.append(page)
        by_lib[lib["slug"]] = entries
    return pages, by_lib


def title_of(page):
    if page["kind"] == "code":
        return page["src"].name
    for line in page["src"].read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return re.sub(r"[*`]", "", line[2:]).strip()
    return page["src"].stem.replace("-", " ")


FENCE_RE = re.compile(r"(^```.*?^```)", re.S | re.M)


def enable_markdown_in_details(text):
    """<details> blocks hold markdown, so tell the renderer to process it.

    python-markdown treats the inside of a raw HTML block as raw HTML, which
    left every collapsible answer section in the question banks showing literal
    `- (a) ...` and unrendered tables. The md_in_html extension fixes that, but
    only when the tag carries markdown="1". Fenced code is left alone so a
    <details> shown as an EXAMPLE is not rewritten.
    """
    def fix(chunk):
        chunk = re.sub(r"<details(?![^>]*\bmarkdown=)([^>]*)>",
                       r'<details markdown="1"\1>', chunk)
        return re.sub(r"<summary(?![^>]*\bmarkdown=)([^>]*)>",
                      r'<summary markdown="1"\1>', chunk)

    parts = FENCE_RE.split(text)
    return "".join(p if p.startswith("```") else fix(p) for p in parts)


FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def front_matter_line(fm_text):
    """One quiet metadata line from a file's YAML front matter (it used to show as a raw paragraph)."""
    fm = dict(re.findall(r"(?m)^(\w+):\s*(.+)$", fm_text))
    bits = []
    if fm.get("tier"):
        bits.append(f"Tier {fm['tier']}")
    for k in ("section", "weightage_pct"):
        if fm.get(k):
            bits.append(fm[k])
    if fm.get("est_study_hours"):
        bits.append(f"about {fm['est_study_hours']} h")
    if fm.get("confidence"):
        bits.append(f"confidence {fm['confidence']}")
    if not bits:
        return ""
    return f'<p class="fm-line" style="color:var(--ink-faint);font-size:13px;margin:-.4em 0 1.2em">{html.escape(" · ".join(bits))}</p>'


def render_markdown(text):
    meta = ""
    m = FM_RE.match(text)
    if m:                                   # drop the front matter from the body; keep a one-line summary
        meta = front_matter_line(m.group(1))
        text = text[m.end():]
    text = enable_markdown_in_details(text)
    md = markdown.Markdown(extensions=MD_EXT, extension_configs=MD_CFG)
    body = md.convert(text)
    if meta:
        body = body.replace("</h1>", "</h1>" + meta, 1) if "</h1>" in body else meta + body
    toc = getattr(md, "toc_tokens", [])
    return body, toc


def render_csv(page):
    import csv as _csv
    raw = page["src"].read_text(encoding="utf-8", errors="replace")
    rows = list(_csv.reader(raw.splitlines()))
    if not rows:
        return "<p>empty</p>", []
    head, body_rows = rows[0], rows[1:]
    out = [f'<p class="src-note">Data file · <code>{html.escape(page["rel"])}</code> · '
           f'{len(body_rows)} rows. Shown in full.</p>', "<table><thead><tr>"]
    out += [f"<th>{html.escape(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for r in body_rows:
        out.append("<tr>" + "".join(
            f"<td>{html.escape(c)}</td>" for c in (r + [""] * (len(head) - len(r)))) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out), []


def render_code(page):
    if page["src"].suffix.lower() == ".csv":
        return render_csv(page)
    raw = page["src"].read_text(encoding="utf-8", errors="replace")
    lang = CODE_SUFFIXES[page["src"].suffix.lower()]
    fence = "```" + lang + "\n" + raw + "\n```"
    body, _ = render_markdown(fence)
    lines = raw.count("\n") + 1
    note = (f'<p class="src-note">Source file · <code>{html.escape(page["rel"])}</code> · '
            f'{lines} lines. Shown read-only.</p>')
    return note + body, []


EMPTY_THEAD = re.compile(r"<thead>\s*<tr>(?:\s*<th[^>]*>\s*</th>)+\s*</tr>\s*</thead>", re.S)


def drop_empty_theads(body):
    """A markdown table written as `| | |` has no real header; do not draw one."""
    return EMPTY_THEAD.sub("", body)


def flatten_toc(tokens, depth=0, out=None):
    out = [] if out is None else out
    for t in tokens:
        if depth <= 1:
            out.append({"id": t["id"], "name": re.sub(r"<[^>]+>", "", t["name"]), "level": depth})
        flatten_toc(t.get("children", []), depth + 1, out)
    return out


# ---------------------------------------------------------------- link rewriting

def rewrite_links(body, page, url_by_source):
    """Point every relative .md / .java / .sql / .html link at its page on the site."""
    src_dir = page["src"].parent

    def fix(m):
        attr, href = m.group(1), m.group(2)
        if re.match(r"^(https?:|#|mailto:|/)", href):
            return m.group(0)
        frag = ""
        if "#" in href:
            href, frag = href.split("#", 1)
            frag = "#" + frag
        if not href:
            return m.group(0)
        target = (src_dir / href).resolve()
        depth = page["url"].count("/")
        up = "../" * depth
        if target in url_by_source:
            return f'{attr}="{up}{url_by_source[target]}{frag}"'
        if target.is_dir():                       # a folder link -> its index, else its first page
            for cand in ("00-INDEX.md", "00-MASTER-INDEX.md", "README.md"):
                if (target / cand).resolve() in url_by_source:
                    return f'{attr}="{up}{url_by_source[(target / cand).resolve()]}{frag}"'
            inside = [u for src, u in url_by_source.items()
                      if str(src).startswith(str(target) + os.sep)]
            if inside:
                return f'{attr}="{up}{sorted(inside)[0]}"'
            return f'{attr}="#" class="dead" title="folder not on the site: {html.escape(href)}"'
        return (f'{attr}="#" class="dead" '
                f'title="not published to the site: {html.escape(href)}"')

    return re.sub(r'(href)="([^"]+)"', fix, body)


# ---------------------------------------------------------------- page chrome

def nav_html(page, by_lib, titles, depth):
    up = "../" * depth
    out = ['<nav class="sidenav" aria-label="Library">']
    out.append(f'<a class="home" href="{up}index.html">Library home</a>')
    for lib in LIBRARIES:
        slug = lib["slug"]
        entries = by_lib.get(slug) or []
        if not entries:
            continue
        current = page is not None and page["lib"] == slug
        out.append(f'<div class="navlib{" open" if current else ""}">')
        first = entries[0]["url"]
        out.append(f'<a class="navlib-h" href="{up}{first}">'
                   f'<span class="navlib-name">{html.escape(lib["short"])}</span>'
                   f'<span class="navlib-n">{len(entries)}</span></a>')
        if current:
            last_section = None
            for e in entries:
                if e["section"] != last_section:
                    last_section = e["section"]
                    out.append(f'<div class="navsec">{html.escape(e["section_name"])}</div>')
                cls = "navitem current" if page and e["url"] == page["url"] else "navitem"
                extra = " code" if e["kind"] == "code" else ""
                out.append(f'<a class="{cls}{extra}" href="{up}{e["url"]}">'
                           f'{html.escape(titles[e["url"]])}</a>')
        out.append("</div>")
    out.append("</nav>")
    return "\n".join(out)


def document(title, lib_name, content, page, by_lib, titles, depth, toc=None,
             prev_page=None, next_page=None, extra_class=""):
    up = "../" * depth
    toc_html = ""
    if toc:
        items = "".join(
            f'<a class="toc-l{t["level"]}" href="#{t["id"]}">{html.escape(t["name"])}</a>'
            for t in toc)
        toc_html = f'<aside class="toc"><div class="toc-h">On this page</div>{items}</aside>'

    pager = []
    if prev_page:
        pager.append(f'<a class="pager prev" href="{up}{prev_page["url"]}">'
                     f'<span>Previous</span><strong>{html.escape(titles[prev_page["url"]])}</strong></a>')
    if next_page:
        pager.append(f'<a class="pager next" href="{up}{next_page["url"]}">'
                     f'<span>Next</span><strong>{html.escape(titles[next_page["url"]])}</strong></a>')
    pager_html = f'<div class="pagers">{"".join(pager)}</div>' if pager else ""

    crumb = ""
    if page:
        sect = page["section_name"]
        crumb = (f'<div class="crumb"><span>{html.escape(page["lib_short"])}</span>'
                 f'<span class="sep">/</span><span>{html.escape(sect)}</span></div>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Infosys SE Prep</title>
<link rel="stylesheet" href="{up}assets/style.css">
<script>
  try {{ var t = localStorage.getItem('aprep-theme');
        if (t) document.documentElement.setAttribute('data-theme', t); }} catch (e) {{}}
</script>
</head>
<body class="{extra_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <button class="menu" id="menuBtn" aria-label="Open navigation" aria-expanded="false">☰</button>
  <a class="brand" href="{up}index.html">Infosys SE Prep</a>
  <div class="searchwrap">
    <input id="q" type="search" placeholder="Search all 4 libraries…" autocomplete="off"
           aria-label="Search" data-base="{up}">
    <div id="results" class="results" hidden></div>
  </div>
  <button class="themeBtn" id="themeBtn" aria-label="Toggle theme">◐</button>
</header>
<div class="shell">
  {nav_html(page, by_lib, titles, depth)}
  <main id="main">
    {crumb}
    <article class="prose">
{content}
    </article>
    {pager_html}
  </main>
  {toc_html}
</div>
<div class="scrim" id="scrim"></div>
<script src="{up}assets/app.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- assets

def pygments_css():
    light = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
    dark = HtmlFormatter(style="monokai").get_style_defs(".codehilite")
    return f"""
{light}
.codehilite {{ background: var(--code-bg) !important; }}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{ }}
  :root:not([data-theme="light"]) .codehilite {{ background: var(--code-bg) !important; }}
{indent_block(dark)}
}}
:root[data-theme="dark"] .codehilite {{ background: var(--code-bg) !important; }}
{scope_block(dark, ':root[data-theme="dark"] ')}
"""


def indent_block(css):
    return "\n".join("  :root:not([data-theme=\"light\"]) " + ln if ln.strip().startswith(".")
                     else "  " + ln for ln in css.splitlines())


def scope_block(css, prefix):
    out = []
    for ln in css.splitlines():
        out.append(prefix + ln if ln.strip().startswith(".") else ln)
    return "\n".join(out)


STYLE = r"""
/* Infosys SE Prep — study library.
   Palette is warm-neutral paper against deep ink blue, with ochre reserved for
   must-memorise callouts and a semantic ramp for the evidence tags. */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  --paper:      #f6f4ef;
  --surface:    #fffdf9;
  --surface-2:  #efece4;
  --ink:        #1a1e26;
  --ink-soft:   #4d5461;
  --ink-faint:  #7b8291;
  --rule:       #ddd8cd;
  --accent:     #1d4e6f;
  --accent-soft:#e3ecf2;
  --ochre:      #9a6b12;
  --ochre-soft: #f6eeda;
  --code-bg:    #f2efe8;
  --good:       #2f6b45;
  --warn:       #9a6b12;
  --bad:        #96392e;
  --shadow:     0 1px 2px rgba(26,30,38,.06), 0 6px 18px rgba(26,30,38,.05);
  --sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --serif: 'IBM Plex Serif', Georgia, serif;
  --mono: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:      #14171d;
    --surface:    #1a1e26;
    --surface-2:  #222832;
    --ink:        #e6e3dc;
    --ink-soft:   #a8aeba;
    --ink-faint:  #767d8b;
    --rule:       #2e3542;
    --accent:     #74b4dc;
    --accent-soft:#1c2d3a;
    --ochre:      #d8a84a;
    --ochre-soft: #2b2415;
    --code-bg:    #10131a;
    --good:       #6dbd8b;
    --warn:       #d8a84a;
    --bad:        #e0847a;
    --shadow:     0 1px 2px rgba(0,0,0,.4), 0 6px 18px rgba(0,0,0,.3);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper:      #14171d;
  --surface:    #1a1e26;
  --surface-2:  #222832;
  --ink:        #e6e3dc;
  --ink-soft:   #a8aeba;
  --ink-faint:  #767d8b;
  --rule:       #2e3542;
  --accent:     #74b4dc;
  --accent-soft:#1c2d3a;
  --ochre:      #d8a84a;
  --ochre-soft: #2b2415;
  --code-bg:    #10131a;
  --good:       #6dbd8b;
  --warn:       #d8a84a;
  --bad:        #e0847a;
  --shadow:     0 1px 2px rgba(0,0,0,.4), 0 6px 18px rgba(0,0,0,.3);
  color-scheme: dark;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: var(--paper); color: var(--ink);
  font-family: var(--sans); font-size: 16px; line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); }
.skip { position: absolute; left: -9999px; }
.skip:focus { left: 8px; top: 8px; background: var(--surface); padding: 8px 12px; z-index: 100; }

/* ---------- top bar ---------- */
.topbar {
  position: sticky; top: 0; z-index: 40;
  display: flex; align-items: center; gap: 12px;
  padding: 10px 16px; background: var(--surface);
  border-bottom: 1px solid var(--rule);
}
.brand {
  font-family: var(--serif); font-weight: 700; font-size: 17px;
  color: var(--ink); text-decoration: none; white-space: nowrap;
}
.menu, .themeBtn {
  background: none; border: 1px solid var(--rule); border-radius: 6px;
  color: var(--ink-soft); font-size: 15px; cursor: pointer;
  width: 34px; height: 34px; flex: none;
}
.menu { display: none; }
.searchwrap { position: relative; flex: 1; max-width: 520px; margin-left: auto; }
#q {
  width: 100%; padding: 8px 12px; border-radius: 7px;
  border: 1px solid var(--rule); background: var(--paper); color: var(--ink);
  font: inherit; font-size: 14px;
}
#q:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
.results {
  position: absolute; top: calc(100% + 6px); left: 0; right: 0;
  max-height: 65vh; overflow-y: auto; background: var(--surface);
  border: 1px solid var(--rule); border-radius: 8px; box-shadow: var(--shadow);
  z-index: 60;
}
.results a {
  display: block; padding: 9px 12px; text-decoration: none;
  border-bottom: 1px solid var(--rule); color: var(--ink);
}
.results a:last-child { border-bottom: none; }
.results a:hover, .results a.sel { background: var(--accent-soft); }
.results .rt { font-weight: 600; font-size: 14px; }
.results .rm { font-size: 12px; color: var(--ink-faint); }
.results .empty { padding: 12px; color: var(--ink-faint); font-size: 14px; }

/* ---------- shell ---------- */
.shell {
  display: grid; grid-template-columns: 270px minmax(0,1fr) 210px;
  gap: 28px; max-width: 1500px; margin: 0 auto; padding: 0 16px;
  align-items: start;
}
.sidenav {
  position: sticky; top: 61px; max-height: calc(100vh - 61px);
  overflow-y: auto; padding: 18px 0 40px; font-size: 14px;
}
.sidenav .home {
  display: block; padding: 6px 10px; margin-bottom: 10px;
  color: var(--ink-soft); text-decoration: none; font-size: 13px;
  border-radius: 6px;
}
.sidenav .home:hover { background: var(--surface-2); }
.navlib { margin-bottom: 6px; }
.navlib-h {
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
  padding: 7px 10px; border-radius: 6px; text-decoration: none;
  color: var(--ink); font-weight: 600; font-size: 14px;
}
.navlib-h:hover { background: var(--surface-2); }
.navlib.open > .navlib-h { background: var(--accent-soft); color: var(--accent); }
.navlib-n { font-size: 11px; color: var(--ink-faint); font-variant-numeric: tabular-nums; }
.navsec {
  margin: 12px 0 4px; padding: 0 10px; font-size: 11px; font-weight: 600;
  letter-spacing: .07em; text-transform: uppercase; color: var(--ink-faint);
}
.navitem {
  display: block; padding: 4px 10px 4px 18px; border-left: 2px solid transparent;
  color: var(--ink-soft); text-decoration: none; font-size: 13.5px;
}
.navitem:hover { color: var(--ink); background: var(--surface-2); }
.navitem.current {
  color: var(--accent); border-left-color: var(--accent);
  background: var(--accent-soft); font-weight: 600;
}
.navitem.code { font-family: var(--mono); font-size: 12px; }

main { min-width: 0; padding: 26px 0 60px; }
.crumb { font-size: 12.5px; color: var(--ink-faint); margin-bottom: 14px; }
.crumb .sep { margin: 0 7px; }

.toc {
  position: sticky; top: 61px; max-height: calc(100vh - 61px); overflow-y: auto;
  padding: 26px 0 40px; font-size: 13px;
}
.toc-h {
  font-size: 11px; font-weight: 600; letter-spacing: .07em;
  text-transform: uppercase; color: var(--ink-faint); margin-bottom: 8px;
}
.toc a {
  display: block; padding: 3px 0 3px 10px; color: var(--ink-soft);
  text-decoration: none; border-left: 2px solid var(--rule); line-height: 1.4;
}
.toc a:hover { color: var(--accent); border-left-color: var(--accent); }
.toc a.toc-l1 { padding-left: 20px; font-size: 12.5px; }
.toc a.active { color: var(--accent); border-left-color: var(--accent); font-weight: 600; }

/* ---------- prose ---------- */
/* Long bare URLs in the Resources sections have no break opportunity and pushed
   14 pages into horizontal scroll at 390px (verify_site 4.18). break-word handles
   prose; `anywhere` is needed on links, code and bold spans, which is where the
   raw URLs actually sit. */
.prose { max-width: 74ch; min-width: 0; overflow-wrap: break-word; }
.prose a, .prose code, .prose strong, .prose li { overflow-wrap: anywhere; }
.prose h1 {
  font-family: var(--serif); font-size: 31px; line-height: 1.2; font-weight: 700;
  margin: 0 0 18px; text-wrap: balance; letter-spacing: -.01em;
}
.prose h2 {
  font-family: var(--serif); font-size: 22px; font-weight: 700; line-height: 1.3;
  margin: 38px 0 12px; padding-top: 14px; border-top: 1px solid var(--rule);
  text-wrap: balance;
}
.prose h3 { font-size: 17px; font-weight: 600; margin: 26px 0 8px; }
.prose h4 { font-size: 15px; font-weight: 600; margin: 20px 0 6px; color: var(--ink-soft); }
.prose p, .prose li { font-size: 15.5px; }
.prose ul, .prose ol { padding-left: 22px; }
.prose li { margin: 4px 0; }
.prose li > ul, .prose li > ol { margin: 4px 0; }
.prose strong { font-weight: 600; }
.prose hr { border: none; border-top: 1px solid var(--rule); margin: 30px 0; }
.prose blockquote {
  margin: 18px 0; padding: 12px 16px; border-left: 3px solid var(--ochre);
  background: var(--ochre-soft); border-radius: 0 6px 6px 0;
}
.prose blockquote p { margin: 6px 0; }
.prose code {
  font-family: var(--mono); font-size: .875em; background: var(--code-bg);
  padding: 1px 5px; border-radius: 4px; word-break: break-word;
}
.prose pre {
  background: var(--code-bg); border: 1px solid var(--rule); border-radius: 8px;
  padding: 14px 16px; overflow-x: auto; margin: 16px 0;
}
.prose pre code { background: none; padding: 0; font-size: 13px; line-height: 1.55; }
.codehilite { border-radius: 8px; margin: 16px 0; }
.codehilite pre { margin: 0; border: 1px solid var(--rule); }
/* A wrapped table must not push the PAGE wide: the wrapper is a block inside
   .prose, whose default min-width lets it grow to its content. Pinning both
   max-width and min-width keeps the overflow inside the wrapper's own scroller.
   Found by verify_site 4.18 -- 4px of horizontal page scroll at 390px. */
.tablewrap { overflow-x: auto; margin: 18px 0; max-width: 100%; min-width: 0; }
.prose table {
  border-collapse: collapse; width: 100%; font-size: 14px;
  font-variant-numeric: tabular-nums;
}
.prose th, .prose td {
  border: 1px solid var(--rule); padding: 7px 11px; text-align: left; vertical-align: top;
}
.prose th { background: var(--surface-2); font-weight: 600; font-size: 13px; }
.prose tr:nth-child(even) td { background: color-mix(in srgb, var(--surface-2) 45%, transparent); }
.prose img { max-width: 100%; }
.prose a.dead { color: var(--ink-faint); text-decoration: line-through; cursor: not-allowed; }
.prose input[type=checkbox] { margin-right: 6px; }
.src-note {
  font-size: 13px; color: var(--ink-faint); border-left: 3px solid var(--rule);
  padding-left: 12px;
}

/* evidence tags — the library's own confidence vocabulary */
.tag { font-weight: 600; font-family: var(--mono); font-size: .82em; }
.tag-confirmed { color: var(--good); }
.tag-likely    { color: var(--accent); }
.tag-reported  { color: var(--warn); }
.tag-inferred, .tag-unverified { color: var(--bad); }

/* ---------- pagers ---------- */
.pagers { display: flex; gap: 12px; margin-top: 44px; flex-wrap: wrap; }
.pager {
  flex: 1 1 240px; display: block; padding: 12px 14px; border: 1px solid var(--rule);
  border-radius: 8px; text-decoration: none; background: var(--surface);
}
.pager:hover { border-color: var(--accent); }
.pager span { display: block; font-size: 11px; text-transform: uppercase;
  letter-spacing: .07em; color: var(--ink-faint); }
.pager strong { display: block; font-size: 14.5px; color: var(--ink); font-weight: 600;
  margin-top: 3px; }
.pager.next { text-align: right; }

/* ---------- home ---------- */
.home-hero { padding: 40px 0 26px; max-width: 70ch; }
.home-hero h1 {
  font-family: var(--serif); font-size: 38px; line-height: 1.12; margin: 0 0 12px;
  letter-spacing: -.015em; text-wrap: balance;
}
.home-hero p { font-size: 17px; color: var(--ink-soft); margin: 0 0 8px; }
.statbar {
  display: flex; flex-wrap: wrap; gap: 10px; margin: 24px 0 34px;
}
.stat {
  border: 1px solid var(--rule); border-radius: 8px; padding: 10px 14px;
  background: var(--surface); min-width: 120px;
}
.stat b {
  display: block; font-family: var(--serif); font-size: 23px; line-height: 1.1;
  font-variant-numeric: tabular-nums;
}
.stat span { font-size: 12px; color: var(--ink-faint); }
.libgrid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); }
.libcard {
  border: 1px solid var(--rule); border-radius: 10px; padding: 18px 20px;
  background: var(--surface); text-decoration: none; color: var(--ink);
  display: flex; flex-direction: column; gap: 8px;
}
.libcard:hover { border-color: var(--accent); box-shadow: var(--shadow); }
.libcard h3 { margin: 0; font-family: var(--serif); font-size: 18px; }
.libcard p { margin: 0; font-size: 14px; color: var(--ink-soft); }
.libcard .meta { font-size: 12px; color: var(--ink-faint); margin-top: auto; padding-top: 6px; }
.home-note {
  margin: 36px 0 0; padding: 16px 18px; border-left: 3px solid var(--ochre);
  background: var(--ochre-soft); border-radius: 0 8px 8px 0; font-size: 14.5px;
}
.home-note p { margin: 6px 0; }
.allpages { margin-top: 40px; }
.allpages h2 {
  font-family: var(--serif); font-size: 20px; border-top: 1px solid var(--rule);
  padding-top: 16px;
}

.scrim { display: none; }
@media (max-width: 1180px) {
  .shell { grid-template-columns: 250px minmax(0,1fr); }
  .toc { display: none; }
}
@media (max-width: 860px) {
  .shell { grid-template-columns: minmax(0,1fr); padding: 0 16px; }
  .menu { display: block; }
  .brand { font-size: 15px; }
  .sidenav {
    position: fixed; top: 0; left: 0; bottom: 0; width: 290px; z-index: 70;
    background: var(--surface); border-right: 1px solid var(--rule);
    transform: translateX(-100%); transition: transform .18s ease;
    max-height: none; padding: 16px 10px 40px;
  }
  body.navopen .sidenav { transform: none; }
  body.navopen .scrim {
    display: block; position: fixed; inset: 0; background: rgba(0,0,0,.35); z-index: 60;
  }
  .prose { max-width: none; }
  .home-hero h1 { font-size: 29px; }
  .prose h1 { font-size: 25px; }
}
@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
"""


APP_JS = r"""
(function () {
  var root = document.documentElement;
  var themeBtn = document.getElementById('themeBtn');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var cur = root.getAttribute('data-theme');
    if (!cur) {
      var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      cur = dark ? 'dark' : 'light';
    }
    var next = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('aprep-theme', next); } catch (e) {}
  });

  var menuBtn = document.getElementById('menuBtn');
  var scrim = document.getElementById('scrim');
  function closeNav() {
    document.body.classList.remove('navopen');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
  }
  if (menuBtn) menuBtn.addEventListener('click', function () {
    var open = document.body.classList.toggle('navopen');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  if (scrim) scrim.addEventListener('click', closeNav);

  // Wide tables and code blocks scroll inside their own box, never the page.
  var prose = document.querySelector('.prose');
  if (prose) {
    prose.querySelectorAll('table').forEach(function (t) {
      if (t.parentElement && t.parentElement.classList.contains('tablewrap')) return;
      var w = document.createElement('div');
      w.className = 'tablewrap';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });
  }

  // Highlight the heading currently in view.
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var a = map[en.target.id];
        if (!a) return;
        if (en.isIntersecting) {
          tocLinks.forEach(function (x) { x.classList.remove('active'); });
          a.classList.add('active');
        }
      });
    }, { rootMargin: '-70px 0px -75% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) obs.observe(el);
    });
  }

  // ---- search: the index is fetched only when the box is first used ----
  var q = document.getElementById('q');
  var results = document.getElementById('results');
  if (!q || !results) return;
  var base = q.getAttribute('data-base') || '';
  var loading = false, sel = -1, shown = [];

  var waiting = [];
  function loadIndex(cb) {
    if (window.APREP_INDEX) { if (cb) cb(); return; }
    if (cb) waiting.push(cb);          // queue, so a second caller is never dropped
    if (loading) return;
    loading = true;
    var s = document.createElement('script');
    s.src = base + 'assets/search-index.js';
    s.onload = function () {
      loading = false;
      var q = waiting; waiting = [];
      q.forEach(function (f) { f(); });
    };
    s.onerror = function () {
      loading = false; waiting = [];
      results.innerHTML = '<div class="empty">Search index did not load.</div>';
      results.hidden = false;
    };
    document.head.appendChild(s);
  }
  q.addEventListener('focus', function () { loadIndex(null); });

  function score(item, terms) {
    var t = item.t.toLowerCase(), h = item.h.toLowerCase(), b = item.b.toLowerCase(), s = 0;
    for (var i = 0; i < terms.length; i++) {
      var w = terms[i];
      if (!w) continue;
      var hit = 0;
      if (t.indexOf(w) !== -1) { s += t.indexOf(w) === 0 ? 60 : 40; hit = 1; }
      if (h.indexOf(w) !== -1) { s += 14; hit = 1; }
      if (b.indexOf(w) !== -1) { s += 4; hit = 1; }
      if (!hit) return 0;
    }
    return s;
  }

  function render() {
    var v = q.value.trim().toLowerCase();
    if (!v) { results.hidden = true; shown = []; return; }
    if (!window.APREP_INDEX) {
      results.innerHTML = '<div class="empty">Loading index…</div>';
      results.hidden = false;
      loadIndex(render);
      return;
    }
    var terms = v.split(/\s+/);
    var out = [];
    for (var i = 0; i < window.APREP_INDEX.length; i++) {
      var sc = score(window.APREP_INDEX[i], terms);
      if (sc > 0) out.push([sc, window.APREP_INDEX[i]]);
    }
    out.sort(function (a, b) { return b[0] - a[0]; });
    out = out.slice(0, 40);
    shown = out.map(function (o) { return o[1]; });
    sel = -1;
    if (!out.length) {
      results.innerHTML = '<div class="empty">Nothing matches “' +
        q.value.replace(/[<>&]/g, '') + '”.</div>';
    } else {
      results.innerHTML = out.map(function (o) {
        var it = o[1];
        return '<a href="' + base + it.u + '"><div class="rt">' + it.t +
               '</div><div class="rm">' + it.l + ' · ' + it.s + '</div></a>';
      }).join('');
    }
    results.hidden = false;
  }

  q.addEventListener('input', render);
  q.addEventListener('keydown', function (e) {
    var links = results.querySelectorAll('a');
    if (e.key === 'Escape') { results.hidden = true; q.blur(); return; }
    if (!links.length) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      sel += (e.key === 'ArrowDown' ? 1 : -1);
      if (sel < 0) sel = links.length - 1;
      if (sel >= links.length) sel = 0;
      for (var i = 0; i < links.length; i++) links[i].classList.toggle('sel', i === sel);
      links[sel].scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter' && sel >= 0) {
      e.preventDefault();
      window.location.href = links[sel].getAttribute('href');
    }
  });
  document.addEventListener('click', function (e) {
    if (!results.contains(e.target) && e.target !== q) results.hidden = true;
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== q &&
        !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)) {
      e.preventDefault(); q.focus();
    }
  });
})();
"""


# ---------------------------------------------------------------- evidence tags

TAG_RE = re.compile(r"\[(CONFIRMED|LIKELY|REPORTED|INFERRED|UNVERIFIED[^\]]*)\]")


def mark_tags(body):
    def repl(m):
        word = m.group(1).split()[0].lower().strip("—- ")
        cls = {"confirmed": "tag-confirmed", "likely": "tag-likely",
               "reported": "tag-reported", "inferred": "tag-inferred"}.get(word, "tag-unverified")
        return f'<span class="tag {cls}">[{m.group(1)}]</span>'
    # only inside code-free text: skip anything already inside a <code>/<pre>
    parts = re.split(r"(<pre.*?</pre>|<code.*?</code>)", body, flags=re.S)
    return "".join(p if p.startswith(("<pre", "<code")) else TAG_RE.sub(repl, p) for p in parts)


# ---------------------------------------------------------------- build

def build():
    pages, by_lib = discover()
    if not pages:
        sys.exit("no source files found")

    titles = {}
    for p in pages:
        titles[p["url"]] = title_of(p)
    url_by_source = {p["src"].resolve(): p["url"] for p in pages}

    OUT.mkdir(exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)
    (OUT / "assets" / "style.css").write_text(STYLE + pygments_css(), encoding="utf-8")
    (OUT / "assets" / "app.js").write_text(APP_JS, encoding="utf-8")

    index_rows, manifest, rendered = [], [], {}
    for i, page in enumerate(pages):
        raw = page["src"].read_text(encoding="utf-8", errors="replace")
        if page["kind"] == "md":
            body, toc_tokens = render_markdown(raw)
            toc = flatten_toc(toc_tokens)
        else:
            body, toc = render_code(page)
        body = rewrite_links(body, page, url_by_source)
        body = mark_tags(body)
        body = drop_empty_theads(body)
        rendered[page["url"]] = body

        plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
        index_rows.append({
            "u": page["url"], "t": titles[page["url"]], "l": page["lib_short"],
            "s": page["section_name"], "h": " ".join(t["name"] for t in toc)[:600],
            "b": plain[:700],
        })
        manifest.append({
            "url": page["url"], "src": f'{page["lib"]}/{page["rel"]}',
            "disk": page["src"].resolve().relative_to(ROOT).as_posix(),
            "title": titles[page["url"]], "kind": page["kind"],
            "src_chars": len(raw), "text_chars": len(plain),
        })

        prev_page = pages[i - 1] if i > 0 else None
        next_page = pages[i + 1] if i + 1 < len(pages) else None
        depth = page["url"].count("/")
        out_file = OUT / page["url"]
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(document(
            titles[page["url"]], page["lib_name"], body, page, by_lib, titles,
            depth, toc, prev_page, next_page), encoding="utf-8")

    (OUT / "assets" / "search-index.js").write_text(
        "window.APREP_INDEX=" + json.dumps(index_rows, separators=(",", ":")) + ";",
        encoding="utf-8")
    (OUT / "assets" / "manifest.json").write_text(
        json.dumps(manifest, indent=1), encoding="utf-8")

    write_home(pages, by_lib, titles)
    return pages, manifest


def write_home(pages, by_lib, titles):
    total_src = sum(p["src"].stat().st_size for p in pages)
    md_n = sum(1 for p in pages if p["kind"] == "md")
    code_n = sum(1 for p in pages if p["kind"] == "code")

    cards = []
    for lib in LIBRARIES:
        entries = by_lib.get(lib["slug"]) or []
        if not entries:
            continue
        kb = sum(e["src"].stat().st_size for e in entries) // 1024
        cards.append(
            f'<a class="libcard" href="{entries[0]["url"]}">'
            f'<h3>{html.escape(lib["name"])}</h3>'
            f'<p>{html.escape(lib["blurb"])}</p>'
            f'<div class="meta">{len(entries)} pages · {kb} KB · '
            f'starts at {html.escape(titles[entries[0]["url"]])}</div></a>')

    listing = []
    for lib in LIBRARIES:
        entries = by_lib.get(lib["slug"]) or []
        if not entries:
            continue
        listing.append(f'<h2>{html.escape(lib["name"])}</h2>')
        last = None
        for e in entries:
            if e["section"] != last:
                last = e["section"]
                listing.append(f'<div class="navsec">{html.escape(e["section_name"])}</div>')
            listing.append(f'<div><a href="{e["url"]}">{html.escape(titles[e["url"]])}</a>'
                           f' <span class="rm" style="color:var(--ink-faint);font-size:12px">'
                           f'{html.escape(e["rel"])}</span></div>')

    content = f"""
<div class="home-hero">
  <h1>Everything for the Infosys Systems Engineer test, in one place.</h1>
  <p>{len(pages)} pages, nothing summarised. Each file is here in full &mdash;
  the study material, the worked solutions, the evidence logs and the build records.</p>
</div>
<div class="statbar">
  <div class="stat"><b>{len(pages)}</b><span>pages</span></div>
  <div class="stat"><b>{md_n}</b><span>markdown files</span></div>
  <div class="stat"><b>{code_n}</b><span>source files</span></div>
  <div class="stat"><b>{total_src // 1024}</b><span>KB of material</span></div>
  <div class="stat"><b>60</b><span>mock questions</span></div>
</div>
<div class="libgrid">{''.join(cards)}</div>
<div class="home-note">
  <p><strong>Press <code>/</code> anywhere to search</strong> across the whole library by title,
  heading or opening text. Arrow keys move through results, Enter opens.</p>
  <p>Evidence tags keep their meaning here: <span class="tag tag-confirmed">[CONFIRMED]</span>
  <span class="tag tag-likely">[LIKELY]</span> <span class="tag tag-reported">[REPORTED]</span>
  <span class="tag tag-inferred">[INFERRED]</span> — colour follows the confidence, so you can
  see at a glance how much weight a claim carries.</p>
</div>
<div class="allpages">{''.join(listing)}</div>
"""
    (OUT / "index.html").write_text(document(
        "Infosys SE Prep", "", content, None, by_lib, titles, 0,
        extra_class="homepage"), encoding="utf-8")



if __name__ == "__main__":
    ps, mf = build()
    print(f"built {len(ps)} pages into {OUT}")
    print(f"  markdown: {sum(1 for m in mf if m['kind'] == 'md')}")
    print(f"  source:   {sum(1 for m in mf if m['kind'] == 'code')}")
