# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('force_blog', '0002_blogpost_view_user'),
        ('profile', '__first__'),
        ('hike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dirs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_name', models.CharField(max_length=30)),
                ('state', models.SmallIntegerField(choices=[(0, b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x82'), (1, b'\xd0\xa2\xd0\xb2\xd0\xbe\xd1\x80\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (2, b'\xd0\x9f\xd0\xb0\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82'), (3, b'\xd0\x94\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82'), (4, b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd1\x8f')], default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('rank', models.SmallIntegerField(choices=[(1, b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xb5\xd0\xbd'), (0, b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd'), (2, b'\xd0\xa3\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbe')], default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('image', models.ImageField(blank=True, default=b'/static/img/folder.png', null=True, upload_to=b'MaterialImageDir/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u043f\u043a\u0430',
                'verbose_name_plural': '\u041f\u0430\u043f\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', max_length=150, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 / \u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c')),
                ('year', models.SmallIntegerField(default=2000, verbose_name='\u0413\u043e\u0434')),
                ('status', models.CharField(blank=True, max_length=800, null=True, verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442')),
                ('rank', models.SmallIntegerField(choices=[(0, b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x82'), (1, b'\xd0\xa2\xd0\xb2\xd0\xbe\xd1\x80\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (2, b'\xd0\x9f\xd0\xb0\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82'), (3, b'\xd0\x94\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82'), (4, b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd1\x8f')], default=0, verbose_name='\u0422\u0438\u043f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430')),
                ('state', models.SmallIntegerField(choices=[(1, b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xb5\xd0\xbd'), (0, b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd'), (2, b'\xd0\x9c\xd0\xb0\xd1\x82\xd0\xb5\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb \xd0\xb2 \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2\xd0\xb5'), (3, b'\xd0\x9c\xd0\xb0\xd1\x82\xd0\xb5\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd')], default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433')),
                ('short_desc', models.CharField(max_length=250, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430(\u0441\u043d\u043e\u0441\u043a\u0430)')),
                ('text', models.TextField(verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430')),
                ('image', django_resized.forms.ResizedImageField(blank=True, null=True, upload_to=b'MaterialImage/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('if_comments', models.BooleanField(default=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u044b')),
                ('category', models.ManyToManyField(related_name='material_category', to='force_blog.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('difficulty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hike.Difficulty', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('karma_users', models.ManyToManyField(blank=True, null=True, related_name='user_karma_materials', to='profile.CustomUser', verbose_name='\u041b\u044e\u0434\u0438 \u0441\u0434\u0435\u043b\u0430\u043b\u0438 \u043e\u0442\u043c\u0435\u0442\u043a\u0438')),
            ],
            options={
                'ordering': ['-date_publication'],
                'verbose_name': '\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b',
                'verbose_name_plural': '\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='MaterialEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_edit', models.DateTimeField(auto_now_add=True)),
                ('user_edit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.CustomUser', verbose_name='\u0410\u0432\u0442\u043e\u0440')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='material_edit',
            field=models.ManyToManyField(blank=True, null=True, related_name='material_edit', to='materials.MaterialEdit', verbose_name='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='material',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.CustomUser', verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AddField(
            model_name='material',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hike.Region', verbose_name='\u0420\u0430\u0439\u043e\u043d \u043f\u043e\u0445\u043e\u0434\u0430'),
        ),
        migrations.AddField(
            model_name='material',
            name='type_hike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hike.TypeHike', verbose_name='\u0422\u0438\u043f \u043f\u043e\u0445\u043e\u0434\u0430'),
        ),
        migrations.AddField(
            model_name='dirs',
            name='materials',
            field=models.ManyToManyField(blank=True, null=True, related_name='Materials', to='materials.Material', verbose_name='\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b'),
        ),
    ]
