"""function to determine whether a year is a leap year."""


def leap_year(year):
    """Used to determine whether a year is a leap year.
    :param year: int/str - Test whether a year is a leap year.
    :retrun： bool - True if it's a leap year, False otherwise.
    """
    try:
        year = int(year)
    except ValueError as exc:
        raise ValueError("The input must be an integer.") from exc

    if year < 1582:
        raise ValueError("Note: The current Gregorian leap year rules were not adopted prior to 1582.")
        
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)