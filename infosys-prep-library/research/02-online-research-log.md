# 02 — Online Research Log

Every URL consulted, with date, **entity**, **role** and credibility. Entity and role filters were applied before reading. Pass 1 ran 22 searches on 2026-09-25.

**Credibility scale.** A = official Infosys document or college placement-cell notice. B = first-hand candidate account with a dated test. C = aggregator/coaching page that cites a specific drive or year. D = undated aggregator, SEO page, or video title only. X = excluded by the entity or role filter.

**Access method.** Scribd documents are not readable by plain fetch; page text was pulled from Scribd's own page-render files with `scratchpad/scribd.py` (the same text a browser renders). Naukri Code360 blocks automation (403); read through the built-in browser.

---

## 1. Official and placement-cell documents (A)

| # | URL | Date | Entity | Role | What it establishes |
|---|---|---|---|---|---|
| A1 | scribd.com/document/922881725 ("Infosys Campus Recruitment 2026 Criteria") | 2026 batch (upload 2025) | Infosys Ltd | All campus roles | Official **Guidelines for Infosys Assessment**: test in **college labs**, on `rec-test.infosys.com`, Chrome/Edge, **proctored in person**, **no calculators or phones**, **stationery allowed**, **15-minute login window**, switching windows auto-tracked. "Behavioral guidelines" = conduct rules, not an assessment |
| A2 | scribd.com/document/950564465 ("Infosys Eligibility Guidelines Instructions Job Details 2026") | 2026 cycle | Infosys Ltd | SP L1/L3 JD + same guidelines as A1 | Same assessment guidelines verbatim as A1. SP selection: "internet-based programming ability test (3 questions, 180 minutes)" + 60-min technical interview. SP L3 = Rs 21 L, L1 = Rs 10 L |
| A3 | scribd.com/document/917202724 (KIIT T&P notice) | **12 Sep 2025** | Infosys Ltd | **Systems Engineer (Trainee)**, Rs 3.60 LPA | Process: registration → **Online Test → Interviews (Tech + HR)**. "Kindly provide personal email addresses only". **Upgrade: "Candidates who clear the test and interview for the Systems Engineer (Trainee) role will also get a chance to upgrade their offer to Digital Specialist Engineer (Trainee) (6.25 LPA) and Specialist Programmer (Trainee) (9.5 LPA) through an additional round of programming test and in-person interview. This is optional and will have no impact on their initial offer."** Drive conducted "at KIIT Campus physically" |
| A4 | scribd.com/document/1061349810 (ITM notice) | 01 Jul 2026 | Infosys Ltd | SP L1/L2/L3, DSE — **not SE** | 2027-batch SP/DSE drive: 3 questions / 180 min programming test + 60-min interview. Role filter: evidence about the upgrade test only |
| A5 | adgips.ac.in/infosys-campus-recruitment-program-2027/ | 2026 | Infosys Ltd | SP/DSE | 2027 SP L3 21 L, L2 16 L, L1 10 L + 1 L bonus, DSE 6.25 L + 75k bonus. No SE. Role filter: upgrade context only |
| A6 | studocu.com/…/141229249 ("INFOSYS RECRUITMENT ELIGIBILITY & INSTRUCTIONS 2026 Batch") | 2026 batch | Infosys Ltd | — | **Unreadable** (Studocu preview shows no document text). Not used |

## 2. First-hand candidate accounts (B)

