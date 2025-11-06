# The rules were deceptively simple. Pick any positive integer.
# If it's even, divide it by 2.
# If it's odd, multiply it by 3 and add 1.

def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            count = count + 1
        else:
            number = number * 3 + 1
            count = count + 1

    return count