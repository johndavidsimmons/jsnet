from flask import Flask, render_template, url_for, request, flash, redirect
from content import Content
from requests import get
import json
import os
import datetime
import MySQLdb
from connection import SecretKey


app = Flask(__name__)
app.secret_key = SecretKey()

CONTENT_DICT = Content()


# Error handlers
@app.errorhandler(404)
def page_not_found(error):
    try:
        return render_template('404.html', CONTENT_DICT=CONTENT_DICT, error=error)
    except Exception as e:
        return str(e)


@app.errorhandler(500)
def error_500(error):
    try:
        return str(error)
    except Exception as e:
        return str(e)


def create_routes(app):
    @app.route("/")
    def index():
        try:
            return render_template('index.html', CONTENT_DICT=CONTENT_DICT)
        except Exception as e:
            # return e
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/resume')
    def resume():
        try:
            return render_template('resume.html', CONTENT_DICT=CONTENT_DICT)
        except Exception as e:
            return str(e)
            # return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/projects')
    def projects():
        try:
            from blog import Projects
            projects_dict = Projects()
            return render_template('projects.html', CONTENT_DICT=CONTENT_DICT, projects_dict=projects_dict)
        except Exception as e:
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/makerchallenge')
    def makerchallenge():
        try:
            return render_template('makerchallenge.html', CONTENT_DICT=CONTENT_DICT)
        except Exception as e:
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/records', methods=['GET', 'POST'])
    def records():
        try:
            
            from connection import Credentials, AddRecordPassword
            from collections import OrderedDict
            from form import AddRecord
            newest = None

            AddRecord = AddRecord(request.form)
            CRED = Credentials()
            AddRecordPassword = AddRecordPassword()
            
            db = MySQLdb.connect(host=CRED['host'],    # your host, usually localhost
                                 user=CRED['username'],         # your username
                                 passwd=CRED['password'],  # your password
                                 db=CRED['db'])        # name of the data base

            cur = db.cursor()

            if request.method == 'POST' and AddRecord.validate():
                if AddRecord.password.data == AddRecordPassword:
                    post_artist = AddRecord.artist.data
                    post_title = AddRecord.title.data
                    post_color = AddRecord.color.data
                    post_year = AddRecord.year.data
                    post_notes = AddRecord.notes.data
                    post_size = AddRecord.size.data

               
                    cur.execute("INSERT INTO records_database (artist, title, color, year, notes, size) VALUES (%s, %s, %s, %s, %s, %s)", (post_artist, post_title, post_color, post_year, post_notes, post_size))
                    db.commit()
                    
                    cur.execute("SELECT * FROM records_database ORDER BY ID DESC LIMIT 1;")


                    flash('<p><i>+ {} - {}</i></p>'.format(post_artist, post_title))
                    return redirect(url_for('records'))
                    
                elif AddRecord.password.data != AddRecordPassword:
                    flash('<p><i>Bad Password</i></p>')
                    return redirect(url_for('records'))

            
                else:
                    flash('<p><i>Something went wrong</i></p>')
                    return redirect(url_for('records'))
            

            cur.execute("SELECT * FROM records_database ORDER BY size, artist, year")
            data_list = [row for row in cur.fetchall()]
            records = {
                        7: [row for row in data_list if int(row[7]) == 7],
                        10: [row for row in data_list if int(row[7]) == 10],
                        12: [row for row in data_list if int(row[7]) == 12]
                    }
            db.close()        
         


            return render_template('records.html', CONTENT_DICT=CONTENT_DICT, records=OrderedDict(sorted(records.items())), AddRecord=AddRecord )
        except Exception as e:
            # return str(e)
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/cl')
    def cl():
        from bs4 import BeautifulSoup as bs4
        try:
            base_url = 'http://detroit.craigslist.org'

            searches = {
                'marantz':'http://detroit.craigslist.org/search/ele?query=marantz&sort=date&postedToday=1', 
                'pioneer': 'http://detroit.craigslist.org/search/ele?postedToday=1&amp;query=pioneer%20receiver&amp;sort=date',
                'minidisc': 'http://detroit.craigslist.org/search/okl/ele?query=minidisc&sort=date&postedToday=1',
                'reel to reel': 'http://detroit.craigslist.org/search/ele?query=reel+to+reel&sort=date&postedToday=1'
            }

            pages = []
            html_string = '<p>Updated On: {}'.format(datetime.datetime.now().strftime('%c'))


            for search, url in searches.iteritems():
                p = get(url).text
                pages.append((bs4(p, 'html5lib'), search))

            for page in pages:

                # Check if results exist
                results = page[0].findAll("p", { "class" : "row" })
                if results:
                    for listing in results:
                        if not listing.find('a').get('href').startswith('//annarbor') and not listing.find('a').get('href').startswith('//toledo'):
                            link = base_url + listing.find('a').get('href')
                            try:
                                price = listing.find("span", { "class" : "price" }).text
                            except:
                                price = 'No Price'
                            title = listing.find("span", { "id" : "titletextonly" }).text
                            html_string += '<p><strong>{3}</strong>: <a href="{0}">{1} - {2}</a></p>'.format(link, title, price, page[1])
            return render_template('cl.html', html_string=html_string)
        except Exception as e:
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

create_routes(app)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    if port == 5000:
        app.run(host='0.0.0.0', port=port, debug=True)



