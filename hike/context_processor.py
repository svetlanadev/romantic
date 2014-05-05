# coding=utf-8

from hike.models import Banner
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def contex_hike(request):
    try:
        banner = Banner.objects.get(state=1)
    except ObjectDoesNotExist:
        banner = "ERROR"
    except MultipleObjectsReturned:
        banner = "ERROR"
    return {'banner': banner}
