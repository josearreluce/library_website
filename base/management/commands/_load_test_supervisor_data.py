from directory_unit.models import DirectoryUnit, UnitSupervisor
from staff.models import StaffPage

unit_supervisor_pairs = [
    ["D'Angelo Law Library - Law Technical Services", "Julie R. Stauffer"],
    ["D'Angelo Law Library - Law User Services - Access Services", "Holly Lipschultz"],
    ["D'Angelo Law Library - Law User Services - Reference", "William A. Schwesig"],
    ["Special Collections Research Center - SCRC Collection Management", "Patti Gibbons"],
    ["Special Collections Research Center - SCRC Exhibits", "Joseph T Scott"],
    ["Special Collections Research Center - SCRC Rare Books", "Catherine Uecker"],
    ["Digital Services", "Elisabeth Long"],
    ["Digital Services - Digital Library Development Center (DLDC)", "Charles Blair"],
    ["Area Studies, Humanities, and Social Sciences - African Studies", "Ellen Bryan"],
    ["Area Studies, Humanities, and Social Sciences - Ancient Near East", "Catherine M. Mardikes"],
    ["Area Studies, Humanities, and Social Sciences - Art and Architecture", "Nancy Spiegel"],
    ["Area Studies, Humanities, and Social Sciences - Business and Economics", "Jeffry D. Archer"],
    ["Area Studies, Humanities, and Social Sciences - Cinema and Media Studies", "Nancy Spiegel"],
    ["Area Studies, Humanities, and Social Sciences - Classics", "Catherine M. Mardikes"],
    ["Area Studies, Humanities, and Social Sciences - Dance", "Scott Landvatter"],
    ["Area Studies, Humanities, and Social Sciences - East Asian Collection", "Jee-Young Park"],
    ["Area Studies, Humanities, and Social Sciences - Geography", "Christopher Winters"],
    ["Area Studies, Humanities, and Social Sciences - Government Documents", "Paul Belloni"],
    ["Area Studies, Humanities, and Social Sciences - History", "Nancy Spiegel"],
    ["Area Studies, Humanities, and Social Sciences - International Relations", "Sarah Hogan"],
    ["Area Studies, Humanities, and Social Sciences - Latin American Studies", "Sarah G. Wenzel"],
    ["Area Studies, Humanities, and Social Sciences - Literature", "June P. Farris"],
    ["Area Studies, Humanities, and Social Sciences - Map Collection", "Christopher Winters"],
    ["Area Studies, Humanities, and Social Sciences - Music", "Scott Landvatter"],
    ["Area Studies, Humanities, and Social Sciences - Philosophy", "Anne Knafl"],
    ["Area Studies, Humanities, and Social Sciences - Political Science", "Sarah Hogan"],
    ["Area Studies, Humanities, and Social Sciences - Public Policy", "Sarah Hogan"],
    ["Area Studies, Humanities, and Social Sciences - Religion", "Anne Knafl"],
    ["Area Studies, Humanities, and Social Sciences - Southern Asia Studies", "James Nye"],
    ["Area Studies, Humanities, and Social Sciences - Theater", "Sarah G. Wenzel"],
    ["Science Libraries", "Andrea Twiss-Brooks"],
    ["Science Libraries", "Barbara Kern"],
    ["Science Libraries - Astronomy and Astrophysics", "Barbara Kern"],
    ["Science Libraries - Chemistry", "Andrea Twiss-Brooks"],
    ["Science Libraries - Computer Science", "Jennifer Hart"],
    ["Science Libraries - Geophysical Sciences", "Andrea Twiss-Brooks"],
    ["D'Angelo Law Library", "Sheri Lewis"],
    ["D'Angelo Law Library - Law User Services", "Margaret A. Schilt"],
    ["Special Collections Research Center", "Daniel Meyer"],
    ["Special Collections Research Center - SCRC Archives and Manuscripts", "Eileen Ielmini"],
    ["Area Studies, Humanities, and Social Sciences", "Catherine M. Mardikes"],
    ["Area Studies, Humanities, and Social Sciences - African American Studies", "Ellen Bryan"],
    ["Area Studies, Humanities, and Social Sciences - Anthropology", "Christopher Winters"],
    ["Area Studies, Humanities, and Social Sciences - Chicago Jazz Archive", "Scott Landvatter"],
    ["Area Studies, Humanities, and Social Sciences - Contemporary Fiction, English and American", "Sarah G. Wenzel"],
    ["Area Studies, Humanities, and Social Sciences - East European Collection", "June P. Farris"],
    ["Science Libraries - Medicine", "Debra A Werner"],
    ["Science Libraries - Nursing", "Debra A Werner"],
    ["Science Libraries - Organismal Biology and Anatomy", "Debra A Werner"],
    ["Science Libraries - Physics", "Barbara Kern"],
    ["Science Libraries - Science and Medicine, History of", "Debra A Werner"],
    ["Science Libraries - Statistics", "Jennifer Hart"],
    ["User Services - Access Services", "David K. Larsen"],
    ["User Services - Access Services - Assessment", "Elizabeth Edwards"],
    ["User Services - Access Services - ID & Privileges Office & Entry Control", "Edd Merkel"],
    ["User Services - Dissertation Office", "Ellen Bryan"],
    ["User Services - Reference, Instruction, and Outreach", "Jeffry D. Archer"],
    ["Adminstrative Services - Shipping and Receiving", "Terry Banks"],
    ["Collection Services - Administrative and Desktop Systems (ADS)", "David Farley"],
    ["Collection Services - Electronic Resources Management (ERM)", "Kristin Martin"],
    ["Collection Services - Integrated Library Systems (ILS)", "Tod Olson"],
    ["Collection Services - Preservation - Binding & Shelf Preparations", "Amy Mantrone"],
    ["Collection Services - Preservation - Digitization", "Kathleen Arthur"],
    ["Area Studies, Humanities, and Social Sciences - Gay and Lesbian Studies", "Julia Gardner"],
    ["Area Studies, Humanities, and Social Sciences - Humanities, General", "Catherine M. Mardikes"],
    ["Area Studies, Humanities, and Social Sciences - Jewish Studies", "Anne Knafl"],
    ["Area Studies, Humanities, and Social Sciences - Linguistics, General", "June P. Farris"],
    ["Area Studies, Humanities, and Social Sciences - Middle Eastern Studies", "Marlis J. Saleh"],
    ["Area Studies, Humanities, and Social Sciences - Psychology and Human Development", "Paul Belloni"],
    ["Area Studies, Humanities, and Social Sciences - Slavic and East European Studies", "June P. Farris"],
    ["Area Studies, Humanities, and Social Sciences - Sociology", "Sarah Hogan"],
    ["Area Studies, Humanities, and Social Sciences - Women's Studies", "Julia Gardner"],
    ["Science Libraries - Biochemistry and Molecular Biology", "Debra A Werner"],
    ["Science Libraries - Eckhart Library", "Jennifer Hart"],
    ["Science Libraries - Mathematics", "Jennifer Hart"],
    ["User Services", "James Vaughan"],
    ["User Services - Access Services - Regenstein Circulation", "Will Degenhard"],
    ["Administration - Communications", "Rachel Rosenberg"],
    ["Collection Services", "James Mouw"],
    ["Collection Services - Preservation", "Sherry Byrne"],
    ["Collection Services - Preservation - Conservation", "Ann Lindsey"]
]

for pair in unit_supervisor_pairs:
    unit_fullname = pair[0]
    staffpage_title = pair[1]
    UnitSupervisor.objects.create(
        unit=DirectoryUnit.objects.get(fullName=unit_fullname),
        supervisor=StaffPage.objects.get(title=staffpage_title)
    )


