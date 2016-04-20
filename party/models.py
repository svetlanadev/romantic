# coding=utf-8

from django.db import models
from force_blog.models import Category
from redactor.fields import RedactorField


class Party(models.Model):
    DISABLE = 0
    ENABLE = 1

    PARTY = 0
    MEETING = 1

    STATE_CHOICE = (
        (DISABLE, 'Выключено'),
        (ENABLE, 'Включено'),
    )

    TYPE_CHOICE = (
        (MEETING, 'Встреча'),
        (PARTY, 'Мероприятие'),
    )

    title = models.CharField(max_length=50, verbose_name=u'Мероприятие')

    date_creation = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(verbose_name=u'Начало мероприятия')
    data_finish = models.DateTimeField(verbose_name=u'Конец мероприятия')

    state = models.SmallIntegerField(default=DISABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    type_party = models.SmallIntegerField(default=MEETING,
                                          choices=TYPE_CHOICE,
                                          verbose_name=u'Статус')

    text = RedactorField(verbose_name=u'Страничка')
    short_desc = models.CharField(max_length=250,
                                  verbose_name=u'Краткое описание(сноска)')

    category = models.ManyToManyField(Category,
                                      verbose_name=u'Категории',
                                      related_name="party_category")

    image = models.ImageField(upload_to='PartyImages/')
    default_image = models.ForeignKey('DefaultImageParty',
                                      verbose_name=u'Изображение по умолчанию',
                                      blank=True, null=True)

    if_comments = models.BooleanField(
        default=True, verbose_name=u'Комментарии включены')

    class Meta:
        ordering = ["date_start"]
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def get_absolute_url(self):
        return u'/party/%s' % self.id

    def __unicode__(self):
        return self.title


class DefaultImageParty(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='DefaultImageParty/',
                              verbose_name=u'Изображение')

    class Meta:
        verbose_name = 'Изображение по умолчанию'
        verbose_name_plural = 'Изображения по умолчанию'

    def __unicode__(self):
        return self.name
