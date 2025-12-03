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

print(list(info.keys()))  # Converting keys to a list
print(list(info.values()))  # Converting values to a list

# items() method to get key-value pairs
print(info.items())