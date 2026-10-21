# 05 — Source Credibility: previous-year questions

**Date:** 2026-10-01. **Question asked:** is there a trustworthy source of previous-year Systems Engineer questions (websites, GitHub, anywhere)? **Rule:** every source is analysed before anything is taken from it.

**Short answer.** There is **one** trustworthy source of real question text: Infosys's own sample paper (a 2020 PDF). Every website that publishes "Infosys previous-year pseudocode / puzzle questions" fails at least one test below, mostly because it never says where its questions come from. GitHub has nothing for this role. Those pages were read but **not imported**.

---

## 1. The tests every source had to pass

| # | Test | Why it matters here |
|---|---|---|
| 1 | **Who publishes it, and what do they sell?** | A page that exists to sell a course has a reason to look current and complete |
| 2 | **Does it say where the questions come from?** (drive, date, slot, candidate, "memory based", official) | Without an origin a question is not evidence of anything; it may be authored by the site |
| 3 | **Role and entity match**: Infosys Limited, Systems Engineer only | SP, DSE, Power Programmer, HackWithInfy and EdgeVerve are different tests |
| 4 | **Date**: is it from the era of the current test? | Pre-2025 patterns are hypotheses in this library |
| 5 | **Are the answers verifiable?** | Published keys on aggregator sites are often wrong; the Accenture build found wrong keys. Anything imported is re-solved by running code |
| 6 | **Does it agree with first-hand accounts?** | A page that contradicts every first-hand candidate account is wrong or about another role |
| 7 | **Can the text be redistributed?** | The library paraphrases and cites; it does not copy |

A source needs tests 2, 3 and 6 to count as evidence. Test 5 decides whether its questions can be used as practice material.

---

## 2. Verdicts

| Source | What I observed | Verdict |
|---|---|---|
| **Infosys official sample paper** `infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf` | **Host checked:** the TLS certificate is issued to `O=Infosys Limited, Bengaluru` (DigiCert, valid to Jan 2027) for `*.onwingspan.com`, so the domain is Infosys's own. The server sends an incomplete certificate chain, so `curl` and Python refuse it while a browser loads it; that is a server misconfiguration, not a sign of a fake. The file is a 14-page PDF. Footer on each page reads "Fresher Recruitment Sample Test paper \| Infosys Ltd"; PDF author metadata "Infosys Ltd", created 22 Sep 2020. Five sections, 54 questions, 100 minutes. Pseudocode 2 marks each; puzzles 3 / 2 / 2 / 3. No answer key. CONFIDENTIAL watermark although it sits at a public path | **A. Used.** Only first-party question text. All 54 items solved (31 by running code, 21 by judgement, 2 not solved). Linked and paraphrased, not copied (`question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md`). Limits: 2020, five-section layout, no key |
| **Talent Battle** "Infosys Pseudocode Previous Year Questions" | Training company; page dated 30 Apr 2024; 15 questions with answers and explanations; **no statement of where the questions came from**; paid-masterclass banners | **Not used.** "Previous year" in the URL is a claim with no support on the page |
| **PrepInsta** "Infosys Pseudo Code Questions and Answers" | Metis Eduventures; dated 16 Jul 2025; 10 sample questions in C (`printf`, `typedef`, `sizeof`); **no origin stated**; its own header says the real section has 5 questions in 10 minutes; heavy subscription promotion | **Not used.** The C-language style also differs from the pseudocode dialect in the official sample |
| **CodeQuotient** blog "Pseudocode questions, Infosys drive" | Dated 17 Aug 2022; six questions with answers; **no drive, date or role named**; paid-bootcamp promotion | **Not used.** Stale and unattributed |
| **placementpapers.app** `/infosys/2025/` | Run by KASP Digital LLC. Says its questions come from "student reports", "PrepInsta", "IndiaBix" and "actual exam patterns", with **no dates or slots**. Describes 65-70 questions, 180 minutes and **two coding problems**; covers SE, DSE and Power Programmer together. The first questions it shows are textbook arithmetic | **Rejected.** Contradicts every first-hand Systems Engineer account (no coding, 120 minutes), mixes roles, and cites another unattributed aggregator as a source |
| **GeeksforGeeks interview experience, GNDEC Ludhiana** (`…/infosys-interview-experience-for-system-engineer-10/`) | First-hand. Test 13 Oct 2025, posted 7 Jan 2026, 2026 batch. Section names listed; "1 hour 30 minutes"; no coding; "overall test is easy". **No question quoted.** Interview 20-25 minutes (OOP, core CS, projects, behavioural). Cleared both; offered the DSE or SP upgrade route | **B. Used** for section naming and interview evidence (logged as B7). Its 90-minute figure conflicts with the 120-minute accounts and is recorded, not adopted. GfG posts are user-submitted |
| **GitHub** `Akhilcrab/infosys-prep`, `ramkumar03ace/infosys-prep`, `karthikreddy-7/Infosys-SP-Coding-Questions` | Judged from the search listing (name and description); the repositories were **not opened or cloned**. They present coding questions for Specialist Programmer and Digital Specialist Engineer. No repository of Systems Engineer aptitude or pseudocode questions turned up in three GitHub-targeted searches | **Excluded by the role filter** (test 3) |
| **Reddit** | One search aimed at r/developersIndia returned no Reddit page at all (Naukri, Scribd and Wikipedia results instead) | **Nothing to assess** |
| Other aggregators from the search results (Campus Monk, FACE Prep, Unstop, assessfy, freshersnow, practiceaptitudetests.com, techtest.io) | **Listed by search but not fetched.** Same class as the four pages above; several were already logged as D-tier in `02-online-research-log.md` §3 | **Not used.** I did not read them, so I make no claim about their content beyond their class |

