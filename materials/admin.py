# coding=utf-8

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from materials.models import *


class MaterialAdmin(SummernoteModelAdmin):
    filter_horizontal = ('files',)
    list_display = ('title', 'owner', 'state')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)


class DirsAdmin(admin.ModelAdmin):
    list_display = ('dir_name', 'state')
    filter_horizontal = ('materials',)

admin.site.register(Material, MaterialAdmin)
admin.site.register(AttachedFiles)
admin.site.register(Dirs, DirsAdmin)
admin.site.register(MaterialEdit)
