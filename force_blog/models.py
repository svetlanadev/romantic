# coding=utf-8

from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    DISABLE = 0
    ENABLE = 1
    DELETE = 2

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
        (DELETE, 'Delete'),
    )

    title = models.CharField(max_length=50, verbose_name=u'Заголовок')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                                 verbose_name=u'Автор')
    text = models.TextField(verbose_name=u'Страничка')
    state = models.SmallIntegerField(default=DISABLE, choices=STATE_CHOICE)
    category = models.ManyToManyField('Category',
                                      verbose_name=u'Категории',
                                      related_name="blogposts_category")
    files = models.ManyToManyField('AttachedFiles', blank=True, null=True)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return u'/blog/%s' % self.id

    def __unicode__(self):
        return u'%s %s - %s' % (self.title,
                                self.owner,
                                self.state,)


class AttachedFiles(models.Model):
    file_name = models.CharField(max_length=50)
    one_file = models.FileField(upload_to='files/')
    category = models.ManyToManyField('Category',
                                      verbose_name=u'Категории',
                                      related_name="file_category")

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def get_absolute_url(self):
        return u'/files/%s' % self.id

    def __unicode__(self):
        return self.file_name


class Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __unicode__(self):
        return self.category
