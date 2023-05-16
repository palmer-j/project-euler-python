"""Unit tests for p018.py"""

import unittest

from problems.p018 import max_path, test_input_string1, test_input_string2


class TestMaxPath(unittest.TestCase):

    def test_max_path(self):
        self.assertEqual(max_path(test_input_string1), 1074)
        self.assertEqual(max_path(test_input_string2), 23)
