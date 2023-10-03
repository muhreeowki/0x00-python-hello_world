#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Test class for max_integer function
    """

    def test_normal(self):
        self.assertIs(max_integer([1, 2, 3, 4]), 4)
        self.assertIs(max_integer([1, 10, 3, 4]), 10)

    def test_empty_list(self):
        self.assertIs(max_integer([]), None)

    def test_list_with_string(self):
        self.assertRaises(TypeError, max_integer(['1', '2', '3', '4']))

    def test_list_with_negatives(self):
        self.assertIs(max_integer([1, -210, -30, -94]), 1)

    def test_list_with_floats(self):
        self.assertIs(max_integer([1.32, 7.84, 910.4, 28.19, 3.212]), 910.4)

    def test_list_with_one_item(self):
        self.assertIs(max_integer([69]), 69)
