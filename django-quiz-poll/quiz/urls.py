from django.conf.urls import url
from .views import views

app_name = 'quiz'

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='categories'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^(?P<category_id>\d+)/topics/$', views.topic_list, name='topics'),
    url(r'^(?P<category_id>\d+)/add_topic/$',
        views.add_topic, name='add_topic'),
    url(r'^(?P<category_id>\d+)/(?P<topic_id>\d+)/add_question_and_answers/$',
        views.add_question_and_answers, name='add_question_and_answers'),
    url(r'^(?P<category_id>\d+)/(?P<topic_id>\d+)/$',
        views.answer, name='answer'),
    url(r'^(?P<category_id>\d+)/(?P<topic_id>\d+)/(?P<points>\d+)/result/$',
        views.results, name='results'),
    url(r'^quiz_detail/(?P<topic_id>\d+)/$',
        views.quiz_detail, name='quiz_detail'),
    url(r'^user_quizes/$', views.user_quizes, name='user_quizes'),
    url(r'^user_quizes/delete$', views.delete_quizes, name='delete_quizes'),
]
