#!/usr/bin/python3
""" Unittests cases for max_integer([..]). """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests case for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        desend_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(desend_list), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_ele_list = [7]
        self.assertEqual(max_integer(one_ele_list), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats_list = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats_list), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        mixed_list = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed_list), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Michael"
        self.assertEqual(max_integer(string), 'l')

    def test_list_of_strings(self):
        """Test a list of strings."""
        string_list = ["I", "Love", "Software", "Engineering"]
        self.assertEqual(max_integer(string_list), "Software")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
