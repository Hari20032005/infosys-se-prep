---
title: OOP — The Four Pillars, Overloading vs Overriding
code: IV2
section: Interview
weightage_pct: interview stage
est_questions: 4
tier: 1
difficulty: Medium
est_study_hours: 1.0
confidence: High
last_updated: 2026-09-30
adapted_from: accenture-prep-final/accenture-prep-library/topics/T05-D1-oop-four-pillars.md
---

# IV2 — OOP — The Four Pillars, Overloading vs Overriding

*Adapted from `accenture-prep-final/accenture-prep-library/topics/T05-D1-oop-four-pillars.md`; verified in that library's QA. §1 and §10 are regenerated for Infosys from `data/weightage.json`; §2 gains an Infosys evidence table; §3–§9 are the source text unchanged, so "observed" in the worked examples refers to the source paper.*

## 1. Why this topic matters here

This is interview material, not test material. **4 questions on this theme** were reported across **3 first-hand interview accounts** (B1, B3, B5), so it is **Tier 1** for the interview stage, 1.0 hours to prepare. Interviews are face to face on campus, 15–40 minutes, technical and HR usually in one conversation (`../research/03-pattern-synthesis.md` §6). The questions are at textbook level; the teaching body below is sized to answer them aloud, not to pass a written exam.

## 2. Exactly what gets asked

### What Infosys interviewers asked

| ID | Account | Date | Question |
|---|---|---|---|
| I03 | B1 | 2025-05-12 | Define OOP and explain its four pillars. |
| I04 | B1 | 2025-05-12 | Explain the access specifiers in Java. |
| I12 | B3 | 2025-12-04 | Difference between method overloading and method overriding, with examples. |
| I19 | B5 | 2025-01 | Java or Python, and why? |

> The pattern notes below come from the library this file was adapted from; their frequency remarks describe that source, not Infosys.



1. **Predict the output of a short inheritance snippet.** Confirmed in Java, C++ and Python. Usually 6–12 lines with a constructor chain or an overridden method, and you state what prints.

**1. (a) Two methods in the same class with the same name but different parameter lists**
Overloading within one class is resolved entirely by the compiler, which is static polymorphism.
- (c) Overriding is dispatched at runtime by the JVM — that is dynamic polymorphism.
- (b) Upcasting is a type conversion; on its own it produces no polymorphism — the behaviour comes from the overriding method that gets dispatched.
- (d) Upcasting is the same mechanism as (b); it enables polymorphism but is not a form of polymorphism itself.

---

2. **Overloading versus overriding.** The most examined conceptual distinction — binding time, parameter rules, return-type rules, access-modifier rules.

**2. (d) `final`**
A `final` method cannot be overridden; declaring a same-signature method in a subclass is a compile-time error.
- (a) A subclass may declare a `static` method with the same signature — that is legal *hiding*, not an error.
- (c) An abstract method is designed to be overridden by concrete subclasses — mandatory, not illegal.
- (b) `synchronized` is not inherited as a constraint; a subclass may freely override the method with or without it.

---

3. **Interface behaviour.** Confirmed local items. What an interface can contain, and what `interface B extends A` means.

**3. (c) Encapsulation**
Encapsulation bundles state and behaviour in one unit (the class) and restricts direct access via access modifiers.
- (a) Inheritance is the reuse of a parent's members by a child class — no data binding involved.
- (b) Polymorphism is one interface with many implementations — unrelated to data hiding.
- (d) Abstraction hides *implementation detail* by exposing only essential behaviour; it is achieved with abstract classes and interfaces, not with access modifiers on fields.

---

4. **Constructor order.** Which constructor runs first in an inheritance chain, and why constructors are not inherited.

**4. (a) `Dog Dog`**
Both calls end at `Dog.sound()`: the first via runtime dispatch on the `Dog` object, the second directly on a `Dog` receiver.
- (b) The first call does not use `Animal`'s version just because the reference is typed `Animal`.
- (c) The second call is made on a `Dog` object with a `Dog` reference — `Animal`'s version can never run for it.
- (d) Both classes declare `sound()`, so overriding applies at every call.

---

5. **Pillar identification.** A described design decision maps to encapsulation, abstraction, inheritance or polymorphism.

**5. (d) The compiler selects the overloaded method at compile time based on the static types of the receiver and the arguments.**
Overloads are bound during compilation using the declared types visible at the call site.
- (a) The JVM has no role in overload selection; only overriding uses the runtime class.
- (b) Return type is not part of the signature for overload resolution — two methods differing only in return type is a compile error.
- (c) There is no "first declared wins" rule; an ambiguous call where neither method is more specific is a compile-time error.

---

6. **Abstract class versus interface.** When to use which.

## 3. Concept notes

### 3.1 Class vs object

A **class** is a blueprint: it declares fields (state) and methods (behaviour) but holds no data itself. An **object** is a runtime instance of a class, allocated on the heap by `new`, with its own copy of instance fields.