| # | URL | Test date | Entity | Role | Mode | Key content |
|---|---|---|---|---|---|---|
| B1 | naukri.com/code360/…/interview-experience-by-shivam-krishna-srivastava-on-campus-nov-2025 | **12 May 2025** | Infosys (India) | SE, 3.6 LPA | On campus | **60 Q / 120 min**: Logical 15/25m, Technical Ability 10/35m, Verbal 20/20m, Pseudocode 5/10m, Puzzle 4/10m, Grammar 5/10m, Writing 1/10m. **Sectional, sequential, no revisiting.** Essay: "Ozone layer depletion". Interview 15 min: SDLC, Waterfall vs Agile, 4 OOP pillars, Java access specifiers. SE clearance required to sit the SP/DSE upgrade test |
| B2 | geeksforgeeks.org/interview-experiences/infosys-interview-experience-for-system-engineer-2025/ | 10 Jan 2025 (posted 19 Feb 2025) | Infosys | SE | On campus, UIT-RGPV Bhopal | 2 h, "offline, computer-based", **7 sections, individual cut-offs**: logical, DI, English grammar & writing, maths, pseudocode. No coding. Interview 20-25 min: rejections, time management, project, CGPA decline, SDLC, Scrum Master, sprint planning. "only 5% of people cleared the assessment" |
| B3 | naukri.com/code360/…/infosys-technologies-limited/interview-experience-on-campus-dec-2025 | **3 Dec 2025** | Infosys | SE, 3.6 LPA | On campus, college labs | 120 min MCQ: aptitude, logical, basic CS. Interview next day, 20-30 min: overloading vs overriding, SDLC models |
| B4 | naukri.com/code360/…/infosys-interview-experience-by-priyanshu-agarwal-on-campus-dec-2024 | 17 Dec 2024 | Infosys | SE, 3.6 LPA | On campus | 120 min, **7 sections**: quant, logical ability, logical reasoning, pattern solving, code debugging, English comprehension. Interview 20 Jan 2025, 15 min: SDLC, joins. Application form from Infosys took ~15 min |

## 3. Aggregator and coaching sources (C/D)

| # | URL | Date | Role | Pattern claimed | Cred |
|---|---|---|---|---|---|
| C1 | scribd.com/document/915628705 ("On Campus Hiring 2025", SE 3.6 LPA) | 2025 | SE | **7 sections, 60 Q, 120 min** with marks: Reasoning 15Q/15M/25m; Technical Ability (maths+logical) 10Q/10M/35m; Verbal 20Q/20M/20m; Pseudocode 5Q/**10M**/10m; Numerical Puzzle 4Q/**10M**/10m ("grid number based puzzles"); English Grammar 5Q/**10M**/10m ("cloze test based"); English Written 1Q/NA/10m ("general topic") | C |
| C2 | scribd.com/document/854200739 ("Infosys Recruitment Process and Exam Pattern 2025") | 2025 | SE | Same 7-section 60/120 split as C1 | C |
| C3 | scribd.com/document/690495443 (cites freshers-job.com 2021) | 2021 | SE | **Older 5-section** pattern: 54 Q / 100 min (LR 15/25, Math 10/35, Verbal 20/20, Pseudocode 5/10, Puzzle 4/10) | D (stale) |
| C4 | scribd.com/document/820309657 ("Infosys Pattern 2025") | 2025 | unclear | 67 Q incl. 2 coding / 120 min, verbal 40 Q | D — contradicts every first-hand account; likely SP/DSE or invented |
| C5 | faceprep.in, placementpreparation.io, prepinsta.com, careerrisehub.com, campusmonk.in, assessfy.com, knoffcampusjobs.com | 2025-26 | SE | Mostly 5-section 54 Q / 100 min; some add Grammar + Writing | D |
| C6 | unstop.com/blog/infosys-recruitment-process; claveprep.com | 2026 | mixed SE/SP | "~3-hour" assessment — conflates SP/DSE test | D |
| C7 | knoffcampusjobs / "papersadda" / search snippet: "180 minutes, 65-70 questions, 2 coding" | 2025 | mixed | Conflates SE with SP | D |

## 4. Excluded by filter (X)

| URL | Reason |
|---|---|
| YouTube "Infosys Systems Engineer Hiring | Edgverve Hiring" | EdgeVerve is a different entity |
| infosys.com HackWithInfy pages, MSIT HackWithInfy report, papersadda HackWithInfy 2026 | HackWithInfy: different programme, SP/DSE |
| sakshi "Systems Engineer for female candidates Rs 9.5 LPA" | Different track (SE Specialist / women-only off-campus) |
| GfG "Infosys SP & DSE 2026" | Role filter: SP/DSE |
| offcampusjobs4u / freshershunt SP drives | Role filter: SP/DSE off-campus |

## 5. Video sources found in Pass 1 (titles; the SE ones were transcribed in Pass 2, §6)

| URL | Date signal | Role | Note |
|---|---|---|---|
| youtube.com/watch?v=r1m-dYWM8l4 "Infosys System Engineer Exam Pattern 2027 — New Pattern" | 2026 | SE | Title claims a new 2027 pattern |
| youtube.com/watch?v=4iOgsXNEKQ4 "Infosys Superset System Engineer Hiring 2027 — New Exam Date — New Exam Pattern" | 2026 | SE | Superset = placement platform |
| youtube.com/watch?v=20nIZyNAP3w "Infosys New Exam Date 01/08/2026 — SE or SP/DSE" | Aug 2026 | SE/SP | |
| youtube.com/watch?v=LuI44614h-s "Infosys 2027 Batch On Campus — Exam in August — Gen AI Project Students" | 2026 | SE? | "Gen AI project" claim unverified |
| youtube.com/watch?v=U7hkPOKo69o "Infosys System Engineer 2027 — 1-SHOT PYQ" | 2026 | SE | Coaching PYQ |

