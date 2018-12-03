import unittest
from flask import current_app, url_for
from app import create_app
import os
from content import Content
from datetime import datetime

CONTENT_DICT = Content()

if os.path.exists('.env'):
	print('Importing environment from .env...')
	for line in open('.env'):
		var = line.strip().split('=')
		if len(var) == 2:
			os.environ[var[0]] = var[1]

class BasicsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()

	def tearDown(self):
		self.app_context.pop()

	def test_app_exists(self):
		self.assertFalse(current_app is None)

	def test_app_is_testing(self):
		self.assertTrue(current_app.config['TESTING'])



class FlaskClientTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.client = self.app.test_client(use_cookies=True)

	def tearDown(self):
		self.app_context.pop()

	def test_home_page_redirect(self):
		response = self.client.get(url_for("main.index"))
		self.assertTrue(response.status_code == 302)

	def test_home_page_redirect_to_resume(self):
		response = self.client.get(url_for("main.index"), follow_redirects=True)
		self.assertTrue(response.status_code == 200)
		self.assertTrue("Quicken Loans" in response.data)
		self.assertTrue('<a class="selected" href="/resume">Resume</a>' in response.data)

	def test_resume_page(self):
		response = self.client.get(url_for("main.resume"))
		self.assertTrue(response.status_code == 200)
		self.assertTrue("Quicken Loans" in response.data)
		self.assertTrue('<a class="selected" href="/resume">Resume</a>' in response.data)

	def test_any_page_redirects_to_resume(self):
		response = self.client.get("/abc1234", follow_redirects=True)
		self.assertTrue(response.status_code == 200)
		self.assertTrue("Quicken Loans" in response.data)
		self.assertTrue('<a class="selected" href="/resume">Resume</a>' in response.data)

	def test_405_redirects(self):
		response = self.client.post(url_for("main.resume"))
		self.assertTrue(response.status_code == 302)

	def test_405_redirects(self):
		response = self.client.post(url_for("main.resume"), follow_redirects=True)
		self.assertTrue(response.status_code == 200)
		self.assertTrue("Quicken Loans" in response.data)
		self.assertTrue('<a class="selected" href="/resume">Resume</a>' in response.data)	


	def test_year(self):
		self.assertTrue(CONTENT_DICT['year'] == datetime.now().strftime('%Y'))	
						

if __name__ == "__main__":
	unittest.main()	