from django.test import TestCase

from ..models import *


class TestModels(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Sport")
        self.topic = Topic.objects.create(
            topic_name="Lewandowski", category=self.category)
        self.quesiton = Question.objects.create(
            quesiton="How old is he?", topic=self.topic)
        self.answer = Answer.objects.create(
            answer="21", quesiton=self.quesiton)

    def test_category(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

        categories = Category.objects.all()

        self.assertEqual(categories.count(), 1)

    def test_category(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

        categories = Category.objects.all()

        self.assertEqual(categories.count(), 1)
