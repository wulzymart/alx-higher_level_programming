#!/usr/bin/python3
"""Module containing class BaseGreometry"""


class BaseGeometry:
    """Class of Base Geometry"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Arguements:
            name (string): name of value passed
            value (int): value to validate
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
