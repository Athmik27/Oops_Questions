# Python OOPs Question Bank



--- 

# 1. OOP Fundamentals

## Q1. What is OOP?

OOP stands for **Object-Oriented Programming**.

It is a programming paradigm that organizes software around **objects**, which contain data and behavior.

---

## Q2. What are the main concepts of OOP?

The four major pillars are:

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

Other important concepts include:

* Class
* Object
* Constructor
* Method
* Composition
* Aggregation
* Method overriding
* Operator overloading

---

## Q3. What are the advantages of OOP?

* Code reusability
* Maintainability
* Modularity
* Data protection
* Easier debugging
* Scalability
* Code organization

---

## Q4. What are the four pillars of OOP?

### Encapsulation

Bundling data and methods together and controlling access to internal state.

### Abstraction

Hiding implementation details and exposing required functionality.

### Inheritance

Acquiring behavior from an existing class.

### Polymorphism

Allowing the same interface/method to have different implementations or behaviors.

---

## Q5. What is the difference between procedural programming and OOP?

| Procedural                                        | OOP                                                 |
| ------------------------------------------------- | --------------------------------------------------- |
| Focuses on functions                              | Focuses on objects                                  |
| Data and functions are generally separate         | Data and methods are grouped                        |
| Less suitable for very large object-based systems | Useful for large modular systems                    |
| Reusability mainly through functions              | Reusability through classes/inheritance/composition |

---

# 2. Classes and Objects

## Q6. What is a class?

A class is a blueprint/template used to create objects.

```python
class Student:
    pass
```

---

## Q7. What is an object?

An object is an instance of a class.

```python
s1 = Student()
```

---

## Q8. Difference between class and object?

**Class:**

* Blueprint
* Defines structure and behavior

**Object:**

* Instance of a class
* Has actual state/data

---

## Q9. Can a class exist without creating an object?

Yes.

A class can be defined without creating an instance.

---

## Q10. Can multiple objects be created from one class?

Yes.

```python
class Student:
    pass

s1 = Student()
s2 = Student()
s3 = Student()
```

---

## Q11. Are objects independent?

Usually, each object has its own instance state.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

```python
s1 = Student("A")
s2 = Student("B")
```

`s1.name` and `s2.name` are independent instance attributes.

---

# 3. Constructors and `self`

## Q12. What is a constructor in Python?

`__init__()` is the initializer method commonly used to initialize an object after it is created.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## Q13. Is `__init__()` actually a constructor?

Strictly speaking, Python's object creation involves `__new__()`, while `__init__()` initializes the newly created object.

For most placement interviews, it is commonly called the **constructor/initializer**.

---

## Q14. What is `self`?

`self` refers to the current object.

```python
class Student:

    def display(self):
        print(self)
```

---

## Q15. Is `self` a keyword?

No.

`self` is a conventional parameter name.

However, using `self` is the standard Python convention.

---

## Q16. Can we use another name instead of `self`?

Technically yes.

```python
class Student:

    def display(this):
        print(this)
```

But using `self` is strongly recommended.

---

## Q17. Why is `self` required?

It allows instance methods to access the current object's:

* Attributes
* Methods
* State

---

## Q18. What happens if we forget `self`?

Example:

```python
class Student:

    def display():
        print("Hello")
```

Calling:

```python
s = Student()
s.display()
```

causes an argument-related error because Python passes the instance to the method.

---

## Q19. Can `__init__()` return a value?

No.

`__init__()` must return `None`.

This is invalid:

```python
def __init__(self):
    return 10
```

---

## Q20. Can a class have more than one `__init__()`?

You can write only one effective `__init__()` method under the same class name.

A later definition replaces the earlier one.

---

# 4. Methods and Variables

## Q21. What is an instance variable?

A variable associated with an individual object.

```python
self.name = name
```

---

## Q22. What is a class variable?

A variable defined at class level and shared through the class unless shadowed by an instance attribute.

```python
class Student:

    college = "ABC"
```

---

## Q23. Instance variable vs class variable?

| Instance Variable                  | Class Variable                           |
| ---------------------------------- | ---------------------------------------- |
| Belongs to object                  | Belongs to class                         |
| Usually defined using `self`       | Defined inside class body                |
| Each object can have its own value | Shared by instances through class lookup |

---

## Q24. What is an instance method?

A method that operates on an object and normally receives `self`.

```python
def display(self):
    pass
```

---

## Q25. What is a class method?

A method associated with the class and normally receiving `cls`.

```python
@classmethod
def method(cls):
    pass
```

---

## Q26. What is a static method?

A method that does not automatically receive `self` or `cls`.

```python
@staticmethod
def add(a, b):
    return a + b
```

---

## Q27. Difference between instance, class and static methods?

| Instance                | Class                  | Static                      |
| ----------------------- | ---------------------- | --------------------------- |
| `self`                  | `cls`                  | No automatic first argument |
| Works with object state | Works with class state | Independent utility logic   |
| `obj.method()`          | `Class.method()`       | `Class.method()`            |

---

## Q28. Can a class method access instance variables directly?

No.

A class method receives `cls`, not a particular instance.

---

## Q29. Can a static method access instance variables directly?

No.

It does not automatically receive an instance.

---

## Q30. Can a static method access class variables?

Not automatically.

It can access them explicitly through the class name if appropriate.

---

# 5. Encapsulation

