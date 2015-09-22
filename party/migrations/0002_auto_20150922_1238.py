# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='type_party',
            field=models.SmallIntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(1, b'\xd0\x92\xd1\x81\xd1\x82\xd1\x80\xd0\xb5\xd1\x87\xd0\xb0'), (0, b'\xd0\x9c\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbf\xd1\x80\xd0\xb8\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb5')]),
        ),
    ]
