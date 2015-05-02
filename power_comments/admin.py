# coding=utf-8

from power_comments.models import PowerComment
from django.contrib import admin


class PowerCommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'text', 'date_creation', 'app', 'position', 'count_inc', 'pre_comment','rating', 'state')
    filter_horizontal = ('karma_users',)


admin.site.register(PowerComment, PowerCommentAdmin)
