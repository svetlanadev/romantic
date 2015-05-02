# coding=utf-8

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from cked.fields import RichTextField


class Hike(models.Model):
    NEW = 0
    PROCESS = 1
    COMPLETE = 2

    STATE_CHOICE = (
        (NEW, 'Подготовка к походу'),
        (PROCESS, 'В походе'),
        (COMPLETE, 'Поход завершен'),
    )

    STATE_CHOICE_GROUP = (
        (NEW, 'Группы нет'),
        (PROCESS, 'Группа набирается'),
        (COMPLETE, 'Группа набрана'),
    )

    user = models.ForeignKey(settings.AUTH_PROFILE_MODULE,  verbose_name=u'Руководитель')
    type_hike = models.ForeignKey('TypeHike',  verbose_name=u'Тип похода')

    text = models.TextField(verbose_name=u'Страничка', blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(verbose_name=u'Начало похода', blank=True, null=True)
    data_finish = models.DateField(verbose_name=u'Конец похода', blank=True, null=True)

    difficulty = models.ForeignKey('Difficulty', verbose_name=u'Категория')

    state_group = models.SmallIntegerField(default=PROCESS,
                                      choices=STATE_CHOICE_GROUP,
                                      verbose_name=u'Статус')

    region = models.ForeignKey('Region', verbose_name=u'Район похода')

    status = models.SmallIntegerField(default=PROCESS,
                                      choices=STATE_CHOICE,
                                      verbose_name=u'Статус')
    
    if_comments = models.BooleanField(default=True, verbose_name=u'Комментарии включены')

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = 'Поход'
        verbose_name_plural = 'Походы'

    def get_absolute_url(self):
        return u'/hikes/%s' % self.id

    def __unicode__(self):
        return u'%s %s - %s, %s' % (self.user.user.first_name,
                                    self.user.user.last_name,
                                    self.type_hike.type_hike,
                                    self.difficulty.difficulty)


# Тип похода - горный, или пеший например
class TypeHike(models.Model):
    type_hike = models.CharField(max_length=50)
    image = models.ImageField(upload_to='TypeHikeImage/',
                              verbose_name=u'Тип похода - изображение')

    class Meta:
        verbose_name = 'Тип похода'
        verbose_name_plural = 'Типы походов'

    def __unicode__(self):
        return self.type_hike


# Регион похода - Кавказ, Крым тд
class Region(models.Model):
    region = models.CharField(max_length=50)

    class Meta:
        ordering = ["-region"]
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __unicode__(self):
        return self.region

# Сложность похода
class Difficulty(models.Model):
    difficulty = models.CharField(max_length=50)

    class Meta:
        ordering = ["-difficulty"]
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложность'

    def __unicode__(self):
        return self.difficulty
