# QB-IV1 — SDLC, Agile vs Waterfall, Testing and Version Control

**Interview** · **Tier 1** · 18 questions

Topic file: [`IV1-sdlc-agile-testing.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/interview/IV1-sdlc-agile-testing.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T33-D8-sdlc-agile-testing.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(Version control — Git branching)*

Which Git command creates a new branch called `feature` and switches to it in a single step?

(a) `git checkout -b feature`
(b) `git branch feature`
(c) `git merge feature`
(d) `git clone feature`

**1. (a) `git checkout -b feature`**
`checkout -b` creates the branch and switches to it in one command.
- (b) `git branch feature` creates the branch but leaves you on the current branch.
- (c) `git merge feature` joins an existing branch into the current one; it creates nothing.
- (d) `git clone feature` is not valid usage — `clone` copies a whole remote repository.

---

**2.** **[Easy]** *(Testing — verification vs validation)*

Which of the following is a **verification** activity?

(a) Static code review performed by peers
(b) Beta testing performed by end users
(c) Acceptance testing performed by the customer
(d) System testing performed against user requirements

**2. (a) Static code review performed by peers**
Verification checks the work products (documents, design, code) without executing them; a peer review does exactly that.
- (c) Acceptance testing executes the system and checks it against user needs — validation.
- (b) Beta testing exercises the running product with real users — validation.
- (d) System testing executes the built system against requirements — validation.

---

**3.** **[Easy]** *(Agile — Scrum artefacts)*

Which of the following is **NOT** a Scrum artefact?

(a) Product Backlog
(b) Gantt chart
(c) Increment
(d) Sprint Backlog

**3. (b) Gantt chart**
Scrum defines exactly three artefacts: Product Backlog, Sprint Backlog and Increment. A Gantt chart is a traditional plan-driven scheduling tool.
- (a) Product Backlog is a defined Scrum artefact.
- (d) Sprint Backlog is a defined Scrum artefact.
- (c) Increment is a defined Scrum artefact.

---

**4.** **[Easy]** *(SDLC — Waterfall)*

Which statement describes the Waterfall model?

(a) Each phase is completed and signed off before the next begins, and requirements are frozen early.
(b) Working software is delivered at the end of every two-week iteration.
(c) Highest-risk features are built first in repeated risk-driven cycles.
(d) The customer sits with the team and requirements may change at any time.

**4. (a) Each phase is completed and signed off before the next begins, and requirements are frozen early.**
Waterfall is strictly sequential; each phase's output is the next phase's input, and late requirement changes are expensive.
- (b) Two-week iterations of working software describe Agile, not Waterfall.
- (c) Building the highest-risk features first in repeated risk-driven cycles describes Spiral.
- (d) An on-site customer with continuously changing requirements describes an Agile/XP-style process.

---

**5.** **[Easy]** *(Testing — levels)*

Testing the smallest individually testable unit of code, usually one function or method, in isolation from the rest of the system, is called:

(a) System testing
(b) Integration testing
(c) Unit testing
(d) Acceptance testing

**5. (c) Unit testing**
Unit testing targets the smallest testable piece — one function, method or class — in isolation.
- (a) System testing exercises the whole integrated product against requirements.
- (b) Integration testing checks interfaces between modules that have already been unit tested.
- (d) Acceptance testing is performed by the customer to decide whether to accept the product.

---

**6.** **[Easy]** *(Version control — Git basics)*

What does `git commit -m "message"` do?

(a) Uploads the staged changes to the remote repository.
(b) Creates a new branch and checks it out.
(c) Records the currently staged snapshot as a new commit in the local repository.
(d) Reverts the working directory to the last commit.

**6. (c) Records the currently staged snapshot as a new commit in the local repository.**
`commit` writes what is in the staging area into the local repository history; nothing leaves the machine until a `push`.
- (a) Uploading to the remote is `git push`, not `commit`.
- (b) Creating and checking out a branch is `git checkout -b` (or `git switch -c`).
- (d) Discarding working-directory changes is `git checkout -- .` / `git restore`.

---

**7.** **[Medium]** *(SDLC — model selection)*

A bank is replacing a legacy batch system. All requirements have been gathered and signed off; the regulator requires a complete, frozen specification and full design documentation before any code is released; the system will be delivered as one release on a fixed date. Which process model fits best?

(a) Spiral
(b) Scrum
(c) Waterfall
(d) Prototyping

**7. (c) Waterfall**
Frozen, fully specified requirements, heavy up-front documentation for a regulator, and a single fixed delivery are the conditions Waterfall is designed for.
- (b) Scrum assumes changing requirements and frequent incremental delivery — neither applies here.
- (a) Spiral is used when risk is high and requirements emerge progressively; here they are already fixed.
- (d) Prototyping is used to discover unclear requirements; these are already signed off.

---

**8.** **[Medium]** *(Agile — Scrum roles)*

In Scrum, who is accountable for ordering the Product Backlog so that it delivers the most value?

(a) The Product Owner
(b) The Developers
(c) The Scrum Master
(d) The Project Manager

**8. (a) The Product Owner**
The Product Owner owns the Product Backlog and is accountable for its ordering and for maximising the value delivered.
- (c) The Scrum Master coaches the process and removes impediments; the role carries no backlog authority.
- (b) The Developers estimate and pull work; they do not own the backlog ordering.
- (d) Scrum has no Project Manager role.

---

**9.** **[Medium]** *(Agile — Scrum ceremonies)*

What is the purpose of the Sprint Retrospective?

(a) Demonstrate the Increment to stakeholders and collect their feedback.
(b) Inspect how the last Sprint went and identify concrete improvements to the team's way of working.
(c) Select the Product Backlog items that will be delivered in the next Sprint.
(d) Give a daily update on progress and blockers.

**9. (b) Inspect how the last Sprint went and identify concrete improvements to the team's way of working.**
The Retrospective is the process-improvement ceremony at the end of a Sprint.
- (a) That is the Sprint Review.
- (c) That is Sprint Planning.
- (d) That is the Daily Scrum.

---

**10.** **[Medium]** *(Testing — level vs type)*

A team runs a test in which 500 virtual users hit the checkout API simultaneously while response times and error rates are recorded. All functional requirements are already known to pass. How should this test be classified?

(a) Unit level, functional type
(b) Integration level, functional type
(c) Unit level, non-functional type
(d) System level, non-functional type

**10. (d) System level, non-functional type**
Load/performance testing measures qualities (response time, throughput, error rate) rather than correctness, and is run against the whole integrated system, so it is a non-functional test at system level.
- (a) It is neither at unit level nor functional.
- (b) It is not an interface check between modules, and it is not functional.
- (c) It is not at unit level, and the classification "functional" is wrong.

---

**11.** **[Medium]** *(Version control — remote operations)*

Which statement correctly distinguishes `git fetch` from `git pull`?

(a) `git fetch` merges remote changes into the current branch; `git pull` only downloads them.
(b) `git fetch` deletes local commits that are not on the remote; `git pull` restores them.
(c) `git fetch` downloads new commits and updates remote-tracking branches without touching the working directory; `git pull` also integrates those commits into the current branch.
(d) `git fetch` sends local commits to the remote; `git pull` retrieves tags only.

**11. (c) `git fetch` downloads new commits and updates remote-tracking branches without touching the working directory; `git pull` also integrates those commits into the current branch.**
`git pull` is defined as `git fetch` followed by a merge (or rebase) of the fetched branch into the current branch.
- (a) Reverses the two commands.
- (b) Neither command deletes local commits.
- (d) Pushing is `git push`; `fetch` and `pull` both retrieve.

---

**12.** **[Medium]** *(Testing — verification vs validation)*

Which pair correctly matches the two terms?

(a) Verification — "Does the product meet user needs?"; Validation — "Does the code follow the coding standard?"
(b) Verification — "Are we building the right product?"; Validation — "Are we building the product right?"
(c) Verification — "Does the product pass acceptance testing?"; Validation — "Does the code compile?"
(d) Verification — "Are we building the product right?"; Validation — "Are we building the right product?"

**12. (d) Verification — "Are we building the product right?"; Validation — "Are we building the right product?"**
Verification confirms that work products conform to their specification; validation confirms that the finished product meets the user's actual needs.
- (b) Swaps the two standard definitions.
- (c) Acceptance testing is validation, and compiling is a build step, not verification of requirements.
- (a) Meeting user needs is validation, and coding standards are internal correctness, not validation of user needs.

---

**13.** **[Medium]** *(SDLC — model selection)*

A five-person start-up is building a mobile marketplace. The scope is unclear, the client wants priorities changed weekly, and a demonstrable release is needed every two weeks. Which approach fits best?

(a) Waterfall
(b) Big-Bang model
(c) V-model
(d) Agile (Scrum)

**13. (d) Agile (Scrum)**
Unclear scope, weekly priority changes and a two-week demonstrable release are exactly the conditions Scrum's short Sprints and reprioritisable Product Backlog handle.
- (a) Waterfall requires frozen, up-front requirements and delivers late.
- (c) The V-model is verification-heavy and sequential, with testing tied to completed design phases.
- (b) Big-Bang writes the whole system and integrates at the end — the highest-risk option for changing scope.

---

**14.** **[Medium]** *(Testing — integration strategies)*

Integration testing is to begin from the lowest modules and work upward. The module tree is shown below.

```
        Top
       /    \
      A      B
     / \      \
    C   D      E
```

Testing starts with C, D and E. Because no higher-level module that calls them has been integrated yet, a temporary piece of code is written to invoke each module under test and feed it test data. What is this temporary code called?

(a) A smoke test
(b) A stub
(c) A regression suite
(d) A driver

**14. (d) A driver**
A driver is the temporary calling routine that invokes the module under test and supplies its inputs; it is required in bottom-up integration.
- (b) A stub is the opposite placeholder: it replaces a lower-level module that the module under test calls, used in top-down integration.
- (c) A regression suite is a set of existing tests re-run after a change, not a calling routine.
- (a) A smoke test is a shallow check that a build is stable enough to test further.

---

**15.** **[Hard]** *(Testing — V-model)*

In the V-model, each phase on the left has a matching test level on the right.

| V-model phase (left) | Matching test level (right) |
|---|---|
| Requirements analysis | Acceptance testing |
| System design | System testing |
| Architectural (high-level) design | ? |
| Detailed design | Unit testing |

Which test level fills the blank?

(a) Integration testing
(b) Acceptance testing
(c) Regression testing
(d) Unit testing

**15. (a) Integration testing**
In the V-model, the architectural/high-level design is verified by integration testing (interfaces between modules), which is exactly what that design phase specifies.
- (d) Unit testing maps to detailed design.
- (b) Acceptance testing maps to requirements analysis.
- (c) Regression testing is not a V-model level; it is a purpose applied at any level.

---

**16.** **[Hard]** *(Version control — rebase)*

The repository has the history below. `main` is at commit D, and the checked-out branch is `feature` at commit F.

```
A --- B --- C --- D     main
       \
        E --- F         feature
```

The command `git rebase main` is run while `feature` is checked out. After it completes, what is the parent of the replayed commit E′?

(a) A
(b) D
(c) B
(d) F

**16. (b) D**
`git rebase main` replays feature's own commits (E and F) on top of the current tip of `main`, which is D, so E′ is created as a child of D; E and F are abandoned and replaced by E′ and F′.

| Step | main | feature | Note |
|---|---|---|---|
| Start | A-B-C-D | A-B-E-F | common ancestor is B |
| `git rebase main` | A-B-C-D (unchanged) | A-B-C-D-E′-F′ | E and F replayed on top of D |
| Parent of E′ | — | — | D |

- (a) A is the root commit, not the rebase base.
- (c) B is the common ancestor (merge base), not the new parent.
- (d) F is the old tip of `feature`; it is replaced by F′ and is not an ancestor of E′.

---

**17.** **[Hard]** *(SDLC — model selection)*

A defence contractor is building a large command-and-control system. The requirements cannot be fully known up front, the technical risks (new hardware, an unfamiliar protocol stack) are high, and management wants each risk analysed and reduced before committing to the next, larger build. Which model fits best?

(a) Waterfall
(b) Spiral
(c) Big-Bang
(d) V-model

**17. (b) Spiral**
Spiral is the risk-driven model: each loop begins with risk analysis and ends with a progressively larger build, which matches high technical risk plus emerging requirements.
- (a) Waterfall assumes requirements can be frozen up front, which they cannot here.
- (c) Big-Bang has no risk analysis and integrates only at the end — the worst fit for high-risk work.
- (d) The V-model is a sequential verification model; it does not contain explicit risk-reduction cycles.

---

**18.** **[Medium]** *(Testing — regression)*

A developer fixes a bug in the tax-calculation module and merges the change. Which type of testing is specifically intended to confirm that this change has not broken functionality that previously worked?

(a) Smoke testing
(b) Regression testing
(c) Acceptance testing
(d) Exploratory testing

---

---

**18. (b) Regression testing**
Regression testing re-runs tests over existing functionality to detect side effects introduced by a change.
- (a) Smoke testing only checks that the build is stable enough for further testing.
- (c) Acceptance testing decides whether the customer accepts the delivered functionality.
- (d) Exploratory testing is simultaneous learning and testing without pre-written scripts; it is not aimed at side effects.

---
