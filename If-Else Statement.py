# ~if else Conditional Statement~
a = int(input("Enter your age: "))
print("Your age is: ", a)
if(a>18):
    print("YOu are eligible to vote")
else:
    print("You are not elegible for vote")

# # Conditional Statement with Logical Operators
# # >, <, >=, <=, ==, !=
print(a>18)  # element is greater than 18
print(a<18)  #element is less than 18
print(a>=18) #element is greater than or equal to 18
print(a<=18) #element is less than or equal to 18
print(a==18) # Checks if a is equal to 18
print(a!=18) # Checks if a is not equal to 18

# Example 1 (If Statement)
appleprice = 100
budget = 90
if (appleprice <= budget):
    print("YOu can buy this apple.")
else:
    print("You cannot buy this apple.")

# Example 2 (If-Else Statement)
appleprice = 50
budget = 100
if (budget - appleprice > 50):
    print("YOu can buy this apple.")
elif (budget - appleprice > 70):
    print("It's OK you can buy this apple.")
else:
    print("You cannot buy this apple.")

# Example 3 (ELif Statement)
num = int(input("Enter the vale of num: "))
if (num < 0):
    print("Number is Negative")
elif (num == 0):
    print("Number is Zero")
elif (num == 987):
    print("Number is Special")
else :
    print("Number is Positive")

# Example 4 (Nested If Statement)
num = 18
if (num < 0):
    print("Number is Negative")
elif (num > 0):
    if (num<=10):
        print("Number is Between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is betwwn 11-20")
    else:
        print("Number iis greater than 20")
else:
    print("Number is Zero")