from django import forms
from django.apps import apps
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
from library_website.settings.base import PHONE_FORMAT, PHONE_ERROR_MSG, POSTAL_CODE_FORMAT, POSTAL_CODE_ERROR_MSG
from unidecode import unidecode
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import ChoiceBlock, TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, ListBlock, RichTextBlock, BooleanBlock, RawHTMLBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock 
from wagtail.wagtailsearch import index
from wagtail.wagtaildocs.models import Document
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel

from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

import logging
import sys

# e.g. path "00010002" returns "000100020004", when "000100020003" is the highest path number that currently exists. 
def get_available_path_under(path):
    child_pages = filter(lambda p: p.path.startswith(path) and len(p.path) == len(path) + 4, apps.get_model('wagtailcore.Page').objects.all())
    child_paths = sorted(map(lambda c: c.path, child_pages))
    if child_paths:
        return "%s%04d" % (path, int(child_paths.pop()[-4:]) + 1)
    else:
        return "%s0001" % path

def make_slug(s):
    s = unidecode(s)
    s = s.lower()
    s = ' '.join(s.split()) # replace multiple spaces with a single space.
    s = s.strip()
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.replace('\'', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('&', 'and')
    s = s.replace(' ', '-')
    return s

class BasePage(Page):
    """
    Adds additional fields to the wagtail Page model.
    Most other content types should extend this model
    instead of Page.
    """
    # Fields 

    start_sidebar_from_here = models.BooleanField(default=False)

    show_sidebar = models.BooleanField(default=False)

    last_reviewed = models.DateField(
        'Last Reviewed', 
        null=True, 
        blank=True
    )

    page_maintainer = models.ForeignKey(
        'staff.StaffPage',
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_maintainer'
    )

    editor = models.ForeignKey(
        'staff.StaffPage',
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_editor'
    )

    sort_order = IntegerField(blank=True, default=0)

    # Searchable fields
    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('page_maintainer'),
                FieldPanel('editor'),
                FieldPanel('last_reviewed', None),
                FieldPanel('sort_order')
            ],
            heading='Page Management'
        ),
        MultiFieldPanel(
            [
                FieldPanel('start_sidebar_from_here'),
                FieldPanel('show_sidebar'),
            ],
            heading='Sidebar Menus'
        ),
    ]

    class Meta:
        abstract = True

    def get_context(self, request):
        context = super(BasePage, self).get_context(request)

        breadcrumbs = list(map(lambda p: {'title': p.title, 'url': p.url}, self.get_ancestors(True)))
        # hack to remove the default root page.
        breadcrumbs.pop(0)
        context['breadcrumbs'] = breadcrumbs

        context['sidebartitle'] = 'Browse this Section'
        if self.specific_class.get_verbose_name() == 'Intranet Units Page':
            for p in list(reversed(self.get_ancestors(True))):
                try:
                    if p.specific.start_sidebar_from_here:
                        context['sidebartitle'] = p.title
                except:
                    pass
                
        # JEJ- fix this later to remove logic from the template. 
        '''
        sidebar = [] 
        if self.show_sidebar:
            ancestors = self.get_ancestors(True)
            while ancestors:
                sidebar_parent = ancestors.pop()
                if sidebar_parent.start_sidebar_from_here:
                    break

            for child in sidebar_parent.get_children().in_menu().order_by('title').order_by('sort_order'):
                grandchildren = []
                for grandchild in child.get_children:
                    sidebar.append({
                        'title': child.title,
                        'url': child.url,
                        'children': [],
                    })
        '''
        
        return context


class PublicBasePage(BasePage):
    """
    Adds additional fields to the wagtail Page model.
    Most other content types should extend this model
    instead of Page.
    """
    # Fields 

    #location = models.ForeignKey('public.LocationPage', 
    #    null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'is_building': True}, 
    #    related_name='%(app_label)s_%(class)s_related')

    unit = models.ForeignKey(
        'units.UnitPage', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='%(app_label)s_%(class)s_related'
    )

    content_specialist = models.ForeignKey(
        'staff.StaffPage',
        null=True, 
        blank=False, 
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_content_specialist'
    )

    # Searchable fields
    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('page_maintainer'),
                FieldPanel('editor'),
                FieldPanel('content_specialist'),
                FieldPanel('unit'),
                FieldPanel('last_reviewed', None),
            ],
            heading='Page Management'
        ),
    ]

    class Meta:
        abstract = True

