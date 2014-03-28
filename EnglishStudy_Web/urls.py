from django.conf.urls import patterns, include, url
from django.contrib import admin

from homepage import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EnglishStudy_Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='homepage'),
    url(r'^khoahoc/$', views.KhoahocView.as_view(), name='khoahoc'),
    url(r'^tracnghiem/$', views.TracNghiemView.as_view(), name='tracnghiem'),

    url(r'^accounts/auth/$', include('homepage.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
