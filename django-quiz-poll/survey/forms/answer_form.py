from django import forms
from survey.models import Answer


class SaveAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        labels = {'answer': ''}
