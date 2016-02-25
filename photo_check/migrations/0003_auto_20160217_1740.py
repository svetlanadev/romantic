# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_check', '0002_auto_20160214_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_start',
            field=models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd1\x8c\xd0\xb5\xd0\xbc\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80 \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0', blank=True),
        ),
    ]
