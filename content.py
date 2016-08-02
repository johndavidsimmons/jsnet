import datetime

def Content():
    CONTENT_DICT = {

        'name': 'John Simmons',
        'year': datetime.datetime.now().strftime('%Y'),
        'Navigation': [
            ['Blog', '/blog', 'Blog'],
            ['Resume', "/resume", 'Resume'],
            ['Records', '/records', 'Records'],
            ['Maker Challenge', "/makerchallenge", "Maker Challenge"]
        ],
        'Home': {
            'bio': 'My name is John Simmons and I am an information technology professional living in the Detroitish area. I love <a href="/records">vinyl</a>, <a class="sammy">dachshunds</a>, and skateboarding. My  interests are Python for web development and data analysis, user experience analytics, and anything that uses a Raspberry Pi. I also write about Qualtrics on Medium from time to time. I believe that you can\'t build a castle in a day, but you can place one perfect brick at a time.'
        },
        'Resume': [
            ['Quicken Loans', 'http://www.quickenloans.com', 'May 2013 - Present', 'UX Analyst',
             'Studying the relationship between user behavior and business analytics of Quicken Loans client facing web products.'],
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
        'Images': {
            'portrait': '/static/img/john.png',
            'sammy': '/static/img/sam.png'
        },
        'Social': {
            "linkedin": {
                'link': 'https://www.linkedin.com/in/johndavidsimmons',
                'fa': 'fa fa-linkedin-square fa-2x'
            },
            'github': {
                'link': 'https://github.com/johndavidsimmons',
                'fa': 'fa fa-github-square fa-2x',
                'fa1x': 'fa fa-github-square'
            }
        },
        'Maker': {
            'ideas': {
                'done': [
                    'Personal website with resume, projects, bio, etc (You are here!)',
                    '<a href="/blog/Pi-Music-Box">Pi powered Spotify music box</a>',
                    'Twitter Budgeting App (Hackathon Project)',
                    '<a href="https://medium.com/@johndavidsimmons/email-sign-up-widget-in-qualtrics-407c384e5ad3#.79rw5rtu8">A Medium post</a>',
                    '<a href="/blog/Magic-Mirror">Pi Powered Magic Mirror</a>',
                    'A stair ramp for Sammy',
                    'Pi powered FM Radio broadcaster',
                    '<a href="/records">Record collection section</a>',
                    '<a href="/cl">Craigslist Scraper</a>'
                ],
                'in-progress': [
                    'Patterned stairwell'
                ],
                'upcoming': [
                    '<a href="https://amzn.com/w/22OXWTGT6FKCV">Model airplane, car, or helicopter</a>',
                    'A magnetic wall mounted bottle opener',
                    'Socket wrench organizing peg board',
                    'A self portrait'
                    
                ]
            },
            'desc': 'Project ideas for the <a href="http://megamaker.co/challenge/">2016 Maker Challenge</a>'
        }
    }
    return CONTENT_DICT
