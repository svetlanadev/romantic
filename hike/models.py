# coding=utf-8

from django.contrib.auth.models import User
from django.db import models


class Hike(models.Model):
    user = models.OneToOneField(User,  verbose_name=u'Руководитель')
    type_hike = models.ForeignKey('TypeHike',  verbose_name=u'Тип похода')
    creation_date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(verbose_name=u'Начало похода')
    data_finish = models.DateField(verbose_name=u'Конец похода')
    difficulty = models.ForeignKey('Difficulty', verbose_name=u'Категория')
    requirements = models.TextField(verbose_name=u'Рекомендации')
    state_group = models.ForeignKey('StateGroup', verbose_name=u'Статус')
    region = models.ForeignKey('Region', verbose_name=u'Район похода')
    # status = Пройден или тд

    class Meta:
        ordering = ["-creation_date"]

    def __unicode__(self):
        return u'%s %s - %s, %s' % (self.user.first_name,
                                    self.user.last_name,
                                    self.type_hike.type_hike,
                                    self.difficulty.difficulty)


# Тип похода - горный, или пеший например
class TypeHike(models.Model):
    type_hike = models.CharField(max_length=50)

    def __unicode__(self):
        return self.type_hike


# Регион похода - Кавказ, Крым тд
class Region(models.Model):
    region = models.CharField(max_length=50)

    def __unicode__(self):
        return self.region


# Состояние группы - набрана или нет
class StateGroup(models.Model):
    state_group = models.TextField()

    def __unicode__(self):
        return self.state_group


# Сложность похода
class Difficulty(models.Model):
    difficulty = models.CharField(max_length=50)

    def __unicode__(self):
        return self.difficulty


class Banner(models.Model):
    DISABLE = 0
    ENABLE = 1

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
    )

    image = models.ImageField(upload_to='banners/')
    text = models.TextField()
    state = models.SmallIntegerField(default=DISABLE, choices=STATE_CHOICE)

    def save(self, force_insert=False, force_update=False, using=None):
        if self.state == 1:
            banners = Banner.objects.all()
            for banner in banners:
                banner.state = 0
                banner.save()
                print banner
        super(Banner, self).save()

    def __unicode__(self):
        return u'%s %s' % (self.text, self.state)
