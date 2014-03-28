__author__ = 'k15bh_000'

from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^accounts/login/$', views.login(), name='login'),
    url(r'^accounts/auth/$', views.auth, name='auth'),
    # url(r'^accounts/logout/$', views.logout, name='logout'),
    # url(r'^accounts/loggedin/$', views.loggedin),
    # url(r'^accounts/invalid/$', views.invalid_login),
)