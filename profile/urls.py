# coding=utf-8

from django.conf.urls import patterns, url, include
from profile.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('profile.views',
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^profile/(?P<profile_id>\d+)/$', 'profile', name='profile'),
    url(r'^profile_block/(?P<profile_id>\d+)/$', 'profile_block', name='profile_block'),
    url(r'^password_change/$', 'password_change', name='password_change'),
    url(r'^restart_password/$', 'restart_password', name='restart_password'),
    url(r'^profile_edit/$', 'profile_edit', name='profile_edit'),
    url(r'^password_change/done$', TemplateView.as_view(template_name="password_change_done.html")),
    # url(r'^password_reset/$', 'password_reset', name='password_reset'),
    # url(r'^password_reset/done/$', 'password_reset_done', name='password_reset_done'),
    url(r'^government/$', 'government', name='government'),
    url(r'^signup/activate/(?P<value>[\w-]+)', 'complete_registration'),
    url(r'^registration_complete/$', TemplateView.as_view(template_name="registration_complete.html")),
    url(r'^restart_password_done/$', TemplateView.as_view(template_name="restart_password_done.html")),
)
