#!/usr/bin/python3
import unittest
import json
import csv
import os
import pep8

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestPep8(unittest.TestCase):
    """Test to validate PEP 8"""
    def test_pep8(self):
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, 'Wrong Pep8 style, adjust your code !')

    def setUp(self):
        """Test setup"""
        pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")

        except FileNotFoundError:
            pass


class TestBase(unittest.TestCase):

    def test_no_id(self):
        """ No id value passed as argument """
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b3.id, 3)

    def test_unique_id(self):
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base(234).id, 234)
