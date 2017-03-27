# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 20:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0004_auto_20170326_2128'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='performer',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='venue',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='performer',
            name='bio',
            field=models.CharField(blank=True, max_length=100, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='performer',
            name='birthday',
            field=models.CharField(blank=True, max_length=30, verbose_name='birthday'),
        ),
        migrations.AddField(
            model_name='performer',
            name='gender',
            field=models.CharField(blank=True, max_length=30, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='performer',
            name='soundcloud',
            field=models.CharField(blank=True, max_length=100, verbose_name='soundcloud link'),
        ),
        migrations.AddField(
            model_name='performer',
            name='status',
            field=models.CharField(blank=True, max_length=50, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='performer',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, verbose_name='youtube link'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'users'),
        ),
        migrations.AlterField(
            model_name='performer',
            name='performer_id',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username.', b'invalid')], verbose_name='username'),
        ),
    ]
