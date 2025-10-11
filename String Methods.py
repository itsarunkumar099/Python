# ~String Methods~ (## String are immutable)

a = "Arun Kumar"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("Arun", "Tarun"))
print(a.split(" "))

b = "!!!!! Arun Kumar !!!!!"
print(b.rstrip("!"))  # Removes trailing exclamation marks
print(b.split(" "))

c = "!!!!! Arun Kumar $$$$$"
print(c.rstrip("$"))  # Removes trailing exclamation marks
print(c.split(" "))

Heading = "HOw tO leArN PyThPOn iN 30 dAys"
print(Heading.capitalize())

str1 = "Welcome to the world of Python"
print(str1.center(50))
print(len(str1))            # Just to show the length of the string
print(len(str1.center(50))) #Just to show the length of the centered string

str1 = "Hello World, Hello Python, Hello Universe"
print(str1.count("Hello"))  # Counts the occurrences of "Hello"

str1 = "Python is a great programming language !!!"
print(str1.endswith("!!!"))  # Checks if the string ends with "!!!"

str1 = "Python is a great programming language !!!"
print(str1.endswith("great", 2, 30))  # Checks if the substring "a" is found between index 2 and 30

str1 = "Python is a great programming language !!!"
print(str1.find("great"))  # Finds the index of the first occurrence of "great"
print(str1.find("Java"))  # Returns -1 if "Java" is not found, instead of raising an error
#print(str1.index("Java"))  # Finds the index of the first occurrence of "Java" (will raise an error if not found)

str1 = "WelcomeToPythonProgramming"
print(str1.isalnum())  # Checks if all characters are alphanumeric

str1 = "Welocme"
print(str1.isalpha())  # Checks if all characters are alphabetic
str1 = "Welocme123"
print(str1.isalpha())  # Returns False because it contains digits

str1 = "hello world"
print(str1.islower())  # Checks if all characters are lowercase
str1 = "Hello World" 
print(str1.islower())  # Returns False because it contains uppercase letters

str1 = "Python is fun"
print(str1.isprintable())
str1 = "Python is fun\n"
print(str1.isprintable())  # Returns False because it contains a newline character

srt1 = "           " # String with only spaces and tabs
print(srt1.isspace())  # Returns True because it contains only whitespace characters

str1 = "World Health Organization"
print(str1.istitle())  # Checks if the string is title-cased (each word starts with an uppercase letter)
str1 = "World health organization"
print(str1.istitle())  # Returns False because "health" is not capitalized

str1 = "Python is a great programming language"
print(str1.startswith("Python"))  # Checks if the string starts with "Python"

str1 = "Python is a great programming language"
print(str1.swapcase())  # Swaps uppercase to lowercase and vice versa

str1 = "His name is Arun. Arun is a good boy."
print(str1.title())  # Converts the first character of each word to uppercase and the rest to lowercase