*Analogy:* a class is the architectural blueprint of a house; an object is an actual house built from it. The blueprint is not a house, and two houses built from the same blueprint are separate entities with separate addresses.

| | Class | Object |
|---|---|---|
| Nature | Template / type definition | Instance of that type |
| Created by | `class` keyword, at compile time | `new`, at runtime |
| Memory | Loaded once per JVM (method area) | Heap; one block per object |
| Holds | Declarations, no values | Actual field values |
| Count | One definition | Many instances |

```java
class Dog {
    String name;                                  // instance field; one per object
    void bark() { System.out.println(name + " says woof"); }
}

Dog d1 = new Dog();   // object 1
Dog d2 = new Dog();   // object 2 — separate 'name'
d1.name = "Rex";
d1.bark();            // Rex says woof
```

---

### 3.2 The four pillars

| Pillar | One-line definition | Why it exists |
|---|---|---|
| Encapsulation | Bundling data and the methods that operate on it, and restricting direct access to the data | Prevents invalid state; lets you change internals without breaking callers |
| Abstraction | Exposing *what* an operation does while hiding *how* it does it | Reduces complexity; decouples caller from implementation |
| Inheritance | A class acquires the fields and methods of another class (`extends`) | Code reuse and IS-A polymorphism |
| Polymorphism | The same call produces different behaviour depending on the actual object type | One interface, many implementations; extensibility |

#### Encapsulation

Implemented with `private` fields + public getters/setters. **Encapsulation** = bundling; **data hiding** = the access restriction that enforces it. Encapsulation is the broader concept.

```java
class Account {
    private double balance;                       // hidden

    public double getBalance() { return balance; }

    public void deposit(double amt) {
        if (amt > 0) balance += amt;              // validation on write
    }
}
// new Account().balance = -500;  // compile error — field not visible
```

#### Abstraction

Hides implementation behind a contract. Two tools: **abstract class** and **interface**.

```java
abstract class Shape {
    abstract double area();                       // WHAT — no body
    void describe() { System.out.println("Area = " + area()); }  // shared code
}
class Circle extends Shape {
    private final double r;
    Circle(double r) { this.r = r; }
    double area() { return Math.PI * r * r; }     // HOW — supplied here
}
interface Vehicle { void start(); }               // pure contract
```

#### Inheritance (`extends`, IS-A)

`Dog extends Animal` means a `Dog` **IS-A** `Animal`. The subclass gets all non-private members of the superclass.

| Type | Structure | Java support |
|---|---|---|
| Single | A → B | Yes |
| Multilevel | A → B → C | Yes |
| Hierarchical | A → B, A → C | Yes |
| Multiple | B → A, C → A | **Classes: no.** Interfaces: yes (`implements A, B`) |
| Hybrid | Combination of the above | Yes via interfaces; not via classes |

```java
class Animal { void eat() { System.out.println("eating"); } }
class Dog extends Animal { void bark() { System.out.println("barking"); } }
new Dog().eat();     // inherited
```

**Why Java forbids multiple inheritance of classes — the diamond problem.** If `B extends A` and `C extends A`, and `D extends B, C`, and `A` defines `void m()`, then `D` inherits two copies of `m()` and two copies of A's fields. The compiler cannot decide which to use and the object layout is ambiguous.

**How interfaces work around it.** A class may `implement` any number of interfaces because interfaces carry no instance state and (pre-Java 8) no implementation — there is nothing to duplicate. Since Java 8, `default` methods reintroduce the risk; Java resolves it deterministically:

1. A superclass method wins over any interface default method.
2. Otherwise the **most specific** interface wins (if `B extends A`, `B`'s default beats `A`'s).
3. If two unrelated interfaces conflict, the class **must** override the method (or call `InterfaceName.super.m()`).

#### Polymorphism

| | Compile-time (static) | Runtime (dynamic) |
|---|---|---|
| Also called | Overloading, static binding, early binding | Overriding, dynamic method dispatch, late binding |
| Decided by | Compiler, from the reference type and argument types | JVM, from the actual object type |
| Requires inheritance | No | Yes |

```java
// Compile-time: compiler picks from the argument list
void print(int x)    { }
void print(String s) { }
print(5);                       // print(int) chosen at compile time

// Runtime: JVM picks from the actual object
class Animal { void sound() { System.out.println("some sound"); } }
class Dog extends Animal { @Override void sound() { System.out.println("woof"); } }

Animal a = new Dog();           // upcast — reference type Animal, object type Dog
a.sound();                      // prints "woof": decided at runtime
```

---

### 3.3 Overloading vs overriding — the most examined distinction

