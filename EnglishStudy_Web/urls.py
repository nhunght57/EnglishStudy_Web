from distutils.command.install import install
from django.conf.urls import patterns, include, url
from django.contrib import admin

from homepage import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EnglishStudy_Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^homepage/', include('homepage.urls',namespace='homepage')),
    url(r'^$',views.IndexView.as_view(), name='index'),


    url(r'^accounts/auth/$', include('homepage.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
