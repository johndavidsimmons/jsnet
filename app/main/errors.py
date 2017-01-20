from flask import render_template
from . import main
from content import Content

CONTENT_DICT = Content()

@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('error.html', CONTENT_DICT=CONTENT_DICT, e=e), 404

@main.app_errorhandler(405)
def method_not_allowed(e):
	return render_template('error.html', CONTENT_DICT=CONTENT_DICT, e=e), 405