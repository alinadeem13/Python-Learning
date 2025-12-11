# a = 5;
# b = 6;

# a = a + b;   
# b = a - b;   
# a = a - b;   

# Using tuple unpacking in Python

# a, b = b, a;

# print("a =", a);
# print("b =", b);

# def swap_numbers(x, y):
#     return y, x;

# def checkNumbers(a):
#     if a % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# number = int(input("Enter a number: "))
# result = checkNumbers(number)
# print(f"The number {number} is {result}.")    

# num = int(input("Enter a number: "))
# print("Even" if num % 2 == 0 else "Odd")

# name = input("Enter your name: ")

# print(name[0]);

# for i in range(len(name)):
#     print(name[i])


# vowels = "aeiouAEIOU"
# str = 'Hello World'

# count = 0;

# for char in str:
#     if char in vowels:
#         count += 1;
# print(f"Number of vowels in '{str}' is: {count}")

# str = 'raceCar';

# print(str[::-1].lower());

# if(str.lower() == str[::-1].lower()):
#     print(f"'{str}' is a palindrome.");
# else:
#     print(f"'{str}' is not a palindrome.");

# a = 21
# b=200
# c=3

# if(a>b and a> c):
#     print("a is the largest number.");
# elif(b> a and b> c):
#     print("b is the largest number.");
# else:
#     print("c is the largest number.");

# print(max(a,b,c))


# Lists = [34, 1, 0, -23, 12, 45, 9]

# print(max(Lists))
# print(sorted(Lists)[-2])  # Output: 34

# reverseLists = list(reversed(Lists))
# print(reverseLists)

# emptyList = []

# print(emptyList)

# print(Lists[::-1]) 

# for i in range(len(Lists)):
#     # emptyList.append(Lists[len(Lists)-1-i])
#     emptyList.append(Lists[::-1][i])


# print(emptyList)
# Lists = [34, 1, 0, -23, 12, 45, 9, 1, 12, 45]

# uniqueList = []

# # for item in Lists:
# #     if item not in uniqueList:
# #         uniqueList.append(item)
# #         print(f"Added {item} to uniqueList.")


# Lists = list(set(Lists))
# print(Lists)

# tuples = (10, 220, 30, 40, 50)

# print(max(tuples))

# sentence = "I love python because python is easy python hm I python , "


# words = sentence.split()
# freq = {}
# print(words)

# for w in words:
#     freq[w] = freq.get(w, 0) + 1

# for w in words:
#     if w in freq:
#         freq[w]+=1
#     else:
#         freq[w]=1

# print(freq)


# dist1 = {
#     "a": 1,
#     "b": 2,
# }
# dist2 = {
#     "c": 3,
#     "d": 4,
# }

# dist1.update(dist2)
# print(dist1)
# print(dist2)

# dictcombined = {**dist1, **dist2}
# print(dictcombined)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print(set1.union(set2))  # Union
# print(set1 & set2)  # Intersection
# print(set1.intersection(set2))  # Intersection
# set1.intersection_update(set2)  # Intersection Update

# print(set1)  # Intersection Update

# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


# list_numbers = [5, 12, 7, 3, 9, 15, 2]
# sum = 0;
# # for i in range(len(list_numbers)):  
#     # sum+= list_numbers[i];

# for i in list_numbers:
#     sum += i;
    
# print(f"The sum of the list is: {sum}")

# for i in range(51):
#     if(i%2 == 0):
#         print(i)

# number = int(input("Enter a number: "))

# def squaredNumber(n):
#     return n*n;

# result = squaredNumber(number)
# print(f"The square of {number} is {result}.")


# vowels = 'aeiouAEIOU'



# def countVowels(s):
#     count = 0;
#     for char in s:
#         if char in vowels:
#             count += 1;
#     return count;
# string = input("Enter a string: ")
# result = countVowels(string)
# print(f"The number of vowels in '{string}' is: {result}")

# number = int(input("Enter a number: "))

# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# result = isPrime(number)
# print(f"The number {number} is {'a prime' if result else 'not a prime'} number.")


number = input("Enter a number: ")

def sum_n(n):
    if n <= 0:
        return 0
    elif(n == 1):
        return 1
    else:
        return n + sum_n(n - 1)
    
    

result = sum_n(int(number))
print(f"The sum of first {number} natural numbers is: {result}")
