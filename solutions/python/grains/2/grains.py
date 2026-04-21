"Module to calculate the grain count on a chessboard according to the wheat and chessboard problem."


def square(number):
    """Calculate the number of grains on a given square.
    
    :param number: int - The number of squares on the chessboard.
    :return:  current quantity of wheat grains in this slot.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

    
def total():
    """Calculate the total number of grains on the chessboard.

    :return: The current total number of wheat grains.
    """
    return (2 ** 64) - 1