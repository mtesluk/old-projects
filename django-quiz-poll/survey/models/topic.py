from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .category import Category


class Topic(models.Model):
    category = models.ForeignKey(Category, related_name="topics", null=True)
    user = models.ForeignKey(
        User, related_name="user_survey_topics", null=True)
    topic_name = models.CharField(max_length=100)
    get_count = models.IntegerField(default=0)

    def __str__(self):
        return self.topic_name

    def get_absolute_url(self):
        return reverse('survey:answer', kwargs={
                       'category_id': self.category.id, 'topic_id': self.id})
