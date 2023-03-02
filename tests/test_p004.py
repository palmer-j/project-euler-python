"""Unit tests for p004.py."""

import unittest

from problems.p004 import is_palindromic

class TestIsPalindromic(unittest.TestCase):

    def test_is_palindromic(self):
        self.assertTrue(is_palindromic(9009))
        self.assertTrue(is_palindromic(15951))
        self.assertTrue(is_palindromic(1))
        self.assertFalse(is_palindromic(123456))
        self.assertFalse(is_palindromic(578426974))
