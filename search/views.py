from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from intranethome.models import IntranetHomePage
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query
from wagtail.contrib.wagtailsearchpromotions.models import SearchPromotion

def loop_search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        sandbox = IntranetHomePage.objects.get(title__contains='Sandbox')
        search_results = Page.objects.live().not_descendant_of(sandbox).search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()

        # Get search picks
        search_picks = query.editors_picks.all()
    else:
        search_results = Page.objects.none()
        search_picks = SearchPromotion.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/loop_search.html', {
        'search_query': search_query,
        'search_results': search_results,
        'search_picks': search_picks,
    })
