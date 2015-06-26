# coding=utf-8

from django.contrib.auth.models import User, UserManager
from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings
from power_comments.settings import *


class CustomUser(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(verbose_name=u'Про себя', blank=True, null=True)
    status = models.CharField(max_length=50, verbose_name=u'Статус', blank=True, null=True)
    karma = models.SmallIntegerField(default=POWER_USER_KARMA_DEFAULT,
                                     verbose_name=u'Карма')

    avatar = models.ImageField(upload_to='avatars/', 
                               blank=True, null=True,
                               default="avatars/no_avatar.png",
                               verbose_name=u'Аватар')

    phone = models.CharField(max_length=30, 
                             verbose_name=u'Номер', 
                             blank=True, null=True)

    vk = models.CharField(max_length=90, 
                          verbose_name=u'VK', 
                          blank=True, null=True)
    facebook = models.CharField(max_length=90, 
                                verbose_name=u'Facebook', 
                                blank=True, null=True)
    od_class = models.CharField(max_length=90, 
                                verbose_name=u'Одноклассники', 
                                blank=True, null=True)

    avatar_150 = ImageSpecField(source='avatar',
                                processors=[ResizeToFill(150, 150)],
                                format='PNG',
                                options={'quality': 80})

    avatar_350 = ImageSpecField(source='avatar',
                                processors=[ResizeToFill(350, 350)],
                                format='PNG',
                                options={'quality': 80})

    writer = models.BooleanField(default=False, verbose_name=u'Писатель') 
    valid_member = models.BooleanField(default=False, verbose_name=u'Действильный член') 
    moderator = models.BooleanField(default=False, verbose_name=u'Модератор') 
    goverment = models.BooleanField(default=False, verbose_name=u'Правление')
    instructor = models.BooleanField(default=False, verbose_name=u'Инструктор')
    black = models.BooleanField(default=False, verbose_name=u'Black')

    objects = UserManager()

    def get_absolute_url(self):
        return u'/profile/%s' % self.id

    def get_full_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return self.user.username
