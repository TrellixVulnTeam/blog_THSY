# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-01 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20180823_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='vars', upload_to='media/photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(max_length=420, null=True, verbose_name='Video link'),
        ),
    ]