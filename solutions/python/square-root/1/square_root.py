def square_root(number):
    left = 0
    right = number+1
    while left < right-1:
        mid = (left + right) // 2
        if mid * mid <= number:
            left = mid
        else:
            right = mid
    return left
