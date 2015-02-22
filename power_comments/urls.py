# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('power_comments.views',
    url(r'^new_power_comment/$', 'new_power_comment', name="new_power_comment"),
    url(r'^karma_power_comments/$',
        'karma_power_comments',
        name="karma_power_comments"),
    url(r'^disable_power_comments/$',
        'disable_power_comments',
        name="disable_power_comments"),
    url(r'^ajax_test/$', 'ajax_test'),
    url(r'^ajax_karma_minus/$', 'ajax_karma_minus'),
    url(r'^ajax_karma_plus/$', 'ajax_karma_plus'),
)
