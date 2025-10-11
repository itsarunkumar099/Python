# ~Recursion~
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n - 1))
    
print(factorial(5)) # 5 * factorial(4)
print(factorial(4)) # 4 * factorial(3)
print(factorial(3)) # 3 * factorial(2)
print(factorial(2)) # 2 * factorial(1)

print(factorial(1)) # Base case returns 1
print(factorial(0)) # Base case returns 1

# Quick Quiz : Write a program to print the Fibonacci series using recursion. 
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(6)) # 8 is f(5) + f(4) => 5 + 3
print(fibonacci(7)) # 13 is f(6) + f(5) => 8 + 5
print(fibonacci(8)) # 21 is f(7) + f(6) => 13 + 8
print(fibonacci(9)) # 34 is f(8) + f(7) => 21 + 13
print(fibonacci(10)) # 55 is f(9) + f(8) => 34 + 21 