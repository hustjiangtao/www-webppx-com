from django.test import TestCase
from django.conf import settings

# Create your tests here.


class DeployTest(TestCase):
    def test_admin(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/console/')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_config(self):
        self.assertEqual(settings.DEBUG, False)
