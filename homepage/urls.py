__author__ = 'k15bh_000'

from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',

        url(r'^videotienganh', views.VideoTiengAnhView.as_view(), name='videotienganh'),
        url(r'^khoahoc', views.KhoahocView.as_view(), name='khoahoc'),
        url(r'^baihattienganh', views.BaiHatTiengAnhView.as_view(), name='baihattienganh'),
        url(r'^tracnghiem', views.TracNghiemView.as_view(), name='tracnghiem'),
        url(r'^tailieu', views.TaiLieuView.as_view(), name='tailieu'),
        url(r'^trochoi', views.TroChoiView.as_view(), name='trochoi'),
     #   url(r'^$', views.IndexView.as_view(), name='home'),

)