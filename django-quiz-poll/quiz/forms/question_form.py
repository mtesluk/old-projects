from django import forms
from quiz.models import Question


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_name']
        labels = {'question_name': ''}
