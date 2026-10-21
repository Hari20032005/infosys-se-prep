---
title: STAR stories from your own work
code: IV5
section: Interview
weightage_pct: interview stage
est_questions: 8
tier: 1
difficulty: Medium
est_study_hours: 1.5
confidence: High
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-comm-interview/interview/STAR-STORIES.md
supporting_for: IV5
---

# IV5 — STAR stories from your own work

*Adapted from `accenture-prep-final/accenture-prep-comm-interview/interview/STAR-STORIES.md`; written from your real work and verified in that library's QA. One patent-date line updated to match your later context file. Fill every `[YOU FILL IN]` truthfully before rehearsing.*

Ten stories from your real work, mapped to the behavioural prompts that actually get asked.

> **Everything here traces to your resume or your own repositories.** Where a story needs a detail
> only you know — team size, exact durations, who said what — it is marked **`[YOU FILL IN]`**.
> **Fill those in truthfully before you rehearse. Do not guess, and do not round upward.**
>
> **No invented metrics.** Several of these stories have no number attached, because you have not
> measured one. That is correct. A story without a metric is fine; a story with a fabricated metric
> is a disaster waiting for one follow-up question.

---

## How to deliver a STAR answer

| Part | Time | Rule |
|---|---|---|
| **S**ituation | ~10 s | Context only. Where, when, what was going on |
| **T**ask | ~10 s | What *you* specifically had to do |
| **A**ction | ~40 s | **The bulk of the answer.** What you actually did, in steps |
| **R**esult | ~15 s | What happened. Honest. "It worked" is a result |

**The most common failure is spending 40 seconds on Situation and 10 on Action.** They are hiring
for the Action. Keep the setup short.

**Say "I", not "we", when describing your own action.** Use "we" for the team's context. An
interviewer cannot credit you for something you described in the plural.

---

## Story 1 — Debugging something genuinely broken
**Prompts:** *"Tell me about a difficult technical problem." · "How do you approach debugging?" · "Tell me about a time something didn't work."*

**S** — Building the Sugarcane Pest Detection system, we had two model types: YOLOv8 segmentation for the Dead Heart pest and detection for Tiller.

**T** — The segmentation model wasn't loading and predicting correctly, and because it sat in the middle of the pipeline, I couldn't tell whether the problem was the model artefact, the preprocessing, or how I was reading the output.

**A** — Rather than keep changing things inside the full application and re-running the whole flow, I pulled the model out into a standalone test script so I could feed it one known image and inspect exactly what came back. That isolated it — I could confirm which stage was actually failing instead of guessing. Once I knew where the fault was, I fixed the loading path properly rather than patching around it, and I kept the test script in the repository so the same check could be re-run later.

**R** — The segmentation path worked correctly, and the diagnostic script stayed in the repo as a reusable check. **`[YOU FILL IN: roughly how long this took, and what the actual root cause turned out to be]`**

> **Why this is your best technical story:** it shows *method* — isolate before you fix. Most
> candidates describe a fix; very few describe how they narrowed it down.

---

## Story 2 — Working in an unfamiliar codebase
**Prompts:** *"Tell me about learning something new quickly." · "How do you handle unfamiliar technology?" · "Adapting to a new environment."*

**S** — I wanted to contribute to a real open-source project, and picked Zulip — a large codebase I had never seen, written largely in TypeScript, which isn't my strongest language.

**T** — I took on a bug where indented lists weren't continuing correctly.

**A** — I got the project running locally first, then reproduced the bug so I had something concrete to work against. Most of the effort was reading — tracing where list handling actually happened and understanding why the indentation case fell through. The change itself was small. I also wrote unit tests covering the broken cases, because without them there was no proof the bug was actually gone rather than just not visible in my manual test. Then I went through review and **`[YOU FILL IN: what the reviewers asked you to change]`**.

**R** — **PR #38394 was merged into Zulip.**

> **Use this for the tech-stack question too.** It is the same evidence.

---

## Story 3 — Improving something nobody asked you to improve
**Prompts:** *"Tell me about going beyond what was required." · "Taking initiative." · "Improving quality."*

**S** — Contributing to Learning Unlimited, a Python codebase, I was working in their student-lottery module.

