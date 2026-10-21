# QB-IV2 — OOP — The Four Pillars, Overloading vs Overriding

**Interview** · **Tier 1** · 54 questions

Topic file: [`IV2-oop-four-pillars.md`](/Users/hariharansundaramoorthy/Documents/my projects/infosys/infosys-prep-library/interview/IV2-oop-four-pillars.md)

*Adapted from `accenture-prep-final/accenture-prep-library/question-banks/QB-T05-D1-oop-four-pillars.md`; verified in that library's QA. Questions and answer key are unchanged.*

**How to use this bank.** Attempt every question before opening the key, at the real pace for this section (120 seconds a question). Answer letters are balanced across a–d.

---

**1.** **[Easy]** *(D1 — runtime polymorphism)*

What is the output of the following Java program?

```java
class Animal { void sound() { System.out.print("generic "); } }
class Dog extends Animal { void sound() { System.out.print("bark "); } }

public class Main {
    public static void main(String[] args) {
        Animal x = new Dog();
        x.sound();
        Animal y = new Animal();
        y.sound();
    }
}
```

(a) bark generic
(b) generic bark
(c) bark bark
(d) generic generic

**1. (a) bark generic**
`x` is declared `Animal` but refers to a `Dog`, so the overridden `Dog.sound()` runs; `y` refers to a plain `Animal`, so its own version runs.
- (d) Assumes the declared (reference) type decides which override runs — that is field/static behaviour, not instance method dispatch.
- (b) Swaps the two calls; the first object is a `Dog`, not an `Animal`.
- (c) Assumes both variables share the same dynamic type; `y` was created with `new Animal()`.

| Statement | Reference type | Object type | Method executed |
|---|---|---|---|
| `x.sound()` | Animal | Dog | `Dog.sound()` → "bark " |
| `y.sound()` | Animal | Animal | `Animal.sound()` → "generic " |

---

**2.** **[Easy]** *(D1 — overloading vs overriding)*

Which statement correctly distinguishes overloading from overriding?

(a) Overloading requires an inheritance relationship; overriding does not.
(b) Overloading is resolved at runtime; overriding is resolved at compile time.
(c) Overloading uses the same method name with different parameter lists in the same class or class hierarchy; overriding redefines an inherited method with the same signature.
(d) Overloading can differ from the original method only in return type.

**2. (c) Overloading uses the same method name with different parameter lists in the same class or class hierarchy; overriding redefines an inherited method with the same signature.**
Overloading is compile-time (static) polymorphism keyed on the parameter list; overriding is runtime (dynamic) polymorphism requiring the same signature in a subtype.
- (b) Reverses the binding times: overloading is resolved at compile time, overriding at runtime.
- (a) Reverses the requirement: overriding needs inheritance, overloading does not.
- (d) A return type alone cannot distinguish overloads; Java rejects two methods differing only in return type.

---

**3.** **[Easy]** *(D1 — encapsulation)*

A class declares all its fields `private` and exposes only public methods that read or modify them with validation. Which OOP pillar does this primarily demonstrate?

(a) Inheritance
(b) Polymorphism
(c) Encapsulation
(d) Composition

**3. (c) Encapsulation**
Private fields plus controlled public accessors bundle state with the behaviour that guards it, which is encapsulation.
- (a) No superclass/subclass relationship is involved.
- (b) No method is redefined or resolved dynamically by object type.
- (d) Composition is a whole-part object relationship, which this snippet does not show.

---

**4.** **[Easy]** *(D2 — constructor chaining order)*

What is printed?

```java
class A {
    A() { System.out.print("A "); }
}
class B extends A {
    B() { System.out.print("B "); }
    B(int x) { this(); System.out.print("B" + x + " "); }
}
public class Main {
    public static void main(String[] s) { new B(5); }
}
```

(a) B5 B A
(b) A B B5
(c) A B5 B
(d) B A B5

**4. (b) A B B5**
`new B(5)` enters `B(int)`, which immediately calls `this()` → `B()`, whose implicit `super()` runs `A()` printing `"A "`; then `B()` prints `"B "`, control returns to `B(int)` which prints `"B5 "`.
- (a) Prints the subclass constructor body before the superclass constructor.
- (d) Assumes `this()` runs after the body of `B(int)`.
- (c) Reverses the order of the two `B` prints.

| Step | Call | Prints |
|---|---|---|
| 1 | `new B(5)` → `B(int)` | — |
| 2 | `this()` → `B()` | — |
| 3 | implicit `super()` → `A()` | `A ` |
| 4 | rest of `B()` | `B ` |
| 5 | rest of `B(int)` | `B5 ` |

---

**5.** **[Easy]** *(D3 — abstract class vs interface)*

Which statement about Java abstract classes and interfaces is correct?

(a) A class may extend multiple abstract classes but implement only one interface.
(b) An interface may declare constructors; an abstract class may not.
(c) An abstract class may not contain any concrete (fully implemented) methods.
(d) An abstract class may have instance fields and constructors; an interface's fields are implicitly `public static final`.

**5. (d) An abstract class may have instance fields and constructors; an interface's fields are implicitly `public static final`.**
An abstract class is a real class and can hold state and constructors; interface fields are constants by definition.
- (a) Reverses the rule: a class can implement many interfaces but extend only one class.
- (b) Interfaces cannot declare constructors; abstract classes can.
- (c) Abstract classes may contain any number of concrete methods.

