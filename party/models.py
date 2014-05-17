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
    date_creation = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(verbose_name=u'Начало похода')
    data_finish = models.DateField(verbose_name=u'Конец похода')
    state = models.SmallIntegerField(default=DISABLE, choices=STATE_CHOICE)
    text = models.TextField(verbose_name=u'Страничка')
    files = models.ManyToManyField('Files', blank=True, null=True)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def get_absolute_url(self):
        return u'/party/%s' % self.id

    def __unicode__(self):
        return self.name
