# coding=utf-8

from django.contrib.auth.models import User, UserManager
from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill


class CustomUser(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
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
        return u'/users/%s' % self.id

    def __unicode__(self):
        return self.user.username