---

**6.** **[Easy]** *(D3 — access modifiers)*

Which sequence lists Java access modifiers from MOST restrictive to LEAST restrictive?

(a) private, protected, default (package-private), public
(b) default (package-private), private, protected, public
(c) protected, private, default (package-private), public
(d) private, default (package-private), protected, public

**6. (d) private, default (package-private), protected, public**
`private` is class-only; package-private adds the package; `protected` adds subclasses (and same-package access); `public` is unrestricted. This is strictly increasing visibility.
- (a) Places `protected` below package-private, but `protected` grants everything package-private grants plus subclass access.
- (c) Starts with `protected`, which is not the most restrictive.
- (b) Starts with package-private, which is not the most restrictive.

---

**7.** **[Medium]** *(D2 — static method hiding vs overriding)*

What is the output?

```java
class Parent {
    static void show() { System.out.print("Parent "); }
    void print() { System.out.print("Pprint "); }
}
class Child extends Parent {
    static void show() { System.out.print("Child "); }
    void print() { System.out.print("Cprint "); }
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        p.show();
        p.print();
        Child c = new Child();
        c.show();
    }
}
```

(a) Parent Pprint Child
(b) Child Cprint Child
(c) Parent Cprint Child
(d) Child Pprint Parent

**7. (c) Parent Cprint Child**
`static` methods are hidden, not overridden, so `p.show()` is bound by the reference type (`Parent`) → `"Parent "`. `print()` is a normal instance method, so `p.print()` dispatches to `Child` → `"Cprint "`. The second `show()` call is on a `Child` reference → `"Child "`.
- (a) Assumes `print()` also dispatches by reference type.
- (b) Assumes static methods are dispatched by object type.
- (d) Swaps the two rules: reference type for `show()`, object type for `print()`.

| Call | Resolution rule | Output |
|---|---|---|
| `p.show()` | static, by reference type `Parent` | `Parent ` |
| `p.print()` | instance, by object type `Child` | `Cprint ` |
| `c.show()` | static, by reference type `Child` | `Child ` |

---

**8.** **[Medium]** *(D2 — super() and method resolution)*

What is printed by this Python program?

```python
class A:
    def __init__(self):
        self.x = 1
    def show(self):
        return "A" + str(self.x)

class B(A):
    def __init__(self):
        super().__init__()
        self.x = 2
    def show(self):
        return super().show() + "B"

print(B().show())
```

(a) A1B
(b) A2B
(c) B2
(d) A2

**8. (b) A2B**
`B.__init__` calls `super().__init__()` (sets `x = 1`) and then overwrites `self.x = 2`. `B.show()` calls `A.show()`, which reads the current `self.x`, i.e. 2, giving `"A2"`, then appends `"B"`.
- (a) Assumes `A.show()` sees the value `1` set before the assignment in `B.__init__`.
- (c) Ignores the `super().show()` call entirely.
- (d) Omits the `"B"` appended by `B.show()`.

| Attribute | Value after `B()` | Read by |
|---|---|---|
| `self.x` | 1, then overwritten to 2 | `A.show()` via `self.x` |
| `A.show()` result | `"A2"` | `B.show()` |
| `B.show()` result | `"A2B"` | `print` |

---

**9.** **[Medium]** *(D2 — virtual vs non-virtual in C++)*

