"""
This file tests the functionality of 
the login module
"""

#from django.test import TestCase
from django.test.client import RequestFactory
from login.views import user_auth
import unittest
#from mock import patch

class TestLogin(unittest.TestCase):
    """
    This class is used to test the login module
    """
    def setup(self):
        """
        This sets up the test of the login module
        """
        self.factory = RequestFactory()

    def test_response(self):
        """ 
        This tests to see whether the login page 
        can be reached without error
        """
        request = self.factory.get('/login/')
        response = user_auth(request)
        self.assertEqual(response.status_code, 200)

