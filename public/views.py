from django.shortcuts import render
from public.models import LocationPage, LocationPageFloorPlacement
from wagtail.wagtailimages.models import Image
from public.models import StandardPage
from library_website.settings import PUBLIC_HOMEPAGE, REGENSTEIN_HOMEPAGE, SSA_HOMEPAGE, MANSUETO_HOMEPAGE, CRERAR_HOMEPAGE, ECKHART_HOMEPAGE, DANGELO_HOMEPAGE, SCRC_HOMEPAGE
from base.utils import get_hours_and_location, sort_buildings
from ask_a_librarian.utils import get_chat_status, get_chat_status_css, get_unit_chat_link
from public.utils import get_features, has_feature
from wagtail.wagtailcore.models import Site


def spaces(request):
    building = request.GET.get('building', None)
    feature = request.GET.get('feature', None)
    floor = request.GET.get('floor', None)
    space_type = request.GET.get('space_type', 'is_study_space')

    possible_features = get_features() 

    # validate form input.
    if not building in LocationPage.objects.filter(is_building=True).values_list('title', flat=True):
        building = None
    if not has_feature(feature):
        feature = None
    if not space_type in ['is_study_space', 'is_teaching_space', 'is_event_space']:
        space_type = None

    # get the feature label. 
    feature_label = ''
    if feature:
        for f in possible_features:
            if f[0] == feature:
                feature_label = f[1]

    # get spaces.
    spaces = LocationPage.objects.live()
    if building:
        spaces = spaces.filter(parent_building = LocationPage.objects.get(title=building))
    if feature:
        spaces = spaces.filter(**{feature: True})
    if floor:
        location_ids = LocationPageFloorPlacement.objects.filter(floor__title=floor).values_list('parent', flat=True)
        spaces = spaces.filter(id__in=location_ids)
    if space_type:
        spaces = spaces.filter(**{space_type: True})

    # Narrow down list of buildings from all buildings by using feature
    # and space_type, create list of libraries for display in dropdown
    # from parent_building of filtered all_spaces. Use set to remove
    # duplicates and sort_buildings to organize resulting list of libraries
    all_spaces = LocationPage.objects.live()
    if feature:
        all_spaces = all_spaces.filter(**{feature: True})
    if space_type:
        all_spaces = all_spaces.filter(**{space_type: True})
    buildings = sort_buildings(all_spaces)

    # make sure all features have at least one LocationPage for the current space_type. 
    features = list(filter(lambda f: spaces.filter(**{f[0]: True}), possible_features))

    # if a library building has been set, get floors that are appropriate for
    # the parameters that have been set. 
    floors = []
    if building:
        # Changed spaces to all_spaces in id_list to bypass filtering in spaces.
        # get all locations that are descendants of this building. 
        id_list = all_spaces.filter(parent_building__title=building).values_list('pk', flat=True)
        # get a unique, sorted list of the available floors here. 
        floors = sorted(list(set(LocationPageFloorPlacement.objects.filter(parent__in=id_list).exclude(floor=None).values_list('floor__title', flat=True))))

    default_image = Image.objects.get(title="Default Placeholder Photo")
    #If building is selected pass respective page id to page context variables,
    #else pass PUBLIC_HOMEPAGE, llid passed to render correct hours in js script,
    friendly_name, unfriendly_a = '', False
    PAGE_ID, llid = PUBLIC_HOMEPAGE, 1357
    if building:
        if building == 'Social Service Administration Library':
            PAGE_ID = SSA_HOMEPAGE
            friendly_name = ' SSA '
            unfriendly_a = True
            llid = 1380
        elif building == 'The Joe and Rika Mansueto Library':
            PAGE_ID = MANSUETO_HOMEPAGE
            llid = 1379
        elif building == 'The John Crerar Library':
            PAGE_ID = CRERAR_HOMEPAGE
            friendly_name = ' Science '
            llid = 1373
        elif building == 'Eckhart Library':
            PAGE_ID = ECKHART_HOMEPAGE
            llid = 1377
        elif building == 'The D\'Angelo Law Library':
            PAGE_ID = DANGELO_HOMEPAGE
            friendly_name = ' Law '
            llid = 1378
        elif building == 'Special Collections Research Center':
            PAGE_ID = SCRC_HOMEPAGE
            llid = 2449
    # Page context variables for templates
    home_page = StandardPage.objects.live().get(id=PAGE_ID)
    location_and_hours = get_hours_and_location(home_page)
    location = str(location_and_hours['page_location'])
    unit = location_and_hours['page_unit']

    # Find banner for given home_page and add to context
    current_site = Site.find_for_request(request)
    section_info = home_page.get_banner(current_site)
    branch_name = section_info[4]
    return render(request, 'public/spaces_index_page.html', {
        'building': building,
        'buildings': buildings,
        'breadcrumb_div_css': 'col-md-12 breadcrumbs hidden-xs hidden-sm',
        'content_div_css': 'container body-container col-xs-12 col-lg-11 col-lg-offset-1',
        'default_image': default_image,
        'feature': feature,
        'feature_label': feature_label,
        'features': features,
        'floor': floor,
        'floors': floors,
        'self': {
            'title': 'Library Spaces',
            'friendly_name': friendly_name
        },
        'spaces': spaces,
        'space_type': space_type,
        'page_unit': str(unit),
        'page_location': location,
        'address': location_and_hours['address'],
        'chat_url': get_unit_chat_link(unit, request),
        'chat_status': get_chat_status('uofc-ask'),
        'chat_status_css': get_chat_status_css('uofc-ask'),
        'hours_page_url': home_page.get_hours_page(request),
        'unfriendly_a': unfriendly_a,
        'libcalid': llid,
        'has_banner': section_info[0],
        'banner': section_info[1],
        'banner_title': section_info[2],
        'banner_url': section_info[3],
        'branch_lib_css': home_page.get_branch_lib_css_class(),
    })
