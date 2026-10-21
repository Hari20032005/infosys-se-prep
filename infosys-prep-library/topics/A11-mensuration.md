---
title: Mensuration: area, surface area, volume
code: A11
section: Technical Ability
weightage_pct: 1.5% of marks
est_questions: 1.16
tier: 3
difficulty: Medium
est_study_hours: 0.7
confidence: Medium
last_updated: 2026-09-30
---

# A11 — Mensuration: area, surface area, volume

## 1. Why this topic matters here

Expect about **1.2 questions and 1.2 marks** on this topic (about 1.5% of the 75 scored marks). It sits in **Technical Ability**, part of the 25-question aptitude block (Reasoning Ability 15 Q / 25 min + Technical Ability 10 Q / 35 min, one cut-off each). **Tier 3**, 0.7 hours to reach reliable recall, confidence **Medium**.

**1 question on this topic are in the observed Infosys pool** (Q08), from 1 source. They are listed in §2 and solved in `../question-banks/QB-99-OBSERVED-POOL.md`.

**Why the tier:** expected marks per study hour, weighted by confidence, is 1.32 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

One observed item (a sphere: surface area given, volume asked) `[REPORTED]`; the topic is also named by the 2025 pattern deck under Technical Ability (C1). Questions are short and formula-driven; the trap is always the formula, not the arithmetic.

| Sub-pattern | How it appears | Observed |
|---|---|---|
| Sphere: surface area ↔ volume | "Surface area of a sphere is 154 cm². Find its volume" | Q08 |
| Cylinder and cone: volume, curved area, total area | authored from the syllabus | — |
| Rectangle: diagonal, area from perimeter, path around a lawn | authored from the syllabus | — |

## 3. Concept notes

### 3.1 Solve for the radius first

Almost every solid question is one step from its radius. Area → radius → volume, or volume → radius → area.

### 3.2 Use π = 22/7

With radii that are multiples of 7 (or 3.5, 10.5, 21), π = 22/7 makes the arithmetic finish cleanly. Say so in your working: “(π = 22/7)”.

### 3.3 Sphere

Surface area = 4πr². Volume = (4/3)πr³.
Q08: 4πr² = 154 → r² = 154 × 7 / (4 × 22) = 12.25 → r = 3.5. Volume = (4/3)(22/7)(3.5)³ = (4/3)(22/7)(42.875) = 179.67 cm³ (exactly 539/3).

### 3.4 Cylinder and cone

| Solid | Volume | Curved area | Total area |
|---|---|---|---|
| Cylinder | πr²h | 2πrh | 2πr(r + h) |
| Cone | (1/3)πr²h | πrl | πr(r + l) |

where slant height l = √(r² + h²). A cone is one-third of the cylinder with the same base and height.

### 3.5 Rectangle

Perimeter 2(l + b); area l × b; diagonal √(l² + b²). A path of width w **around the outside** of an l × b lawn has area (l + 2w)(b + 2w) − lb.

## 4. Must-memorise block

| Shape | Area / surface | Volume |
|---|---|---|
| Sphere | 4πr² | (4/3)πr³ |
| Hemisphere | 3πr² (total), 2πr² (curved) | (2/3)πr³ |
| Cylinder | 2πrh (curved), 2πr(r + h) (total) | πr²h |
| Cone | πrl (curved), πr(r + l) (total) | (1/3)πr²h |
| Cube | 6a² | a³ |
| Cuboid | 2(lb + bh + hl) | lbh |

**Pythagorean triples:** 3-4-5, 5-12-13, 8-15-17, 7-24-25, 20-21-29. Multiples work too.

## 5. Worked examples

**Example 1 — sphere (observed Q08).** 154 cm² → r = 3.5 → volume **179.67 cm³** (539/3). The source said “around 180”.

**Example 2 — cylinder.** Radius 7 cm, height 10 cm. Volume = (22/7) × 49 × 10 = **1540 cm³**. Curved area = 2 × (22/7) × 7 × 10 = **440 cm²**.

**Example 3 — cone.** Radius 3 cm, height 4 cm. Slant height = √(9 + 16) = 5. Curved area = (22/7) × 3 × 5 = 330/7 ≈ **47.14 cm²**. Volume = (1/3)(22/7)(9)(4) = 264/7 ≈ **37.71 cm³**.

**Example 4 — path around a lawn.** Lawn 20 m × 12 m, path 2 m wide outside. Outer rectangle = 24 × 16 = 384; lawn = 240; path = **144 m²**.

**Example 5 — diagonal.** Rectangle 15 m × 8 m. Diagonal = √(225 + 64) = √289 = **17 m**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Forgetting to find r first | The given is an area or a volume | Always solve for r |
| Using the radius as the diameter | Some questions give d | Halve it |
| Cone: using height where slant height belongs | Curved area uses l | Compute l = √(r² + h²) |
| Path inside vs outside | Changes the outer rectangle | Read “inside” or “outside” |
| Using 3.14 with multiples of 7 | Messy | Use 22/7 when r is a multiple of 7 |
| Mixing units | cm and m | Convert before multiplying |

