def Projects():
    projects_content = [{
                'pimusicbox': {
                    'name': 'Pi Music Box',
                    'link': 'https://github.com/johndavidsimmons/pimusic',
                    'date' : 'Winter 2016',
                    'img': [
                        {'path': '/static/img/finalbox.png', 'alt': 'My completed Spotify Music Box'},
                        {'path': '/static/img/stainbox.png', 'alt': 'First coat of stain'},
                        {'path': '/static/img/pimusicdiagram.png', 'alt': 'Original rough layout for the music box'},
                        {'path': '/static/img/rawbox.png', 'alt': 'The untouched pine box from Etsy '},
                        {'path': '/static/img/fittest.png', 'alt': 'Testing the fit of lights and buttons'},
                        {'path': '/static/img/soundtest.png', 'alt': 'Dialing in the default volume'},
                        {'path': '/static/img/polybox.png', 'alt': 'Applying polyurethane for protection and shine'}
                    ],
                    'desc': "My Raspberry Pi powered Spotify Music Box streams a 10,000+ song playlist on random; essentially creating a custom internet radio station. The Pi itself is running <a href='https://www.mopidy.com/'>Mopidy</a> music server with a Python script for the controls and lights.<br><br> I drew a rough blueprint for the case and had it made by the fine people at <a href='https://www.etsy.com/shop/Tilnic Box'>Tilnic Box</a>. I originally intended to paint it silver to match my other stereo equipment, but thankfully decided against that. I went with a gunstock stain and a couple coats of polyurethane which made for a more aesthetically pleasing look. Check out how it works in the video: Despite primarily using breadboards, I was able to practice soldering on the buttons and lights. It is harder than it looks! As for the code, Python GPIO library is fairly straight forward and handles all the user input. The most challenging part was setting the script for the controls to run when the Pi is booted. After much Googling, I was able to figure it out using a Linux crontab."
                }},
                {'magicmirror': {
                    'name': 'Magic Mirror',
                    'link': 'https://github.com/johndavidsimmons/magicmirror',
                    'date' : 'Winter 2016',
                    'img': [
                        {'path': '/static/img/mirrorfinal.png', 'alt': 'The final product'},
                        {'path': '/static/img/monitorteardown.png', 'alt': 'Removing the monitor case'},
                        {'path': '/static/img/mirrorplacement.png',
                         'alt': 'Wifi is sketchy at best up here, but everything worked out fine'},
                        {'path': '/static/img/piboot.png', 'alt': 'Making sure I have the Pi\'s orientation set correctly'},
                        {'path': '/static/img/framesize.png', 'alt': 'Making sure everything fits before locking it in'},
                        {'path': '/static/img/firstboot.png', 'alt': 'First boot. It works! Better fix that positioning'}
                    ],
                    'desc': "I was inspired to make my Magic Mirror after seeing several posts on r/diy and r/raspberry_pi about them. What I never understood about these mirrors is how the text is 'projected' onto the mirror. Learning that its just a black webpage with white text behind a two-way mirror made making one of these actually seem possible. <br><br>I started out by building the frame with some old 2x4s I had in the basement. I figured I would do the hardest (at least for me) part first and if I couldn't get it right at least I didn't waste a bunch of time and money. I picked out, but held off on purchasing the <a href='http://www.amazon.com/gp/product/B00KSBBGA4?psc=1&redirect=true&ref_=oh_aui_detailpage_o02_s00'>monitor</a> I was going to use to get the measurements. An added bonus about this monitor is that it has a USB input that can power the Pi. After several attempts I was able to build a square-ish frame. Next time I will definitely spring for a few right angle clamps instead of the needlessly elaborate system I used. The 'mirror' is just plastic with a double sided mirror coating from <a href='http://www.tapplastics.com/product/plastics/cut_to_size_plastic/two_way_mirrored_acrylic/558'>TAP Plastics</a>. It was a lot cheaper than glass, but is flimsy and does not sit flat in the frame unfortunately. <br><br>After assembling and staining, I bought the monitor and wrote the code. Since the <a href='http://mirror.john-simmons.net'>webpage</a> is live, it is easy to update and add components should I so desire. The current version has the time, date, sunrise/sunset times, current temp, daily high/low temps, weather conditions icon, and the top story from r/news. It pulls new data every 30 minutes. All weather related data is pulled from the <a href='https://developer.yahoo.com/weather/'>Yahoo weather API</a>, and the weather icons are from <a href='http://www.weathericons.io'>weathericons.io</a>. The Reddit feed of course uses the <a href='https://www.reddit.com/dev/api'>Reddit API</a>. In the future I would like to a add a few things like traffic conditions to work, the price of Bitcoin, or watched eBay items that are ending."
                }},
                {'ebayscraper': {
                    'name': 'Ebay Scraper',
                    'link': 'https://github.com/johndavidsimmons/ebayscrape',
                    'date' : 'Fall 2015',
                    'img': [
                        {'path': '/static/img/ebaypy.png', 'alt': 'An overview of the script'},
                        {'path': '/static/img/scrape.png', 'alt': 'The current search is shown in the terminal'},
                        {'path': '/static/img/spread.png',
                         'alt': 'The output spreadsheet. Color coding handled by Google Docs'},
                        {'path': '/static/img/tweet.png', 'alt': 'Tweets at me when a rare match is found'}
                    ],
                    'desc': "There are a lot of <a href='http://howsyouredge.com/swap/display.php?page=1405' target='_blank'>records</a> I want. As much as I would like to, I do not have time to constantly search eBay for them. Also, a good portion of my want list are rare titles that: do not come up for auction very often thus searching for them typically yields no results. Solution: Remove myself from the equation. Create a list of search queries, search eBay automatically, and return a list of results. <br><br>Sounds like a perfect job for a web scraper. First, the easy part, I made a plain text file of searches I want to perform. Then, for each search query I use <a href='http://wwwsearch.sourceforge.net/mechanize/'>Mechanize</a> to traverse and search eBay and <a href='http://www.crummy.com/software/BeautifulSoup/'>Beautiful Soup</a> to parse the page of search results. After the results are collected, the <a href='https://github.com/burnash/gspread'>gspread</a> library posts them to a <a href='https://docs.google.com/spreadsheets/d/13oj2hpTJL9blQJdxg4g3A1sM09LEnKCgACZuDio1BXA/edit#gid=1087720188'>Google Spreadsheet</a>. Finally, if there are any rare matches, the program will tweet me."
                }},
                {'jsnet': {
                    'name': 'John-Simmons.net',
                    'link': 'https://github.com/johndavidsimmons/jsnet',
                    'date' : 'Summer 2015',
                    'img': [
                        {'path': '/static/img/jsnet.png', 'alt': 'JSNet project image'}
                    ],
                    'desc': "John-Simmons.net is using the <a href='http://flask.pocoo.org/'>Flask</a> framework and running via <a href='http://www.heroku.com'>Heroku</a>. It was written in Sublime Text 2 using the Emmet and Hayaku plugins. Special thanks to Sentdex and all his fantastic Python tutorials on Youtube and <a href='http://www.pythonprogramming.net'>PythonProgramming.net</a>. Check it out if you are at all interested in Python. <br><br>This is the third or fourth iteration of this website, and definitely the version that I feel I have done \"right\". At the very least, it is the most concise. Though its creation, I was (and still am) able to hone my skills and apply them to more complex projects. <br><br>The decision to take programming more seriously was a very logical: I was tired of struggling. My strategy was take it slow, learn (or re-learn) the basics, and build a solid foundation of understanding. I once heard the phrase \"You can't build a castle in a day, but you can lay one perfect brick at a time.\" I feel that is an apt metaphor to describe my learning philosophy in regards to just about anything."
                }
            }]

    return projects_content