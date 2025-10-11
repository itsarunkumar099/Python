# ~Dictionary Methods~
ep1 = {122: 45, 123: 67, 124: 89, 125: 90}
ep2 = {126: 56, 127: 78, 128: 90}

ep1.update(ep2) # Merging two dictionaries
print(ep1)

# ep1.clear() # Clearing all items in the dictionary
# print(ep1)

# ep1.pop(123) # Removing item with key 123
# print(ep1)

# ep1.popitem() # Removing and returning an arbitrary item
# print(ep1)

# del ep1
# print(ep1) # This will raise an error since ep1 is deleted

# del ep1[122] # Deleting item with key 122
# print(ep1)