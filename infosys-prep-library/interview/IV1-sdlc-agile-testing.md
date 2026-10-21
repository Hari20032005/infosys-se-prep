---
title: SDLC, Agile vs Waterfall, Testing and Version Control
code: IV1
section: Interview
weightage_pct: interview stage
est_questions: 7
tier: 1
difficulty: Medium
est_study_hours: 1.0
confidence: High
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T33-D8-sdlc-agile-testing.md
---

# IV1 — SDLC, Agile vs Waterfall, Testing and Version Control

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T33-D8-sdlc-agile-testing.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

This is interview material, not test material. **7 questions on this theme** were reported across **4 first-hand interview accounts** (B1, B2, B3, B4), so it is **Tier 1** for the interview stage, 1.0 hours to prepare. Interviews are face to face on campus, 15–40 minutes, technical and HR usually in one conversation (`../research/03-pattern-synthesis.md` §6). The questions are at textbook level; the teaching body below is sized to answer them aloud, not to pass a written exam.

## 2. Exactly what gets asked

### What Infosys interviewers asked

| ID | Account | Date | Question |
|---|---|---|---|
| I01 | B1 | 2025-05-12 | Define SDLC. |
| I02 | B1 | 2025-05-12 | Difference between Waterfall and Agile. |
| I09 | B2 | 2025-01-10 | What is the SDLC? |
| I10 | B2 | 2025-01-10 | Who is a Scrum Master? |
| I11 | B2 | 2025-01-10 | What is sprint planning? |
| I13 | B3 | 2025-12-04 | Explain the SDLC and different SDLC models. |
| I15 | B4 | 2025-01-20 | What is SDLC and why is it needed? |

> The pattern notes below come from the library this file was adapted from; their frequency remarks describe that source, not Infosys.



1. **Model selection from a scenario.** Fixed requirements and heavy documentation point to Waterfall; changing requirements and frequent delivery point to Agile.

1. **(a) Requirements analysis** — The SRS is the output of requirements analysis.  
- (b) Design turns requirements into architecture and detailed design.  
- (c) Implementation writes code from the design.  
- (d) Maintenance changes the system after delivery.

---

2. **Waterfall versus Agile discrimination.** The standard comparison.

2. **(d) Phases execute sequentially with limited overlap** — Waterfall completes one phase before the next begins.  
- (a) Short iterations are typical of Agile, not Waterfall.  
- (c) Free requirement changes are not a Waterfall characteristic.  
- (b) Waterfall generally requires documentation.

---

3. **Scrum vocabulary.** Roles, artefacts and ceremonies — which is which.

3. **(b) Product Owner** — The Product Owner manages and prioritizes the Product Backlog.  
- (c) The Scrum Master facilitates Scrum and removes impediments.  
- (a) The Development Team builds the product increment.  
- (d) The PMO is not a Scrum role.

---

4. **Testing level versus testing type.** Unit/integration/system/acceptance are *levels*; smoke, regression and load are *types*.

4. **(a) Copy a remote repository to the local machine** — `git clone` creates a local copy of a remote repository.  
- (b) Branch creation is done with `git branch` or `git checkout -b`.  
- (c) Fetching and merging remote changes is `git pull`.  
- (d) Removing untracked files is `git clean`.

---

5. **Verification versus validation.** "Building the product right" versus "building the right product".

5. **(d) Unit testing** — Unit testing checks individual components in isolation.  
- (b) Integration testing checks interactions between components.  
- (a) System testing checks the complete system.  
- (c) Acceptance testing checks fitness for user needs.

---

6. **Git command purpose.** What `add`, `commit`, `push`, `pull`, `fetch` and `merge` each do.

## 3. Concept notes

**SDLC phases in order** — requirements → analysis → design → implementation → testing → deployment → maintenance.

**SDLC models**

