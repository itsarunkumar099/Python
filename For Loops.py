# ~For Loops~
name = "Arun Kumar" # Iterates through each character in the string
for i in name:
    print(i)

colors = ["Red", "Green", "Blue", "Yellow"] # Iterates through each color in the list
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5): # Generates numbers from 0 to 4
    print(k)

for k in range(5): # Generates numbers from 0 to 4 and adds 1 to each
    print(k+1)

for k in range(1, 11): # Generates numbers from 1 to 10
    print(k)

for k in range (1, 12, 3): # Generates numbers from 1 to 11 with a step of 3
    print(k)