# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findingaids', '0016_auto_20160708_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='findingaidspage',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
