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
        number = (3 * number + 1) if number % 2 != 0 else (number // 2)
        step += 1
    return step
    #The ternary operator was used.
    #variable = [value if condition is met] if [condition] else [value if condition is not met]  