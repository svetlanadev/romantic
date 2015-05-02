# coding=utf-8

from party.models import Party
from django.contrib import admin
from cked.widgets import CKEditorWidget
from django.forms import CharField, ModelForm


class ArticleForm(ModelForm):
    text = CharField(widget=CKEditorWidget())


class PartyAdmin(admin.ModelAdmin):
    form = ArticleForm
    filter_horizontal = ('files', 'category')
    list_display = ('name', 'date_creation', 'state')


admin.site.register(Party, PartyAdmin)
