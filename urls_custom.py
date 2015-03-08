# coding=utf-8

from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^contact-only/$', TemplateView.as_view(template_name="contact-only.html")),
)
