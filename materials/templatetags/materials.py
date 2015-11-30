# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers

register = template.Library()


# @register.simple_tag()
# def url_materials(obj):
#     url = urlresolvers.reverse('admin:%s_%s_change' % (obj._meta.app_label,
#                                                        obj._meta.module_name),
#                                                        args=[obj.id])
#     return url
