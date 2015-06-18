# coding: utf-8

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core import urlresolvers
from django.shortcuts import render_to_response, redirect, render
from django.template import Context
from party.models import Party
from materials.models import Material
from force_blog.models import BlogPost
from power_comments.models import PowerComment

register = template.Library()


@register.simple_tag()
def page_navigation(request):
    partys = Party.objects.exclude(state=0)[:5]
    materials = Material.objects.exclude(state=0)[:5]
    comments = PowerComment.objects.order_by().values('app').distinct()

    print comments
    conversation = []
    for comment in comments:
        app_url = comment['app']
        print app_url
        id_content = ''.join(filter(lambda x: x.isdigit(), app_url))
        print id_content
        if "blog" in app_url:
            obj = BlogPost.objects.get(id=id_content)
            url = obj.title
        elif "materials" in app_url:
            obj = Material.objects.get(id=id_content)
            url = obj.title
        elif "party" in app_url:
            obj = Party.objects.get(id=id_content)
            url = obj.name

        if obj.state != 0:
            print obj.state
            conversation.append(obj)
        else:
            pass


    url = template.loader.get_template("page_navigation/page.html")
    data = {'materials': materials, 
            'partys': partys,
            'conversation': conversation}

    return url.render(Context(data))
