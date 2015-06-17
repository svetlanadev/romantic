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
    blogs = []
    for comment in comments:
        id_content = ''.join(filter(lambda x: x.isdigit(), comment['app']))
        blog = BlogPost.objects.get(id=id_content)
        if blog.state != 0:
            blogs.append(blog)

    url = template.loader.get_template("page_navigation/page.html")
    data = {'materials': materials, 
            'partys': partys, 
            'comments': comments, 
            'blogs': blogs,}

    return url.render(Context(data))