## Q31. What is encapsulation?

Encapsulation is the bundling of data and methods into a class while controlling access to internal state.

---

## Q32. Why is encapsulation important?

It helps:

* Protect internal state
* Validate data
* Prevent accidental modification
* Improve maintainability
* Provide controlled interfaces

---

## Q33. Does Python support private variables?

Python does not have Java-style strict private access control.

Double underscore triggers **name mangling**.

```python
self.__balance
```

---

## Q34. What is name mangling?

Python changes the internal name of a double-underscore attribute roughly to:

```text
_ClassName__attribute
```

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 90
```

The attribute is internally associated with:

```text
_Student__marks
```

---

## Q35. What is a protected variable in Python?

A single underscore is a convention indicating internal/subclass-oriented use.

```python
self._salary
```

It is not strict access protection.

---

## Q36. What is a public variable?

A normal attribute.

```python
self.name
```

---

## Q37. Does Python have true private variables?

Python primarily uses conventions and name mangling rather than strict private access modifiers.

---

## Q38. What is a getter?

A method/property used to retrieve internal data.

---

## Q39. What is a setter?

A method/property used to modify internal data, often with validation.

---

## Q40. Why use getters and setters?

To control how data is read or modified.

Example:

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
```

---

# 6. Abstraction

## Q41. What is abstraction?

Abstraction hides unnecessary implementation details and exposes the essential interface.

---

## Q42. How is abstraction implemented in Python?

Commonly using:

```python
from abc import ABC, abstractmethod
```

---

## Q43. What is an abstract class?

A class intended to define an interface/base behavior and may contain abstract methods.

Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Q44. What is an abstract method?

A method declared using `@abstractmethod` that concrete subclasses are expected to implement.

---

## Q45. Can we create an object of an abstract class?

If the class has unimplemented abstract methods, Python prevents instantiation.

---

## Q46. Can an abstract class contain normal methods?

Yes.

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Sleeping")
```

---

## Q47. Can an abstract class have a constructor?

Yes.

An abstract class can define `__init__()`.

---

## Q48. Can an abstract class have instance variables?

Yes.

---

## Q49. Can an abstract method have implementation?

Yes.

An abstract method can contain code, although subclasses still need to satisfy the abstract contract.

---

## Q50. What happens if a subclass does not implement all abstract methods?

The subclass remains abstract and cannot be instantiated until all required abstract methods are implemented.

---

## Q51. Abstraction vs encapsulation?

### Abstraction

Focuses on:

> What should the user see/use?

### Encapsulation

Focuses on:

> How do we control and protect internal state?

---

## Q52. Real-world example of abstraction?

ATM:

You interact with:

* Withdraw
* Deposit
* Balance

You don't need to know the internal banking implementation.

---

# 7. Inheritance

## Q53. What is inheritance?

Inheritance allows a child class to reuse or extend behavior from a parent class.

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

---

## Q54. Why use inheritance?

* Code reuse
* Extending existing behavior
* Representing IS-A relationships
* Supporting polymorphism

---

## Q55. What are the types of inheritance in Python?

1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid

---

## Q56. What is single inheritance?

One child inherits from one parent.

```text
Animal
   ↓
 Dog
```

---

## Q57. What is multiple inheritance?

One child inherits from multiple parents.

```python
class Child(Father, Mother):
    pass
```

---

## Q58. What is multilevel inheritance?

Inheritance through multiple levels.

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

---

## Q59. What is hierarchical inheritance?

Multiple children inherit from one parent.

```text
       Animal
       /    \
     Dog    Cat
```

---

## Q60. What is hybrid inheritance?

A combination of multiple inheritance structures.

---

## Q61. Can Python support multiple inheritance?

Yes.

```python
class C(A, B):
    pass
```

---

## Q62. What are the disadvantages of inheritance?

Potential issues include:

* Tight coupling
* Complex class hierarchies
* Difficult maintenance
* Multiple inheritance complexity
* Fragile base-class behavior

---

## Q63. What is IS-A relationship?

Inheritance generally represents an IS-A relationship.

```text
Dog IS-A Animal
```

---

## Q64. What is HAS-A relationship?

Composition/aggregation generally represents HAS-A.

```text
Car HAS-A Engine
```

---

# 8. Polymorphism

## Q65. What is polymorphism?

Polymorphism means that a common interface can produce different behavior depending on the object.

---

## Q66. What are common forms of polymorphism in Python?

Examples include:

* Method overriding
* Duck typing
* Operator overloading
* Generic functions working with different object types

---

## Q67. What is runtime polymorphism?

When the method implementation used depends on the object involved at runtime.

Method overriding is a common example.

---

## Q68. What is method overriding?

A child class provides its own implementation of a parent method.

```python
class Animal:

    def sound(self):
        print("Animal")


class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

## Q69. What is duck typing?

Python focuses on whether an object supports the required behavior rather than requiring a specific class.

> "If it behaves like the required object, it can be used."

---

## Q70. What is operator overloading?

Defining how operators behave with custom objects.

Examples:

```python
__add__()
__sub__()
__eq__()
__lt__()
```

---

## Q71. Can Python achieve polymorphism without inheritance?

Yes.

Duck typing allows unrelated classes to provide the same method.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

Both can be used by code expecting an object with `sound()`.

---

# 9. Method Overloading

## Q72. Does Python support method overloading?

