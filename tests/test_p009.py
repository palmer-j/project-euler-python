"""Unit tests for p009.py"""

import unittest

from problems.p009 import pythag_trip_with_target


class TestLargestProduct(unittest.TestCase):

    def test_largest_product(self):
        self.assertEqual(pythag_trip_with_target(12), 60)
        self.assertEqual(pythag_trip_with_target(1000), 31875000)
