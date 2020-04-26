from django.test import TestCase, Client
from django.urls import reverse
import json
from ..serializers.jsons_to_tests import full_survey_dict
from survey.models import Category, Topic, Question

class TestPostSurveySerializer(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_post_json_correct_response(self):
        response = self.client.post(reverse('api:survey'), data=json.dumps(full_survey_dict), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], full_survey_dict['name'])
        self.assertEqual(response.data['topics'][0]['topic_name'], full_survey_dict['topics'][0]['topic_name'])
        self.assertEqual(response.data['topics'][0]['questions'][0]['question'], 
                         full_survey_dict['topics'][0]['questions'][0]['question'])

    def test_post_json_correct_data_in_database(self):
        self.client.post(reverse('api:survey'), data=json.dumps(full_survey_dict), content_type='application/json')
        database_obj = Category.objects.get(id=1)
        self.assertEqual(database_obj.name, full_survey_dict['name'])
        self.assertEqual(database_obj.topics.first().topic_name, full_survey_dict['topics'][0]['topic_name'])
        self.assertEqual(database_obj.topics.first().questions.first().question, 
                         full_survey_dict['topics'][0]['questions'][0]['question'])