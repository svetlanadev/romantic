# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopage',
            name='owner',
            field=models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to='profile.CustomUser'),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='state',
            field=models.SmallIntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0'), (1, b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb2\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0')]),
        ),
    ]
