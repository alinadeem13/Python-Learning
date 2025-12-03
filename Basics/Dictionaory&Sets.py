# ======= Dictonaries & Sets in Python =======

#  ------ Dictionaries are like Objets in JS and are mutable ------

info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# print(info)  # Printing the entire dictionary
# print(info["name"])  # Accessing value by key
# info["age"] = 31  # Modifying value
# info["profession"] = "Engineer"  # Adding new key-value pair
# print(info)
# del info["city"]  # Deleting a key-value pair
# print(info)

# for key in info:
#     print(f"{key}: {info[key]}")  # Iterating through keys  

# for key in info:
#     print(info[key])
# print(info.values())  # Iterating through values
# print(info.keys())  # Iterating through keys

# print(list(info.keys()))  # Converting keys to a list
# print(list(info.values()))  # Converting values to a list

# items() method to get key-value pairs
# print(info.items())


# ------ Sets are unordered collections of unique elements ------

my_set = {1, 2, 3, 4, 5}
# print(my_set)  # Printing the entire set
# my_set.add(6)  # Adding an element
# print(my_set)
# my_set.add(3)  # Adding a duplicate element (will have no effect)
# print(my_set)
# my_set.remove(2)  # Removing an element
# print(my_set)
# # my_set.remove(10)  # Trying to remove a non-existent element (will raise KeyError)
# my_set.discard(10)  # Trying to remove a non-existent element (will not raise an error)
# print(my_set)
# print(3 in my_set)  # Checking membership
# print(10 in my_set)  # Checking membership
# for item in my_set:
#     print(item)  # Iterating through the set


# set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# print(set_a.union(set_b))  # Union
# print(set_a.intersection(set_b))  # Intersection
# print(set_a.difference(set_b))  # Difference
# print(set_b.difference(set_a))  # Difference
# print(set_a.symmetric_difference(set_b))  # Symmetric Difference
# print(set_a.issubset(set_b))  # Subset
# print(set_a.issuperset(set_b))  # Superset
# print(set_a.isdisjoint(set_b))  # Disjoint

# Frozen Set - Immutable version of a set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
# frozen_set.add(6)  # Trying to add an element (will raise AttributeError)
# print(frozen_set)

# frozen_set.remove(3)  # Trying to remove an element (will raise AttributeError)
# print(frozen_set)

print(3 in frozen_set)  # Checking membership