Python does not support traditional method overloading where multiple methods with the same name coexist based solely on different parameter lists.

---

## Q73. How can we simulate method overloading?

Using:

### Default arguments

```python
def add(a, b=0):
    return a + b
```

### `*args`

```python
def add(*numbers):
    return sum(numbers)
```

### `**kwargs`

```python
def display(**data):
    print(data)
```

---

## Q74. Method overloading vs overriding?

| Overloading                                       | Overriding                           |
| ------------------------------------------------- | ------------------------------------ |
| Same method name with different argument patterns | Child replaces/extends parent method |
| Traditional form not directly supported in Python | Supported                            |
| Usually within same class                         | Requires inheritance                 |
| Compile-time concept in languages like Java       | Runtime behavior                     |

---

# 10. Method Overriding

## Q75. What is method overriding?

When a subclass provides its own implementation of an inherited method.

---

## Q76. Why is method overriding useful?

It allows subclasses to specialize parent behavior.

---

## Q77. Can we call the parent version after overriding?

Yes.

Use:

```python
super().method()
```

---

## Q78. Can a static method be overridden?

Yes, a subclass can define a method with the same name, although static/class/instance method descriptors have different binding behavior.

---

# 11. `super()`

## Q79. What is `super()`?

`super()` provides a way to access behavior from the next class in the MRO.

---

## Q80. Why use `super()`?

Common uses:

* Calling parent initialization
* Calling inherited behavior
* Supporting cooperative multiple inheritance

---

## Q81. Can `super()` call a parent constructor?

Yes.

```python
super().__init__()
```

---

## Q82. Can `super()` call a parent method?

Yes.

```python
super().display()
```

---

## Q83. Does `super()` always mean "direct parent"?

Not exactly.

It follows the **Method Resolution Order (MRO)**.

This distinction becomes important in multiple inheritance.

---

# 12. MRO

## Q84. What is MRO?

MRO stands for:

**Method Resolution Order**

It determines the order in which Python searches classes for attributes and methods.

---

## Q85. How can we see MRO?

```python
ClassName.mro()
```

or:

```python
ClassName.__mro__
```

---

## Q86. Why is MRO important?

It is especially important in:

* Multiple inheritance
* `super()`
* Diamond inheritance

---

## Q87. What algorithm does Python use for MRO?

Python 3 uses **C3 linearization**.

---

# 13. Multiple Inheritance

## Q88. What is multiple inheritance?

A class inherits from more than one parent.

```python
class C(A, B):
    pass
```

---

## Q89. What problem can occur with multiple inheritance?

Potential problems include:

* Method ambiguity
* Complex hierarchies
* Diamond problem

Python resolves method lookup using MRO.

---

## Q90. What is the diamond problem?

Example:

```text
       A
      / \
     B   C
      \ /
       D
```

`D` inherits through both `B` and `C`.

Python's MRO determines the order in which methods are searched.

---

## Q91. How does Python solve the diamond problem?

Using **C3 MRO**.

---

# 14. Access Modifiers

## Q92. What access levels are commonly discussed in Python?

```text
Public
Protected
Private
```

---

## Q93. What is public?

```python
self.name
```

No special naming convention.

---

## Q94. What is protected?

```python
self._name
```

A convention indicating internal/subclass use.

---

## Q95. What is private?

```python
self.__name
```

Python performs name mangling.

---

## Q96. Is `_variable` truly protected?

No.

It is mainly a convention.

---

## Q97. Is `__variable` completely inaccessible?

No.

Name mangling can be bypassed using the mangled name.

Example:

```python
obj._ClassName__variable
```

This should generally not be used unless you understand why you need it.

---

# 15. Properties

## Q98. What is `@property`?

It allows a method to be accessed like an attribute.

```python
class Student:

    @property
    def name(self):
        return self._name
```

---

## Q99. Why use properties?

* Encapsulation
* Validation
* Controlled access
* Cleaner API

---

## Q100. What is a setter?

```python
@name.setter
def name(self, value):
    self._name = value
```

---

## Q101. What is a getter?

A property method used to retrieve a value.

---

## Q102. Why use `@property` instead of normal getter methods?

It allows an API like:

```python
student.name
```

instead of:

```python
student.get_name()
```

while still allowing logic behind the scenes.

---

# 16. Magic/Dunder Methods

## Q103. What are magic methods?

Special methods with double underscores.

Examples:

```python
__init__
__str__
__repr__
__len__
__add__
__eq__
```

---

## Q104. What is `__str__()`?

Defines the user-friendly string representation of an object.

---

## Q105. What is `__repr__()`?

Defines a representation intended to be useful for developers/debugging.

---

## Q106. `__str__()` vs `__repr__()`?

| `__str__`                     | `__repr__`                                   |
| ----------------------------- | -------------------------------------------- |
| User-friendly representation  | Developer-oriented representation            |
| Used by `str()` and `print()` | Used by `repr()`                             |
| Focuses on readability        | Focuses on useful/unambiguous representation |

---

## Q107. What is `__len__()`?

Defines behavior for:

```python
len(object)
```

---

## Q108. What is `__add__()`?

Defines behavior for:

```python
object1 + object2
```

---

## Q109. What is `__eq__()`?

Defines equality comparison:

```python
object1 == object2
```

---

## Q110. What is `__new__()`?

`__new__()` is responsible for creating/returning a new instance before `__init__()` initializes it.

