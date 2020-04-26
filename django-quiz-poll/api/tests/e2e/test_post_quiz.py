from django.test import TestCase, Client
from django.urls import reverse
import json
from ..serializers.jsons_to_tests import full_quiz_dict
from quiz.models import Category, Topic, Question, Answer

class TestPostQuizSerializer(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_post_json_correct_response(self):
        response = self.client.post(reverse('api:quiz'), data=json.dumps(full_quiz_dict), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], full_quiz_dict['name'])
        self.assertEqual(response.data['topics'][0]['topic_name'], full_quiz_dict['topics'][0]['topic_name'])
        self.assertEqual(response.data['topics'][0]['questions'][0]['question_name'], 
                         full_quiz_dict['topics'][0]['questions'][0]['question_name'])
        self.assertEqual(response.data['topics'][0]['questions'][0]['answers'][0]['answer'], 
                         full_quiz_dict['topics'][0]['questions'][0]['answers'][0]['answer'])

    def test_post_json_correct_data_in_databasey(self):
        self.client.post(reverse('api:quiz'), data=json.dumps(full_quiz_dict), content_type='application/json')
        database_obj = Category.objects.get(id=1)
        self.assertEqual(database_obj.name, full_quiz_dict['name'])
        self.assertEqual(database_obj.topics.first().topic_name, full_quiz_dict['topics'][0]['topic_name'])
        self.assertEqual(database_obj.topics.first().questions.first().question_name, 
                         full_quiz_dict['topics'][0]['questions'][0]['question_name'])
        self.assertEqual(database_obj.topics.first().questions.first().answers.first().answer, 
                         full_quiz_dict['topics'][0]['questions'][0]['answers'][0]['answer'])   