from django.conf.urls import url

from . import views

app_name = 'survey'
urlpatterns = [
    url(r'^$', views.categories_list, name='categories'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^(?P<category_id>\d+)/topics/$', views.topic_list, name='topics'),
    url(r'^(?P<category_id>\d+)/add_topic/$',
        views.add_topic, name='add_topic'),
    url(r'^(?P<category_id>\d+)/(?P<topic_id>\d+)/add_question/$',
        views.add_question, name='add_question'),
    url(r'^(?P<category_id>\d+)/(?P<topic_id>\d+)/$',
        views.answer, name='answer'),
    url(r'^survey_detail/(?P<topic_id>\d+)/$',
        views.survey_detail, name='survey_detail'),
    url(r'^user_survey/$', views.user_survey, name='user_survey'),
    url(r'^user_survey/delete$', views.delete_survey, name='delete_survey'),
]
