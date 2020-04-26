from django.test import TestCase
from .jsons_to_tests import full_quiz_dict
from api.serializers import QuizAnswerSerializer
from quiz.models import Answer


class TestQuizAnswerSerializer(TestCase):

    def setUp(self):
        self.answer_dict = full_quiz_dict['topics'][0]['questions'][0]['answers'][0]
        Answer.objects.create(**self.answer_dict)

    def test_deserializer_json_to_object(self):
        deserialized_data = QuizAnswerSerializer(data=self.answer_dict)
        deserialized_data.is_valid()
        answer_obj = deserialized_data.save()
        self.assertEqual(answer_obj.answer, self.answer_dict['answer'])
        self.assertEqual(answer_obj.is_good, self.answer_dict['is_good'])

    def test_serializer_object_to_json(self):
        obj = Answer.objects.first()
        serialized_data = QuizAnswerSerializer(obj)
        answer_json = serialized_data.data
        self.assertEqual(obj.answer, answer_json['answer'])
