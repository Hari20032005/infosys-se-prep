---
title: OOP in pseudocode: inheritance and overriding
code: P9
section: Pseudocode
weightage_pct: 0.7% of marks
est_questions: 0.25
tier: 4
difficulty: Medium
est_study_hours: 0.6
confidence: Low
last_updated: 2026-09-30
---

# P9 — OOP in pseudocode: inheritance and overriding

## 1. Why this topic matters here

Expect about **0.3 questions and 0.5 marks** on this topic (about 0.7% of the 75 scored marks). It sits in **Pseudocode**: 5 questions, 10 marks, 10 minutes. **Tier 4**, 0.6 hours to reach reliable recall, confidence **Low**.

**No Infosys question on this topic was recovered.** It rests on syllabus lists or first-hand naming only (C1), so its share is an allocation, not an observation.

**Why the tier:** expected marks per study hour, weighted by confidence, is 0.51 against a paper average of 1.84 (`../data/analysis-tables.md` §6). Every section has its own cut-off, so a zero here costs the whole section's chance, not only these marks. There is no calculator. Negative marking: none reported.

## 2. Exactly what gets asked

Tier 4, recognise-only. The 2025 pattern deck lists “inheritance” and “method overriding” among the pseudocode topics (C1), and a 2026 coach's list adds “object-oriented concepts” `[REPORTED]`. No observed item was recovered, so this file is light: how to trace a call through a class hierarchy. You write Java, so the snippets below are plain Java and **every output was produced by running the code**.

| Sub-pattern | How it appears |
|---|---|
| Which version of a method runs | `A a = new B(); a.show();` |
| Constructor order | `new B()` prints the parent's line first |
| `super.method()` calls | Output joins two classes' lines |
| Fields and static methods do **not** dispatch | Reference type decides |
| Overloading is chosen at compile time | `f(5)` versus `f(5.0)` |

## 3. Concept notes

### 3.1 Four rules

1. **Instance methods dispatch on the object's real class** (runtime). `A a = new B(); a.show();` runs B's `show`.
2. **Fields and static methods use the reference type** (compile time). `a.x` is A's `x`; `a.greet()` (static) is A's.
3. **A constructor calls the parent constructor first** (`super(...)`), so parent prints come first.
4. **Overloads are picked by the declared argument types**, not by the object.

### 3.2 A trace template

Write the *declared* type, the *real* type and the method; apply rules 1–4 in order.

## 4. Must-memorise block

| Code | What runs |
|---|---|
| `Parent p = new Child(); p.m()` | Child's `m` (if overridden) |
| `p.field` | Parent's field |
| `Parent.staticM()` or `p.staticM()` | Parent's static method |
| `new Child()` | Parent constructor, then Child constructor |
| `super.m()` inside Child | Parent's `m` |
| `private` method | not overridden |

## 5. Worked examples

All snippets are in the question bank; below is the core trace.

```java
class A { void show() { System.out.print("A"); } }
class B extends A { void show() { super.show(); System.out.print("B"); } }
// A obj = new B(); obj.show();   -> prints AB
```
The real class is B, so B's `show` runs; its first line is `super.show()` (prints A), then it prints B: **AB**.

```java
class A { int x = 10; }
class B extends A { int x = 20; }
// A a = new B(); System.out.println(a.x);   -> 10
```
Fields use the reference type: **10**.

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid it |
|---|---|---|
| Assuming fields are overridden | They are hidden, not overridden | Fields: reference type |
| Forgetting the parent's constructor output | It runs first | Print parent, then child |
| Treating static methods as dynamic | They are bound at compile time | Static: reference type |
| Picking the overload by the object | Chosen by the declared type | Check the argument type |

## 7. Practice questions

More questions: [`QB-P9-oop-in-pseudocode.md`](../question-banks/QB-P9-oop-in-pseudocode.md).

**1.** **[OOP trace]** What is the output?

```java
class A { void show() { System.out.print("A"); } }
class B extends A { void show() { System.out.print("B"); } }

// main:
A obj = new B(); obj.show();
```

a) B
b) AB
c) A
d) BA

**2.** **[OOP trace]** What is the output?

```java
class A { void show() { System.out.print("A"); } }
class B extends A { void show() { super.show(); System.out.print("B"); } }

// main:
A obj = new B(); obj.show();
```

a) A
b) BA
c) AB
d) B

**3.** **[OOP trace]** What is the output?

```java
class A { A() { System.out.print("A"); } }
class B extends A { B() { System.out.print("B"); } }

// main:
new B();
```

a) B
b) AA
c) BA
d) AB

**4.** **[OOP trace]** What is the output?

```java
class A { int x = 10; }
class B extends A { int x = 20; }

// main:
A a = new B(); System.out.print(a.x);
```

a) 10
b) 30
c) 0
d) 20

**5.** **[OOP trace]** What is the output?

```java
class A { int x = 10; }
class B extends A { int x = 20; }

// main:
A a = new B(); System.out.print(((B) a).x);
```

a) 10
b) 20
c) 20 10
d) 30

**6.** **[OOP trace]** What is the output?

```java
class A { static void hi() { System.out.print("A"); } }
class B extends A { static void hi() { System.out.print("B"); } }

// main:
A a = new B(); a.hi();
```

a) AB
b) A
c) B
d) BA

### ANSWER KEY

1. **a** — The real class is B and `show` is an instance method, so B's version runs. (Output: `B`, produced by running the code.)
2. **c** — B's `show` runs; its first statement `super.show()` prints A, then it prints B. (Output: `AB`, produced by running the code.)
3. **d** — A constructor starts by calling the parent constructor, so A prints first. (Output: `AB`, produced by running the code.)
4. **a** — Fields are not overridden: the reference type A decides, so `a.x` is A's 10. (Output: `10`, produced by running the code.)
5. **b** — The cast makes the compiler read B's field: 20. (Output: `20`, produced by running the code.)
6. **b** — Static methods are bound at compile time by the reference type A, so A's `hi` runs. (Output: `A`, produced by running the code.)

## 8. Resources

- **https://docs.oracle.com/javase/tutorial/java/IandI/override.html** — the Java tutorial on overriding and hiding.
- **https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html** — the Java tutorial page on polymorphism and dynamic dispatch.

## 9. Self-check

1. What prints for `A a = new B(); a.show();` when B overrides `show`?
2. Which `x` does `a.x` read if both classes declare it?
3. In which order do constructors print?
4. Is an overload chosen at compile time or runtime?
5. Can a `private` method be overridden?

## 10. Sources

This file was written for this library. **Infosys evidence:** observed questions none in `../data/questions-observed.csv`; section structure and marks in `../research/03-pattern-synthesis.md` §1; weightage, tier and hours in `../data/weightage.json` (code `P9`). Confidence **Low**. Practice questions in §7 and the bank were generated and checked by execution (brute force, simulation or inverse); see `../research/04-qa-report.md`. Nothing here is a published Infosys syllabus.
