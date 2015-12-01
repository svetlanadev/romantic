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
from info_pages.models import InfoPage
from power_comments.models import PowerComment
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import re


register = template.Library()


@register.simple_tag()
def page_navigation(request):
    partys = Party.objects.prefetch_related('category').filter(date_start__gt=datetime.now()).exclude(state=0)[:3]

    try:
        materials = Material.objects.filter(state=1)[:5]
    except ObjectDoesNotExist:
        materials = ''

    comments = []
    apps = []

    last_comment = PowerComment.objects.exclude(state=0)[0:]
    last_comment = last_comment[0]

    print last_comment.id
    comments.append(last_comment)
    apps.append(last_comment.app)

    iteration = last_comment.id

    while iteration > 0:
        iteration -= 1
        try:
            comment = PowerComment.objects.get(id=iteration)
            if comment.state == 0:
                pass
            else:
                if not comment.app in apps:
                    comments.append(comment)
                    apps.append(comment.app)

        except ObjectDoesNotExist:
            pass

        if len(apps) > 6:
            break

    conversation = []
    for app in apps:
        app_url = app
        id_content = ''.join(filter(lambda x: x.isdigit(), app_url))
        if "blog" in app_url:
            obj = BlogPost.objects.get(id=id_content)
        elif "materials" in app_url:
            try:
                obj = Material.objects.get(id=id_content)
            except ObjectDoesNotExist:
                break

        elif "party" in app_url:
            obj = Party.objects.get(id=id_content)

        else:
            pass

        try:
            if obj.state != 0:
                if obj in conversation:
                    pass
                else:
                    conversation.append(obj)
        except UnboundLocalError:
            pass

        if len(conversation) >= 7:
            break

    url = template.loader.get_template("page_navigation/page.html")
    data = {'materials': materials,
            'partys': partys,
            'conversation': conversation,
            'request': request}

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


@register.simple_tag()
def get_active_users():
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

    url = template.loader.get_template("page_navigation/active_users.html")
    data = {'active_users': active_users}
    return url.render(Context(data))


@register.simple_tag()
def get_profile_template(request):
    custom_user = ""
    try:
        custom_user = CustomUser.objects.get(user=request.user)
    except ObjectDoesNotExist:
        custom_user = request.user

    url = template.loader.get_template("page_navigation/profile.html")
    data = {'custom_user': custom_user,
            'request': request}
    return url.render(Context(data))
