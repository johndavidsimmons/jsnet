from flask import render_template
from . import main
from content import Content
import cloudinary as CD

CONTENT_DICT = Content()

@main.route('/', methods=['GET'])
def index():
	return render_template('index.html', CONTENT_DICT=CONTENT_DICT)

@main.route('/resume', methods=['GET'])
def resume():
	return render_template('resume.html', CONTENT_DICT=CONTENT_DICT)

@main.route('/todo', methods=['GET'])
def todo():
	return render_template('todo.html', CONTENT_DICT=CONTENT_DICT)