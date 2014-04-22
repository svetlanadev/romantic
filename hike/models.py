# coding=utf-8

from django.contrib.auth.models import User
from django.db import models


class Hike(models.Model):
    user = models.OneToOneField(User)
    type_hike = models.ForeignKey('TypeHike')
    creation_date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    data_finish = models.DateField()
    state_group = models.ForeignKey('Difficulty')
    requirements = models.TextField()
    state_group = models.ForeignKey('StateGroup')
    region = models.ForeignKey('Region')

    class Meta:
        ordering = ["-creation_date"]

    def __unicode__(self):
        return u'%s %s %s' % (self.user.username,
                              self.type_hike.type_hike,
                              self.difficulty)


# Тип похода - горный, или пеший например
class TypeHike(models.Model):
    type_hike = models.CharField(max_length=50)

    def __unicode__(self):
        return self.typehike


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
