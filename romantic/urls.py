# coding=utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

import debug_toolbar

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='blog/'), name='blog'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^history/$', TemplateView.as_view(template_name="history.html")),
    url(r'^rules/$', TemplateView.as_view(template_name="rules.html")),
    url(r'^contact-only/$', TemplateView.as_view(template_name="contact-only.html")),

    url(r'^', include('hike.urls')),
    url(r'^', include('profile.urls')),
    url(r'^', include('party.urls')),
    url(r'^', include('force_blog.urls')),
    url(r'^', include('power_comments.urls')),
    url(r'^', include('info_pages.urls')),
    url(r'^', include('materials.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
