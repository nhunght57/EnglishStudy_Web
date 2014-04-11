__author__ = 'k15bh_000'

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

                       # /accounts/login/
                       url(r'^auth/', 'accounts.views.auth', name='auth'),

                       # /accounts/logout/
                       url(r'^logout/', 'accounts.views.logout_view', name='logout'),

)