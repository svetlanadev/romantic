# coding: utf-8
# author: dlyapun

from django import forms
from django_summernote.widgets import SummernoteWidget


class PowerCommentForm(forms.Form):
    text = forms.CharField(min_length=1,
                           max_length=1000,
                           widget=SummernoteWidget(
                               attrs={'width': '100%',
                                      'height': '200px',
                                      }),
                           error_messages={'required': 'Максимум 1000 символов'})
