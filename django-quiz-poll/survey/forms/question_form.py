from django import forms
from survey.models import Question


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        labels = {'question': ''}
