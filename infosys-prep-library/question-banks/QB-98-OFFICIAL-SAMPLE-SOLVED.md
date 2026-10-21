# QB-98 — The official sample paper, solved

**Source:** Infosys's own sample test for Systems Engineer, a PDF made by Infosys Ltd in September 2020: [open the PDF](https://infytq.onwingspan.com/public-assets/InfosysCampusRecruitmentSampleTest-SystemsEngineer.pdf). Open it beside this file; the question numbers below are the PDF's own.

**What this is.** 54 questions in five timed sections (Reasoning 25 min, Technical 35 min, Verbal 20 min, Pseudocode 10 min, Puzzle 10 min). It is the only first-party sample question paper I could find for this exam, which is why it ranks above every video and blog in this library (see `../research/05-source-credibility.md`).

**What this is not.**
- It is a **2020** sample with five sections. The 2027-batch test is reported to have seven. Treat it as the best evidence of *question style*, not of the current section counts.
- The PDF has a CONFIDENTIAL watermark although it sits at a public address. So this file links to it and gives only a **paraphrased gist** of each question plus my own answer and working. Nothing is copied.
- The PDF **has no answer key**. Every answer here was worked out for this library, not copied from anywhere.

**How each answer was decided** (31 by running code · 21 by judgement · 2 not solved):
- *decided by running code*: brute force over the real constraints, a simulation, or a model search. Re-run it with `python3 data/official_sample.py`; it exits non-zero if any check fails.
- *judgement*: verbal and unit-reasoning items. These are the least certain answers in the library, so read the reason, not just the letter.
- *NOT SOLVED*: the two multi-select deduction items. They never say which triples count as "related", and the key is not published, so no answer is invented.

Two answers deserve a warning. Deductive items 3 to 5 (O13 to O15 here) are answered on the reading that *the first two statements must entail the third*; on a looser reading the answer to O15 changes. The code states both readings.

---


## Section 1: Reasoning Ability · logic set: a thief, three computers (data interpretation)

### O01 · logic set: a thief, three computers (data interpretation) · question 1

- **Asks (paraphrased):** Thief, three computers, three tools: which tool was used on Tejas?
- **Answer:** wire cutter
- **Why:** Enumerate all assignments; exactly one satisfies every clue
- **How decided:** decided by running code · topic `A19`

### O02 · logic set: a thief, three computers (data interpretation) · question 2

- **Asks (paraphrased):** Same set: in which month was the keyboard taken?
- **Answer:** February
- **Why:** Same unique assignment
- **How decided:** decided by running code · topic `A19`

### O03 · logic set: a thief, three computers (data interpretation) · question 3

- **Asks (paraphrased):** Same set: which peripheral did Prithvi lose?
- **Answer:** printer
- **Why:** Same unique assignment
- **How decided:** decided by running code · topic `A19`

### O04 · logic set: a thief, three computers (data interpretation) · question 4

- **Asks (paraphrased):** Same set: in which month was the wire cutter used? (fill in)
- **Answer:** March
- **Why:** Same unique assignment
- **How decided:** decided by running code · topic `A19`

### O05 · logic set: a thief, three computers (data interpretation) · question 5

- **Asks (paraphrased):** Same set: which computer lost its monitor?
- **Answer:** Tejas
- **Why:** Same unique assignment
- **How decided:** decided by running code · topic `A19`


## Section 1: Reasoning Ability · data sufficiency

### O06 · data sufficiency · question 1

- **Asks (paraphrased):** How many litres of juice can 375 trees give (oranges per tree; one cup per orange)?
- **Answer:** 4 (cannot be determined)
- **Why:** A cup is not a volume in litres, so no statement fixes the answer
- **How decided:** judgement (no machine check possible) · topic `A6`

### O07 · data sufficiency · question 2

- **Asks (paraphrased):** Three consecutive integers X, Y, Z in no fixed order: which is highest?
- **Answer:** 3 (both together)
- **Why:** Enumerated every assignment of three consecutive integers: I alone and II alone each leave two candidates; together only X
- **How decided:** decided by running code · topic `A6`

### O08 · data sufficiency · question 3

- **Asks (paraphrased):** Rs 4 in 50-paisa and one-rupee coins: how many 50-paisa coins?
- **Answer:** 1 (one statement alone: the second)
- **Why:** Enumerated (a, b): "fewer 50p than Re 1 coins" leaves two cases; "five coins in total" leaves one
- **How decided:** decided by running code · topic `A6`

