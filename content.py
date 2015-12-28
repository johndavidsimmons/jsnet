def Content():
	CONTENT_DICT = {
					'Navigation':[
									['Home', "/", "John Simmons"],
									['Resume', "/resume", 'Resume'],
									['Projects', '/projects', 'Projects'],
								],	
					'Home':{
							'bio' : 'My name is John Simmons and I am a 30-something information technology professional living in the Detroitish area. I love <a href="http://howsyouredge.com/swap/display.php?page=1405">punk vinyl</a>, dachshunds, and skateboarding. My professional pastimes are Python for web development and data analysis, user experience analytics, and anything that uses a Raspberry Pi. I would rather be a carpenter than an architect.'
								},
					'Resume': [
								['Quicken Loans', 'http://www.quickenloans.com', 'May 2013 - Present', 'UX Analyst', 'Studying the relationship between user behavior and business analytics of Quicken Loans client facing web products.'],
								['University of Michigan Library', 'http://www.lib.umich.edu/library-information-technology/design-discovery', 'January 2013 - May 2013', 'UX Intern', "As an intern I helped prototype and test new layouts, and manage website content for library's many web domains."],
								['University of Michigan Library', 'http://www.lib.umich.edu/scholarspace', 'August 2012 - December 2013', 'Technology Assistant', 'Library technologists functioned as drop in tech-support staff that helped patrons use Photoshop, install drivers, build websites, and everything in-between.'],
								['Schawk', 'http://www.schawk.com/', 'August 2011 - August 2012', 'Production Artist', 'More of a builder than a designer; I prepared digital art files for printing for clients such as Pepsi, Mars, and other high profile companies.']
							],
						'Education':[
										['University of Michigan', 'https://www.si.umich.edu/', "MS Information", "December 2013", 'The focus of my coursework at UMSI was user experience methodology, behavioral psychology, and web development.'],
										['Western Michigan University', 'https://wmich.edu/academics/undergraduate/graphic-printing', "BS Imaging", "May 2010", 'The Imaging program at WMU focused on the business and technical aspects side of commercial printing.']
									],
					'Projects' : {
							'name' : 'Coming soon...'
						},
					'Images' : {
						'portrait' : 'static/img/john.png'
						},
					'Social' : {
							'facebook' : {
								'link' : 'https://www.facebook.com/john.simmons.737',
								'fa' : 'fa fa-facebook-square fa-4x'
							},
							"linkedin" : {
								'link' : 'https://www.linkedin.com/in/johndavidsimmons',
								'fa' : 'fa fa-linkedin-square fa-4x'
							},
							'github' : {
								'link' : 'https://github.com/johndavidsimmons',
								'fa' : 'fa fa-github-square fa-4x'
							},
							'twitter' : {
								'link' : 'https://twitter.com/johnsimmons517',
								'fa' : 'fa fa-twitter-square fa-4x'
							}
						}
					}
	return CONTENT_DICT