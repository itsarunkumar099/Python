# ~Data Type~
# a= 10
# b= 20
# print(a + b)

# a = "10"
# b = "30"
# print(int(a) + int(b))

# ~Variable~
# a = 5
# b = 3
# print("the vale of a + b is:", a + b)
# print("the vale of a - b is:", a - b)
# print("the vale of a * b is:", a * b)
# print("the vale of a / b is:", a / b)

# ~Typecasting~
# a = input("Enter first number of Sum: ")
# b = input("Enter second number of Sum: ")
# print("The value of a + b is:", int(a) + int(b)) 
# # if
# print(a + b)   

# c = input("Enter first number of multiply: ")
# d = input("Enter second number of multiply: ")
# print("The value of c * d is:", int(c) * int(d))

# e = input("Enter first number of subtraction: ")
# f = input("Enter second number of subtraction: ")
# print("The value of e - f is:", int(e) - int(f))

# g = input("Enter first number of division: ")
# h = input("Enter second number of division: ")
# print("The value of g + h is:", int(g) / int(h))

# ~String~
# name  = "Arun Kumar"
# work = 'Studing'
# intro = '''Hello, my name is Arun Kumar.
# I am Good boy
# My hobby is GYM'''
# print("Hello, " + name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])
# print(name[8])
# print(name[9])
# # print(name[10]) # Throws an error because index 10 is out of range

# print("Lets use a for Loop")
# # for character in name:
# #     print(character)

# for character in intro:
#     print(character)

# ~String Slicing~
# name = "Arun Kumar"
# ArunKumar = len(name)
# print(ArunKumar)
# print(name[0:4])  # including 0 not including 4
# print(name[6:10]) # including 6 not including 10
# print(name[0:5])  # including 0 not including 5
# print(name[:7])
# print(name[5:])
# #
# print(name[0:-4])   # Negative string slicing
# print(name[-9:-5])  # Negative string slicing

# ~String Methods~
# # String are immutable
# a = "Arun Kumar"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.replace("Arun", "Tarun"))
# print(a.split(" "))

# b = "!!!!! Arun Kumar !!!!!"
# print(b.rstrip("!"))  # Removes trailing exclamation marks
# print(b.split(" "))

# c = "!!!!! Arun Kumar $$$$$"
# print(c.rstrip("$"))  # Removes trailing exclamation marks
# print(c.split(" "))

# Heading = "HOw tO leArN PyThPOn iN 30 dAys"
# print(Heading.capitalize())

# str1 = "Welcome to the world of Python"
# print(str1.center(50))
# print(len(str1))            # Just to show the length of the string
# print(len(str1.center(50))) #Just to show the length of the centered string

# str1 = "Hello World, Hello Python, Hello Universe"
# print(str1.count("Hello"))  # Counts the occurrences of "Hello"

# str1 = "Python is a great programming language !!!"
# print(str1.endswith("!!!"))  # Checks if the string ends with "!!!"

# str1 = "Python is a great programming language !!!"
# print(str1.endswith("great", 2, 30))  # Checks if the substring "a" is found between index 2 and 30

# str1 = "Python is a great programming language !!!"
# print(str1.find("great"))  # Finds the index of the first occurrence of "great"
# print(str1.find("Java"))  # Returns -1 if "Java" is not found, instead of raising an error
# #print(str1.index("Java"))  # Finds the index of the first occurrence of "Java" (will raise an error if not found)

# str1 = "WelcomeToPythonProgramming"
# print(str1.isalnum())  # Checks if all characters are alphanumeric

# str1 = "Welocme"
# print(str1.isalpha())  # Checks if all characters are alphabetic
# str1 = "Welocme123"
# print(str1.isalpha())  # Returns False because it contains digits

# str1 = "hello world"
# print(str1.islower())  # Checks if all characters are lowercase
# str1 = "Hello World" 
# print(str1.islower())  # Returns False because it contains uppercase letters

# str1 = "Python is fun"
# print(str1.isprintable())
# str1 = "Python is fun\n"
# print(str1.isprintable())  # Returns False because it contains a newline character

# srt1 = "           " # String with only spaces and tabs
# print(srt1.isspace())  # Returns True because it contains only whitespace characters