### O09 · data sufficiency · question 4

- **Asks (paraphrased):** Alloy in ratio 8:6:3:1, zinc Rs 30/kg: cost of copper per kg?
- **Answer:** 4 (neither, even together)
- **Why:** Two different cost vectors satisfy both statements but give copper at Rs 250 and Rs 260
- **How decided:** decided by running code · topic `A6`

### O10 · data sufficiency · question 5

- **Asks (paraphrased):** Is 2000 the average GRE score? (range given; half above, half below 2000)
- **Answer:** 4 (neither, even together)
- **Why:** Two data sets fit both statements, one with mean 2000 and one without; "half above" describes the median, not the mean
- **How decided:** decided by running code · topic `A6`


## Section 1: Reasoning Ability · deductive reasoning

### O11 · deductive reasoning · question 1

- **Asks (paraphrased):** Nurses, demand, efficient: choose the three related statements (multi-select)
- **Answer:** not solved
- **Why:** Multi-select with no stated rule for which triple counts; the official key is not published, so no answer is asserted
- **How decided:** NOT SOLVED · topic `A4`

### O12 · deductive reasoning · question 2

- **Asks (paraphrased):** Rohan, jesters, magicians, criminals: choose the three related statements (multi-select)
- **Answer:** not solved
- **Why:** Same: multi-select, key not published
- **How decided:** NOT SOLVED · topic `A4`

### O13 · deductive reasoning · question 3

- **Asks (paraphrased):** Books, novels, fiction: which triple is logically related?
- **Answer:** a (ADE)
- **Why:** "Only novels are fiction" plus "some books are not novels" give "some books are not fiction" (first two entail the third); only ADE passes
- **How decided:** decided by running code · topic `A4`

### O14 · deductive reasoning · question 4

- **Asks (paraphrased):** Painters, farmers, choreographers: which triple is logically related?
- **Answer:** c (ACE)
- **Why:** "All painters are choreographers" plus "some painters are farmers" give "some farmers are choreographers"; only ACE
- **How decided:** decided by running code · topic `A4`

### O15 · deductive reasoning · question 5

- **Asks (paraphrased):** Fishes, swimmers, carnivorous: which triple is logically related?
- **Answer:** d (none of the above)
- **Why:** On the reading that the first two statements must entail the third, none of DCB, EDA, BEC works (B and C entail E, but BEC puts E second). On an unordered reading BEC would be the answer; the official key is not published
- **How decided:** decided by running code · topic `A4`


## Section 2: Technical Ability · mathematical questions

### O16 · mathematical questions · question 1

- **Asks (paraphrased):** LET + LEE = ALL with E = 5: find A + L + L
- **Answer:** c (value 5; L=1, T=6, A=3)
- **Why:** Brute force over all digit assignments: exactly one solution
- **How decided:** decided by running code · topic `A20`

### O17 · mathematical questions · question 2

- **Asks (paraphrased):** 5 distinct chocolates into 3 distinct containers, none empty: ways?
- **Answer:** b (150)
- **Why:** 3^5 - 3·2^5 + 3 = 150, confirmed by listing all 243 assignments
- **How decided:** decided by running code · topic `A18`

### O18 · mathematical questions · question 3

- **Asks (paraphrased):** Arrangements of KEYBOARD with the vowels only in odd places?
- **Answer:** a (2880)
- **Why:** P(4,3) × 5! = 24 × 120, confirmed by listing all 40,320 arrangements
- **How decided:** decided by running code · topic `A18`

### O19 · mathematical questions · question 4

- **Asks (paraphrased):** Missing term in 0, 2, 5, 10, 17, _, 41
- **Answer:** 28
- **Why:** Gaps are the consecutive primes 2, 3, 5, 7, 11, 13
- **How decided:** decided by running code · topic `A2`

### O20 · mathematical questions · question 5

- **Asks (paraphrased):** 8 L drawn from a can of milk and replaced by water, four times in all; milk : total = 16 : 81. Original quantity?
- **Answer:** c (24 litres)
- **Why:** (1 - 8/x)^4 = 16/81 gives 1 - 8/x = 2/3, so x = 24
- **How decided:** decided by running code · topic `A9`


## Section 2: Technical Ability · logic set: who attends the wedding

