# coding=utf-8

from django.conf.urls import patterns, url, include
from profile.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('profile.views',
	url(r'^register/$', RegisterFormView.as_view()),
	url(r'^login/$', LoginFormView.as_view()),
	url(r'^logout/$', LogoutView.as_view()),
    url(r'^profile/(?P<profile_id>\d+)/$', 'profile', name='profile'),
    url(r'^profile_edit/$', 'profile_edit', name='profile_edit'),
    # url(r'^profile/(?P<pk>\d+)/$', ProfileDetailView.as_view()),
    url(r'^government/$', 'government', name='government'),
    url(r'^registration_complete/$', TemplateView.as_view(template_name="registration_complete.html")),
)