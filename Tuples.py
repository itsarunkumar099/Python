# ~Tuples~
tup = (1, 2, 3, 4, 5)
print(type(tup), tup) # This is a tuple

tup =(1)
print(type(tup), tup) # This is not a tuple, it's an integer

tup = (1,)
print(type(tup), tup) # This is a tuple

tup = [1, 2, 3, 4, 5]
tup[0] = 10
print(type(tup), tup) # This is a list

tup = (1, 2, 3, 4, 5, "Arun", "Kumar")
print(tup) # Printing the entire tuple
print(tup[0]) # Accessing the first element
print(tup[1]) # Accessing the second element  
print(tup[2]) # Accessing the third element 
print(tup[-1]) # Accessing the last element using negative indexing
print(tup[-3]) # Accessing the third last element using negative indexing

if 5 in tup:
    print("5 is present in the tuple")
tup2 = tup[1:4]
print(tup2) # Slicing the tuple to get elements from index 1 to 3
print(tup[1:-1]) # Slicing the tuple to get elements from index 1 to the second last element