### O21 · logic set: who attends the wedding · question 1

- **Asks (paraphrased):** Wedding guests with if-then rules: if Qhorin comes, who must stay away?
- **Answer:** e (nobody is forced to stay away)
- **Why:** Checked all 128 attendance patterns against the four rules
- **How decided:** decided by running code · topic `A19`

### O22 · logic set: who attends the wedding · question 2

- **Asks (paraphrased):** If Ramsay does not come, what must be true?
- **Answer:** b (Umar does not come)
- **Why:** No Ramsay forces Petyr and Qhorin to come, and Petyr coming rules Umar out; checked all 128 patterns
- **How decided:** decided by running code · topic `A19`

### O23 · logic set: who attends the wedding · question 3

- **Asks (paraphrased):** If Umar comes, which statement must NOT be true?
- **Answer:** c (Ramsay does not come)
- **Why:** If Umar comes, Petyr cannot, so Ramsay must come; checked all 128 patterns
- **How decided:** decided by running code · topic `A19`

### O24 · logic set: who attends the wedding · question 4

- **Asks (paraphrased):** Which listed group could be exactly the attendees?
- **Answer:** e (none of the listed groups works)
- **Why:** Each listed group breaks at least one rule
- **How decided:** decided by running code · topic `A19`

### O25 · logic set: who attends the wedding · question 5

- **Asks (paraphrased):** Who can attend regardless of who else attends?
- **Answer:** Varys (and also Qhorin)
- **Why:** Adding them never breaks a rule, because neither appears on the "if" side of any rule
- **How decided:** decided by running code · topic `A19`


## Section 3: Verbal Ability · critical reasoning (strengthen, weaken, inference)

### O26 · critical reasoning (strengthen, weaken, inference) · question 1

- **Asks (paraphrased):** Computer chips from Japan and US missile accuracy: which statement strengthens the argument?
- **Answer:** a
- **Why:** It ties missile accuracy to computer quality, the link the argument needs
- **How decided:** judgement (no machine check possible) · topic `V6`

### O27 · critical reasoning (strengthen, weaken, inference) · question 2

- **Asks (paraphrased):** Ethanol blending and "Jetrol": which statement weakens the argument?
- **Answer:** a
- **Why:** A fuel that pollutes three times more removes the claimed benefit
- **How decided:** judgement (no machine check possible) · topic `V6`

### O28 · critical reasoning (strengthen, weaken, inference) · question 3

- **Asks (paraphrased):** Health of income groups (heights, infant deaths): what can be inferred?
- **Answer:** c
- **Why:** Nutrition is one factor and is not without significance; the others overreach
- **How decided:** judgement (no machine check possible) · topic `V6`


## Section 3: Verbal Ability · English Corrective Usage (fill in the blank)

### O29 · English Corrective Usage (fill in the blank) · question 1

- **Asks (paraphrased):** Fill the blank after "raises transaction costs and ___ in the economy"
- **Answer:** a (inefficiencies)
- **Why:** The only noun that fits "transaction costs and ..."
- **How decided:** judgement (no machine check possible) · topic `G1`

### O30 · English Corrective Usage (fill in the blank) · question 2

- **Asks (paraphrased):** Fill the blank: majority of emotional and physical problems ___ the stresses of life
- **Answer:** c (have their origins in)
- **Why:** Plural subject, "origins in"
- **How decided:** judgement (no machine check possible) · topic `G1`

### O31 · English Corrective Usage (fill in the blank) · question 3

- **Asks (paraphrased):** Fill the blank: music retailing relies on walk-ins and ___
- **Answer:** a (impulse purchase)
- **Why:** Walk-in customers buy on impulse
- **How decided:** judgement (no machine check possible) · topic `G1`

### O32 · English Corrective Usage (fill in the blank) · question 4

- **Asks (paraphrased):** Fill the blank: what has happened since is a ___ of fortune
- **Answer:** b (startling reversal)
- **Why:** "Reversal of fortune" is the fixed phrase
- **How decided:** judgement (no machine check possible) · topic `G1`


## Section 3: Verbal Ability · English Error Correction (best phrasing of the underlined part)

### O33 · English Error Correction (best phrasing of the underlined part) · question 1

- **Asks (paraphrased):** Skeptics emphasise conditions that fluctuate "and also has ..." : best replacement
- **Answer:** b (and have a significant psychological component)
- **Why:** Plural subject "conditions" needs "have"
- **How decided:** judgement (no machine check possible) · topic `V3`

