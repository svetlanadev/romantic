# coding=utf-8
# author: dlyapun

from django import template
from django.conf import settings
from django.core import urlresolvers
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django_resized import ResizedImageField
from django.contrib import admin

import time


class Photo(models.Model):
    DISABLE = 0
    ENABLE = 1

    STATE_CHOICE = (
        (DISABLE, 'Отключено'),
        (ENABLE, 'Включено'),
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    owner = models.CharField(max_length=100, verbose_name='Автор снимка', blank=True, null=True,)
    email_owner = models.CharField(max_length=100,
                                   verbose_name='Email автора',
                                   blank=True, null=True,)
    name = models.CharField(max_length=100, verbose_name='Название снимка', blank=True, null=True,)
    text = models.TextField(verbose_name='Описание снимка',
                            blank=True, null=True,)

    place = models.CharField(max_length=300,
                             verbose_name='Место снимка',
                             blank=True, null=True,)
    camera = models.CharField(max_length=300,
                              verbose_name='Параметры камеры',
                              blank=True, null=True,)
    date_start = models.DateField(verbose_name='Дата сьемки', blank=True, null=True,)

    # image = models.ImageField(upload_to='photos_check/',
    #                           verbose_name='Снимок')

    image = ResizedImageField(size=[1000, 1500],
                              quality=75, upload_to='photos_check/')

    original_image = models.ImageField(upload_to='photos_check_original/',
                                       blank=True, null=True,
                                       verbose_name='Оригинальный снимок')

    nomination = models.ForeignKey('Nomination', verbose_name='Номинация')

    state = models.SmallIntegerField(default=ENABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    rating = models.SmallIntegerField(default=0, verbose_name=u'Рейтинг')
    karma_users = models.ManyToManyField(settings.AUTH_PROFILE_MODULE,
                                         blank=True, null=True,
                                         verbose_name=u'Люди сделали отметки',
                                         related_name="user_karma_photos")

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Снимок'
        verbose_name_plural = 'Снимки'

    def nomination_view_admin(self):
        return self.nomination.name
    nomination_view_admin.short_description = 'Номинация'
    nomination_view_admin.allow_tags = True

    def image_view(self):
        if self.image:
            url = u'<img src="%s" width="100px"/>' % self.image.url
        else:
            url = u'<img src="%sforce_shop_static/images/logos/brand_icon.png" width="100px"/>' % settings.STATIC_URL
        return url
    image_view.short_description = 'Снимок'
    image_view.allow_tags = True

    def __unicode__(self):
        return self.name


class Nomination(models.Model):
    name = models.CharField(max_length=100, verbose_name='Номинация')
    text = models.TextField(verbose_name='Описание номинации',
                            blank=True, null=True,)

    class Meta:
        verbose_name = 'Номинация'
        verbose_name_plural = 'Номинации'

    def __unicode__(self):
        return self.name


class StatisticsPhto(models.Model):
    ONE_PHOTO = 0
    TWO_PHOTO = 1

    STATE_CHOICE = (
        (ONE_PHOTO, 'Первая фотография'),
        (TWO_PHOTO, 'Вторая фотография'),
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_PROFILE_MODULE, verbose_name='Имя')
    photo_one = models.ForeignKey('Photo', verbose_name='Фото 1',
                                  related_name="photo_one_related")
    photo_two = models.ForeignKey('Photo', verbose_name='Фото 2',
                                  related_name="photo_two_related")
    rating = models.SmallIntegerField(default=0, verbose_name=u'Рейтинг фотки')

    state = models.SmallIntegerField(default=ONE_PHOTO,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'

    # def __unicode__(self):
    #     return self.ip_address


def reset_users(modeladmin, request, queryset):
    print queryset
    for photo in queryset:
        photo.karma_users.clear()
        photo.rating = 0
        photo.save()
    # null_list = []
    # queryset.update(karma_users=null_list)
    # request.queryset.remove(karma_users)
reset_users.short_description = "Reset users"


def image_view(self):
    if self.image:
        return u'<img src="%s" width="100px"/>' % self.image.url
    else:
        return '(none)'
image_view.short_description = "Фото"
image_view.allow_tags = True


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'image', 'rating', 'nomination_view_admin', 'image_view')
    search_fields = ['owner', 'name', 'image']
    actions = [reset_users]


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Nomination)
admin.site.register(StatisticsPhto)
