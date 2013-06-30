import pymongo
import sys
def main():
	
	connection = pymongo.MongoClient("mongodb://localhost")
	
	db = connection.m101
	people = db.people
	
	person = {'name': 'Hiral patel', 'role':'Professor'}
	print(person)
	print("about to insert person")
	
	try:
		people.insert(person)
	except:
		print("insert failed: ", sys.exc_info()[0])
		
	person = {'name': 'Hiral patel', 'role':'Professor'}	
		
	print(person)
	print("about to insert person")
	
	try:
		people.insert(person)
	except:
		print("insert failed: ", sys.exc_info()[0])	

main()