## 7. Practice questions

More questions: [`QB-A11-mensuration.md`](../question-banks/QB-A11-mensuration.md).

**1.** **[Sphere]** The volume of a sphere is 4851 cm³. Find its surface area (π = 22/7).
a) 693
b) 1386
c) 132
d) 346.5

**2.** **[Area from perimeter]** The perimeter of a rectangle is 76 m and its length is 33 m. Find its area (in m²).
a) 1089
b) 361
c) 165
d) 924

**3.** **[Area from perimeter]** The perimeter of a rectangle is 66 m and its length is 21 m. Find its area (in m²).
a) 252
b) 189
c) 441
d) 272

**4.** **[Sphere]** The volume of a sphere is 130977 cm³. Find its surface area (π = 22/7).
a) 396
b) 3118.5
c) 12474
d) 6237

**5.** **[Path around a rectangle]** A rectangular lawn is 26 m by 13 m. A path 1 m wide runs all around it **outside** the lawn. What is the area of the path (in m²)?
a) 156
b) 40
c) 78
d) 82

**6.** **[Cylinder / cone]** Find the volume of a cylinder of radius 3.5 cm and height 15 cm (π = 22/7).
a) 577.5
b) 330
c) 192.5
d) 165

**7.** **[Cylinder / cone]** Find the total surface area of a closed cylinder of radius 3 cm and height 12 cm (π = 22/7).
a) 339.43
b) 226.29
c) 56.57
d) 282.86

**8.** **[Sphere]** The surface area of a sphere is 1386 cm². Find its volume (π = 22/7).
a) 7276.5
b) 9702
c) 3638.25
d) 4851

**9.** **[Path around a rectangle]** A rectangular lawn is 23 m by 8 m. A path 3 m wide runs all around it **outside** the lawn. What is the area of the path (in m²)?
a) 222
b) 102
c) 186
d) 372

**10.** **[Cylinder / cone]** Find the curved surface area of a cylinder of radius 21 cm and height 10 cm (π = 22/7).
a) 13860
b) 4092
c) 1320
d) 660

**11.** **[Area from perimeter]** The perimeter of a rectangle is 72 m and its length is 12 m. Find its area (in m²).
a) 144
b) 288
c) 324
d) 291

**12.** **[Cylinder / cone]** Find the volume of a cone with base radius 21 cm and height 7 cm (π = 22/7).
a) 154
b) 3234
c) 4851
d) 9702

### ANSWER KEY

1. **b** — (4/3)πr³ = 4851 → r³ = 1157.62 → r = 10.5. Surface area = 4πr² = 4(22/7)(10.5)² = **1386 cm²**.
2. **c** — Length + breadth = 76/2 = 38, so breadth = 38 − 33 = 5. Area = 33 × 5 = **165**.
3. **a** — Length + breadth = 66/2 = 33, so breadth = 33 − 21 = 12. Area = 21 × 12 = **252**.
4. **c** — (4/3)πr³ = 130977 → r³ = 31255.88 → r = 31.5. Surface area = 4πr² = 4(22/7)(31.5)² = **12474 cm²**.
5. **d** — Outer rectangle = (26 + 2) × (13 + 2) = 420; minus the lawn 338 = **82**.
6. **a** — πr²h = (22/7) × 3.5² × 15 = **577.5 cm³**.
7. **d** — 2πr(r + h) = 2 × (22/7) × 3 × (3 + 12) = **282.86 cm²**.
8. **d** — 4πr² = 1386 → r² = 110.25 → r = 10.5. Volume = (4/3)πr³ = (4/3)(22/7)(10.5)³ = **4851 cm³**.
9. **a** — Outer rectangle = (23 + 6) × (8 + 6) = 406; minus the lawn 184 = **222**.
10. **c** — 2πrh = 2 × (22/7) × 21 × 10 = **1320 cm²**.
11. **b** — Length + breadth = 72/2 = 36, so breadth = 36 − 12 = 24. Area = 12 × 24 = **288**.
12. **b** — (1/3)πr²h = (1/3)(22/7) × 21² × 7 = **3234 cm³**.

## 8. Resources

- **https://www.indiabix.com/aptitude/volume-and-surface-area/** — solids practice.
- **https://www.geeksforgeeks.org/mensuration-formulas/** — a formula sheet for all standard shapes.

## 9. Self-check

1. Can you write the sphere, cylinder and cone volume formulas from memory?
2. Given a sphere's surface area, can you get r in one line?
3. What is l for a cone with r = 3 and h = 4?
4. Can you compute the area of a path around a lawn in one line?
5. When is π = 22/7 the right choice?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions Q08 in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `A11`). Confidence **Medium**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