What is the output?

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    void show() { cout << "Base "; }
    virtual void tell() { cout << "BaseTell "; }
};
class Derived : public Base {
public:
    void show() { cout << "Derived "; }
    void tell()  { cout << "DerivedTell "; }
};
int main() {
    Base* b = new Derived();
    b->show();
    b->tell();
}
```

(a) Derived DerivedTell
(b) Base BaseTell
(c) Base DerivedTell
(d) Derived BaseTell

**9. (c) Base DerivedTell**
`show()` is non-virtual, so `b->show()` is bound statically to `Base::show` → `"Base "`. `tell()` is `virtual`, so `b->tell()` dispatches to `Derived::tell` → `"DerivedTell "`.
- (a) Assumes `show()` is also virtual.
- (b) Assumes `tell()` is not virtual, so no dynamic dispatch occurs.
- (d) Reverses the two members: virtual `show()`, non-virtual `tell()`.

---

**10.** **[Medium]** *(D4 — overload resolution phases)*

What is the output?

```java
public class Main {
    static void f(int x)     { System.out.print("int "); }
    static void f(long x)    { System.out.print("long "); }
    static void f(Integer x) { System.out.print("Integer "); }
    public static void main(String[] a) {
        byte b = 5;
        f(b);
        f(5);
        f(Integer.valueOf(5));
    }
}
```

(a) int long Integer
(b) Integer int Integer
(c) int int Integer
(d) long int Integer

**10. (c) int int Integer**
`f(c)` matches `f(int)` by widening (byte → int) in phase 1, which is preferred over any boxing; `f(5)` matches `f(int)` exactly; `f(Integer.valueOf(5))` matches `f(Integer)` exactly by reference identity.
- (a) Assumes `f(c)` widens to `long`; `int` is the more specific applicable widening target.
- (b) Assumes `byte` is boxed to `Integer`; primitive widening is applied before boxing.
- (d) Assumes `f(5)` widens to `long`; `int` is already an exact match.

| Call | Argument type | Applicable in phase 1? | Chosen |
|---|---|---|---|
| `f(c)` | byte | `f(int)`, `f(long)` | `int` (most specific) |
| `f(5)` | int | `f(int)` exact | `int` |
| `f(Integer.valueOf(5))` | Integer | `f(Integer)` exact | `Integer` |

---

**11.** **[Medium]** *(D5 — association, aggregation, composition)*

Which statement about aggregation and composition is correct?

(a) In composition the part's lifetime is bound to the whole; in aggregation the part can outlive the whole.
(b) Association implies ownership; aggregation implies no relationship at all.
(c) Composition allows one part to be shared by several wholes simultaneously; aggregation does not.
(d) Aggregation is a stronger whole-part relationship than composition because the part is destroyed with the whole.

**11. (a) In composition the part's lifetime is bound to the whole; in aggregation the part can outlive the whole.**
Composition is strong ownership (part destroyed with the whole); aggregation is weak ownership (part exists independently and can be shared).
- (d) Inverts the strength of the two relationships.
- (b) Both aggregation and association are relationships; aggregation is a specialised association, not the absence of one.
- (c) Inverts the sharing property: aggregation permits sharing, composition normally does not.

---

**12.** **[Medium]** *(D3 — interface default methods)*

What is printed?

```java
interface A { default String who() { return "A"; } }
interface B { default String who() { return "B"; } }
class C implements A, B {
    public String who() { return A.super.who() + B.super.who(); }
}
public class Main {
    public static void main(String[] x) { System.out.print(new C().who()); }
}
```

(a) BA
(b) Runtime exception (`ClassCastException`)
(c) Compile-time error, because `C` inherits two conflicting default methods
(d) AB

**12. (d) AB**
Both `A` and `B` declare a default `who()`, but `C` explicitly overrides it, resolving the conflict. `A.super.who()` yields `"A"` and `B.super.who()` yields `"B"`, concatenated in that order.
- (a) Reverses the concatenation order written in `C.who()`.
- (c) The conflict rule only forces an override when a class inherits two defaults without overriding; `C` does override.
- (b) No cast or runtime failure occurs here.

---

**13.** **[Medium]** *(D2 — static block, instance initializer, constructor order)*

What is printed?

```java
class Demo {
    static { System.out.print("S "); }
    { System.out.print("I "); }
    Demo() { System.out.print("C "); }
}
public class Main {
    public static void main(String[] args) {
        System.out.print("M ");
        new Demo();
        new Demo();
    }
}
```

(a) S M I C I C
(b) M S I C I C
(c) M I C S I C
(d) M S I C C I

**13. (b) M S I C I C**
`main` prints `"M "` first. The static initializer runs on the first class initialisation of `Demo`, i.e. at the first `new Demo()`. Every `new` then runs instance initializers (`"I "`) before the constructor body (`"C "`).
- (a) Places `"S "` before `"M "`, implying class initialisation happens before `main` starts.
- (c) Places the instance initializer before the static initializer.
- (d) Swaps the constructor body and the instance initializer for the second object (also for the first).

| Event | Output |
|---|---|
| `System.out.print("M ")` | `M ` |
| first `new Demo()` → static init | `S ` |
| first `new Demo()` → instance init | `I ` |
| first `new Demo()` → ctor body | `C ` |
| second `new Demo()` → instance init | `I ` |
| second `new Demo()` → ctor body | `C ` |

---

**14.** **[Medium]** *(D2 — class attribute vs instance attribute)*

What is printed?

```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
a.count += 10
print(Counter.count, a.count, b.count)
```

(a) 2 12 2
(b) 12 12 2
(c) 2 12 12
(d) 2 2 2

**14. (a) 2 12 2**
`Counter.count` is incremented twice in `__init__`, so it is 2. `a.count += 10` reads the class attribute (2) and creates an instance attribute `a.count = 12`. `b` never gets an instance attribute, so `b.count` still reads the class attribute, 2.
- (b) Assumes `a.count += 10` updates `Counter.count`.
- (c) Assumes `b.count` also sees the instance attribute created on `a`.
- (d) Assumes the class-level increments are lost.

| Expression | Value | Source |
|---|---|---|
| `Counter.count` | 2 | class attribute after two `__init__` calls |
| `a.count` | 12 | new instance attribute on `a` |
| `b.count` | 2 | class attribute (no instance attribute) |

---

**15.** **[Medium]** *(D3 — abstract class with constructor)*

What is printed?

```java
abstract class Shape {
    String name;
    Shape(String n) { name = n; }
    abstract double area();
    public String toString() { return name + ":" + area(); }
}
class Sq extends Shape {
    double s;
    Sq(double s) { super("Square"); this.s = s; }
    double area() { return s * s; }
}
public class Main {
    public static void main(String[] a) {
        Shape sh = new Sq(3);
        System.out.print(sh.toString());
    }
}
```

(a) Square:9
(b) Sq:9.0
(c) Compile-time error — an abstract class cannot declare a constructor
(d) Square:9.0

**15. (d) Square:9.0**
`Sq(3)` chains to `Shape("Square")`, so `name` is `"Square"`. `area()` returns `3.0 * 3.0 = 9.0` as a `double`, and string concatenation via `toString()` prints `9.0`.
- (a) Assumes `double` would be printed without a decimal part.
- (b) Assumes `name` holds the subclass name; it holds the string passed to `super("Square")`.
- (c) Abstract classes may declare constructors; they are invoked by subclass constructors.

---

**16.** **[Hard]** *(D2 — field hiding vs method dispatch)*

What is printed?

```java
class Parent {
    int v = 1;
    int getV() { return v; }
    int call() { return getV() + v; }
}
class Child extends Parent {
    int v = 2;
    int getV() { return v; }
}
public class Main {
    public static void main(String[] a) {
        Parent p = new Child();
        System.out.print(p.v + " " + p.getV() + " " + p.call());
    }
}
```

(a) 2 2 3
(b) 1 2 3
(c) 1 1 3
(d) 1 2 2

**16. (b) 1 2 3**
Fields are not polymorphic: `p.v` resolves by reference type → `Parent.v = 1`. `p.getV()` is an overridden instance method → `Child.getV()` returns `Child.v = 2`. `Parent.call()` is not overridden, so it runs in `Parent`; inside it, `getV()` dispatches virtually to `Child.getV()` (2) while `v` is resolved lexically to `Parent.v` (1) → 3.
- (a) Assumes `p.v` also uses dynamic dispatch and returns `Child.v`.
- (c) Assumes `p.getV()` is bound to `Parent.getV()` by reference type.
- (d) Assumes `call()` resolves `getV()` to `Parent.getV()`, which would give 1 + 1 = 2.

| Expression | Resolution | Value |
|---|---|---|
| `p.v` | field, by reference type `Parent` | 1 |
| `p.getV()` | virtual method, object type `Child` | 2 |
| `p.call()` | `Parent.call`: `getV()` → 2, `v` → 1 | 3 |

---

**17.** **[Hard]** *(D2 — C3 linearisation / super() in multiple inheritance)*

What does this Python program print?

```python
class A:
    def tag(self): return "A"
