# Reddit research through Arctic Shift

**Pulled 2026-10-02 to 2026-10-03.** Everything here is `[REPORTED]` unless the line says otherwise. Reddit posts are anonymous and unverifiable, so they never reach `[CONFIRMED]` on their own. A claim is marked `[LIKELY]` only when three or more separate threads, from different dates and different colleges, say the same thing.

**Privacy.** The `author` field was never requested, so no username was stored. The raw posts stay in a session scratchpad outside this library and are not redistributed. Findings below are paraphrased and aggregated. Thread IDs are public Reddit post IDs, given so that a claim can be re-checked by hand.

---

## 1. The tool: what Arctic Shift is (observed, not assumed)

| Question | What I observed |
|---|---|
| What is it | A free archive and API for Reddit data: dumps, a search API and a web UI (`arctic-shift.photon-reddit.com`). README: "Making Reddit data accessible to researchers, moderators and everyone else" |
| Who | One individual maintainer (GitHub user `ArthurHeitmann`). Repo created 2023-08-03, last push 2026-09-12, about 1.6k stars, not archived |
| Licence | **None.** GitHub reports no licence and `/LICENSE` returns 404. The code may be read and run, but there is no stated right to copy or redistribute the repository. The data is Reddit users' content, so I used it for private reading and aggregate counts only |
| Where the data comes from | The official Reddit API. Private and quarantined communities are excluded. Posts are archived when posted and updated about 36 hours later (`file_content_explanations.md`) |
| Access | No key. Dynamic rate limit; HTTP 429 with `X-RateLimit-Reset` when exceeded. The docs say: for massive volumes, use the dumps |
| Hard limit | Keyword search on posts and comments only works together with a `subreddit` or `author` filter, and "is not supported with very active users or subreddits" |
| Reliability claim | "No uptime or performance guarantees" (API README) |
| Removal | The maintainer honours removal requests, so the archive is incomplete by design |

**Verdict.** Usable as a read-only research archive, with these cautions: it is one person's free service, the data can be incomplete, and it carries no licence. I used the API only for slow, sequential reads, and backed off when it returned 429.

**Observed behaviour.** Small and medium subreddits could be paged without a keyword filter. A keyword search in r/developersIndia (1.17M members) timed out even for a one-week window, and so did r/Btechtards (186k). After roughly 28,000 rows I hit the rate limit for about two minutes and paused.

---

## 2. What was collected

| Community | Posts pulled | Notes |
|---|---|---|
| r/Infosys | 8,466 (8,406 of them since 2025-11-01) | Whole subreddit, 2018 to 2026-10-02. Mostly employees, joiners and DSE/SP candidates |
| r/infosysmysore | 1,348 | Training-campus community, from 2025-11 |
| r/Infosys_DSE_2026 | 197 | DSE joiners, from 2026-05 |
| r/PlacementsPrep | 18,386 (938 mention Infosys) | General placements; the main source of first-hand SE accounts (Sep 2025 to Jan 2026) |
| r/infosys_offcampus2026, r/placementOA, r/Infosys_Tales | 1, 2, 5 | Effectively empty |
| **Not reached** | r/developersIndia, r/Btechtards | Keyword search times out; bulk coverage would need the multi-GB dumps, which I did not download |

Comment threads were fetched for about 40 selected posts only. Counts about "how many posts" cover posts (title and body), not comments.

---

## 3. Findings

### F1. The 2027-batch Systems Engineer test: still nobody has reported it
Two posts from 18 and 26 Sep 2026 (r/Infosys `1wjvzja`, `1wqs2sr`) ask exactly what this library tries to answer: the exam pattern for the 2026-27 SE drive, and previous questions. Neither has a substantive answer. A third (`1wvkrsi`, 2 Oct) asks which aptitude videos to use. No 2027-batch SE test report was found in the four communities searched, which agrees with the library's standing note that none exists (as of 2026-10-03). Absence from these archives is not proof that none exists.

### F2. What the Oct 2025 to Jan 2026 SE test and interview accounts say
r/PlacementsPrep, mostly single comments under candidates' questions: about ten comments and posts across ten threads, each one poster's word.


