# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 15:59
from __future__ import unicode_literals

import base.models
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0026_auto_20160502_2055'),
        ('wagtailcore', '0028_merge'),
        ('units', '0050_auto_20160328_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirBrowsePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('sort_order', models.IntegerField(blank=True, default=0)),
                ('body', wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Secondary'), ('btn-reserve', 'Reservation')], default='btn-primary')), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StructBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', icon='title', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), help_text='A talk or event with a title, presenter             room number, and description', icon='edit', label=' '))), icon='date', template='base/blocks/agenda.html'))), blank=True, null=True)),
                ('dir_browse_script_url', models.URLField(max_length=255)),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_editor', to='staff.StaffPage')),
                ('page_maintainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_maintainer', to='staff.StaffPage')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_related', to='units.UnitPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