# str1 = "World Health Organization"
# print(str1.istitle())  # Checks if the string is title-cased (each word starts with an uppercase letter)
# str1 = "World health organization"
# print(str1.istitle())  # Returns False because "health" is not capitalized

# str1 = "Python is a great programming language"
# print(str1.startswith("Python"))  # Checks if the string starts with "Python"

# str1 = "Python is a great programming language"
# print(str1.swapcase())  # Swaps uppercase to lowercase and vice versa

# str1 = "His name is Arun. Arun is a good boy."
# print(str1.title())  # Converts the first character of each word to uppercase and the rest to lowercase

# ~if else Conditional Statement~
# a = int(input("Enter your age: "))
# print("Your age is: ", a)
# if(a>18):
#     print("YOu are eligible to vote")
# else:
#     print("You are not elegible for vote")

# # Conditional Statement with Logical Operators
# # >, <, >=, <=, ==, !=
# print(a>18)  # element is greater than 18
# print(a<18)  #element is less than 18
# print(a>=18) #element is greater than or equal to 18
# print(a<=18) #element is less than or equal to 18
# print(a==18) # Checks if a is equal to 18
# print(a!=18) # Checks if a is not equal to 18

# Example 1 (If Statement)
# appleprice = 100
# budget = 90
# if (appleprice <= budget):
#     print("YOu can buy this apple.")
# else:
#     print("You cannot buy this apple.")

# Example 2 (If-Else Statement)
# appleprice = 50
# budget = 100
# if (budget - appleprice > 50):
#     print("YOu can buy this apple.")
# elif (budget - appleprice > 70):
#     print("It's OK you can buy this apple.")
# else:
#     print("You cannot buy this apple.")

# Example 3 (ELif Statement)
# num = int(input("Enter the vale of num: "))
# if (num < 0):
#     print("Number is Negative")
# elif (num == 0):
#     print("Number is Zero")
# elif (num == 987):
#     print("Number is Special")
# else :
#     print("Number is Positive")

# Example 4 (Nested If Statement)
# num = 18
# if (num < 0):
#     print("Number is Negative")
# elif (num > 0):
#     if (num<=10):
#         print("Number is Between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is betwwn 11-20")
#     else:
#         print("Number iis greater than 20")
# else:
#     print("Number is Zero")

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print("Hours: ", timestamp)
# timestamp = time.strftime('%M')
# print('Minutes: ', timestamp)
# timestamp = time.strftime('%S')
# print("Seconds: ", timestamp)
# a = int(input("Enter time: "))
# if a < 7:
#     print("Good Morning Sir")
# elif a < 16:
#     print ("Good Afternoon Sir")
# elif a < 20:
#     print("Good Night Sir")
# else:
#     print("Good Evening Sir")

# ~For Loops~
# name = "Arun Kumar"
# for i in name:
#     print(i)

# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for k in range(5):
#     print(k)

# for k in range(5):
#     print(k+1)

# for k in range(1, 11):
#     print(k)

# for k in range (1, 12, 3):
#     print(k)
 
# ~While Loops~
# i = 0 
# while (i < 10):
#     print(i)
#     i = i + 1
# print("Loop ended")

# i= int(input("Enter a number: "))
# while (i<=35):
#     i = int(input("Enter a number: "))
# print("Loop ended")

# count = 5
# while count > 0:
#     print (count)
#     count = count - 1
# else:
#     print("Loop ended")

# do while loop
# it is not available in python
# but we can use while loop to achieve the same effect

# ~Break and Continues~
# for i in range(15):
#     if (i == 10):
#         break  # Breaks the loop when i is 10
#     print("5 X ", i + 1, "=", 5 * (i + 1))
# print("Loop ended")

# for i in range(15):
#     if (i == 10):
#         continue  # Skips the iteration when i is 10
#     print("5 X ", i + 1, "=", 5 * (i + 1))

# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if(i%100 == 0):
#         break

# ~Functions~
# a = 9
# b = 8
# if (a > b):
#         print("a is greater than b")
# else:
#         print("b is greater than a")
# gmean1 = (a*b)/(a+b)
# print("The value of gmean1 is:", gmean1)

# c = 6 
# d = 9
# if (c>d):
#     print("c is greater than d")    
# else:
#     print("d is greater than c")
# gemaon2 = (c*d)/(c+d)
# print("The value of gmean2 is:", gemaon2)

