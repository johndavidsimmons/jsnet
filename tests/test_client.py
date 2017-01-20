import unittest
from flask import current_app, url_for
from app import create_app
import os
from content import Content

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

	def test_home_page(self):
		response = self.client.get(url_for("main.index"))
		self.assertTrue(response.status_code == 200)
		self.assertTrue("All projects and other writings have been migrated" in response.data)
		self.assertTrue('<a class="selected" href="/">Home</a>' in response.data)

	def test_resume_page(self):
		response = self.client.get(url_for("main.resume"))
		self.assertTrue(response.status_code == 200)
		self.assertTrue("Quicken Loans" in response.data)
		self.assertTrue('<a class="selected" href="/resume">Resume</a>' in response.data)

	def test_todo_page(self):
		response = self.client.get(url_for("main.todo"))
		self.assertTrue(response.status_code == 200)
		self.assertTrue("To-Do List" in response.data)
		self.assertTrue('<a class="selected"href="/todo">To-Do</a>' in response.data)

	def test_404_page(self):
		response = self.client.get('/yolo')
		self.assertTrue(response.status_code == 404)
		self.assertTrue("Not Found" in response.data)

	def test_405_page(self):
		response = self.client.post('/')
		self.assertTrue(response.status_code == 405)
		self.assertTrue("Method Not Allowed" in response.data)

		response = self.client.post('/resume')
		self.assertTrue(response.status_code == 405)
		self.assertTrue("Method Not Allowed" in response.data)

		response = self.client.post('/todo')
		self.assertTrue(response.status_code == 405)
		self.assertTrue("Method Not Allowed" in response.data)

	def test_year(self):
		self.assertTrue(CONTENT_DICT['year'] == '2017')	
						

if __name__ == "__main__":
	unittest.main()	