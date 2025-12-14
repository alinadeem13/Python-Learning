import os

# os.remove(r"D:\Learning\MyProjects\Python\Python-Learning\Intermediate\demo.txt")


with open(r"D:\Learning\MyProjects\Python\Python-Learning\Intermediate\pactice.txt", "r") as f:
    data = f.read()
    if(data.find("Learning")):
        print("Found")
    else:
        print("not FOund")

