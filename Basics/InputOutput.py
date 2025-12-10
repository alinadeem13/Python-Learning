f = open(r"d:/Learning/MyProjects/Python/Python-Learning/Basics/demo.txt", "a")
# content = f.read()
# print(content)
# print(type(content))

# content = f.readlines()
# for line in content:
#     print(line.strip())
# print(content)

content = f.write("\nI see now")
# print(content)


# f.close()

with open(r"d:/Learning/MyProjects/Python/Python-Learning/Basics/demo.txt", "r") as f:
    content = f.read()
    print(content)

# The file is automatically closed after the with block
# print(f.closed)

# import os
# os.remove(r"d:/Learning/MyProjects/Python/Python-Learning/Basics/demo.txt")

# os.rename(r"d:/Learning/MyProjects/Python/Python-Learning/Basics/demo.txt", r"d:/Learning/MyProjects/Python/Python-Learning/Basics/demo_renamed.txt")

# import shutil
