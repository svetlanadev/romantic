# coding=utf-8

from django.contrib import admin
from materials.models import *
from django.forms import CharField, ModelForm
from datetime import datetime


class MaterialAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    list_display = ('title', 'id', 'owner', 'year', 'state', 'rank', 'date_publication', 'date_creation')
    list_filter = ('date_creation', 'state', 'rank')
    ordering = ('-date_creation',)

    def save_model(self, request, obj, form, change):
        obj.date_publication = datetime.now()
        obj.save()


class DirsAdmin(admin.ModelAdmin):
    list_display = ('dir_name', 'state')
    filter_horizontal = ('materials',)

admin.site.register(Material, MaterialAdmin)
admin.site.register(Dirs, DirsAdmin)
admin.site.register(MaterialEdit)
