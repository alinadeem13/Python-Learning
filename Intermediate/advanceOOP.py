# Q1. Create a class Person with name and age, and print details

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age;

#     def details(self):
#         print(self.name, self.age);

# p1 =Person("Ali", 25);
# p1.details()


# Q2. Difference between class variable and instance variable

# class Student:
#     school = "ABC School"   # class variable

#     def __init__(self, name):
#         self.name = name    # instance variable

# s1 = Student("Ali")
# s2 = Student("Ahmed")

# print(s1.school, s2.name)

# Q3. Add a method to check if age >= 18

# class Person:
#     def __init__(self):
#         # self.age = age;
#         pass
    
#     def getAge(self):
#         self.age = int(input("Enter Age"))
#         return self.age

#     def checkAge(self):
#         if(self.age > 18):
#             print("can vote")
#         else:
#             print("cant")

         

# p1 = Person();
# p1.getAge();
# p1.checkAge()


# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

# class Manager(Employee):
#     def show_salary(self):
#         print(self.salary)

# m = Manager(50000)
# m.show_salary()


# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# d = Dog()
# d.sound()

# class A:
#     def __init__(self):
#         print("A init")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B init")

# b = B()

# class Account:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = Account()
# acc.deposit(1000)
# print(acc.get_balance())


# class Bird:
#     def fly(self):
#         print("Some birds fly")

# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow flies")

# class Ostrich(Bird):
#     def fly(self):
#         print("Ostrich can't fly")

# for bird in (Sparrow(), Ostrich()):
#     bird.fly()


# class A:
#     def methodA(self):
#         print("A")

# class B:
#     def methodB(self):
#         print("B")

# class C(A, B):
#     pass

# c = C()
# c.methodA()
# c.methodB()

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# print(C.mro())

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# print(Square(4).area())

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print(self.balance)

# acc = BankAccount("Ali", 1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.show_balance()


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

# v1 = Vector(1,2)
# v2 = Vector(3,4)
# v3 = v1 + v2
# print(v3.x, v3.y)


class Dataset:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

d = Dataset([10, 20, 30])
print(d.mean())
