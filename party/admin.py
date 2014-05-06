# coding=utf-8

from party.models import Party, Files
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


class PartyAdmin(SummernoteModelAdmin):
    filter_horizontal = ('files',)
    list_display = ('name', 'date', 'state')


admin.site.register(Party, PartyAdmin)
admin.site.register(Files)
