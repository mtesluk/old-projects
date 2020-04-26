from django.conf.urls import url
from django.contrib.auth import views as view
from .views import views


app_name = 'account'
urlpatterns = [
    url(r'^login/$', view.login,
        {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout/$', view.logout,
        {'template_name': 'user/logout.html'}, name='logout'),
    url(r'^logout_then_login/$',
        view.logout_then_login,
        name='logout_then_login'),
    url(r'^password_change/$', view.password_change,
        {'post_change_redirect': 'account:password_change_done',
            'template_name': 'user/password_change.html'},
        name='password_change'),
    url(r'^password_change/done/$', views.password_change_done,
        name='password_change_done'),
    url(r'^password_reset/$', view.password_reset,
        {'post_reset_redirect': 'account:password_reset_done',
            'template_name': 'user/password_reset.html'},
        name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done,
        name='password_reset_done'),
    url(r'^password_reset/complete/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        views.password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset/confirm/$', view.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^registration/$', views.register, name='register'),
]
