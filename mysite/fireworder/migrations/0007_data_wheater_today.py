# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-09 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireworder', '0006_auto_20171209_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='wheater_today',
            field=models.TextField(blank=True, null=True),
        ),
    ]
