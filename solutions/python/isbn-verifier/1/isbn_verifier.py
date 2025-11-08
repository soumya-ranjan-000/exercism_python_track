'''
(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
the check digit of an ISBN-10 may be 'X' (representing '10'). For instance 3-598-21507-X is a valid ISBN-10.
'''


def is_valid(isbn):
    sum_of_all_digit=0
    count=0
    for i in isbn:
        if i.isalpha() and i != 'X':
            return False
        if i.isdigit():
            sum_of_all_digit+= int(i) * (10 - count)
            count+=1
        if i=='X':
            sum_of_all_digit+= 10 * 1
            count+=1
    return count==10 and sum_of_all_digit%11 == 0
