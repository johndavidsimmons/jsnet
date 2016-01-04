def Content():
	CONTENT_DICT = {
					
					'name' : 'John Simmons',
					'Navigation':[
									['Home', "/", "John Simmons"],
									['Resume', "/resume", 'Resume'],
									['Projects', '/projects', 'Projects'],
								],	
					'Home':{
							'bio' : 'My name is John Simmons and I am an information technology professional living in the Detroitish area. I love <a href="http://howsyouredge.com/swap/display.php?page=1405" target="_blank">vinyl</a>, <a class="sammy">dachshunds</a>, and skateboarding. My professional pastimes are Python for web development and data analysis, user experience analytics, and anything that uses a Raspberry Pi. I believe that you can\'t build a castle in a day, but you can lay one perfect brick at a time.'
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
							# 'musicbox' : {
							# 	'name' : 'Pi Music Box',
							# 	'img' : 'static/img/product.png',
							# 	'desc' : 'A Spotify connected Raspberry Pi powered music box'
							# },
							'ebayscraper' : {
								'name' : 'Ebay Scraper',
								'link' : 'https://github.com/johndavidsimmons/ebayscrape',
								'img' : ['static/img/ebaypy.png','static/img/scrape.png', 'static/img/spread.png', 'static/img/tweet.png'],
								'overview' : "Problem: There are a lot of records I want. As much as I would like to, I do not have time to constantly search eBay for them. Also, a good portion of my want list are rare titles that: do not come up for auction very often thus searching for them typically yields no results. Solution: Remove myself from the equation. Create a list of search queries, search eBay automatically, and return a list of results. Sounds like a perfect job for a web scraper.",
								'details' : "First, the easy part, I made a plain text file of searches I want to perform. Then, for each search query I use <a href='http://wwwsearch.sourceforge.net/mechanize/'>Mechanize</a> to traverse and search eBay and <a href='http://www.crummy.com/software/BeautifulSoup/'>Beautiful Soup</a> to parse the page of search results. After the results are collected, the <a href='https://github.com/burnash/gspread'>gspread</a> library posts them to a <a href='https://docs.google.com/spreadsheets/d/13oj2hpTJL9blQJdxg4g3A1sM09LEnKCgACZuDio1BXA/edit#gid=1087720188'>Google Spreadsheet</a>. Finally, if there are any rare matches, the program will tweet me."
							}
						},
					'Images' : {
						'portrait' : 'static/img/john.png',
						'sammy' : 'static/img/sam.png'
						},
					'Social' : {
							'facebook' : {
								'link' : 'https://www.facebook.com/john.simmons.737',
								'fa4x' : 'fa fa-facebook-square fa-4x'
							},
							"linkedin" : {
								'link' : 'https://www.linkedin.com/in/johndavidsimmons',
								'fa4x' : 'fa fa-linkedin-square fa-4x'
							},
							'github' : {
								'link' : 'https://github.com/johndavidsimmons',
								'fa4x' : 'fa fa-github-square fa-4x',
								'fa2x' : 'fa fa-github-square fa-2x'
							},
							'twitter' : {
								'link' : 'https://twitter.com/johnsimmons517',
								'fa4x' : 'fa fa-twitter-square fa-4x'
							}
						}
					}
	return CONTENT_DICT