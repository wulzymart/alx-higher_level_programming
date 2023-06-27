#!/usr/bin/python3
"""Magic class Module for circle properties"""
from math import pi


class MagicClass:
    """Magic class for circle area and circumference"""
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculates area of circle"""
        return (self.__radius**2) * pi

    def circumference(self):
        """Calculates circumference of a circle"""
        return 2 * pi * self.__radius
