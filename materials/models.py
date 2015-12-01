# coding=utf-8

from django.db import models
from django.conf import settings
from hike.models import *
from force_blog.models import Category


class Material(models.Model):

    ENABLE = 1
    DISABLE = 0
    BACKUP = 2
    DELETE = 3

    REPORT = 0
    ART = 1
    PASSPORT = 2
    DOC = 3
    ARTICLE = 4

    RANK_CHOICE = (
        (REPORT, 'Отчет'),
        (ART, 'Творчество'),
        (PASSPORT, 'Паспорт'),
        (DOC, 'Документ'),
        (ARTICLE, 'Статья'),
    )

    STATE_CHOICE = (
        (ENABLE, 'Просмотр доступен'),
        (DISABLE, 'Просмотр запрещен'),
        (BACKUP, 'Материал в архиве'),
        (DELETE, 'Материал удален'),
    )

    title = models.CharField(max_length=150,
                             verbose_name=u'Название / Руководитель',
                             default='Название')
    year = models.SmallIntegerField(verbose_name=u'Год', default=2000)
    status = models.CharField(max_length=800,
                              verbose_name=u'Маршрут',
                              blank=True, null=True)

    # Готовые модели и поля из приложения Hike
    type_hike = models.ForeignKey(TypeHike,
                                  verbose_name=u'Тип похода',
                                  blank=True, null=True,)
    difficulty = models.ForeignKey(Difficulty,
                                   verbose_name=u'Категория',
                                   blank=True, null=True,)
    region = models.ForeignKey(Region,
                               verbose_name=u'Район похода',
                               blank=True, null=True,)

    rank = models.SmallIntegerField(default=REPORT,
                                    choices=RANK_CHOICE,
                                    verbose_name=u'Тип материала')

    state = models.SmallIntegerField(default=DISABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0, verbose_name=u'Рейтинг')

    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                              verbose_name=u'Автор')

    short_desc = models.CharField(max_length=250,
                                  verbose_name=u'Краткое описание материала(сноска)')

    text = models.TextField(verbose_name=u'Страничка')

    category = models.ManyToManyField(Category,
                                      verbose_name=u'Категории',
                                      related_name="material_category")

    material_edit = models.ManyToManyField('MaterialEdit',
                                           blank=True, null=True,
                                           verbose_name=u'Редактирование',
                                           related_name="material_edit")

    karma_users = models.ManyToManyField(settings.AUTH_PROFILE_MODULE,
                                         blank=True, null=True,
                                         verbose_name=u'Люди сделали отметки',
                                         related_name="user_karma_materials")

    image = models.ImageField(upload_to='MaterialImage/',
                              verbose_name=u'Изображение',
                              blank=True,
                              null=True)

    if_comments = models.BooleanField(
        default=True, verbose_name=u'Комментарии включены')

    class Meta:
        ordering = ["-date_publication"]
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def get_absolute_url(self):
        return u'/materials/%s' % self.id

    def get_type_material(self):
        if self.rank == 0 or self.rank == 2:
            name_material = "report"
        else:
            name_material = "article"
        return name_material

    def get_template_material(self):
        if self.rank == 0:
            name_material = "Отчет похода"
        if self.rank == 1:
            name_material = "Творчество"
        if self.rank == 2:
            name_material = "Паспорт препятствия"
        if self.rank == 3:
            name_material = "Документ"
        if self.rank == 4:
            name_material = "Статья"
        return name_material

    def get_rank_material(self):
        if self.rank == 0:
            name_material = "report"
        if self.rank == 1:
            name_material = "art"
        if self.rank == 2:
            name_material = "passport"
        if self.rank == 3:
            name_material = "doc"
        if self.rank == 4:
            name_material = "article"
        return name_material

    def save(self, force_insert=False, force_update=False, using=None):
        print "asdasdasdasdasdasd=+++++++++++++"
        super(Material, self).save()

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s' % (self.title,
                                            self.owner.get_full_name(),
                                            self.year,
                                            self.type_hike,
                                            self.difficulty,
                                            self.region,)


class Dirs(models.Model):
    ENABLE = 1
    DISABLE = 0
    DELETE = 2

    REPORT = 0
    ART = 1
    PASSPORT = 2
    DOC = 3
    ARTICLE = 4

    STATE_CHOICE = (
        (REPORT, 'Отчет'),
        (ART, 'Творчество'),
        (PASSPORT, 'Паспорт'),
        (DOC, 'Документ'),
        (ARTICLE, 'Статья'),
    )

    RANK_CHOICE = (
        (ENABLE, 'Просмотр доступен'),
        (DISABLE, 'Просмотр запрещен'),
        (DELETE, 'Удалено'),
    )

    dir_name = models.CharField(max_length=30)
    state = models.SmallIntegerField(default=REPORT,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    rank = models.SmallIntegerField(default=ENABLE,
                                    choices=RANK_CHOICE,
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


def get_template_materials(self):
    if self.rank == 0:
        name_material = "Отчет похода"
    if self.rank == 1:
        name_material = "Творчество"
    if self.rank == 2:
        name_material = "Паспорт препятствия"
    if self.rank == 3:
        name_material = "Документ"
    if self.rank == 4:
        name_material = "Статья"
    return name_material


def get_rank_materials(self):
    if self.rank == 0:
        name_material = "report"
    if self.rank == 1:
        name_material = "art"
    if self.rank == 2:
        name_material = "passport"
    if self.rank == 3:
        name_material = "doc"
    if self.rank == 4:
        name_material = "article"
    return name_material