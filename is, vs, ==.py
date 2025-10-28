# ~is, vs, ==~
a = 4       # Assigning integer value 4 to variable a
b = '4'    # Assigning string value '4' to variable b

print(a is b) # Checks if a and b refer to the same object in memory
print(a == b) # Checks if the values of a and b are equal

#OR

a = [1, 2, 3]   # Assigning a list to variable a
b = [1, 2, 3]   # Two different lists with same content

print(a is b) # Checks if a and b refer to the same object in memory
print(a == b) # Checks if the values of a and b are equal

#OR

a = 3       # Assigning integer value 3 to variable a
b = 3       # Assigning integer value 3 to variable b

print(a is b) # Checks if a and b refer to the same object in memory
print(a == b) # Checks if the values of a and b are equal

#OR

a = "Arun"   # Assigning string value "Arun" to variable a
b = "Arun"   # Assigning string value "Arun" to variable b

print(a is b) # Checks if a and b refer to the same object in memory
print(a == b) # Checks if the values of a and b are equal

#OR

a = (1, 2, 3)   # Assigning a tuple to variable a
b = (1, 2, 3)   # Two different tuples with same content

print(a is b) # Checks if a and b refer to the same object in memory
print(a == b) # Checks if the values of a and b are equal

#AND

a = None
b = None

print(a is b) # Checks if a and b refer to the same object in memory
print(a is None) # Checks if a is None
print(a == b) # Checks if the values of a and b are equal

