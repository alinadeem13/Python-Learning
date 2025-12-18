


# try:
#     x = int(input("Enter a number:"))
#     print(x)
# except ValueError:
#     print("Invalid Input")


# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("cant divide by 0")

# try:
#     with open (r"D:\Learning\MyProjects\Python\Python-Learning\Intermediate\pactice.txt", "r") as f:
#         content = f.read()  
#         print(content)
# finally:
#     f.close();    

# with open("file1.txt", "w") as f:
#     f.write("Line 1\n")
#     f.write("Line 2\n")
#     f.write("Line 3\n")
#     f.write("Line 4\n")
#     f.write("Line 5\n")

# with open("file1.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("file2.txt", "w") as f:
#     f.write("1\n2\n3\n4")

# try:
#     total = 0;
#     with open("file2.txt", "r"):
#         for line in f:
#             total+=int(line.strip())
#         print(total);
# except FileNotFoundError:
#     print("file not found")


# import json

# with open("file2.json", "w") as f:
#     json.dump([1, 2, 3, 4], f)


# with open("file2.json", "r") as f:
#     numbers = json.load(f)

# print(sum(numbers))