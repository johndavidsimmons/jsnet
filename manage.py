#!/usr/bin/env python
import os
COV = None

if os.environ.get('FLASK_COVERAGE'):
	import coverage
	COV = coverage.coverage(branch=True, include='app/*')
	COV.start()

if os.path.exists('.env'):
	for line in open('.env'):
		var = line.strip().split('=')
		if len(var) == 2:
			os.environ[var[0]] = var[1]

from app import create_app
from flask_script import Manager
from flask_script import Shell
from content import Content
 
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
CONTENT_DICT = Content()


def make_shell_context():
	return dict(app=app, CONTENT_DICT=CONTENT_DICT)

manager.add_command('shell', Shell(make_context = make_shell_context))

@manager.command
def test(coverage=True):
	"""Run the unit tests."""
	if coverage and not os.environ.get('FLASK_COVERAGE'):
		import sys
		os.environ['FLASK_COVERAGE'] = '1'
		os.execvp(sys.executable, [sys.executable] + sys.argv)
	
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

	if COV:
		COV.stop()
		COV.save()
		# print "Coverage Summary"
		COV.report()
		basedir = os.path.abspath(os.path.dirname(__file__))
		covdir = os.path.join(basedir, 'tmp/coverage')
		COV.html_report(directory=covdir)
		# print 'HTML version: file://{}/index.html'.format(covdir)
		COV.erase()

if __name__ == '__main__':
	manager.run()