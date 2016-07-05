# coding=utf-8

from django.conf.urls import url, include
from photo_check.views import *

urlpatterns = [
    url(r'^photo/nomination/(?P<nomination_id>\d+)/$', photo_nomination_view),
    url(r'^photo/competition/$', photo_competition_view),
    url(r'^photo/check/(?P<nomination_id>\d+)/$', photo_check_view),
]
