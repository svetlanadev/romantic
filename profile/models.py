# coding=utf-8

from django.contrib.auth.models import User, UserManager
from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings


class CustomUser(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField(blank=True, null=True)
    # position = models.ForeignKey('TypeUser',  verbose_name=u'Категория')
    karma = models.SmallIntegerField(default=settings.DEFAULT_KARMA,
                                     verbose_name=u'Статус')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # connection = models.ManyToManyField('ConnectionUser', verbose_name=u'Связь')

    phone = models.CharField(max_length=30, verbose_name=u'Номер', blank=True, null=True)
    vk = models.CharField(max_length=90, verbose_name=u'VK', blank=True, null=True)
    facebook = models.CharField(max_length=90, verbose_name=u'Facebook', blank=True, null=True)
    od_class = models.CharField(max_length=90, verbose_name=u'Одноклассники', blank=True, null=True)
    #karma_url = models

    avatar_150 = ImageSpecField(source='avatar',
                                processors=[ResizeToFill(150, 150)],
                                format='PNG',
                                options={'quality': 80})

    avatar_350 = ImageSpecField(source='avatar',
                                processors=[ResizeToFill(350, 350)],
                                format='PNG',
                                options={'quality': 80})

    objects = UserManager()

    def get_absolute_url(self):
        return u'/profile/%s' % self.id

    def get_full_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return self.user.username


# class TypeUser(models.Model):
#     type_user = models.CharField(max_length=50)
#     type_goverment = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

#     def __unicode__(self):
#         return self.type_user


# class ConnectionUser(models.Model):
#     name = models.ForeignKey('ConnectionType', verbose_name=u'Тип связи')
#     number = models.CharField(max_length=30, verbose_name=u'Номер/Аккаунт')

#     def __unicode__(self):
#         return u'%s - %s' % (self.name,
#                              self.number,)


# class ConnectionType(models.Model):
#     name = models.CharField(max_length=30)

#     def __unicode__(self):
#         return self.name
