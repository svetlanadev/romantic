# coding: utf-8
# author: dlyapun

from django import forms


class PowerCommentForm(forms.Form):
    text = forms.CharField(min_length=1,
                           max_length=1000,
                           error_messages={'required': 'Максимум 1000 символов'})
