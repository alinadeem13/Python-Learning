# Tuples Practice Questions

tup1 = ("C", 'D', 'A','A', 'B', 'B','A')

print(tup1.count('A'))

newList = []

for item in tup1:
    newList.append(item)
newList.sort()

print(tuple(newList))   
print(tup1.index('B'))
print(newList)
print(newList.index('B'))