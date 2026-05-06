"""A function calculate the points scored in a single toss of a Darts game."""


import math 
def score(x, y):
    """Calculate the points scored in a single toss.

    :param x: x-coordinate of the dart's position.
    :param y: y-coordinate of the dart's position.
    :return: Score obtained from a single throw.
    """
    distanse = math.hypot(x, y)
    for limit, points_socre in [(1.0, 10), (5.0, 5), (10.0, 1)]:
        if distanse <= limit: return points_socre
    return 0