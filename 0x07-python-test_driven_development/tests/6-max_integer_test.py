#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for testing function add integer"""

    def test_int_list(self):
        """tests for when list is a  non empty list of integers"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_empty_list(self):
        """tests for when empty list is passed"""
        self.assertIsNone(max_integer([]))

    def test_no_arg(self):
        """tests for when no arguement is passed"""
        self.assertIsNone(max_integer())

    def test_floats_list(self):
        """tests for when list is a  non empty list of floats"""
        self.assertEqual(max_integer([1.0, 4.0, 3, 0, 5.0]), 5.0)

    def test_mixed_list_floats_int(self):
        """tests for when list is a  non empty mixed list of floats and int"""
        self.assertEqual(max_integer([1.0, 4, 3, 0, 5]), 5)

    def test_floats_list(self):
        """tests for when list is a  non empty list of floats"""
        self.assertEqual(max_integer([1.0, 4.0, 3, 0, 5.0]), 5.0)

    def test_strings(self):
        """tests for when arguement is a string"""
        self.assertEqual(max_integer("Hello"), "o")

    def test_strings_list(self):
        """tests for when arguement is a list of string"""
        self.assertEqual(max_integer(
            ["Hello", "World", "Hi", "Zoo", "zoo"]), "zoo")

    def test_mixed_list_with_string(self):
        """tests for when arguement is a mixed list with string"""
        with self.assertRaises(TypeError):
            max_integer([1, "World", 8.9, "Zoo", "j"])

    def test_dict(self):
        """tests for when arguement is a dict"""
        with self.assertRaises(KeyError):
            max_integer({1: 3, 2: 4, 5: 7})

    def test_list_of_dicts(self):
        """tests for when arguement is a list of dicts"""
        with self.assertRaises(TypeError):
            max_integer([{"hello": 3, "world": 4, "xoo": 7},
                         {"hello": 3, "world": 6, "xoo": 8}])

    def test_int_list(self):
        """tests for when list of list of int or floats"""
        self.assertEqual(max_integer(
            [[1, 3, 4, 5], [1, 4, 5.0, 7]]), [1, 4, 5.0, 7])

    def test_non_iteratables(self):
        """tests for when arguement is a dict"""
        with self.assertRaises(TypeError):
            max_integer(1)


if __name__ == "__main__":
    unittest.main()
