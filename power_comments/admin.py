# coding=utf-8

from power_comments.models import PowerComment
from django.contrib import admin


class PowerCommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'app', 'text', 'rating', 'state')


admin.site.register(PowerComment, PowerCommentAdmin)
