"""Function to classify positive integers"""


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    total_sum = sum([i for i in range(1, number) if number % i == 0])
    return  ["deficient", "abundant"][total_sum > number] if total_sum != number else "perfect"

#There are several ways to simplify if....else statements.

#The first is the ternary operator. - "prafect"if total_sum == number else "deficient"

#The second type is the nested ternary operator. - "perfiect"if total_sum == number else("abundant"total_sum > number "deficient")

#The third type—tuples and dictionaries—corresponds to the methods mentioned above.

#The fourth method involves using dictionary mapping - 
#status = {(True, False): "abudant", (False, True): "perfect", (False, False): "deficient"}
#return status[(total_sum > number, total_sum == number)]