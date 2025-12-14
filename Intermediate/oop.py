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

# class Account:
#     def __init__(self, blnce, accountNo):
#         self.blnce = blnce
#         self.accountNo = accountNo

#     # debit method
    
#     def debit(self, amount):
#         self.blnce -= amount
#         print("Amount debited: ", amount)
#         print("Balance Now: ", self.getBalance())
    
#     # credit method
#     def credit(self, amount):
#         self.blnce += amount
#         print("Amount Credited: ", amount)
#         print("Balance Now: ", self.getBalance())

     
#     def getBalance(self):
#         return self.blnce

# acc1 = Account(1000, 1234)     
# acc1.credit(5000)  
# acc1.debit(870)
# print(acc1.blnce)


# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("ho")

# s1 = Student("Ali Nadeem")
# print(s1.name)
# del s1.name
# del s1
# # print(s1)


# class Account:
#     def __init__(self, acc_no, accPass):
#         self.acc_no = acc_no;
#         self.__accPass = accPass;

#     def reset_pass(self): 
#         newPass =  self.__accPass;
#         return newPass

# acc1 = Account("1234", "abcd")
# print(acc1.acc_no, acc1.reset_pass() )

# class Person:
#     __name = "Ali";

#     def __hello(self):
#         print("HI ", self.__name);

#     def welcome(self):
#         self.__hello();

# p1 = Person();
# print(p1.welcome())


# ---------- Inheritance -------------

# class Car:

#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started ...")
    
#     @staticmethod
#     def stop():
#         print("Car stopped")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name;
#         # self.type = type

#         # superMethod -> inheriting parent class
#         super().__init__(type)
#         super().start()


# # c1 = ToyotaCar("Hilex")
# # print(c1.name)
# # print(c1.start())

# c2 = ToyotaCar("Prius", "electric")
# print(c2.type)


# class person:
#     name = "none"

#     # def changeName(self, name):
#     #     # self.name = name
#     #     person.name = name

#     @classmethod
#     def changeName(classs, name):
#         classs.name = name

# p1 = person()
# p1.changeName("Ali")
# print(p1.name)    
# print(person.name)    

# print([1,2] + [3,4])

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real , "i", "+" , self.img , "j")

    def add(self, num2):
        newReal = self.real + num2.real;
        newImg = self.img + num2.img;
        return Complex(newReal, newImg)  

    # dunder function.
    def __mul__(self, num2):
        newReal = self.real * num2.real;
        newImg = self.img * num2.img;
        return Complex(newReal, newImg) 


c1 = Complex(1,4)
c1.show()   
c2 = Complex(11,64)
c2.show()

c3 = c1.add(c2)
c3.show()
c4 = c1 * c2   #dunder function calling, same as c3
c4.show()