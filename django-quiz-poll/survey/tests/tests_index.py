from django.urls import reverse, resolve
from django.test import TestCase
from django.test import Client


class TestIndex(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).view_name, 'index')

    def test_index_response(self):
        response = self.client.get(reverse('index'))
        self.assertIn("Home", response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
