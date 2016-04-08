# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0075_auto_20160307_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupindexpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupindexpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupmeetingminutesindexpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupmeetingminutesindexpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupmeetingminutesindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupmeetingminutesindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupmeetingminutespage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupmeetingminutespage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupmeetingminutespage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupmeetingminutespage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='grouppage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_grouppage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='grouppage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_grouppage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupreportsindexpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupreportsindexpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupreportsindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupreportsindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupreportspage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupreportspage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='groupreportspage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_groupreportspage_maintainer', to='staff.StaffPage'),
        ),
    ]