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
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)

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


# Модератор, писатель, правление.
# class TypeUser(models.Model):
#     type_user = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

#     def __unicode__(self):
#         return self.type_user
