# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0083_auto_20160702_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='donorpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site'),
        ),
        migrations.AlterField(
            model_name='floorplanpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='floorplanpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site'),
        ),
        migrations.AlterField(
            model_name='locationpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='locationpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site'),
        ),
        migrations.AlterField(
            model_name='publicrawhtmlpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='publicrawhtmlpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site'),
        ),
        migrations.AlterField(
            model_name='staffpublicpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='staffpublicpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site'),
        ),
    ]