class B(A):
    def tag(self): return "B" + super().tag()
class C(A):
    def tag(self): return "C" + super().tag()
class D(B, C):
    pass

print(D().tag())
print([c.__name__ for c in D.__mro__])
```

(a) BAC then `['D', 'B', 'A', 'C', 'object']`
(b) BCA then `['D', 'B', 'C', 'A', 'object']`
(c) BCA then `['D', 'C', 'B', 'A', 'object']`
(d) ABC then `['D', 'B', 'C', 'A', 'object']`

**17. (b) BCA then `['D', 'B', 'C', 'A', 'object']`**
With `class D(B, C)`, the C3 linearisation is `D, B, C, A, object`. `super()` inside `B.tag` therefore moves to `C`, not to `A`, giving `"B" + ("C" + "A")` = `"BCA"`.
- (a) Assumes `super()` in `B` jumps straight to `A`, which would happen only with `class D(B)`.
- (d) Assumes `super()` in `B` reaches `A` first and `C` never runs, producing `"ABC"`.
- (c) Reverses the base order in the MRO; Python uses the declared order `(B, C)`.

| Attribute | Value after `B.__init__` for `B()` | Read by |
|---|---|---|
| `self.x` (B) | 1, then set to 2 | `A.show()` |
| superclass call | `A.__init__()` | sets `x = 1` |
| `show()` result | `"A" + "2" + "B"` | `print` |

Corrected table for Q17:

| MRO position | Class | `super()` step in `B.tag` |
|---|---|---|
| 1 | D | — |
| 2 | B | next → C |
| 3 | C | next → A |
| 4 | A | returns `"A"` |
| 5 | object | — |

Result string: `"B" + "C" + "A"` = `"BCA"`.

---

**18.** **[Hard]** *(D4 — widening vs boxing vs varargs priority)*

What is the output?

```java
public class Main {
    static void g(long x)    { System.out.print("long "); }
    static void g(Integer x) { System.out.print("Integer "); }
    static void g(int... x)  { System.out.print("varargs "); }
    public static void main(String[] a) {
        g(5);
        g(Integer.valueOf(5));
    }
}
```

(a) long Integer
(b) varargs Integer
(c) Integer Integer
(d) long varargs

---

**18. (a) long Integer**
For `g(5)` the literal is `int`; phase 1 (no boxing, no varargs) finds `g(long)` by widening, which beats any phase-3 varargs match. For `g(Integer.valueOf(5))`, phase 1 finds the exact `g(Integer)` match by reference subtyping, so it wins over the unboxing route to `g(long)`.
- (b) Varargs is considered only in phase 3, after widening and boxing have failed.
- (c) Assumes `int` is boxed; primitive widening to `long` is preferred over boxing.
- (d) Assumes `g(Integer.valueOf(5))` unboxes and widens to `long` instead of matching `g(Integer)` exactly.

| Call | Argument type | Phase 1 candidates | Chosen |
|---|---|---|---|
| `g(5)` | int | `g(long)` by widening | `long` |
| `g(Integer.valueOf(5))` | Integer | `g(Integer)` by identity | `Integer` |

---

**19.** **[Easy]** *(D1 — abstract class vs interface)*

Which statement is correct?

(a) A class may extend only one class but may implement several interfaces.

(b) An interface may declare instance fields, and each implementing class gets its own copy of them.

(c) An abstract class cannot declare a constructor.

(d) An interface can declare a constructor that implementers invoke with `super()`.

---

**19. (d) A class may extend only one class but may implement several interfaces.**
Class inheritance is single in Java/C#, while interface implementation is multiple.

- (b) Interface fields are implicitly `public static final` constants shared by all implementers; C# interfaces cannot declare instance fields at all.
- (c) Abstract classes can declare constructors; they run when a subclass instance is created.
- (a) Interfaces cannot declare constructors in either Java or C#.

---

**20.** **[Easy]** *(D1 — access modifiers and visibility)*

```java
// p1/A.java
package p1;
public class A {
    void show() { System.out.print("A"); }
}

