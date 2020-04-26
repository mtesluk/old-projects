from django.test import TestCase
from .jsons_to_tests import full_quiz_dict
from api.serializers import QuizTopicSerializer
from quiz.models import Topic, Question, Answer


class TestQuizTopicSerializer(TestCase):

    def setUp(self):
        self.topic_dict = full_quiz_dict['topics'][0]
        self.topic_obj = Topic.objects.create(
            topic_name=self.topic_dict['topic_name'])

        self.question_dict = self.topic_dict['questions'][0]
        self.question_obj = Question.objects.create(
            question_name=self.question_dict['question_name'],
            topic_id=self.topic_obj.id)

        self.answer_dict = self.question_dict['answers'][0]
        self.answer_obj = Answer.objects.create(
            **self.answer_dict, question_id=self.question_obj.id)

    def test_deserializer_json_to_object(self):
        deserialized_data = QuizTopicSerializer(data=self.topic_dict)
        deserialized_data.is_valid()
        topic_obj = deserialized_data.save()
        self.assertEqual(topic_obj.topic_name, self.topic_dict['topic_name'])
        self.assertEqual(topic_obj.questions.all()[
                         0].question_name, self.question_dict['question_name'])

    def test_serializer_object_to_json(self):
        serialized_data = QuizTopicSerializer(self.topic_obj)
        topic_json = serialized_data.data
        self.assertEqual(self.topic_obj.topic_name, topic_json['topic_name'])
        self.assertEqual(self.question_obj.question_name,
                         topic_json['questions'][0]['question_name'])
