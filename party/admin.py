# coding=utf-8

from party.models import Party
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


class PartyAdmin(SummernoteModelAdmin):
    filter_horizontal = ('files', 'category')
    list_display = ('name', 'date_creation', 'state')


admin.site.register(Party, PartyAdmin)
