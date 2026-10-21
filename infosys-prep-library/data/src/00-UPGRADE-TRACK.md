# The Upgrade Track (DSE and SP) — what candidates report

**As of 2026-10-03.** This is a **different test from the Systems Engineer (SE) test** this library prepares you for. It is a coding assessment for the Digital Specialist Engineer (DSE) and Specialist Programmer (SP) roles. It is optional for an SE candidate. This file only tells you what recent candidates say, so you can decide whether to try it.

Source: Reddit, read through Arctic Shift (method, counts and limits: `../research/07-reddit-arctic-shift.md`). Everything is `[REPORTED]` unless the line says otherwise.

## 1. What is official

| Fact | Tag |
|---|---|
| SE candidates who clear the test and interview can sit an optional extra programming test and an in-person interview for DSE (Rs 6.25 LPA) or SP (Rs 9.5 LPA). It has no effect on the initial SE offer | `[CONFIRMED — official placement-cell notice]` (see `00-INFOSYS-SPECIFIC.md`) |
| On **10 June 2026** Infosys deferred its hiring assessments for **Specialist Programmer (Trainee) and Digital Specialist Engineer (Trainee)** candidates, over 20,000 people, after detecting impersonation and malpractice. It said a revised timeline would follow. The reports do not mention Systems Engineer | `[CONFIRMED]` as news reporting: Storyboard18 (citing the Times of India) and HRKatha, both dated 10 June 2026 and both read in full. The original Times of India article was not opened |

## 2. What the tests look like after the pause

Reported by many separate posters in Aug–Sep 2026 about the DSE/SP tests (not SE):

| Stage | What they say | Tag |
|---|---|---|
| Online or on-campus assessment | Four coding problems, graded easy, medium, hard and "complex". Problems are scored by hidden test cases, and many posters report 12 per problem. One poster says candidates in the same hall get different sets | `[LIKELY]` for the structure |
| How much you must solve | Posters say solving one problem fully was enough for an interview call for DSE or L1, and about three for the L2/L3 interviews. Nobody can verify this | `[REPORTED]` |
| Kinds of problems named | A greedy problem told as a long story; dynamic programming combined with another idea; counting numbers in a range by a digit rule; a longest-increasing-subsequence variant with a budget; a string cut where two letter-weights balance | `[REPORTED]` |
| Proctoring | Fully proctored. One poster says a proctor scans a QR code from your screen before the test starts | `[REPORTED]` |
| In-person coding round | Several off-campus candidates describe an in-person round on 5–6 September, introduced, in one poster's words, because of the cheating cases | `[REPORTED]` |
| Interview, the coding part | Two coding problems on the Wingspan portal; you solve one in about 30 minutes, although the portal's own timer shows 45. The interviewer then asks for your approach, edge cases and complexity. Problem types named: sorting with two pointers, greedy pairing, a sliding window, XOR conditions, a variation of Kadane's algorithm | `[LIKELY]` |
| Interview, the rest | Projects (architecture, REST API, how you would scale it); SQL (types of joins, writing an inner join, second-highest salary); OOP; DBMS; OS (race condition, semaphore, the four deadlock conditions); TCP versus UDP; Dijkstra and Bellman-Ford; time complexity of trees and BSTs; in some accounts AI/ML (RAG, embeddings, vector databases, backpropagation); sometimes a design question, for example an extensible payment system | `[LIKELY]` for the areas, `[REPORTED]` for each question |
| Interview, how it is scored | One poster saw the interviewer's sheet with six columns: problem solving, operating systems, DBMS, computer networks, programming language, projects. The same poster was told, roughly, that about 70% of test cases is the bar, and says they are not sure | `[REPORTED]`, single source |
| Size and length | One centre: about 525 candidates in the assessment and about 90 at the interview. Interviews ranged from about 45 minutes to about two hours | `[REPORTED]` |
| Which role you get | Decided by the test score together with the interview. Posters are unsure how, and one was told this cycle "mainly hires for L1 and DSE" | `[REPORTED]` |

## 3. How often topics appear in these accounts

I read 267 posts that look like first-hand DSE, SP or HackWithInfy accounts (Sep 2025 to Oct 2026; 142 of them from Sep 2026). **The table counts how many accounts mention a topic. It is not how often the topic is asked.** Keyword matching was used, so treat the percentages as rough.

| Topic | Mentioned in | Topic | Mentioned in |
|---|---|---|---|
| Coding problems (test or live) | 85% | OS | 23% |
| Projects and resume | 64% | AI / ML / GenAI | 19% |
| SQL | 48% | Computer networks | 18% |
| OOP | 27% | System design / patterns | 17% |
| DBMS | 23% | Dynamic programming | 15% |

Graphs appear in about 11% of the accounts, trees in 7% and greedy in 7%, so DP is named more than any other single algorithm family. **SQL in nearly half the accounts is the surprise:** it is cheap to prepare and you may already know it.

## 4. Where the sources disagree

- **Online or offline?** Some SE-selected candidates say the upgrade test is in the college with strict invigilation; others say it was online like HackWithInfy; one poster says the SE-upgrade hiring "has now been stopped". Timing is also unclear: "November" for some colleges, "after training" for others.
- **Risk to the SE offer.** Two commenters warn that sitting the SP/DSE test while holding an SE offer can get the SE offer revoked or close other roles. Nobody quotes an official source. **Check the official email or ask your placement officer before you sit it.**

## 5. If you want to try (`[INFERRED]`)

1. Do the SE test first. It is the filter for everything else, and this track does not replace it.
2. This library has no practice banks for the coding track. The Java problem patterns that help are in the Accenture coding library you already have.
3. Rough order by what the accounts mention: arrays and strings; one pass of dynamic-programming basics; SQL joins and group by; OOP and DBMS fundamentals; one clear explanation of each project.
4. Hard problems in these accounts were described as dynamic programming plus something else. Nothing here shows how many candidates solve them.

## 6. Evidence and limits

- Test and interview accounts read in full: r/Infosys `1w2fqa3`, `1wthk77`, `1vxzqoh`, `1vxzwhf`, `1vu3jat`, `1wcg4bi`, `1wcryxe`, `1web12n`, `1wm9rfa`. Counts come from 267 first-hand-looking posts in r/Infosys, r/Infosys_DSE_2026 and r/PlacementsPrep. Problem statements are described by type only, not reproduced.
- Upgrade-test remarks by SE candidates: r/PlacementsPrep `1ogb23w`, `1osk3lc`; r/Infosys `1uu64li`, `1vcg4yj`, `1v46h6o`.
- Reddit is anonymous and self-selected. People who did well and people who were rejected both post, but the rejected may post more. The 2027 on-campus SE drive had not started on most campuses when this was written.
