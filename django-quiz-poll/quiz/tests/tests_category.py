from django.urls import reverse, resolve
from django.test import TestCase
from django.test import Client
from ..models import *
from ..forms import *


class TestsurveyCategories(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Sport", get_count=0)

    def test_categories_url(self):
        path = reverse('quiz:categories')
        self.assertEqual(resolve(path).view_name, 'quiz:categories')

    def test_categories_response(self):
        response = self.client.get(reverse('quiz:categories'))
        self.assertIn(b"Quiz", response.content)
        self.assertEqual(response.status_code, 200)

    def test_category_amount(self):
        response = self.client.get(reverse('quiz:categories'))
        category_amount = Category.objects.all().count()
        self.assertEqual(len(response.context["categories"]), category_amount)

    def test_model(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_add_category(self):
        data_correct = {'name': 'Animal'}
        data_incorrect = {'lol': '12'}
        form_correct = AddCategoryForm(data=data_correct)
        form_incorrect = AddCategoryForm(data=data_incorrect)
        self.assertTrue(form_correct.is_valid())
        self.assertFalse(form_incorrect.is_valid())

    def tearDown(self):
        pass