## 6. Pass 2 — video transcripts read (auto-captions, 2026-09-25)

Captions were pulled through the built-in browser (the page's own signed caption request) and saved as `scratchpad/tr-<id>.txt`. Question extraction from the transcripts was drafted by DeepSeek V4.1 Flash (`ds.py`, 12 jobs) and **every item was then re-read against the raw transcript and re-solved by hand and by `data/verify_observed.py`**.

| ID | URL | Published | Channel | Role | Claim | Items kept | Cred |
|---|---|---|---|---|---|---|---|
| V3 / YT-5XTG | youtube.com/watch?v=5XTGOVtBkiw | 2025-10-09 | OnlineStudy4u | SE | Candidate recall of early-Oct 2025 slots, **shift-tagged**; "many failed the cut-off on puzzle and verbal"; 3×3 and 4×4 matrix puzzles | 9 | C |
| YT-2NTB | youtube.com/watch?v=2ntBG9N_8Kk | 2025-09-29 | Placement Walaa | SE | "asked in recent Infosys examination"; "this year more DI questions" | 11 | C |
| YT-2YHL | youtube.com/watch?v=2yhl7EzbY2Q | 2025-09-25 | OnlineStudy4u | SE | "Infosys PYQ"; exams 4-5 Oct 2025 announced | 12 | C |
| V2 / YT-U7HK | youtube.com/watch?v=U7hkPOKo69o | 2026-09-18 | OnlineStudy4u | SE (2027 batch) | PYQ from "4th, 11th, 16th October 2025"; exam expected end-Sep / early-Oct 2026 | 8 new | C |
| V5 / YT-2MBO | youtube.com/watch?v=2mbo13B9QWU | 2026-09-22 | OnlineStudy4u | SE | "questions are one or two years old because the recent campus exam did not happen" | 9 | C |
| YT-6UFT | youtube.com/watch?v=6uftMFrZdzc | 2025-09-27 | OnlineStudy4u | SE | "Infosys previous year puzzles" | 5 | C |
| YT-HZGK | youtube.com/watch?v=HZGkyKYqSA0 | 2024-12-18 | Code Bashers | SE | "latest pseudo code questions asked in SE hiring" | 6 | C |
| V4 / YT-KC2G | youtube.com/watch?v=Kc2gqLaBVsE | 2024-11-04 | Tekno UF | SE | candidate reports from the 3 Nov 2024 exam; "once submitted or skipped cannot be attempted" | 4 | C |
| V1 | youtube.com/watch?v=r1m-dYWM8l4 | 2026-09-20 | Online Learning | SE (2027 batch) | relays the 2027 notice: "3.6 LPA in-person campus recruitment … technical plus behavioral assessment"; 7-section pattern "as of Oct 2025" | pattern only | C |

## 7. Pass 3 — gap-filling

| # | URL | Date | Entity | Role | Closes thread |
|---|---|---|---|---|---|
| B5 | geeksforgeeks.org/interview-experiences/infosys-interview-experience-for-system-engineer-1/ | Jan 2025 (posted 24 Jun 2025) | Infosys Ltd | SE | A (navigation conflict), D, F: GenAI opinion + daily AI use asked in HR; offered DSE/SP upgrade interviews |
| B6 | geeksforgeeks.org/interview-experiences/infosys-interview-experience-campus-system-engineer/ | undated | Infosys Ltd | SE | Stale pattern (35 min, 20 + 40); interview: SQL top-3, normal forms |
| DSE-J25 | naukri.com/code360/interview-experiences/infosys/infosys-interview-experience-on-campus-jun-2025 | 22 Jun 2025 | Infosys | **DSE** (6.25 L) | E: 180-min, 3-problem test; interview with 45-min live coding |
| OL-25 | scribd.com/document/884645375 (SE Trainee offer letter) | 4 Jul 2025 | Infosys Ltd | SE Trainee | F: Mysore location, 18-month probation, Rs 1,00,000 early-exit compensation, Rs 25,000/month gross first 6 months. **Personal details in the letter are not reproduced** |
| GEC | infosys.com/careers/graduates/global-education-center.html; hechingerreport.org | — | Infosys Ltd | all | F: residential training at Mysuru, 19-23 weeks reported |
| TCS-450 | `tcs_new/_analysis/text2/TCS_TCS_ninja_450_Infosys_Puzzles.pdf.txt` (local) | pre-2015 | — | — | **Not used**: classic brain-teasers, not the grid-number type confirmed for 2025-26 |

**Stop rule.** The last three sources (B6, the offer-letter search, the GEC search) added only Infosys-specific joining terms and nothing new about the test. Research stopped there.

## 9. Pass 4 — previous-year question sources (2026-10-01)

Question asked: is there trustworthy previous-year Systems Engineer question text anywhere (websites, GitHub)? Every source was analysed before use; verdicts and reasons are in `research/05-source-credibility.md`.

| # | URL | Date | Entity | Role | Verdict |
|---|---|---|---|---|---|
| A7 | infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf | 2020-09-22 (PDF metadata) | Infosys Ltd (certificate holder: Infosys Limited, Bengaluru) | Systems Engineer | **A. Used.** 54 questions, 5 sections, 100 minutes, no key. Solved in `question-banks/QB-98-OFFICIAL-SAMPLE-SOLVED.md` |
| B7 | geeksforgeeks.org/interview-experiences/infosys-interview-experience-for-system-engineer-10/ | test 2025-10-13, posted 2026-01-07 | Infosys | SE, 2026 batch | **B. Used** for section names and interview evidence; states 90 minutes (conflict recorded, not adopted); no questions quoted |
| C8 | talentbattle.in … infosys-pseudocode-previous-year-questions | 2024-04-30 | — | — | Not used: no stated origin |
| C9 | prepinsta.com/infosys/pseudo-code-questions-and-answers/ | 2025-07-16 | — | — | Not used: no stated origin; C-style questions |
| C10 | codequotient.com/blog/pseudocode-questions-infosys-drive/ | 2022-08-17 | — | — | Not used: stale, unattributed |
| C11 | placementpapers.app/infosys/2025/ | 2026 | mixed SE/DSE/PP | — | **Rejected:** claims 180 minutes and two coding problems; cites other aggregators |
| X | github.com: Akhilcrab/infosys-prep, ramkumar03ace/infosys-prep, karthikreddy-7/Infosys-SP-Coding-Questions | — | — | SP/DSE | Excluded by role filter (judged from search listing; not opened) |

The four aggregator pages were read through a fetch tool that returns a summary of the page. Nothing from them was imported.

## 8. Totals

| | Count |
|---|---|
| Searches | 36 |
| URLs logged | 65 |
| Survived entity + role filters | 47 |
| Official / placement-cell documents read | 5 (A1-A5), plus the 2020 official sample paper (A7) |
| First-hand candidate accounts | 7 (B1-B7; B6 stale) |
| Video transcripts read | 9 |
| Excluded by filter | 8 (EdgeVerve, HackWithInfy x3, SE-women drive, SP/DSE x2, GitHub SP/DSE repositories) |

## 10. Pass 5 — Reddit through Arctic Shift (2026-10-03)

Asked by Hari: use the open-source Arctic Shift tool to research Reddit for important topics and shared interview experiences, then re-analyse and rebuild. Full record, counts and limits: `07-reddit-arctic-shift.md`. Source verdicts: `05-source-credibility.md` §6.

| Step | What was done |
|---|---|
| Tool vetting | Read the README, API docs and data notes as raw files; checked the licence (none), maintainer, data origin and rate limits; tested the API with small requests |
| Collection | Paged r/Infosys (8,466 posts), r/infosysmysore (1,348), r/Infosys_DSE_2026 (197), r/PlacementsPrep (18,386; 938 mention Infosys), and three tiny communities. The `author` field was never requested |
| Not reachable | r/developersIndia and r/Btechtards: keyword search times out even for one-week windows |
| Reading | Selected threads read in full with comments (about 40), including every SE test, SE interview, pre-test and FA thread found by keyword scans |
| Result | No 2027-batch SE test report exists in these communities. Older SE accounts agree with the library's model. New: cloud and OSI interview questions, the offer-letter delay, the Mysuru pre-test and FA exams, the DSE/SP track and the June 2026 pause |

