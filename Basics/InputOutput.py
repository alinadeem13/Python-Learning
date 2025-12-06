f = open(r"d:/Learning/MyProjects/Python/Python-Learning/Basics/demo.txt", "a")
# content = f.read()
# print(content)
# print(type(content))

# content = f.readlines()
# for line in content:
#     print(line.strip())
# print(content)

content = f.write("\nI see now")
print(content)

f.close()