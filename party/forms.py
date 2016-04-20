# coding: utf-8
# author: dlyapun

from django import forms
from django.forms import ModelForm
from party.models import Party
from redactor.widgets import RedactorEditor


class PartyForm(ModelForm):
    text = forms.CharField(widget=RedactorEditor())
    date_time_start = forms.DateTimeField()
    date_time_finish = forms.DateTimeField()

    class Meta:
        model = Party
        exclude = ['date_creation', 'files', 'category', 'image', 'files', ]

    def save_with_owner(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        obj = super(BlogPostForm, self).save(commit=False)
        obj.owner = owner
        obj.save()
        return obj
