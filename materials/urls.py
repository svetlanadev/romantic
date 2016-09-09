# coding=utf-8

from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^report/$', materials, {'state': 'report'}),
    url(r'^passport/$', materials, {'state': 'passport'}),
    url(r'^art/$', materials, {'state': 'art'}),
    url(r'^doc/$', materials, {'state': 'doc'}),
    url(r'^article/$', materials, {'state': 'article'}),
    url(r'^material_new/$', material_page),
    url(r'^sandbox/$', sandbox),
    url(r'^material_new/(?P<state>\w+)/$', material_new),
    url(r'^material_edit/(?P<material_id>\w+)/$', material_edit, name="material_edit"),
    url(r'^materials/(?P<material_id>\w+)/$', material_detail),
    url(r'^material/category/(?P<category_id>\d+)/$', material_category),
    url(r'^materials/dirs/(?P<dir_id>\w+)/$', material_folder),
    url(r'^material_hidden/(?P<material_id>\w+)/$', material_hidden),
    url(r'^material_delete/(?P<material_id>\w+)/$', material_delete),
]
