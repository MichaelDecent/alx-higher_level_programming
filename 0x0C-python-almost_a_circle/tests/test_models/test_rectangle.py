#!/usr/bin/python3
import unittest
import pep8

from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout


class TestPep8(unittest.TestCase):
    """Test to validate PEP 8"""
    def test_pep8(self):
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, 'Wrong Pep8 style, adjust your code !')


class TestRectangle(unittest.TestCase):
    """Several test cases for the rectangle class"""

    def setUp(self):
        """For dictionary conversion"""
        self.rect = Rectangle(2, 3, 1, 2, 6)

    def test_initialization(self):
        """ test for the init process """
        rect = Rectangle(4, 8, 2, 1, 5)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_default_val(self):
        """ test for default values """
        rect = Rectangle(5, 3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_setters_validations(self):
        """ tests for the setters validation """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
            Rectangle([50], 8)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
            Rectangle(50, [8])

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
            Rectangle(0, 8)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
            Rectangle(50, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "1", 3)
            Rectangle(50, 8, [2], 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, "3")
            Rectangle(50, 8, 2, [1])

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 3)
            Rectangle(50, 8, -2, 1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -3)
            Rectangle(50, 8, 2, -1)

    def test_area(self):
        """ test for the method area """
        self.assertEqual(self.rect.area(), 6)

    def test_display(self):
        """ test for the display method """
        check = "\n\n ##\n ##\n ##\n"
        with StringIO() as buff, redirect_stdout(buff):
            self.rect.display()
            output = buff.getvalue()
        self.assertEqual(output, check)

        rect2 = Rectangle(3, 4)
        check2 = "###\n###\n###\n###\n"
        with StringIO() as buff, redirect_stdout(buff):
            rect2.display()
            output2 = buff.getvalue()
        self.assertEqual(output2, check2)
