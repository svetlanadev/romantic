# coding=utf-8

from django.contrib import admin
from force_blog.models import BlogPost, Category, DefaultImageBlog
from django.forms import CharField, ModelForm
# from django_summernote.admin import SummernoteModelAdmin


class BlogPostAdmin(admin.ModelAdmin):  # SummernoteModelAdmin
    filter_horizontal = ('category',)
    list_display = ('title',
                    'date_publication',
                    'get_owner_fullname',
                    'state',
                    'if_comments')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)


class DefaultImageBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(DefaultImageBlog, DefaultImageBlogAdmin)