It is particularly relevant for immutable types and advanced object creation.

---

# 17. Composition and Aggregation

## Q111. What is composition?

Composition is a strong HAS-A relationship where one object contains another object.

```text
Car HAS-A Engine
```

---

## Q112. What is aggregation?

Aggregation is a weaker HAS-A relationship where the contained object can exist independently.

---

## Q113. Composition vs inheritance?

```text
Inheritance → IS-A

Composition → HAS-A
```

---

## Q114. Why is composition often preferred over deep inheritance?

Composition can provide:

* Lower coupling
* Greater flexibility
* Easier replacement of components
* Simpler class hierarchies

---

# 18. Duck Typing

## Q115. What is duck typing?

Duck typing means an object's suitability is determined by whether it supports the required operations rather than by its exact type.

---

## Q116. Give an example of duck typing.

```python
class Dog:

    def speak(self):
        print("Bark")


class Person:

    def speak(self):
        print("Hello")


def speak(obj):
    obj.speak()
```

Both can be passed:

```python
speak(Dog())
speak(Person())
```

---

## Q117. Is duck typing compile-time or runtime behavior?

It is associated with Python's dynamic/runtime behavior.

---

# 19. OOP Design Questions

## Q118. What is an IS-A relationship?

Inheritance.

```text
Dog IS-A Animal
```

---

## Q119. What is a HAS-A relationship?

Composition/aggregation.

```text
Car HAS-A Engine
```

---

## Q120. When should you use inheritance?

Use it when there is a meaningful subtype relationship and the child genuinely represents a specialized form of the parent.

---

## Q121. When should you use composition?

Use composition when one object contains or uses another object and you want flexible collaboration between components.

---

## Q122. What is loose coupling?

Classes have minimal dependency on each other's internal implementation.

---

## Q123. What is tight coupling?

Classes depend heavily on each other's implementation details.

---

## Q124. Why is loose coupling preferred?

It improves:

* Maintainability
* Testing
* Flexibility
* Reusability

---

# 20. Python-Specific OOP Questions

## Q125. Is everything an object in Python?

Almost everything you interact with in Python is an object, including:

* Numbers
* Strings
* Functions
* Classes
* Modules
* Instances

---

## Q126. Are classes themselves objects?

Yes.

Classes are objects created by a metaclass, normally `type`.

---

## Q127. What is `type`?

`type` is the default metaclass used to create classes.

Example:

```python
class Student:
    pass

print(type(Student))
```

Typically:

```text
<class 'type'>
```

---

## Q128. What is `isinstance()`?

Checks whether an object is an instance of a class or its subclasses.

```python
isinstance(obj, ClassName)
```

---

## Q129. What is `issubclass()`?

Checks whether one class is a subclass of another.

```python
issubclass(Child, Parent)
```

---

## Q130. `isinstance()` vs `type()`?

```python
type(obj)
```

checks the object's exact type.

```python
isinstance(obj, Class)
```

also considers inheritance.

---

## Q131. What is dynamic typing?

Python determines types at runtime.

```python
x = 10
x = "Hello"
```

The same variable name can refer to objects of different types at different times.

---

## Q132. Does Python support multiple inheritance?

Yes.

---

## Q133. Does Python support interfaces?

Python does not have Java-style interfaces as a separate language construct.

Common approaches include:

* Abstract Base Classes
* Protocols
* Duck typing

---

## Q134. What is an ABC?

ABC means:

**Abstract Base Class**

Python provides it through the `abc` module.

---

# 21. Output-Based Questions

These are commonly useful for interview practice.

---

## Q135. What is the output?

```python
class Student:

    college = "ABC"


s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)
```

### Answer

```text
ABC
ABC
```

---

## Q136. What is the output?

```python
class Student:

    college = "ABC"


s1 = Student()

s1.college = "XYZ"

print(s1.college)
print(Student.college)
```

### Answer

```text
XYZ
ABC
```

### Why?

`s1.college = "XYZ"` creates an instance attribute that shadows the class attribute for `s1`.

---

## Q137. What is the output?

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


obj = B()

obj.show()
```

### Answer

```text
B
```

The child method overrides the parent method.

---

## Q138. What is the output?

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


B().show()
```

### Answer

```text
A
B
```

---

## Q139. What is the output?

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


s = Student("Rahul")

s.display()
```

### Answer

```text
Rahul
```

---

## Q140. What is the output?

```python
class Test:

    def __init__(self):
        print("Constructor")


obj = Test()
```

### Answer

```text
Constructor
```

`__init__()` runs during object initialization.

---

# 22. Coding Interview Questions

These are questions you should practice by actually writing code.

---

## Beginner

### Q141. Create a `Student` class with:

* Name
* Roll number
* Marks
* Display method

---

### Q142. Create an `Employee` class with:

* Name
* Salary
* Department

Display all information.

---

### Q143. Create a `Rectangle` class.

Calculate:

* Area
* Perimeter

---

### Q144. Create a `BankAccount` class.

Implement:

* Deposit
* Withdraw
* Balance

---

### Q145. Create a `Car` class.

Implement:

* Start
* Stop
* Display details

---

## Encapsulation Questions

### Q146. Create a bank account using a private balance.

Requirements:

* `deposit()`
* `withdraw()`
* `get_balance()`

---

### Q147. Create a student class where marks cannot be outside:

```text
0 to 100
```

Use encapsulation.

---

### Q148. Create an employee class with private salary.

Implement a setter that rejects negative salary.

---

## Abstraction Questions

### Q149. Create an abstract `Vehicle` class.

Abstract method:

```python
start()
```

Implement:

* Car
* Bike

---

### Q150. Create an abstract `Shape` class.

Abstract method:

```python
area()
```

Implement:

* Circle
* Rectangle
* Triangle

---

### Q151. Create an abstract `Payment` class.

Implement:

* CreditCardPayment
* UPIPayment
* CashPayment

Each should implement:

```python
pay()
```

---

## Inheritance Questions

### Q152. Create:

```text
Animal
   ↓
