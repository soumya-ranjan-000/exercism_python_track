def square(number):
    if 0 < number < 65:
        return 2 ** (number-1)
    raise ValueError("square must be between 1 and 64")

def total():
    s = 0
    for i in range (1,65):
        s = s + (2 ** (i-1))
    return s
