# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0014_dirbrowsepage_news_feed_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirbrowsepage',
            name='active_tag',
            field=models.CharField(blank=True, help_text='A WordPress tag name used for display purposes, e.g. "Library Kiosk"', max_length=30),
        ),
    ]
