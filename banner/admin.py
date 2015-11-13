# coding=utf-8

from banner.models import BannerTitle
from django.contrib import admin


class BannerTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'text', 'image_view')


admin.site.register(BannerTitle, BannerTitleAdmin)
