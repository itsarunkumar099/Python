# ~Break and Continues~
for i in range(15):
    if (i == 10):
        break  # Breaks the loop when i is 10
    print("5 X ", i + 1, "=", 5 * (i + 1))
print("Loop ended")

for i in range(15): 
    if (i == 10):
        continue  # Skips the iteration when i is 10
    print("5 X ", i + 1, "=", 5 * (i + 1))

i = 0 # Infinite loop example
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break