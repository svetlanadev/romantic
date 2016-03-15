# coding=utf-8

from party.models import Party
from django.contrib import admin
from django.forms import CharField, ModelForm


class PartyAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    list_display = ('title', 'date_creation', 'date_start', 'data_finish', 'state')


admin.site.register(Party, PartyAdmin)
