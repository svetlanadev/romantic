# coding=utf-8

from government.models import CustomUser
from imagekit.admin import AdminThumbnail
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='avatar')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
