from django.test import TestCase
from .jsons_to_tests import full_quiz_dict
from api.serializers import QuizQuestionSerializer
from quiz.models import Question, Answer


class TestQuizQuestionSerializer(TestCase):

    def setUp(self):
        self.question_dict = full_quiz_dict['topics'][0]['questions'][0]
        self.question_obj = Question.objects.create(
            question_name=self.question_dict['question_name'])

        self.answer_dict = self.question_dict['answers'][0]
        self.answer_obj = Answer.objects.create(
            **self.answer_dict, question_id=self.question_obj.id)

    def test_deserializer_json_to_object(self):
        deserialized_data = QuizQuestionSerializer(data=self.question_dict)
        deserialized_data.is_valid()
        question_obj = deserialized_data.save()
        self.assertEqual(question_obj.question_name,
                         self.question_dict['question_name'])
        self.assertEqual(question_obj.answers.all()[
                         0].answer, self.answer_dict['answer'])

    def test_serializer_object_to_json(self):
        serialized_data = QuizQuestionSerializer(self.question_obj)
        question_json = serialized_data.data
        self.assertEqual(self.question_obj.question_name,
                         question_json['question_name'])
        self.assertEqual(self.answer_obj.answer,
                         question_json['answers'][0]['answer'])
