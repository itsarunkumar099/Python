# ~Functions~
a = 9
b = 8
if (a > b):
        print("a is greater than b")
else:
        print("b is greater than a")
gmean1 = (a*b)/(a+b)
print("The value of gmean1 is:", gmean1)

c = 6 
d = 9
if (c>d):
    print("c is greater than d")    
else:
    print("d is greater than c")
gemaon2 = (c*d)/(c+d)
print("The value of gmean2 is:", gemaon2)

# so we can use function to avoid code repetition

def gmean(a, b):
    mean = (a * b) / (a + b)
    print("The value of gmean is:", mean)

def isGreater(a, b):
    if (a > b):
        print("First number is greater than Second number")
    else:
        print("Second number is greater than First number")

def isLesser(a, b):
    pass  # Placeholder for future implementation

a = 9
b = 8
isGreater(a, b)
gmean(a, b)       # Now we can call the function with different values

c = 6
d = 9
isGreater(c, d)
gmean(c, d)

e = 3
f = 5
isGreater(e, f)
gmean(e, f)