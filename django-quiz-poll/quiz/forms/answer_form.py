from django import forms
from quiz.models import Answer


class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'is_good']
        labels = {'answer': '', 'is_good': ''}
