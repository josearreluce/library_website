# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0040_auto_20160629_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceindexpage',
            name='rich_text_external_link',
            field=models.URLField(blank=True, help_text='Optional external link that displays next to the heading'),
        ),
        migrations.AddField(
            model_name='conferencepage',
            name='rich_text_external_link',
            field=models.URLField(blank=True, help_text='Optional external link that displays next to the heading'),
        ),
        migrations.AddField(
            model_name='conferencesubpage',
            name='rich_text_external_link',
            field=models.URLField(blank=True, help_text='Optional external link that displays next to the heading'),
        ),
    ]
