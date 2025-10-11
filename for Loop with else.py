# ~for Loop with else~
for  i in range(5):  # Loop will run from 0 to 4
    print(i)
else:
    print("Sorry no i")

for i in []: # Empty list, loop will not run
    print(i)
else:
    print("Sorry no i") 

for i in range(6): #` Loop will run from 0 to 5
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i") 

i = 0        # Infinite loop
while i<7:
    print(i)
    i = i + 1    # Incrementing i
    if i == 4:   # Breaking the loop when i is 4
        break
else:
    print("Sorry no i")

for x in range(5):
    print("interation no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of for loop")