import bottle

@bottle.route('/')
def homepage():
	mythings = ['apple','baanananana','orange','peach']

	# passing parameter in DICTIONARY
	return bottle.template('form_post',{'usernameInHtml':"Andrew", 'thingsInHtml':mythings})
	
@bottle.post('/favourite_fruit')
def favouritefood():
		fruit_selected = bottle.request.forms.get("fruit")
		
		if(fruit_selected == None or fruit_selected == ""):
			fruit_selected = "No Fruit selected"
			
		bottle.response.set_cookie("fruit_cookie", fruit_selected);	
		bottle.redirect("/show_fruit")
		
@bottle.route('/show_fruit')
def showfavouritefood():
		fruit_selected = bottle.request.get_cookie("fruit_cookie")	
		return bottle.template('form_selection.tpl',{'fruit_selectedInHtml':fruit_selected})
							
bottle.debug(True);
bottle.run(host='localhost', port=8082)