#!/usr/bin/python3
"""Module containing class Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class of Square inherits from Rectangle"""
    def __init__(self, size):
        """initializes an instance of square
        Arguement:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
