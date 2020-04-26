from django.test import TestCase
from .jsons_to_tests import full_survey_dict
from api.serializers import SurveyQuestionSerializer
from survey.models import Question


class TestQuestionSerializer(TestCase):

    def setUp(self):
        self.question_dict = full_survey_dict['topics'][0]['questions'][0]
        Question.objects.create(**self.question_dict)

    def test_deserializer_json_to_object(self):
        deserialized_data = SurveyQuestionSerializer(data=self.question_dict)
        deserialized_data.is_valid()
        question_obj = deserialized_data.save()
        self.assertEqual(question_obj.question, self.question_dict['question'])

    def test_serializer_object_to_json(self):
        obj = Question.objects.first()
        serialized_data = SurveyQuestionSerializer(obj)
        question_json = serialized_data.data
        self.assertEqual(obj.question, question_json['question'])
