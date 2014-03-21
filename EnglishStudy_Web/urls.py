from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EnglishStudy_Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('homepage.urls', namespace='')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
