#!/usr/bin/python3
"""base class of all classes"""


import json
import csv
import turtle


class Base:
    """Base Class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of instance dictionaries to json file"""
        to_print = []
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            to_print.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(to_print))

    @classmethod
    def create(cls, **dictionary):
        """Creates a new class instance from a dictionary"""
        if not dictionary or dictionary == {}:
            return
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Creates an instance from json file"""
        name = cls.__name__ + ".json"
        try:
            with open(name, encoding="utf-8") as f:
                list_dicts = Base.from_json_string(f.read())
                list_Objs = []
                for item in list_dicts:
                    list_Objs.append(cls.create(**item))
                return list_Objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the instance to csv"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", encoding="utf-8") as f:
            field_names = ["id", "width", "height", "x", "y"] \
                if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
            csv_writer = csv.DictWriter(f, fieldnames=field_names)
            csv_writer.writeheader()
            list_objs = list_objs if list_objs and len(list_objs) else []
            for obj in list_objs:
                csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads from a csv"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, encoding="utf-8") as f:
                field_names = ["id", "width", "height", "x", "y"] \
                    if cls.__name__ == "Rectangle" else\
                    ["id", "size", "x", "y"]
                lines = csv.DictReader(f)
                list_objs = []
                for line in lines:
                    obj = {}
                    for k, v in line.items():
                        obj[k] = int(v)
                    list_objs.append(cls.create(**obj))
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws all the Rectangles and Squares:"""
        art = turtle.Turtle()
        art.screen.bgcolor("#1D5B79")
        art.pensize(3)
        art.shape("arrow")
        art.color("#FAF0D7")
        for rectangle in list_rectangles:
            art.showturtle()
            art.up()
            art.goto(rectangle.x, rectangle.y)
            art.pd()
            for _ in range(2):
                art.forward(rectangle.width)
                art.left(90)
                art.forward(rectangle.height)
                art.left(90)
            art.hideturtle()

        art.color("#F8FDCF")
        for square in list_squares:
            art.showturtle()
            art.up()
            art.goto(square.x, square.y)
            art.pd()
            for _ in range(4):
                art.forward(square.size)
                art.left(90)
            art.hideturtle()
        turtle.exitonclick()
