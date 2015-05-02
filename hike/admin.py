# coding=utf-8

from hike.models import Hike, TypeHike, Region, Difficulty
from django.contrib import admin


admin.site.register(TypeHike)
admin.site.register(Hike)
admin.site.register(Region)
admin.site.register(Difficulty)
