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

    # try:
    #     profile = CustomUser.objects.get(user=request.user)
    #     if profile.valid_member:
    #         data = {'page': page, }
    #         return render_to_response('info_pages/page.html',
    #                                   data,
    #                                   context_instance=RequestContext(request))
    #
    #     elif page.access == GOVERNMENTS and profile.goverment:
    #         data = {'page': page, }
    #         return render_to_response('info_pages/page.html',
    #                                   data,
    #                                   context_instance=RequestContext(request))
    #
    #     elif page.access == MODERATORS and profile.moderator:
    #         data = {'page': page, }
    #         return render_to_response('info_pages/page.html',
    #                                   data,
    #                                   context_instance=RequestContext(request))
    #     else
    #
    # except ObjectDoesNotExist:
    #     profile = request.user
    #     info_pages = info_pages.filter(access=ALL_USERS)

    data = {'info_pages': info_pages, }
    return data

# (ALL_USERS, 'Доступно для всех'),
#         (REGISTERS, 'Зарегестрированные пользователи'),
#         (FULLMEMBERS, 'Доступно только для ДЧ'),
#         (GOVERNMENTS, 'Доступно только правления'),
#         (MODERATORS, 'Только модераторы'),
#     )