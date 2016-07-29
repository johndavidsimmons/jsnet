import os

def Credentials():
	CREDENTIALS = {
		'username': os.environ['DB_USERNAME'],
		'password': os.environ['DB_PASSWORD'],
		'host': os.environ['DB_HOST'],
		'db' : os.environ['DB']
	}

	return CREDENTIALS


def SecretKey():
	return os.environ['SECRET_KEY']

def AddRecordPassword():
	return os.environ['ADD_PASS']		