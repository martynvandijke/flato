# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flato', '0007_auto_20171216_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news_slug',
            new_name='slug',
        ),
    ]
