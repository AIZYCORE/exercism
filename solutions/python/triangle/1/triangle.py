"""Used to determine the type of a triangle."""


def equilateral(sides):
    """Used to determine whether a triangle is equilateral.
    
    :param sides: list - Triangle Length.
    :return: bool - Is this an equilateral triangle?
    """
    return all(s > 0 for s in sides )and len(set(sides)) == 1
    

def isosceles(sides):
    """Determine if it is an isosceles triangle.

    :param sides: list - Triangle Length.
    :return: bool - Is this an isosceles triangle?
    """
    a, b, c = sides 
    
    if sum(sides) < 2 * max(sides):
        return False
    return all(s > 0 for s in sides ) and len(set(sides)) <= 2
   #"sum(sides) < 2 * max(sides)" equal to "if not (a + b >= c) or not (a + c >= b)or not (c + b >= a)"

def scalene(sides):
    """Determine whether it is a scalene triangle.

    :param sides: list - Triangle Length.
    :return: bool - Is this a scalene triangle?
    """
    a, b, c = sides
    
    if sum(sides) < 2 * max(sides):
        return False
    return all(s > 0 for s in sides ) and len(set(sides)) == 3 