Dog
```

Add appropriate methods.

---

### Q153. Create:

```text
Vehicle
   ↓
Car
   ↓
ElectricCar
```

Demonstrate multilevel inheritance.

---

### Q154. Demonstrate multiple inheritance using:

```text
Father
Mother
   ↓
Child
```

---

### Q155. Demonstrate hierarchical inheritance:

```text
Animal
 /   \
Dog  Cat
```

---

## Polymorphism Questions

### Q156. Create `Dog` and `Cat` classes.

Both should implement:

```python
sound()
```

Call the method polymorphically.

---

### Q157. Create different payment classes.

Each should implement:

```python
pay()
```

Process all payments using one loop.

---

### Q158. Demonstrate operator overloading using `__add__()`.

---

### Q159. Demonstrate `__eq__()` with custom objects.

---

### Q160. Demonstrate duck typing with two unrelated classes.

---

# 23. Tricky Questions

These are particularly useful for interviews.

---

## Q161. Is Python purely object-oriented?

Python is strongly object-oriented and treats most entities as objects, but it also supports procedural and functional programming styles.

---

## Q162. Is `self` a keyword?

No.

It is the conventional name for the instance parameter.

---

## Q163. Can we create an object without calling `__init__()`?

Object creation and initialization are separate mechanisms.

Advanced object creation can involve `__new__()` directly.

---

## Q164. Can we have private methods?

Yes, using the double-underscore convention/name mangling:

```python
def __calculate(self):
    pass
```

But this is not strict security.

---

## Q165. Can a child class access a private parent attribute?

Not directly through the original double-underscore name because of name mangling.

---

## Q166. Can a child class override a private method?

A double-underscore method is name-mangled based on the defining class, so a child method with the same source-level name is generally a different attribute.

This differs from normal overriding.

---

## Q167. Can constructors be inherited?

A child class inherits the parent's `__init__()` if it does not define its own initializer.

---

## Q168. If a child defines `__init__()`, does the parent constructor automatically run?

No.

You generally need:

```python
super().__init__()
```

if you want the parent initialization to execute.

---

## Q169. Can a class inherit from itself?

No.

Circular inheritance is invalid.

---

## Q170. Can a class inherit from multiple classes?

Yes.

```python
class C(A, B):
    pass
```

---

## Q171. Can an object belong to multiple classes?

An object has one concrete class/type, but because of inheritance it can satisfy `isinstance()` checks for multiple classes in its hierarchy.

---

## Q172. Can we dynamically add attributes to an object?

Usually yes, for normal Python objects that have a `__dict__`.

```python
obj.age = 20
```

Classes using `__slots__` can restrict this behavior.

---

## Q173. What is `__slots__`?

`__slots__` can restrict which instance attributes are allowed and can reduce per-instance memory overhead in suitable cases.

Example:

```python
class Student:

    __slots__ = ("name", "age")
```

---

## Q174. What is object identity?

Identity tells whether two references refer to the same object.

Use:

```python
is
```

---

## Q175. `is` vs `==`?

```text
is  → identity
==  → equality/value comparison
```

Example:

```python
a is b
```

checks whether they are the same object.

```python
a == b
```

checks whether they compare equal.

---

## Q176. What is shallow copy?

A shallow copy creates a new outer object but may share references to nested objects.

---

## Q177. What is deep copy?

A deep copy recursively copies nested objects.

Python provides:

```python
import copy

