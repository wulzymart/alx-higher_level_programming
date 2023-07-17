#!/usr/bin/python3
"""Module containing Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a square instance"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes with positional arguements or kwargs"""
        if args and len(args):
            for position in range(len(args)):
                if position == 0:
                    super(Rectangle, self).__init__(args[position])
                if position == 1:
                    self.size = args[position]
                if position == 2:
                    self.x = args[position]
                if position == 3:
                    self.y = args[position]
        else:
            if kwargs and len(kwargs):
                for k, v in kwargs.items():
                    if k == "id":
                        super(Rectangle, self).__init__(v)
                    if k == "size":
                        self.size = v
                    if k == "x":
                        self.x = v
                    if k == "y":
                        self.y = v

    def __str__(self):
        """Creates a custom string representation of the instance"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """returns dictionary representation of object"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
