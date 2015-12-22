from datetime import datetime

from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone

from base.models import BasePage, DefaultBodyFields
from staff.models import StaffPage

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class NewsPage(BasePage):
    """
    News story content type used on intranet pages.
    """
    excerpt = RichTextField(blank=True, null=True)
    author = models.ForeignKey(
        'staff.StaffPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='news_stories'
    )
    story_date = models.DateField(default=timezone.now)
    sticky_until = models.DateField(blank=True, null=True)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    body = StreamField(DefaultBodyFields(), blank=False, null=False)

    content_panels = Page.content_panels + [ 
        FieldPanel('excerpt'),
        FieldPanel('author'),
        FieldPanel('story_date'),
        FieldPanel('sticky_until'),
        ImageChooserPanel('thumbnail'),
        StreamFieldPanel('body'),
    ] + BasePage.content_panels

class NewsIndexPage(BasePage):
    """
    Index page for intranet news stories.
    """
    intro = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ] + BasePage.content_panels

    subpage_types = ['news.NewsPage']

    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)
        # need to add order_by('story_date')

        sticky_pages = []
        for sticky_page in NewsPage.objects.live().exclude(sticky_until=None):

            # skip sticky stories that have 'expired'.
            if sticky_page.sticky_until and datetime.date(datetime.now()) > sticky_page.sticky_until:
                continue

            day = int(sticky_page.story_date.strftime('%d'))
            if 4 <= day <= 20 or 24 <= day <= 30:
                suffix = "th"
            else:
                suffix = ["st", "nd", "rd"][day % 10 - 1]

            if sticky_page.author:
                author_title = sticky_page.author.title
                author_url = sticky_page.author.url
            else:
                cnetid = sticky_page.owner.username
                author_title = StaffPage.objects.get(cnetid=cnetid).title
                author_url = StaffPage.objects.get(cnetid=cnetid).url

            sticky_pages.append({
                'story_date_sort': sticky_page.story_date,
                'story_date': sticky_page.story_date.strftime('%B %d').replace(' 0', ' ') + suffix,
                'author_title': author_title,
                'author_url': author_url,
                'excerpt': sticky_page.excerpt,
                'title': sticky_page.title,
                'url': sticky_page.url,
                'body': sticky_page.body
            })
        sticky_pages = sorted(sticky_pages, key=lambda p: p['story_date_sort'] )
        if sticky_pages:
            sticky_pages = [sticky_pages.pop(0)]

        news_pages = []
        for news_page in NewsPage.objects.live():
            # skip stories that are in the future. 
            if news_page.story_date > datetime.date(datetime.now()):
                continue

            # skip active sticky stories. 
            if news_page.sticky_until and datetime.date(datetime.now()) < news_page.sticky_until:
                continue

            day = int(news_page.story_date.strftime('%d'))
            if 4 <= day <= 20 or 24 <= day <= 30:
                suffix = "th"
            else:
                suffix = ["st", "nd", "rd"][day % 10 - 1]

            if news_page.author:
                author_title = news_page.author.title
                author_url = news_page.author.url
            else:
                cnetid = news_page.owner.username
                author_title = StaffPage.objects.get(cnetid=cnetid).title
                author_url = StaffPage.objects.get(cnetid=cnetid).url

            # sticky_until
            
            news_pages.append({
                'story_date_sort': news_page.story_date,
                'story_date': news_page.story_date.strftime('%B %d').replace(' 0', ' ') + suffix,
                'author_title': author_title,
                'author_url': author_url,
                'excerpt': news_page.excerpt,
                'title': news_page.title,
                'url': news_page.url,
                'body': news_page.body
            })
        news_pages = sorted(news_pages, key=lambda p: p['story_date_sort'])

        context['sticky_pages'] = sticky_pages
        context['news_pages'] = news_pages
        return context
