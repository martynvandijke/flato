# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 19:26
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flato', '0015_movie_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
