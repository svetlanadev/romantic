# coding: utf-8
# author: dlyapun

from profile.models import CustomUser
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from info_pages.models import InfoPage
from django.core.exceptions import ObjectDoesNotExist

DISABLE = 0
ENABLE = 1

NATIVE_PLACE = 0
ANOTHER_PLACE = 1

ALL_USERS = 0
REGISTERS = 1
FULLMEMBERS = 2
GOVERNMENTS = 3
MODERATORS = 4


def info_page(request, page):
    try:
        page = InfoPage.objects.get(url_link=page)
    except ObjectDoesNotExist:
        return redirect('/')

    if page.state == DISABLE:
        return redirect('/')
    else:
        if page.access == ALL_USERS:
            data = {'page': page, }
            return render_to_response('info_pages/page.html',
                                      data,
                                      context_instance=RequestContext(request))
        else:
            try:
                profile = CustomUser.objects.get(user=request.user)
            except:
                return redirect('/')

            if page.access == REGISTERS:
                data = {'page': page, }
                return render_to_response('info_pages/page.html',
                                          data,
                                          context_instance=RequestContext(request))

            elif page.access == FULLMEMBERS and profile.valid_member:
                data = {'page': page, }
                return render_to_response('info_pages/page.html',
                                          data,
                                          context_instance=RequestContext(request))

            elif page.access == GOVERNMENTS and profile.goverment:
                data = {'page': page, }
                return render_to_response('info_pages/page.html',
                                          data,
                                          context_instance=RequestContext(request))

            elif page.access == MODERATORS and profile.moderator:
                data = {'page': page, }
                return render_to_response('info_pages/page.html',
                                          data,
                                          context_instance=RequestContext(request))

            else:
                return redirect('/')

    return redirect('/')
