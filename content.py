import datetime

def Content():
    CONTENT_DICT = {
        'year': datetime.datetime.now().strftime('%Y'),
        'Resume': [
            ['Bounteous', 'https://www.bounteous.com', '', 'Adobe Analytics Engineer', "As an Adobe Analytics Engineer, my goal is to deliver data collection solutions that are nothing less than excellent in order to exceed our clients expectations." ]
            # ['Quicken Loans', 'http://www.quickenloans.com', 'August 2016 - August 2019', 'Analytics Developer', "Part strategist, part developer; I am responsible for maintaining Quicken Loans' web analytics tools (Adobe Analytics, Google Analytics, DTM/Launch, mParticle, Qualtrics, etc.)." ],
            # ['Quicken Loans', 'http://www.quickenloans.com', 'May 2013 - August 2016', 'UX Analyst',
            #  'I provided insights on the relationship between user behavior and business analytics of Quicken Loans\' client facing web products.'],
            # ['University of Michigan Library',
            #  'http://www.lib.umich.edu/library-information-technology/design-discovery', 'January 2013 - May 2013',
            #  'UX Intern',
            #  "As an intern I helped prototype and test new layouts, and manage website content for library's many web domains."],
            # ['University of Michigan Library', 'http://www.lib.umich.edu/scholarspace', 'August 2012 - December 2013',
            #  'Technology Assistant',
            #  'Library technologists functioned as drop in tech-support staff that helped patrons use Photoshop, install drivers, build websites, and everything in-between.'],
            # ['Schawk', 'http://www.schawk.com/', 'August 2011 - August 2012', 'Production Artist',
            #  'More of a builder than a designer; I prepared digital art files for printing for clients such as Pepsi, Mars, and other high profile companies.']
        ],
        # 'Education': [
        #     ['University of Michigan', 'https://www.si.umich.edu/', "MS Information", "December 2013",
        #      'The focus of my coursework at UMSI was user experience methodology, behavioral psychology, and web development.'],
        #     ['Western Michigan University', 'https://wmich.edu/academics/undergraduate/graphic-printing', "BS Imaging",
        #      "May 2010",
        #      'The Imaging program at WMU focused on the business and technical aspects commercial printing.']
        # ],
    }
    return CONTENT_DICT
