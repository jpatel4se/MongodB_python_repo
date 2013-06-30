import bottle

@bottle.route('/')
def homepage():
	mythings = ['apple','baanananana','orange','peach']
	#return bottle.template('view_python_bottle_viewController', usernameInHtml="Andrew", thingsInHtml=mythings)
	
	# passing parameter in DICTIONARY
	return bottle.template('view_python_bottle_viewController',{'usernameInHtml':"Andrew", 'thingsInHtml':mythings})
		
bottle.debug(True);
bottle.run(host='localhost', port=8082)