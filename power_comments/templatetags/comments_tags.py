# coding: utf-8

from django import template
from power_comments.models import PowerComment
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers

register = template.Library()


@register.inclusion_tag('power_comments/comments.html')
def power_comments(request, app_url):
    comments = PowerComment.objects.all().filter(app=app_url, state=1)
    count_comments = comments
    data = {'comments': comments,
            'app_url': app_url,
            'count_comments': count_comments,
            'request': request}
    return data


@register.simple_tag()
def count_power_comments(app_url):
    comments = PowerComment.objects.all().filter(app=app_url, state=1)
    count_power_comments = comments.count()
    return count_power_comments


@register.simple_tag()
def power_url_edit(obj):
    url = urlresolvers.reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                                       obj._meta.module_name),
                                                       args=[obj.id])
    return url
