# coding=utf-8

from django.conf.urls import patterns, url, include


urlpatterns = patterns('materials.views',
    url(r'^materials/$', 'material_list'),
    # url(r'^report/$', 'material_report'),
    # url(r'^passport/$', 'material_passport'),
    # url(r'^art/$', 'material_art'),
    url(r'^material_new/$', 'material_new'),
    url(r'^materials/(?P<material_id>\w+)/$', 'material_detail'),
    url(r'^materials/dirs/(?P<dir_id>\w+)/$', 'material_folder'),
    # url(r'^blog/(?P<pk>\d+)/$', BlogPostDetailView.as_view()),
    # url(r'^blog_edit/$', 'blog_edit', name="blog_edit"),
    # url(r'^hidden_blog/$', 'hidden_blog', name='hidden_blog'),
    # url(r'^karma_force_blog/$', 'karma_force_blog', name="karma_force_blog"),
)
