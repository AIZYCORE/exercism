"""Used to determine whether a number is an Armstrong number."""


def is_armstrong_number(number):
    """Used to determine whether a number is an Armstrong number.

    :pararm number: int - The number to be checked.
    :return: bool - Is this number an Armstrong number?
    """
    s = str(number) # The input is an int; convert it to a character.
    power = len(s)#Find the Power
    
    result = [int(x) ** power for x in s]# List comprehensions can also be applied to strings. The output is a list.
    final_result = sum(result)#Sum the numbers in the list
    return final_result == number#Check if it's correct

    """
    #A more concise way of writing it
    s = str(number)
    return sum(int(x)**len(s) for x in s) == number
    """