# # so we can use function to avoid code repetition

# def gmean(a, b):
#     mean = (a * b) / (a + b)
#     print("The value of gmean is:", mean)

# def isGreater(a, b):
#     if (a > b):
#         print("First number is greater than Second number")
#     else:
#         print("Second number is greater than First number")

# def isLesser(a, b):
#     pass  # Placeholder for future implementation

# a = 9
# b = 8
# isGreater(a, b)
# gmean(a, b)       # Now we can call the function with different values

# c = 6
# d = 9
# isGreater(c, d)
# gmean(c, d)

# e = 3
# f = 5
# isGreater(e, f)
# gmean(e, f)

#  ~Function Arguments~
# def average(a, b):
#     print("The Average is: ", (a+b)/2)
#    
# average(4,6)   # Calling the function with two arguments
# average(10,20)
# #OR
# def average(a=9, b=1):
#     print("The Average is: ", (a+b)/2)
# 
# average(a = 4) # Default value for b will be used
# average(b = 6) 
# #OR
# def average(a, b, c=2):
#     print("The Average is: ", (a+b+c)/2)
# 
# average(4, 6)  # Default value for c will be used
# average(10, 20, 30)  # All three arguments are provided
# 
# def average(*number):
#     sum = 0
#     for i in number:
#         sum = sum + i
#         print("Average is: ", sum/len(number))
            #   
# average(4, 6, 8, 10)  # Variable-length argument list
# average(10, 20, 30, 40, 50)
# 
# def average(*number):
#     sum = 0
#     for i in number:
#         sum = sum + i
#     return sum/len(number)
# c = average(4, 6, 8, 10)  # Variable-length argument list
# print("Average is: ", c)
# 
# def name(fname, mname = "Kumar", lname = "Singh"):
#     print("Hello,", fname, mname, lname)
# 
# name("Arun", "Kumar", "Jain") 
# name("Tarun")
# name("Ravi", "Gupta")
# 
# def name(**name):
#     print("Hello, ", name["fnmae"], name["mname"], name["lname"])
# 
# name(mname = "Kumar", lname = "Singh", fnmae = "Arun")

# ~List~
# marks = [10, 20, 30, "Arun", "Tarun"]
# print("Marks:", marks) 
# print("Length of Marks:", len(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# 
# print(marks[-3]) # Accessing elements using negative indexing
# print(marks[len(marks)-3]) #Conert into Positive indexing equivalent
# print(marks[5-3]) # Accessing elements using a calculated index
# print(marks[2]) # Positive indexing
# 
# if 7 in marks:
#     print("7 is present in the list")
# else:
#     print("7 is not present in the list")
# 
# if "Arun" in marks:
#     print("Arun is present in the list")
# else:
#     print("Arun is not present in the list")
# 
# if "run" in "Arun":  # Checking if substring "run" is present in the string "Arun"
#     print("run is present in Arun")
# else:
#     print("run is not present in Arun")
# 
# if "ran" in "Arun":   #Same thing applies for strings as well !
#     print("ran is present in Arun")
# else:
#     print("ran is not present in Arun")
# 
# marks = [10, 20, 30, 40, 50, "Arun", "Tarun", "Ravi", "Kumar", "Singh"]
# print(marks)
# print(marks[:])  # Printing the entire list
# print(marks[1:4])  # Slicing the list to get elements from index
# print(marks[1:-1])  # Slicing the list to get elements from index 1 to the second last element
# print(marks[1:9:3])  # Slicing the list to get elements from index 1 to 9 with a step of 3
# print(marks[1:3 + 1]) 
# 
# lst = [ i for i in range(6)]
# print([lst])
# lst = [ i*i for i in range(8)]
# print([lst])
# lst = [ i*i for i in range(10) if i%2 == 0]
# print([lst])

