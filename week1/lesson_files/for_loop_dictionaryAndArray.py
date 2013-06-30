
#Initialize object

person={'name':'hiral', 
		'favourite_color':"red", 
		"hair":"black",
		"interests":["hiking","research","studying"]}

print(person)

for key in person:
	if(key == 'interests'):
		print("key: "+key)
		
		for interest in person[key]:
			print(interest)
		
	else:
		print("key: "+key+", value: "+person[key])
		

