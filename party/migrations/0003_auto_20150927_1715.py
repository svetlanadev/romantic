# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_auto_20150922_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ['date_start'], 'verbose_name': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435', 'verbose_name_plural': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f'},
        ),
    ]
