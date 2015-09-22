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
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.simple_tag()
def page_navigation(request):

    if request.user.is_authenticated():
        try:
            custom_user = CustomUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            custom_user = request.user
    else:
        custom_user = ""

    partys = Party.objects.exclude(state=0)[:3]

    try:
        materials = Material.objects.filter(state=1)[:5]
    except ObjectDoesNotExist:
        materials = ''


    comments_active_users = PowerComment.objects.values('owner').distinct()
    comments_active_users_count = comments_active_users.count() - 8
    try:
        comments_active_users = comments_active_users[comments_active_users_count:]
    except AssertionError:
        pass

    active_users = []
    for x in comments_active_users:
        active_user = CustomUser.objects.get(id=x['owner'])

        if not active_user in active_users:
            active_users.append(active_user)

        if len(active_users) >= 8:
            break

    comments = PowerComment.objects.values('app').distinct()
    print comments
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
            try:
                obj = Material.objects.get(id=id_content)
                url = obj.title
            except ObjectDoesNotExist:
                break

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
            'active_users': active_users,
            'request': request,
            'custom_user': custom_user}

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