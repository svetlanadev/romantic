# coding=utf-8

from profile.models import CustomUser
from imagekit.admin import AdminThumbnail
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'last_login', 'date_joined')
    inlines = (UserProfileInline, )


# class CustomUserAdmin(admin.ModelAdmin):
#     # list_display = ('__str__', 'admin_thumbnail 'status', 'karma')
#     list_display = ('__str__', 'status', 'karma')
#     admin_thumbnail = AdminThumbnail(image_field='avatar')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)
