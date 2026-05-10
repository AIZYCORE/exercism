"""A function for determining whether a word or phrase is an anagram."""


#import re

def is_isogram(string):
    """Determine if a word or phrase is an isogram.
    
    :param string: str - Characters used to determine whether a word is an isogram.
    :return: bool - Is this an isogram?
    """
    s = string.lower()
    letters = [c for c in s if c.isalpha()]
    return len(letters) == len(set(letters))

    #Regular Expression Syntax↓
    #pattern = r"(.).*\1"
    #return not re.search(pattern, "".join(letters))