**T** — The module had **no tests at all**, which meant any change to it was unverifiable.

**A** — I wrote the first tests for it. Separately, I noticed a config key duplicated in several places across the codebase — the kind of thing that works fine until someone changes one copy and not the others — so I centralised it in a second PR.

**R** — **Both PRs (#4957 and #4997) were merged.** The lottery module went from untested to having a test suite.

> **This is a strong "quality mindset" story and it is entirely true.** It also implicitly answers
> "do you write tests?" before it is asked.

---

## Story 4 — A hard technical trade-off
**Prompts:** *"Tell me about a difficult decision." · "A time you had to choose between two approaches." · "Making a judgement call."*

**S** — In the RAG document explainer, the ingestion pipeline depends on downloading a sentence-transformers embedding model.

**T** — If that download fails — on a constrained or offline environment — the entire pipeline dies, and nothing else in the application works.

**A** — I had to choose between failing loudly and degrading. I built a hash-based fallback embedder that takes over when the real model isn't available. Retrieval quality is clearly worse, but the system stays up. I went that way because a document explainer that returns weaker answers is still usable, whereas one that won't start is not. I'm aware of the counter-argument — silently giving worse results is its own problem — and the right version would surface that it's running in fallback mode rather than hiding it.

**R** — The system runs end to end without an embedding model present, which is also what made the test suite and CI viable.

> **Naming the counter-argument yourself is what makes this answer strong.** It shows you made a
> decision rather than just built a feature.

---

## Story 5 — Designing for constraints
**Prompts:** *"Tell me about working with limited resources." · "A constraint that shaped your design."*

**S** — Both of my deployed projects had to run on free-tier infrastructure with no budget, and the RAG project needed an LLM, which normally costs money per call.

**T** — I needed the system to be developable, testable and demonstrable without a paid API key.

**A** — I made the LLM provider pluggable — OpenAI, Gemini, a local HuggingFace model, or a mock — configured by a single setting, and I made **mock the default**. That meant the whole pipeline around the model, which is most of the system, could be exercised without any key or any spend. It also meant I wasn't locked to one provider if a free tier changed.

**R** — The project runs, tests and demos with no API key, and it's deployed and working end to end on free infrastructure.

---

## Story 6 — Teamwork and a shared outcome
**Prompts:** *"Tell me about working in a team." · "A successful team project." · "Your role in a group."*

**S** — Sugarcane Pest Detection was built as Team Deepcrop for Agrithon 2.0, a DBT-sponsored hackathon at VIT.

**T** — **`[YOU FILL IN: team size, and which parts were specifically yours]`**

**A** — **`[YOU FILL IN: how the work was divided, and how you coordinated]`** On my side, **`[YOU FILL IN: your components]`**. The integration point that needed the most agreement was the fusion step, where the image score and the questionnaire score combine — we settled on weighting the image 0.6 and the questionnaire 0.4, and made the weights configurable rather than hard-coded so they could be changed without a redeploy.

**R** — **We won first prize at Agrithon 2.0**, and the system is deployed and working end to end.

> ⚠️ **This is the story most likely to catch you out.** Be precise about what was yours. Claiming
> the whole system is the single easiest thing for an interviewer to unpick, and you do not need to
> — "I built the X and Y components, and we won first prize" is already a strong answer.

---

## Story 7 — Explaining something technical to a non-technical person
**Prompts:** *"Explain a technical concept simply." · "Communicating with non-technical stakeholders."*

**S** — The Sugarcane system is meant for farmers and agri-extension workers, not engineers.

**T** — The output had to be trustworthy to someone who has no reason to trust a model's number.

**A** — Rather than returning a bare confidence score, the system returns the image with the detected region drawn on it — the mask or box overlaid on the plant. So the user sees *where* the model thinks the symptom is, not just what it concluded. We also designed the questionnaire as plain symptom questions rather than technical parameters.

**R** — The result is explainable at a glance: a farmer can look at the overlay and judge for themselves whether the system is looking at the right part of the plant.

> **This doubles as your answer to "how do you make ML trustworthy?"**

---

## Story 8 — Working with senior people
**Prompts:** *"Tell me about working with someone more experienced." · "Receiving feedback." · "Working under guidance."*

**S** — I'm a co-inventor on two published patent applications, both with faculty at VIT — one on a secure toll management system with cryptographic authentication and transaction sequencing, one on a federated physics-informed neural network for semiconductor quality control.

**T** — **`[YOU FILL IN: your specific contribution to each — be precise and modest]`**

**A** — **`[YOU FILL IN: how you worked with the faculty member, what you were responsible for, how feedback was handled]`**

**R** — Both applications were filed in spring 2026 and have since been published (application numbers 202641056093 and 202641065392). Your own context file notes that the specification is dated April 2026 while the resume says May: confirm the month from your paperwork before you state one.

> ⚠️ **Say "published patent applications", never "patents".** They are filed and published, not
> granted. Getting this wrong costs you credibility on everything else.

---

## Story 9 — A deadline under pressure
**Prompts:** *"Tell me about working under pressure." · "A tight deadline." · "Prioritising."*

**S** — Agrithon 2.0 was a hackathon, so the whole Sugarcane build happened against a fixed deadline. **`[YOU FILL IN: how long you actually had]`**

**T** — We needed a working end-to-end demo, not a collection of parts.

**A** — The decision that mattered was scoping to **two pests** — Dead Heart and Tiller — rather than trying to cover more. That kept the model work tractable and let us spend time on the thing judges would actually see: the full flow from photo upload through to an explained result. **`[YOU FILL IN: what you personally cut or deprioritised]`**

**R** — We had a working end-to-end system at the deadline, and **won first prize**.

> **The transferable point:** cutting scope to protect the demo. Say that explicitly — it is exactly
> the judgement a services firm wants.

---

## Story 10 — A weakness, or something you'd do differently
**Prompts:** *"What's your biggest weakness?" · "What would you do differently?" · "Tell me about a mistake."*

**Use a real one. This one is real and it is safe, because it is about rigour rather than competence.**

> "Across both of my main projects, I built things that work but I didn't build a way to *measure*
> how well they work. In the Sugarcane system the fusion weights — 0.6 image, 0.4 questionnaire —
> are a reasoned default, not a measured optimum. In the RAG project I can tell you it returns
> citations, but I can't tell you how often the retrieved chunk actually contains the answer.
>
> I noticed it when I was preparing to talk about these projects and realised I couldn't give an
> accuracy number I'd stand behind. What I've taken from it is that 'it works' and 'I can show you
> how well it works' are different standards, and the second one is what makes a result defensible.
> So on the open-source side I've been writing tests first — the Learning Unlimited module had none,
> and that was the contribution I made.
>
> It's still the thing I'd fix first if I went back to either project."

> **Why this works:** it is a genuine limitation, it is specific, it does not disguise a strength as
> a weakness, and it ends with concrete evidence that you are already acting on it. **It also
> inoculates you** — if they later ask "how accurate is it?", you have already framed the answer.

---

## Mapping — prompt to story

| If they ask… | Use |
|---|---|
| Difficult technical problem / debugging | **1** |
| Learning something new fast / unfamiliar tech | **2** |
| Initiative / going beyond the ask / quality | **3** |
| Difficult decision / trade-off | **4** |
| Limited resources / constraints | **5** |
| Teamwork / your role in a group | **6** |
| Explaining to non-technical people | **7** |
| Working with seniors / receiving feedback | **8** |
| Pressure / deadlines / prioritising | **9** |
| Weakness / mistake / do differently | **10** |
| Proudest achievement | **6** or **2** |
| Conflict in a team | **`[YOU FILL IN — no true story for this in your material. Prepare one or say honestly that you haven't hit a significant one]`** |
| Leadership | **6** or **9**, but only if you genuinely led. Otherwise say so |

---

## Before you rehearse

1. **Fill in every `[YOU FILL IN]` truthfully.** A story with a gap you improvise under pressure is
   how fabrications happen.
2. **Say each one out loud, timed.** Target 75 seconds. Most run long on Situation.
3. **For each, ask yourself: "what's the obvious follow-up?"** Then prepare that answer too.
4. **Cut anything you cannot defend.** Every time.
