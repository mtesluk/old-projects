from django.test import TestCase
from .jsons_to_tests import full_survey_dict
from api.serializers import SurveySerializer
from survey.models import Topic, Question, Category


class TestSurveySerializer(TestCase):

    def setUp(self):
        self.category_obj = Category.objects.create(
            name=full_survey_dict['name'])

        self.topic_dict = full_survey_dict['topics'][0]
        self.topic_obj = Topic.objects.create(
            topic_name=self.topic_dict['topic_name'],
            category_id=self.category_obj.id)

        self.question_dict = self.topic_dict['questions'][0]
        self.question_obj = Question.objects.create(
            **self.question_dict, topic_id=self.topic_obj.id)

    def test_deserializer_json_to_object(self):
        deserialized_data = SurveySerializer(data=full_survey_dict)
        deserialized_data.is_valid()
        obj = deserialized_data.save()
        self.assertEqual(obj.name, full_survey_dict['name'])
        self.assertEqual(obj.topics.all()[0].topic_name, 
                         self.topic_dict['topic_name'])

    def test_serializer_object_to_json(self):
        serialized_data = SurveySerializer(self.category_obj)
        category_json = serialized_data.data
        self.assertEqual(self.category_obj.name, category_json['name'])
        self.assertEqual(self.topic_obj.topic_name,
                         category_json['topics'][0]['topic_name'])
