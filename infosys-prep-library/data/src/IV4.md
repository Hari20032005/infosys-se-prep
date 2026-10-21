## 2. Exactly what gets asked

Project questions were asked in **two of five** first-hand Infosys interview accounts `[REPORTED]`: “Please explain your final-year project in detail” (B2) and “Explain your capstone project” (B5). A third candidate (B4) credits “the technical skills I mentioned in my resume” for answering well, so expect resume-driven questions too. The interview is 15–40 minutes, so expect **one project to be chosen** and probed for 5–10 minutes.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| “Explain your final-year / capstone project” | Open prompt, then follow-ups | B2, B5 |
| “Tell me about a project or skill on your resume” | Panel picks one from the resume | B4 (implied) |
| “Why this technology?” | Choice of stack, database, model | common follow-up |
| “What would you improve?” | Checks honesty and depth | common follow-up |

**Hari-specific warning, read first.** Your resume lists an **Infosys Springboard Virtual Internship 6.0 (WasteZero)**. An Infosys interviewer knows that programme and may open the GitHub link. The link is a **fork** whose commit history shows **no commits by you** (checked 27 Sep 2026, in your own `HARIHARAN_INTERVIEW_CONTEXT.md` §9.1). Before you walk into the room you must be able to say, truthfully, **which module you built and where that work lives.** If you cannot, describe your part as a team contribution in a shared batch and do not claim the repository. **`[YOU FILL IN]`**: the module, the milestone, the teammate who maintained the consolidated repo.

## 3. Concept notes

### 3.1 The five-part project answer (90 seconds)

| Part | What to say | Time |
|---|---|---|
| Problem | Who has the problem and why it matters | 15 s |
| Approach | The design in two or three sentences | 25 s |
| Your part | What **you** built, in “I” sentences | 25 s |
| Result | What works, measured or shown; say “not measured” if it is not | 15 s |
| Improvement | One honest thing you would do differently | 10 s |

### 3.2 Choose the project by the panel's likely interest

Infosys hires for services: applications, testing, maintenance, databases (Systems Engineer: “application development, testing, and maintenance”, per the drive pages). A project with **a database, an API and a front end** will be discussed comfortably. Lead with one of those.

### 3.3 Your three candidates (facts from your own verified context file)

| Project | One-line pitch | Say this | Do not say |
|---|---|---|---|
| **RAG-based academic document explainer** (solo; all 9 commits are yours) | Upload a paper, ask a question, get an answer with the chunk and page cited | Stack: FastAPI, ChromaDB, MiniLM embeddings, React; pluggable LLM; async upload with job polling | “multi-turn” (the `/ask` endpoint sends no history); any retrieval-improvement percentage (no evaluation code exists). **Redeploy the backend before the interview**: the Railway backend returned “Application not found” on 27 Sep 2026 |
| **Sugarcane pest detection** (team Deepcrop, first prize, DBT-sponsored Agrithon 2.0) | Fuses a YOLOv8 image model with a questionnaire model to detect two pests | Why two inputs; segmentation vs detection; how the 0.6/0.4 fusion works | Any accuracy figure (none was measured); that you built all of it (it was a team of four) `[YOU FILL IN: your part]` |
| **Infosys Springboard WasteZero** (virtual internship, Feb–Apr 2026) | MERN platform for waste pickups and volunteer–NGO matching | It was a virtual, mentor-led programme; state the module you built | That it was on-site or industry experience; that you authored the consolidated repo |

### 3.4 “What would you improve?” (a strong answer for WasteZero)

If you worked on this codebase, these are real defects you can discuss as a code reviewer (from your context file §2.6). Say only what you have checked yourself in the code:
1. The auth middleware sets `req.user.id` but many controllers read `req.user._id`, so some writes fail validation.
2. Account suspension is never enforced at login or in the middleware.
3. The JWT is also stored in `localStorage`, which undoes the protection of the httpOnly cookie.
4. OTPs use `Math.random()` and are stored in plaintext.

### 3.5 Questions a services panel asks about any project

Why that database? How does authentication work? What happens if two users click at the same time? How did you test it? How is it deployed? What would break first at 100× the users? Have a one-sentence answer for each of your three projects.

## 4. Must-memorise block

| Item | Fact |
|---|---|
| Your degree | Integrated M.Tech Software Engineering, VIT Vellore, graduating May 2027 |
| Strongest language | Java (projects use Python, JS and TS) |
| RAG | FastAPI, Python 3.11, ChromaDB, all-MiniLM-L6-v2 (384-dim), chunk 3000 / overlap 800, top_k 5 |
| Sugarcane | YOLOv8 (segmentation for Dead Heart, detection for Tiller) + questionnaire model; HF Spaces backend; first prize at Agrithon 2.0 |
| Patents | Two **published patent applications**, co-inventor, assigned to VIT. Never “I have two patents” |
| Honest gaps | Node.js “learning”; Docker “basics”; no measured accuracy on Sugarcane; no retrieval evaluation on RAG |

## 5. Worked examples

**Example 1 — RAG, 90 seconds.**
“Researchers often need one fact from a long paper. My project lets you upload a paper and ask a question, and the answer comes back with the page and the exact chunk it used, so you can check it. I built it on FastAPI with a Chroma vector store and a sentence-transformer model; uploads are processed in the background so the page does not time out. I added a section-tree layer that steers a question like ‘what dataset did they use’ towards the experiments section. I have not measured retrieval quality yet; the next step would be a labelled question set and recall@k.” *(No percentages, no “multi-turn”.)*

**Example 2 — Sugarcane, 90 seconds.**
“Farmers in our region lose crops to two pests. Our team of four built a system that combines a photo of the plant, analysed by a YOLOv8 model, with a questionnaire the farmer fills in; the two scores are blended. We won first prize at a DBT-sponsored hackathon. *[My part:* YOU FILL IN.*]* We did not measure accuracy on a held-out set, and the blend weights were set by judgement, not tuned.”

**Example 3 — “Why MongoDB for WasteZero?”**
“The data is document-shaped: opportunities with a list of required skills, applications, notifications. Mongoose gave us schema validation. For pickups and payments at scale, a relational database would be safer because those need transactions.”

**Example 4 — “How do you stop duplicate applications?”**
“A compound unique index on (opportunity, volunteer), so the database rejects duplicates even if two requests arrive together.”

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Claiming a repository you did not author | The link is public and the interviewer is at the company that ran the programme | Name your module; do not claim the repo |
| Listing every project | 15 minutes is not enough | Offer two and let them pick |
| A percentage with no evaluation behind it | One follow-up exposes it | Say “not measured” |
| Saying “we” for everything | They cannot credit you | “I” for your actions, “we” for context |
| A dead live demo | A broken link looks careless | Test the URLs the day before |
| Reading the resume aloud | Wastes the time | Give the story, not the bullets |

## 8. Resources

- **https://fastapi.tiangolo.com/** — revise the framework behind your RAG and Sugarcane backends.
- **https://docs.github.com/en/get-started/using-git/about-git** — if you are asked how you used Git in the project.

## 9. Self-check

1. Can you describe each of your three projects in 90 seconds using the five parts?
2. Can you name exactly which WasteZero module you built?
3. Why is “multi-turn” not a safe word for the RAG project?
4. What will you say when asked for the accuracy of the Sugarcane model?
5. Which two projects will you offer when asked to “walk me through your projects”?
