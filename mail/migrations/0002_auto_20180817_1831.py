# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-17 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abone',
            name='mail',
            field=models.CharField(max_length=170, unique=True, verbose_name='mail'),
        ),
    ]
