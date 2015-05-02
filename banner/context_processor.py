# coding=utf-8

from banner.models import BannerTitle
from profile.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist


def contex_banner(request):
    if request.user.is_authenticated():
        try:
            profile = CustomUser.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = request.user
    else:
        profile = ""
    
    banners = BannerTitle.objects.filter(state=1)
    return {'banner_title': banners, 'profile':profile}
