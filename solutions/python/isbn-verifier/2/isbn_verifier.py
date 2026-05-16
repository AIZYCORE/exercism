"""A function for validating whether an ISBN is valid."""


def is_valid(isbn):
    """Use to check if it is a valid ISBN-10.

    :param : str - String for detection.
    :return: bool - Is this a valid ISBN-10?
    """
    allowed_chars = "0123456789-Xx"
    if any(char not in allowed_chars for char in isbn): return False
        
    clean = isbn.replace("-", "")
    if len(clean) != 10: return False
        
    if "X" in clean[:9].upper(): return False
    
    integers = [10 if x.upper() == "X" else int(x) for x in clean]
    return sum([r *(10 - i) for i, r in enumerate(integers)]) % 11 == 0