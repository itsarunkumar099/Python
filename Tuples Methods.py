# ~Operation on Tuples~
countries = ("India", "USA", "UK", "Germany", "France")
temp = list(countries) # Converting tuple to list
temp.append("Italy") # Adding an element to the list
temp.pop(2) # Removing the element at index 2
temp[2] = "Canada" # Modifying the element at index 2
countries = tuple(temp) # Converting list back to tuple
print(countries)

countries = ("Paksitan", "China", "Russia", "Nepal")
countries2 = ("India", "USA", "UK")
SouthEastAsia = countries + countries2 # Concatenating two tuples
print(SouthEastAsia)

tuple1 = (0, 1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 4, 5)
res = tuple1.count(1) # Counting occurrences of 1 in the tuple
print("Count of 1 in the tuple:", res)

index = tuple1.index(3) # Finding the index of the first occurrence of 3
print("Index of first occurrence of 3 in the tuple:", index)

res = tuple1.index(3, 4) # Finding the index of 3 starting from index 4
print("Index of 3 in the tuple after index 4:", res)
# Note: Tuples are immutable, so we cannot add, remove, or modify elements directly in a tuple.

res = tuple1.index(3, 6, 10) # Finding the index of 3 between index 6 and 10
print("Index of 3 in the tuple between index 6 and 10:", res)

res = len(tuple1) # Finding the length of the tuple
print("Length of the tuple:", res)

res = sorted(tuple1) # Sorting the tuple (returns a list)
print("Sorted tuple:", res) 