// p2/B.java
package p2;
public class B extends A { }

// p2/Main.java
package p2;
public class Main {
    public static void main(String[] args) { new B().show(); }
}
```

What happens when `Main` is compiled?

(a) It prints `A`.

(b) It throws a runtime exception because `show()` is not accessible.

(c) It compiles and prints nothing, because the inherited method is suppressed.

(d) Compile-time error in `Main`: `show()` is not public in `A`; cannot be accessed from outside package.

---

**20. (b) Compile-time error in `Main`: `show()` is not public in `A`; cannot be accessed from outside package.**
`show()` has default access, so it is visible only inside `p1`; `Main` in `p2` cannot call it.

- (a) The program never reaches runtime; the call is rejected while compiling `Main`.
- (c) Access failure is a compile-time error, not a runtime exception.
- (d) Compilation fails outright, so nothing is printed.

---

**21.** **[Easy]** *(D1 — static vs instance members)*

Which statement about a `static` method is true?

(a) It can access instance variables of its own class directly.

(b) It is overridden by a subclass method with a different return type.

(c) It cannot be overloaded.

(d) It can be called using the class name without creating an instance of the class.

---

**21. (c) It can be called using the class name without creating an instance of the class.**
Static methods belong to the class, not to an object, so no instance is required.

- (a) A static method has no `this`, so it cannot touch instance variables directly.
- (b) Overloading depends only on the parameter signature and applies to static methods too.
- (d) Static methods are hidden, not overridden, and hiding requires a compatible return type.

---

**22.** **[Medium]** *(D1 — method hiding)*

```java
class P { static void f() { System.out.print("P"); } }
class C extends P { static void f() { System.out.print("C"); } }

P ref = new C();
ref.f();
```

What is printed?

(a) `C`

(b) Compile-time error: a static method cannot be inherited

(c) `C` followed by a runtime exception

(d) `P`

---

**22. (a) `P`**
Static methods are resolved at compile time from the reference type, and `ref` is declared as `P`.

- (d) Dynamic dispatch applies only to instance methods, not to static methods.
- (b) It compiles; calling a static method through an instance reference is legal in Java.
- (c) No exception occurs; the static call is bound to `P.f()` at compile time.

---

**23.** **[Medium]** *(D1 — association vs aggregation vs composition)*

An `Order` object creates its own `OrderLine` objects inside its constructor, and no other object ever holds a reference to those `OrderLine` objects. When the `Order` is discarded, its lines are gone with it. Which relationship is modelled?

(a) Association

(b) Aggregation

(c) Composition

(d) Inheritance

---

**23. (c) Composition**
The whole creates the parts, owns them, and their lifetime ends with it — the defining traits of composition.

- (b) Aggregation parts are separate objects referenced from outside and can outlive the whole.
- (a) Association is a general link with no ownership or lifetime control.
- (d) Inheritance is an "is-a" relationship, not a whole–part one.

---

**24.** **[Medium]** *(D1 — abstract class vs interface)*

```java
abstract class Shape {
    abstract double area();
    double describe() { return "area=" + area(); }
}
```

Which statement is true?

(a) `Shape` can be instantiated because it contains the concrete method `describe()`.

(b) `Shape` cannot be instantiated, and a class extending `Shape` that does not implement `area()` must itself be declared abstract.

(c) Every subclass of `Shape` must implement `area()`, whether or not it is declared abstract.

(d) An anonymous subclass of `Shape` must override both `area()` and `describe()`.

---

**24. (d) `Shape` cannot be instantiated, and a class extending `Shape` that does not implement `area()` must itself be declared abstract.**
An abstract class cannot be instantiated, and any concrete subclass must implement all inherited abstract methods.

- (a) Concrete methods do not make an abstract class instantiable.
- (b) A subclass that does not implement `area()` compiles fine if it is declared abstract.
- (c) `describe()` is concrete and inherited; only `area()` must be implemented.

---

**25.** **[Medium]** *(D1 — access modifiers and visibility)*

In Java, which statement about access modifiers is true?

(a) A `private` member is visible to every class in the same package.

(b) A `protected` member of a class in package `p1` can be accessed by any unrelated class in package `p2`.

(c) A `protected` member is visible in the same package and, from a subclass in another package, only through a reference whose type is that subclass or a subtype of it.

(d) The default (package-private) modifier is more restrictive than `private`.

---

**25. (d) A `protected` member is visible in the same package and, from a subclass in another package, only through a reference whose type is that subclass or a subtype of it.**
This matches the JLS rule for protected access from a subclass in a different package.

- (a) `private` is visible only within the declaring class (and its nested classes).
- (c) Unrelated classes in another package cannot access a `protected` member at all.
- (b) Default is less restrictive than `private`, not more.

---

**26.** **[Medium]** *(D1 — association vs aggregation vs composition)*

Which statement about whole–part relationships is true?

(a) In aggregation, the part is automatically destroyed when the whole is destroyed.

(b) In aggregation the part can outlive the whole and is usually supplied from outside; in composition the whole creates, owns and controls the lifetime of the part.

(c) Aggregation and composition both require the part class to inherit from the whole class.

(d) Composition is a weak "has-a" relationship and aggregation is a strong "has-a" relationship.

---

**26. (b) In aggregation the part can outlive the whole and is usually supplied from outside; in composition the whole creates, owns and controls the lifetime of the part.**
Aggregation is a weak whole–part link; composition is the strong, owner-controlled form.

- (a) Destroying parts with the whole is a property of composition, not aggregation.
- (d) The definitions are reversed: composition is the strong form.
- (c) Both are "has-a" relationships and neither requires inheritance.

---

**27.** **[Hard]** *(D1 — static vs instance members, constructor dispatch)*

```java
abstract class A {
    A() { print(); }
    abstract void print();
}
class B extends A {
    int v = 5;
    void print() { System.out.println(v); }
}
public class Main {
    public static void main(String[] args) { new B(); }
}
```

What is the output?

(a) `0`

(b) `5`

(c) Compile-time error: an abstract method cannot be called from a constructor

(d) `NullPointerException` at runtime

---

**27. (b) `0`**
`A`'s constructor calls the overridden `print()` before `B`'s field initializer runs, so `v` still holds its default value.

- (a) `v = 5` is assigned only after the superclass constructor finishes.
- (c) It compiles; calling an overridable method from a constructor is legal, though risky.
- (d) No exception is thrown — `v` simply prints its default int value.

---

**28.** **[Easy]** *(D1 — constructor chaining order)*

What does this program print?

```java
class A {
    A()      { System.out.print("A"); }
    A(int x) { this(); System.out.print("A" + x); }
}
class B extends A {
    B()      { super(5); System.out.print("B"); }
}
public class Main {
    public static void main(String[] args) { new B(); }
}
```

(a) A5AB
(b) ABA5
(c) AA5B
(d) A5B

---

**28. (d) AA5B** — `B()` calls `super(5)`, which calls `this()` → `A()` prints `A`, then `A(5)` prints `A5`, then `B()` prints `B`.
- (a) reverses the order of the two `A` prints.
- (b) misplaces `B` before `A5`; `super(5)` must finish first.
- (c) drops the `A()` call triggered by `this()`.

---

**29.** **[Easy]** *(D1 — overriding and dynamic dispatch)*

What is the output?

```python
class A:
    def show(self):
        print("A", end="")

