str1 = "hi there Alis"
# print(str1)

str2 = "Giving the next line method \n is used to give the next line in the string"

# print(str2)

# to check length of string
# print(len(str2))

#  Indexinggg ==========

print(str1[3])  # to print the 3rd index character
# str1[2] = 'T'  # this will give error as strings are immutable


# Slicing ==========

print(str1[0:5])  # to print from index 0 to 4
print(str1[:5])   # to print from starting to index 4
print(str1[3:])   # to print from index 3 to end
print(str1[-4:-1])  # to print from index -4 to -2
print(str1[::-1])  # to print the string in reverse order

# Strings Functions and Methods ==========

print(str1.lower())  # to convert string to lowercase
print(str1.upper())  # to convert string to uppercase
print(str1.replace("hi", "hello"))  # to replace a substring with another substring
print(str1.count("e"))  # to count occurrences of a substring in the string
print(str1.find("Ali"))  # to find the starting index of a substring in the string
print(str1.index("there"))  # to find the starting index of a substring in the string 
print(str1.isalnum())  # to check if all characters in the string are alphanumeric
print(str1.isalpha())  # to check if all characters in the string are alphabetic
print(str1.endswith("Alis"))  # to check if the string ends with a specific substring
arr = print(str1.split(" "))  # to split the string into a list of substrings based on a delimiter
print(arr)
print(str1.startswith("hi"))  # to check if the string starts with a specific substring

# Conditional Statements ==========


print(" ========= Conditional Statements Example: ===========")

age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")
# Nested if-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
    if marks >= 80:
        print("You are eligible for scholarship.")
    else:
        print("You are not eligible for scholarship.")
else:
    print("Grade: C")
# Logical Operators
temperature = 25
if temperature > 20 and temperature < 30:
    print("The weather is pleasant.")
if temperature < 15 or temperature > 35:
    print("The weather is extreme.")
# Using 'not' operator
is_raining = False
if not is_raining:
    print("You can go for a walk.")
# Ternary Operator
is_even = "Even" if age % 2 == 0 else "Odd"
print(f"The age is {is_even}.")
# Nested Ternary Operator
category = "Adult" if age >= 18 else "Minor" if age >= 13 else "Child"
print(f"The category is {category}.")


print(" ========= End of Conditional Statements Example. ===========")

print(" ========= End of Strings & Conditional Statements Example. ===========")

print(" ========= Basics Complete. ===========")
print("PRATCICE MORE TO GET BETTER! ")

# Practice Example: Check if a number is even or odd

number = int(input("Enter a positive number: "))
if(number%2 == 0):
    print("The number is even")
else:
    print("The number is odd")

# WAP to find the greatest of 3 numbers entered by the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3
print(f"The greatest number is {greatest}")

# WAP ot check if a number is a multiple of 7 or not

num = int(input("Enter a number: "))

if(num % 7 == 0):
    print(f"{num} is a multiple of 7")
else:
    print(f"{num} is not a multiple of 7")



# WAP to check if string is palindrome or not
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
    

print(" ========= End of Practice Example. ===========")

