from flask import Flask, render_template, url_for
from content import Content
from requests import get
import json
import csv

app = Flask(__name__)

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
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)

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

    @app.route('/records')
    def records():
        try:
            records = list(json.loads(get('https://sheetsu.com/apis/v1.0/c8f9d5b7').text))
            seveninches = [record for record in records if record['Size'] == '7']
            teninches = [record for record in records if record['Size'] == '10']
            twelveinches = [record for record in records if record['Size'] == '12']
            return render_template('records.html', CONTENT_DICT=CONTENT_DICT, seveninches=seveninches,
                                   teninches=teninches, twelveinches=twelveinches)
        except Exception as e:
            # return e
            return render_template('500.html', CONTENT_DICT=CONTENT_DICT, error=e)


create_routes(app)

# if __name__ == "__main__":
# 	create_routes(app)
# 	app.debug = True
# 	app.run()