class B(A):
    def show(self):
        print("B", end="")

class C(A):
    pass

for obj in (B(), C(), A()):
    obj.show()
```

(a) BAA
(b) ABA
(c) BBB
(d) AAA

---

**29. (c) BAA** — `B` overrides `show`, `C` inherits `A.show`, so the loop resolves to `B`, `A`, `A`.
- (a) reverses the last two objects.
- (b) assumes `C` also overrides — it does not.
- (d) ignores the override in `B`.

---

**30.** **[Medium]** *(D1 — multi-level constructor chaining)*

What does this print?

```java
class P { P() { System.out.print("P"); } }

class Q extends P {
    Q()      { System.out.print("Q"); }
    Q(int n) { this(); System.out.print(n); }
}

class R extends Q {
    R() { super(7); System.out.print("R"); }
}

public class Main {
    public static void main(String[] args) { new R(); }
}
```

(a) PQ7R
(b) Q7PR
(c) P7QR
(d) PQR7

---

**30. (b) PQ7R** — `super(7)` → `Q(7)` → `this()` → `Q()` → `super()` → `P()`, giving `P Q 7 R`.
- (a) prints `R` before the argument passed to `super(7)`.
- (d) starts with `Q`, but `P()` always runs first.
- (c) prints `7` before `Q()`'s body, which runs earlier.

---

**31.** **[Hard]** *(D1 — static overload resolution vs dynamic dispatch)*

What is the output of `main`?

```java
class Base {
    void show(Object o) { System.out.print("B-obj "); }
    void show(String s) { System.out.print("B-str "); }
}
class Derived extends Base {
    void show(Object o) { System.out.print("D-obj "); }
    void show(String s) { System.out.print("D-str "); }
}
public class Main {
    public static void main(String[] args) {
        Base b = new Derived();
        b.show("hi");
        b.show((Object) "hi");
    }
}
```

(a) D-str B-obj
(b) D-str D-obj
(c) B-str B-obj
(d) B-str D-obj

---

**31. (b) B-str D-obj** — Overload choice uses the static type (`Base`) → `B-str`; the call dispatches to the override in `Derived` for the `Object` version → `D-obj`.
- (a) wrongly treats overload selection as dynamic.
- (c) wrongly treats the second call as non-virtual.
- (d) gets both mechanisms backwards.

---

**32.** **[Medium]** *(D1 — Python MRO and `super()` chaining)*

What does this print?

```python
class A:
    def __init__(self): print("A", end="")

class B(A):
    def __init__(self): print("B", end=""); super().__init__()

class C(A):
    def __init__(self): print("C", end=""); super().__init__()

class D(B, C):
    def __init__(self): print("D", end=""); super().__init__()

