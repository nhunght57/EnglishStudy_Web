__author__ = 'k15bh_000'

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

                       # /accounts/auth/
                       url(r'^auth/', 'accounts.views.auth', name='auth'),

                       # /accounts/logout/
                       url(r'^logout/', 'accounts.views.logout_view', name='logout'),

                       # /accounts/detail/
                       url(r'^detail/', 'accounts.views.account_detail', name='detail'),

                       # /accounts/login/
                       url(r'^login', 'accounts.views.login_view', name='login'),

)