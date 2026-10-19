"""A function for judge resistor color. """

COLORS_GROUP = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet","grey", "white"]

def value(colors):
    """Determine the numeric value of resistor colors.

    :param colors: list[str] - A list of color names as strings.
    :return: int - The numerical value corresponding to the first two colors.
    """
    res = ""
    for i in colors:
        number = COLORS_GROUP.index(i)
        res += str(number)
        res = res[:2]
        final_res = int(res)
    return final_res