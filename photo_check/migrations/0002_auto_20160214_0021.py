# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='camera',
            field=models.CharField(max_length=300, null=True, verbose_name=b'\xd0\x9f\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x82\xd1\x80\xd1\x8b \xd0\xba\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x80\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='place',
            field=models.CharField(max_length=300, null=True, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='state',
            field=models.SmallIntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, b'\xd0\x9e\xd1\x82\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe'), (1, b'\xd0\x92\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe')]),
        ),
    ]
