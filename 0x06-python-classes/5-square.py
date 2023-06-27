#!/usr/bin/python3
"""Module for square generation"""


class Square:
    """Class for getting squares of any size"""
    def __init__(self, size=0):
        """Initializes a square instance"""
        self.size = size

    @property
    def size(self):
        """Gets value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the value of size"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the square based on current size"""
        return self.__size ** 2

    def my_print(self):
        """Prints Square of current size using charcter#"""
        if self.__size:
            for i in range(self.__size):
                [print('#', end='') for _ in range(self.__size)]
                print('')
        else:
            print('')
