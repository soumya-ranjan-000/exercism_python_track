import math
def score(x, y):
    fx = math.fabs(x)
    fy = math.fabs(y)
    if fx > 10 or fy > 10:
        return 0
    hy = math.sqrt(fx ** 2 + fy ** 2)
    if  5<hy<= 10:
        return 1
    elif 1<hy <= 5:
        return 5
    elif hy <= 1:
        return 10
    else:
        return 0





