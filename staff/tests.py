from base.utils import get_xml_from_directory_api
from directory_unit.models import DirectoryUnit
from django.test import TestCase
from io import StringIO
from lxml import etree
from staff.utils import get_all_library_cnetids_from_directory, get_individual_info_from_directory


class UniversityDirectoryTestCase(TestCase):
    def test_directory_xml_validates(self):
        dtd = etree.DTD(StringIO("""
        <!ELEMENT responseData    (response, totalResults, organizations)>
        <!ELEMENT response        (#PCDATA)>
        <!ELEMENT totalResults    (#PCDATA)>
        <!ELEMENT organizations   (organization+)>
        <!ELEMENT organization    (name, type, departments, members, resources)>
        <!ELEMENT name            (#PCDATA)>
        <!ELEMENT type            (#PCDATA)>
        <!ELEMENT departments     (department+)>
        <!ELEMENT department      (name, resources)>
        <!--      name (see above) -->
        <!ELEMENT resources       (directoryURL, xmlURL)>
        <!ELEMENT directoryURL    (#PCDATA)>
        <!ELEMENT xmlURL          (#PCDATA)>
        <!ELEMENT members         (member+)>
        <!ELEMENT member          (name, displayName, cnetid, chicagoid, title, email, phone, facultyExchange, resources)>
        <!--      name (see above) -->
        <!ELEMENT displayName     (#PCDATA)>
        <!ELEMENT cnetid          (#PCDATA)>
        <!ELEMENT chicagoid       (#PCDATA)>
        <!ELEMENT title           (#PCDATA)>
        <!ELEMENT email           (#PCDATA)>
        <!ELEMENT phone           (#PCDATA)>
        <!ELEMENT facultyExchange (#PCDATA)>
        <!--      resources (see above) -->
        """))

        root = etree.XML(get_xml_from_directory_api('https://directory.uchicago.edu/api/v2/divisions/16.xml'))
        self.assertEqual(dtd.validate(root), True)

    def test_individual_xml_validates(self):
        dtd = etree.DTD(StringIO("""
        <!ELEMENT responseData    (response, totalResults, individuals)>
        <!ELEMENT response        (#PCDATA)>
        <!ELEMENT totalResults    (#PCDATA)>
        <!ELEMENT individuals     (individual+)>
        <!ELEMENT individual      (name, displayName, cnetid, chicagoid, contacts, resources)>
        <!ELEMENT name            (#PCDATA)>
        <!ELEMENT displayName     (#PCDATA)>
        <!ELEMENT cnetid          (#PCDATA)>
        <!ELEMENT chicagoid       (#PCDATA)>
        <!ELEMENT contacts        (contact)>
        <!ELEMENT contact         (title, division, department, subDepartment, email, phone, facultyExchange)>
        <!ELEMENT title           (#PCDATA)>
        <!ELEMENT division        (name, resources)>
        <!ELEMENT resources       (directoryURL, xmlURL)>
        <!ELEMENT directoryURL    (#PCDATA)>
        <!ELEMENT xmlURL          (#PCDATA)>
        <!ELEMENT department      (name, resources)>
        <!ELEMENT subDepartment   (name, resources)>
        <!ELEMENT email           (#PCDATA)>
        <!ELEMENT phone           (#PCDATA)>
        <!ELEMENT facultyExchange (#PCDATA)>
        """))

        cnetids = get_all_library_cnetids_from_directory()
        root = etree.XML(get_xml_from_directory_api('https://directory.uchicago.edu/api/v2/individuals/' + cnetids[0] + '.xml'))
        self.assertEqual(dtd.validate(root), True)

    def test_get_all_library_cnet_ids_from_directory_two_staff(self):
        xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <responseData>
          <response>Success</response>
          <totalResults>1</totalResults>
          <organizations>
            <organization>
              <name>Library</name>
              <type>Division</type>
              <departments>
                <department>
                  <name>Digital Services</name>
                  <resources>
                    <directoryURL>https://directory.uchicago.edu/organizations/575?type=departments</directoryURL>
                    <xmlURL>https://directory.uchicago.edu/api/v2/departments/575</xmlURL>
                  </resources>
                </department>
              </departments>
              <members>
                <member>
                  <name>Scooter McDanger</name>
                  <displayName>Scooter McDanger</displayName>
                  <cnetid>danger</cnetid>
                  <chicagoid>12345678L</chicagoid>
                  <title>Programmer/Analyst</title>
                  <email>danger@uchicago.edu</email>
                  <phone>(773) 702-1234</phone>
                  <facultyExchange>JRL 220</facultyExchange>
                  <resources>
                    <directoryURL>https://directory.uchicago.edu/individuals/12345678L</directoryURL>
                    <xmlURL>https://directory.uchicago.edu/api/v2/individuals/12345678L</xmlURL>
                  </resources>
                </member>
                <member>
                  <name>Margaret Lovelee</name>
                  <displayName>Margaret Lovelee</displayName>
                  <cnetid>lovelee</cnetid>
                  <chicagoid>12345678L</chicagoid>
                  <title>Programmer/Analyst</title>
                  <email>lovelee@uchicago.edu</email>
                  <phone>(773) 702-1234</phone>
                  <facultyExchange>JRL 220</facultyExchange>
                  <resources>
                    <directoryURL>https://directory.uchicago.edu/individuals/12345678L</directoryURL>
                    <xmlURL>https://directory.uchicago.edu/api/v2/individuals/12345678L</xmlURL>
                  </resources>
                </member>
              </members>
              <resources>
                <directoryURL>https://directory.uchicago.edu/organizations/16?type=divisions</directoryURL>
                <xmlURL>https://directory.uchicago.edu/api/v2/divisions/16</xmlURL>
              </resources>
            </organization>
          </organizations>
        </responseData>
        """

        cnetids = get_all_library_cnetids_from_directory(xml_string)

        self.assertEqual(set(cnetids), set(('lovelee', 'danger')))

    def assertInfoEqual(self, a, b):
        for field in ['cnetid', 'officialName', 'displayName']:
            if not a[field] == b[field]:
                return False

        tds_a = sorted([a['title_department_subdepartments']])
        tds_b = sorted([b['title_department_subdepartments']])

        if not len(tds_a) == len(tds_b):
            return False

        t = 0
        while t < len(tds_a):
            if not tds_a[t] == tds_b[t]:
                return False
            t = t + 1

        tds_a = sorted(a['title_department_subdepartments_dicts'], key = lambda t: t['title'] + t['department'])
        tds_b = sorted(b['title_department_subdepartments_dicts'], key = lambda t: t['title'] + t['department'])

        if not len(tds_a) == len(tds_b):
            return False

        t = 0
        while t < len(tds_a):
            for field in ['department', 'title', 'email', 'facultyexchange', 'phone']:
                if not tds_a[t][field] == tds_b[t][field]:
                    return False
            t = t + 1

        return True

    def test_get_individual_info_from_directory(self):
        self.maxDiff = None

        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <responseData>
          <response>Success</response>
          <totalResults>1</totalResults>
          <individuals>
            <individual>
              <name>Scooter McDanger</name>
              <displayName>Scooter McDanger</displayName>
              <cnetid>scootermcdanger</cnetid>
              <chicagoid>12345678X</chicagoid>
              <contacts>
                <contact>
                  <title>Programmer Analyst</title>
                  <division>
                    <name>Library</name>
                    <resources>
                      <directoryURL>https://directory.uchicago.edu/organizations/16?type=divisions</directoryURL>
                      <xmlURL>https://directory.uchicago.edu/api/v2/divisions/16</xmlURL>
                    </resources>
                  </division>
                  <email>scootermcdanger@uchicago.edu</email>
                  <phone>(773) 702-1234</phone>
                  <facultyExchange>JRL 220</facultyExchange>
                </contact>
              </contacts>
              <resources>
                <directoryURL>https://directory.uchicago.edu/individuals/12345678X</directoryURL>
                <xmlURL>https://directory.uchicago.edu/api/v2/individuals/12345678X</xmlURL>
              </resources>
            </individual>
          </individuals>
        </responseData>
        """

        DirectoryUnit.objects.create(
            name = "Library",
            fullName = "Library",
            parentUnit = None,
            xmlUrl = "https://directory.uchicago.edu/api/v2/divisions/16"
        )

        info = {
            'cnetid': 'scootermcdanger',
            'officialName': 'Scooter McDanger',
            'displayName': 'Scooter McDanger',
            'title_department_subdepartments': {'Programmer Analyst\nLibrary\nJRL 220\n773-702-1234'},
            'title_department_subdepartments_dicts': [{
                'department': DirectoryUnit.objects.get(name='Library'),
                'title': 'Programmer Analyst',
                'email': 'scootermcdanger@uchicago.edu',
                'facultyexchange': 'JRL 220',
                'phone': '773-702-1234'
            }]
        }

        self.assertInfoEqual(get_individual_info_from_directory(xml), info)
    


