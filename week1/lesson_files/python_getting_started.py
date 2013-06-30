import pymongo

from pymongo import MongoClient

#connect to dB
connection = MongoClient('localhost', 27017)

#localhost: name of dB
dB = connection.localhost

#users: name of collection inside "databse: localhost"
users = dB.users

item = users.find_one()

print( item['username'] )
