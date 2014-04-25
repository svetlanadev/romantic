# coding=utf-8

from django.conf.urls import patterns, url, include
from hike.views import HikeListView

urlpatterns = patterns('hike.views',
    url(r'^hikes/$', HikeListView.as_view()),
)
