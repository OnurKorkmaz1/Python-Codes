
from functools import reduce
"""
def Myfunction(x):
    return x+1

Myfunction(3+5))
"""

def greet(first_name,last_name):   #parameters
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")

greet("onur","korkmaz")      # arguments

# 1-perform a task
# 2-return a value

def increment(number,by=1):  # optional parameter eklendi
    return number + by

print(increment(2,1))
print(increment(number=2, by =1))  # more readable parameters


# number of arguments

def multiple(x,y):
    return x*y

print(multiple(2,8))

# multiple parameters functions
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(multiply(2,3,4,5))

# MAP --- FILTER --- REDUCE

def subs(x):
    return x - 1
scores = [10,9,8,7,6,5]
new_scores = list(map(subs,scores))
print(new_scores)

#filter
even_scores = list(filter(lambda x: (x%2 ==0),scores))
print(even_scores)

#reduce
sum_scores = reduce((lambda x,y: x+y),scores)
print(sum_scores)
