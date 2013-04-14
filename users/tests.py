"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.test.client import RequestFactory
import unittest
from users.views import user_reg, user_auth
#from mock import patch

class TestRegister(unittest.TestCase):
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

    def test_register_response(self):
        """
        This simulates a registration and verifies
        that it receives a successful url request
        """
        request = self.factory.get('/register/')
        response = user_reg(request)
        self.assertEqual(response.status_code, 200)

    def test_new_user(self):
        """
        This simulates the creation of a new user and verifies
        that it receives a successful url request
        """
        request = self.factory.post('/register/', POST={
            'username': 'dummyuser',
            'password1': 'dummypass',
            'password2': 'dummypass',
            })
        response = user_reg(request)
        self.assertEqual(response.status_code, 200)

class TestLogin(unittest.TestCase):
    """
    This class is used to test the login module
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

    def test_login_response(self):
        """
        This simulates a login and verifies
        that it receives a successful url request
        """
        request = self.factory.get('/login/')
        response = user_auth(request)
        self.assertEqual(response.status_code, 200)

    def test_existing_user(self):
        """
        This simulates the login of an existing user and
        verifies that it receives a successful url request
        """
        request = self.factory.post('/login/', POST={
            'username': 'dummyuser',
            'password': 'dummypass',
            })
        response = user_auth(request)
        self.assertEqual(response.status_code, 200)

