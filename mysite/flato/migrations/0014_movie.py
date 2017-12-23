# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flato', '0013_news_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('vote_count', models.TextField(blank=True, null=True)),
                ('vote_average', models.TextField(blank=True, null=True)),
                ('poster_path', models.TextField(blank=True, null=True)),
                ('gerne_ids', models.TextField(blank=True, null=True)),
                ('backdrop_path', models.TextField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]