# coding=utf-8

from django.conf.urls import patterns, url, include
from government.views import GovernmentListView, GovernmentDetailView

urlpatterns = patterns('government.views',
    url(r'^team/$', GovernmentListView.as_view()),
    url(r'^team/(?P<pk>\d+)/$', GovernmentDetailView.as_view())
)