copy.copy()
copy.deepcopy()
```

---

# 24. Rapid-Fire Questions

Use these for quick revision before an interview.

### Q178. What does OOP stand for?

Object-Oriented Programming.

### Q179. What is a class?

Blueprint for objects.

### Q180. What is an object?

Instance of a class.

### Q181. What is `self`?

Current object reference.

### Q182. What is `cls`?

Class reference commonly used in class methods.

### Q183. What is `__init__()`?

Object initializer.

### Q184. What is encapsulation?

Bundling and controlled access to data/state.

### Q185. What is abstraction?

Hiding implementation details.

### Q186. What is inheritance?

Acquiring/extending behavior from another class.

### Q187. What is polymorphism?

One interface/common operation with different behavior.

### Q188. What is method overriding?

Child replaces/specializes inherited method behavior.

### Q189. Does Python support traditional method overloading?

No.

### Q190. What is `super()`?

Accesses the next class in the MRO.

### Q191. What is MRO?

Method Resolution Order.

### Q192. What is multiple inheritance?

One class inherits from multiple classes.

### Q193. What is name mangling?

Transformation of double-underscore attribute names.

### Q194. What is `_variable`?

Protected/internal-use convention.

### Q195. What is `__variable`?

Private-style attribute using name mangling.

### Q196. What is `@property`?

Creates attribute-style access to a method.

### Q197. What is ABC?

Abstract Base Class.

### Q198. What is `@abstractmethod`?

Marks a method as abstract.

### Q199. What is duck typing?

Behavior-based typing.

### Q200. What is operator overloading?

Defining operator behavior for custom objects.

### Q201. What is composition?

HAS-A relationship.

### Q202. What is inheritance relationship?

IS-A relationship.

### Q203. What is `__str__()`?

User-friendly string representation.

### Q204. What is `__repr__()`?

Developer-oriented representation.

### Q205. What is `__new__()`?

Creates/returns a new instance before initialization.

### Q206. What is `__slots__`?

Restricts instance attributes and can reduce memory overhead.

---

# 25. Most Important Questions

> "Explain OOP concepts in Python."

You should be able to explain.

```text
1. What is OOP?
2. What is a class?
3. What is an object?
4. What is self?
5. What is __init__()?
6. What are the four pillars?
7. What is encapsulation?
8. What is abstraction?
9. What is inheritance?
10. What is polymorphism?
11. Encapsulation vs abstraction
12. Method overriding
13. Method overloading
14. super()
15. Types of inheritance
16. Multiple inheritance
17. MRO
18. Diamond problem
19. Public/protected/private
20. Name mangling
21. Getter/setter
22. @property
23. Abstract class
24. Abstract method
25. Duck typing
26. Operator overloading
27. Composition
28. Aggregation
29. IS-A vs HAS-A
30. Magic methods
```

---

# Questions You MUST Know

For a fresher/entry-level Python placement interview, make sure you can answer these clearly:

### 1. What is OOP?

### 2. What are the four pillars of OOP?

### 3. Explain encapsulation with a Python example.

### 4. Explain abstraction with an abstract class.

### 5. Explain inheritance and its types.

### 6. Explain polymorphism with an example.

### 7. What is method overriding?

### 8. Does Python support method overloading?

### 9. What is the difference between abstraction and encapsulation?

### 10. What is the difference between inheritance and composition?

### 11. What is `super()`?

### 12. What is MRO?

### 13. Explain public, protected and private members in Python.

### 14. What are `@classmethod` and `@staticmethod`?

### 15. Explain duck typing in Python.

---

# Python OOPs —  Syntax & Coding Examples



# 1. What is OOP?

OOP stands for:

> **Object-Oriented Programming**

It is a programming approach based on **classes and objects**.

The four major pillars are:

```text
Encapsulation
Abstraction
Inheritance
Polymorphism
```

---

# 2. Basic Class Syntax

## Syntax

```python
class ClassName:

    # variables
    # methods
    pass
```

Example:

```python
class Student:

    name = "Rahul"
    age = 20
```

---

# 3. Creating Objects

## Syntax

```python
object_name = ClassName()
```

Example:

```python
class Student:
    pass


s1 = Student()
s2 = Student()
```

Here:

```text
Student → Class
s1      → Object
s2      → Object
```

---

# 4. Constructor

Python commonly uses `__init__()` to initialize an object.

## Syntax

```python
class ClassName:

    def __init__(self, parameters):
        self.variable = parameters
```

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Rahul", 20)

print(s1.name)
print(s1.age)
```

Output:

```text
Rahul
20
```

---

# 5. self

`self` refers to the current object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


s1 = Student("Rahul")

s1.display()
```

When:

```python
s1.display()
```

Python effectively passes `s1` as the instance to the method.

---

# 6. Instance Variables

Instance variables belong to individual objects.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create objects:

```python
s1 = Student("Rahul", 20)
s2 = Student("Anu", 21)
```

Now:

```python
print(s1.name)
print(s2.name)
```

Output:

```text
Rahul
Anu
```

Each object has its own instance data.

---

# 7. Instance Methods

An instance method normally receives `self`.

## Syntax

```python
class ClassName:

    def method_name(self):
        # code
        pass
```

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


s = Student("Rahul")

s.display()
```

---

# 8. Class Variables

A class variable is defined inside the class but outside instance methods.

```python
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name
```

Usage:

```python
s1 = Student("Rahul")
s2 = Student("Anu")

print(s1.college)
print(s2.college)
```

Both can access the class variable.

---

# 9. Class Methods

Class methods use:

```python
@classmethod
```

and normally receive `cls`.

## Syntax

```python
class ClassName:

    @classmethod
    def method_name(cls):
        pass
```

Example:

```python
class Student:

    college = "ABC College"

    @classmethod
    def change_college(cls, name):
        cls.college = name


Student.change_college("XYZ College")

print(Student.college)
```

---

# 10. Static Methods

Static methods use:

```python
@staticmethod
```

They do not automatically receive `self` or `cls`.

## Syntax

```python
class ClassName:

    @staticmethod
    def method_name(parameters):
        pass
```

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

Output:

```text
30
```

---

# 11. Encapsulation

Encapsulation means:

> Bundling data and methods together while controlling access to internal state.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())
```

Output:

```text
1500
```

---

# 12. Public Variables

Normal attributes are public by convention.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Access:

```python
s = Student("Rahul")

print(s.name)
```

---

# 13. Protected Variables

A single underscore is used as a convention.

```python
class Student:

    def __init__(self, marks):
        self._marks = marks
```

Access:

```python
s = Student(90)