D()
```

(a) DBCA
(b) ABCD
(c) DBAC
(d) DCBA

---

**32. (c) DBCA** — MRO is `D, B, C, A`; each `super().__init__()` moves to the next class in that chain.
- (a) puts `A` before `C`, breaking the MRO.
- (b) reverses the entire order.
- (d) reverses the order of `B` and `C`.

---

**33.** **[Medium]** *(D1 — field hiding vs method overriding)*

What is printed?

```java
class Parent {
    int x = 10;
    int getX() { return x; }
}
class Child extends Parent {
    int x = 20;
    int getX() { return x; }
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.x + " " + p.getX());
    }
}
```

(a) 20 20
(b) 10 10
(c) 20 10
(d) 10 20

---

**33. (b) 10 20** — Field access `p.x` is resolved by the reference type `Parent` (10); `p.getX()` is virtual and runs `Child.getX()` (20).
- (a) treats fields as polymorphic.
- (c) applies virtual dispatch to the field and static binding to the method.
- (d) ignores the override in `Child`.

---

**34.** **[Easy]** *(D1 — inheritance with `super().__init__`)*

What is the output?

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return self.name + " says meow"

print(Cat("Tom").speak())
```

(a) Tom says meow
(b) Cat says meow
(c) ...
(d) ... says meow

---

**34. (a) Tom says meow** — `Cat.__init__` passes `name` to `Animal.__init__`, and `Cat.speak` returns `self.name` + `" says meow"`.
- (d) assumes `speak` was not overridden.
- (b) uses the class name instead of the argument.
- (c) calls the base class version of `speak`.

---

**35.** **[Hard]** *(D1 — overridable method called from a constructor)*

What does this program print?

```java
class Base {
    Base()       { print(); }
    void print() { System.out.print("Base "); }
}
class Derived extends Base {
    int v = 5;
    Derived()    { super(); System.out.print("D" + v); }
    void print() { System.out.print("v" + v + " "); }
}
public class Main {
    public static void main(String[] args) { new Derived(); }
}
```

(a) Base D5
(b) v5 D5
(c) v0 D5
(d) v0 D0

---

**35. (a) v0 D5** — `Base()` calls the overridden `print()` before `Derived`'s field initialiser runs, so `v` is still 0; then `D` + `5` is printed.
- (b) assumes fields are initialised before `super()` returns.
- (c) assumes the call is statically bound to `Base.print`.
- (d) assumes `v` stays 0 inside the constructor body.

---

**36.** **[Medium]** *(D1 — dynamic dispatch inside an inherited method)*

What is the output?

```python
class Base:
    def greet(self):
        return "Base:" + self.name()
    def name(self):
        return "base"

class Child(Base):
    def name(self):
        return "child"

print(Base().greet(), Child().greet())
```

(a) Base:base Base:base
(b) Base:base Base:child
(c) child base
(d) Base:child Base:child

---

---

**19.** **[Easy]** *(D1 — abstract class vs interface)*

Which statement is correct?

(a) An interface can declare a constructor that implementers invoke with `super()`.

(b) An interface may declare instance fields, and each implementing class gets its own copy of them.

(c) An abstract class cannot declare a constructor.

(d) A class may extend only one class but may implement several interfaces.

---

**20.** **[Easy]** *(D1 — access modifiers and visibility)*

```java
// p1/A.java
package p1;
public class A {
    void show() { System.out.print("A"); }
}

// p2/B.java
package p2;
public class B extends A { }

// p2/Main.java
package p2;
public class Main {
    public static void main(String[] args) { new B().show(); }
}
```

What happens when `Main` is compiled?

(a) It prints `A`.

(b) Compile-time error in `Main`: `show()` is not public in `A`; cannot be accessed from outside package.

(c) It throws a runtime exception because `show()` is not accessible.

(d) It compiles and prints nothing, because the inherited method is suppressed.

---

**21.** **[Easy]** *(D1 — static vs instance members)*

Which statement about a `static` method is true?

(a) It can access instance variables of its own class directly.

(b) It cannot be overloaded.

(c) It can be called using the class name without creating an instance of the class.

(d) It is overridden by a subclass method with a different return type.

---

**22.** **[Medium]** *(D1 — method hiding)*

```java
class P { static void f() { System.out.print("P"); } }
class C extends P { static void f() { System.out.print("C"); } }

P ref = new C();
ref.f();
```

What is printed?

(a) `P`

(b) Compile-time error: a static method cannot be inherited

(c) `C` followed by a runtime exception

(d) `C`

---

**23.** **[Medium]** *(D1 — association vs aggregation vs composition)*

An `Order` object creates its own `OrderLine` objects inside its constructor, and no other object ever holds a reference to those `OrderLine` objects. When the `Order` is discarded, its lines are gone with it. Which relationship is modelled?

(a) Association

(b) Aggregation

(c) Composition

(d) Inheritance

---

**24.** **[Medium]** *(D1 — abstract class vs interface)*

```java
abstract class Shape {
    abstract double area();
    double describe() { return "area=" + area(); }
}
```

Which statement is true?

(a) `Shape` can be instantiated because it contains the concrete method `describe()`.

(b) Every subclass of `Shape` must implement `area()`, whether or not it is declared abstract.

(c) An anonymous subclass of `Shape` must override both `area()` and `describe()`.

(d) `Shape` cannot be instantiated, and a class extending `Shape` that does not implement `area()` must itself be declared abstract.

---

**25.** **[Medium]** *(D1 — access modifiers and visibility)*

In Java, which statement about access modifiers is true?

(a) A `private` member is visible to every class in the same package.

(b) The default (package-private) modifier is more restrictive than `private`.

(c) A `protected` member of a class in package `p1` can be accessed by any unrelated class in package `p2`.

