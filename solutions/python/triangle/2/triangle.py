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
    sides.sort()
    if isTriangle(sides):
        return sides.count(sides[0]) >= 2 or sides.count(sides[1]) >= 2
    else:
        return False


def scalene(sides):
    if isTriangle(sides):
        return not (equilateral(sides) or isosceles(sides))
    else:
        return False

def isTriangle(sides):
    sides.sort()
    if sides[0]+sides[1] > sides[2]:
        return True
    else:
        return False