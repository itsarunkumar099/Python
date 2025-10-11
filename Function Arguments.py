#  ~Function Arguments~
def average(a, b):
    print("The Average is: ", (a+b)/2)
   
average(4,6)   # Calling the function with two arguments
average(10,20)
#OR
def average(a=9, b=1):
    print("The Average is: ", (a+b)/2)

average(a = 4) # Default value for b will be used
average(b = 6) 
#OR
def average(a, b, c=2):
    print("The Average is: ", (a+b+c)/2)

average(4, 6)  # Default value for c will be used
average(10, 20, 30)  # All three arguments are provided

def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
        print("Average is: ", sum/len(number))
              
average(4, 6, 8, 10)  # Variable-length argument list
average(10, 20, 30, 40, 50)

def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    return sum/len(number)
c = average(4, 6, 8, 10)  # Variable-length argument list
print("Average is: ", c)

def name(fname, mname = "Kumar", lname = "Singh"):
    print("Hello,", fname, mname, lname)

name("Arun", "Kumar", "Jain") 
name("Tarun")
name("Ravi", "Gupta")

def name(**name):
    print("Hello, ", name["fnmae"], name["mname"], name["lname"])

name(mname = "Kumar", lname = "Singh", fnmae = "Arun")