
def my_generator(n):
    value =0

    while value <n:
        yield value     # produce the current value of the counter

        value += 1



for value in my_generator(5):
    print(value)


