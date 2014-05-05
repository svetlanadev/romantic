# coding=utf-8

from party.models import Party, Files
from django.contrib import admin


class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'state')


class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'one_file')


admin.site.register(Party, PartyAdmin)
admin.site.register(Files, FilesAdmin)
