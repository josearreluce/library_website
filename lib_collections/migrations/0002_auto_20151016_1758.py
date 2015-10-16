# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpageaccesslinks',
            name='access_link_url',
            field=models.URLField(verbose_name='Access link', blank=True),
        ),
    ]
