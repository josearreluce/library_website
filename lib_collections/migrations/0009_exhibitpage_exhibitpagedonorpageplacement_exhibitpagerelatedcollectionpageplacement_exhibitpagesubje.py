# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('public', '0052_auto_20160328_1905'),
        ('subjects', '0004_subjectseealsotable'),
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
        ('units', '0050_auto_20160328_1905'),
        ('staff', '0024_auto_20160328_1905'),
        ('lib_collections', '0008_auto_20160328_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('sort_order', models.IntegerField(blank=True, default=0)),
                ('short_abstract', models.TextField(default='')),
                ('full_description', models.TextField(default='')),
                ('thumbnail_caption', models.TextField(blank=True, default='')),
                ('student_exhibit', models.BooleanField(default=False)),
                ('exhibit_open_date', models.DateField(blank=True, null=True)),
                ('exhibit_close_date', models.DateField(blank=True, null=True)),
                ('exhibit_daily_hours', models.CharField(blank=True, default='', max_length=255)),
                ('exhibit_cost', models.CharField(blank=True, default='', max_length=255)),
                ('space_type', models.CharField(blank=True, choices=[('Case', 'Case'), ('Gallery', 'Gallery')], max_length=255)),
                ('web_exhibit_url', models.URLField(blank=True, verbose_name='Web Exhibit URL')),
                ('publication_description', models.CharField(blank=True, default='', max_length=255)),
                ('publication_price', models.CharField(blank=True, default='', max_length=255)),
                ('publication_url', models.URLField(blank=True, verbose_name='Publication URL')),
                ('ordering_information', models.BooleanField(default=False)),
                ('exhibit_text', models.URLField(blank=True, verbose_name='Exhibit Text')),
                ('exhibit_checklist', models.URLField(blank=True, verbose_name='Exhibit Checklist')),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitpage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitpage_editor', to='staff.StaffPage')),
                ('exhibit_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='public.LocationPage')),
                ('page_maintainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitpage_maintainer', to='staff.StaffPage')),
                ('staff_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.StaffPage')),
                ('thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitpage_related', to='units.UnitPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ExhibitPageDonorPagePlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_page_donor_page', to='public.DonorPage')),
                ('parent', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_page_donor_page_list_placement', to='lib_collections.ExhibitPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='ExhibitPageRelatedCollectionPagePlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('parent', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_page_related_collection_placement', to='lib_collections.ExhibitPage')),
                ('related_collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exhibit_page_related_collection', to='lib_collections.CollectionPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='ExhibitPageSubjectPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibit_subject_placements', to='lib_collections.ExhibitPage')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='subjects.Subject')),
            ],
            options={
                'verbose_name_plural': 'Subbject Placements',
                'verbose_name': 'Subject Placement',
            },
        ),
    ]
