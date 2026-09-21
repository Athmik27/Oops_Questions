#Create a parent class Animal:
# Create a method sound()
# It should print "Animal makes a sound"
# Create two child classes:
# Dog(Animal)
# Override sound()
# Print "Dog barks"
# Cat(Animal)
# Override sound()
# Print "Cat meows"
# Create one object of Dog and one object of Cat.
# Call sound() for both objects.
class Animal:
    def method_sound(self):
        print("Animal makes an sound")

class Dog(Animal):
    def method_sound(self):
        print("Barks")

class Cat(Animal):
    def method_sound(self):
        print("Meow")

dog=Dog()
dog.method_sound()

cat=Cat()
cat.method_sound()


# Create a parent class Animal:
# Create a method sound()
# Print "Animalsound"
# Create two child classes:
# Dog(Animal)
# Override sound()
# Print "Dog barks"
# Cat(Animal)
# Override sound()
# Print "Cat meows"
# Create a function make_sound(animal):
# Accept an animal object as an argument
# Call its sound() method
# Create objects of Dog and Cat.
# Pass both objects to make_sound().
# class Animal:
#     def Sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     def Sound(self) :
#         print("Bark") 

# class Cat(Animal):
#     def Sound(self):
#         print("Meow")

# def make_sound(animal):
#         animal.Sound()

# dog=Dog()
# dog.Sound()

# cat=Cat()
# cat.Sound()

# Create a class Duck:
# Create a method speak()
# It should print "Duck says Quack"
# Create another class Person:
# Create a method speak()
# It should print "Person says Hello"
# Create a function make_speak(obj):
# Accept an object as an argument
# Call its speak() method
# Create one object of Duck and one object of Person.
# Pass both objects to make_speak(). 
# Duck and Person should not inherit from each other.
# This question is specifically testing duck typing.
# class Duck:
#      def speak(self):
#           print("duck says quack")

# class Person:
#      def speak(self):
#           print("person says hello")

# def make_speak(obj):
#      obj.speak() # duck typing is an concept which determines objects behaviour based on the method and attributes


# duck=Duck()
# person=Person()

# duck.speak()
# person.speak()

# operator overloading
# Create a class Number:
# __init__() should accept a number
# Store it in self.value
# Implement __add__() to add two Number objects
# # Return the result as a Number object
# class Number:
#     def __init__(self,number):
#           self.number=number

#     def __add__(self,value):
#          return Number(self.number+value.number)

# num1=Number(10)
# num2=Number(20)

# result=num1+num2

# print(result.number)

# Create a class Student:
# __init__() should accept marks
# Store it in self.marks
# Implement __gt__() to compare the marks of two Student objects
# Return True if the first student's marks are greater than the second student's marks
# class Student:
#     def __init__(self,marks):
#         self.marks=marks

#     def __gt__(self,other):
#         return self.marks>other.marks

# student1=Student(85)
# student2=Student(90)

# print(student1>student2)

# Create a class Calculator:
# Create a method add()
# It should be able to add two or three numbers
# If two numbers are provided, return their sum
# If three numbers are provided, return the sum of all three
# Use default arguments to achieve this
# Create a Calculator object and test:
# class Calculator:

#     def add(self,a,b,c=0):
#         return a+b+c

# calculator=Calculator()
# print(calculator.add(10,20))   
# print(calculator.add(10,20,30))

# Create a class Calculator:
# Create a method add()
# It should accept any number of numbers
# Use *args
# Return the sum of all the numbers
# class Calculator:

#     def add(self,*args):
#         return sum(args)
    
# calculator=Calculator()
# print(calculator.add(10,20))
# print(calculator.add(10,20,30))


# Create a class Rectangle:
# __init__() should accept length and width
# Create a method area()
# Return length × width
# Create another class Circle:
# __init__() should accept radius
# Create a method area()
# Return π × radius²
# Create a function calculate_area(shape):
# Accept a shape object
# Call its area() method
# Print the returned area
import math #for value of pi
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius**2
circle=Circle(5)
print(circle.area())

rectangle=Rectangle(5,5)
print(rectangle.area())

        


    
