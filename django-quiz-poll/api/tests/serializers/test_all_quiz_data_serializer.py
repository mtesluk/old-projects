from django.test import TestCase
from .jsons_to_tests import full_quiz_dict
from api.serializers import QuizSerializer
from quiz.models import Category, Topic, Question, Answer


class TestQuizSerializer(TestCase):
    def setUp(self):
        self.category_obj = Category.objects.create(
            name=full_quiz_dict['name'])

        self.topic_dict = full_quiz_dict['topics'][0]
        self.topic_obj = Topic.objects.create(
            topic_name=self.topic_dict['topic_name'],
            category_id=self.category_obj.id)

        self.question_dict = self.topic_dict['questions'][0]
        self.question_obj = Question.objects.create(
            question_name=self.question_dict['question_name'],
            topic_id=self.topic_obj.id)

        self.answer_dict = self.question_dict['answers'][0]
        self.answer_obj = Answer.objects.create(
            **self.answer_dict, question_id=self.question_obj.id)

    def test_deserializer_json_to_object(self):
        deserialized_data = QuizSerializer(data=full_quiz_dict)
        deserialized_data.is_valid()
        obj = deserialized_data.save()
        self.assertEqual(obj.name, full_quiz_dict['name'])
        self.assertEqual(obj.topics.all()[
                         0].topic_name, self.topic_dict['topic_name'])

    def test_serializer_object_to_json(self):
        serialized_data = QuizSerializer(self.category_obj)
        full_json = serialized_data.data
        self.assertEqual(self.category_obj.name, full_json['name'])
        self.assertEqual(self.topic_obj.topic_name,
                         full_json['topics'][0]['topic_name'])
