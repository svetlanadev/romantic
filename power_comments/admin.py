# coding=utf-8

from django_summernote.admin import SummernoteModelAdmin
from power_comments.models import PowerComment
from django.contrib import admin


class PowerCommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'app', 'text', 'rating', 'state')
    filter_horizontal = ('karma_users',)


admin.site.register(PowerComment, PowerCommentAdmin)
