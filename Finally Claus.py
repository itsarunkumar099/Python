# ~Finally Claus~
def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter an index: "))
        print(l[i])
    except:     # Catching any exception
        print("An error occurred.")
        return 0
    
    finally: # Finally block will always execute    # regardless of whether an exception occurred or not
        print("Execution of func1 is complete.")

x = func1()     
print(x)