from django.db import models
from .question import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", null=True)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.answer