| Model | One-line description | When to use | Drawback |
|---|---|---|---|
| Waterfall | Sequential phases, no going back | Fixed, clear requirements | Changes are expensive |
| V-model | Waterfall with testing paired to each phase | Safety-critical projects | Rigid |
| Iterative | Repeated cycles, refine each time | Evolving requirements | Can waste effort |
| Incremental | Build and deliver in increments | Partial delivery needed | Integration overhead |
| Spiral | Iterative + risk analysis | Large, high-risk projects | Costly |
| Prototype | Build a quick model first | Unclear requirements | User may expect prototype as final |
| Agile | Short iterative cycles, continuous feedback | Changing requirements | Needs disciplined team |

**Waterfall vs Agile**

| Aspect | Waterfall | Agile |
|---|---|---|
| Requirements | Fixed upfront | Evolving |
| Change handling | Difficult | Welcomed |
| Delivery | One final delivery | Frequent increments |
| Customer involvement | Low, at milestones | High, continuous |
| Documentation | Heavy | Lightweight |
| Risk | High, late discovery | Lower, early feedback |
| Team size | Large, specialised | Small, cross-functional |
| Best suited for | Stable, regulated projects | Fast-changing products |

**Agile values** — individuals and interactions over processes/tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan.
**12 principles summarised** — early delivery, welcome change, frequent delivery, daily collaboration, motivated team, face-to-face communication, working software as measure, sustainable pace, technical excellence, simplicity, self-organising teams, regular reflection.

**Scrum**

| Element | Items |
|---|---|
| Roles | Product Owner, Scrum Master, Development Team |
| Artefacts | Product backlog, sprint backlog, increment |
| Ceremonies | Sprint planning, daily stand-up, sprint review, sprint retrospective |

Sprint length is typically **2–4 weeks**.
**Kanban vs Scrum** — Kanban: continuous flow, WIP limits, no fixed roles. Scrum: time-boxed sprints, defined roles, sprint backlog.
**User story** — “As a `<role>`, I want `<feature>`, so that `<benefit>`.” **Story points** — relative size estimate.

**Testing levels in order** — unit → integration → system → acceptance.
**Testing types**

| Category | Types |
|---|---|
| Functional vs non-functional | Functional: features work; Non-functional: performance, security, usability |
| Black/white/grey box | Black: no internal knowledge; White: internal code known; Grey: partial |
| Smoke | Basic build check |
| Sanity | Narrow check after minor change |
| Regression | Re-test after changes |
| Alpha | In-house before release |
| Beta | Real users before release |
| Performance | Speed under normal load |
| Load | Behaviour under expected load |
| Stress | Beyond normal limits |
| Security | Vulnerabilities |
| Usability | Ease of use |

**Verification vs validation** — verification: “are we building the product right?” (reviews, static). Validation: “are we building the right product?” (execution, dynamic).
**Test pyramid** — many unit tests, fewer integration tests, few UI/end-to-end tests.
**Severity vs priority** — severity = impact on system; priority = urgency to fix.

**Version control** — centralised (single server, e.g. SVN) vs distributed (full copy, e.g. Git).
**Git basics** — working directory → staging area → local repo → remote.
**Core commands** — `init`, `clone`, `add`, `commit`, `push`, `pull`, `fetch`, `status`, `log`.
**Branching and merging** — branch creates an independent line; merge combines it.
**Merge vs rebase** — merge preserves history with a merge commit; rebase rewrites history onto another base.
**Merge conflict** — same file region changed differently; must be resolved manually.
**Pull request** — request to merge a branch, with review.
**.gitignore** — lists files/folders Git should not track.

## 4. Must-memorise block

- SDLC order: **requirements → analysis → design → implementation → testing → deployment → maintenance**.
- Waterfall = fixed, sequential, documentation-heavy. Agile = iterative, flexible, customer-focused.
- Scrum roles: Product Owner, Scrum Master, Development Team. Artefacts: product backlog, sprint backlog, increment. Ceremonies: planning, daily stand-up, review, retrospective.
- Testing levels: **unit → integration → system → acceptance**.
- Verification = build right; Validation = right product.
- Git flow: working directory → staging → local repo → remote. `add` stages, `commit` saves locally, `push` uploads, `pull` fetches + merges.
- `.gitignore` excludes untracked files.

