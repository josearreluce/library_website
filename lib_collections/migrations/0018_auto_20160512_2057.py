# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0017_auto_20160512_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpagesupplementaryaccesslinks',
            name='supplementary_access_link_url',
            field=models.URLField(verbose_name='Supplementary access link URL'),
        ),
    ]
