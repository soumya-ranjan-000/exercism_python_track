def is_armstrong_number(number):
    total = 0
    length = len(str(number))
    for digit in str(number):
        total += (int(digit) ** length)

    if total == number:
        return True
    else:
        return False
