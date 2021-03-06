# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import base.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import datetime
from django.utils.timezone import utc
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0023_auto_20151123_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h2.html', icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h3.html', icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h4.html', icon='title', classname='title')), ('h5', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h5.html', icon='title', classname='title')), ('h6', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h6.html', icon='title', classname='title')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('alignment', base.models.ImageFormatChoiceBlock())), label='Image', icon='image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))))),
        ),
        migrations.AlterField(
            model_name='grouppage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h2.html', icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h3.html', icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h4.html', icon='title', classname='title')), ('h5', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h5.html', icon='title', classname='title')), ('h6', wagtail.wagtailcore.blocks.CharBlock(template='base/blocks/h6.html', icon='title', classname='title')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('alignment', base.models.ImageFormatChoiceBlock())), label='Image', icon='image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock()))))), blank=True),
        ),
        migrations.AlterField(
            model_name='grouppage',
            name='meeting_end_time',
            field=models.TimeField(default=datetime.datetime(2015, 11, 23, 18, 52, 40, 223152, tzinfo=utc), blank=True),
        ),
    ]
