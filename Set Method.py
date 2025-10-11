# ~Set Methods~
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2)) # Union of two sets
print(s1.intersection(s2)) # Intersection of two sets
print(s1.difference(s2)) # Elements in s1 but not in s2
print(s2.difference(s1)) # Elements in s2 but not in s1
print(s1.symmetric_difference(s2)) # Elements in either s1 or s2 but not
print(s1.isdisjoint(s2)) # Checks if s1 and s2 have no elements in common
print(s1.issubset(s2)) # Checks if s1 is a subset of s2
print(s1.issuperset(s2)) # Checks if s1 is a superset of s2

# s1.update(s2) # Updating s1 with elements from s2
# print(s1)

# s1.add(6) # Adding an element to the set    
# print(s1)

# s1.remove(3) # Removing an element from the set (raises error if not found
# print(s1)

# s1.discard(10) # Removing an element from the set (does not raise error if not found)
# print(s1)

# s1.pop() # Removing and returning an arbitrary element from the set
# print(s1)

# s1.clear() # Removing all elements from the set
# print(s1)

# del s1 # Deleting the set
# print(s1) # This will raise an error since s1 is deleted

# info ={"Arun", 22, "Engineer", 5.6}
# if "Arun" in info:
#     print("Arun is present in the set")
# else:
#     print("Arun is not present in the set")

# info.add("Kumar")
# print(info)