| Aspect | Overloading | Overriding |
|---|---|---|
| Binding time | Compile time (static) | Runtime (dynamic dispatch) |
| Where | Same class, or subclass | Subclass only |
| Inheritance required | No | **Yes** |
| Parameters | **Must differ** (count, type, or order) | **Must be identical** |
| Method name | Same | Same |
| Return type | May differ freely; return type alone is **not** enough to overload | Must be same or a **covariant** subtype |
| Access modifier | Any, no rule | **Cannot be more restrictive**; may be wider |
| `static` methods | Can be overloaded | **Cannot** be overridden — the subclass method *hides* it |
| `final` methods | Can be overloaded | **Cannot** be overridden |
| `private` methods | Can be overloaded | **Cannot** be overridden — the subclass method is a new, unrelated method |
| Checked exceptions | No restriction | May throw fewer or narrower; may **not** throw broader |
| Constructors | Can be overloaded | Constructors are **not inherited**, so never overridden |
| Annotation | none | `@Override` |

```java
// OVERLOADING — same name, different parameter lists, same class
class Calc {
    int add(int a, int b)         { return a + b; }
    double add(double a, double b){ return a + b; }   // different types
    int add(int a, int b, int c)  { return a + b + c; } // different count
}

// OVERRIDING — same signature, subclass replaces superclass behaviour
class Animal {
    void sound() { System.out.println("some sound"); }
}
class Dog extends Animal {
    @Override
    void sound() { System.out.println("woof"); }      // same signature
}

// WRONG: not an overload — return type alone cannot distinguish
// int  foo(int x) { ... }
// long foo(int x) { ... }     // compile error: duplicate method
```

---

### 3.4 Constructors

A constructor has the class name, no return type, and runs once per `new`. It is **not a member** of the class, therefore **not inherited**. A subclass cannot be constructed without invoking a superclass constructor.

| Type | Definition | Notes |
|---|---|---|
| Default | No-arg constructor supplied by the compiler | Provided **only if you declare no constructor at all**. Declaring any constructor removes it. |
| Parameterised | Takes arguments to initialise fields | Once declared, the compiler's default no-arg version is gone |
| Copy | Takes an object of the same class and copies its fields | **Java does not provide one**; you must write it manually |

```java
class Point {
    int x, y;
    Point()              { this(0, 0); }        // default, chained to parameterised
    Point(int x, int y)  { this.x = x; this.y = y; }   // parameterised
    Point(Point p)       { this(p.x, p.y); }    // copy — user-written
}
```

**Chaining.**

- `this(...)` calls another constructor **of the same class**; `super(...)` calls a constructor **of the direct superclass**.
- Both must be the **first statement** in a constructor body — at most one per constructor.
- If you write neither, the compiler inserts `super()` (the no-arg superclass constructor). If the superclass has no no-arg constructor and you did not call `super(...)` explicitly, it is a **compile error**.

```java
class A {
    A()      { this(10); System.out.println("A()"); }
    A(int x) { System.out.println("A(int) " + x); }
}
class B extends A {
    B()      { super(5); System.out.println("B()"); }
}
new B();   // output: A(int) 5 / A() / B()
```

**Order of execution for `new Child()` where `Child extends Parent`:**

1. Load `Parent`, run its **static** initialisers (once per JVM).
2. Load `Child`, run its static initialisers (once per JVM).
3. Allocate the object; all fields zeroed/defaulted.
4. Run `Parent`'s instance initialisers and instance field initialisers, then **`Parent`'s constructor body**.
5. Run `Child`'s instance initialisers and instance field initialisers, then **`Child`'s constructor body**.

Rule to memorise: **statics top-down (once), then construction superclass → subclass.**

---

### 3.5 Abstract class vs interface

| | Abstract class | Interface |
|---|---|---|
| Keyword | `abstract class` | `interface` |
| Instantiable | No | No |
| Inheritance syntax | `extends` (exactly one) | `implements` (many), `extends` (many interfaces) |
| Constructors | Yes | No |
| Instance fields | Yes | No — fields are implicitly `public static final` (constants) |
| Methods | abstract or concrete | Pre-8: implicitly `public abstract`. Java 8: `default` and `static` methods with bodies. Java 9: `private` methods. |
| Access modifiers on members | Any | Members are implicitly `public` (pre-9); `private` allowed for Java 9+ helper methods |
| `final` / `static` methods | Allowed | `static` allowed (Java 8+); `final` not permitted |
| When to use | Related classes sharing state and code | Unrelated classes sharing a capability/contract |

**Java 8 change:** interfaces gained `default` methods (with a body, inheritable and overridable) and `static` methods (called on the interface, not inherited). This lets you add methods to an interface without breaking existing implementers. `default` methods bring back diamond conflicts, resolved by: class beats interface → most specific interface wins → otherwise override.

---

### 3.6 static vs instance members

| | `static` member | Instance member |
|---|---|---|
| Belongs to | The class | Each object |
| Memory | One copy, at class load | One copy per object |
| Access | `ClassName.member` | `reference.member` |
| Can access instance members | **No** (no `this`) | Yes |
| `this` / `super` usable | No | Yes |
| Can be overridden | No — hidden (static methods) | Yes |
| Inside `main` | Directly callable | Requires an object |

---

