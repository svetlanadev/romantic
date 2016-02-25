# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers

register = template.Library()


@register.simple_tag()
def url_edit(obj):
    return 'url'
