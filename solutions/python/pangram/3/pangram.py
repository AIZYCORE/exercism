"""The functions determine whether a sentence is a pangram."""


import string
def is_pangram(sentence):
    """Determine whether a sentence is a pangram.

    :param sentence: A sentence used to determine whether is a pangram.
    :return: bool - Is the input a pangram?
    """
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))
    #set()-Remove Duplicates
    #string.ascii_lowercase - Utilizes the built-in lowercase alphabet from the `string` library.
    #.issubset - A function that checks whether a string consists entirely of English letters.
    #.lower() - Convert the string to all lowercase.

    #s = sentence.lower()
    #return all(c in s for c in string.ascii_lowercase)
    #Use list Comprehensions to write.