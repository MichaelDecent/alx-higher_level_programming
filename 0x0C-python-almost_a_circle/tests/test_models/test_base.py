import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

'''
TEST CASES FOR Class Base
'''

class TestBase(unittest.TestCase):
    """ Testing Base """

    def test_no_id(self):
        '''
        passing no id
        '''
        a = Base()
        self.assertEqual(1, a.id)

    def test_valid_id(self):
        '''
        passing a valid id
        '''
        a = Base(10)
        self.assertEqual(10, a.id)

    def test_string_id(self):
        '''
        passing a string id
        '''
        a = Base("Decent")
        self.assertEqual("Decent", a.id)

    def test_to_json_string(self):
        '''
        passing a list of dictionaries
        '''
        a = Base(5)
        list_dict = a.to_dictionary() 
        self.assertEqual(type(Base.to_json_string([list_dict]), str))