# ~List Method~
# a = [1, 2, 3, 4]
# a.append(5)
# print(a)
# 
# a = [9, 5, 3, 7, 1, 6, 2, 8, 4]
# a.sort()  # Sorting the list in ascending order
# print(a)
# 
# a.sort(reverse=True)  # Sorting the list in descending order
# print(a)
# 
# a.reverse()  # Reversing the order of the list
# print(a)
# 
# print(a.index(3))  # Finding the index of the first occurrence of 3
# print(a)
# 
# a = [1, 2, 3, 4, 3, 5]
# print(a.count(3))  # Counting the occurrences of 3 in the list
# print(a)
# 
# m = a.copy() #don't recomment in python programming
# m[0] = 0
# print(a)
# 
# a.insert(1 , 58)
# print(a)
# 
# m = [900, 1000, 1100]
# a.extend(m)
# print(a)
# 
# m = [900, 1000, 1100]
# k = a + m
# a.extend(m)
# print(a)

# ~Tuples~
# tup = (1, 2, 3, 4, 5)
# print(type(tup), tup) # This is a tuple
# 
# tup =(1)
# print(type(tup), tup) # This is not a tuple, it's an integer
# 
# tup = (1,)
# print(type(tup), tup) # This is a tuple
# 
# tup = [1, 2, 3, 4, 5]
# tup[0] = 10
# print(type(tup), tup) # This is a list
# 
# tup = (1, 2, 3, 4, 5, "Arun", "Kumar")
# print(tup) # Printing the entire tuple
# print(tup[0]) # Accessing the first element
# print(tup[1]) # Accessing the second element  
# print(tup[2]) # Accessing the third element 
# print(tup[-1]) # Accessing the last element using negative indexing
# print(tup[-3]) # Accessing the third last element using negative indexing
# 
# if 5 in tup:
#     print("5 is present in the tuple")
# tup2 = tup[1:4]
# print(tup2) # Slicing the tuple to get elements from index 1 to 3
# print(tup[1:-1]) # Slicing the tuple to get elements from index 1 to the second last element

# ~Operation on Tuples~
# countries = ("India", "USA", "UK", "Germany", "France")
# temp = list(countries) # Converting tuple to list
# temp.append("Italy") # Adding an element to the list
# temp.pop(2) # Removing the element at index 2
# temp[2] = "Canada" # Modifying the element at index 2
# countries = tuple(temp) # Converting list back to tuple
# print(countries)
# 
# countries = ("Paksitan", "China", "Russia", "Nepal")
# countries2 = ("India", "USA", "UK")
# SouthEastAsia = countries + countries2 # Concatenating two tuples
# print(SouthEastAsia)
# 
# tuple1 = (0, 1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 4, 5)
# res = tuple1.count(1) # Counting occurrences of 1 in the tuple
# print("Count of 1 in the tuple:", res)
# 
# index = tuple1.index(3) # Finding the index of the first occurrence of 3
# print("Index of first occurrence of 3 in the tuple:", index)
# 
# res = tuple1.index(3, 4) # Finding the index of 3 starting from index 4
# print("Index of 3 in the tuple after index 4:", res)
# # Note: Tuples are immutable, so we cannot add, remove, or modify elements directly in a tuple.
# 
# res = tuple1.index(3, 6, 10) # Finding the index of 3 between index 6 and 10
# print("Index of 3 in the tuple between index 6 and 10:", res)
# 
# res = len(tuple1) # Finding the length of the tuple
# print("Length of the tuple:", res)
# 
# res = sorted(tuple1) # Sorting the tuple (returns a list)
# print("Sorted tuple:", res) 

# ~f-strings~
# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Arun Kumar"
# print(letter.format(country, name)) # str.format() way of formatting
# print(f"Hey my name is {name} and I am from {country}") # f-string way of formattin
# print(f"We use f-stings like this: Hey my name is {{name}} and I am from {{country}}") # To print curly braces
# 
# price = 49.099999
# txt = f"For only {price:.2f} dollars!" # Formatting float to 2 decimal places
# print(txt)
# 
# print(type(f"{2*30}")) # f-string can evaluate expressions

# ~Docstrings~
# def square(n):
#     '''Takes in a number n and returns the square of that number'''
#     print(n**2)
# square(4)
# print(square.__doc__)  # Accessing the docstring of the function

