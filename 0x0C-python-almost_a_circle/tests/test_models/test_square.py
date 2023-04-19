#!/usr/bin/python3

"""
This module contains test cases based on Square class
The tests can be run using these commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_rectangle.py
Below are several test cases on the class
"""

import unittest
import os
import pep8
from io import StringIO
from models.square import Square
from contextlib import redirect_stdout


class TestPep8(unittest.TestCase):
    """Test to validate PEP 8"""
    def test_pep8(self):
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, 'Wrong Pep8 style, adjust your code !')

    def setUp(self):
        """For dictionary conversion"""
        self.square = Square(10, 2, 1, 5)

    def test_square_attr(self):
        """ passing size attr """
        a = Square(1)
        self.assertEqual(a.size, 1)

    def test_attrs(self):
        """ passing 2 attrs """
        a = Square(1, 2)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.size, 1)

    def test_more_attr(self):
        """ paasing 3 attrs """
        b = Square(10, 2, 3)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 3)
        self.assertEqual(b.size, 10)

    def test_excess_attr(self):
        """ Excess attrs """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_wrong_attr(self):
        """ passing a wrong type of attribute """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_less_than_zero(self):
        """ passing attr less than zero """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_display(self):
        """ testing the magic method __str__ """
        with StringIO() as buf, redirect_stdout(buf):
            print(self.square, end='')
            output = buf.getvalue()
        self.assertEqual(output, "[Square] (5) 2/1 - 10")

    def test_to_dictionary(self):
        """ testing to dictionary function """
        sq_dic = self.square.to_dictionary()
        self.assertEqual(sq_dic, {'size': 10, 'x': 2, 'y': 1, 'id': 5})
        self.assertEqual(type(sq_dic), dict)
