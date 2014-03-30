from django.conf.urls import patterns, include, url
from django.contrib import admin

from homepage import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EnglishStudy_Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # Every menu is put under /homepage (should we let it or not?)
    url(r'^homepage/', include('homepage.urls', namespace='homepage')),

    # Main homepage
    url(r'^$',views.IndexView.as_view(), name='index'),

    # /accounts/auth - authentication system
    # maybe we should put it in namespace 'accounts' later
    url(r'^accounts/auth/$', 'homepage.views.auth'),


    # /polls - example polls application
    url(r'^polls/', include('polls.urls', namespace='polls')),

    # /admin - Django built-in interactive Admin page
    url(r'^admin/', include(admin.site.urls)),
)
