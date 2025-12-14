f = open(r"D:\Learning\MyProjects\Python\Python-Learning\Intermediate\demo.txt", "a")
# data = f.read();
# print(type(data))

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# data = f.write("\nHHAHAH fool")
# print(data)
f.close()

with open("../sampleOne.txt", "r") as a:
    data=a.read()
    print(data)
a.close()

with open(r"D:\Learning\MyProjects\Python\Python-Learning\Intermediate\sampleTwo.txt", "r") as b:
    data = b.read()
    print(data);
b.close()