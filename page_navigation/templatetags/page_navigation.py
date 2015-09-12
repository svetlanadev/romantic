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

register = template.Library()

@register.simple_tag()
def page_navigation(request):
    partys = Party.objects.exclude(state=0)[:5]
    materials = Material.objects.exclude(state=0)[:5]

    comments_active_users = PowerComment.objects.values('owner').distinct()
    comments_active_users_count = comments_active_users.count() - 8
    try:
        comments_active_users = comments_active_users[comments_active_users_count:]
    except AssertionError:
        pass

    active_users = []
    for x in comments_active_users:
        active_user = CustomUser.objects.get(id=x['owner'])
        active_users.append(active_user)

        if len(active_users) >= 8:
            break

    comments = PowerComment.objects.values('app').distinct()
    comments_count = comments.count() - 5
    try:
        comments = comments[comments_count:]
    except AssertionError:
        pass

    conversation = []
    for comment in comments:
        app_url = comment['app']
        id_content = ''.join(filter(lambda x: x.isdigit(), app_url))
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
            conversation.append(obj)
        else:
            pass

        if len(conversation) >= 5:
            break


    conversation.reverse()
    url = template.loader.get_template("page_navigation/page.html")
    data = {'materials': materials, 
            'partys': partys,
            'conversation': conversation,
            'active_users': active_users}

    return url.render(Context(data))
