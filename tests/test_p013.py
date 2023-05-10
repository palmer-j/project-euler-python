"""Unit tests for p012.py"""

import unittest

from problems.p013 import solve


class TestP13(unittest.TestCase):

    def test_solved(self):
        self.assertEqual(solve(), '5537376230')