print(s._marks)
```

Python does not strictly prevent this.

---

# 14. Private Variables

Double underscore triggers name mangling.

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks
```

Normally:

```python
s = Student(90)

print(s.__marks)
```

will fail because the attribute is name-mangled.

---

# 15. Getters and Setters

## Getter

Used to retrieve data.

```python
def get_marks(self):
    return self.__marks
```

## Setter

Used to modify data.

```python
def set_marks(self, marks):
    self.__marks = marks
```

Complete example:

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


s = Student(80)

print(s.get_marks())

s.set_marks(90)

print(s.get_marks())
```

---

# 16. Property Decorator

`@property` allows a method to behave like an attribute.

```python
class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")
```

Usage:

```python
s = Student(80)

print(s.marks)

s.marks = 90
```

---

# 17. Abstraction

Abstraction means:

> Hide implementation details and expose only necessary functionality.

Python commonly implements abstraction using the `abc` module.

```python
from abc import ABC, abstractmethod
```

---

# 18. Abstract Classes

Syntax:

```python
from abc import ABC, abstractmethod


class ClassName(ABC):

    @abstractmethod
    def method(self):
        pass
```

Example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

# 19. Abstract Methods

An abstract method is declared using:

```python
@abstractmethod
```

Example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts")


class Bike(Vehicle):

    def start(self):
        print("Bike starts")
```

Usage:

```python
car = Car()
bike = Bike()

car.start()
bike.start()
```

Output:

```text
Car starts
Bike starts
```

---

# 20. Inheritance

Inheritance allows a child class to reuse or extend a parent class.

## Basic syntax

```python
class Parent:
    pass


class Child(Parent):
    pass
```

Example:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

---

# 21. Single Inheritance

One parent → one child.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")
```

---

# 22. Multilevel Inheritance

Example:

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

Code:

```python
class Grandparent:

    def house(self):
        print("House")


class Parent(Grandparent):

    def car(self):
        print("Car")


class Child(Parent):

    def bike(self):
        print("Bike")


c = Child()

c.house()
c.car()
c.bike()
```

---

# 23. Multiple Inheritance

One child → multiple parents.

```python
class Father:

    def skills(self):
        print("Driving")


class Mother:

    def hobbies(self):
        print("Painting")


class Child(Father, Mother):
    pass


c = Child()

c.skills()
c.hobbies()
```

---

# 24. Hierarchical Inheritance

One parent → multiple children.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")
```

---

# 25. Hybrid Inheritance

Hybrid inheritance is a combination of inheritance types.

Example:

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

This also introduces the diamond inheritance structure.

---

# 26. `super()`

`super()` is used to access behavior from the next class in the MRO.

## Parent constructor

```python
class Parent:

    def __init__(self):
        print("Parent")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child")


c = Child()
```

Output:

```text
Parent
Child
```

---

## Parent method

```python
class Parent:

    def display(self):
        print("Parent")


class Child(Parent):

    def display(self):

        super().display()

        print("Child")


c = Child()

c.display()
```

---

# 27. Method Overriding

A child class provides its own implementation of a parent method.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()
```

Output:

```text
Bark
```

---

# 28. Method Overloading

Python does not support traditional method overloading based only on different parameter lists.

This:

```python
class Calculator:

    def add(self, a):
        return a

    def add(self, a, b):
        return a + b
```

does **not** create two overloads.

The second definition replaces the first.

---

## Using Default Arguments

```python
class Calculator:

    def add(self, a, b=0):
        return a + b


c = Calculator()

print(c.add(10))
print(c.add(10, 20))
```

---

## Using `*args`

```python
class Calculator:

    def add(self, *numbers):
        return sum(numbers)


c = Calculator()

print(c.add(10))
print(c.add(10, 20))
print(c.add(10, 20, 30))
```

---

# 29. Polymorphism

Polymorphism means:

> Same interface → different behavior.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

---

# 30. Duck Typing

Python cares about supported behavior rather than requiring an exact type.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


def make_sound(animal):

    animal.sound()


make_sound(Dog())
make_sound(Cat())
```

---

# 31. Operator Overloading

Operator overloading allows custom objects to define operator behavior.

Important methods:

```text
__add__()   +
__sub__()   -
__mul__()   *
__truediv__() /
__eq__()    ==
__lt__()    <
__gt__()    >
```

Example:

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


a = Number(10)
b = Number(20)

print(a + b)
```

Output:

```text
30
```

---

# 32. Magic/Dunder Methods

Magic methods have double underscores.

Common methods:

```text
__init__()
__str__()
__repr__()
__len__()
__add__()
__sub__()
__eq__()
__lt__()
__gt__()
__new__()
```

---

## `__str__()`

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


s = Student("Rahul")

print(s)
```

---

## `__len__()`

```python
class Team:

    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team(["A", "B", "C"])

print(len(team))
```

Output:

```text
3
```

---

## `__eq__()`

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

---

# 33. Composition

Composition represents a strong HAS-A relationship.

Example:

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()

car.start()
```

Relationship:

```text
Car HAS-A Engine
```

---

# 34. Aggregation

Aggregation is also a HAS-A relationship, but the contained object can exist independently.

```python
class Teacher:

    def teach(self):
        print("Teaching")


class School:

    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher()

school = School(teacher)

