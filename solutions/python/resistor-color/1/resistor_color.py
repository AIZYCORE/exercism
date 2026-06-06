"""Used to look up the numerical values associated with resistor color codes."""

COLORS_GROUP = ["black", "brown", "red", "orange", "yellow", 
                "green", "blue", "violet", "grey", "white"
               ]

def color_code(color):
    """Look up the numerical value associated with each resistor color.
    
    :param color: str - Resistor colors.
    :return: int - The numerical value associated with each resistor color.
    """
    return COLORS_GROUP.index(color)


def colors():
    """Complete list of resistor color code values
    
    :return: list- Complete list of resistor color code values.
    """
    return COLORS_GROUP