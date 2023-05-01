"""Unit tests for p011.py"""

import unittest

from problems.p011 import solve


class TestP11(unittest.TestCase):

    def test_p11(self):
        self.assertEqual(solve(), 70600674)
