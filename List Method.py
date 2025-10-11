# ~List Method~
a = [1, 2, 3, 4]
a.append(5)
print(a)

a = [9, 5, 3, 7, 1, 6, 2, 8, 4]
a.sort()  # Sorting the list in ascending order
print(a)

a.sort(reverse=True)  # Sorting the list in descending order
print(a)

a.reverse()  # Reversing the order of the list
print(a)

print(a.index(3))  # Finding the index of the first occurrence of 3
print(a)

a = [1, 2, 3, 4, 3, 5]
print(a.count(3))  # Counting the occurrences of 3 in the list
print(a)

m = a.copy() #don't recomment in python programming
m[0] = 0
print(a)

a.insert(1 , 58)
print(a)

m = [900, 1000, 1100]
a.extend(m)
print(a)

m = [900, 1000, 1100]
k = a + m
a.extend(m)
print(a)