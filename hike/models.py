# coding=utf-8

from django.contrib.auth.models import User
from django.db import models


class Hike(models.Model):
    STATE_CHOICE = (
        (1, '1 к.с'),
        (2, '2 к.с'),
        (3, '3 к.с'),
        (4, '4 к.с'),
        (5, '5 к.с'),
        (6, '6 к.с'),
        ('PVD', 'ПВД'),
        ('Expedition', 'Экспедиция'),
    )

    user = models.OneToOneField(User)
    type_hike = models.ForeignKey('TypeHike')
    creation_date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    data_finish = models.DateField()
    difficulty = models.TextField(choices=STATE_CHOICE)
    requirements = models.TextField()
    state_group = models.ForeignKey('StateGroup')
    state_group = models.ForeignKey('Region')

    class Meta:
        ordering = ["-creation_date"]

    def __unicode__(self):
        return self.type_hike


# Тип похода - горный, или пеший например
class TypeHike(models.Model):
    typehike = models.CharField(max_length=50)

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
