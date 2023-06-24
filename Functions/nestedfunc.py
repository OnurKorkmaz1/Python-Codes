# ENCAPSULATION 

def outer(num):
    print("outer")

    def inner(num):
        return num + 1
    num_1 =inner(num)
    print(num_1)


outer(10)

#-------------------------------------------------------

def factorial(number):

    if not isinstance(number,int):
        raise TypeError("Number must be an integer")
    
    if not number >= 0:
        raise TypeError("Number must be zero or posisitive")

    def inner_factorial(number):
        if number <=1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

try:
    print(factorial("4"))

except Exception as ex:
    print(ex)

#-------------------------------------------------------