Already assessed in the first pass (`02-online-research-log.md`): Naukri Code360 first-hand accounts (B), Scribd decks (C/D), YouTube coaching transcripts (C), college placement-cell notices (A).

---

## 3. What these verdicts changed in the library

| Change | Detail |
|---|---|
| **New evidence tier** | The 54 official-sample items are a separate channel (`OFF-2020`, shown as "Infosys (official sample)"). They count as sightings and as a channel in the confidence rule, but because the paper is from 2020 they carry the *older* weight in the frequency formula, and they are left out of the repeat-rate (3 of 60) and difficulty figures |
| **Tier list moved** | Recomputed by `data/analyze.py` (tiers: T1 15 · T2 7 · T3 5 · T4 15). **Up:** A6 data sufficiency T2→T1, V3 sentence correction T3→T1, V6 critical reasoning T2→T1, A4 syllogisms and deduction T3→T2, P6 conditionals T4→T3, A21 non-verbal reasoning T4→T2. **Down:** V5 para-jumbles T2→T3, A9 averages and mixtures T2→T3, A11 mensuration T2→T3. A21's rise comes only from one first-hand account (B7) naming "non-verbal reasoning" as a section, plus the C1 deck; it costs 0.4 hours, so the plan keeps it optional. A19 (logic sets) stays T4 by the model's rule, because all ten sightings come from one 2020 paper; the 7-day plan still books it on the final day |
| **New practice material** | Question types seen in the sample but missing from the library now have generators with an independent check: data sufficiency (1-2-3-4), if-then attendance puzzles, ordered deduction, replacement mixtures, constrained arrangements, prime-gap series, grid-sum / cube-box / zig-zag puzzles, "identify the correct sentence", and pseudocode printed in the official dialect |
| **Aggregator questions** | None imported. Providing a key is not evidence of correctness, and without an origin there is nothing to be evidence of |

## 4. Honest limits

- The sample is **2020** and **five sections**. It shows how Infosys *writes* questions. It does not show how many of each the 2027-batch test contains. Section counts still rest on the 2025 accounts (see `03-pattern-synthesis.md` §1 and §8).
- 21 of the 54 sample answers are judgement (verbal, units), not execution. Two items cannot be answered without a key that is not published.
- I read the four aggregator pages through a fetch tool that returns a summary of the page, not its raw HTML. Their question counts, dates and publisher names are what that tool reported; the page text itself was not archived. That is one more reason none of them were imported.
- A newer official sample, a dated slot-wise paper, or a first-hand account that quotes questions would change these verdicts. None was found as of 2026-10-01.

## 5. How to judge a new source (for the next one you find)

1. Find the publisher and what they sell.
2. Look for a sentence saying where the questions came from. If there is none, stop: treat it as practice material at best.
3. Check it names **Systems Engineer** and Infosys Limited, and a date within the last 18 months.
4. Check it does not contradict first-hand accounts (no coding, about two hours, seven sections).
5. Re-solve every answer by running code or a second method before trusting the key.

---

## 6. Pass 5 — Reddit and the tools around it (2026-10-03)

Method and findings: `07-reddit-arctic-shift.md`. Verdicts below follow the same tests as §1.

| Source | What I observed | Verdict |
|---|---|---|
| **Arctic Shift** (`github.com/ArthurHeitmann/arctic_shift`, API at `arctic-shift.photon-reddit.com`) | README and API docs read as raw files. One individual maintainer; created Aug 2023, last push 12 Sep 2026; **no licence file** (GitHub reports none; `/LICENSE` is 404). Data comes from the official Reddit API; removal requests honoured; no API key; dynamic rate limit (429); keyword search needs a subreddit or author filter and times out on very active subreddits (observed: r/developersIndia and r/Btechtards). "No uptime or performance guarantees" | **B. Used as a read-only archive**, slowly and sequentially. No usernames requested or stored. Raw posts kept outside the library and not redistributed. Findings paraphrased and aggregated |
| **Reddit communities** r/Infosys, r/infosysmysore, r/Infosys_DSE_2026, r/PlacementsPrep | 28,000 posts pulled, about 40 comment threads read. Anonymous, self-selected, unverifiable. r/Infosys is mostly joiners and DSE/SP candidates; first-hand SE test content is scarce | **C for any single claim; `[LIKELY]` only where three or more separate threads agree.** Never used for numbers |
| **Storyboard18**, "Infosys defers hiring assessments for 20,000 candidates…" | Raw page read. Dated 10 Jun 2026; cites the Times of India; names Specialist Programmer (Trainee) and Digital Specialist Engineer (Trainee); Systems Engineer is not mentioned | **B. Used** for the June 2026 pause. The original Times of India article was not opened |
| **HRKatha**, "Infosys delays hiring exams for 20,000 candidates…" | Raw page read. Dated 10 Jun 2026; same facts; names no roles | **B. Used** as the second outlet |
| **NIST SP 800-145**, "The NIST Definition of Cloud Computing" | 5-page PDF from `nvlpubs.nist.gov`, September 2011, read in full. First-party standards body. Three service models, four deployment models | **A. Used** for the cloud quick answers in `interview/00-INTERVIEW-FORMAT.md` §7. Note it is from 2011 |
| **IBM Think**, "What is the OSI model?" | Raw page read. Published 7 Aug 2024, modified 17 Nov 2025; vendor explainer; seven layers named and described | **B. Used** for the layer list. The ISO standard was not read |
| Cloudflare Learning Centre (OSI) | Returned a bot-check page ("Just a moment…") | **Not used.** I did not try to get past the check |
| Cisco Support (OSI) | Returned HTTP 403 | **Not used** |
| The web-search tool on `reddit.com` | The tool refused the domain | **Nothing to assess.** Reddit threads were reached through Arctic Shift, not through search |

