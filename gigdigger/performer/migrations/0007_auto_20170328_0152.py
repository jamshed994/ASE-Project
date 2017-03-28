# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0006_auto_20170328_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='venue_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='venue name string'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='address string'),
        ),
    ]
