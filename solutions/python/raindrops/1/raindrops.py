"""A function for converting numbers into the sound of rain."""


def convert(number):
    """Used to convert numbers into the sound of rain.
    
    :param number: int - Numbers Preparing to Transform into the Sound of Rain.
    :return: The sound of rain, or the original digits
    """
    reslut = "".join(value for key, value in {3:"Pling", 5:"Plang", 7:"Plong"}.items() if number % key == 0)
    return reslut or str(number)
    
    #Both a list comprehension and a dictionary were used.
    #List Comprehensions - [ result for variable in iterable if condition ]
    #dictionary - { Key: Value, Key: Value }
    #both:d.items() / key:d.key() / value:d.value()
    #for.....in - action, loop.