# ~Recursion~
# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return (n * factorial(n - 1))
#  
# print(factorial(5)) # 5 * factorial(4)
# print(factorial(4)) # 4 * factorial(3)
# print(factorial(3)) # 3 * factorial(2)
# print(factorial(2)) # 2 * factorial(1)
# 
# print(factorial(1)) # Base case returns 1
# print(factorial(0)) # Base case returns 1
#  
# # Quick Quiz : Write a program to print the Fibonacci series using recursion. 
# # f(0) = 0
# # f(1) = 1
# # f(2) = f(1) + f(0)
# # f(n) = f(n-1) + f(n-2)
#  
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# 
# print(fibonacci(6)) # 8 is f(5) + f(4) => 5 + 3
# print(fibonacci(7)) # 13 is f(6) + f(5) => 8 + 5
# print(fibonacci(8)) # 21 is f(7) + f(6) => 13 + 8
# print(fibonacci(9)) # 34 is f(8) + f(7) => 21 + 13
# print(fibonacci(10)) # 55 is f(9) + f(8) => 34 + 21 

# ~Set~
# s = {1, 2, 3, 4, 5, 2, 4, 1}
# print(s) # Sets automatically remove duplicates
# 
# info = {"Carla", 22, "Engineer", 22, "Carla", 5.6}
# print(info) # Sets can contain mixed data types and remove duplicates
# 
# a = {}
# print(type(a)) # This is a dictionary, not a set
# 
# a = set()
# print(type(a)) # This is an empty set
# 
# for value in info:
#     print(value) # Iterating through the set

# ~Set Methods~
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# print(s1.union(s2)) # Union of two sets
# print(s1.intersection(s2)) # Intersection of two sets
# print(s1.difference(s2)) # Elements in s1 but not in s2
# print(s2.difference(s1)) # Elements in s2 but not in s1
# print(s1.symmetric_difference(s2)) # Elements in either s1 or s2 but not
# print(s1.isdisjoint(s2)) # Checks if s1 and s2 have no elements in common
# print(s1.issubset(s2)) # Checks if s1 is a subset of s2
# print(s1.issuperset(s2)) # Checks if s1 is a superset of s2
# 
# # s1.update(s2) # Updating s1 with elements from s2
# # print(s1)
# 
# # s1.add(6) # Adding an element to the set    
# # print(s1)
# 
# # s1.remove(3) # Removing an element from the set (raises error if not found
# # print(s1)
# 
# # s1.discard(10) # Removing an element from the set (does not raise error if not found)
# # print(s1)
# 
# # s1.pop() # Removing and returning an arbitrary element from the set
# # print(s1)
# 
# # s1.clear() # Removing all elements from the set
# # print(s1)
# 
# # del s1 # Deleting the set
# # print(s1) # This will raise an error since s1 is deleted
# 
# info ={"Arun", 22, "Engineer", 5.6}
# if "Arun" in info:
#     print("Arun is present in the set")
# else:
#     print("Arun is not present in the set")
# 
# info.add("Kumar")
# print(info)

# ~Dictionaries~
# dic = {"Arun": "Human Being",
#        "Spoon": "Object"}
# print(dic["Arun"]) # Accessing value using key
# 
# dic = {
#     101: "Arun",
#     102: "Amqn",
#     103: "Shubham",
#     104: "Ravi",
#     105: "Tarun"
# }
# 
# print(dic[101]) # Accessing value using key 
# print(dic[103]) # Accessing value using key
# 
# info ={'name': "Arun Kumar",
#        'age': 22, 
#        'eligible': True,}
# print(info)
# print(info['name']) # Accessing value using key
# print(info.get('name2')) # Using get() method to access value (returns None if key not found)
# print(info.keys()) # Getting all keys
# 
# for key in info.keys(): # Iterating through keys
#     print(info[key])
# 
# for key in info.keys(): 
#     print(f"The value corresponding to the key {key} is {info[key]}")
# 
# print(info.items())
# for key, value in info.items(): # Iterating through key-value pairs
#     print(f"The value corresponding to the key {key} is {value}")
# 
# print(info.values()) # Getting all values

# ~Dictionary Methods~
# ep1 = {122: 45, 123: 67, 124: 89, 125: 90}
# ep2 = {126: 56, 127: 78, 128: 90}
# 
# ep1.update(ep2) # Merging two dictionaries
# print(ep1)
# 
# ep1.clear() # Clearing all items in the dictionary
# print(ep1)
# 
# ep1.pop(123) # Removing item with key 123
# print(ep1)
# 
# ep1.popitem() # Removing and returning an arbitrary item
# print(ep1)
# 
# del ep1
# print(ep1) # This will raise an error since ep1 is deleted
# 
# del ep1[122] # Deleting item with key 122
# print(ep1)

