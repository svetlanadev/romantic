# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('power_comments.views',
    url(r'^new_power_comment/$', 'new_power_comment', name="new_power_comment"),
    url(r'^karma_power_comments/$', 'karma_power_comments', name="karma_power_comments"),
)
