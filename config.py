import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	FLASK_CONFIG=os.environ.get('FLASK_CONFIG')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True

class ProductionConfig(Config):

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)


class HerokuConfig(ProductionConfig):
	SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

	@classmethod
	def init_app(cls, app):
		ProductionConfig.init_app(app)

		# handle proxy server headers
		from werkzeug.contrib.fixers import ProxyFix
		app.wsgi_app = ProxyFix(app.wsgi_app)

		# log to stderr
		import logging
		from logging import StreamHandler
		file_handler = StreamHandler()
		file_handler.setLevel(logging.WARNING)
		app.logger.addHandler(file_handler)


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'heroku': HerokuConfig,
	'default': DevelopmentConfig
}