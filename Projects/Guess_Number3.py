import random

n = random.randint(0,11)


guess = int(input("guess a random number"))

while n != guess:
    if guess < n:
        print("to low")
        guess = int(input("guess a random number"))
    elif guess > n:
        print("to high")
        guess = int(input("guess a random number"))
    else:
        break
print("you guessed it right!!")
