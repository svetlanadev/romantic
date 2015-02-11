# coding: utf-8
# author: dlyapun

from django import forms
from django.forms import ModelForm
from force_blog.models import BlogPost
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class BlogPostForm(ModelForm):
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = BlogPost
        exclude = ['owner', 'date_publication', 'date_creation', 'rating', 'state']

    # def save(self, *args, **kwargs):
    #     owner = kwargs.pop('owner')
    #     obj = super(BlogPost, self).save(commit=False)
    #     obj.owner = owner
    #     obj.save()
    #     return obj
        