## 5. Worked examples

### Example 1 — Selecting an SDLC model from a project description

**Scenario.** A defence contractor must deliver a system under a fixed-price contract. The customer's requirements are frozen and signed off. Certification requires documented outputs and formal review sign-off at the end of each phase before the next phase begins. Requirements changes are contractually prohibited mid-project. Which model fits best?

(A) Scrum (B) Waterfall (C) Prototyping (D) Spiral

**Reasoning**

1. Identify the dominant driver: **requirement stability**. Requirements are frozen and changes are prohibited — this removes the main problem Agile exists to solve.
2. Identify the compliance driver: **phase-wise documentation and formal gates**. Sequential models produce reviewable artefacts at each phase boundary by default; Agile produces them only if the team adds them.
3. Test each option against those drivers:
   - Scrum — optimised for frequent change; the ceremony overhead buys nothing when change is banned.
   - Prototyping — used when requirements are unclear; here they are signed off.
   - Spiral — driven by **risk analysis loops**; nothing in the scenario identifies high technical risk as the governing factor.
   - Waterfall — sequential phases with defined deliverables and review gates.
4. Check the classic counter-argument: Waterfall handles late change poorly, but the contract already forbids late change, so that weakness does not bite.

Model-selection shortcut table:

| Driver | Model that fits |
|---|---|
| Requirements frozen, contractual phase gates, heavy documentation | Waterfall / V-model |
| Unclear requirements, need user feedback early | Prototyping |
| Large, high-risk, risk reduction dominates | Spiral |
| Requirements evolve continuously, frequent deliverable increments | Agile (Scrum/XP/Kanban) |
| Verification paired with validation from the start | V-model |

**Answer: (B) Waterfall.**

---

### Example 2 — Scrum accountabilities and ceremonies

**Scenario.** Which ONE statement about Scrum is correct?

(A) The Daily Scrum is a 15-minute status meeting chaired by the Scrum Master, who uses it to reassign work.
(B) The Sprint Review inspects the Increment with stakeholders and may result in Product Backlog adjustments.
(C) The Scrum Master is accountable for ordering the Product Backlog to maximise value.
(D) The Sprint Retrospective is the event at which the Sprint Goal is formally set.

**Reasoning**

1. (A) The Daily Scrum is **for the Developers**, is timeboxed to 15 minutes, and exists to inspect progress toward the **Sprint Goal** and adapt the Sprint Backlog. The Scrum Master facilitates but does not chair or reassign. The team is self-managing. **False.**
2. (B) The Sprint Review inspects the **outcome of the Sprint** — the Increment — with stakeholders, and the Product Backlog is adapted as a result. It is a working session, not a one-way demo. **True.**
3. (C) Ordering the Product Backlog is the **Product Owner's** accountability. The Scrum Master serves the team and organisation by coaching and removing impediments. **False.**
4. (D) The Sprint Goal is set at **Sprint Planning**. The Retrospective inspects the *process and team interactions* and produces improvement actions. **False.**

Scrum reference:

| Item | Owner / Purpose |
|---|---|
| Product Backlog ordering | Product Owner |
| Sprint Goal, Sprint Backlog | Created at Sprint Planning by the whole Scrum Team |
| Daily Scrum (15 min) | Developers; inspect progress toward Sprint Goal |
| Sprint Review | Inspect Increment with stakeholders; adapt Product Backlog |
| Sprint Retrospective | Inspect process/team; plan improvements |
| Impediment removal, coaching | Scrum Master |

**Answer: (B).**

---

### Example 3 — Testing-level discrimination

**Scenario.** A team performs four activities. Classify each by test level.

