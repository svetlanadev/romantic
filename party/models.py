# coding=utf-8

from django.db import models
from force_blog.models import AttachedFiles, Category
from cked.fields import RichTextField


class Party(models.Model):
    DISABLE = 0
    ENABLE = 1
    PARTY = 2

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Встреча'),
        (PARTY, 'Мероприятие'),
    )

    name = models.CharField(max_length=50, verbose_name=u'Мероприятие')

    date_creation = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(verbose_name=u'Начало мероприятия')
    data_finish = models.DateTimeField(verbose_name=u'Конец мероприятия')

    state = models.SmallIntegerField(default=PARTY,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    text = models.TextField(verbose_name=u'Страничка')
    
    files = models.ManyToManyField(AttachedFiles, blank=True, null=True)
    category = models.ManyToManyField(Category,
                                      verbose_name=u'Категории',
                                      related_name="party_category")
    image = models.ImageField(upload_to='PartyImages/')
    if_comments = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def get_absolute_url(self):
        return u'/party/%s' % self.id

    def __unicode__(self):
        return self.name
