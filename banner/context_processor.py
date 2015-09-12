# coding=utf-8

from banner.models import BannerTitle
from profile.models import CustomUser
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


def contex_banner(request):
    if request.user.is_authenticated():
        try:
            profile = CustomUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = request.user
    else:
        profile = ""

    if request.path == '/passport/':
        banner = 'pano.jpg'
    else:
        banner = 'general.jpg'

    print banner
    return {'banner': banner, 'profile':profile, 'mode_site': settings.DEBUG}
