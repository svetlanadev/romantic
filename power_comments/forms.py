# coding: utf-8
# author: dlyapun

from django import forms


class PowerCommentForm(forms.Form):
    text = forms.CharField(min_length=10,
                           max_length=400,
                           error_messages={'required': 'Миннимум 10 символов'})
