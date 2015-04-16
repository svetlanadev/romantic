from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic.base import RedirectView

from mezzanine.core.views import direct_to_template
from django.conf import settings
import debug_toolbar


admin.autodiscover()

urlpatterns = i18n_patterns("",
    ("^admin/", include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r"^$", RedirectView.as_view(url='/blog/'), name='home'),
    url(r'^', include('hike.urls')),
    url(r'^', include('profile.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^', include('party.urls')),
    url(r'^', include('force_blog.urls')),
    url(r'^', include('power_comments.urls')),
    url(r'^', include('materials.urls')),
    url(r'^', include('urls_custom')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'', include('social_auth.urls')),
    # url(r'^', include('registration.backends.default.urls')),

    ("^", include("mezzanine.urls")),
)

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
