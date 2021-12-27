from django.test import TestCase, SimpleTestCase

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

# Create your tests here.