### O34 · English Error Correction (best phrasing of the underlined part) · question 2

- **Asks (paraphrased):** Dutch Health Council found "none of the evidence ... were harmful": best replacement
- **Answer:** c (no evidence ... was harmful)
- **Why:** Singular uncountable "evidence" takes "was"
- **How decided:** judgement (no machine check possible) · topic `V3`

### O35 · English Error Correction (best phrasing of the underlined part) · question 3

- **Asks (paraphrased):** Fear of an enemy "is definitely to be an instinctive quality": best replacement
- **Answer:** c (is certainly an instinctive quality)
- **Why:** Removes the awkward "definitely to be"
- **How decided:** judgement (no machine check possible) · topic `V3`

### O36 · English Error Correction (best phrasing of the underlined part) · question 4

- **Asks (paraphrased):** Globalization "too uses ... relationships as well for creating": best replacement
- **Answer:** b (social and political relationships to create)
- **Why:** Plural noun and "to create"; removes the redundancy
- **How decided:** judgement (no machine check possible) · topic `V3`


## Section 3: Verbal Ability · English Error Identification (identify the correct sentence)

### O37 · English Error Identification (identify the correct sentence) · question 1

- **Asks (paraphrased):** Passionate efforts "on their own have the ability ...": which sentence is correct?
- **Answer:** 1
- **Why:** Plural subject, plural pronoun, plural verb, "legendary"
- **How decided:** judgement (no machine check possible) · topic `V2`

### O38 · English Error Identification (identify the correct sentence) · question 2

- **Asks (paraphrased):** Another relief for airlines and shipping: which sentence is correct?
- **Answer:** 3
- **Why:** "in relation to" and "hospitality" are right; the others have "An other", "have", "hospitability"
- **How decided:** judgement (no machine check possible) · topic `V2`

### O39 · English Error Identification (identify the correct sentence) · question 3

- **Asks (paraphrased):** Power sector gains if the coal scheme works: which sentence is correct?
- **Answer:** 2
- **Why:** "can gain ... scheme ... works" agrees in number and tense
- **How decided:** judgement (no machine check possible) · topic `V2`

### O40 · English Error Identification (identify the correct sentence) · question 4

- **Asks (paraphrased):** Earning endorsements is a primary challenge: which sentence is correct?
- **Answer:** 3
- **Why:** "is one of the primary challenges that we face every day"
- **How decided:** judgement (no machine check possible) · topic `V2`


## Section 3: Verbal Ability · reading comprehension

### O41 · reading comprehension · question 1

- **Asks (paraphrased):** Shakespeare's comedies: what is noted about the techniques?
- **Answer:** b (consistently employed in his comedies)
- **Why:** The passage says they stay consistent across the comedies
- **How decided:** judgement (no machine check possible) · topic `V1`

### O42 · reading comprehension · question 2

- **Asks (paraphrased):** What is the content of Shakespeare's comedies?
- **Answer:** a (love and marriage)
- **Why:** Stated directly
- **How decided:** judgement (no machine check possible) · topic `V1`

### O43 · reading comprehension · question 3

- **Asks (paraphrased):** Which statement is understood from the passage?
- **Answer:** b (techniques consistently evident in all his comedies)
- **Why:** Matches the passage; the others misstate it
- **How decided:** judgement (no machine check possible) · topic `V1`

### O44 · reading comprehension · question 4

- **Asks (paraphrased):** Where is the lower class made fun of (Dogberry and Verges)?
- **Answer:** d (Much Ado About Nothing)
- **Why:** Named in the passage
- **How decided:** judgement (no machine check possible) · topic `V1`

### O45 · reading comprehension · question 5

- **Asks (paraphrased):** Why are the comedies treasured?
- **Answer:** d (the intuitive use of the techniques)
- **Why:** The closing sentence
- **How decided:** judgement (no machine check possible) · topic `V1`


## Section 4: Pseudocode (2 marks each) · pseudocode

### O46 · pseudocode · question 1

- **Asks (paraphrased):** Number = 90 tested against 90 < Number < 95: what is displayed?
- **Answer:** b (not within the range)
- **Why:** The condition 90 > 90 is false, so the else branch runs
- **How decided:** decided by running code · topic `P6`

