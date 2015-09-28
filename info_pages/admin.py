# coding=utf-8

from django.contrib import admin
from info_pages.models import InfoPage
from django_summernote.admin import SummernoteModelAdmin


class InfoPageAdmin(SummernoteModelAdmin):
    list_display = (
        'title', 'url_link', 'date_creation', 'owner', 'state', 'place', 'access', 'if_comments')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)


admin.site.register(InfoPage, InfoPageAdmin)
