#!/usr/bin/python3
"""Unit test module for Base class"""


import unittest
from models.base import Base
from models import base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBaseInit(unittest.TestCase):
    """unit test for initialization of base"""

    def test_id_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_arg_more(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 2)

    def test_with_arg(self):
        self.assertEqual(Base(10).id, 10)

    def test_with_bool(self):
        self.assertEqual(Base(True).id, True)

    def test_with_string(self):
        self.assertEqual(Base("1").id, "1")

    def test_with_float(self):
        self.assertEqual(Base(1.5).id, 1.5)

    def test_with_list(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_with_tuple(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))

    def test_with_dict(self):
        self.assertEqual(Base({"a": 1}).id, {"a": 1})

    def test_mixed_id(self):
        b1 = Base()
        b2 = Base(100)
        self.assertGreater(b2.id, b1.id + 1)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_module_doc(self):
        self.assertGreater(len(base.__doc__), 0)

    def test_class_doc(self):
        self.assertGreater(len(Base.__doc__), 0)

    def test_class_method_doc(self):
        self.assertGreater(len(Base.create.__doc__), 0)

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


class TestToJsonString(unittest.TestCase):
    """Testing to_json_string method"""

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_None_list(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_one_dict(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[' + json.dumps(dictionary) + ']')
        self.assertIs(type(json_dictionary), str)

    def test_2_dicts(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2, 10)
        dictionary = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary, dictionary2])
        self.assertEqual(json_dictionary, '[' + json.dumps(dictionary) + ', ' +
                         json.dumps(dictionary2) + ']')
        self.assertIs(type(json_dictionary), str)

    def test_no_arguement(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_multiple_args(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        with self.assertRaises(TypeError):
            Base.to_json_string(dictionary, dictionary2)

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        dictionary = s.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dict))
        self.assertEqual(json_dict, '[' + json.dumps(dictionary) + ']')

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        dictionary1 = s1.to_dictionary()
        dictionary2 = s2.to_dictionary()
        list_dicts = [dictionary1, dictionary2]
        j_dict = Base.to_json_string(list_dicts)
        self.assertEqual(j_dict, '[' + json.dumps(dictionary1) + ', ' +
                         json.dumps(dictionary2) + ']')


class TestFromJsonString(unittest.TestCase):
    """unit test for from_json_string method"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_one_dict_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        from_json = Base.from_json_string(json_dictionary)
        self.assertEqual([dictionary], from_json)
        self.assertEqual(list, type(from_json))

    def test_2_dicts_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2, 10)
        dictionary = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary, dictionary2])
        from_json = Base.from_json_string(json_dictionary)
        self.assertEqual([dictionary, dictionary2], from_json)

    def test_multiple_args(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary, dictionary2])
        with self.assertRaises(TypeError):
            Base.from_json_string(dictionary, dictionary2)

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        dictionary = s.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        from_json = Base.from_json_string(json_dict)
        self.assertEqual([dictionary], from_json)
        self.assertEqual(list, type(from_json))

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        dictionary1 = s1.to_dictionary()
        dictionary2 = s2.to_dictionary()
        list_dicts = [dictionary1, dictionary2]
        j_dict = Base.to_json_string(list_dicts)
        from_json = Base.from_json_string(j_dict)
        self.assertEqual([dictionary1, dictionary2], from_json)

    def test_other_types(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(1)
            Base.from_json_string("hell")
            Base.from_json_string({"h": 1})
            Base.from_json_string([1, 2, 3, 4])


class TestBaseSaveToFile(unittest.TestCase):
    """tests the save to file method"""
    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_one_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 54)

    def test_2_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 107)

    def test_one_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

    def test_2_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 78)

    def test_base(self):
        b = Base()
        with self.assertRaises(AttributeError):
            Base.save_to_file([b])

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 2)

    def test_other_types(self):
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("hello")
            Rectangle.save_to_file({"a": 1})
            Rectangle.save_to_file([1, 2])

    def test__None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_multiple_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])


class TestBaseCreate(unittest.TestCase):
    """tests create method"""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_with_id(self):
        r1 = Rectangle(3, 5, 1, 2, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (10) 1/2 - 3/5", str(r2))

    def test_create_square(self):
        s1 = Square(3, 5, 1, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (10) 5/1 - 3", str(s1))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_not_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(17, 7, 2, 7, 1)
        r2 = Rectangle(2, 10, 8, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        r3 = list_rectangles[0]
        r4 = list_rectangles[1]
        self.assertEqual(str(r1) + str(r2), str(r3) + str(r4))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares = Square.load_from_file()
        s3 = list_squares[0]
        s4 = list_squares[1]
        self.assertEqual(str(s1) + str(s2), str(s3) + str(s4))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