### 3.7 Keyword quick reference

| Keyword | Applies to | Effect |
|---|---|---|
| `static` | field, method, block, nested class | Belongs to the class, not an instance; loaded once |
| `final` | variable | Value assigned once, cannot be reassigned |
| `final` | method | Cannot be overridden |
| `final` | class | Cannot be extended (e.g. `String`, `Integer`) |
| `this` | inside instance context | Reference to the current object; `this(...)` chains constructors in the same class |
| `super` | inside instance context | Reference to the superclass part; `super(...)` calls a superclass constructor; `super.m()` calls an overridden superclass method |

`final` on a reference variable freezes the reference, **not** the object's contents — a `final List` can still have elements added.

---

### 3.8 Access modifiers

| Modifier | Same class | Same package | Subclass in another package | Anywhere (world) |
|---|---|---|---|---|
| `private` | Yes | No | No | No |
| *(default / package-private — no keyword)* | Yes | Yes | No | No |
| `protected` | Yes | Yes | Yes | No |
| `public` | Yes | Yes | Yes | Yes |

Note: `protected` also grants package access, so it is *wider* than default, not orthogonal to it. A `protected` member inherited into another package is accessible through a reference of the subclass type only.

---

### 3.9 Method hiding vs overriding (static methods)

| | Overriding | Hiding |
|---|---|---|
| Applies to | Instance methods | `static` methods |
| Binding | Runtime, based on the object type | Compile time, based on the reference type |
| Polymorphic | Yes | **No** |
| Access rule | Cannot reduce visibility | Cannot reduce visibility |
| Annotation | `@Override` | None (use of `@Override` on a static method is a compile error) |

```java
class A { static void m() { System.out.println("A"); } }
class B extends A { static void m() { System.out.println("B"); } }

A ref = new B();
ref.m();          // prints "A" — decided by the REFERENCE type, not the object
((B) ref).m();    // prints "B"
```

`A ref = new B(); ref.m();` printing `"A"` is the single most reliable test of whether you understand static binding.

---

### 3.10 Association, aggregation, composition

| Relationship | Strength | UML | Lifecycle | Example |
|---|---|---|---|---|
| Association | "uses-a" | plain line | Independent | `Teacher` ↔ `Student` |
| Aggregation | "has-a" (weak) | hollow diamond | Part outlives the whole | `Department` has `Professor`s |
| Composition | "has-a" (strong) | filled diamond | Part dies with the whole | `House` has `Room`s |

```java
class Department { List<Professor> staff; }   // aggregation: professors exist independently
class House      { private final List<Room> rooms = new ArrayList<>(); } // composition: rooms owned
```

Composition is the stronger form of encapsulation: the part is not shared and not exposed.

---

### 3.11 SOLID principles

| Letter | Principle | One line |
|---|---|---|
| S | Single Responsibility | A class should have one reason to change. |
| O | Open/Closed | Open for extension, closed for modification. |
| L | Liskov Substitution | A subtype must be usable anywhere its supertype is expected. |
| I | Interface Segregation | Prefer many small client-specific interfaces over one general interface. |
| D | Dependency Inversion | Depend on abstractions, not on concrete classes. |

---

## 4. Must-memorise block

**Four pillars (one line each)**

| Pillar | Recall line |
|---|---|
| Encapsulation | `private` fields + public getters/setters — bundle data with its methods and hide it |
| Abstraction | Show *what*, hide *how* — via abstract class or interface |
| Inheritance | `extends` — subclass IS-A superclass, reuses its members |
| Polymorphism | One call, many forms — overloading (compile time) and overriding (runtime) |

**Overloading vs overriding — compressed**

| | Overloading | Overriding |
|---|---|---|
| Binding | Compile time | Runtime |
| Parameters | Must differ | Must be identical |
| Return type | Free | Same or covariant |
| Access | Any | Cannot narrow |
| Inheritance | Not required | **Required** |
| `static` / `final` / `private` | Allowed | None can be overridden (static → hidden) |
| Exceptions | Free | Only narrower/none |

**Access-modifier matrix**

| | Class | Package | Subclass (other pkg) | World |
|---|---|---|---|---|
| `private` | ✔ | ✘ | ✘ | ✘ |
| default | ✔ | ✔ | ✘ | ✘ |
| `protected` | ✔ | ✔ | ✔ | ✘ |
| `public` | ✔ | ✔ | ✔ | ✔ |

Widening order: `private` < default < `protected` < `public`.

**Abstract class vs interface — compressed**

| | Abstract class | Interface |
|---|---|---|
| Extend / implement | one | many |
| Constructor | Yes | No |
| Instance fields | Yes | No (only `public static final`) |
| Concrete methods | Yes | `default` + `static` since Java 8; `private` since Java 9 |
| Use for | related classes with shared state | capability contract across unrelated classes |

**Constructor rules**

