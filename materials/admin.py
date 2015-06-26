# coding=utf-8

from django.contrib import admin
from materials.models import *
from django_summernote.admin import SummernoteModelAdmin
from django.forms import CharField, ModelForm


class MaterialAdmin(SummernoteModelAdmin):
    filter_horizontal = ('category',)
    list_display = ('title', 'owner', 'year', 'state', 'rank', 'status')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)


class DirsAdmin(admin.ModelAdmin):
    list_display = ('dir_name', 'state')
    filter_horizontal = ('materials',)

admin.site.register(Material, MaterialAdmin)
admin.site.register(Dirs, DirsAdmin)
admin.site.register(MaterialEdit)
