# coding: utf-8

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('social_auth_widget.html')
def social_auth_widget():
    return {
        'providers': settings.SOCIAL_AUTH_PROVIDERS,
    }
