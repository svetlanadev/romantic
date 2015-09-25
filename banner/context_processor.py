# coding=utf-8

from banner.models import BannerTitle
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


def contex_banner(request):
    if request.path == '/party/':
        banner = 'winter.jpg'
    else:
        banner = 'general.jpg'

    return {'banner': banner }