# ~for Loop with else~
# for  i in range(5):  # Loop will run from 0 to 4
#     print(i)
# else:
#     print("Sorry no i")
# 
# for i in []: # Empty list, loop will not run
#     print(i)
# else:
#     print("Sorry no i") 
# 
# for i in range(6): #` Loop will run from 0 to 5
#     print(i)
#     if i == 4:
#         break
# else:
#     print("Sorry no i") 
# 
# i = 0        # Infinite loop
# while i<7:
#     print(i)
#     i = i + 1    # Incrementing i
#     if i == 4:   # Breaking the loop when i is 4
#         break
# else:
#     print("Sorry no i")
# 
# for x in range(5):
#     print("interation no {} in for loop".format(x+1))
# else:
#     print("else block in loop")
# print("Out of for loop")

# # ~Exception Handling~
# a = input("Enter a number: ")
# print(f"Multiplication table of {a} is:")
# try:                                        # Try block to catch exceptions
#     for i in range(1, 11):                  # Loop from 1 to 10
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:                                     # Except block to handle exceptions
#     print("Invalid Input! Please enter a valid number.")
# 
# print("Thanks for using the program!")
# print("End of the program")
# 
# try:
#     num = int(input("Enter a number: "))
#     a = [6,3]                                   # List with two elements
#     print(a[num])                               # Accessing element at index num
# except ValueError:
#     print("Number entered is not an integer.")  # Handling ValueError
# except IndexError:
#     print("Index Error occurred.")              # Handling IndexError

# ~Finally Claus~
# def func1():
#     try:
#         l = [1, 2, 3, 4, 5]
#         i = int(input("Enter an index: "))
#         print(l[i])
#     except:     # Catching any exception
#         print("An error occurred.")
#         return 0
# 
#     finally: # Finally block will always execute    # regardless of whether an exception occurred or not
#         print("Execution of func1 is complete.")
# 
# x = func1()     
# print(x)

# ~Raising Custom Error~
# a = int(input("Enter any vale between 5 and 9 : ")) # Taking input from user
# 
# if a<5 and a>9: # Checking if the value is not between 5 and 9
#     raise ValueError("The value is not between 5 and 9") # Raising a ValueError with a custom message

# ~Exercise 3~
# print("Welcome to KBC")
# print("You will be asked 15 questions")
# questions = [
#     ["What is the capital of India?", "Chandigarh", "Delhi", "Mumbai", "Lucknow", 2],
#     ["What is the national animal of India?", "Lion", "Tiger", "Elephant", "Leopard", 2],
#     ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
#     ["Who is known as the Father of Nation in India?", "Subhash Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Bhagat Singh", 2],
#     ["Which is the largest state in India by area?", "Rajasthan", "Maharashtra", "Uttar Pradesh", "Madhya Pradesh", 1],
#     ["Which is the longest river in India?", "Yamuna", "Brahmaputra", "Ganga", "Godavari", 3],
#     ["Which is the national flower of India?", "Rose", "Lotus", "Lily", "Sunflower", 2],
#     ["Which is the fastest land animal?", "Cheetah", "Tiger", "Horse", "Lion", 1],
#     ["Which country is known as the Land of Rising Sun?", "China", "Japan", "Korea", "Thailand", 2],
#     ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
#     ["What is H2O commonly known as?", "Salt", "Water", "Sugar", "Acid", 2],
#     ["Which is the largest ocean?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
#     ["Who invented the light bulb?", "Newton", "Edison", "Einstein", "Tesla", 2],
#     ["Which is the smallest continent?", "Africa", "Australia", "Europe", "Antarctica", 2],
#     ["What is the national currency of India?", "Dollar", "Yen", "Rupee", "Pound", 3],
# ]
# 
# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 
#           160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
# 
# safe_money = 0
# 
# for i in range(len(questions)):
#     question = questions[i]
#     print(f"\nYour question for Rs.{levels[i]} is:")
#     print(question[0])  # print the question text
#     print(f"a. {question[1]} \nb. {question[2]} \nc. {question[3]} \nd. {question[4]}")
# 
#     try:
#         reply = int(input("Enter your answer (1/2/3/4): "))
#     except ValueError:
#         print("Invalid input! Game over.")
#         break
# 
#     if reply == question[-1]:
#         print(f"✅ Correct answer! You have won Rs.{levels[i]}")
# 
#         if i == 4:
#             safe_money = 10000
#             print("🎉 Congratulations! You have reached the safe level of Rs. 10,000")
#         elif i == 9:
#             safe_money = 320000
#             print("🎉 Congratulations! You have reached the safe level of Rs. 3,20,000")
#         elif i == 14:
#             safe_money = 10000000
#             print("🎉 Congratulations! You have won Rs. 1 Crore")
#             break
#     else:
#         print("❌ Wrong answer! Game over.")
#         print(f"You will take home Rs.{safe_money}")
#         break

