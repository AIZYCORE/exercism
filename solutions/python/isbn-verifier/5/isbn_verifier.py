"""A function for validating whether an ISBN is valid."""


def is_valid(isbn):
    """Use to check if it is a valid ISBN-10.

    :param : str - String for detection.
    :return: bool - Is this a valid ISBN-10?
    """
    clean = isbn.replace("-", "")
    
    if len(clean) != 10: return False
        
    if not clean[:9].isdigit(): return False
        
    if not (clean[-1].isdigit() or clean[-1].upper() == "X"): return False
        
    integers = [10 if x == "X" else int(x) for x in clean]
    return 0 == sum(r *(10 - i) for i, r in enumerate(integers)) % 11