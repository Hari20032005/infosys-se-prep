# Infosys SE Prep

A self-contained preparation library for the **Infosys Systems Engineer (Trainee)** campus drive, 2026-27 batch.

Built from evidence rather than memory: every claim about the test carries a confidence tag, and the question banks, mock test, worked solutions and core course are generated and verified in this repository.

## What is inside

| Path | Contents |
|---|---|
| `infosys-prep-library/` | The source library: 192 markdown files — study plan, topic weightage, test strategy, 22-lesson core course, topic guides, question banks, mock test, interview material, evidence logs and verifier scripts. |
| `study-site/` | The generated static site: 213 HTML pages with search, dark mode and the full library. This is what gets deployed. |
| `artifact/` | Single-file artifact build of the library (`index.html` plus embedded content). |
| `build_site.py` | Builds `study-site/` from the markdown in `infosys-prep-library/`. |
| `build_artifact.py` | Builds the single-file artifact. |
| `verify_site.py` | Checks the generated site for broken links and missing pages. |
| `prompt.md` | The research and build brief the library was produced against. |

## Read online

Open `study-site/index.html`, or run a local server:

```bash
cd study-site
python3 -m http.server 8000
```

Then visit http://localhost:8000.

## Rebuild

```bash
python3 -m pip install markdown pygments
python3 build_site.py
python3 verify_site.py
```

## Deploy

The site is static. On Vercel the project root is `study-site/` — no build command and no output directory are required.
