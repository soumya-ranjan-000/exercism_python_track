def rebase(input_base, digits, output_base):
    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    # 1st step - convert to base 10 if it is not
    # [1, 0, 1, 0, 1, 0]
    total = 0
    length = len(digits)
    for i in range(0,length):
        position = length-i-1
        digit = digits[i]
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        total+=digit*(input_base**position)
    print(f"Base 10 value of the number {digits} is {total}")

     #2nd Step - convert from base 10 to another base
    new_digits = []
    while total >= output_base:
        rem = total%output_base
        new_digits.append(rem)
        total = total//output_base
    new_digits.append(total)
    new_digits.reverse()
    print(f"New digits {new_digits} with base {output_base}")
    return new_digits

if __name__ == '__main__':
    rebase(2, [1, 0, 1, 0, 1, 0],10)
    rebase(10, [4, 2], 2)
    rebase(16, [2, 10], 3)
    rebase(3, [1, 1, 2, 0], 16)



        


