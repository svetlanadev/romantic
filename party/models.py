# coding=utf-8

from django.db import models


class Party(models.Model):
    DISABLE = 0
    ENABLE = 1

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
    )

    name = models.CharField(max_length=50, verbose_name=u'Мероприятие')
    date = models.CharField(max_length=30, verbose_name=u'Дата')
    state = models.SmallIntegerField(default=DISABLE, choices=STATE_CHOICE)
    text = models.TextField(verbose_name=u'Страничка')
    files = models.ManyToManyField('Files', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Files(models.Model):
    file_name = models.CharField(max_length=50)
    one_file = models.FileField(upload_to='files/')

    def __unicode__(self):
        return self.file_name
