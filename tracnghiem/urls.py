__author__ = 'k15bh_000'

from django.conf.urls import patterns, url

from tracnghiem import views

urlpatterns = patterns('',

    # /tracnghiem/
    url(r'^$', views.TracNghiemView.as_view(), name='index'),

    # /tracnghiem/post/
    url(r'^post', 'tracnghiem.views.post', name='post'),

    )