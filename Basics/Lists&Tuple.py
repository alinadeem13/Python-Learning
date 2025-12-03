# Lists

marks = [90, 85, 78, 92, 88]; 
# just like array in JS

# print(marks)  # Output: [90, 85, 78, 92, 88]
# print(marks[0])  # Output: 90
# print(len(marks))  # Output: 5
# marks.append(95)  # Adding an element
# print(marks)  # Output: [90, 85, 78, 92, 88, 95]
# print(marks[1:4])  # Slicing: Output: [85, 78, 92]
# marks.remove(78)  # Removing an element
# print(marks)  # Output: [90, 85, 92, 88, 95]
# print(type(marks))  # Output: <class 'list'>

# print( marks)
# marks.sort()
sortingList = sorted(marks)
# print(marks)
# print(sortingList)
marks.pop(0);
# print(marks)
marks.remove(88);
# print(marks)
marks.insert(1, 89);
# print(marks)
# marks.remove(213); # will throw error