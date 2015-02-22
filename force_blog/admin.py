# coding=utf-8

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from force_blog.models import BlogPost, AttachedFiles, Category, BlogEdit, DefaultImageBlog


class BlogPostAdmin(SummernoteModelAdmin):
    filter_horizontal = ('files', 'category')
    list_display = ('title', 'owner', 'state')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)


class AttachedFilesAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(AttachedFiles, AttachedFilesAdmin)
admin.site.register(Category)
admin.site.register(BlogEdit)
admin.site.register(DefaultImageBlog)
