"""
these are tests for the books module
"""

from django.test import TestCase


class SimpleTest(TestCase):
    '''
    this is for testing the books
    '''
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
