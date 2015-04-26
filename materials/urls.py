# coding=utf-8

from django.conf.urls import patterns, url, include


urlpatterns = patterns('materials.views',
    url(r'^report/$', 'materials', {'state': 'report'}),
    url(r'^passport/$', 'materials', {'state': 'passport'}),
    url(r'^art/$', 'materials', {'state': 'art'}),
    url(r'^sandbox/$', 'sandbox', {'state': 'sandbox'}),
    url(r'^library/$', 'library'),
    url(r'^material_new/$', 'material_new'),
    url(r'^material_edit/(?P<material_id>\w+)/$', 'material_edit', name="material_edit"),
    url(r'^sandbox_new/$', 'sandbox_new'),
    url(r'^materials/(?P<material_id>\w+)/$', 'material_detail'),
    url(r'^materials/dirs/(?P<dir_id>\w+)/$', 'material_folder'),
    # url(r'^blog/(?P<pk>\d+)/$', BlogPostDetailView.as_view()),
    # url(r'^blog_edit/$', 'blog_edit', name="blog_edit"),
    # url(r'^hidden_blog/$', 'hidden_blog', name='hidden_blog'),
    # url(r'^karma_force_blog/$', 'karma_force_blog', name="karma_force_blog"),
)
