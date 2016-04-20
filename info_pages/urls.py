# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('info_pages.views',
    url(r'^page/(?P<page>[\w-]+)/$', 'info_page', name="info_page"),
)
