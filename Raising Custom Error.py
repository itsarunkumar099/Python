# ~Raising Custom Error~
a = int(input("Enter any vale between 5 and 9 : ")) # Taking input from user

if a<5 and a>9: # Checking if the value is not between 5 and 9
    raise ValueError("The value is not between 5 and 9") # Raising a ValueError with a custom message