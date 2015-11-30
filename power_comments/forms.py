# coding: utf-8
# author: dlyapun

from django import forms
from power_comments.settings import *


class PowerCommentForm(forms.Form):
    text = forms.CharField(min_length=1,
                           max_length=1000,)
