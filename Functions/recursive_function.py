def factorial(x):

    #this is a recursive function to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

num = 8
print("The factorial of", num, "is", factorial(num))

# --> In the above example, factorial() is a recursive function as it calls itself.    