| Item | Reported | Where |
|---|---|---|
| Difficulty of the written test | "very easy" / "easy level" (3 separate posters) | PP `1o7s41n`, `1ofrcxs`, `1mnhd9r` |
| Sections named | Simple aptitude, simple English, simple puzzles, a last section that is an essay; or logical reasoning, essay writing, numerical ability, technical ability | PP `1o7s41n`, `1ofrcxs` |
| Topics named by one commenter | Puzzles, boats and streams, statement and conclusion, data interpretation, syllogism, ranking, arrangement | PP `1nzmoxe` |
| Sectional cut-off | Two separate posters say puzzles (and pseudocode) are where people fail on the sectional cut-off; one is second-hand, about a friend | PP `1oe8tjb`, `1ojbogx` |
| Shortlisting ratios, per campus | 58 of the test-qualifiers shortlisted for interview and 50 selected; 386 of 530 shortlisted. Single-campus anecdotes | PP `1oe8tjb` |
| Timeline | Test and interviews on consecutive days; result announced the same day (two separate campuses). One off-campus drive: test 11 Oct, interview 12 Oct, selection mail 7 Nov | PP `1p1zwxi`; r/Infosys `1pduj7h` |
| Interview, length and mode | About 20 minutes, offline | PP `1oe8tjb`, `1qog301` |
| Interview, content | Mostly resume and projects; hobbies; one easy DSA concept; DBMS clauses; SDLC; inheritance; C versus C++; cloud basics (public, private, hybrid; IaaS, PaaS, SaaS); OSI layers; "latest movie you watched"; "are you willing to relocate"; "what do you know about Infosys" | PP `1o1hhaz`, `1oe8tjb`, `1qog301` |
| Interview, outcome | Described as easy by 4 separate posters. One poster says an interview that went well still ended in rejection, so it is not purely a formality | same |

**Reading.** This matches the library's existing model: the sections, "puzzles and pseudocode have sectional cut-offs", and "interview mostly resume, OOP, DBMS, SDLC and HR". It adds: cloud basics and OSI layers as occasional interview questions (each appears in one account); relocation as a standard HR question; and "statement and conclusion" and "ranking" as topic mentions with a single source. The official 2020 sample contains neither of those two types.

### F3. Offer letters, joining dates and portal status: the biggest practical finding
In r/Infosys, 331 SE-flavoured posts exist since 2025-11. Of those, 167 are about offer letters, joining dates or portal status, and 126 use waiting or delay wording. The monthly count of such posts grows from 2 or 3 per month in late 2025 to 29 in August 2026. Typical reports:

- People selected in Oct to Nov 2025 were still without an offer letter in Aug to Sep 2026, about ten months later (e.g. `1vuj8dz`, `1w0qqot`, `1vldv9c`); a few received it in early Sep 2026 (`1w64khq`, `1w6afhl`).
- The careers portal shows "To be interviewed" or "Decision pending" for months after selection; offer letters arrive in tranches (`1vhw03y`, `1wbacu5`).
- Joining dates reported for the Oct to Nov 2025 cohort range from February 2026 to November 2026 (e.g. 5 Oct `1w6w2n9`, 28 Sep `1vlu93u`, 23 Nov PP `1wdn4tl`).
- Some posters report being told the offer letter arrives "about 2 to 3 weeks before joining" (`1w0qqot`); others were told it comes after the final semester, about a month before joining (PP `1oxqprz`).

`[LIKELY]` for "offer letters and joining dates for SE selections are slow and uneven" (well over three separate threads, many colleges, spanning ten months). The reason is `[REPORTED]` only: posters quote "business requirements" from an automated reply.

### F4. After selection: Mysore training, the pre-test and FA1/FA2
Sources: a long first-hand guide by a joiner (r/Infosys `1wk28ot`, 18 Sep 2026, 112 comments) plus about a dozen question threads in r/infosysmysore.

| Item | Reported | Strength |
|---|---|---|
| Pre-test, timing | Within the first week | guide + 1 comment |
| Pre-test, content | Objective. Basic vocabulary/English, aptitude and basic maths, logical reasoning, Java fundamentals and Java output questions, DBMS and SQL, OOP. No negative marking (one poster) | **3 separate posters agree on the shape** |
| Pre-test, purpose | A score above 65% lets you pick your stream; otherwise streams are allotted | **guide + a second poster** |
| Generic training | Phase 1: Java, OOP, DSA. Phase 2: SQL (the guide writes "HSQL") | guide |
| FA1 / FA2 | FA1: Java, OOP, DSA. FA2: SQL. Pass mark 65% in each; objective part 40%, hands-on coding 60%; up to three retests | guide only |
| Difficulty | "moderate"; "basic coding is enough"; multiple attempts; one joiner failed the generic exam twice. Opinions are anecdotal | 3 separate posters |
| Pay during training | Guide says about ₹17,000; a reply says ₹15,000; another post says ₹16k. **Disputed** | disputed |
| Score-linked monthly incentive | Guide lists tiers from ₹1,250 up to ₹5,000 by score; a reply says there is no one-time bonus and that failing once leaves only the two lowest tiers; an Instagram-reel version quoted different figures that nobody could confirm | **disputed; do not rely on any figure** |

`[REPORTED]` throughout. Not corroborated by any official source I could read. Whether Hari's 2027 cohort follows the same structure is `[INFERRED]`.

