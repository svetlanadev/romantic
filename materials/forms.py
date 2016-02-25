# coding: utf-8
# author: dlyapun

from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from materials.models import Material


class MaterialForm(ModelForm):
    text = forms.CharField(widget=SummernoteWidget())
    status = forms.CharField(min_length=1,
                             max_length=1000,)

    class Meta:
        model = Material
        exclude = ['owner', 'date_publication', 'date_creation',
                   'rating', 'karma_users', 'material_edit', 'if_comments']

    def save_with_owner(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        obj = super(MaterialForm, self).save(commit=False)
        obj.owner = owner
        obj.save()
        return obj
