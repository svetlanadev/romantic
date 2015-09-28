# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '__first__'),
        ('profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('url_link', models.CharField(max_length=300, verbose_name='URL \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
                ('date_creation', models.DateTimeField()),
                ('text', models.TextField(verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430')),
                ('state', models.SmallIntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', choices=[(0, b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0'), (1, b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb2\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0')])),
                ('place', models.SmallIntegerField(default=0, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043d\u0430 \u0441\u0430\u0439\u0442\u0435:', choices=[(0, b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb2 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5 "\xd0\x9e \xd0\x9a\xd0\xbb\xd1\x83\xd0\xb1\xd0\xb5"'), (1, b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb9 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb')])),
                ('access', models.SmallIntegerField(default=0, verbose_name='\u0414\u043e\u0441\u0442\u0443\u043f \u043a \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0438\u043c\u0435\u044e\u0442:', choices=[(0, b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbd\xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb2\xd1\x81\xd0\xb5\xd1\x85'), (1, b'\xd0\x97\xd0\xb0\xd1\x80\xd0\xb5\xd0\xb3\xd0\xb5\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8'), (2, b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbd\xd0\xbe \xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd0\x94\xd0\xa7'), (3, b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbd\xd0\xbe \xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'), (4, b'\xd0\xa2\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b')])),
                ('if_comments', models.BooleanField(default=True)),
                ('banner', models.ForeignKey(verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440', blank=True, to='banner.BannerTitle', null=True)),
                ('owner', models.ForeignKey(verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0441\u0442\u0430\u0442\u044c\u0438', to='profile.CustomUser')),
            ],
            options={
                'ordering': ['-date_creation'],
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=(models.Model,),
        ),
    ]
