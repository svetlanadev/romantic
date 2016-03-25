# coding=utf-8

from django.contrib import admin
from info_pages.models import InfoPage
from profile.models import CustomUser


class InfoPageAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'date_creation',
                    'owner',
                    'state', 'place', 'access',
                    'if_comments')
    list_filter = ('date_creation',)
    ordering = ('-date_creation',)

    fieldsets = (
        (None, {
            'fields': (('title', 'state'),
                       ('text'),
                       ('date_creation', 'place', 'access'),
                       ('banner'),
                       )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (('meta_title', 'meta_url'),
                       ('meta_description', 'meta_keywords'),
                       ('if_comments'),
                       )
        }),
    )

    prepopulated_fields = {"meta_url": ("title",)}

    def save_model(self, request, obj, form, change):
        owner = CustomUser.objects.get(user=request.user)
        obj.owner = owner
        obj.save()


admin.site.register(InfoPage, InfoPageAdmin)
