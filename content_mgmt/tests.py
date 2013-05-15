"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
import unittest
from django.test.client import RequestFactory
from content_mgmt.views import upload
from content_mgmt.forms import UploadForm
class TestContentManager(TestCase):
    def setUp(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.factory=RequestFactory()

    def test_upload_response(self):
        """
        This simulates a login and verifies
        that it receives a successful url request
        """
        request = self.factory.post('/upload/', POST={
                'language':"DE",
                'title':"dummy",
                'file':"dummyfile.txt"
                })
        response = upload(request)
        self.assertEqual(response.status_code, 200)

