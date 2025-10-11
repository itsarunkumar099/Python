# ~List~
marks = [10, 20, 30, "Arun", "Tarun"]
print("Marks:", marks) 
print("Length of Marks:", len(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) # Accessing elements using negative indexing
print(marks[len(marks)-3]) #Conert into Positive indexing equivalent
print(marks[5-3]) # Accessing elements using a calculated index
print(marks[2]) # Positive indexing

if 7 in marks:
    print("7 is present in the list")
else:
    print("7 is not present in the list")

if "Arun" in marks:
    print("Arun is present in the list")
else:
    print("Arun is not present in the list")

if "run" in "Arun":  # Checking if substring "run" is present in the string "Arun"
    print("run is present in Arun")
else:
    print("run is not present in Arun")

if "ran" in "Arun":   #Same thing applies for strings as well !
    print("ran is present in Arun")
else:
    print("ran is not present in Arun")

marks = [10, 20, 30, 40, 50, "Arun", "Tarun", "Ravi", "Kumar", "Singh"]
print(marks)
print(marks[:])  # Printing the entire list
print(marks[1:4])  # Slicing the list to get elements from index
print(marks[1:-1])  # Slicing the list to get elements from index 1 to the second last element
print(marks[1:9:3])  # Slicing the list to get elements from index 1 to 9 with a step of 3
print(marks[1:3 + 1]) 

lst = [ i for i in range(6)]
print([lst])
lst = [ i*i for i in range(8)]
print([lst])
lst = [ i*i for i in range(10) if i%2 == 0]
print([lst])