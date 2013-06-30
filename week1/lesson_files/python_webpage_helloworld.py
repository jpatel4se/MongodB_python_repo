import pymongo
import bottle

from pymongo import MongoClient

@bottle.route('/')
def index():

	#connect to dB
	connection = MongoClient('localhost', 27017)

	#localhost: name of dB
	dB = connection.localhost

	#users: name of collection inside "databse: localhost"
	users = dB.users

	item = users.find_one()

	return '<b>Hello %s!</b>' %item['username']
	
	
bottle.run(host='localhost', port=8082)