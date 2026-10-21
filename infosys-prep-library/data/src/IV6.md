## 2. Exactly what gets asked

Two AI questions were asked in one first-hand 2025 interview `[REPORTED]` (B5): **“What is your opinion of generative AI?”** and **“How do you use AI in your daily life?”** The drive email frames the whole programme around an “**AI-driven vision**” and says Infosys wants to assess “technical and behavioural competencies” (`research/00-official-terms.md`). Infosys describes itself as AI-first (its Topaz offering, described on infosys.com as “an AI-first set of services, solutions and platforms”), so expect at least one AI question in 2026 `[INFERRED]`.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Opinion | “What do you think about generative AI?” | B5 |
| Personal use | “How do you use AI in daily life?” | B5 |
| Risk and responsibility | hallucination, privacy, jobs | likely follow-ups `[INFERRED]` |
| Basic vocabulary | LLM, prompt, RAG, fine-tuning | likely follow-ups `[INFERRED]` |

## 3. Concept notes

### 3.1 A three-part answer to the opinion question

1. **Value:** it speeds up drafting, explaining and coding; give one concrete example from your own work.
2. **Limits:** it can be wrong with confidence (hallucination), it reflects its training data, and it can leak private data if used carelessly.
3. **Your rule:** you verify what it says, you keep confidential data out, and you stay responsible for the final result.

### 3.2 A true “daily use” answer

Use only what is true. From your own record: you built a **RAG application whose answers cite the exact page and chunk** so they can be checked; you hold the **Azure AI Fundamentals (AI-900)** certification, which covers responsible-AI principles and generative AI services; and you use AI tools while studying and coding. Say *how* you use them and *how you check them*.

### 3.3 Vocabulary to use correctly

| Term | One line |
|---|---|
| LLM | A neural network trained on large text data to predict the next token |
| Hallucination | Fluent output that is false |
| Prompt | The instruction and context given to the model |
| RAG | Retrieve relevant text first, then let the model answer from it, usually with citations |
| Fine-tuning | Further training a model on your own data |
| Token | A small piece of text the model reads and writes |

### 3.4 What not to say

Do not say AI will replace all developers, or that you never use it. Do not call a tool “100% accurate”. Do not claim to have trained a model you did not train.

## 4. Must-memorise block

| Item | Line |
|---|---|
| Why citations matter | They make a RAG answer checkable |
| Your safeguard | Verify, do not paste confidential data, own the result |
| Responsible-AI principles (AI-900) | Fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability |
| Limitation | RAG reduces hallucination; it does not remove it |

## 5. Worked examples

**Example 1 — opinion.** “Generative AI is a strong assistant, not a replacement for judgement. It helps me explain an unfamiliar codebase or draft a test quickly. The risk is that it is fluent even when wrong, so I check its output against the code or the source. In my RAG project I made the model cite the page it used for exactly that reason.”

**Example 2 — daily use.** “I use it to explain things I am learning and to draft first versions of code or text. I always run the code and read the sources before I rely on anything. I keep private or confidential material out of public tools.”

**Example 3 — “Will AI take your job?”** “It will change the work. Routine tasks will be automated, and people who can design, verify and explain systems will be more valuable. That is why I build and check things end to end.”

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Hype | Sounds uncritical | Name a limit |
| “I never use it” | Not credible and not aligned with the company | Say how you use it and check it |
| Buzzwords without meaning | One follow-up exposes it | Use only terms from the table |
| Claiming a metric | No evaluation exists | “Not measured” |
| Ignoring privacy | A services firm handles client data | Mention confidentiality |

## 8. Resources

- **https://www.infosys.com/services/data-ai-topaz.html** — Infosys's own description of its AI-first offering.
- **https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/** — the AI-900 syllabus, for vocabulary you already studied.

## 9. Self-check

1. Can you give a 30-second opinion on generative AI with one example and one limit?
2. Can you say how you use AI and how you check it?
3. Can you define RAG in one sentence and say why citations help?
4. Which six principles does responsible AI name?
5. What will you say if asked whether AI will take developer jobs?
