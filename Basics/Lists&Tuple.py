# ====================== Lists =================

marks = [90, 85, 78, 92, 88]; 
# just like array in JS but mutable

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


# ======================= Tuples ================
# just like array in JS but immutable
coordinates = (10, 220, 30, 99, 40);
# print(coordinates)  # Output: (10, 20)
# print(coordinates[0])  # Output: 10
# print(len(coordinates))  # Output: 2
# print(type(coordinates))  # Output: <class 'tuple'>
# coordinates[0] = 15  # This will raise an error since tuples are immutable
# print(coordinates)
# print(coordinates[0:2])  # Slicing: Output: (10, 220)
# print(coordinates.count(30))  # Output: 1



#  ============ Practivce Questions ================
movies = []

answer1 = print(input("Enter 1st Favourite Movie: "))

movies.append(answer1)
answer2 = print(input("Enter 2nd Favourite Movie: "))
movies.append(answer2)
answer3 = print(input("Enter 3rd Favourite Movie: "))
movies.append(answer3)
print("Your Favourite Movies are: ")
print(movies)
for movie in movies:
    print(movie)    