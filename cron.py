import requests
from bs4 import BeautifulSoup as bs4
import datetime

base_url = 'http://detroit.craigslist.org'

searches = {
	'marartz':'http://detroit.craigslist.org/search/ele?query=marantz&sort=date&postedToday=1', 
	'pioneer': 'http://detroit.craigslist.org/search/ele?postedToday=1&amp;query=pioneer%20receiver&amp;sort=date',
	'minidisc': 'http://detroit.craigslist.org/search/okl/ele?query=minidisc&sort=date&postedToday=1',
	'reel to reel': 'http://detroit.craigslist.org/search/ele?query=reel+to+reel&sort=date&postedToday=1'
}

pages = []
html_string = '<p>Updated On: {}'.format(datetime.datetime.now().strftime('%c'))


for search, url in searches.iteritems():
	p = requests.get(url).text
	pages.append((bs4(p, 'html5lib'), search))

for page in pages:

	# Check if results exist
	results = page[0].findAll("p", { "class" : "row" })
	if results:
		for listing in results:
			if not listing.find('a').get('href').startswith('//annarbor'):
				link = base_url + listing.find('a').get('href')
				try:
					price = listing.find("span", { "class" : "price" }).text
				except:
					price = 'No Price'
				title = listing.find("span", { "id" : "titletextonly" }).text
				html_string += '<p><strong>{3}</strong>: <a href="{0}">{1} - {2}</a></p>'.format(link, title, price, page[1])
				


html_file= open("templates/cl.html","w")
html_file.write(html_string)
html_file.close()
		


