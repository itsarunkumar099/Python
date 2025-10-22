# ~Map, Filter, Reduce~
# Example:
def cube(x):
    return x * x * x
print(cube(2))

l = [1, 2, 3, 4, 5]
newl = []
for item in l:
    newl.append(cube(item))  # Using a for loop to apply cube function to each item in the list
print(newl)

#OR

# Map Function
def cube(x):
    return x * x * x
print(cube(2))

l = [1, 2, 3, 4, 5]
newl = list(map(cube, l))       # Using map to apply cube function to each item in the list
print(newl)

# OR

l = [1, 2, 3, 4, 5]
newl = list(map(lambda x: x * x * x, l))   # Using map with a lambda function to cube each item in the list
print(newl)

# Filter Function
def filter_function(a):         # Function to filter items greater than 2
    return a>2

l = [1, 2, 4, 6, 4, 3]
newnewl = list(filter(filter_function, l))  # Using filter to get items greater than 4
print(newnewl)

# Reduce Function\
from functools import reduce    # Importing reduce from functools module
numbers = [1, 2, 3, 4, 5]

def mysum(x, y):                # Function to sum two numbers
    return x + y

sum = reduce(mysum, numbers)    # Using reduce to sum all numbers in the list
print(sum)
