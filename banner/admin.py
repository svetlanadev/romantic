# coding=utf-8

from banner.models import BannerTitle
from django.contrib import admin


class BannerTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'text')


admin.site.register(BannerTitle, BannerTitleAdmin)
