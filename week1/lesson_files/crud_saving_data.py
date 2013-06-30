import pymongo

def main():
	
	connection = pymongo.MongoClient("mongodb://localhost")
	
	db = connection.m101
	people = db.people
	
	person = {'name': 'Hiral patel', 'role':'Professor',
				'address':{'address1':'The white House',
							'state': 'Oregon'
							}
				}
	
	people.insert(person)

main()
