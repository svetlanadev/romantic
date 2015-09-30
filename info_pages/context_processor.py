# coding=utf-8

from info_pages.models import InfoPage
from profile.models import CustomUser
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template import RequestContext


DISABLE = 0
ENABLE = 1

NATIVE_PLACE = 0
ANOTHER_PLACE = 1

ALL_USERS = 0
REGISTERS = 1
FULLMEMBERS = 2
GOVERNMENTS = 3
MODERATORS = 4


def contex_info_pages(request):
    info_pages = InfoPage.objects.filter(state=ENABLE, place=NATIVE_PLACE)
    pages = []
    # conversation.append(obj)
    try:
        profile = CustomUser.objects.get(user=request.user)
    except:
        info_pages = InfoPage.objects.filter(state=ENABLE, place=NATIVE_PLACE, access=ALL_USERS)
        data = {'info_pages': info_pages, }
        return data

    if profile.user.is_superuser or profile.moderator:
        info_pages = InfoPage.objects.filter(state=ENABLE, place=NATIVE_PLACE)
    elif profile.goverment and profile.valid_member:
        info_pages = info_pages.exclude(access=MODERATORS)
    elif profile.goverment:
        info_pages = info_pages.exclude(access=MODERATORS).exclude(access=FULLMEMBERS)
    elif profile.valid_member:
        info_pages = info_pages.exclude(access=MODERATORS).exclude(access=GOVERNMENTS)
    else:
        info_pages = info_pages.exclude(access=MODERATORS).exclude(access=FULLMEMBERS).exclude(access=GOVERNMENTS)

    print info_pages

    data = {'info_pages': info_pages, }
    return data