### O47 · pseudocode · question 2

- **Asks (paraphrased):** a=6, b=3, c=2 with a three-way condition, else a=b+1: print a+b+c
- **Answer:** 9
- **Why:** Condition is false, so a = 4; 4 + 3 + 2 = 9
- **How decided:** decided by running code · topic `P6`

### O48 · pseudocode · question 3

- **Asks (paraphrased):** Loop i = 1..5 printing k, then j = j+1, k = k+j: which series?
- **Answer:** a (1 3 6 10 15)
- **Why:** Trace j and k each pass: triangular numbers
- **How decided:** decided by running code · topic `P1`

### O49 · pseudocode · question 4

- **Asks (paraphrased):** Function with while(b): temp = a MOD b ... called with a=10, b=6
- **Answer:** a (2)
- **Why:** This is Euclid's algorithm: gcd(10, 6) = 2
- **How decided:** decided by running code · topic `P7`

### O50 · pseudocode · question 5

- **Asks (paraphrased):** For i from 1 to 1, for j from i to 1: print k+1 with k = 6
- **Answer:** c (7)
- **Why:** The body runs once: 6 + 1 = 7
- **How decided:** decided by running code · topic `P1`


## Section 5: Puzzle · number puzzles

### O51 · number puzzles · question 1

- **Asks (paraphrased):** 3x3 grids: first grid's row sums are 12, 15, 18; fill the missing cell of the second (3 marks)
- **Answer:** c (9)
- **Why:** Row sums rise by 3 and carry on into the second grid: 21, 24, 27, so 7 + 5 + ? = 21
- **How decided:** decided by running code · topic `Z1`

### O52 · number puzzles · question 2

- **Asks (paraphrased):** Plus figures: arms 7,4,6,8 give 50 and 1,12,20,7 give 80; find the centre for 13,11,9,14 (2 marks)
- **Answer:** b (94)
- **Why:** Centre = 2 × (sum of the four arms)
- **How decided:** decided by running code · topic `Z2`

### O53 · number puzzles · question 3

- **Asks (paraphrased):** Circles 4→64 and 3→27 give 98; 6→216 and 2→8 give 232; third pair 9→729 and A→125 (2 marks)
- **Answer:** A = 5 (a) and B = 868 (c)
- **Why:** Each box = cube + cube + sum of the two small numbers: 64+27+7 = 98; 216+8+8 = 232; so A = 5 and B = 729+125+14
- **How decided:** decided by running code · topic `Z2`

### O54 · number puzzles · question 4

- **Asks (paraphrased):** Rows 16,25,36,49,64 → 14,16,22,23 → 12,X,9: find X (3 marks)
- **Answer:** 11
- **Why:** Each number is the digit-sum of its upper-left neighbour plus the digit-sum of its upper-right neighbour
- **How decided:** decided by running code · topic `Z2`


## What this paper tells you

| Topic | Items in this paper |
|---|---|
| `A19` | 10 (O01, O02, O03, O04, O05, O21, O22, O23, O24, O25) |
| `A4` | 5 (O11, O12, O13, O14, O15) |
| `A6` | 5 (O06, O07, O08, O09, O10) |
| `V1` | 5 (O41, O42, O43, O44, O45) |
| `G1` | 4 (O29, O30, O31, O32) |
| `V2` | 4 (O37, O38, O39, O40) |
| `V3` | 4 (O33, O34, O35, O36) |
| `V6` | 3 (O26, O27, O28) |
| `Z2` | 3 (O52, O53, O54) |
| `A18` | 2 (O17, O18) |
| `P1` | 2 (O48, O50) |
| `P6` | 2 (O46, O47) |
| `A2` | 1 (O19) |
| `A20` | 1 (O16) |
| `A9` | 1 (O20) |
| `P7` | 1 (O49) |
| `Z1` | 1 (O51) |

Logic sets (`A19`, `A6`, `A4`) are 20 of the 25 questions in the Reasoning and Technical sections of this paper, so they are worth more practice than a plain topic-count suggests. Practise data sufficiency on the **1 / 2 / 3 / 4** scale used here (the banks `QB-A6-…`, `QB-A19-…`, `QB-A4-…` do). Pseudocode uses a numbered-line dialect with `Set`, `For (each i from a to b)`, `End-for` and `MOD`; the bank `QB-P1-…` prints its traces in exactly that dialect.
