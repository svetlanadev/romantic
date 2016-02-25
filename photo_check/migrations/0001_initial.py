# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f')),
                ('text', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', blank=True)),
            ],
            options={
                'verbose_name': '\u041d\u043e\u043c\u0438\u043d\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u041d\u043e\u043c\u0438\u043d\u0430\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('owner', models.CharField(max_length=100, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80 \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0')),
                ('email_owner', models.CharField(max_length=100, null=True, verbose_name=b'Email \xd0\xb0\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0')),
                ('text', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0', blank=True)),
                ('place', models.CharField(max_length=300, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xba\xd0\xb0')),
                ('camera', models.CharField(max_length=300, verbose_name=b'\xd0\x9f\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x82\xd1\x80\xd1\x8b \xd0\xba\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x80\xd1\x8b')),
                ('date_start', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd1\x8c\xd0\xb5\xd0\xbc\xd0\xba\xd0\xb8')),
                ('image', models.ImageField(upload_to=b'photos_check/', verbose_name=b'\xd0\xa1\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xbe\xd0\xba')),
                ('original_image', models.ImageField(upload_to=b'photos_check_original/', null=True, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb8\xd0\xb3\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xbe\xd0\xba', blank=True)),
                ('state', models.SmallIntegerField(default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, b'\xd0\x9e\xd1\x82\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe'), (1, b'\xd0\x92\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe')])),
                ('rating', models.SmallIntegerField(default=0, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433')),
                ('karma_users', models.ManyToManyField(related_name='user_karma_photos', null=True, verbose_name='\u041b\u044e\u0434\u0438 \u0441\u0434\u0435\u043b\u0430\u043b\u0438 \u043e\u0442\u043c\u0435\u0442\u043a\u0438', to='profile.CustomUser', blank=True)),
                ('nomination', models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f', to='photo_check.Nomination')),
            ],
            options={
                'ordering': ['-date_creation'],
                'verbose_name': '\u0421\u043d\u0438\u043c\u043e\u043a',
                'verbose_name_plural': '\u0421\u043d\u0438\u043c\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='StatisticsPhto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433 \u0444\u043e\u0442\u043a\u0438')),
                ('state', models.SmallIntegerField(default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f'), (1, b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f')])),
                ('photo_one', models.ForeignKey(related_name='photo_one_related', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 1', to='photo_check.Photo')),
                ('photo_two', models.ForeignKey(related_name='photo_two_related', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 2', to='photo_check.Photo')),
                ('user', models.ForeignKey(verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', to='profile.CustomUser')),
            ],
            options={
                'ordering': ['-date_creation'],
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430',
            },
        ),
    ]
