# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('staff', '0033_auto_20160610_1600'),
        ('units', '0051_auto_20160610_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('quicklinks', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('quicklinks_title', models.CharField(blank=True, max_length=100)),
                ('view_more_link', models.URLField(blank=True, default='', max_length=255)),
                ('view_more_link_label', models.CharField(blank=True, max_length=100)),
                ('change_to_callout', models.BooleanField(default=False)),
                ('display_hours_in_right_sidebar', models.BooleanField(default=False)),
                ('enable_index', models.BooleanField(default=False)),
                ('display_hierarchical_listing', models.BooleanField(default=False)),
                ('events_feed_url', models.URLField(blank=True, help_text='Link to a Tiny Tiny RSS Feed')),
                ('banner_title', models.CharField(blank=True, max_length=100)),
                ('news_feed_url', models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site')),
                ('external_news_page', models.URLField(blank=True, help_text='Link to an external news page, e.g. wordpress')),
                ('rich_text_heading', models.CharField(blank=True, max_length=25)),
                ('rich_text', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Should be a bulleted list or combination of h3 elements and bulleted lists')),
                ('rich_text_external_link', models.URLField(blank=True, help_text='Optional external link that displays next to the heading')),
                ('rich_text_link_text', models.CharField(blank=True, help_text='Display text for the rich text link', max_length=25)),
                ('banner_image', models.ForeignKey(blank=True, help_text='Banners should be approximately 1200 × 200 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertindexpage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertindexpage_editor', to='staff.StaffPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='AlertPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('quicklinks', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('quicklinks_title', models.CharField(blank=True, max_length=100)),
                ('view_more_link', models.URLField(blank=True, default='', max_length=255)),
                ('view_more_link_label', models.CharField(blank=True, max_length=100)),
                ('change_to_callout', models.BooleanField(default=False)),
                ('display_hours_in_right_sidebar', models.BooleanField(default=False)),
                ('enable_index', models.BooleanField(default=False)),
                ('display_hierarchical_listing', models.BooleanField(default=False)),
                ('events_feed_url', models.URLField(blank=True, help_text='Link to a Tiny Tiny RSS Feed')),
                ('banner_title', models.CharField(blank=True, max_length=100)),
                ('news_feed_url', models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site')),
                ('external_news_page', models.URLField(blank=True, help_text='Link to an external news page, e.g. wordpress')),
                ('rich_text_heading', models.CharField(blank=True, max_length=25)),
                ('rich_text', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Should be a bulleted list or combination of h3 elements and bulleted lists')),
                ('rich_text_external_link', models.URLField(blank=True, help_text='Optional external link that displays next to the heading')),
                ('rich_text_link_text', models.CharField(blank=True, help_text='Display text for the rich text link', max_length=25)),
                ('banner_message', wagtail.wagtailcore.fields.RichTextField()),
                ('more_info', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('alert_level', models.CharField(choices=[('alert-info', 'Informational Alert'), ('alert-high', 'Critical Alert')], default='alert-info', max_length=25)),
                ('banner_image', models.ForeignKey(blank=True, help_text='Banners should be approximately 1200 × 200 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertpage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertpage_editor', to='staff.StaffPage')),
                ('internal_news_page', models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('page_maintainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertpage_maintainer', to='staff.StaffPage')),
                ('rich_text_link', models.ForeignKey(blank=True, help_text='Optional link that displays next to the heading', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertpage_related', to='units.UnitPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AddField(
            model_name='alertindexpage',
            name='internal_news_page',
            field=models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='alertindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AddField(
            model_name='alertindexpage',
            name='rich_text_link',
            field=models.ForeignKey(blank=True, help_text='Optional link that displays next to the heading', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='alertindexpage',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts_alertindexpage_related', to='units.UnitPage'),
        ),
    ]
