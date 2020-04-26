from django.conf.urls import url

from .views import api_info, QuizView, SurveyView

app_name = 'api'
urlpatterns = [
    url(r'^$', api_info, name='api_info'),
    url(r'^survey/$', SurveyView.as_view(), name='survey'),
    url(r'^quiz/$', QuizView.as_view(), name='quiz'),
]
