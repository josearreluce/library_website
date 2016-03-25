# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('staff', '0023_auto_20160301_1838'),
        ('units', '0049_unitpage_alphabetical_directory_name'),
        ('wagtaildocs', '0007_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('sort_order', models.IntegerField(blank=True, default=0)),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_editor', to='staff.StaffPage')),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('page_maintainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_maintainer', to='staff.StaffPage')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_related', to='units.UnitPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
