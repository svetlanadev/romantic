# coding=utf-8

from django.db import models
from django.conf import settings
from hike.models import *


class Material(models.Model):
    DISABLE = 0
    HIKE = 1
    ART = 2
    PASSPORT = 3
    SANDBOX = 4

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (HIKE, 'Отчет'),
        (ART, 'Творчество'),
        (PASSPORT, 'Паспорт'),
        (SANDBOX, 'Песочница'),
    )

    title = models.CharField(max_length=50, verbose_name=u'Заголовок', default='Отчет о походе')
    year = models.SmallIntegerField(verbose_name=u'Год', default=2000)
    status = models.CharField(max_length=250, verbose_name=u'Краткое описание', blank=True, null=True)

    # Готовые модели и поля из приложения Hike
    type_hike = models.ForeignKey(TypeHike,  verbose_name=u'Тип похода', blank=True, null=True,)
    difficulty = models.ForeignKey(Difficulty, verbose_name=u'Категория', blank=True, null=True,)
    region = models.ForeignKey(Region, verbose_name=u'Район похода', blank=True, null=True,)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0, verbose_name=u'Рейтинг')

    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                              verbose_name=u'Автор')
    text = models.TextField(verbose_name=u'Страничка')

    state = models.SmallIntegerField(default=HIKE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    

    material_edit = models.ManyToManyField('MaterialEdit',
                                       blank=True, null=True,
                                       verbose_name=u'Редактирование',
                                       related_name="material_edit")
    
    files = models.ManyToManyField('AttachedFiles', blank=True, null=True)

    karma_users = models.ManyToManyField(settings.AUTH_PROFILE_MODULE,
                                         blank=True, null=True,
                                         verbose_name=u'Люди сделали отметки',
                                         related_name="user_karma_blog2")

    image = models.ImageField(upload_to='MaterialImage/',
                              verbose_name=u'Изображение',
                              blank=True,
                              null=True)

    if_comments = models.BooleanField(default=True, verbose_name=u'Комментарии включены')

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return u'/materials/%s' % self.id

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.title,
                                            self.owner.get_full_name(),
                                            self.year,
                                            self.type_hike,
                                            self.difficulty,
                                            self.region,)


class AttachedFiles(models.Model):
    file_name = models.CharField(max_length=50)
    one_file = models.FileField(upload_to='files_materials/')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def get_absolute_url(self):
        return u'/files/%s' % self.id

    def __unicode__(self):
        return self.file_name


class Dirs(models.Model):
    DISABLE = 0
    HIKE = 1
    ART = 2
    PASSPORT = 3

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (HIKE, 'Отчет'),
        (ART, 'Творчество'),
        (PASSPORT, 'Паспорт'),
    )

    dir_name = models.CharField(max_length=30)
    state = models.SmallIntegerField(default=HIKE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')
    materials = models.ManyToManyField('Material',
                                       blank=True, null=True,
                                       verbose_name=u'Материалы',
                                       related_name="Materials")

    image = models.ImageField(upload_to='MaterialImageDir/',
                              verbose_name=u'Изображение',
                              default='/static/img/folder.png',
                              blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'

    def get_absolute_url(self):
        return u'/materials/dirs/%s' % self.id

    def __unicode__(self):
        return self.dir_name


class MaterialEdit(models.Model):
    date_edit = models.DateTimeField(auto_now_add=True)
    user_edit = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                                  verbose_name=u'Автор')

    class Meta:
        verbose_name = 'Редактирование'
        verbose_name_plural = 'Редактирование'

    def __unicode__(self):
        return u'%s - %s' % (self.date_edit,
                             self.user_edit,)
