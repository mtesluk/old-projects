from rest_framework import serializers
from quiz.models import Category, Topic, Question, Answer


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_good']

    def create(self, validated_data):
        obj = Answer.objects.create(**validated_data)
        return obj


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question_name', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question_obj = Question.objects.create(**validated_data)

        for answer in answers_data:
            answer_serializer = QuizAnswerSerializer(data=answer)
            answer_serializer.is_valid()
            answer_serializer.save(question_id=question_obj.id)

        return question_obj


class QuizTopicSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['topic_name', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        topic_obj = Topic.objects.create(**validated_data)

        for question in questions_data:
            question_serializer = QuizQuestionSerializer(data=question)
            question_serializer.is_valid()
            question_serializer.save(topic_id=topic_obj.id)

        return topic_obj


class QuizSerializer(serializers.ModelSerializer):
    topics = QuizTopicSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'topics']

    def create(self, validated_data):
        topics_data = validated_data.pop('topics')
        category_obj = Category.objects.create(**validated_data)

        for topic in topics_data:
            topic_serializer = QuizTopicSerializer(data=topic)
            topic_serializer.is_valid()
            topic_serializer.save(category_id=category_obj.id)

        return category_obj
