from flask import redirect, render_template, send_file, url_for
from . import main
from content import Content

CONTENT_DICT = Content()

@main.route('/', defaults={'path': ''}, methods=['GET'])
@main.route('/<path:path>', methods=['GET'])
def index(path):
	return render_template('resume.html', CONTENT_DICT=CONTENT_DICT)


@main.route('/resume', methods=['GET'])
def resume():
	return render_template('resume.html', CONTENT_DICT=CONTENT_DICT)


@main.route('/download', methods=['GET'])
def download():
	return send_file('static/John_Simmons_Resume.pdf', as_attachment=True)
