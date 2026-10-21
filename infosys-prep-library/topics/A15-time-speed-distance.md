---
title: Time, speed, distance and trains
code: A15
section: Technical Ability
weightage_pct: 0.7% of marks
est_questions: 0.53
tier: 4
difficulty: Medium
est_study_hours: 1.0
confidence: Low
last_updated: 2026-09-30
adapted_from: L&T/lt-prep-library/topics/Q2-time-speed-distance-and-trains.md
---
<!-- Drafted by DeepSeek V4.1 Flash via ds.py; reviewed by Claude 2026-09-21. Answer
     letters rebalanced by data/shuffle.py (correctness-preserving: option text is
     swapped and the key letter repointed). Numeric keys re-checked by
     data/verify_keys.py. -->

# A15 — Time, speed, distance and trains

*Adapted from `L&T/lt-prep-library/topics/Q2-time-speed-distance-and-trains.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

Expect about **0.5 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 4**, 1.0 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1, V1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.32 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

### What Infosys asked

No question on this topic was recovered. Listed by: C1, V1.

> The pattern notes below come from the library this file was adapted from. Any frequency or "observed paper" remark in them describes that source paper, not Infosys. The Infosys evidence is the table above.



**Observed on an old (probably 2007-08) IndiaBIX paper:** *"Distance between two poles is 50 m, train at 48 kmph, how many poles crossed in one minute?"* The source publishes **no answer key**, and the question is ambiguous: the train covers 800 m, which is **16 gaps**. That is 16 poles if the train starts between poles, or **17 if the pole at the starting instant is counted**. The skill being tested is noticing the fencepost, then reading the wording or the options to decide which count is meant.

| Sub-pattern | How it appears | Roughly how often |
|---|---|---|
| Unit conversion | kmph ↔ m/s as a stand-alone step, or the first half of any train question | 1 of every 2 train questions |
| Train crossing a pole / man | Given length + speed, find time (or reverse) | ~1 question |
| Train crossing a platform / bridge | (train + platform) length over speed | ~1 question |
| Two trains crossing each other | Opposite direction: sum speeds; same direction: difference | ~1 question |
| Poles / trees / posts at fixed gaps | Fencepost: gaps + 1 | 1 observed question |
| Boats and streams | Downstream/upstream pair, find boat or stream speed | occasionally |
| Average speed over two legs | Harmonic mean, equal distances | occasionally |

## 3. Concept notes

### 3.1 The conversion that solves half the paper

Speed in kmph → multiply by **5/18** to get m/s.
Speed in m/s → multiply by **18/5** to get kmph.

Example: 72 kmph = 72 × 5/18 = **20 m/s**. Example: 25 m/s = 25 × 18/5 = **90 kmph**.

Reason: 1 km = 1000 m, 1 hour = 3600 s, so 1 kmph = 1000/3600 = 5/18 m/s.

Do this in your head, not on paper: divide by 18 then multiply by 5 (or the reverse). 90 ÷ 18 = 5, × 5 = 25. That is a two-second operation.

### 3.2 Distance, speed, time

**Distance = Speed × Time**. **Speed = Distance / Time**. **Time = Distance / Speed**.

Keep units consistent. If speed is kmph, time must be in hours; if speed is m/s, time must be in seconds. Most train questions are m/s and seconds; most car/travel questions are kmph and hours.

### 3.3 Relative speed

- **Same direction:** relative speed = **difference** of the two speeds.
- **Opposite direction:** relative speed = **sum** of the two speeds.

Example: 60 kmph and 40 kmph in the same direction → a gap closes at 20 kmph. In opposite directions → it closes at 100 kmph.

The classic use: closing time = initial gap ÷ relative speed.

### 3.4 Trains

| Situation | Distance to cover | Formula |
|---|---|---|
| Crossing a pole, tree, or a standing man | Train length only | Time = L / v |
| Crossing a platform the same length as a person walking | Train length + platform length | Time = (L + P) / v |
| Two trains, opposite directions | L₁ + L₂ | Time = (L₁ + L₂) / (v₁ + v₂) |
| Two trains, same direction | L₁ + L₂ | Time = (L₁ + L₂) / (v₁ − v₂) |

The rule behind all four: a train has *cleared* an object only when its **last point** has passed the **far end** of that object. That is why a pole needs only the train's own length, but a platform needs both lengths.

### 3.5 Boats and streams

Let **b** = speed of boat in still water, **s** = speed of stream.

- Downstream (with the current): **d = b + s**
- Upstream (against the current): **u = b − s**
- **b = (d + u) / 2**
- **s = (d − u) / 2**

Example: downstream 12 kmph, upstream 8 kmph → boat = 10 kmph, stream = 2 kmph.

### 3.6 Average speed

Average speed is **total distance ÷ total time**, never the plain average of the two speeds.

For **two equal distances** covered at x and y, the average speed is the harmonic mean:

**Average speed = 2xy / (x + y)**

Example: 40 kmph out, 60 kmph back → 2(40)(60)/100 = **48 kmph**, not 50.

### 3.7 Poles, gaps and the fencepost

If poles are **G** metres apart and a train covers **D** metres, then:

- Number of **gaps** = D / G
- Number of **poles passed** = **D / G + 1**

The train passes a pole at the start of the first gap and another at the end of the last one. That extra pole is the whole trap.

Example: 50 m gaps, 800 m covered → 16 gaps → **17 poles if the starting pole is counted**, otherwise 16.

## 4. Must-memorise block

| Item | Value |
|---|---|
| **kmph → m/s** | **× 5/18** |
| **m/s → kmph** | **× 18/5** |
| Distance / Speed / Time | **D = S × T** |
| Same-direction relative speed | **v₁ − v₂** |
| Opposite-direction relative speed | **v₁ + v₂** |
| Train past a pole | **T = L / v** |
| Train past a platform | **T = (L + P) / v** |
| Two trains crossing | **T = (L₁ + L₂) / relative speed** |
| Downstream | **b + s** |
| Upstream | **b − s** |
| Boat in still water | **(d + u) / 2** |
| Stream speed | **(d − u) / 2** |
| Average speed, equal distances | **2xy / (x + y)** |
| **Poles at gap G, distance D** | **poles = D/G + 1** |

Instant conversions worth having cold: 18 kmph = 5 m/s · 36 = 10 · 54 = 15 · 72 = 20 · 90 = 25 · 108 = 30.

## 5. Worked examples

**Example 1 (the observed question).** Poles are 50 m apart. A train runs at 48 kmph. How many poles does it cross in one minute?

Step 1: 48 kmph = 48 × 5/18 = 40/3 m/s.
Step 2: distance in 60 s = (40/3) × 60 = 800 m.
Step 3: gaps = 800 / 50 = 16.
Step 4: poles = 16 gaps, or **16 + 1 = 17 if the pole at the starting instant is counted**. Decide from the wording; if both 16 and 17 are offered, look for "including the first" or "starting at a pole".

The slow method — sketching poles on a timeline — takes three minutes. The fast method is the formula plus one addition.

**Example 2.** A train 240 m long crosses a pole in 12 s. Find its speed and its time to cross a 360 m platform.

Speed = 240 / 12 = 20 m/s = 20 × 18/5 = **72 kmph**.
Platform: distance = 240 + 360 = 600 m; time = 600 / 20 = **30 s**.

Note the trap: people answer 360/20 = 18 s. The train must also clear its own 240 m.

**Example 3.** Two trains, 120 m and 180 m, run in opposite directions at 42 kmph and 30 kmph. How long until they have fully crossed each other?

Relative speed = 42 + 30 = 72 kmph = 72 × 5/18 = 20 m/s.
Total distance = 120 + 180 = 300 m.
Time = 300 / 20 = **15 s**.

**Example 4.** A boat covers 24 km downstream in 3 hours and the same 24 km upstream in 4 hours. Find the stream speed.

Downstream = 24/3 = 8 kmph. Upstream = 24/4 = 6 kmph.
Stream = (8 − 6) / 2 = **1 kmph**. (Boat in still water = (8+6)/2 = 7 kmph.)

**Example 5.** A car covers the first half of a journey at 40 kmph and the second half at 60 kmph. Find the average speed.

Fast method: 2xy/(x+y) = (2 × 40 × 60) / 100 = 4800/100 = **48 kmph**.

The slow method works but wastes time: take total 120 km, so 60 km each way. Times are 1.5 h and 1 h, total 2.5 h; 120/2.5 = 48 kmph. The losing move is answering "50 kmph" by averaging the speeds — that is the trap, and it is always wrong.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Averaging two speeds arithmetically | Feels intuitive; 40 and 60 "obviously" give 50 | Always use **2xy/(x+y)** for equal distances, or actual total distance ÷ total time |
| Forgetting the train's own length on a platform | You see "platform 360 m" and use only that | Distance is always **L + P** |
| Using the wrong relative speed | Sum and difference are easy to swap | Same direction = subtract (slower train falls behind); opposite = add |
| Mixing kmph with seconds | Numbers are given in different units in the same question | Convert to m/s and seconds the moment a train length appears |
| Fencepost: reporting gaps as poles | 800/50 = 16 gaps feels like a complete answer | **Poles = gaps + 1 only if the starting pole is counted.** Read the wording |
| Reading "crosses a man walking" as a pole | A walking man moves, so relative speed applies | If the man moves, use relative speed; if he stands, use train speed |
| Boat: confusing boat-with-current and boat-in-still-water | The question asks for the wrong one of the two | Label b and s; compute b = (d+u)/2 and s = (d−u)/2 separately |
| Time lost on arithmetic | 48 × 5/18 done long-hand eats 40 seconds | Memorise the 18→5 table: 36=10, 54=15, 72=20, 90=25 |

## 7. Practice questions

1. A train 180 m long runs at 54 kmph. How long does it take to pass a pole?
a) 10 s b) 11 s c) 12 s d) 15 s

2. Convert 90 kmph into metres per second.
a) 27 m/s b) 25 m/s c) 22.5 m/s d) 32.4 m/s

3. A train 300 m long crosses a platform 200 m long in 25 seconds. Its speed is:
a) 72 kmph b) 60 kmph c) 75 kmph d) 80 kmph

4. Two trains, 100 m and 150 m long, move in the same direction at 60 kmph and 48 kmph. How long until the faster has completely passed the slower?
a) 50 s b) 60 s c) 70 s d) 75 s

5. A boat covers 24 km downstream in 3 hours and returns the same distance in 4 hours. The speed of the stream is:
a) 0.5 kmph b) 2 kmph c) 3 kmph d) 1 kmph

6. A man walks 6 km at 5 kmph and a further 6 km at 8 kmph. His average speed for the whole journey is:
a) 6.0 kmph b) 6.5 kmph c) 6.15 kmph d) 7.0 kmph

7. A train running at 72 kmph crosses a bridge 400 m long in 30 seconds. The length of the train is:
a) 120 m b) 160 m c) 240 m d) 200 m

8. Poles are fixed 50 m apart along a track. A train runs at 48 kmph. The timer starts at the instant its front is level with one pole, and that pole is counted. How many poles has the front passed after one minute?
a) 15 b) 17 c) 16.5 d) 16

9. Two trains, 120 m and 180 m long, approach each other at 42 kmph and 30 kmph. How long until they have completely crossed?
a) 15 s b) 12 s c) 18 s d) 20 s

10. A train leaves a station at 8 am at 60 kmph. A second train leaves the same station on the same track at 9 am at 80 kmph. At what time does the second train catch the first?
a) 11 am b) 11:30 am c) 12 noon d) 12:30 pm

11. Two stations are 300 km apart. Trains leave both stations at the same time towards each other at 40 kmph and 60 kmph. They meet after:
a) 3 h b) 2.5 h c) 3.5 h d) 4 h

12. A train 110 m long passes a man standing on a platform in 3 seconds and completely clears the same platform in 12 seconds. The length of the platform is:
a) 110 m b) 330 m c) 275 m d) 220 m

### ANSWER KEY

1. **c)** 54 × 5/18 = 15 m/s; 180 / 15 = 12 s.
2. **b)** 90 × 5/18 = 25 m/s.
3. **a)** (300 + 200) / 25 = 20 m/s; 20 × 18/5 = 72 kmph.
4. **d)** Relative = 12 kmph = 10/3 m/s; (100 + 150) / (10/3) = 75 s.
5. **d)** Down = 8 kmph, up = 6 kmph; stream = (8 − 6) / 2 = 1 kmph.
6. **c)** Harmonic mean = (2 × 5 × 8) / 13 = 80/13 ≈ 6.15 kmph.
7. **d)** 72 kmph = 20 m/s; 30 × 20 = 600 m total; 600 − 400 = 200 m.
8. **b)** 48 kmph = 40/3 m/s; 60 s → 800 m; 800/50 = 16 gaps; the starting pole is counted, so 16 + 1 = 17.
9. **a)** Relative = 72 kmph = 20 m/s; (120 + 180) / 20 = 15 s.
10. **c)** At 9 am the lead is 60 km; closing speed 20 kmph; 60/20 = 3 h after 9 am = 12 noon.
11. **a)** Relative = 40 + 60 = 100 kmph; 300 / 100 = 3 h.
12. **b)** Speed = 110/3 m/s; 12 s gives (110/3) × 12 = 440 m; platform = 440 − 110 = 330 m.

## 8. Resources

- **Time and Distance - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/time-and-distance/ — MCQ set with options, answers and explanations (verified).
- **Problems on Trains - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/problems-on-trains/ — MCQ set with options, answers and explanations (verified).
- **Boats and Streams - Aptitude Questions and Answers** — https://www.indiabix.com/aptitude/boats-and-streams/ — MCQ set with options, answers and explanations (verified).
- **Speed, Time and Distance – Solved Questions and Answers** — https://www.geeksforgeeks.org/aptitude/time-speed-distance/ — index of question sets - open a sub-topic for the actual questions.
- **Harmonic mean - Wikipedia** — https://en.wikipedia.org/wiki/Harmonic_mean — reference article.

## 9. Self-check

1. Can you convert 54, 72 and 90 kmph to m/s in under three seconds each, without writing anything?
2. Can you state the four train-crossing formulas (pole, platform, opposite, same direction) from memory?
3. Do you stop and decide whether the pole at the start counts before you add 1 to the number of gaps?
4. Can you derive boat and stream speeds from a downstream/upstream pair without hesitating?
5. Do you reach for 2xy/(x+y) the moment a question mentions two speeds over the same distance?
6. Can you finish any of the twelve practice questions above in under 60 seconds, on paper, without checking the key?

If you answered no to any of these, re-read sections 3 and 4 before moving on.

## 10. Sources

**Teaching content (§3–§9)** is adapted from `L&T/lt-prep-library/topics/Q2-time-speed-distance-and-trains.md`, which lists its own sources and was verified in that library's QA. **Infosys evidence** for this file: observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A15`). Confidence **Low**. Nothing in this file is a published Infosys syllabus.
