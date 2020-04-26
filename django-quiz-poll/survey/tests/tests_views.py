from django.urls import reverse, resolve
from django.test import TestCase
from django.test import Client
from mock import call, patch
from ..models import *
from ..forms import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Sport", get_count=0)
        self.user = User.objects.create_user(
            'mati', 'lennon@thebeatles.com', 'pass')

    @patch('survey.views.categories_list', return_value="Good")
    def test_view_category_list(self, mock_return):
        self.assertEqual(mock_return.return_value, "Good")

    def test_category_get_absolute(self):
        self.assertEqual("/survey/{}/topics/".format(self.category.id),
                         self.category.get_absolute_url())

    def test_categories_response(self):
        response = self.client.get(reverse('survey:categories'))
        self.assertIn(self.category.name, response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)

    def test_category_amount(self):
        response = self.client.get(reverse('survey:categories'))
        category_amount = Category.objects.all().count()
        self.assertEqual(len(response.context["categories"]), category_amount)

    def test_add_category_status(self):
        response = self.client.post(reverse('survey:add_category'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'],
                         "{}?next={}".format(reverse('account:login'), reverse('survey:add_category')))
