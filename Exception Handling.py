# ~Exception Handling~

a = input("Enter a number: ")
print(f"Multiplication table of {a} is:")
try:                                        # Try block to catch exceptions
    for i in range(1, 11):                  # Loop from 1 to 10
        print(f"{int(a)} X {i} = {int(a)*i}")
except:                                     # Except block to handle exceptions
    print("Invalid Input! Please enter a valid number.")

print("Thanks for using the program!")
print("End of the program")

#OR

try:
    num = int(input("Enter a number: "))
    a = [6,3]                                   # List with two elements
    print(a[num])                               # Accessing element at index num
except ValueError:
    print("Number entered is not an integer.")  # Handling ValueError
except IndexError:
    print("Index Error occurred.")              # Handling IndexError
