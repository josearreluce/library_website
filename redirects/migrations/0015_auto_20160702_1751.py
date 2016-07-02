# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('redirects', '0014_remove_redirectpage_active_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirectpage',
            name='external_news_page',
            field=models.URLField(blank=True, help_text='Link to an external news page, e.g. wordpress'),
        ),
        migrations.AddField(
            model_name='redirectpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an external news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
