# number = input("Enter a number: ")
# if number.isdigit():
#     number = int(number)
#     if number % 2 == 0:
#         print(f"{number} is an even number.")
#     else:
#         print(f"{number} is an odd number.")
# else:
#     print("Please enter a valid number.")

# num = float(input("Enter one number: "))
# num2 = float(input("Enter another number: "))

# print(type(num))

# print((num + num2)/2)  # This will concatenate the two strings

# num = int(input("Enter one number: "))
# num2 = int(input("Enter one number: "))
# num3 = int(input("Enter one number: "))

# if(num >= num2):
#     print(True)
# else:
#     print(False)

# if(num % 2 == 0):
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")

# if(num > num2 and num > num3):
#     print(f"{num} is the greatest number.")
# elif(num2 > num and num2 > num3):
#     print(f"{num2} is the greatest number.")
# else:
#     print(f"{num3} is the greatest number.")

# lists1 = [1,2,3,4,5]

# print(type(lists1))

# lists1.append(6)
# lists1.insert(0, 0)
# lists1.remove(4)
# lists1.pop()
# lists1[2] = 1213

# for i in lists1:
#     print(i)    


# tuples1 = (1,2,3,4,5)
# print(type(tuples1))

# tuples1 = list(tuples1)
# tuples1.append(6)
# tuples1.insert(0, 0)
# tuples1.remove(4)

# lists2 = list(tuples1)
# print(lists2)

# tuples1.pop()
# tuples1[2] = 1213
# # print(tuples1)
# # print(type(tuples1))


# lists1 = []

# for i in range(3):
#     lists1.append(input("Enter the name of your favorite movie: "))

# print(lists1)

# list1 = [1,2,3,4,5,2]

# print(list1[1:4])  # Slicing

# if list1 == list1[::-1]:
#     print("The list is a palindrome.")
# else:
#     print("The list is not a palindrome.")

# tuple1 = ('C','D','A','A','B','B', 'A');

# print(tuple1.count('A'))  # Count the number of occurrences of 'A' in the tuple

# print(tuple1.__len__())  # Get the length of the tuple

# count = 0;

# print(tuple1[::-1])  # Reverse the tuple

# listOne = []

# for i in tuple1:
#     listOne.append(i)
#     if(i == 'A'):
#         count += 1;
        


# listOne.sort()  # Sort the list in place
# print("Count " ,count)    
# print("Lists :",listOne)

# set1 = {'A', 'B', 'C', 'D', 'A', 'B'}

# print(type(set1))  # Sets do not allow duplicate values, so 'A' and 'B' will only appear once in the set

# set1.add('E')  # Add an element to the set
# set1.remove('C')  # Remove an element from the set
# print(set1)


# dict1 = {
#     "name": "Ali",
#     "age": 25,
#     "city": "London",
#     "name": "Ali_N",  # Duplicate key, the last value will overwrite the previous one

# }

# print(dict1)


# lists1 = ["python", "java", "c++", "javascript", "c", "javascript", "python", "c++"]

# classes = set(lists1)

# print(classes.__len__())  # Get the number of unique classes in the list

# dict1 = {}

# for i in range(3):
#   key = input("enter the suject name: ")
#   value = input("enter the marks: ")
#   dict1[key] = value

# print(dict1)

# set1 = {1, 2, 3, 4, 5,5.0}
# print(set1)

set1 = {}

for i in range(2,10):
    set1[i] = i*i

print(set1)    

def num(x):

    for i in set1:
        if i == x:
            print(f"Found {x} at index {i} with value {set1[i]}")
    else:
        print(f"{x} not found in the set.")


number = int(input("Enter a number to search in the set: "))
num(number)