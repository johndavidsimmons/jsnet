import datetime
import os
import cloudinary as Cloud

Cloud.config.update = ({
    'cloud_name':os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
})

width = {"width":600}

pibox = Cloud.CloudinaryImage("finalbox_g5av0y.png")
pibox.url_options.update(width)

magicmirror = Cloud.CloudinaryImage("magicmirror.jpg")
magicmirror.url_options.update(width)

pipeshelf = Cloud.CloudinaryImage("pipeshelf.jpg")
pipeshelf.url_options.update(width)



def Content():
    CONTENT_DICT = {
        'year': datetime.datetime.now().strftime('%Y'),
        'Resume': [
            ['Quicken Loans', 'http://www.quickenloans.com', 'August 2016 - Present', 'Data Analytics Developer', "Part data analyst, part web developer; I am responsible for coding Quicken Loans' web analytics tools (Omniture, Google Analytics, DTM, Qualtrics)." ],
            ['Quicken Loans', 'http://www.quickenloans.com', 'May 2013 - August 2016', 'UX Analyst',
             'I provided insights on the relationship between user behavior and business analytics of Quicken Loans\' client facing web products.'],
            ['University of Michigan Library',
             'http://www.lib.umich.edu/library-information-technology/design-discovery', 'January 2013 - May 2013',
             'UX Intern',
             "As an intern I helped prototype and test new layouts, and manage website content for library's many web domains."],
            ['University of Michigan Library', 'http://www.lib.umich.edu/scholarspace', 'August 2012 - December 2013',
             'Technology Assistant',
             'Library technologists functioned as drop in tech-support staff that helped patrons use Photoshop, install drivers, build websites, and everything in-between.'],
            ['Schawk', 'http://www.schawk.com/', 'August 2011 - August 2012', 'Production Artist',
             'More of a builder than a designer; I prepared digital art files for printing for clients such as Pepsi, Mars, and other high profile companies.']
        ],
        'Education': [
            ['University of Michigan', 'https://www.si.umich.edu/', "MS Information", "December 2013",
             'The focus of my coursework at UMSI was user experience methodology, behavioral psychology, and web development.'],
            ['Western Michigan University', 'https://wmich.edu/academics/undergraduate/graphic-printing', "BS Imaging",
             "May 2010",
             'The Imaging program at WMU focused on the business and technical aspects commercial printing.']
        ],
        'todo': {
            '2017': {
                'done': [
                    ('Pipe Shelf', pipeshelf.url),
                    "BJJ Belt Stripes",
                    "Raspberry Pi Security Camera",
                    "Raspberry Pi Google Assistant"

                ],
                'upcoming': [
                    'Raspberry Pi Photo Booth',
                    "Self Portrait",
                    "Learn to juggle",
                    "Earn some Bitcoin",
                    "Smoke a turkey"
                ]
            },
            '2016': {
                'done': [
                    'Personal website with resume, projects, bio, etc (You are here!)',
                    ('Pi powered Spotify music box', pibox.url),
                    'Twitter Budgeting App (Hackathon Project)',
                    ('A Medium post', 'https://medium.com/@johndavidsimmons/email-sign-up-widget-in-qualtrics-407c384e5ad3#.79rw5rtu8'),
                    ('Pi Powered Magic Mirror', magicmirror.url),
                    'A stair ramp for Sammy',
                    'Pi powered FM Radio broadcaster',
                    ('Record collection website', "http://www.recordbin.online"),
                    'Craigslist Scraper'
                ],
                'upcoming': [
                    'Patterned stairwell',
                    ('Model airplane, car, or helicopter','https://amzn.com/w/22OXWTGT6FKCV'),
                    'A magnetic wall mounted bottle opener',
                    'Socket wrench organizing peg board',
                    'A self portrait'
                    
                ]
            }
            }
    }
    return CONTENT_DICT