1. `calculateTax()` is tested with all external dependencies replaced by stubs.
2. The Order service is tested calling the live Payment gateway sandbox to check the request/response contract.
3. The full deployed application is run end-to-end against the SRS on a production-like environment.
4. Business users confirm the refund workflow meets their operational need before go-live.

**Reasoning**

1. Activity 1 exercises **one component in isolation** with dependencies replaced → **unit testing**. The defining property is scope, not the tool used.
2. Activity 2 exercises the **interface between two components/subsystems** → **integration testing**. The sandbox is incidental; the target is the interaction.
3. Activity 3 exercises the **whole integrated system** against specified requirements → **system testing**.
4. Activity 4 is conducted by **users/customers** against **business need**, not against the SRS → **acceptance testing (UAT)**.

Level ladder:

| Level | Scope | Typical basis |
|---|---|---|
| Unit / component | One component in isolation | Detailed design / code |
| Integration | Interfaces between components or subsystems | Interface design |
| System | Whole integrated system | SRS / requirements spec |
| Acceptance | Whole system, judged by users | Business need / contract |

**Answer: 1 = unit, 2 = integration, 3 = system, 4 = acceptance (UAT).**

---

### Example 4 — Verification versus validation

**Scenario.** Which single activity is an example of **validation**?

(A) Static analysis flags an unreachable branch in the code.
(B) A formal inspection compares the detailed design document against the SRS.
(C) The requirements specification is walked through with the customer and re-worded for clarity.
(D) The released build is executed by end users against real business scenarios in a UAT environment.

**Reasoning**

1. Apply the standard test: verification asks *"are we building the product right?"* — conformance to specification, performed on work products without executing them. Validation asks *"are we building the right product?"* — fitness for intended use, assessed by exercising the product.
2. (A) Static analysis examines source without executing it → **verification**.
3. (B) A document inspection against a specification → **verification**.
4. (C) A requirements walkthrough is a static review of a work product → **verification**.
5. (D) The artefact is **executed**, and the judgement is made against **business need** rather than the spec → **validation**.

Split:

| | Verification | Validation |
|---|---|---|
| Question | Building the product right? | Building the right product? |
| Executes code? | No (static) | Yes (dynamic) |
| Typical techniques | Reviews, walkthroughs, inspections, static analysis | Unit/integration/system testing, UAT, alpha/beta |
| Reference point | Specification, design, standards | User need, business requirement |

**Answer: (D).**

---

### Example 5 — Git command purposes

**Scenario.** Match each situation to the correct command.

1. A wrong change was already pushed to the shared `main` branch; it must be undone without rewriting shared history.
2. You want to download the latest commits from the remote so you can inspect them, without altering your working branch.
3. Your three local commits were made on an outdated base; you want them replayed on top of the latest `origin/main` to produce linear history.
4. You want to create a new branch and switch to it in a single command.

**Reasoning**

1. Situation 1 — undoing a **published** commit must not delete the commit from shared history, so a new commit that inverts the change is required → **`git revert <commit>`**. (`git reset` moves the branch pointer and rewrites history; it is unsafe on shared branches.)
2. Situation 2 — `git fetch` downloads remote objects and updates remote-tracking refs (`origin/main`) but does **not** merge into your current branch or touch your working tree → **`git fetch`**. (`git pull` = fetch + merge, which does alter your branch.)
3. Situation 3 — replaying your own unpushed commits onto a new base is exactly what rebase does, producing a linear history at the cost of new commit hashes → **`git rebase origin/main`**.
4. Situation 4 — `git branch <name>` only creates; the combined create-and-switch is **`git switch -c <name>`** (equivalent older form: `git checkout -b <name>`).

Quick reference:

