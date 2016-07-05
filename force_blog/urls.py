# coding=utf-8

from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', BlogPostListView.as_view()),
    url(r'^blog/$', BlogPostListView.as_view()),
    url(r'^blog/(?P<pk>\d+)/$', blog_detail),
    url(r'^blog_edit/(?P<blog_id>\w+)/$', blog_edit, name="blog_edit"),
    url(r'^blog_new/$', blog_new, name='blog_new'),
    url(r'^blog_hidden/(?P<action>\w+)/(?P<blog_id>\w+)/$', blog_hidden, name='blog_hidden'),
    url(r'^arhive_news/$', BlogPostArhiveListView.as_view()),
    url(r'^blog/category/(?P<category_id>\d+)/$', BlogPostListViewTag.as_view()),
]
