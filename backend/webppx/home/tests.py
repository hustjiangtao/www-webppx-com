from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):
    def test_home(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
