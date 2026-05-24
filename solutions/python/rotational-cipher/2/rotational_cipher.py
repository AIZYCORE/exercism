"""A python function to create an implementation of the rotational cipher."""


def rotate(text, key):
    """to create an implementation of the rotational cipher.

    :param text: str - The string to be rotated according to the rotation cipher.
    :param key: int - The number of bits to rotate.
    :return: str - The rotated string.
    """
    low_letter = "abcdefghijklmnopqrstuvwxyz"
    up_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = [
        low_letter[(low_letter.index(char) + key) % 26] if char in low_letter else
        up_letter[(up_letter.index(char) + key) % 26] if char in up_letter else
        char 
        for char in text
    ]
    return "".join(result)
   
    #low = "abcdefghijklmnopqrstuvwxyz"
    #up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #result = ""
    #for char in text:
        #if char.isalpha() and char in low:
            #after_idx = (low.index(char) + key) % 26
            #result += low[after_idx]
            
        #if char.isalpha() and char in up:
            #aft_idx = (up.index(char) + key) % 26
            #result += up[aft_idx]
            
        #if not char.isalpha():
            #result += char
    #return result 