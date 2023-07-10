#!/usr/bin/python3
"""Contains a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class of rectangle objects inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle class

        Arguments:
            width (int): width of rectangle
            height (int): height og rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
