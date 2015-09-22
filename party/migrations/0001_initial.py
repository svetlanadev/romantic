# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('force_blog', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultImageParty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=b'DefaultImageParty/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField(verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')),
                ('data_finish', models.DateTimeField(verbose_name='\u041a\u043e\u043d\u0435\u0446 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')),
                ('state', models.SmallIntegerField(default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, b'\xd0\x92\xd1\x8b\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe'), (1, b'\xd0\x92\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe')])),
                ('type_party', models.SmallIntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, b'\xd0\x92\xd1\x8b\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe'), (1, b'\xd0\x92\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe')])),
                ('text', models.TextField(verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430')),
                ('short_desc', models.CharField(max_length=250, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430(\u0441\u043d\u043e\u0441\u043a\u0430)')),
                ('image', models.ImageField(upload_to=b'PartyImages/')),
                ('if_comments', models.BooleanField(default=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u044b')),
                ('category', models.ManyToManyField(related_name=b'party_category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', to='force_blog.Category')),
                ('default_image', models.ForeignKey(verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e', blank=True, to='party.DefaultImageParty', null=True)),
                ('files', models.ManyToManyField(to='force_blog.AttachedFiles', null=True, blank=True)),
            ],
            options={
                'ordering': ['-date_creation'],
                'verbose_name': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
            bases=(models.Model,),
        ),
    ]