### F5. The upgrade route (DSE 6.25 L / SP 9.5 L) and the June 2026 pause
- Three commenters say the upgrade test is offline in the college with strict invigilation, covers harder data structures (DP, graphs, trees) and is followed by a technical interview `[REPORTED]` (PP `1ogb23w`, `1osk3lc`). Another says the upgrade tests come after training, and one poster writes that the upgrade hiring process "has now been stopped" (r/Infosys `1uu64li`). The sources disagree.
- A Reddit-shared news item is confirmed against two outlets: on **10 June 2026**, Infosys deferred its SP and DSE trainee hiring assessments for over 20,000 candidates after impersonation and malpractice were detected. Storyboard18 (citing the Times of India) names the two roles and does not mention Systems Engineer; HRKatha gives the same date and facts without naming roles. `[CONFIRMED]` as news reporting; the original TOI article was not opened.
- Two commenters warn that an SE offer may be revoked, or other roles closed to you, if you sit the SP/DSE test while holding it (r/Infosys `1vcg4yj`, `1v46h6o`). This is hearsay and could not be confirmed.

### F6. What DSE/SP candidates report (a different role, but the upgrade route)
I read 267 posts that look like first-hand DSE, SP or HackWithInfy accounts (since Sep 2025; 142 of them from Sep 2026). **The counts below are "mentioned in N of 267 accounts", not how often each topic is asked.**

| Topic | Mentioned in | | Topic | Mentioned in |
|---|---|---|---|---|
| Coding problems in a test or live | 229 (85%) | | OS | 62 (23%) |
| Projects and resume | 173 (64%) | | AI / ML / GenAI | 53 (19%) |
| SQL | 130 (48%) | | Computer networks | 49 (18%) |
| OOP | 74 (27%) | | System design / patterns | 48 (17%) |
| DBMS | 63 (23%) | | Dynamic programming | 42 (15%) |

Recent on-campus drives (Aug to Sep 2026), reported by many separate posters: an online assessment of four coding problems (easy, medium, hard, "complex"); solving even one fully was said to be enough for an interview call; an interview with a "solve one of two problems in 30 minutes" step on the Wingspan platform, then DSA, OOP, DBMS, SQL, OS and networks; some off-campus drives added an in-person coding round. These are `[LIKELY]` for the shape and `[REPORTED]` for the numbers. All of it concerns SP/DSE, not the 3.6 LPA Systems Engineer test, and it contradicts nothing in the library.

### F7. Things that look like findings but are not
- Most posts mentioning "SE" or "aptitude" are joiners asking about letters, joining and accommodation. They contain no test content.
- A few posts tagged SE are really about the DSE/SP coding test (e.g. `1vu3jat`, `1v46h6o`). They were separated out and not counted as SE test evidence.
- Hearsay such as "75% cut-off" or "7 LPA after training" stays out of the library.

---

## 4. What this changes and does not change

| Area | Verdict |
|---|---|
| Test tiers and section weights | **No change.** Reddit agrees with the model, adds no new numbers, and the sample is too thin to move a tier |
| "Puzzles and pseudocode matter most for the cut-off" | Slightly stronger: two separate posters now say it (was: derived from the sectional-cut-off rule alone) |
| Interview pages | **Added** (done 2026-10-03): a section in `interview/00-INTERVIEW-FORMAT.md` listing the three first-hand Reddit accounts beside the five vetted ones (kept out of the B1–B5 tallies), and quick answers on cloud models and the OSI layers. Relocation was already in the library (I21 and the IV5 drills); "what do you know about Infosys" points to `00-INFOSYS-SPECIFIC.md` |
| Statement-and-conclusion, ranking | One mention, not in the official sample. Optional short note, not a lesson |
| After-selection material (offer-letter reality, Mysore pre-test, FA1/FA2, pass marks) | **Added**: `interview/00-AFTER-SELECTION.md`. The library had nothing on this |
| DSE/SP upgrade | **Added**: `interview/00-UPGRADE-TRACK.md`, a digest clearly separate from the SE test. No practice banks were built for it |
| Core Course lessons | **No lesson changed.** `00-START-HERE.md` gained one paragraph on what Reddit says and an "After the test" pointer |

## 5. Limits

1. Reddit is self-selected and anonymous. Easy tests are reported by people who passed; people who failed post less.
2. The strongest SE-test evidence is single comments from Sep to Nov 2025 drives. No 2027-batch SE test report exists in the archive.
3. The two biggest Indian tech communities could not be searched; they may hold SE test accounts I did not see.
4. Comments were read for about 40 threads only; most threads were read at the post level.
5. Keyword counts overcount where a word has other meanings. A first pass inflated OS, SQL and networks ("process", "query", "join" in the sense of joining the company), so I tightened the patterns and quote the strict counts as order of magnitude only.
6. Pay and incentive figures are disputed in the replies. None is used in the library.
