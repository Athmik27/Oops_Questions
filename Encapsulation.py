# Create a class BankAccount
# A private variable __balance
# A constructor that initializes the balance
# A method deposit(amount) to add money
# A method withdraw(amount) to deduct money
# A method get_balance() to display the current balance
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
        

#     def Deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             return self.__balance

#     def Withdraw(self,amount):
#         if self.amount > 0 and self.amount <= self.__balance:
#             self.__balance-=self.amount
#             return self.__balance
# bank_account=(BankAccount(1000))
# print(bank_account.Deposit(500))
# print(bank_account.Withdraw(500))

#Create a class Student
# Create a private variable __marks.
# Initialize it using __init__().
# Create a method set_marks(marks) to update the marks.
# Marks must be between 0 and 100.
# If the marks are invalid, print:marks invalid
# Create a method get_marks() to return the marks.
# Create an object with initial marks 75.
# Change the marks to 90 and display them

class Student:
    def __init__(self,marks):
        self.__marks=marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks
student=Student(50)
print(student.get_marks())
student.set_marks(95)
print(student.get_marks())
        



        
