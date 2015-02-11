# coding=utf-8

from django.conf.urls import patterns, url, include
from force_blog.views import BlogPostListView, BlogPostDetailView

urlpatterns = patterns('force_blog.views',
    url(r'^blog/$', BlogPostListView.as_view()),
    url(r'^blog/(?P<pk>\d+)/$', BlogPostDetailView.as_view()),
    url(r'^blog_edit/$', 'blog_edit', name="blog_edit"),
    url(r'^hidden_blog/$', 'hidden_blog', name='hidden_blog'),
    url(r'^karma_force_blog/$', 'karma_force_blog', name="karma_force_blog"),
)
