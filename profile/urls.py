# coding=utf-8

from django.conf.urls import patterns, url, include
from profile.views import ProfileListView, ProfileDetailView

urlpatterns = patterns('profile.views',
    url(r'^profile/$', ProfileListView.as_view()),
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetailView.as_view()),
    url(r'^government/$', 'government', name='government'),
)
