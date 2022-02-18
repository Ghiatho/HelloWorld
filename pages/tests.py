'''
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
Above is a list of all HTTP responses


'''

from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

