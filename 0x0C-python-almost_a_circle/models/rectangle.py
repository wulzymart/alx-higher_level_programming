#!/usr/bin/python3
"""Module containing Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Class for all Rectangles"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @property
    def x(self):
        """gets x"""
        return self.__x

    @property
    def y(self):
        """gets y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of the triangle"""
        return (self.__width * self.__height)

    def display(self):
        """displays a triangle"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Creates a custom string representation of the instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the attributes with positional arguements or kwargs"""
        if args and len(args):
            for position in range(len(args)):
                if position == 0:
                    super().__init__(args[position])
                if position == 1:
                    self.width = args[position]
                if position == 2:
                    self.height = args[position]
                if position == 3:
                    self.x = args[position]
                if position == 4:
                    self.y = args[position]
        else:
            if kwargs and len(kwargs):
                for k, v in kwargs.items():
                    if k == "id":
                        super().__init__(v)
                    if k == "width":
                        self.width = v
                    if k == "height":
                        self.height = v
                    if k == "x":
                        self.x = v
                    if k == "y":
                        self.y = v

    def to_dictionary(self):
        """returns dictionary representation of object"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
