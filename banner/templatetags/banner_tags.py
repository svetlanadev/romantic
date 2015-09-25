# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers
from django.shortcuts import render_to_response, redirect, render
from django.template import Context
from party.models import Party
from materials.models import Material
from profile.models import CustomUser
from force_blog.models import BlogPost
from power_comments.models import PowerComment
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.conf import settings

register = template.Library()


@register.simple_tag()
def banner_template(request):

    if '/party/' in request.path:
        if request.path == '/party/':
            banner = 'winter.jpg'
        else:
            return ''
    else:
        banner = 'general.jpg'

    s = '<div id="events-banner" class="fill hidden-print" style="background-image: url(%simages/banners/%s)"><div class="header-cone"></div><div class="header-cone right"></div></div><br>' % (settings.STATIC_URL, banner)
    return s
