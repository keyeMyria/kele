# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-16 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doginfo', '0016_auto_20180416_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogbreed',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否显示'),
        ),
        migrations.AddField(
            model_name='dogloss',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否显示'),
        ),
    ]
