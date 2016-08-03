# System packages
import json
import os
import datetime
import gc
from functools import wraps

# Installed Packages
from flask import Flask, render_template, url_for, request, flash, redirect, session
from content import Content
from requests import get
import MySQLdb
from passlib.hash import sha256_crypt

# My packages
from connection import SecretKey, Credentials

#*********************
#      App Setup      *
#*********************
app = Flask(__name__)
app.secret_key = SecretKey()
CRED = Credentials()
CONTENT_DICT = Content()


#*********************
#     Decorators     *
#*********************
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)

        else:
            flash("Login required")
            return redirect(url_for("index"))

    return wrap


#*********************
#   Error Handlers   *
#*********************

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

#*********************
#     App Routes     *
#*********************

def create_routes(app):
    @app.route("/")
    def index():
        try:
            return redirect(url_for('blog'))
        except Exception as e:
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/resume')
    def resume():
        try:
            return render_template('resume.html', CONTENT_DICT=CONTENT_DICT)
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
        db = MySQLdb.connect(host=CRED['host'],    
                             user=CRED['username'],
                             passwd=CRED['password'],
                             db=CRED['db'])

        cur = db.cursor()
        try:
            
            from connection import AddRecordPassword
            from collections import OrderedDict
            from form import AddRecord

            AddRecord = AddRecord(request.form)
            AddRecordPassword = AddRecordPassword()
            

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
                    db.close()

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
            return str(e)
            # return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

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

    @app.route('/blog', methods=['GET', 'POST'])
    @app.route('/blog/<int:page>')
    @app.route('/blog/<string:posttitle>')
    def blog(page=1, posttitle=None):
        
        db = MySQLdb.connect(host=CRED['host'],    
                             user=CRED['username'],
                             passwd=CRED['password'],
                             db=CRED['db'])

        cur = db.cursor()
        try:

            from images import image_dict
            from form import AddPost
            
            IMAGES = image_dict()
            AddPost = AddPost(request.form)

            cur.execute("SELECT * FROM blog ORDER BY ID DESC;")
            posts = [row for row in cur.fetchall()]
            num_of_posts = len(posts)
            num_of_pages = ((num_of_posts - 1) / 2) + 1
            page_plus_1 = page + 1
            ptt = (page * 2) - 2

            db.close()
            return render_template('blog.html', 
                CONTENT_DICT=CONTENT_DICT, 
                page=page, 
                posts = posts, 
                num_of_posts=num_of_posts,
                num_of_pages=num_of_pages,
                page_plus_1=page_plus_1,
                ptt = ptt,
                IMAGES=IMAGES,
                posttitle=posttitle,
                AddPost=AddPost)
        except Exception as e:
            return str(e)
            # return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        db = MySQLdb.connect(host=CRED['host'],    
                             user=CRED['username'],
                             passwd=CRED['password'],
                             db=CRED['db'])

        cur = db.cursor()

        try:
            from form import LoginForm
            LoginForm = LoginForm(request.form)


            if request.method == 'POST':

                cur.execute("SELECT * FROM users WHERE username=%s", (LoginForm.username.data,))
                row = cur.fetchone()

                # if the username exists and password verifies
                if row and sha256_crypt.verify(LoginForm.password.data, row[2]):
                    session["logged_in"] = True
                    session["username"] = request.form["username"]
                    return redirect(url_for('index'))
                else:
                    flash('<p>Bad Credentials</p>')
                    return redirect(url_for('login'))

            return render_template('login.html', CONTENT_DICT=CONTENT_DICT, LoginForm=LoginForm)
        except Exception as e:
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

    @app.route('/logout')
    @login_required
    def logout():
        try:
            session.clear()
            flash('You have logged out')
            gc.collect()
            return redirect(url_for('blog'))
        except Exception as e:
            flash(e)
            return redirect(url_for('login'))

    @app.route('/addpost', methods=['GET', 'POST'])
    @login_required
    def addpost():
        db = MySQLdb.connect(host=CRED['host'],    
                             user=CRED['username'],
                             passwd=CRED['password'],
                             db=CRED['db'])

        cur = db.cursor()

        try:
            from form import AddPost
            AddPost = AddPost(request.form)

            if request.method =='POST' and session["logged_in"] == True:
                cur.execute("INSERT INTO blog (title, timestamp, content, ghlink) VALUES (%s, %s, %s, %s)", (AddPost.title.data, AddPost.timestamp.data, AddPost.content.data, AddPost.ghlink.data))
                db.commit()
                db.close()
                flash('<p>Title: {}, Timestamp: {}</p>'.format(AddPost.title.data, AddPost.timestamp.data))
                return redirect(url_for('blog'))
        except Exception as e:
            flash("Error: {}".format(e))
            return redirect(url_for('blog'))        

    @app.route('/deletepost/<int:id_num>', methods=['GET', 'POST'])
    @login_required
    def deletepost(id_num=None):
        db = MySQLdb.connect(host=CRED['host'],    
                             user=CRED['username'],
                             passwd=CRED['password'],
                             db=CRED['db'])

        cur = db.cursor()

        try:
            cur.execute("DELETE FROM blog WHERE ID = %s", (id_num,)) 
            db.commit()
            db.close()
            
            flash('Deleted post {}'.format(id_num))
            return redirect(url_for('blog'))
        except Exception as e:
            return str(e)


    @app.route('/deleterecord/<int:id_num>', methods=['GET', 'POST'])
    @login_required
    def deleterecord(id_num=None):
        db = MySQLdb.connect(host=CRED['host'],    
                             user=CRED['username'],
                             passwd=CRED['password'],
                             db=CRED['db'])

        cur = db.cursor()

        try:
            # Get deleted record info for flash
            cur.execute("SELECT * FROM records_database WHERE ID = %s LIMIT 1", (id_num,))
            row = cur.fetchone()
            deleted_artist, deleted_title = row[1], row[2]

            # Deleting
            cur.execute("DELETE FROM records_database WHERE ID = %s", (id_num,)) 
            db.commit()
            db.close()
            
            
            flash('<p><i>- {} - {}</i></p>'.format(deleted_artist, deleted_title))
            return redirect(url_for('records'))
        except Exception as e:
            flash('Something went wrong deleting record')
            return redirect(url_for('records'))

create_routes(app)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    if port == 5000:
        app.run(host='0.0.0.0', port=port, debug=True)



