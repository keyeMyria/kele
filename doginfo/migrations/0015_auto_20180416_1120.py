# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-16 03:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doginfo', '0014_auto_20180416_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogloss',
            old_name='color',
            new_name='colors',
        ),
    ]
