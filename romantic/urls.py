# coding=utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^factory/', include(admin.site.urls)),
    url(r'^', include('force_blog.urls')),
    url(r'^', include('materials.urls')),
    url(r'^', include('hike.urls')),
    url(r'^', include('profile.urls')),
    url(r'^', include('party.urls')),
    url(r'^', include('info_pages.urls')),
    # url(r'^', include('photo_check.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^contacts/$', TemplateView.as_view(template_name="contacts.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
]

# urlpatterns += [
# ]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
# python -m smtpd -n -c DebuggingServer localhost:1025
