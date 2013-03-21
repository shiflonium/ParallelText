"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.test.client import RequestFactory
import register
from register.views import user_reg
import unittest
#from mock import patch

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_response(self):
        request = self.factory.get('/register/')
        response = register.views.user_reg(request)
        self.assertEqual(response.status_code, 200)

    def test_newuser(self):
        request = self.factory.post('/register/', POST={
            'username': 'dummyuser',
            'password1': 'dummypass',
            'password2': 'dummypass',
            })
        response = register.views.user_reg(request)
        self.assertEqual(response.status_code, 200)

