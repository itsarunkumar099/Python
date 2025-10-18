# ~Lambda Function~
def double(x):     # Regular function to double a number
    return x * 2
print(double(5))  # Output: 10
# OR
double = lambda x: x * 2        # Lambda function to double a number
print(double(5))  # Output: 10

cube = lambda x: x * x * x      # Lambda function to calculate cube
print(cube(5))  # Output: 125

avg = lambda x, y, z: (x + y + z) / 3   # Lambda function to calculate average
print(avg(4, 6, 8))  # Output: 6.0

def appl(fx, value):        # Function that applies a lambda function
    return 6 + fx(value)
print(appl(lambda x: x * x, 2))  # Output: 10
