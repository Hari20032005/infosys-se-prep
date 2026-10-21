---
title: Data sufficiency
code: A6
section: Reasoning Ability
weightage_pct: 2.5% of marks
est_questions: 1.89
tier: 1
difficulty: Medium
est_study_hours: 0.8
confidence: High
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/L2-data-sufficiency.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A6 — Data sufficiency

*Adapted from `L&T/lt-prep-library/topics/L2-data-sufficiency.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **1.9 questions and 1.9 marks** on this topic (about 2.5% of the 75 scored marks). It sits in **Reasoning Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 1**, 0.8 hours to reach reliable recall, confidence **High**.

**6 questions on this topic are in the observed Infosys pool** (R04, O06, O07, O08, O09, O10), from 2 sources. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 2.36 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

| ID | Source date | What was asked |
|---|---|---|
| O06 | 2020-09-22 | How many litres of juice can 375 trees give (oranges per tree; one cup per orange)? |
| O07 | 2020-09-22 | Three consecutive integers X, Y, Z in no fixed order: which is highest? |
| O08 | 2020-09-22 | Rs 4 in 50-paisa and one-rupee coins: how many 50-paisa coins? |
| O09 | 2020-09-22 | Alloy in ratio 8:6:3:1, zinc Rs 30/kg: cost of copper per kg? |
| O10 | 2020-09-22 | Is 2000 the average GRE score? (range given; half above, half below 2000) |
| R04 | 2026-09-22 | What is the smallest of four consecutive even numbers? I. Their sum is 132. II. The difference between the smallest and the largest is 6. |

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



Every data sufficiency question hands you a question stem plus two statements, gives no diagram, and asks which of the statements are enough to answer it. The answer is never the numerical value. The answer is one of five fixed options.

The five options are always the same shape:

| Letter | Meaning |
|---|---|
| a) | Statement 1 alone is sufficient, statement 2 alone is not |
| b) | Statement 2 alone is sufficient, statement 1 alone is not |
| c) | Both statements together are sufficient, neither alone is |
| d) | Either statement alone is sufficient |
| e) | Both statements together are still not sufficient |

Some papers reorder these letters. Read the option block once before you start reading the statements, because the ordering is the one thing a careless candidate gets wrong.

The critical discipline: **you decide sufficiency without computing the answer**. If a question asks "what is the value of x" and statement 1 gives you a single linear equation in x, statement 1 is sufficient immediately, even if you never solve it. Conversely, if a statement gives you two unknowns in one equation, it is insufficient even if the arithmetic looks inviting. The exam is testing whether you can stop yourself from calculating.

Sub-patterns observed in this family:

| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Age / number word problems | "What is Ravi's age?" with ratio and sum statements | Common |
| Linear equations in 2-3 variables | "What is the value of x + y?" with equations in x and y | Common |
| Averages and totals | "What is the average of five numbers?" with partial sums | Occasional |
| Ratio and proportion | "What is the ratio a:b?" with two ratio relations | Occasional |
| Geometry (area, perimeter) | Shape question where a statement fixes one dimension only | Occasional |
| Percentage / profit-loss | Cost price and selling price given separately | Occasional |
| Counting / sets | "How many students play both games?" with totals | Rare |
| Miscellaneous direct | Single statement gives the answer outright | Occasional |

## 3. Concept notes

### 3.1 The core rule

The question asks: **given this much information, can the answer be uniquely determined?**

"Sufficient" means the statement pins down exactly one possible value or configuration. It does not mean the statement is true, relevant in spirit, or numerically large. A statement that produces two possible answers is insufficient, however close they are.

### 3.2 The unique-solution test

This is the single most important rule in the topic. For a question asking for the value of an unknown expression, a statement is sufficient if and only if it leaves exactly one possible value.

Rule: **an equation in n distinct unknowns, on its own, is insufficient for n > 1.**

Example: "x + y = 10" alone cannot fix x + y's components, so any question asking for x alone is unanswered by it. But a question asking for x + y is answered instantly: the target expression itself is given.

Rule: **n independent equations in n unknowns are sufficient.**

Example: "x + y = 10" and "x − y = 2" together fix x = 6 and y = 4. Both together are sufficient; neither alone is.

Rule: **a single equation whose only unknown is the target is sufficient.**

Example: "3x = 21" alone gives x = 7. Sufficient, no second statement needed.

### 3.3 The "question asks for a combination" shortcut

Many stems ask for a combined expression: x + y, x − y, x² − y², xy, 2x + 3y. These are frequently answerable from statements that would never answer "what is x?"

Worked reasoning: to get **x² − y²** you only need (x + y)(x − y). A statement giving x + y = 8 and another giving x − y = 3 together settle it. You never need x or y individually.

A statement giving **x² + y² = 25** is not sufficient for x + y on its own. Two different pairs, (3, 4) and (4, 3), give different x + y values (7 and 7 — same here, but (−3, 4) gives 1 and (3, −4) gives −1). Signs matter.

### 3.4 The two-value trap

A statement that looks sufficient but yields two values is insufficient. Standard cases:

- **x² = 16** gives x = 4 or x = −4. Two values. Insufficient for "what is x?" unless the stem also fixes x's sign or says x is positive.
- **|x| = 6** gives x = 6 or x = −6. Same problem.
- **Quadratic with two real roots** gives two values unless one root is excluded by a condition.

Fast rule: whenever squaring or absolute value enters, check the sign constraint in the stem. If the stem says "x is a positive integer", x² = 16 collapses to 4 and the statement becomes sufficient.

### 3.5 Geometry sufficiency

For any shape, you need enough information to fix the relevant measurements.

| Target | Minimum needed |
|---|---|
| Rectangle area | Both length and breadth (equivalently area or the pair) |
| Rectangle perimeter | l + b (sum suffices, individual values not needed) |
| Circle area | Radius, or diameter, or circumference |
| Triangle area | Base and height, or three sides, or two sides and included angle |
| Cube volume | Edge length |
| Cylinder volume | r and h |

A statement giving only the perimeter of a rectangle cannot give its area. Example: l + b = 10 is satisfied by (4, 6) with area 24 and (5, 5) with area 25. Different areas. Insufficient.

### 3.6 Averages and totals

Average = Total / Count. So:

- To find the average of n numbers, you need the total (and n).
- A statement giving the sum directly is sufficient.
- A statement giving each number individually is sufficient, but wasteful.
- A statement giving the average and one missing element is rarely sufficient for that element unless the count is also known.

Rule: **the count must be known to convert between average and total.** A statement "the average of a set is 12" does not fix the total unless you know how many elements the set has.

### 3.7 Ratio sufficiency

A ratio a:b = 3:5 fixes the relationship, not the values. It is sufficient for any question about the ratio itself (a:b, b:a, (a+b):b) and insufficient for any question about absolute values unless a scale is supplied.

Example: "a:b = 3:5" answers "what is (a + b)/b?" (it is 8/5). It does not answer "what is a?" A second statement giving a = 12 makes it sufficient.

### 3.8 The "either alone" reading

Option d) — either statement alone — is the least-chosen and most-missed option. It requires you to test statement 1 alone and statement 2 alone independently and find both sufficient by different routes.

Example: "What is the value of x?" Statement 1: 2x + 3 = 11, so x = 4. Statement 2: x − 1 = 3, so x = 4. Each alone suffices. The answer is d), not c).

### 3.9 Execution protocol

Follow this order every time. It costs about 40 seconds and prevents every error mode.

1. Read the stem. Identify exactly what is asked: a value, a ratio, a yes/no, a comparison.
2. Read statement 1 alone. Ignore statement 2 completely. Ask: does this produce one answer? Note sufficient or not.
3. Read statement 2 alone. Ignore statement 1 completely. Ask the same.
4. If both insufficient alone, combine them. Ask if the combination produces one answer.
5. Map to the option block.

The most common error is contaminating statement 1's judgement with statement 2's information. Never do this.

## 4. Must-memorise block

- **The five canonical options.** "1 alone", "2 alone", "both together", "either alone", "neither".
- **n equations in n unknowns → sufficient. Fewer equations than unknowns → not sufficient.**
- **A single equation with only the target unknown → sufficient.**
- **A question asking for a combined expression needs only the combination, not the components.**
- **x² = k has two solutions (±√k) unless the sign is constrained.**
- **|x| = k has two solutions (±k) unless the sign is constrained.**
- **Average = Total / Count. Total known + Count known → Average known.**
- **A ratio alone never fixes absolute values.**
- **Rectangle area needs BOTH l and b. Perimeter needs only l + b.**
- **Circle area needs r. Circumference gives r, therefore circumference is sufficient for area.**
- **"How many" questions need a count, not a rate.**
- **Option d) means each statement independently suffices. It is rarer, not impossible.**

## 5. Worked examples

### Example 1

**Question:** What is the value of x + y?

Statement 1: x − y = 4
Statement 2: x² − y² = 20

**Fast method.** Statement 1 alone: one equation, two unknowns, cannot give x + y. Insufficient.

Statement 2 alone: x² − y² = (x + y)(x − y) = 20. Two unknowns in one equation. Insufficient alone.

Together: substitute x − y = 4 into (x + y)(x − y) = 20, giving 4(x + y) = 20, so x + y = 5. Sufficient.

**Answer: c) Both together are sufficient, neither alone.**

The slow method — solving for x and y individually — takes three times as long and arrives at the same letter. The combination shortcut is the whole point of the question.

### Example 2

**Question:** What is the value of x?

Statement 1: x² = 25
Statement 2: x is a negative integer

**Fast method.** Statement 1 alone gives x = 5 or x = −5. Two values. Insufficient.

Statement 2 alone says nothing about x's magnitude. Insufficient.

Together: the only negative integer satisfying x² = 25 is x = −5. Sufficient.

**Answer: c).**

The trap is treating statement 1 as sufficient. Signs matter. This exact shape appears regularly.

### Example 3

**Question:** What is the area of rectangle R?

Statement 1: The perimeter of R is 20 cm.
Statement 2: The diagonal of R is 5 cm.

**Fast method.** Statement 1: 2(l + b) = 20, so l + b = 10. Area = l × b is not fixed by the sum. (4, 6) gives 24; (5, 5) gives 25. Insufficient.

Statement 2 alone: l² + b² = 25. One equation, two unknowns. Insufficient.

Together: l + b = 10 and l² + b² = 25. From the first, (l + b)² = 100, so l² + b² + 2lb = 100, giving 25 + 2lb = 100, so lb = 37.5. Area = 37.5. Sufficient.

**Answer: c).**

Note the fast route: you never solve for l and b. You only need the product lb. Recognising that l² + b² and l + b combine to give lb is the whole skill.

### Example 4

**Question:** What is the average of five numbers?

Statement 1: The sum of the five numbers is 150.
Statement 2: Each number is a multiple of 5.

**Fast method.** Statement 1 alone: Average = Total / Count = 150 / 5 = 30. Sufficient.

Statement 2 alone: no values given. Insufficient.

**Answer: a).**

This is the case where option a) is correct and you must not waste time on statement 2. The stem supplies the count; statement 1 supplies the total. Done.

### Example 5

**Question:** What is the value of the two-digit number N?

Statement 1: The sum of its digits is 9.
Statement 2: The difference between its digits is 1.

**Fast method.** Statement 1 alone: pairs summing to 9 are (1,8), (2,7), (3,6), (4,5) and reverses. Also 90, 09, 81, ... many numbers. Insufficient.

Statement 2 alone: pairs differing by 1 are (1,2), (2,3), ..., (8,9) and reverses. Many numbers. Insufficient.

Together: digit pairs summing to 9 and differing by 1. Solving a + b = 9 and a − b = 1 gives a = 5, b = 4, so N is 54. But reversing: b + a = 9 and b − a = 1 gives a = 4, b = 5, so N is 45. Two valid two-digit numbers, 54 and 45.

**Answer: e) Both together are still not sufficient.**

This is the trap that catches people. The arithmetic produces a clean-looking answer, and the candidate forgets the digit reversal. The question asks for the two-digit number, and both 45 and 54 satisfy the statements.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Computing the answer instead of judging sufficiency | The mind wants to solve; sufficiency is a yes/no judgement | Stop the moment you can say "one value" or "more than one value" |
| Letting statement 2 influence the judgement of statement 1 | You read both before deciding, and unconsciously combine them | Physically cover statement 2 with your hand while reading statement 1 |
| Missing the two-value case from squaring or absolute value | x² = 16 feels like x = 4 | Every time you see a square or modulus, ask "what about the negative?" |
| Forgetting digit reversal in number questions | 45 and 54 both satisfy the clues | For any two-digit number question, always test the reversed pair |
| Assuming a ratio fixes absolute values | "a:b = 3:5" reads like real numbers | A ratio is a relationship; it needs a scale to become values |
| Confusing area needs (l and b) with perimeter needs (l + b) | The formulas look similar | Perimeter is a sum; area is a product. A sum never gives a product |
| Missing option d) because it is rare | Candidates default to c) when both look useful | Test each statement alone first, in isolation, before combining |
| Assuming "both together" because four equations sound generous | More equations with more unknowns can still be underdetermined | Count distinct unknowns after substitution, not equations listed |
| Ignoring an integer / positive constraint in the stem | x² = 25 with "x is positive" collapses to 5 | Re-read the stem's qualifiers before judging statement 1 |
| Solving a question that is already insufficient | Arithmetic feels productive | If a statement has two unknowns and no constraint, stop immediately |

## 7. Practice questions

Every question below uses the **same four options in the same order.** That order is a convention, not a variable - learn it once and you never re-read it. **Do not shuffle these options**, in this file or any other: in data sufficiency the option letters carry fixed meanings.

```
a) Statement 1 alone is sufficient, statement 2 alone is not
b) Statement 2 alone is sufficient, statement 1 alone is not
c) Both together are sufficient, but neither alone is
d) Both together are still not sufficient
```

**1.** What is the value of x? **Statement 1:** 4x + 7 = 31. **Statement 2:** x squared = 36.

**2.** What is the value of p + q? **Statement 1:** p - q = 6. **Statement 2:** p squared - q squared = 30.

**3.** What is the average of four numbers? **Statement 1:** Their sum is 96. **Statement 2:** Each number is even.

**4.** What is the ratio a:b? **Statement 1:** a + b = 25. **Statement 2:** 2a = 3b.

**5.** What is the area of a circle? **Statement 1:** Its radius is an even number of centimetres. **Statement 2:** Its circumference is 12*pi cm.

**6.** What is the value of y? **Statement 1:** y is a negative integer. **Statement 2:** y squared = 49.

**7.** What is the value of x + 2y? **Statement 1:** x + y = 10. **Statement 2:** y = 4.

**8.** What is the two-digit number N? **Statement 1:** The sum of its digits is 7. **Statement 2:** The product of its digits is 12.

**9.** Is the integer m divisible by 6? **Statement 1:** m is divisible by 3. **Statement 2:** m is even.

**10.** What is the area of rectangle R? **Statement 1:** Its length is twice its breadth. **Statement 2:** Its perimeter is 36 cm.

**11.** What is the value of x? **Statement 1:** x + y = 12. **Statement 2:** 2x + 6 = 20.

**12.** What is the two-digit number M? **Statement 1:** M is a multiple of 9. **Statement 2:** The sum of its digits is 9.

### ANSWER KEY

**1. a)** S1 gives x = 6 uniquely. S2 gives x = +6 or -6 - two values, so it cannot pin x down. **A square root always offers two candidates**, and this is the most common DS trap there is.

**2. c)** Neither alone works. Together, p squared - q squared = (p+q)(p-q) = 30 and p - q = 6, so p + q = 30/6 = 5. You never need p or q separately - **DS asks whether the value is determined, not what it is.**

**3. a)** S1 gives the sum, and average = 96/4 = 24. S2 says nothing about the total. Note you never need the individual numbers.

**4. b)** S1 fixes a total, not a ratio - a:b could be 1:24 or 12:13. S2 gives 2a = 3b, so a:b = 3:2. **A ratio needs a relationship, not a total.**

**5. b)** S1 narrows the radius to even values but leaves infinitely many. S2 gives 2×π×r = 12π, so r = 6 and the area is 36π sq cm.

**6. c)** S1 leaves infinitely many integers. S2 gives y = +7 or -7. Together the negative constraint selects y = -7.

**7. c)** S1 alone leaves both unknowns free; S2 alone gives no x at all. Together x = 6, so x + 2y = 6 + 8 = 14.

**8. d)** S1 allows 16, 25, 34, 43, 52, 61, 70. S2 allows 26, 62, 34, 43. Together **both 34 and 43 survive** - two answers, so the data is still insufficient. Verified by enumeration.

**9. c)** Neither alone decides it. Together m is divisible by both 2 and 3, hence by 6 - a definite YES. **For a yes/no question a firm NO would count as sufficient too**; what matters is that the answer is settled.

**10. c)** S1 gives shape without size, S2 size without shape. Together l = 2b and 2(l+b) = 36 give b = 6, l = 12, area = 72 sq cm.

**11. b)** S1 has two unknowns and settles nothing. S2 alone gives 2x = 14, so x = 7. **Scan for a statement that resolves on its own before you start combining.**

**12. d)** S1 allows ten values: 18, 27, 36, 45, 54, 63, 72, 81, 90 and **99**. S2 allows nine - 99 is excluded, because its digits sum to 18, not 9. Together nine values survive, so the data is still insufficient. The trap is assuming the two statements are equivalent: **the divisibility rule is that the digit sum is a multiple of 9, not that it equals 9.** Verified by enumeration.


## 8. Resources

- **Data Sufficiency in Logical Reasoning** — https://www.geeksforgeeks.org/aptitude/data-sufficiency/ — page content not classified - read it before relying on it.
- **Data Sufficiency in Logical Reasoning** — https://www.geeksforgeeks.org/aptitude/data-sufficiency/ — page content not classified - read it before relying on it.
- **Logical Reasoning Questions and Answers** — https://www.indiabix.com/logical-reasoning/ — index of question sets - open a sub-topic for the actual questions.

## 9. Self-check

1. Can you state the five canonical data-sufficiency options from memory without reading them?
2. Do you instinctively ask "one value or more than one?" before reaching for arithmetic?
3. Can you spot the two-value case in a squared or absolute-value statement within five seconds?
4. Do you cover statement 2 while evaluating statement 1, rather than reading both at once?
5. Can you identify when a question asks for a combination (x + y, x² − y²) that needs fewer facts than the individual variables?
6. Do you test option d) — either statement alone — instead of defaulting to c)?

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/L2-data-sufficiency.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions R04, O06, O07, O08, O09, O10 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A6`). Confidence **High**. Nothing in this file is a published Infosys syllabus.
