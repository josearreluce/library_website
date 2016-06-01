# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0050_auto_20160328_1905'),
        ('wagtailcore', '0028_merge'),
        ('staff', '0026_auto_20160502_2055'),
        ('public', '0058_staffpublicpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicRawHTMLPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('sort_order', models.IntegerField(blank=True, default=0)),
                ('html', wagtail.wagtailcore.fields.StreamField((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()),))),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_publicrawhtmlpage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_publicrawhtmlpage_editor', to='staff.StaffPage')),
                ('page_maintainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_publicrawhtmlpage_maintainer', to='staff.StaffPage')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_publicrawhtmlpage_related', to='units.UnitPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]