1. Name = class name, no return type; runs on every `new`.
2. Default no-arg constructor exists **only if no constructor is declared**.
3. Java gives **no copy constructor** — write it yourself.
4. Constructors are **not inherited** — never overridden, but can be overloaded.
5. `this(...)` / `super(...)` must be the **first statement**; at most one per constructor.
6. No explicit call → compiler inserts `super()`. Missing no-arg superclass constructor = compile error.

**6. (b) `Puppy+Dog`**
`super()` inside `Puppy.speak()` resolves to the next class in the MRO, which is `Dog`, and `Dog.speak()` returns `"Dog"` without calling further up.
- (a) `super()` inside `Puppy` does not jump all the way to `Animal`; it goes one step along the MRO.
- (c) The result is the concatenation `"Puppy+" + "Dog"`, not the bare return value of `Dog.speak()`.
- (d) `super()` never re-invokes the same class's method; it moves past `Puppy` in the MRO.

---

7. Execution order: superclass statics → subclass statics → superclass instance init + constructor → subclass instance init + constructor.

**7. (b) A class implementing `B` must provide implementations for the abstract methods of both `A` and `B`.**
`B` inherits all of `A`'s abstract methods, so its implementers inherit the whole obligation.
- (a) Redeclaring inherited abstract methods in a sub-interface is optional redundancy, not a requirement.
- (c) An interface may extend several interfaces, e.g. `interface B extends A, C` — that is legal.
- (d) `B` inherits `A`'s abstract methods, so an implementer of `B` must implement them too.

---

8. `static` methods: reference type decides. Instance methods: object type decides.

**Inheritance types:** single, multilevel, hierarchical, multiple, hybrid.
**Java classes:** single inheritance only. **Interfaces:** multiple inheritance allowed.
**Diamond problem:** two paths to the same superclass member → ambiguity → Java forbids it for classes.
**Diamond fix for `default` methods:** class wins → most specific interface wins → else override.

## 5. Worked examples

### Example 1 — Runtime polymorphism with an Animal/Dog setup

```java
class Animal {
    void sound() { System.out.println("Animal"); }
}
class Dog extends Animal {
    void sound() { super.sound(); System.out.println("Dog"); }
}
public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.sound();
    }
}
```
**Reasoning**
1. `new Dog()` builds a `Dog` object. Variable `a` has **static type** `Animal`, **dynamic type** `Dog`.
2. Compile-time check: does `Animal` declare `sound()`? Yes → the call is legal, so this compiles.
3. Runtime dispatch: the JVM looks at the object's *actual* class (`Dog`), not the reference type, and runs `Dog.sound()`.
4. `Dog.sound()` first calls `super.sound()` → prints `Animal`, then prints `Dog`.

Trace: `a.sound()` → `Dog.sound()` → `Animal.sound()` then `println("Dog")`.

Output:
```
Animal
Dog
```

**Final answer: `Animal` on line 1, `Dog` on line 2 — dynamic method dispatch selects `Dog.sound()`, and `super.sound()` explicitly runs the parent version.**

---

### Example 2 — Overload resolution at compile time

```java
class Calc {
    void add(int a, int b)    { System.out.println("int"); }
    void add(double a, double b) { System.out.println("double"); }
}
public class Main {
    public static void main(String[] args) {
        Calc c = new Calc();
        c.add(5, 10);
        c.add(5.0, 10.0);
        c.add(5, 10.5);
    }
}
```
**Reasoning**
Java resolves overloads in phases. Phase 1 (strict invocation) allows primitive widening but no boxing or varargs.

| Call | `add(int,int)` applicable? | `add(double,double)` applicable? | Chosen |
|---|---|---|---|
| `add(5, 10)` | Yes (identity) | Yes (widening 5→5.0, 10→10.0) | `add(int,int)` — more specific |
| `add(5.0, 10.0)` | No (double cannot narrow to int) | Yes (identity) | `add(double,double)` |
| `add(5, 10.5)` | No (10.5 cannot narrow to int) | Yes (5→5.0 widening) | `add(double,double)` |

For `add(5, 10)` both are applicable, so the compiler picks the **most specific**: `int` converts to `double` by widening, but `double` cannot convert to `int`, so `add(int,int)` is more specific.

Output:
```
int
double
double
```

**Final answer: `int`, `double`, `double` — all three decisions are made by the compiler, not the JVM.**

---

### Example 3 — Python inheritance chain with `super()`

```python
class Animal:
    def speak(self):
        return "Animal"
class Dog(Animal):
    def speak(self):
        return "Dog"
class Puppy(Dog):
    def speak(self):
        return "Puppy+" + super().speak()
print(Puppy().speak())
```
**Reasoning**
1. `Puppy` inherits from `Dog`, which inherits from `Animal`. The MRO of `Puppy` is `Puppy → Dog → Animal → object`.
2. `Puppy().speak()` runs `Puppy.speak()`.
3. `super()` inside a method means "the next class after the current one in the instance's MRO". Inside `Puppy`, that is `Dog`.
4. `super().speak()` → `Dog.speak()` → returns `"Dog"` (it does **not** continue up to `Animal`, because `Dog.speak()` does not itself call `super()`).
5. String concatenation: `"Puppy+" + "Dog"` = `"Puppy+Dog"`.

