# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flato', '0006_auto_20171215_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
