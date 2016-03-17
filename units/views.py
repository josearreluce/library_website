from django.shortcuts import render
from django.utils.html import escape
from units.models import UnitPage

def units(request):
    hierarchical_units = UnitPage.heirarchical_units()

    # JEJ
    def get_unit_info(unit_page):
        h = ''
        #h = h + unit_page.get_short_name() + "<br/>"

        # phone number
        if unit_page.phone_number:
            if unit_page.phone_label:
                h = h + '<em>' + unit_page.phone_label + ':' + '</em> '
            h = h + unit_page.phone_number 
            h = h + '<br/>'

        # fax_number  
        if unit_page.fax_number:
            h = h + 'Fax: ' + unit_page.fax_number + '<br/>'

        # email_label, email
        if unit_page.email:
            if unit_page.email_label:
                h = h + unit_page.email_label + ': '
            h = h + unit_page.email

        # link_text, link_page
        if unit_page.link_page:
            if unit_page.link_text:
                h = h + unit_page.link_text + ': '
            h = h + unit_page.link_page.url
        return h
        
    # hierarchical html. e.g.,
    # <ul>
    #   <li>Administration</li>
    #   <li>Collection Services
    #      <ul>
    #         <li>Administration</li>
    # ...
    def get_html(tree):
        if not tree:
            return ''
        else:
            return "<ul>" + "".join(list(map(lambda t: "<li>" + (t.unit_page.get_short_name() + "<br/>" if t.unit_page else "") + get_unit_info(t.unit_page) + get_html(t) + "</li>", tree.children))) + "</ul>"
    hierarchical_html = get_html(hierarchical_units)

    # alphabetical units. 
    alphabetical_html = '<table>'
    for unit_page in UnitPage.objects.filter(display_in_directory=True).extra(select={'lc': 'lower(alphabetical_directory_name)'}).order_by('lc'):
        alphabetical_html = alphabetical_html + '<tr>'
        alphabetical_html = alphabetical_html + '<td><strong>' + unit_page.alphabetical_directory_name + '</strong></td>'
        alphabetical_html = alphabetical_html + '<td>'
        alphabetical_html = alphabetical_html + get_unit_info(unit_page)
        alphabetical_html = alphabetical_html + '</td>'
        alphabetical_html = alphabetical_html + '</tr>'
    alphabetical_html = alphabetical_html + '</table>'

    return render(request, 'units/unit_index_page.html', {
        'alphabetical_units': alphabetical_html,
        'hierarchical_units': hierarchical_html
    })