# Global streamfield definitions
class ImageFormatChoiceBlock(FieldBlock):
    """
    Alignment options to use with the ImageBlock.
    """
    field = forms.ChoiceField(choices=(
        ('pull-left', 'Wrap left'), ('pull-right', 'Wrap right'), ('center-block', 'Center'),
    ))

class ImageBlock(StructBlock):
    """
    Image streamfield block.
    """
    image = ImageChooserBlock()
    citation = CharBlock(required=False)
    caption = TextBlock(required=False)
    alt_text = CharBlock(required=False) #Img title in the system is a fallback. 
    alignment = ImageFormatChoiceBlock()
    source = CharBlock(required=False)
    lightbox = BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'image'
        template ='base/blocks/img.html'

class BlockQuoteBlock(StructBlock):
    """
    Blockquote streamfield block.
    """
    quote = TextBlock('quote title')
    attribution = CharBlock()

    class Meta:
        icon = 'openquote'
        template = 'base/blocks/blockquote.html'

class ParagraphBlock(StructBlock):
    """
    Paragraph streamfield block.
    """
    paragraph = RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        form_classname = 'paragraph-block struct-block'
        template = 'base/blocks/paragraph.html'

class CodeBlock(StructBlock):
    """
    Code Highlighting Block
    """

    LANGUAGE_CHOICES = (
        ('bash', 'Bash/Shell'),
        ('css', 'CSS'),
        ('html', 'HTML'),
        ('javascript', 'Javascript'),
        ('json', 'JSON'),
        ('ocaml', 'OCaml'),
        ('php5', 'PHP'),
        ('html+php', 'PHP/HTML'),
        ('python', 'Python'),
        ('scss', 'SCSS'),
        ('yaml', 'YAML'),
    )

    language = ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='default',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))

class DefaultBodyFields(StreamBlock):
    """
    Standard default streamfield options to be shared 
    across content types.
    """
    h2 = CharBlock(icon='title', classname='title', template='base/blocks/h2.html')
    h3 = CharBlock(icon='title', classname='title', template='base/blocks/h3.html')
    h4 = CharBlock(icon='title', classname='title', template='base/blocks/h4.html')
    h5 = CharBlock(icon='title', classname='title', template='base/blocks/h5.html')
    h6 = CharBlock(icon='title', classname='title', template='base/blocks/h6.html')
    paragraph = ParagraphBlock()
    image = ImageBlock(label='Image')
    blockquote = BlockQuoteBlock()
    code = CodeBlock()
    #ordered_list = ListBlock(RichTextBlock(), icon="list-ol")
    #unordered_list = ListBlock(RichTextBlock(), icon="list-ul")

class DefaultBodyField(StreamField):
    """
    We need to get rid of this! Don't use this! 
    """
    def __init__(self, block_types=None, **kwargs):
        block_types = [
            ('heading', CharBlock(classname='full title', icon='title')),
            ('paragraph', RichTextBlock(icon='pilcrow')),
            ('image', ImageChooserBlock(icon='image / picture')),
        ]

        super(DefaultBodyField, self).__init__(block_types, **kwargs)

class IntranetPlainPage(BasePage):
    body = StreamField(DefaultBodyFields())

    subpage_types = ['base.IntranetIndexPage', 'base.IntranetPlainPage']

IntranetPlainPage.content_panels = Page.content_panels + [
    StreamFieldPanel('body')
] + BasePage.content_panels

