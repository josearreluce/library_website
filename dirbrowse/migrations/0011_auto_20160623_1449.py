# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0010_dirbrowsepage_display_hours_in_right_sidebar'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirbrowsepage',
            name='display_hierarchical_listing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dirbrowsepage',
            name='enable_index',
            field=models.BooleanField(default=False),
        ),
    ]
