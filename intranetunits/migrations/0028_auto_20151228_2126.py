# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import base.models


class Migration(migrations.Migration):

    dependencies = [
        ('intranetunits', '0027_auto_20151218_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intranetunitspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(required=False, default=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intranetunitspage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(required=False, default=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))), blank=True),
        ),
    ]
