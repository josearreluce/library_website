# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0059_publicrawhtmlpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpublicpage',
            name='cnetid',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
