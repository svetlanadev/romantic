# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 23:03
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('photo_check', '0003_auto_20160217_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=django_resized.forms.ResizedImageField(upload_to=b'photos_check/'),
        ),
    ]
