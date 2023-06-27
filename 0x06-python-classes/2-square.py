#!/usr/bin/python3
"""Module for square generation"""


class Square:
    """Class for getting squares of any size"""
    def __init__(self, size=0):
        """Initializes a square instance"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:

            raise TypeError("size must be an integer")
