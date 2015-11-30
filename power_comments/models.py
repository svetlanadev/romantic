# coding=utf-8

from django.db import models
from django.conf import settings


class PowerComment(models.Model):
    DISABLE = 0
    ENABLE = 1
    BAD_KARMA = 2
    CHECK = 3

    STATE_CHOICE = (
        (DISABLE, 'Скрыт'),
        (ENABLE, 'Активен'),
        (BAD_KARMA, 'Плохая карма'),
        (CHECK, 'На проверке'),
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    # date_edit = models.DateTimeField(blank=True, null=True)
    rating = models.SmallIntegerField(default=0, verbose_name=u'Рейтинг')
    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                              verbose_name=u'Автор')
    karma_users = models.ManyToManyField(settings.AUTH_PROFILE_MODULE,
                                         blank=True, null=True,
                                         verbose_name=u'Люди сделали отметки',
                                         related_name="user_karma_comment")
    text = models.TextField(verbose_name=u'Страничка')
    state = models.SmallIntegerField(default=CHECK,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')
    app = models.CharField(max_length=1000)
    position = models.SmallIntegerField(default=1)
    count_inc = models.SmallIntegerField(verbose_name=u'Кол-во вложений',
                                         blank=True, null=True,)
    pre_comment = models.CharField(max_length=1000,
                                   verbose_name=u'Пре коммент',
                                   blank=True, null=True,)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def get_absolute_url(self):
        return u'/comments/%s' % self.id

    def get_full_name(self):
        if self.owner.first_name or self.owner.last_name:
            full_name = u'%s %s' % (self.owner.first_name,
                                    self.owner.last_name)
            return full_name
        else:
            return "No first or last name"

    def __unicode__(self):
        return u'%s %s - %s' % (self.text,
                                self.owner,
                                self.state,)
