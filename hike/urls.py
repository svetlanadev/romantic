# coding=utf-8

from django.conf.urls import patterns, url, include
from hike.views import HikeListView, HikeDetailView

urlpatterns = patterns('hike.views',
    url(r'^hikes/$', HikeListView.as_view()),
    url(r'^hikes/(?P<pk>\d+)/$', HikeDetailView.as_view())
)
