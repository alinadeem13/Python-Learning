# # ----------- Classes in Python -----------------

# class Student:


# # default constructor
#     def __init__(self):
#         pass

# # parameterized constructor
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        # print("Student object created for:", self.name)


#     def welcomeMethod(self):
#         print("Welcome Everybody: ", self.name)

#     def getMarks(self):
#         return self.marks               


# s1 = Student("Ali Nadeem", 97)
# print(s1.name, s1.marks)
# s1.welcomeMethod();
# print("Marks are: ",s1.getMarks())






# ---- practice questions ---------

# class Student:


#     @staticmethod
#     def helloStatic():
#         print("yoo static")

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):
#         total = 0
#         for i in range(len(self.marks)):
#             total += self.marks[i]
#         return total / len(self.marks)

# s1 = Student("Ali Nadeem", [90, 89, 87])
# print(s1.name, round(s1.avg(),2))
# s1.helloStatic()



#  ============ Abstraction ===============

# class Car:
#     def __init(self):
#         self.brk = False
#         self.acc = False
#         self.cluth = False;

#     def start(self):
#         self.cluth = True;   
#         self.acc = True
#         print("Car Started ...")

# c1 = Car()
# c1.start()
# print(c1.cluth)


#  ------- practice questions ---------

class Account:
    def __init__(self, blnce, accountNo):
        self.blnce = blnce
        self.accountNo = accountNo

    # debit method
    
    def debit(self, amount):
        self.blnce -= amount
        print("Amount debited: ", amount)
        print("Balance Now: ", self.getBalance())
    
    # credit method
    def credit(self, amount):
        self.blnce += amount
        print("Amount Credited: ", amount)
        print("Balance Now: ", self.getBalance())

     
    def getBalance(self):
        return self.blnce

acc1 = Account(1000, 1234)     
acc1.credit(5000)  
acc1.debit(870)
print(acc1.blnce)