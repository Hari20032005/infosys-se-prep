# Interview Format — what is known

**As of 2026-10-03.** Sections 1–5 are built from five first-hand Infosys Systems Engineer interview accounts (Dec 2024 – Dec 2025) and the official Infosys guidelines. Section 6 adds a later Reddit pass (Oct 2025 – Jan 2026); section 7 gives quick answers to two topics it surfaced. No account of a 2026-27 (2027-batch) interview exists yet. Everything below is `[REPORTED]` unless it says otherwise.

## 1. The shape of the round

| Item | Finding | Sources |
|---|---|---|
| Mode | Face to face, on the college campus, after the written test | B1–B5 |
| Panel | One interviewer in the detailed account (“one-to-one”); friendly and supportive | B3 |
| Length | B1: 15 minutes · B4: 15 · B2: 20–25 · B5: 20 · B3: 20–30 (its page shows 39) | B1–B5 |
| Timing after the test | Next day (B1, B3), or some weeks later (B4: test 17 Dec, interview 20 Jan) | B1, B3, B4 |
| Content | SDLC in four of five; OOP in three; joins once; projects in two; HR and behavioural in three | see `data/questions-observed.csv` rows I01–I25 |
| Coding | At most a small program (palindrome) or a SQL query | B5, B6 |
| Outcome | Selection was announced after the interviews; “only 5% cleared the assessment and those who advanced to the interviews mostly got the final selection” | B2 |

## 2. What the official text says about the process

The drive email says the process assesses “**both technical and behavioural competencies**” in person `[CONFIRMED — official]`. A placement-cell notice for the same role (KIIT, 12 Sep 2025) lists the process as **Online Test, then Interviews (Tech + HR)** and states that candidates who clear both “will also get a chance to upgrade their offer” through “an additional round of programming test and in-person interview” `[CONFIRMED — official placement-cell notice]`.

## 3. What to carry (official, for the whole process)

- **Original college ID card and government photo ID**, both, “during the entire process” `[CONFIRMED — official guidelines]`.
- Follow the college dress code `[CONFIRMED — official guidelines]`.
- Resume copies, marksheets and certificates: good practice; one account says the interviewer reviewed certificates at the end `[REPORTED, B6]`.

## 4. How to spend the preparation hours

| Theme | Why | File |
|---|---|---|
| SDLC, Agile, Scrum | 4 of 5 accounts | `IV1-sdlc-agile-testing.md` |
| OOP and Java | 3 of 5 | `IV2-oop-four-pillars.md` |
| HR and behavioural | 3 of 5 | `IV5-hr-and-behavioural.md` |
| Projects and resume | 2 of 5, plus your Springboard link | `IV4-projects-and-resume.md` |
| DBMS and SQL | 1 of 5 (plus the DSE account) | `IV3-dbms-sql.md` |
| Generative AI | 1 of 5, but the drive is framed around AI | `IV6-generative-ai.md` |
| Light coding | 1 of 5 | `IV7-light-coding-in-java.md` |

## 5. If you want the higher roles

The upgrade test is a **programming test of three problems in 180 minutes**, followed by an interview with live coding, for DSE (Rs 6.25 LPA) or Specialist Programmer (Rs 9.5 LPA) `[LIKELY]`. It is optional and does not affect the Systems Engineer offer `[CONFIRMED — official]`. The coding material for it is outside this library's practice banks; the Java problem patterns that help are in the Accenture coding library you already have. What candidates report about it is in `00-UPGRADE-TRACK.md`; what happens after you are selected is in `00-AFTER-SELECTION.md`.

## 6. A later pass: Reddit, October 2025 – January 2026

On 2026-10-03 I read Reddit through Arctic Shift (method, counts and limits: `../research/07-reddit-arctic-shift.md`). In r/PlacementsPrep it found **three first-hand Systems Engineer interview accounts** and about five advice comments from people who had been through it. They are weaker than B1–B5: anonymous, and not checkable. They are **not** counted in the tallies in sections 1 and 4. Everything here is `[REPORTED]`.

| Item | What they say |
|---|---|
| Mode and length | Offline; about 20 minutes |
| Questions named | Self-introduction; hobbies (one interview spent ten minutes on them); the project and its challenges; inheritance; C versus C++; clauses in DBMS; SDLC; cloud basics (public, private, hybrid; IaaS, PaaS, SaaS); the layers of the OSI model; "the latest movie you watched"; "are you willing to relocate?"; "what do you know about Infosys?" |
| Difficulty | Called easy or basic by five posters. Advice repeated: know your resume, expect maybe one easy DSA idea, speak clearly |
| Outcome | Two of the three first-hand accounts were selected. A person whose interview "went very well" was rejected, so it is not a formality |
| Campus tallies | One campus: 58 shortlisted for interview, 50 selected. Another: 386 of 530 shortlisted. Single-campus anecdotes, not rates |
| Pattern on the day | At two campuses the written test and the interviews were on consecutive days, with results the same day |

**What it changes for you.** The plan does not move. The written test is the filter; in the two campus tallies most interviewees were selected, but not all. Two topics are new and cheap to cover: cloud basics and the OSI layers (section 7). The relocation question is already in `IV5` (drill 8), and "what do you know about Infosys?" is answered from `00-INFOSYS-SPECIFIC.md` sections 3 and 5.

## 7. Two occasional topics: quick answers

Each was asked in one account only, so they are low priority. Ten minutes is enough.

### Cloud: models and types

The U.S. standards body NIST defines cloud computing with three *service* models and four *deployment* models (NIST SP 800-145, September 2011, read in full) `[CONFIRMED — NIST]`.

| Service model | What you get | What you manage |
|---|---|---|
| **SaaS** (software) | A finished application, used through a browser or an interface. NIST's own example is web-based email | Only your own settings |
| **PaaS** (platform) | A place to deploy applications you wrote or bought | The application and its settings, but not the servers, operating system or storage |
| **IaaS** (infrastructure) | Processing, storage and networks on which you can run any software | The operating system, your storage and your applications |

| Deployment model | Meaning |
|---|---|
| **Private** | Used by one organisation only |
| **Community** | Used by a specific community of organisations with shared concerns, such as security or compliance rules |
| **Public** | Open to the general public |
| **Hybrid** | Two or more of the above, bound together so that data and applications can move between them |

An interviewer who says "public, private, hybrid" names the three common types. Adding "and community" shows you know the full list.

Say it in 20 seconds: "Cloud means renting computing instead of owning it. With software as a service I get the finished application. With platform as a service I get a place to run my own application. With infrastructure as a service I get the machines and install everything myself."

### The OSI model: seven layers

A model that splits network communication into seven layers. The names and jobs below were read on IBM's explainer "What is the OSI model?" (published 7 Aug 2024, updated 17 Nov 2025). The ISO standard itself was not read, so the tag is `[LIKELY]`.

| Layer | Name | Its job in one line |
|---|---|---|
| 7 | Application | Starts communication with the network; turns network data into something a user can read |
| 6 | Presentation | Prepares data for the application: translation, compression, encryption |
| 5 | Session | Starts and ends the connection between two devices |
| 4 | Transport | Carries data end to end between two devices and checks it is not lost or corrupted |
| 3 | Network | Addresses the data and routes it between different networks |
| 2 | Data link | Moves data between two devices on the same network |
| 1 | Physical | Sends raw bits over cables and connectors |

Memory aid, top to bottom: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing.

If you are asked "where does a router work?", the answer from the table is layer 3, the network layer (it routes between networks). Layer 2 is the same-network step.
