# coding=utf-8

from django.db import models
from django.conf import settings
from redactor.fields import RedactorField
from django.utils.translation import ugettext as _
from django.utils.translation import (ugettext, ugettext_lazy as _,
                                      pgettext_lazy as __)


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
    date_creation = models.DateTimeField()

    banner = models.ImageField(upload_to='BannerInfoPage/')

    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                              verbose_name=u'Автор')

    text = RedactorField(verbose_name=u'Страничка')

    state = models.SmallIntegerField(default=ENABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    place = models.SmallIntegerField(default=NATIVE_PLACE,
                                     choices=NATIVE_CHOICE,
                                     verbose_name=u'Размещение страницы на сайте:')
    access = models.SmallIntegerField(default=ALL_USERS,
                                      choices=ACCESS_STATE,
                                      verbose_name=u'Доступ к странице имеют:')

    if_comments = models.BooleanField(default=True,
                                      verbose_name=u'Включение комментариев')

    # ======= META INFORMATION ABOUT PRODUCT ======= #
    meta_title = models.CharField(max_length=100,
                                  verbose_name=_('Meta Title'),
                                  blank=True, null=True,)
    meta_url = models.CharField(max_length=100,
                                verbose_name=_('Meta url'),)
    meta_description = models.CharField(max_length=500,
                                        verbose_name=_('Meta descriptoin'),
                                        blank=True, null=True,)
    meta_keywords = models.CharField(max_length=100,
                                     verbose_name=_('Meta Keywords'),
                                     blank=True, null=True,)
    # ============================================== #

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
