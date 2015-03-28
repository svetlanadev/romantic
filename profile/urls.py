# coding=utf-8

from django.conf.urls import patterns, url, include
from profile.views import *

urlpatterns = patterns('profile.views',
	url(r'^register/$', RegisterFormView.as_view()),
	url(r'^login/$', LoginFormView.as_view()),
	url(r'^logout/$', LogoutView.as_view()),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetailView.as_view()),
    url(r'^government/$', 'government', name='government'),
)
