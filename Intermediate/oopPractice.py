# class Circle:
#     __pi = 3.14;
#     def __init__(self,radius):
#         self.radius = radius

#     def Area(self):
#          print("Area of a circle is: ", self.__pi * self.radius * self.radius)

#     def Permeter(self):
#         print("Perimeter ", 2 * self.__pi * self.radius)

# c1 = Circle(2)            
# print(c1.Area());
# c2 = Circle(3)
# print(c2.Permeter())

# class Employee:
#     def __init__(self,role, department, salary):
#         self.role = role;
#         self.department = department
#         self.salary = salary;
    
#     def showDetails(self):
#         print("The Employee salary is: ", self.salary)
#         print("The Employee department is: ", self.role)
#         print("The Employee role is: ", self.role)

# class Engineer(Employee):
#     def __init__(self, name, age, role, department, salary):
#         super().__init__(role, department, salary)
#         self. name = name
#         self.age = age


#     def engineerDetails(self):
#         print(self.name , " ", self.age)

# e1 = Engineer("Ali", 25, "Engineer", "Associate",90000)
# e1.showDetails()

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("Employee salary:", self.salary)
#         print("Employee department:", self.department)
#         print("Employee role:", self.role)

# class Engineer(Employee):
#     def __init__(self, name, age, role, department, salary):
#         super().__init__(role, department, salary)
#         self.name = name
#         self.age = age

#     def engineerDetails(self):
#         print(self.name, self.age)

# e1 = Engineer("Ali", 25, "Engineer", "IT", 90000)
# e1.showDetails()
# e1.engineerDetails()


# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price=price
#     def __gt__(self, num2):
#         return self.price > num2.price    

# o1 = Order("cake", 90)
# o2 = Order("Coke", 60)       
# print(o1 > o2)


