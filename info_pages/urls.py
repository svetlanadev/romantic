# coding=utf-8

from django.conf.urls import url, include
from .views import info_page

urlpatterns = [
    url(r'^page/(?P<page>[\w-]+)/$', info_page, name="info_page"),
]
