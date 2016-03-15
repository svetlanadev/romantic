# coding=utf-8

from django.contrib import admin
from force_blog.models import BlogPost, Category, DefaultImageBlog
from django.forms import CharField, ModelForm
from profile.models import CustomUser


class BlogPostAdmin(admin.ModelAdmin):  # SummernoteModelAdmin
    filter_horizontal = ('category',)
    list_display = ('title',
                    'date_publication',
                    'get_owner_fullname',
                    'state',
                    'if_comments')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)

    fieldsets = (
        (None, {
            'fields': (('title',),
                       ('text'),
                       ('category'),
                       )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (('image', 'default_image'),
                       ('state', 'if_comments', 'view_user'),
                       )
        }),
    )

    def save_model(self, request, obj, form, change):
        owner = CustomUser.objects.get(user=request.user)
        obj.owner = owner
        obj.save()


class DefaultImageBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(DefaultImageBlog, DefaultImageBlogAdmin)
