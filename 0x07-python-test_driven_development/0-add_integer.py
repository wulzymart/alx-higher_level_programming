#!/usr/bin/python3
"""Module containing add integer function for addition of 2 integers"""


def add_integer(a, b=98):
    """Returns integer value of addition of both a and b
    Floats are first casted to integers before addition

    Args:
        a (int or float): First number
        b: (int or float): Second number, default value is 98

    Raises:
        TypeError: if either number is not an int or float
        TypeError: if eaither number is float infinity or NaN
    Returns:
        result of integer addition of the 2 numbers
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (float('-inf') < float(a) < float('inf')):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if not (float('-inf') < float(b) < float('inf')):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
