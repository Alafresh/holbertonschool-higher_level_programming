#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertAlmostEqual(max_integer([50, 40, 60]), 60)

    def max_at_the_beginning(self):
        self.assertAlmostEqual(max_integer([110, 40, 60, 30]), 110)

    def max_in_the_middle(self):
        self.assertAlmostEqual(max_integer([50, 40, 90, 30, 15]), 90)

    def one_negative(self):
        self.assertAlmostEqual(max_integer([-50, -40, -60, -30]), -60)

    def list_of_one(self):
        self.assertAlmostEqual(max_integer([60]), 60)

    def empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)
