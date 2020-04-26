from django import forms
from survey.models import Topic


class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']
        labels = {'topic_name': ''}
