#!/usr/bin/python3

"""
This module contains test cases of Base class
The tests can be run using these commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base.py
Below are several test cases on the class
"""
import json
import csv
import unittest
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

    def test_base_no_id(self):
        """ passing no id """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_base_id(self):
        """ passing a valid id """
        self.assertEqual(Base(100).id, 100)

    def test_to_json_string(self):
        """ a list of dictionaries """
        obj = Rectangle(2, 3, 4, 5)
        dic_obj = obj.to_dictionary()
        json_string = Base.to_json_string([dic_obj])
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(dic_obj), dict)

    def test_to_json_string_None(self):
        """ passing None """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """ passing a empty list """
        self.assertEqual(Base.to_json_string([]), "[]")

    def from_json_string(self):
        """ passing json string """
        obj = Rectangle(2, 3, 4, 5)
        dic_obj = obj.to_dictionary()
        json_string = Base.to_json_string([dic_obj])
        list_dict = Base.from_json_string(json_string)
        self.assertEqual(type(list_dict), list)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(dic_obj), dict)

    def test_from_json_string_None(self):
        """ passing None """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        """ passing a empty list """
        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """ passing dictionary of an object """
        r1 = Rectangle(10, 20, 2, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)
