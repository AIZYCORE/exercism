"""A Python function for reversing a string """


def reverse(text):
    """Used to reverse a string.
    :param : str - The string to be reversed.
    :return : str - The string after reversal.
    """ 
    result = "".join([text[-1 - i] for i in range(len(text))])
    return result
    #result = "" 
    #for i in range(len(text)):
        #index = -1 - i
        #result = result + text[index]
    #return result
    #The above is the solution using a loop.