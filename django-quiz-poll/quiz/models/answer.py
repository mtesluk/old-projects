from django.db import models
from .question import Question


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', null=True)
    answer = models.CharField(max_length=500)
    is_good = models.BooleanField(default=False)
    picked = models.IntegerField(default=0)

    def __str__(self):
        return self.answer

    # def check_if_correct(self):
    #     if self.is_good == True:
    #         self.question.topic
