__author__ = 'k15bh_000'

from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',
        # Currently all menus listed here are under namespace 'homepage'

        # /homepage/videotienganh
        url(r'^videotienganh', views.VideoTiengAnhView.as_view(), name='videotienganh'),

        # /homepage/khoahoc
        url(r'^khoahoc', views.KhoahocView.as_view(), name='khoahoc'),

        # /homepage/baihattienganh
        url(r'^baihattienganh', views.BaiHatTiengAnhView.as_view(), name='baihattienganh'),

        # /homepage/tracnghiem
        url(r'^tracnghiem', views.TracNghiemView.as_view(), name='tracnghiem'),

        # /homepage/tailieu
        url(r'^tailieu', views.TaiLieuView.as_view(), name='tailieu'),

        # /homepage/trochoi
        url(r'^trochoi', views.TroChoiView.as_view(), name='trochoi'),
     #   url(r'^$', views.IndexView.as_view(), name='home'),

)