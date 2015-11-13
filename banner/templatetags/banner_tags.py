# coding: utf-8

from django import template
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from info_pages.models import InfoPage
from banner.models import BannerTitle
import re

register = template.Library()


@register.simple_tag()
def banner_template(request):
    path_banner = BannerTitle.objects.filter(text_author=request.path)[:1]

    if path_banner:
        banner = str(settings.MEDIA_URL) + str(path_banner[0].image)

    else:
        banner = str(settings.STATIC_URL) + 'images/banners/general.jpg'

    s = '<div id="events-banner" class="fill hidden-print" style="background-image: url(%s)"><div class="header-cone"></div><div class="header-cone right"></div></div><br>' % (banner)
    return s
