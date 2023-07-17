#!/usr/bin/python3
"""Module containing unittest classes for Square class"""

import unittest
from models.square import Square
from models.base import Base
import io
import sys


class TestClassInit (unittest.TestCase):
    """Test class initializer"""

    def test_all_var(self):
        s = Square(10, 2, 2, 9)
        self.assertEqual(s.width, s.height)
        self.assertEqual(s.id, 9)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)

    def test_auto_id(self):
        s = Square(10, 2, 2)
        s1 = Square(10, 2, 2)
        self.assertEqual(s.id, s1.id - 1)

    def test_auto_x_y(self):
        s = Square(10)
        self.assertEqual(s.x, s.y)
        self.assertEqual(s.x, 0)

    def test_setters(self):
        s = Square(10, 2, 2, 20)
        s.size = 20
        s.x = 0
        s.y = 0
        self.assertEqual([s.width, s.height, s.x, s.y], [20, 20, 0, 0])

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            s = Square(10, 2, 2, 9, 10)

    def test_too_few_args(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_private_attr(self):
        s = Square(10, 2, 2, 9)
        with self.assertRaises(AttributeError):
            print(s.__height)
        with self.assertRaises(AttributeError):
            print(s.__width)
        with self.assertRaises(AttributeError):
            print(s.__x)
        with self.assertRaises(AttributeError):
            print(s.__y)
        with self.assertRaises(AttributeError):
            print(s.__nb_objects)

    def test_not_int_var(self):
        with self.assertRaises(TypeError):
            Square(10.9)
        with self.assertRaises(TypeError):
            Square(10, "1")
        with self.assertRaises(TypeError):
            Square(10, 1, [1])
        with self.assertRaises(TypeError):
            Square(10, 1, {"a", 1})

    def test_width_first_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, None)

    def test_val_less_0(self):
        with self.assertRaises(ValueError):
            Square(0, 10)
        with self.assertRaises(ValueError):
            Square(10, -5)
        with self.assertRaises(ValueError):
            Square(10, 1, -1)

    def test_square_is_base(self):
        self.assertIsInstance(Square(10), Base)


class TestArea(unittest.TestCase):
    """Runs unit test on area method"""

    def test_area(self):
        self.assertEqual(Square(10).area(), 100)

    def test_passing_arg(self):
        with self.assertRaises(TypeError):
            Square(10).area(5)

    def test_area_large(self):
        s = Square(999999999999999)
        self.assertEqual(999999999999998000000000000001, s.area())

    def test_area_changed_attributes(self):
        s = Square(2)
        s.size = 20
        self.assertEqual(400, s.area())


class TestPrintOuts(unittest.TestCase):
    """unit tests for the display and __str__ methods"""

    @staticmethod
    def get_print_out(obj, method):
        """redirects stdout to a a string stream"""
        stdout = io.StringIO()
        sys.stdout = stdout
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return stdout

    def test_str_method(self):
        s = Square(4)
        correct = "[Square] ({}) 0/0 - 4".format(s.id)
        self.assertEqual(correct, str(s))
        s = Square(1, 2)
        correct = "[Square] ({}) 2/0 - 1".format(s.id)
        self.assertEqual(correct, s.__str__())
        s = Square(8, 2, 4)
        correct = "[Square] ({}) 2/4 - 8".format(s.id)
        self.assertEqual(correct, str(s))
        s = Square(13, 2, 4, 7)
        self.assertEqual("[Square] (7) 2/4 - 13", str(s))
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_with_arg(self):
        with self.assertRaises(TypeError):
            Square(1, 2).__str__(1)

    def test_display_width_height(self):
        s = Square(2, 0, 0, 0)
        stdout = TestPrintOuts.get_print_out(s, "")
        self.assertEqual("##\n##\n", stdout.getvalue())
        s = Square(3, 1, 0, 1)
        stdout = TestPrintOuts.get_print_out(s, "")
        self.assertEqual(" ###\n ###\n ###\n", stdout.getvalue())
        s = Square(4, 0, 1, 0)
        stdout = TestPrintOuts.get_print_out(s, "")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, stdout.getvalue())
        s = Square(2, 3, 2, 0)
        stdout = TestPrintOuts.get_print_out(s, "")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, stdout.getvalue())

    def test_display_arg(self):
        with self.assertRaises(TypeError):
            Square(1, 2).display(1)


class TestUpate(unittest.TestCase):
    """Tests the update method"""

    # Test args
    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))
        s.update(None, 4, 5, 2)
        correct = "[Square] ({}) 5/2 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(6, 5, 4, 3)
        self.assertEqual("[Square] (6) 4/3 - 5", str(s))

    def test_update_args_invalid_width(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -5)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 2, "")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(89, 1, -6)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 2, 4, "invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(89, 1, 3, -6)

    def test_update_args_width_validation_first(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid", "invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 1, "invalid")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 3, "invalid")

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))
        s.update(size=2, id=1)
        self.assertEqual("[Square] (1) 10/10 - 2", str(s))
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))
        s.update(id=None, size=7, y=9)
        correct = "[Square] ({}) 10/9 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, size=2)
        s.update(y=3, size=15)
        self.assertEqual("[Square] (89) 1/3 - 15", str(s))

    def test_update_kwargs_invalid_width(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_inavlid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, x=4, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 5", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """testing to_dictionary method of the Square class."""

    def test_output(self):
        s = Square(10, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'size': 10}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_update(self):
        s1 = Square(10, 1, 9, 5)
        s2 = Square(5, 1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            Square(10, 2, 4, 1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
