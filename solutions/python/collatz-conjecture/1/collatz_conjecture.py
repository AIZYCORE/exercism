"""Calculate the number of steps required for a number to reach 1, according to the rules of the Collatz conjecture.
"""


def steps(number):
    """Steps for deriving a number according to the rules of the Collatz Conjecture.

    :param number: int - A number used to estimate the number of steps.
    :return: int - The number of steps required to return to 1, based on the input number.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    step = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        step += 1
    return step