# coding=utf-8

# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class BannerTitle(models.Model):
    DISABLE = 0
    ENABLE = 1

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
    )

    title = models.CharField(max_length=40,
                             verbose_name=u'Название')
    image = models.ImageField(upload_to='BannerTitle/',
                              verbose_name=u'Изображение',
                              blank=True,
                              null=True)
    text = models.CharField(max_length=150,
                            blank=True,
                            null=True,
                            verbose_name=u'Описание')
    text_author = models.CharField(max_length=150,
                                   blank=True,
                                   null=True,
                                   verbose_name=u'Автор')
    state = models.SmallIntegerField(default=DISABLE, choices=STATE_CHOICE)
    creation_date = models.DateTimeField(auto_now_add=True)
    button_name = models.CharField(max_length=40,
                                   default="Узнать подробнее / Обсудить",
                                   verbose_name=u'Название кнопки')

    url = models.CharField(max_length=150, blank=True, null=True,)

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапки'

    def get_absolute_url(self):
        return u'/banner_title/%s' % self.id

    # def save(self, force_insert=False, force_update=False, using=None):
    #     if self.state == 1:
    #         enable_banner = 0
    #         banners = BannerTitle.objects.all()
    #         for banner in banners:
    #             if banner.state == 1:
    #                 if enable_banner == settings.DEFAULT_BANNER_TITLE:
    #                     banner.state = 0
    #                     #banner.save()
    #                 else:
    #                     enable_banner = enable_banner + 1
    #     super(BannerTitle, self).save()

    def __unicode__(self):
        return u'%s %s - %s' % (self.title,
                                self.text,
                                self.state)
    