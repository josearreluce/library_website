# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0042_auto_20160701_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conferenceindexpage',
            name='active_tag',
        ),
        migrations.RemoveField(
            model_name='conferencepage',
            name='active_tag',
        ),
        migrations.RemoveField(
            model_name='conferencesubpage',
            name='active_tag',
        ),
    ]
