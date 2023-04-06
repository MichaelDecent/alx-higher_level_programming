import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):

        my_list = [10, 20, 30, 100]
        empty_list = []
        self.assertEqual(max_integer(my_list), 100)
        self.assertEqual(max_integer(empty_list), None)
