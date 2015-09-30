# coding=utf-8

from django.conf.urls import patterns, url, include
from party.views import *

urlpatterns = patterns('party.views',
    url(r'^party/$', PartyListView.as_view()),
    url(r'^party/(?P<pk>\d+)/$', PartyDetailView.as_view()),
    url(r'^party_new/$', 'party_new'),
    url(r'^party/category/(?P<category_id>\d+)/$', PartyPostListViewTag.as_view()),
)
