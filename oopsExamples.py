#Bank Account Prgm          ex for encapsulation
# class BankAccount:
#     def __init__(self, account_number,balance):
#         self.account_number = account_number
#         self.__balance = balance
#     def deposit(self, amount): # 40000
#         self.__balance += amount
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds!")
#
#     def get_balance(self):  # Public method to access private variable # Getter Method..
#         return self.__balance

# Creating an object
# account1 = BankAccount("123456", 5000)
# account2 = BankAccount("345644",10000)
#
# account1.deposit(5000)
# account1.withdraw(1000)
# print("Account 1 Balance is:",account1.get_balance())
#
# account2.deposit(5000)
# account2.withdraw(1000)
# print("Account 2 Balance is:",account2.get_balance())

#2. Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1= Person("Raju", 20)
# p2= Person("Martin", 25)
#
# print(p1.name)
# print(p1.age)

#-----------------------------------------------------------------------
#Getter and Setter Method
# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def getName(self):
#         return self.__name
#     def getAge(self):
#         return self.__age
#     def setAge(self, new_age):
#         if new_age > 0 :
#             self.__age = new_age
#         else:
#             print("Invalid age")
#
# student = Student("John", 25)
# print(student.getName())
# print(student.getAge())
#
# student.setAge(24)
# print(student.getAge())
# student.setAge(-10)
# print(student.getAge())

#1 Single inheritance
# super() is built-in function. Used to call a method from PC inside the CC.It is used inside
#the _init_ to initialize the PC attributes when we extend functionality in CC.

# class Employee:
#     def __init__(self, name, emp_id):
#         self.name = name
#         self.emp_id = emp_id
#
#     def show_details(self):
#         print(f"Name: {self.name} | ID: {self.emp_id}  ")
#
# class Developer(Employee):
#     def __init__(self, name, emp_id, language):
#         super().__init__(name, emp_id)
#         self.language = language
#
#     def show_role(self):
#         print(f"Role: Backend Dev | Language: {self.language}  ")
#
# engg = Developer("Jyoti", "12345", "Python")
# engg.show_details()
# engg.show_role()

# Multiple Inheritance
# class Camera: #Parent A
#     def take_picture(self):
#         print("Picture taken with 100 MP camera")
#
# class Phone: # Parent B
#     def make_call(self, number):
#         print("Calling the number")
#
# class SmartPhone(Camera, Phone): # Child class
#     def browse_internet(self):
#         print("Browsing Internet")
#
# a = SmartPhone()
# a.take_picture()
# a.make_call("000000000")
# a.browse_internet()

#3. Multilevel Inheritance
# Scenario: Vehicle, car, electric car

# class Vehicle:
#     def move(self):
#         print("Vehicle can move")
#
# class Car(Vehicle):
#     def fuel(self):
#         print("Car uses Petrol")
#
# class ElectricCar(Car):#Multilevel
#     def battery(self):
#         print("Electric car uses battery")
#
# skoda = ElectricCar()
# skoda.move()
# skoda.fuel()
# skoda.battery()

#4. Hierarchical Inheritance and hybrid
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print("Person name",self.name)
#
# class Student(Person):
#     def __init__(self, name, roll_no):
#         Person.__init__(self,name)
#         self.roll_no = roll_no
#     def display(self):
#         print("Student name",self.name,"roll no",self.roll_no)
#
# class Employee(Person):
#     def __init__(self, name, emp_id):
#         Person.__init__(self,name)
#         self.emp_id = emp_id
#     def display(self):
#         print("Employee name",self.name,"employee id",self.emp_id)
#
# class Intern(Student, Employee):            #Multiple inheritance
#     def __init__(self, name, emp_id, roll_no, duration):
#         Student.__init__(self, name, roll_no)        # MRO - Method Resolution Order -> it creates some problem( diamond issue)
#         Employee.__init__(self, name, emp_id)
#         self.duration = duration
#
#     def show_intern(self):
#         print("intern:", self.name, "Roll:",self.roll_no,"EmpID:",self.emp_id,"Duration:",self.duration)
#
# s = Student("John", "12345")
# e = Employee("Peter", "1234")
# i = Intern("Selenium",100,"C2345","2 yrs")
#
# s.display()
# e.display()
# s.show()
# e.show()
# i.show()
# i.show_intern()

#Polymorphism
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
#         else:
#             print("Insufficient balance!")
#
#     def str(self):
#         return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"
#
# # Child class: Savings Account
# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, balance=0, interest_rate=0.03):
#         super().__init__(account_holder, balance)
#         self.interest_rate = interest_rate
#
#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")
#
# # Child class: Current Account
# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         # No withdrawal limit for Current Accounts
#         self.balance -= amount
#         print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
#
# # Child class: Fixed Deposit Account
# class FixedDepositAccount(BankAccount):
#     def __init__(self, account_holder, balance=0, interest_rate=0.07, duration=12):
#         super().__init__(account_holder, balance)
#         self.interest_rate = interest_rate
#         self.duration = duration  # in months
#
#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f"Fixed deposit interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")
#
#     def withdraw(self, amount):
#         print("Withdrawal not allowed before maturity!")
#
# # print("DEBUG:",SavingsAccount)
# savings = SavingsAccount("FITA", 1000)
# current = CurrentAccount("FITA", 2000)
# fixed = FixedDepositAccount("FITA", 5000)
#
#
# # print(savings)
# savings.deposit(500)
# savings.add_interest()
# savings.withdraw(300)
#
# print("\n", current)
# current.withdraw(2500)
#
# print("\n", fixed)
# fixed.add_interest()
# fixed.withdraw(1000)

#Abstraction----------------------------
# from abc import ABC, abstractmethod
# class BankAccount(ABC):     ## abc -> abstract base class module.ABC -> it's a base class which inherit from when defining an abc
#     @abstractmethod
#     def deposit(self, amount):
#         pass         # statement will run without any errors
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
# # Above two methods, declared / implemented in the child classes
#
#  # Concrete class for a Savings Account
# class SavingsAccount(BankAccount):
#     def __init__(self):
#         self._balance = 0        # # internal detail hidden
#     def deposit(self, amount):
#         self._balance += amount
#         print(f"Deposited {amount} Current bal: {self._balance}")
#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#             print(f"Withdrew ₹{amount}. Current balance: ₹{self._balance}")
#         else:
#             print("Insufficient balance")
#
# account = SavingsAccount()
# account.deposit(1000)
# account.withdraw(500)
# account.withdraw(600)
#---------------------------------------------------------
#map function
# def square(x):
#     return x * x
# num = [1,2,3,4,5]
# squared_num = map(square, num)
# print(list(squared_num))
#
# #lamda function ->  lambda is an anonymous function
# num = [1,2,3,4,5]
# squared_num = map(lambda x: x*x , num)
# print(list(squared_num))

#Filter
# num = [1,2,3,4,5]
# even_no = filter(lambda x: x % 2 == 0, num)
# print(list(even_no))

# Enumerator
# a = ["Apples", "Oranges", "Bananas"]
# for index, fruit in enumerate(a, start=5):
#     print(f"index: {index} value: {fruit}")

#decorator
def my_decorator(func):
    def wrapper():
        print("Java")
        func()
        print("Python")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
# Calling the decorated function
say_hello()




