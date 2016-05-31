# coding=utf-8

from django.conf.urls import url, include
from hike.views import HikeListView, HikeDetailView

urlpatterns = [
	url(r'^hikes/$', HikeListView.as_view()),
    url(r'^hikes/(?P<pk>\d+)/$', HikeDetailView.as_view())
]
