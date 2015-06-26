# coding=utf-8

from django.contrib import admin
from force_blog.models import BlogPost, AttachedFiles, Category, BlogEdit, DefaultImageBlog
from django.forms import CharField, ModelForm
from django_summernote.admin import SummernoteModelAdmin


class BlogPostAdmin(SummernoteModelAdmin):
    filter_horizontal = ('category',)
    list_display = (
        'title', 'date_publication', 'owner', 'state', 'if_comments')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)


class AttachedFilesAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(AttachedFiles, AttachedFilesAdmin)
admin.site.register(Category)
admin.site.register(BlogEdit)
admin.site.register(DefaultImageBlog)
