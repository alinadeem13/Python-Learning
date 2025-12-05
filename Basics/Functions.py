# ------- Functions --------------
# Functions are reusable blocks of code that perform a specific task.

# Defining a function
# def greet(name):
#     """This function greets the person passed in as a parameter."""
#     return f"Hello, {name}!"
# # Calling a function
# print(greet("Alice"))

# def add(a,b):
#     return (a + b)

# answer = add(5, 3)    
# print("The answer is:", answer)

# def factorial(n):
#     """Returns the factorial of a number n."""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print("Factorial of 5 is:", factorial(5))

# def is_even(num):
#     """Checks if a number is even."""
#     return num % 2 == 0
# print("Is 4 even?", is_even(4))
# print("Is 7 even?", is_even(7))

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# print("The 6th Fibonacci number is:", fibonacci(6))

def power(base, exponent=2):
    """Returns the base raised to the exponent. Default exponent is 2."""
    return base ** exponent

# print("3 squared is:", power(4))

# print("2 to the power of 5 is:", power(2, 5))

def greet_all(*names):
    """Greets all the names passed as arguments."""
    for name in names:
        print(f"Hello, {name}!")
# greet_all("Alice", "Bob", "Charlie")

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width
# print("Area of rectangle 5x3 is:", calculate_area(5, 3))

def calculate_area_square(side):
    """Calculates the area of a square."""
    return side * side
# print("Area of square with side 4 is:", calculate_area_square(4))

def outer_function(x):
    """An example of a nested function."""
    def inner_function(y):
        return y * y
    return inner_function(x) + 10
# print("Result of outer_function(5):", outer_function(6))

def modify_list(lst):
    """Modifies the input list by appending a new value."""
    lst.append(100)
    return lst
my_list = [1, 2, 3]
# print("Modified list:", modify_list(my_list))