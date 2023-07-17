#!/usr/bin/python3
"""Module containing unittest classes for Rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestClassInit (unittest.TestCase):
    """Test class initializer"""

    def test_all_var(self):
        r = Rectangle(10, 8, 2, 2, 9)
        self.assertEqual(r.id, 9)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_auto_id(self):
        r = Rectangle(10, 8, 2, 2)
        r1 = Rectangle(10, 8, 2, 2)
        self.assertEqual(r.id, r1.id - 1)

    def test_auto_x_y(self):
        r = Rectangle(10, 8)
        self.assertEqual(r.x, r.y)
        self.assertEqual(r.x, 0)

    def test_setters(self):
        r = Rectangle(10, 8, 2, 2, 20)
        r.width = 20
        r.height = 15
        r.x = 0
        r.y = 0
        self.assertEqual([r.width, r.height, r.x, r.y], [20, 15, 0, 0])

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 8, 2, 2, 9, 10)

    def test_too_few_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10)
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_private_attr(self):
        r = Rectangle(10, 8, 2, 2, 9)
        with self.assertRaises(AttributeError):
            print(r.__height)
        with self.assertRaises(AttributeError):
            print(r.__width)
        with self.assertRaises(AttributeError):
            print(r.__x)
        with self.assertRaises(AttributeError):
            print(r.__y)
        with self.assertRaises(AttributeError):
            print(r.__nb_objects)

    def test_not_int_var(self):
        with self.assertRaises(TypeError):
            Rectangle(10.9, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, 1, [1])
        with self.assertRaises(TypeError):
            Rectangle(10, 1, 1, {"a", 1})

    def test_width_first_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 2, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 2, 2, None)

    def test_val_less_0(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10)
        with self.assertRaises(ValueError):
            Rectangle(10, -5)
        with self.assertRaises(ValueError):
            Rectangle(10, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 1, 1, -10)

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)


class TestArea(unittest.TestCase):
    """Runs unit test on area method"""

    def test_area(self):
        self.assertEqual(Rectangle(10, 5).area(), 50)

    def test_passing_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(19, 5).area(5)

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10)
        r.width = 20
        r.height = 5
        self.assertEqual(100, r.area())


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
        r = Rectangle(4, 2)
        correct = "[Rectangle] ({}) 0/0 - 4/2".format(r.id)
        self.assertEqual(correct, str(r))
        r = Rectangle(1, 2, 1)
        correct = "[Rectangle] ({}) 1/0 - 1/2".format(r.id)
        self.assertEqual(correct, r.__str__())
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).__str__(1)

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        stdout = TestPrintOuts.get_print_out(r, "")
        self.assertEqual("##\n##\n##\n", stdout.getvalue())
        r = Rectangle(3, 2, 1, 0, 1)
        stdout = TestPrintOuts.get_print_out(r, "")
        self.assertEqual(" ###\n ###\n", stdout.getvalue())
        r = Rectangle(4, 5, 0, 1, 0)
        stdout = TestPrintOuts.get_print_out(r, "")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, stdout.getvalue())
        r = Rectangle(2, 4, 3, 2, 0)
        stdout = TestPrintOuts.get_print_out(r, "")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, stdout.getvalue())

    def test_display_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).display(1)


class TestUpate(unittest.TestCase):
    """Tests the update method"""

    # Test args
    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_validation_first(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """testing to_dictionary method of the Rectangle class."""

    def test_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_update(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, 1, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
