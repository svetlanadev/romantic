# coding: utf-8
# author: dlyapun

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from photo_check.models import Nomination, Photo, StatisticsPhto
from django.contrib.auth.decorators import login_required
from profile.models import CustomUser

import random


@login_required
def photo_competition_view(request):
    profile = CustomUser.objects.get(user=request.user)
    not_check_photos = Photo.objects.exclude(karma_users=profile)

    nominations = Nomination.objects.all()

    count_1_check = len(Photo.objects.filter(karma_users=profile, nomination__id=1))
    count_1_all = len(Photo.objects.filter(nomination__id=1))
    coun1_1_full = count_1_check * 100 / count_1_all
    if count_1_check == count_1_all:
        coun1_1_full = 100
    if count_1_check == 0:
        coun1_1_full = 1

    count_2_check = len(Photo.objects.filter(karma_users=profile, nomination__id=2))
    count_2_all = len(Photo.objects.filter(nomination__id=2))
    count_2_full = count_2_check * 100 / count_2_all
    if count_2_check == count_2_all:
        count_2_full = 100
    if count_2_check == 0:
        count_2_full = 1

    count_3_check = len(Photo.objects.filter(karma_users=profile, nomination__id=3))
    count_3_all = len(Photo.objects.filter(nomination__id=3))
    count_3_full = count_3_check * 100 / count_3_all
    if count_3_check == count_3_all:
        count_3_full = 100
    if count_3_check == 0:
        count_3_full = 1

    count_4_check = len(Photo.objects.filter(karma_users=profile, nomination__id=4))
    count_4_all = len(Photo.objects.filter(nomination__id=4))
    count_4_full = count_4_check * 100 / count_4_all
    if count_4_check == count_4_all:
        count_4_full = 100
    if count_4_check == 0:
        count_4_full = 1

    data = {'nominations': nominations,
            'not_check_photos': not_check_photos,
            'coun1_1_full': coun1_1_full,
            'count_2_full': count_2_full,
            'count_3_full': count_3_full,
            'count_4_full': count_4_full,
            }
    return render_to_response('photo_check/photo_competition.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def photo_nomination_view(request, nomination_id):
    profile = CustomUser.objects.get(user=request.user)

    count_1_check = len(Photo.objects.filter(karma_users=profile, nomination__id=nomination_id))
    count_1_all = len(Photo.objects.filter(nomination__id=nomination_id))

    count_full = count_1_check * 100 / count_1_all
    if count_1_check == count_1_all:
        count_full = 100
    if count_1_check == 0:
        count_full = 1

    photo_one = Photo.objects.filter(nomination__id=nomination_id).exclude(karma_users=profile)
    try:
        photo_one = random.choice(photo_one)
    except IndexError:
        return redirect('/photo/competition/')

    photo_twos = Photo.objects.filter(nomination__id=nomination_id).exclude(karma_users=profile)
    count_photos_two = len(Photo.objects.filter(nomination__id=nomination_id).exclude(karma_users=profile))

    i = 0
    while 1:
        photo_two = random.choice(photo_twos)
        if photo_one != photo_two:
            status = True
            break

        i = i + 1
        if i > count_photos_two:
            status = False
            break

    if status is False:
        return redirect('/photo/competition/')

    nomination = Nomination.objects.get(id=nomination_id)
    data = {'nomination': nomination,
            'count_full': count_full,
            'photo_one': photo_one,
            'photo_two': photo_two,
            }
    return render_to_response('photo_check/photo_nomination.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def photo_check_view(request, nomination_id):
    profile = CustomUser.objects.get(user=request.user)

    photo_win = Photo.objects.get(id=request.GET.get('win'))
    photo_lose = Photo.objects.get(id=request.GET.get('lose'))

    photo_win.rating = photo_win.rating + 1
    photo_win.save()
    photo_win.karma_users.add(profile)

    photo_lose.karma_users.add(profile)

    statistic = StatisticsPhto.objects.create(user=profile,
                                              photo_one=photo_win,
                                              photo_two=photo_lose,
                                              rating=photo_win.rating,
                                              state=0)

    return redirect('/photo/nomination/%s/' % nomination_id)
