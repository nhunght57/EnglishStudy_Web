from django.conf.urls import patterns, include, url
from django.contrib import admin

from EnglishStudy_Web import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EnglishStudy_Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='home'),

    # /tracnghiem
    url(r'^tracnghiem/', include('tracnghiem.urls', namespace='tracnghiem')),

    # /accounts
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # /polls - example polls application
    url(r'^polls/', include('polls.urls', namespace='polls')),

    # /admin - Django built-in interactive Admin page
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

