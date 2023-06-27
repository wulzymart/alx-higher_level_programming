#!/usr/bin/python3
"""Module for square generation"""


class Square:
    """Class for getting squares of any size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the tuple position"""
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the value for position"""
        if isinstance(position, tuple) and len(position) == 2 and\
            isinstance(position[0], int) and isinstance(position[1], int)\
                and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of the square based on current size"""
        return self.__size ** 2

    def my_print(self):
        """Prints Square of current size using charcter#"""
        if self.__size:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(' ', end='') for _ in range(self.__position[0])]
                [print('#', end='') for _ in range(self.__size)]
                print('')
        else:
            print('')
