# coding=utf-8

from banner.models import BannerTitle, Banner
from django.contrib import admin


class BannerTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'text')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('image', 'text', 'state')


admin.site.register(BannerTitle, BannerTitleAdmin)
admin.site.register(Banner, BannerAdmin)