school.teacher.teach()
```

---

# 35. MRO

MRO = **Method Resolution Order**

It determines the order in which Python searches classes.

Example:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

You can also use:

```python
print(C.__mro__)
```

Python uses **C3 linearization** for class MRO.

---

# 36. isinstance()

Checks whether an object is an instance of a class or its subclasses.

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output:

```text
True
True
```

---

# 37. issubclass()

Checks whether a class is derived from another class.

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
```

Output:

```text
True
```

---

# 38. `is` vs `==`

## `==`

Checks equality.

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

Output:

```text
True
```

## `is`

Checks object identity.

```python
print(a is b)
```

Usually:

```text
False
```

because `a` and `b` are different list objects.

---

# 39. `__new__()`

`__new__()` is responsible for creating/returning a new instance.

Example:

```python
class Student:

    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")


s = Student()
```

Output:

```text
Creating object
Initializing object
```

Order:

```text
__new__()
   ↓
__init__()
```

---

# 40. `__slots__`

`__slots__` can restrict allowed instance attributes.

```python
class Student:

    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This allows:

```python
s = Student("Rahul", 20)

print(s.name)
```

but arbitrary new attributes such as:

```python
s.marks = 90
```

are generally not allowed unless `marks` is included in `__slots__`.

---

# 41. OOP Examples

# Example 1 — Student Management

```python
class Student:

    college = "ABC College"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("College:", self.college)


s1 = Student("Rahul", 101, 85)

s1.display()
```

---

# Example 2 — Bank Account

```python
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Amount deposited")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 5000)

account.deposit(1000)

account.withdraw(2000)

print(account.get_balance())
```

Concepts:

```text
Class
Object
Constructor
Encapsulation
Private variable
Methods
```

---

# Example 3 — Employee

```python
class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)


e1 = Employee("Rahul", 40000)

e1.display()
```

---

# Example 4 — Rectangle

```python
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())
```

---

# Example 5 — Calculator

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):

        if b != 0:
            return a / b

        return "Cannot divide by zero"


c = Calculator()

print(c.add(10, 20))
print(c.subtract(20, 10))
print(c.multiply(5, 4))
print(c.divide(20, 5))
```

---

# Example 6 — Encapsulation

```python
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")


e = Employee(30000)

print(e.get_salary())

e.set_salary(40000)

print(e.get_salary())
```

---

# Example 7 — Abstraction

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


p1 = CreditCard()
p2 = UPI()

p1.pay(1000)
p2.pay(500)
```

---

# Example 8 — Inheritance

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

---

# Example 9 — Multilevel Inheritance

```python
class Vehicle:

    def start(self):
        print("Vehicle starts")


class Car(Vehicle):

    def drive(self):
        print("Car drives")


class ElectricCar(Car):

    def charge(self):
        print("Charging")


car = ElectricCar()

car.start()
car.drive()
car.charge()
```

---

# Example 10 — Multiple Inheritance

```python
class Father:

    def father_skill(self):
        print("Driving")


class Mother:

    def mother_skill(self):
        print("Cooking")


class Child(Father, Mother):

    def child_skill(self):
        print("Gaming")


c = Child()

c.father_skill()
c.mother_skill()
c.child_skill()
```

---

# Example 11 — Method Overriding

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


Dog().sound()
Cat().sound()
```

---

# Example 12 — Polymorphism

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

---

# Example 13 — Operator Overloading

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print(self.value)


a = Number(10)
b = Number(20)

c = a + b

c.display()
```

---

# Example 14 — Composition

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()

car.start()
```

---

# Example 15 — Property

```python
class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")


s = Student(80)

print(s.marks)

s.marks = 95

print(s.marks)
```

---


# 42. Quick Syntax Cheat Sheet

## Class

```python
class Student:
    pass
```

## Object

```python
s = Student()
```

## Constructor

```python
def __init__(self):
    pass
```

## Instance Variable

```python
self.name = name
```

## Instance Method

```python
def display(self):
    pass
```

## Class Variable

```python
class Student:

    college = "ABC"
```

## Class Method

```python
@classmethod
def method(cls):
    pass
```

## Static Method

```python
@staticmethod
def method():
    pass
```

## Inheritance

```python
class Child(Parent):
    pass
```

## Multiple Inheritance

```python
class Child(Parent1, Parent2):
    pass
```

## Private Variable

```python
self.__data
```

## Protected Convention

```python
self._data
```

## Property

```python
@property
def data(self):
    return self._data
```

## Setter

```python
@data.setter
def data(self, value):
    self._data = value
```

## Abstract Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    pass
```

## Abstract Method

```python
@abstractmethod
def sound(self):
    pass
```

## Parent Method

```python
super().method()
```

## Parent Constructor

```python
super().__init__()
```

## Method Overriding

```python
class Child(Parent):

    def method(self):
        pass
```

## Operator Overloading

```python
def __add__(self, other):
    pass
```

## String Representation

```python
def __str__(self):
    return "text"
```

## Object Type

```python
type(obj)
```

## Instance Check

```python
isinstance(obj, ClassName)
```

## Subclass Check

```python
issubclass(Child, Parent)
```

## MRO

```python
ClassName.mro()
```

---

# Four Pillars — Syntax 

## Encapsulation

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks
```

---

## Abstraction

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Inheritance

```python
class Parent:

    def display(self):
        print("Parent")


class Child(Parent):
    pass
```

---

## Polymorphism

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

---

