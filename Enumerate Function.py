# ~Enumerate Function~
marks = [12, 15, 20, 1, 80, 70, 30, 25]

index = 0             # Initializing index
for mark in marks:    # Iterating through the list
    print(mark)
    if(index==4):
        print("awesome")
    index += 1        # Incrementing index

# OR

for index, mark in enumerate(marks):  # Using enumerate to get index and value  
    print(mark)
    if(index==4):                     # Checking if index is 4
        print("awesome")
