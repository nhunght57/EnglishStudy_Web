__author__ = 'k15bh_000'

from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

)