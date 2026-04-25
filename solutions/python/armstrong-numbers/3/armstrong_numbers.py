"""Used to determine whether a number is an Armstrong number."""


def is_armstrong_number(number):
    """Used to determine whether a number is an Armstrong number.

    :param number: int - The number to be checked.
    :return: bool - Is this number an Armstrong number?
    """
    str_number = str(number)#Convert to characters
    power = len(str_number)#Derive the Power
    
    return sum(map(lambda x: int(x) ** power, str_number)) == number
    #map(function, iterable) - Apply action 'x' to `str_number`.
    #lambda arguments: expression - Define a temporary action "x". Multiply x by the power.
    #sum - Put together.