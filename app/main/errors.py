from flask import redirect, render_template, url_for
from . import main
from content import Content

CONTENT_DICT = Content()

@main.app_errorhandler(405)
def method_not_allowed(e):
    return redirect(url_for("main.resume"))