---
title: Syllogisms and logical deduction
code: A4
section: Reasoning Ability
weightage_pct: 2.2% of marks
est_questions: 1.63
tier: 2
difficulty: Medium
est_study_hours: 0.8
confidence: High
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/L6-syllogisms-and-logical-deduction.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A4 — Syllogisms and logical deduction

*Adapted from `L&T/lt-prep-library/topics/L6-syllogisms-and-logical-deduction.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **1.6 questions and 1.6 marks** on this topic (about 2.2% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 2**, 0.8 hours to reach reliable recall, confidence **High**.

**6 questions on this topic are in the observed Infosys pool** (R10, O11, O12, O13, O14, O15), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.03 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O11 | 2020-09-22 | Nurses, demand, efficient: choose the three related statements (multi-select) |
| O12 | 2020-09-22 | Rohan, jesters, magicians, criminals: choose the three related statements (multi-select) |
| O13 | 2020-09-22 | Books, novels, fiction: which triple is logically related? |
| O14 | 2020-09-22 | Painters, farmers, choreographers: which triple is logically related? |
| O15 | 2020-09-22 | Fishes, swimmers, carnivorous: which triple is logically related? |
| R10 | 2025-09-29 | Statements: All shoes are legs. Some legs are pairs. Some pairs are hands. Conclusions: I. Some hands are shoes. II. Some pairs are shoes. |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Two-statement syllogism | "All A are B. Some B are C." Then 4-5 conclusions; pick which follow | Most common by far |
| Three-statement syllogism | Chain of All/Some/No; ask which conclusion is valid | Common |
| Possibility conclusions | "Which is a possibility?" - needs the possibility rule, not certainty | Frequent |
| "Either-or" conclusion pair | Two conclusions where exactly one must hold | Occasional |
| Statement + course of action | Given a situation, decide which action logically follows | Occasional |
| Statement + assumption / inference | Mark the hidden assumption or the direct inference | Occasional |
| Blood-relation or direction deduction | Short coded deduction, 2-3 steps | Occasional, overlaps L5/L7 |

Count the conclusion set, not the statements. A 5-conclusion question costs 5 quick checks, but each check is mechanical once the Venn is drawn.

## 3. Concept notes

### 3.1 The four statement types

| Type | Form | Venn picture |
|---|---|---|
| Universal affirmative | **All A are B** | A fully inside B |
| Universal negative | **No A is B** | A and B fully disjoint |
| Particular affirmative | **Some A are B** | A and B overlap by at least one element |
| Particular negative | **Some A are not B** | At least one element of A lies outside B |

### 3.2 The three-line diagram method (the fast method)

Draw only what the statements force. Then test each conclusion against **every** diagram consistent with the statements. A conclusion follows only if it is true in all of them.

Rule: if you can draw one valid diagram where the conclusion fails, the conclusion does not follow.

### 3.3 Immediate inference rules

- **All A are B** gives **Some B are A** (valid - overlap is non-empty), and **Some A are B** (valid).
- **No A is B** gives **No B is A** (valid - disjointness is symmetric).
- **Some A are B** gives **Some B are A** (valid - overlap is symmetric).
- **Some A are not B** gives **Some A are not B** only; you may **not** convert it to "Some B are not A". The element outside B may or may not be in B's complement in a way that gives B elements. This is the single most exploited trap.

### 3.4 The two-statement chain rules

- All A are B + All B are C → **All A are C**. Also gives Some A are C, Some C are A.
- All A are B + No B is C → **No A is C**. Also No C is A.
- All A are B + Some B are C → **No definite conclusion**. "Some A are C" is a *possibility*, not a certainty, because the Some-B could sit outside A.
- Some A are B + All B are C → **Some A are C**. Also Some C are A.
- Some A are B + No B is C → **Some A are not C**.
- No A is B + All B are C → **Some C are not A** (the B-part is outside A).
- Two "Some" statements → **no conclusion**.
- Two "No" statements → **no conclusion** in either direction beyond the stated disjointness.

### 3.5 The possibility rule

A conclusion is a **possibility** when at least one consistent diagram makes it true, and no statement forbids it.

- All A are B ⇒ "Some A are B" is a possibility (and in fact a certainty).
- All A are B ⇒ "Some A are not B" is **not** possible; it is contradicted.
- Some A are B ⇒ "All A are B" **is** a possibility. This surprises people; a single overlap does not forbid full containment.
- No A is B ⇒ "Some A are B" is impossible.

Shortcut line: **possibility = can be drawn without breaking a statement.**

### 3.6 The either-or rule

For the pair "Some A are B" and "Some A are not B" to be an either-or answer, both must individually fail, and they must be exact complements. Then exactly one must hold. If both fail and they are not complements, nothing follows.

### 3.7 The complement table

| Conclusion | Complement |
|---|---|
| All A are B | Some A are not B |
| Some A are B | No A is B |
| No A is B | Some A are B |
| Some A are not B | All A are B |

### 3.8 Course of action

An action follows only if it is (a) practical for the authority named, and (b) directly aimed at fixing the stated problem. Actions that are morally nice but unrelated are rejected. "Both I and II follow" is a normal answer.

## 4. Must-memorise block

**Statement meanings**
- **All A are B** = A ⊆ B
- **No A is B** = A ∩ B = ∅
- **Some A are B** = A ∩ B ≠ ∅
- **Some A are not B** = A − B ≠ ∅

**Conversions**
- All A are B → Some B are A ✔
- Some A are B → Some B are A ✔ (two-way)
- No A is B → No B is A ✔ (two-way)
- Some A are not B → **no valid converse** ✘

**Chain results (definite conclusions only)**
- All + All → All ✔
- All + No → No ✔
- All + Some → **nothing certain** (only a possibility)
- Some + All → Some ✔
- Some + No → **Some A are not C** ✔
- Some + Some → nothing ✘
- No + All → **Some C are not A** ✔

**Possibility**
- Possibility is allowed unless a statement forbids it.
- **Some A are B ⇒ "All A are B" is possible.**

**Either-or**
- Both conclusions must fail alone AND be complements.

**Time budget**
- Two-statement syllogism: **20 seconds**
- Three-statement: **35 seconds**
- If over 45 seconds, mark and move. No negative marking means never leave a blank.

## 5. Worked examples

**Example 1.** Statements: All dogs are mammals. All mammals are animals. Conclusions: I. All dogs are animals. II. Some animals are dogs.
Fast method: All + All → All, so I follows. All A are B gives Some B are A, so II follows. **Both follow.**
Slow method: drawing three circles costs 40 seconds for the same result.

**Example 2.** Statements: All pens are books. Some books are red. Conclusions: I. Some pens are red. II. Some red are books.
I: All + Some → nothing certain; the red books may lie outside the pen set. Fails. II: direct conversion of "Some books are red". Follows. **Only II follows.**

**Example 3.** Statements: No cat is a dog. All dogs are pets. Conclusions: I. Some pets are not cats. II. No pet is a cat.
I: No + All → Some C are not A, i.e. Some pets are not cats. Follows. II: the pet set includes cats? Not forbidden, and not forced. Not a certainty. **Only I follows.**

**Example 4.** Statements: Some A are B. Some B are C. Conclusion: Some A are C.
Two Some statements give nothing. Draw A and C as separate overlaps on B - the conclusion fails. **Does not follow.** A frequent wrong answer is "follows", which is exactly why this pattern is set.

**Example 5.** Statements: Some roses are flowers. Conclusion: All roses are flowers.
Under the possibility rule, a single overlap does not forbid full containment, so "All roses are flowers" is a **valid possibility**. If the question says "definitely follows", the answer is no; if it says "is a possibility", the answer is **yes**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Converting "Some A are not B" | Feels symmetric like the other three | Memorise: this one does **not** convert |
| Reading "Some" as "only some" | Everyday English implies a part, not an overlap | In logic, Some = at least one, possibly all |
| Assuming "All + Some" chains | Looks like a chain, is not one | All + Some → no definite conclusion |
| Treating possibility as certainty | Both are asked with near-identical wording | Look for the word "possibility" in the stem |
| Drawing one diagram and stopping | One diagram can make a false conclusion look true | Test the counter-diagram before answering |
| Ignoring the either-or requirement | Picking a pair where only one fails | Both must fail, and they must be complements |
| Choosing "Both follow" too fast | Two conclusions look compatible | Verify each independently |
| Blank answers | Fear of being wrong | **No negative marking - never leave a blank** |

## 7. Practice questions

1. Statements: All A are B. All B are C. Conclusions: I. All A are C. II. Some C are A.
a) Only I follows b) Only II follows c) Neither follows d) Both follow

2. Statements: Some P are Q. All Q are R. Conclusions: I. Some P are R. II. All R are P.
a) Neither follows b) Only II follows c) Both follow d) Only I follows

3. Statements: No X is Y. All Y are Z. Conclusions: I. Some Z are not X. II. No Z is X.
a) Both follow b) Only II follows c) Only I follows d) Neither follows

4. Statements: All cats are animals. Some animals are wild. Conclusion: Some cats are wild.
a) Does not follow b) Follows c) Follows only if no wild is a cat d) Cannot be determined but likely true

5. Statements: Some cups are saucers. Conclusion: All cups are saucers.
a) Definitely follows b) Is a possibility c) Definitely does not follow d) Contradicts the statement

6. Statements: All engineers are graduates. Some graduates are managers. Conclusions: I. Some engineers are managers. II. Some managers are graduates.
a) Only I follows b) Only II follows c) Both follow d) Neither follows

7. Statements: Some A are B. Some B are C. Conclusions: I. Some A are C. II. Some C are A.
a) Only I follows b) Only II follows c) Neither follows d) Both follow

8. Statements: All roses are flowers. No flower is a stone. Conclusions: I. No rose is a stone. II. Some stones are roses.
a) Only I follows b) Only II follows c) Both follow d) Neither follows

9. Statements: No doctor is a lawyer. Some lawyers are rich. Conclusions: I. Some rich are not doctors. II. No rich person is a doctor.
a) Only II follows b) Only I follows c) Both follow d) Neither follows

10. Statements: All M are N. All N are O. Some O are P. Conclusions: I. All M are O. II. Some P are M.
a) Neither follows b) Only II follows c) Both follow d) Only I follows

11. Statements: Some books are novels. No novel is a magazine. Conclusions: I. Some books are not magazines. II. All books are magazines.
a) Both follow b) Only II follows c) Only I follows d) Neither follows

12. Statements: All keys are locks. Some locks are doors. All doors are windows. Conclusions: I. Some locks are windows. II. Some keys are windows.
a) Only I follows b) Only II follows c) Both follow d) Neither follows

### ANSWER KEY

1. **d)** All + All chains to All A are C, and All A are B gives Some C are A.
2. **d)** Some + All gives Some P are R; "All R are P" reverses a particular and fails.
3. **c)** No + All gives Some Z are not X; Z may still overlap X, so II fails.
4. **a)** All + Some gives no definite conclusion; wild animals may lie outside cats.
5. **b)** A single overlap does not forbid full containment, so All cups are saucers is possible.
6. **b)** All + Some gives nothing for I; II is straightforward conversion of Some graduates are managers.
7. **c)** Two Some statements yield no conclusion in any direction.
8. **a)** All + No gives No rose is a stone; II contradicts the statements outright.
9. **b)** Some lawyers are rich, and no lawyer is a doctor, so some rich are not doctors; II is not forced.
10. **d)** All M are N and All N are O chain to All M are O; the Some O are P branch gives nothing about M.
11. **c)** The books that are novels lie outside the magazine set, so some books are not magazines; II contradicts.
12. **a)** Some locks are doors and All doors are windows give Some locks are windows; the keys branch never meets doors.

## 8. Resources

- **Syllogism - Verbal Reasoning Questions and Answers** — https://www.indiabix.com/verbal-reasoning/syllogism/ — MCQ set with options, answers and explanations (verified).
- **Syllogism** — https://www.geeksforgeeks.org/aptitude/syllogism/ — page content not classified - read it before relying on it.
- **Logical Deduction - Logical Reasoning Questions and Answers** — https://www.indiabix.com/logical-reasoning/logical-deduction/ — MCQ set with options, answers and explanations (verified).
- **Statement and Assumption - Logical Reasoning Questions and Answers** — https://www.indiabix.com/logical-reasoning/statement-and-assumption/ — MCQ set with options, answers and explanations (verified).
- **Syllogism - Wikipedia** — https://en.wikipedia.org/wiki/Syllogism — reference article.

## 9. Self-check

1. Can you state the four statement types and their Venn meanings without looking?
2. Do you know instantly that "Some A are not B" does not convert?
3. Can you produce the definite conclusions for All+All, All+No, Some+All, Some+No, and No+All?
4. Do you apply the possibility rule correctly, including "Some A are B ⇒ All A are B is possible"?
5. Can you state both conditions for an either-or pair to be the answer?
6. Can you finish a two-statement syllogism in under 25 seconds without a full diagram?

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/L6-syllogisms-and-logical-deduction.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions R10, O11, O12, O13, O14, O15 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A4`). Confidence **High**. Nothing in this file is a published Infosys syllabus.
