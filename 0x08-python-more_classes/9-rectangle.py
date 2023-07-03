#!/usr/bin/python3
"""Module containing the definition of class rectangle"""


class Rectangle:
    """Class for instances of rectangles"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes a new instance"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of instance of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks for the bigest rectangle
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError if either parameter is not a Rectangle instance
        Returns: The bigger rectangle based on area, rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that creates a square from class
        with same height and width

        Args:
            size (int): size of the sides of the square
        """
        return (cls(size, size))

    def __str__(self):
        """string representation of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        res = []
        for i in range(self.__height):
            [res.append(str(self.print_symbol)) for _ in range(self.__width)]
            if i != self.__height - 1:
                res.append("\n")
        return "".join(res)

    def __repr__(self):
        """returns official representation of the instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Called when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
