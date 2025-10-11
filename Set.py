# ~Set~
s = {1, 2, 3, 4, 5, 2, 4, 1}
print(s) # Sets automatically remove duplicates

info = {"Carla", 22, "Engineer", 22, "Carla", 5.6}
print(info) # Sets can contain mixed data types and remove duplicates

a = {}
print(type(a)) # This is a dictionary, not a set

a = set()
print(type(a)) # This is an empty set

for value in info:
    print(value) # Iterating through the set