(d) A `protected` member is visible in the same package and, from a subclass in another package, only through a reference whose type is that subclass or a subtype of it.

---

**26.** **[Medium]** *(D1 — association vs aggregation vs composition)*

Which statement about whole–part relationships is true?

(a) In aggregation, the part is automatically destroyed when the whole is destroyed.

(b) In aggregation the part can outlive the whole and is usually supplied from outside; in composition the whole creates, owns and controls the lifetime of the part.

(c) Aggregation and composition both require the part class to inherit from the whole class.

(d) Composition is a weak "has-a" relationship and aggregation is a strong "has-a" relationship.

---

**27.** **[Hard]** *(D1 — static vs instance members, constructor dispatch)*

```java
abstract class A {
    A() { print(); }
    abstract void print();
}
class B extends A {
    int v = 5;
    void print() { System.out.println(v); }
}
public class Main {
    public static void main(String[] args) { new B(); }
}
```

What is the output?

(a) `5`

(b) `0`

(c) Compile-time error: an abstract method cannot be called from a constructor

(d) `NullPointerException` at runtime

---

**28.** **[Easy]** *(D1 — constructor chaining order)*

What does this program print?

```java
class A {
    A()      { System.out.print("A"); }
    A(int x) { this(); System.out.print("A" + x); }
}
class B extends A {
    B()      { super(5); System.out.print("B"); }
}
public class Main {
    public static void main(String[] args) { new B(); }
}
```

(a) A5AB
(b) ABA5
(c) A5B
(d) AA5B

---

**29.** **[Easy]** *(D1 — overriding and dynamic dispatch)*

What is the output?

```python
class A:
    def show(self):
        print("A", end="")

class B(A):
    def show(self):
        print("B", end="")

class C(A):
    pass

for obj in (B(), C(), A()):
    obj.show()
```

(a) ABA
(b) BBB
(c) BAA
(d) AAA

---

**30.** **[Medium]** *(D1 — multi-level constructor chaining)*

What does this print?

```java
class P { P() { System.out.print("P"); } }

class Q extends P {
    Q()      { System.out.print("Q"); }
    Q(int n) { this(); System.out.print(n); }
}

class R extends Q {
    R() { super(7); System.out.print("R"); }
}

public class Main {
    public static void main(String[] args) { new R(); }
}
```

(a) PQR7
(b) PQ7R
(c) P7QR
(d) Q7PR

---

**31.** **[Hard]** *(D1 — static overload resolution vs dynamic dispatch)*

What is the output of `main`?

```java
class Base {
    void show(Object o) { System.out.print("B-obj "); }
    void show(String s) { System.out.print("B-str "); }
}
class Derived extends Base {
    void show(Object o) { System.out.print("D-obj "); }
    void show(String s) { System.out.print("D-str "); }
}
public class Main {
    public static void main(String[] args) {
        Base b = new Derived();
        b.show("hi");
        b.show((Object) "hi");
    }
}
```

(a) D-str D-obj
(b) B-str D-obj
(c) B-str B-obj
(d) D-str B-obj

---

**32.** **[Medium]** *(D1 — Python MRO and `super()` chaining)*

What does this print?

```python
class A:
    def __init__(self): print("A", end="")

class B(A):
    def __init__(self): print("B", end=""); super().__init__()

class C(A):
    def __init__(self): print("C", end=""); super().__init__()

class D(B, C):
    def __init__(self): print("D", end=""); super().__init__()

D()
```

(a) DBAC
(b) ABCD
(c) DBCA
(d) DCBA

---

**33.** **[Medium]** *(D1 — field hiding vs method overriding)*

What is printed?

```java
class Parent {
    int x = 10;
    int getX() { return x; }
}
class Child extends Parent {
    int x = 20;
    int getX() { return x; }
}
public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.x + " " + p.getX());
    }
}
```

(a) 20 20
(b) 10 20
(c) 20 10
(d) 10 10

---

**34.** **[Easy]** *(D1 — inheritance with `super().__init__`)*

What is the output?

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return self.name + " says meow"

print(Cat("Tom").speak())
```

(a) Tom says meow
(b) Cat says meow
(c) ...
(d) ... says meow

---

**35.** **[Hard]** *(D1 — overridable method called from a constructor)*

What does this program print?

```java
class Base {
    Base()       { print(); }
    void print() { System.out.print("Base "); }
}
class Derived extends Base {
    int v = 5;
    Derived()    { super(); System.out.print("D" + v); }
    void print() { System.out.print("v" + v + " "); }
}
public class Main {
    public static void main(String[] args) { new Derived(); }
}
```

(a) v0 D5
(b) v5 D5
(c) Base D5
(d) v0 D0

---

**36.** **[Medium]** *(D1 — dynamic dispatch inside an inherited method)*

What is the output?

```python
class Base:
    def greet(self):
        return "Base:" + self.name()
    def name(self):
        return "base"

class Child(Base):
    def name(self):
        return "child"

print(Base().greet(), Child().greet())
```

(a) Base:base Base:child
(b) child base
(c) Base:base Base:base
(d) Base:child Base:child

---

---

**36. (a) Base:base Base:child** — `greet` is inherited unchanged and calls `self.name()`, which resolves to each object's own class.
- (c) ignores the override of `name` in `Child`.
- (b) treats the return of `greet` as just the name.
- (d) uses `child` for the `Base` instance as well.

---
