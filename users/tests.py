"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.test.client import RequestFactory
import unittest
import users
#from mock import patch

class TestRegister(unittest.TestCase):
    """
    This class is used to test the register module
    """
    def setup(self):
        """
        this function prepares the module for testing
        """
        self.factory = RequestFactory()

    def test_register_response(self):
        """
        This simulates a registration and verifies
        that it receives a successful url request
        """
        request = self.factory.get('/register/')
        response = users.views.user_reg(request)
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
        response = users.views.user_reg(request)
        self.assertEqual(response.status_code, 200)

    def test_login_response(self):
        """
        This simulates a login and verifies
        that it receives a successful url request
        """
        request = self.factory.get('/login/')
        response = users.views.user_auth(request)
        self.assertEqual(response.status_code, 200)

    def test_existing_user(self):
        """
        This simulates the login of an existing user and
        verifies that it receives a successful url request
        """
        request = self.factory.post('/login/', POST={
            'username': 'dummyuser',
            'password1': 'dummypass',
            'password2': 'dummypass',
            })
        response = users.views.user_auth(request)
        self.assertEqual(response.status_code, 200)

