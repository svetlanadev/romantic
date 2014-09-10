# coding=utf-8

from banner.models import BannerTitle


def contex_banner(request):
    banners = BannerTitle.objects.filter(state=1)
    return {'banner_title': banners}
