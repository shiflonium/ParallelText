"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.test.client import RequestFactory
import login
from login.views import user_auth
import unittest
#from mock import patch

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_response(self):
        request = self.factory.get('/login/')
        response = login.views.user_auth(request)
        self.assertEqual(response.status_code, 200)

