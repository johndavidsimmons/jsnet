from flask import render_template, send_file
from . import main
from content import Content

CONTENT_DICT = Content()


@main.route('/', methods=['GET'])
def index():
	return render_template('index.html', CONTENT_DICT=CONTENT_DICT)


@main.route('/resume', methods=['GET'])
def resume():
	return render_template('resume.html', CONTENT_DICT=CONTENT_DICT)


@main.route('/download', methods=['GET'])
def download():
	return send_file('static/John_Simmons_Resume.pdf', as_attachment=True)
