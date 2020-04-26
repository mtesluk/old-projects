from django.db import models
from .topic import Topic


class Question(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='questions', null=True)
    question_name = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.question_name
