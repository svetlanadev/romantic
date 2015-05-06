# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers
from django.shortcuts import render_to_response, redirect, render
from django.template import Context
from party.models import Party
from materials.models import Material
from power_comments.models import PowerComment

register = template.Library()


@register.simple_tag()
def page_navigation(request):
    partys = Party.objects.all()[:5]
    materials = Material.objects.exclude(state=0)[:5]
    comments = PowerComment.objects.order_by().values('app').distinct()
    url = template.loader.get_template("page_navigation/page.html")
    data = {'materials': materials, 'partys': partys, 'comments': comments}

    return url.render(Context(data))