class IntranetIndexPage(BasePage):
    intro = StreamField(DefaultBodyFields())
    display_hierarchical_listing = models.BooleanField(default=False)
    body = StreamField(DefaultBodyFields())

    subpage_types = ['base.IntranetIndexPage', 'base.IntranetPlainPage']

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
        FieldPanel('display_hierarchical_listing'),
        StreamFieldPanel('body')
    ] + BasePage.content_panels

    def get_context(self, request):
        context = super(IntranetIndexPage, self).get_context(request)

        pages = [{
            'title': self.title,
            'url': self.url,
            'children': [],
        }]

        if self.display_hierarchical_listing:
            def recursively_add_children(page):
                return {
                    'title': page.title,
                    'url': page.url,
                    'children': list(map(lambda p: recursively_add_children(p), page.get_children().live()))
                }
            pages[0]['children'] = list(map(lambda p: recursively_add_children(p), self.get_children().live()))
                
            ''''
            for page in self.get_descendants():
                pages[0]['children'].append({
                    'title': page.title,
                    'url': page.url,
                    'children': []
                })
                ancestors = list(Page.objects.ancestor_of(page)) + [page]
                while True:
                    if not ancestors:
                        break
                    if ancestors.pop(0) == self:
                        break
                currentlevel = pages
                while ancestors:
                    ancestor = ancestors.pop(0)
                    nextlevels = list(filter(lambda g: g['url'] == ancestor.url, currentlevel))
                    if nextlevels:
                        currentlevel = nextlevels[0]['children']
                    else:
                        newnode = {
                            'title': ancestor.title,
                            'url': ancestor.url,
                            'children': [],
                        }
                        currentlevel.append(newnode)
                        currentlevel = newnode['children']
            '''
        else:
            pages[0]['children'] = list(map(lambda p: {'title': p.title, 'url': p.url, 'children': []}, self.get_children()))

        def alphabetize_pages(currentlevel):
            for node in currentlevel:
                node['children'] = alphabetize_pages(node['children'])
            return sorted(currentlevel, key=lambda c: c['title'])
        pages = alphabetize_pages(pages)

        def get_html(currentlevel):
            if not currentlevel:
                return ''
            else:
                return "<ul>" + "".join(list(map(lambda n: "<li><a href='" + n['url'] + "'>" + n['title'] + "</a>" + get_html(n['children']) + "</li>", currentlevel))) + "</ul>"
        pages_html = get_html(pages[0]['children'])
        
        context['pages_html'] = pages_html

        context['pages'] = pages[0]['children']
        context['pages_html'] = pages_html
        return context

class Address(models.Model):
    """
    Reusable address fields.
    """
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal_code_regex = RegexValidator(regex=POSTAL_CODE_FORMAT, message=POSTAL_CODE_ERROR_MSG)
    postal_code = models.CharField(validators=[postal_code_regex], max_length=5, blank=True)

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('address_1'),
                FieldPanel('address_2'),
                FieldPanel('city'),
                FieldPanel('postal_code'),
            ],
            heading='Address'
        ),
    ]

    class Meta:
        abstract = True


class Email(models.Model):
    """
    Reusable email address.
    """
    email = models.EmailField(max_length=254, blank=True)
    
    content_panels = [
        FieldPanel('email'),
    ]

    class Meta:
        abstract = True


class PhoneNumber(models.Model):
    """
    Abstract phone number type.
    """
    phone_label = models.CharField(max_length=25, blank=True)
    phone_regex = RegexValidator(regex=PHONE_FORMAT, message=PHONE_ERROR_MSG)
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)

    content_panels = [
        FieldPanel('phone_label'),
        FieldPanel('phone_number'),
    ]

    class Meta:
        abstract = True


class FaxNumber(models.Model):
    """
    Abstract phone number type.
    """
    phone_regex = RegexValidator(regex=PHONE_FORMAT, message=PHONE_ERROR_MSG)
    fax_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)

    panels = [
        FieldPanel('number'),
    ]

    class Meta:
        abstract = True


class Report(models.Model):
    """
    Model for group and unit reports
    """
    date = models.DateField(blank=False)
    summary = models.TextField(null=False, blank=False)
    link = models.URLField(max_length=254, blank=False, default='')
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('date'),
        FieldPanel('summary'),
        DocumentChooserPanel('document'),
        FieldPanel('link'),
    ]

    class Meta:
        abstract = True


class LinkFields(models.Model):
    """
    Reusable abstract class for general links.
    """
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True 
