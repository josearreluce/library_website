# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redirects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirectpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='redirectpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='redirectpage',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_related', to='units.UnitPage'),
        ),
    ]