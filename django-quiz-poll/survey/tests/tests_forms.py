from django.urls import reverse, resolve
from django.test import TestCase
from ..models import *
from ..forms import *


class TestForms(TestCase):

    def test_add_category(self):
        data_correct = {'name': 'Animal'}
        data_incorrect = {'names': '12'}
        form_correct = AddCategoryForm(data=data_correct)
        form_incorrect = AddCategoryForm(data=data_incorrect)

        self.assertTrue(form_correct.is_valid())
        self.assertFalse(form_incorrect.is_valid())

        category = form_correct.save(commit=False)
        self.assertEqual(category.name, 'Animal')

    def test_add_topic(self):
        data_correct = {'topic_name': 'Animal...'}
        data_incorrect = {'name': '12'}
        form_correct = AddTopicForm(data=data_correct)
        form_incorrect = AddTopicForm(data=data_incorrect)

        self.assertTrue(form_correct.is_valid())
        self.assertFalse(form_incorrect.is_valid())

        topic = form_correct.save(commit=False)
        self.assertEqual(topic.topic_name, 'Animal...')

    def test_add_question(self):
        data_correct = {'question': 'What is yours favourite animal?'}
        data_incorrect = {'name': '12'}
        form_correct = AddQuestionForm(data=data_correct)
        form_incorrect = AddQuestionForm(data=data_incorrect)

        self.assertTrue(form_correct.is_valid())
        self.assertFalse(form_incorrect.is_valid())

        question = form_correct.save(commit=False)
        self.assertEqual(question.question, 'What is yours favourite animal?')

    def test_save_answer(self):
        data_correct = {'answer': 'Dog'}
        data_incorrect = {'answers': '12'}
        form_correct = SaveAnswerForm(data=data_correct)
        form_incorrect = SaveAnswerForm(data=data_incorrect)

        self.assertTrue(form_correct.is_valid())
        self.assertFalse(form_incorrect.is_valid())

        answer = form_correct.save(commit=False)
        self.assertEqual(answer.answer, 'Dog')
