# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0029_auto_20160627_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectingareapage',
            name='active_tag',
            field=models.CharField(blank=True, help_text='A WordPress tag name used for display purposes, e.g. "Library Kiosk"', max_length=30),
        ),
        migrations.AddField(
            model_name='collectionpage',
            name='active_tag',
            field=models.CharField(blank=True, help_text='A WordPress tag name used for display purposes, e.g. "Library Kiosk"', max_length=30),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='active_tag',
            field=models.CharField(blank=True, help_text='A WordPress tag name used for display purposes, e.g. "Library Kiosk"', max_length=30),
        ),
    ]
