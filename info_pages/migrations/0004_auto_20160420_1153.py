# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-20 11:53
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info_pages', '0003_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopage',
            name='text',
            field=redactor.fields.RedactorField(verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430'),
        ),
    ]