# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers
from django.shortcuts import render_to_response, redirect, render
from django.template import Context
from info_pages.models import InfoPage
from materials.models import Material
from profile.models import CustomUser
from force_blog.models import BlogPost
from power_comments.models import PowerComment
from django.core.exceptions import ObjectDoesNotExist
import re
from django.conf import settings

register = template.Library()


@register.simple_tag()
def banner_template(request):
    path = request.path

    if '/party/' in path:
        if path == '/party/':
            banner = str(settings.STATIC_URL) + 'images/banners/winter.jpg'
        else:
            return ''
    elif '/page/' in path:
        # IF REQUEST PATH =  "/page/history", WE GET "history"
        link = re.split(r'/', path)[2]
        page = InfoPage.objects.get(url_link=link)
        try:
            banner = str(settings.MEDIA_URL) + str(page.banner.image)
        except AttributeError:
            banner = str(settings.STATIC_URL) + 'images/banners/general.jpg'

    else:
        banner = str(settings.STATIC_URL) + 'images/banners/general.jpg'

    s = '<div id="events-banner" class="fill hidden-print" style="background-image: url(%s)"><div class="header-cone"></div><div class="header-cone right"></div></div><br>' % (banner)
    return s