**Final answer: `Puppy+Dog`.**

---

### Example 4 — Overload and override in the same hierarchy

```java
class Animal {
    public String eat() { return "Animal eats"; }
}
class Dog extends Animal {
    public String eat()              { return "Dog eats"; }
    public String eat(String food)   { return "Dog eats " + food; }
}
public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        Dog d = new Dog();
        System.out.println(a.eat());
        System.out.println(d.eat("bone"));
    }
}
```
**Reasoning**
1. `Dog.eat()` has the same signature as `Animal.eat()` → **overriding** → runtime dispatch.
2. `Dog.eat(String)` adds a parameter → **overloading**, and it exists only in `Dog`.
3. `a.eat()` — `Animal` declares a no-arg `eat()`, so it compiles; at runtime the object is a `Dog`, so `Dog.eat()` runs.
4. `d.eat("bone")` — receiver static type is `Dog`, which declares `eat(String)`; binds at compile time to that method.

Output:
```
Dog eats
Dog eats bone
```

Note the trap: `a.eat("bone")` would be a **compile-time error**, because `Animal` has no `eat(String)` — the reference type decides which overloads are visible.

**Final answer: `Dog eats` then `Dog eats bone`.**

---

### Example 5 — Python has no overloading

```python
class Report:
    def show(self):
        return "no-arg"
    def show(self, fmt):
        return "formatted:" + fmt

r = Report()
print(r.show("pdf"))
```
**Reasoning**
1. A Python class body is executed top to bottom, and each `def` binds a name in the class namespace.
2. The second `def show` **rebinds** the name `show`. The first definition is discarded — the class dict holds exactly one `show`, taking two parameters (`self`, `fmt`).
3. `r.show("pdf")` binds `self = r`, `fmt = "pdf"` → returns `"formatted:pdf"`.
4. `r.show()` would raise `TypeError: show() missing 1 required positional argument: 'fmt'` — there is no zero-argument version left to call.

**Final answer: `formatted:pdf` — the second definition replaced the first; Python never overloads by arity.**

---

## 6. Traps and gotchas

| Trap | Why it catches people | How to avoid |
|---|---|---|
| Calling overloading "runtime polymorphism" | Both are called "polymorphism", so the labels get swapped | Memorise the one-line mapping: **overloading = compile-time / static binding**; **overriding = runtime / dynamic binding** |
| Believing the object's runtime type picks the overload | Unconsciously reusing the "actual object wins" rule from overriding | For overloads, read only two things: the **static type of the receiver** and the **static types of the arguments**. The `new` keyword on the right is irrelevant |
| Expecting `static` methods to behave polymorphically | `Animal a = new Dog(); a.staticMethod();` reads like the overriding pattern | Static methods are **hidden**, not overridden. The call is bound at compile time by the reference type, so `Animal`'s version runs |
| Trying to override a `private` or `final` method | `private` looks inherited because the code is in the same file package | `final` + override = **compile error**. `private` methods are not visible to subclasses, so a same-named method there is a brand-new method, and the `@Override` annotation will fail |
| Making the overriding method less accessible (`public` → `protected`) | Visibility feels like a free choice | An override may only **widen or keep** access. Narrowing is a compile error. Overloading has no such rule |
| Adding a broader checked exception in an override | The signature "looks" compatible | An override may throw the **same or narrower** checked exceptions, or none. Adding `throws IOException` to a method that previously threw nothing fails to compile. Unchecked exceptions (`RuntimeException`) are unrestricted |
| Writing two same-named methods in one Python class expecting overloading | Every other OOP language allows it, and there is no error message at definition time | Python keeps only the **last** definition. Simulate overloading with default arguments, `*args`, or `functools.singledispatch` |
| Assuming fields/attributes are polymorphic like methods | Methods dispatch on the object, so people expect fields to as well | Fields are resolved by the **static type of the reference** and are *hidden*, not overridden. Only method calls participate in dynamic dispatch |

---

## 7. Practice questions

1. **[Easy]** *(D1 — polymorphism types)* Which of the following is an example of compile-time (static) polymorphism in Java?
(a) Two methods in the same class with the same name but different parameter lists
(b) Assigning a subclass object to a superclass reference variable
(c) A subclass overriding a superclass method
(d) Upcasting a `Dog` object to an `Animal` reference

2. **[Easy]** *(D1 — overriding rules)* In Java, which modifier on a superclass method makes it a compile-time error for a subclass to declare a method with the same signature?
(a) `static`
(b) `synchronized`
(c) `abstract`
(d) `final`

3. **[Easy]** *(D1 — the four pillars)* Which OOP pillar is defined as "binding data and the methods that operate on that data into a single unit while restricting direct access to the data"?
(a) Inheritance
(b) Polymorphism
(c) Encapsulation
(d) Abstraction

