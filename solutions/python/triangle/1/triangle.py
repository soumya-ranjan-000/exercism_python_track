def equilateral(sides):
    if 0 in sides:
        return False
    if sides.count(sides[0]) == 3:
        return True
    else:
        return False


def isosceles(sides):
    if 0 in sides:
        return False
    return True if sides.count(sides[0]) == 2 else False



def scalene(sides):
    return not (equilateral(sides) | isosceles(sides))
