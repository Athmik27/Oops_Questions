#Create a parent class called Person.
# It should have:
# An __init__() method that accepts name
# A method display_name() that prints the name
# Then create a child class called Student that inherits from Person.
# Student should have:
# An __init__() method that accepts name and course
# A method display_course() that prints the course
class Person:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print("The name of the student is:",self.name)
        
class Student(Person):
    def __init__(self,name,course):
            self.name=name
            self.course=course
    def display_course(self):
        print("The course selected by an student is:",self.course)
person=Person("Athmik")
person.display_name()
student = Student("Athmik", "Python")
student.display_course()

# Create a parent class Person:
# __init__() should accept name
# Store it in self.name
# Create a method display_name()
# Create a child class Student(Person):
# __init__() should accept name and course
# Use super() to initialize name
# Store course in self.course
# Create display_course()
class Person():
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print("the name of an student is :",self.name)
class Student(Person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course
    def display_course(self):
        print("the course selected by the student is :",self.course)
person=Person("Athmik")
person.display_name()
student=Student("Athmik","Python")
student.display_course()

#Method Overriding
class Animal:
    def sound(self):
        print("Bark")
class Dog(Animal):
    def sound(self):
        print('Dog Barks')
dog=Dog()
dog.sound()

# Multiple Inheritance
# Create a parent class Father:
# Create a method father_skill()
# It should print "Father: Driving"
# Create another parent class Mother:
# Create a method mother_skill()
# It should print "Mother: Cooking"
# Create a child class Child:
# Inherit from both Father and Mother
# Do not create any additional methods
class Father:
    def father_skill(self):
        print("Skill of an Father is Driving the Car")
class Mother:
    def mother_skill(self):
        print('Mothers skill is Cooking')
class Child(Father,Mother):
    pass
child=Child()
child.father_skill()
child.mother_skill()

# Multilevel Inhertance
# Create a parent class Grandparent:
# Create a method grandparent_method()
# It should print "Grandparent method"
# Create a child class Parent(Grandparent):
# Create a method parent_method()
# It should print "Parent method"
# Create another child class Child(Parent):
# Create a method child_method()
# It should print "Child method"
# Create an object of Child.
# Call all three methods using the Child object.
class GrandParent:
    def grandparent_method(self):
        print("GrandParent Method")

class Parent(GrandParent):
        def parent_method(self):
             print("Parent Method")

class Child(Parent):
     def child_method(self):
          print("child method")
child=Child()
child.grandparent_method()
child.parent_method()

#Heirarchial inheritance
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")
car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()



# Create a parent class Employee:
# __init__() should accept name and salary
# Store them in self.name and self.salary
# Create a method display_employee() that prints the employee's name and salary
# Create a child class Manager(Employee):
# __init__() should accept name, salary, and department
# Use super() to initialize name and salary
# Store department in self.department
# Create a method display_manager() that prints the department

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_employee(self):
        print("name of an employee:",self.name)
        print("salary of an employee:",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display_manager(self):
        print("department of an employee:",self.department) 

manager=Manager("Athmik",1000,"Finance")
manager.display_employee()

# Create a parent class Employee:
# Create a method calculate_bonus()
# It should return 5000
# Create a child class Manager(Employee):
# Override the calculate_bonus() method
# It should return 10000
# Create an object of Manager.
# Call calculate_bonus() and print the returned value.
class Employee:
    def calculate_bonus(self):
        return 5000

class Manager(Employee):
    def calculate_bonus(self):
        return 10000

manager = Manager()
print(manager.calculate_bonus())


#Inheritance and Encapsulation
# Create a parent class BankAccount:
# __init__() should accept balance
# Store the balance in a private variable __balance
# Create a method get_balance() that returns the balance
# Create a child class SavingsAccount(BankAccount):
# __init__() should accept balance and interest
# Use super() to initialize balance
# Store interest in self.interest
# Create a method calculate_interest() that returns the interest amount

class BankAccount:

    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):

    def __init__(self,balance,interest):
        super().__init__(balance)
        self.interest=interest

    def calculate_interest(self):
        return  self.interest * self.get_balance() / 100
    
savings_account=SavingsAccount(10000,5)
print(savings_account.get_balance())
print(savings_account.calculate_interest())