| Command | Purpose |
|---|---|
| `git add` | Stage changes into the index |
| `git commit` | Record the staged snapshot in local history |
| `git fetch` | Download remote commits/refs; working branch unchanged |
| `git pull` | Fetch, then merge into the current branch |
| `git push` | Upload local commits to the remote |
| `git merge` | Join histories; creates a merge commit when diverged |
| `git rebase` | Replay commits on a new base; rewrites commit hashes |
| `git revert` | New commit that undoes a previous commit; safe on shared branches |
| `git reset` | Move the branch pointer; `--soft`/`--mixed`/`--hard` control what survives |
| `git stash` | Shelve uncommitted changes temporarily |

**Answer: 1 = `git revert`, 2 = `git fetch`, 3 = `git rebase`, 4 = `git switch -c` (or `git checkout -b`).**

---

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Swapping verification and validation | Both sound like "checking the product is correct"; only one involves executing code | Verification = **static**, product right, checked against the spec. Validation = **dynamic**, right product, checked against user need |
| Assuming Agile means no planning or documentation | "Working software over comprehensive documentation" is misread as "no documentation" | Agile still plans (Product Backlog, Sprint Planning, Sprint Goal) and documents as needed; it just prioritises working software when the two conflict |
| Treating the Daily Scrum as a status report to the Scrum Master | Most workplaces run stand-ups as manager-facing status updates | It is a 15-minute event **for the Developers** to inspect progress toward the Sprint Goal and adapt the Sprint Backlog; the Scrum Master facilitates, does not chair or assign |
| Confusing Sprint Review with Sprint Retrospective | Both occur at the end of the Sprint | Review = **product**: inspect the Increment with stakeholders, adapt the Product Backlog. Retrospective = **process**: inspect how the team worked, plan improvements |
| Judging test level by the tool or environment instead of the scope | "It runs the whole build, so it must be system testing" | Level is fixed by **what is under test**: one component (unit), interfaces (integration), whole system against the SRS (system), business need by users (acceptance) |
| Confusing regression testing with retesting | Both are re-runs after a change | Retesting = confirm a **specific defect fix** works. Regression = confirm the change **broke nothing else** |
| Believing `git fetch` and `git pull` are interchangeable | Both contact the remote, so they look equivalent | `fetch` downloads and updates remote-tracking refs only; `pull` = fetch **+ merge into your current branch**, so it changes your working state |
| Using `git reset` to undo a commit already pushed to a shared branch | `reset` is the natural "undo commit" instinct | `reset` moves the branch pointer and rewrites history, breaking others' clones. Use **`git revert`**, which adds a new inverse commit |
| Choosing the SDLC model by project size or team size | Big projects feel like they "need" Waterfall, small ones like they "need" Agile | The deciding factor is **requirement stability and tolerance for change**, plus risk and compliance needs — not headcount |

## 7. Practice questions

1. **[Easy]** *(D8 — SDLC phases)* In SDLC, which phase primarily produces the Software Requirements Specification (SRS)?  
(a) Requirements analysis
(b) Design
(c) Implementation
(d) Maintenance

2. **[Easy]** *(D8 — Waterfall model)* Which is a defining characteristic of the Waterfall model?  
(a) Working software is delivered in short iterations
(b) No documentation is required
(c) Requirements can change freely at any time
(d) Phases execute sequentially with limited overlap

3. **[Easy]** *(D8 — Scrum roles)* In Scrum, who is responsible for maximizing product value and managing the Product Backlog?  
(a) Development Team
(b) Product Owner
(c) Scrum Master
(d) Project Management Office

4. **[Easy]** *(D8 — Git commands)* What is the primary purpose of `git clone`?  
(a) Copy a remote repository to the local machine
(b) Create a new branch
(c) Merge changes from remote into the current branch
(d) Remove untracked files

5. **[Easy]** *(D8 — Testing levels)* Which testing level focuses on individual functions, methods, or classes in isolation?  
(a) System testing
(b) Integration testing
(c) Acceptance testing
(d) Unit testing

