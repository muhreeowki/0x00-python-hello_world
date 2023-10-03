#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
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
        self.assertIs(max_integer([1.321, 7.8934, 910.324, 28.12839, 3.23012]), 910.324)
    def test_list_with_one_item(self):
        self.assertIs(max_integer([69]), 69)
