# coding=utf-8

from hike.models import Hike, TypeHike, Region, StateGroup, Banner, Difficulty
from django.contrib import admin


class BannerAdmin(admin.ModelAdmin):
    list_display = ('image', 'text', 'state')


admin.site.register(TypeHike)
admin.site.register(Hike)
admin.site.register(Region)
admin.site.register(StateGroup)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Difficulty)
