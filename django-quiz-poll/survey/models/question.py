from django.db import models
from .topic import Topic


class Question(models.Model):
    topic = models.ForeignKey(Topic, related_name="questions", null=True)
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question