4. **[Medium]** *(D1 — Java output)* What is the output?
```java
class Animal { void sound() { System.out.print("Animal "); } }
class Dog extends Animal { void sound() { System.out.print("Dog "); } }
public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.sound();
        Dog d = new Dog();
        d.sound();
    }
}
```
(a) `Dog Dog`
(b) `Animal Dog`
(c) `Dog Animal`
(d) `Animal Animal`

5. **[Medium]** *(D1 — overloading resolution)* Which statement about Java method-overload resolution is correct?
(a) The JVM selects the overloaded method at runtime based on the actual object type.
(b) Overload resolution considers only the return type of the methods.
(c) If two overloads are equally applicable and neither is more specific, the compiler picks whichever was declared first.
(d) The compiler selects the overloaded method at compile time based on the static types of the receiver and the arguments.

6. **[Medium]** *(D1 — Python output)* What is the output?
```python
class Animal:
    def speak(self):
        return "Animal"
class Dog(Animal):
    def speak(self):
        return "Dog"
class Puppy(Dog):
    def speak(self):
        return "Puppy+" + super().speak()
print(Puppy().speak())
```
(a) `Puppy+Animal`
(b) `Puppy+Dog`
(c) `Dog`
(d) `Puppy+Puppy`

7. **[Medium]** *(D1 — interfaces)* In Java, given `interface B extends A`, which statement is true?
(a) `B` must redeclare every method of `A` before it compiles.
(b) A class implementing `B` must provide implementations for the abstract methods of both `A` and `B`.
(c) `B` may extend at most one interface.
(d) A class implementing `B` is not required to implement `A`'s methods.

8. **[Medium]** *(D1 — Python output)* What is the output?
```python
class Base:
    def greet(self):
        return "Hello from " + self.name()
    def name(self):
        return "Base"
class Derived(Base):
    def name(self):
        return "Derived"
print(Derived().greet())
```
(a) `Hello from Base`
(b) `TypeError`
(c) `Derived`
(d) `Hello from Derived`

**8. (d) `Hello from Derived`**
`self.name()` inside `Base.greet` is a method call on the instance, so it dispatches dynamically to `Derived.name()`.
- (a) Only the *definition* of `greet` lives in `Base`; the call it makes is resolved on the actual instance type.
- (c) The printed value is the full return of `greet()`, which prefixes `"Hello from "`.
- (b) No error occurs — `self.name()` is a legitimate instance-method call that resolves to `Derived.name`.

---

9. **[Medium]** *(D1 — overriding signatures)* Which pair of methods is a valid **override** in Java?
(a) `Animal: public void eat()` / `Dog: public void eat()`
(b) `Animal: public void eat()` / `Dog: public int eat()`
(c) `Animal: public void eat()` / `Dog: public void eat(int n)`
(d) `Animal: public void eat()` / `Dog: private void eat()`

**9. (a) `Animal: public void eat()` / `Dog: public void eat()`**
Identical signatures and identical access — a textbook override.
- (c) Adding an `int` parameter changes the signature, so this is overloading, not overriding.
- (b) `void` and `int` are unrelated return types; Java only permits *covariant* (subtype) return narrowing, so this is a compile error.
- (d) Reducing visibility from `public` to `private` is a compile error — an override may not narrow access.

---

10. **[Medium]** *(D1 — static binding)* What is the output?
```java
class Animal { static void who() { System.out.print("Animal "); } }
class Dog extends Animal { static void who() { System.out.print("Dog "); } }
public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.who();
    }
}
```
(a) Compilation error
(b) `Animal`
(c) `Animal Dog`
(d) `Dog`

**10. (b) `Animal`**
Static methods are hidden, not overridden, and the call is bound at compile time by the reference type, which is `Animal`.
- (d) This assumes static methods participate in dynamic dispatch, which they do not.
- (c) Only one method executes; the `Dog` version is never reached through an `Animal` reference.
- (a) Calling a static method through an instance reference is legal in Java (it is discouraged style), so this compiles.

---

11. **[Medium]** *(D1 — interface polymorphism)* What is the output?
```java
interface Shape { double area(); }
class Square implements Shape {
    double side = 4;
    public double area() { return side * side; }
}
public class Main {
    public static void main(String[] args) {
        Shape s = new Square();
        System.out.println(s.area());
    }
}
```
(a) Compilation error: `area()` is not public in `Square`
(b) `0.0`
(c) `16.0`
(d) Compilation error: `side` cannot be accessed through a `Shape` reference

**11. (c) `16.0`**
`Square` implements `Shape.area()` and the field `side` is initialized to `4`, so `4 * 4` returns `16.0`, printed with its decimal point.
- (b) `side` is explicitly initialized to `4` in its declaration, so `area()` cannot return `0.0`.
- (a) `Square.area()` is declared `public`, which satisfies the interface requirement — no error.
- (d) `main` never touches `side`; it calls `area()` through the interface, which is legal.