6. **[Medium]** *(D8 — Model selection)* A small team has vague and rapidly changing requirements, needs frequent releases, and can get regular customer feedback. Which SDLC model is best?  
(a) Waterfall
(b) Big Bang
(c) Agile
(d) V-Model

6. **(c) Agile** — Agile suits changing requirements, frequent releases, and continuous feedback.  
- (a) Waterfall expects stable requirements and sequential delivery.  
- (d) V-Model emphasizes verification and validation with planned phases.  
- (b) Big Bang is not a suitable controlled SDLC model here.

---

7. **[Medium]** *(D8 — Scrum ceremonies)* Which Scrum event is a 15-minute time-boxed meeting held daily to inspect progress toward the Sprint Goal?  
(a) Daily Scrum
(b) Sprint Planning
(c) Sprint Review
(d) Sprint Retrospective

7. **(a) Daily Scrum** — The Daily Scrum is a 15-minute daily inspect-and-adapt event.  
- (c) Sprint Review inspects the product increment with stakeholders.  
- (b) Sprint Planning defines the Sprint Goal and Sprint Backlog.  
- (d) Sprint Retrospective inspects team process and improvements.

---

8. **[Medium]** *(D8 — Verification vs validation)* Which activity is an example of verification?  
(a) User acceptance testing
(b) Reviewing a requirements specification for consistency
(c) Beta testing by end users
(d) System testing against user needs

8. **(b) Reviewing a requirements specification for consistency** — Verification checks whether we are building the product right.  
- (a) User acceptance testing is validation.  
- (c) Beta testing by end users is validation.  
- (d) System testing against user needs is validation.

---

9. **[Medium]** *(D8 — Testing types)* Which is a non-functional testing type?  
(a) Unit testing
(b) Performance testing
(c) Integration testing
(d) Regression testing

9. **(b) Performance testing** — Performance testing checks non-functional attributes like speed and responsiveness.  
- (a) Unit testing is a functional testing level.  
- (c) Integration testing is a functional testing level.  
- (d) Regression testing is a functional testing type.

---

10. **[Hard]** *(D8 — Git commands)* Which Git command reverses changes from a published commit by creating a new commit?  
(a) `git reset --hard`
(b) `git rebase`
(c) `git revert`
(d) `git checkout`

---

10. **(c) `git revert`** — `git revert` creates a new commit that reverses an earlier commit.  
- (a) `git reset --hard` moves the branch and discards changes.  
- (d) `git checkout` switches branches or restores files.  
- (b) `git rebase` reapplies commits onto another base.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — SDLC V-model | Article | https://www.geeksforgeeks.org/software-engineering/software-engineering-sdlc-v-model/ | Free | 20 min | Covers the model family and where each testing level attaches |
| roadmap.sh — DevOps | Roadmap | https://roadmap.sh/devops | Free | 10 min | Scope-setting for the version-control and CI vocabulary |
| IndiaBix — Computer science Q&A | Practice set | https://www.indiabix.com/computer-science/questions-and-answers/ | Free | 20 min | MCQ volume |
| `question-banks/QB-T33-D8-sdlc-agile-testing.md` | Question bank | (this library) | Free | 20 min | 20 original questions |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] I can list the SDLC phases in order
- [ ] I can compare Waterfall and Agile across at least six dimensions
- [ ] I can name the three Scrum roles, three artefacts and four ceremonies
- [ ] **I can distinguish a testing level from a testing type**
- [ ] I can define smoke, sanity, regression, alpha and beta testing
- [ ] I can state the difference between verification and validation
- [ ] I can explain black box versus white box testing
- [ ] I can say what `git fetch` does that `git pull` also does
- [ ] I scored 8/10 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T33-D8-sdlc-agile-testing.md`, verified in that library's QA. **Infosys evidence:** first-hand interview accounts in `../data/reviews-online.csv` and `../data/questions-observed.csv` (rows `I01`–`I25`); interview format in `../research/03-pattern-synthesis.md` §6.
