# coding=utf-8

from django.db import models
from django.conf import settings
from banner.models import BannerTitle


class InfoPage(models.Model):
    DISABLE = 0
    ENABLE = 1

    NATIVE_PLACE = 0
    ANOTHER_PLACE = 1

    ALL_USERS = 0
    REGISTERS = 1
    FULLMEMBERS = 2
    GOVERNMENTS = 3
    MODERATORS = 4

    STATE_CHOICE = (
        (DISABLE, 'Страница отключена'),
        (ENABLE, 'Страница включена'),
    )

    NATIVE_CHOICE = (
        (NATIVE_PLACE, 'Страница в разделе "О Клубе"'),
        (ANOTHER_PLACE, 'Другой раздел'),
    )

    ACCESS_STATE = (
        (ALL_USERS, 'Доступно для всех'),
        (REGISTERS, 'Зарегестрированные пользователи'),
        (FULLMEMBERS, 'Доступно только для ДЧ'),
        (GOVERNMENTS, 'Доступно только правления'),
        (MODERATORS, 'Только модераторы'),
    )

    title = models.CharField(max_length=300, verbose_name=u'Заголовок')
    url_link = models.CharField(max_length=300, verbose_name=u'URL страницы')
    date_creation = models.DateTimeField()

    banner = models.ForeignKey(BannerTitle,
                               verbose_name=u'Баннер',
                               blank=True, null=True,)

    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                              verbose_name=u'Автор')
    text = models.TextField(verbose_name=u'Страничка')

    state = models.SmallIntegerField(default=ENABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')
    place = models.SmallIntegerField(default=NATIVE_PLACE,
                                     choices=NATIVE_CHOICE,
                                     verbose_name=u'Размещение страницы на сайте:')
    access = models.SmallIntegerField(default=ALL_USERS,
                                      choices=ACCESS_STATE,
                                      verbose_name=u'Доступ к странице имеют:')

    if_comments = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def get_absolute_url(self):
        return u'/page/%s' % self.url_link

    def __unicode__(self):
        return u'%s %s - %s' % (self.title,
                                self.owner,
                                self.state,)