---

12. **[Hard]** *(D1 — ambiguous overload)* What happens when this program is compiled?
```java
class Calc {
    void add(int a, double b)    { System.out.print("id "); }
    void add(double a, int b)    { System.out.print("di "); }
}
public class Main {
    public static void main(String[] args) {
        Calc c = new Calc();
        c.add(5, 10);
    }
}
```
(a) Prints `id`
(b) Prints `id di`
(c) Compilation error: the reference to `add` is ambiguous
(d) Prints `di`

**12. (c) Compilation error: the reference to `add` is ambiguous**
Both overloads are applicable by primitive widening for `add(5, 10)`, and neither is more specific than the other, so the compiler reports an ambiguity.
- (a) Choosing `add(int, double)` would require it to be more specific, but `double` cannot convert to `int`, so it is not.
- (d) Choosing `add(double, int)` fails for the same reason, symmetrically.
- (b) The program never compiles, so no output is produced at all.

---

13. **[Hard]** *(D1 — Python MRO)* What is the output?
```python
class A:
    def f(self): return "A"
class B(A):
    def f(self): return "B" + super().f()
class C(A):
    def f(self): return "C" + super().f()
class D(B, C):
    pass
print(D().f())
```
(a) `BA`
(b) `BCA`
(c) `BAC`
(d) `CBA`

**13. (b) `BCA`**
The MRO of `D` is `D → B → C → A → object`; `B.f` runs, its `super()` moves to `C`, whose `super()` moves to `A`, giving `"C"+"A"` then `"B"+"CA"` = `"BCA"`.
- (c) `BAC` would mean `B`'s `super()` jumped straight to `A`, skipping `C` in the MRO.
- (a) `BA` omits `C`'s contribution entirely, which is impossible since `C` lies between `B` and `A` in the MRO.
- (d) `CBA` reverses the chain; `super()` always moves forward along the MRO, never backward.

---

14. **[Hard]** *(D1 — override legality)* Which of the following is **NOT** a valid override in Java?
(a) `Animal: public void eat()` overridden by `Dog: public void eat() throws IOException`
(b) `Animal: public void eat() throws IOException` overridden by `Dog: public void eat() throws FileNotFoundException`
(c) `Animal: public void eat()` overridden by `Dog: public void eat()`
(d) `Animal: protected Number get()` overridden by `Dog: public Integer get()`

---

**14. (a) `Animal: public void eat()` overridden by `Dog: public void eat() throws IOException`**
An overriding method may not introduce a *broader* checked exception than the overridden method declares — here the parent declares none, so any checked exception is illegal.
- (d) This is legal: `Integer` is a covariant (narrower) return type for `Number`, and `protected` → `public` widens access.
- (b) This is legal: `FileNotFoundException` is a subclass of `IOException`, so the override throws a narrower checked exception.
- (c) Identical signature and identical `public` access is the standard, valid override.

---
## 8. Resources

| Resource | Type | Link | Free/Paid | Time | Why this one |
|---|---|---|---|---|---|
| GfG — OOP concepts in Java | Article | https://www.geeksforgeeks.org/java/object-oriented-programming-oops-concept-in-java/ | Free | 35 min | The four pillars with runnable examples in the exam's language |
| IndiaBix — Computer science Q&A | Practice set | https://www.indiabix.com/computer-science/questions-and-answers/ | Free | 30 min | MCQ volume on OOP concepts |
| PrepInsta — Accenture technical assessment | Practice set | https://prepinsta.com/accenture/technical-assessment/ | Free | 25 min | Lists OOPS explicitly; company-specific phrasing |
| `question-banks/QB-T05-D1-oop-four-pillars.md` | Question bank | (this library) | Free | 40 min | 35 original questions, half of them output prediction |

*All external links verified resolving 2026-09-16.*

## 9. Self-check

- [ ] I can define all four pillars and give a one-line code example of each
- [ ] **I can fill in the overloading-versus-overriding comparison table from memory**
- [ ] I can state the access-modifier rule when overriding a method
- [ ] I can explain why `static`, `final` and `private` methods cannot be overridden
- [ ] I can trace the constructor execution order in a three-level inheritance chain
- [ ] I can explain why Java forbids multiple inheritance of classes and how interfaces work around it
- [ ] I can state four differences between an abstract class and an interface
- [ ] I can predict the output of a short inheritance snippet in Java or Python
- [ ] I can distinguish association, aggregation and composition
- [ ] I scored 11/14 or better on the practice questions

## 10. Sources

**Teaching content (§3–§9)** is adapted from `accenture-prep-final/accenture-prep-library/topics/T05-D1-oop-four-pillars.md`, verified in that library's QA. **Infosys evidence:** first-hand interview accounts in `../data/reviews-online.csv` and `../data/questions-observed.csv` (rows `I01`–`I25`); interview format in `../research/03-pattern-synthesis.md` §6.
