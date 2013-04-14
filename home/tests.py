"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.test.client import RequestFactory
import unittest
from home.views import index
#from mock import patch

class TestIndex(unittest.TestCase):
    """
    This class is used to test the register module
    """
    def setUp(self):
        """
        Every test needs access to the request factory.

        Pylint error: Invalid name "setUp" for type method
                      (should match [a-z_][a-z0-9_]{2,30}$)
        Comment: Do not change "setUp"; it will break testing otherwise
                 with test error: ...object has no attribute 'factory'
        """
        self.factory = RequestFactory()

    def test_home_page(self):
        """
        This simulates viewing the home page and verifies
        that it receives a successful url request
        """
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)

