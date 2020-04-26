from rest_framework import serializers
from survey.models import Category, Topic, Question, Answer


class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_good']

    def create(self, validated_data):
        obj = Answer.objects.create(**validated_data)
        return obj


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']

    def create(self, validated_data):
        obj = Question.objects.create(**validated_data)
        return obj

class SurveyTopicSerializer(serializers.ModelSerializer):
    questions = SurveyQuestionSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['topic_name', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        topic_obj = Topic.objects.create(**validated_data)

        for question in questions_data:
            question_serializer = SurveyQuestionSerializer(data=question)
            question_serializer.is_valid()
            question_serializer.save(topic_id=topic_obj.id)

        return topic_obj


class SurveySerializer(serializers.ModelSerializer):
    topics = SurveyTopicSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'topics']

    def create(self, validated_data):
        topics_data = validated_data.pop('topics')
        category_obj = Category.objects.create(**validated_data)

        for topic in topics_data:
            topic_serializer = SurveyTopicSerializer(data=topic)
            topic_serializer.is_valid()
            topic_serializer.save(category_id=category_obj.id)

        return category_obj
