# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-16 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogtype', '0002_auto_20180302_0918'),
        ('doginfo', '0008_auto_20180302_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogBreed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('ages', models.CharField(max_length=50, verbose_name='狗龄')),
                ('colors', models.CharField(max_length=10, verbose_name='颜色')),
                ('desc', models.CharField(max_length=50, verbose_name='特点')),
                ('picture', models.CharField(max_length=50, verbose_name='图片')),
                ('price', models.CharField(max_length=100, verbose_name='价格区间')),
                ('ownername', models.CharField(max_length=100, verbose_name='狗主姓名')),
                ('telephone', models.CharField(max_length=50, verbose_name='电话')),
                ('showtime', models.DateTimeField(verbose_name='显示时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogtype.Dogtype', verbose_name='品种')),
            ],
            options={
                'verbose_name': '配种',
                'verbose_name_plural': '配种',
                'ordering': ['create_time'],
            },
        ),
        migrations.RemoveField(
            model_name='dogfeed',
            name='typeid',
        ),
        migrations.DeleteModel(
            name='DogFeed',
        ),
    ]
