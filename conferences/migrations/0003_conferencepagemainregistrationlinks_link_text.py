# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_auto_20160202_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencepagemainregistrationlinks',
            name='link_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