# ~Short hand if else~
# a = 330
# b = 3303
# print("A") if a > b else print("=") if a == b else print("B") # Short hand if else
# 
# c = 9 if a > b else 0 # Short hand if else to assign value to c
# print(c)

# ~Enumerate Function~
# marks = [12, 15, 20, 1, 80, 70, 30, 25]
# 
# # index = 0             # Initializing index
# # for mark in marks:    # Iterating through the list
# #     print(mark)
# #     if(index==4):
# #         print("awesome")
# #     index += 1        # Incrementing index
# 
# OR
# 
# for index, mark in enumerate(marks):  # Using enumerate to get index and value  
# print(mark)    
# if(index==4):                     # Checking if index is 4
#         print("awesome")

# ~Import functions~
# from math import sqrt, pi           # imports specific functions from math module
# from math import *                  # imports all functions from math module
# from math import pi, sqrt as s      # imports specific functions and renames sqrt to s
# import math as m                    # imports math module and renames it to m
# import math as math_builtin_puthon  # imports math module and renames it to math_builtin_python
# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result) # Output: 3.0
# 
#OR
# 
# import math
# print(dir(math)) # Lists all functions and constants in the math module
# print(math.nan, type(math.nan))

# ~if__name__ == "__main__"~
# import demo
# demo.welcome()

# # ~OS module~
# import os  # Importing the os module to interact with the operating system
# 
# if (not os.path.exists("data")): # Checking if the "data" directory does not exist
#     os.mkdir("data") # Creating the "data" directory
#  
# for i in range (0, 100): # Looping from 0 to 99
#     os.mkdir(f"data/Day{i+1}") # Creating subdirectories Day1, Day2, ..., Day100 inside the "data" directory
# 
# #OR
# 
# import os  # Importing the os module to interact with the operating system
#  
# for i in range (0, 100): # Looping from 0 to 99
#     os.rename(f"data/Day{i+1}", f"data/Tutprial {i+1}")  # Renaming subdirectories Day1, Day2, ..., Day100 to Tutorial 1, Tutorial 2, ..., Tutorial 100
# 
# #OR
# 
# import os
# folders = os.listdir("data") # Listing all items in the "data" directory
# print(folders) # Printing the list of items in the "data" directory
# 
# for folder in folders: # Iterating through each item in the list
#     print(folder) # Printing the name of each item
#     print(os.listdir(f"data/{folder}")) # Listing contents of each subdirectory
# 
# #OR
# 
# print(os.getcwd()) # Printing the current working directory
# 
# os.chdir("/Users") # Changing the current working directory to "/Users"
# print(os.getcwd()) # Printing the new current working directory

# # ~Local Vs Global Variables~
# x = 4
# print(x)
# def hello(): # Function definition
#     x = 5
#     print(f"The Local x is {x}") # Local variable x
#     print("Hello Arun")
# 
# print(f"The Global x is {x}") # Global variable x
# hello() # Calling the function
# x = 5
# print(f"The Global X is {x}")
# 
# # OR
# 
# x = 10
# def my_function(): # Function definition
#     global x # Declaring x as a global variable
#     x = 4 # Modifying the global variable x
#     y = 5 # Local variable y
#     print(y)
# 
# my_function() # Calling the function
# print(x)
# # print(y) # This will raise an error since y is a local variable and not accessible outside the function

# ~File IO~
f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# OR

with open('myfile.txt', 'r') as f:  # Using 'with' statement to automatically close the file
    text = f.read()  # Reading the entire file content
    print(text)  # Printing the content of the file