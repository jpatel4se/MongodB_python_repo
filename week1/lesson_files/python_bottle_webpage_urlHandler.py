import bottle

@bottle.route('/')
def homepage():
	return "Hello World"
	
@bottle.route('/testpage')
def homepage():
	return "Hello World - test page"	

bottle.debug(True);
bottle.run(host='localhost', port=8082)