# ~Local Vs Global Variables~
x = 4
print(x)

def hello(): # Function definition
    x = 5
    print(f"The Local x is {x}") # Local variable x
    print("Hello Arun")

print(f"The Global x is {x}") # Global variable x
hello() # Calling the function
x = 5
print(f"The Global X is {x}")

# OR

x = 10

def my_function(): # Function definition
    global x # Declaring x as a global variable
    x = 4 # Modifying the global variable x
    y = 5 # Local variable y
    print(y)

my_function() # Calling the function
print(x)
# print(y) # This will raise an error since y is a local variable and not accessible outside the function
