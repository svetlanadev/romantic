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
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import re


register = template.Library()


@register.simple_tag()
def page_navigation(request):
    partys = Party.objects.prefetch_related('category').filter(date_start__gt=datetime.now()).exclude(state=0)[:3]

    try:
        materials = Material.objects.filter(state=1)[:5]
    except ObjectDoesNotExist:
        materials = ''

    apps = []

    url = template.loader.get_template("page_navigation/page.html")
    data = {'materials': materials,
            'partys': partys,
            'request': request}

    return url.render(Context(data))


@register.simple_tag()
def sandbox_user_count(request):
    if request.user.is_authenticated():
        try:
            custom_user = CustomUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            custom_user = request.user

        materials = Material.objects.filter(owner=custom_user, state=0)
    else:
        materials = ""

    return materials.count()


@register.simple_tag()
def get_active_users():
    url = template.loader.get_template("page_navigation/active_users.html")
    data = {'active_users': 'active_users'}
    return url.render(Context(data))


@register.simple_tag()
def get_profile_template(request):
    if request.user.is_authenticated():
        try:
            custom_user = CustomUser.objects.get(user=request.user)
        except TypeError:
            custom_user = request.user
    else:
        custom_user = request.user

    url = template.loader.get_template("page_navigation/profile.html")
    data = {'custom_user': custom_user,
            'request': request}
    return url.render(Context(data))


@register.simple_tag()
def get_tokenize_template():
    from django.conf import settings
    return '<link href="%scss/jquery.tokenize.min.css" rel="stylesheet" type="text/css">' % (settings.STATIC_URL)


@register.simple_tag()
def get_tokenize_template_js():
    from django.conf import settings
    return '<script src="%sjs/jquery.tokenize.js" type="text/javascript"></script>' % (settings.STATIC_URL)
