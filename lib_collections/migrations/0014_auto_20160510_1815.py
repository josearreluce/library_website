# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0013_auto_20160509_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionpage',
            name='acknowledgments',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='acknowledgments',
            field=models.TextField(blank=True, default=''),
        ),
    ]
