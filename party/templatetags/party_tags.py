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
import datetime

register = template.Library()


@register.simple_tag()
def party_date_tag(party):
    start_date = party.date_start.date()
    finish_date = party.data_finish.date()
    start_time = str(party.date_start.time())
    finish_time = str(party.data_finish.time())
    x = start_date.strftime("%B")
    if start_date == finish_date:
        s = '<span class="glyphicon glyphicon-time" aria-hidden="true"></span> Начало - %s %s %s года<br> с %s до %s' % (start_date.day,_month_name(start_date.month), start_date.year, start_time[:5], finish_time[:5])
    else:
        start_date = party.date_start.strftime("%d.%m.%Y в %H:%M")
        finish_date = party.data_finish.strftime("%d.%m.%Y в %H:%M")
        s = '<span class="glyphicon glyphicon-time" aria-hidden="true"></span> Начало - %s<br><span class="glyphicon glyphicon-ban-circle" aria-hidden="true"></span> Конец - %s' % (start_date, finish_date)

    return s


def _month_name(number):
    if number == 1:
        s = "Января"
    elif number == 2:
        s = "Февраля"
    elif number == 3:
        s = "Марта"
    elif number == 4:
        s = "Апреля"
    elif number == 5:
        s = "Мая"
    elif number == 6:
        s = "Июня"
    elif number == 7:
        s = "Июля"
    elif number == 8:
        s = "Августа"
    elif number == 9:
        s = "Сентября"
    elif number == 10:
        s = "Октября"
    elif number == 11:
        s = "Ноября"
    elif number == 12:
        s = "Декабря"
    else:
        s = "Error month"
    return s
