# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers
from django.shortcuts import render_to_response, redirect, render
from django.template import Context
from party.models import Party

register = template.Library()


@register.simple_tag()
def page_navigation(request):
    partys = Party.objects.all()
    if request.path == "/party/":
        url = template.loader.get_template("page_navigation/party.html")
    else:
    	if request.path == "/login/":
    		url = template.loader.get_template("page_navigation/null.html")
    	else:
        	url = template.loader.get_template("page_navigation/page.html")

    return url.render(Context({'partys': partys}))

# ('page_navigation/page.html')
# @register.inclusion_tag('power_comments/comments.html')
# def power_comments(request, app_url):
#     comments = PowerComment.objects.all().filter(app=app_url, state=1)
#     count_comments = comments
#     data = {'comments': comments,
#             'app_url': app_url,
#             'count_comments': count_comments,
#             'request': request}
#     return data
