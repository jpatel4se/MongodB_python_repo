<html>
<head>
<title>Hello world</title>
</head>
	<body>
		<p>
			Welcome {{usernameInHtml}}
		</p>
		<ul>
			%for fruits in thingsInHtml:
			<li>{{fruits}}</li>
			%end
		</ul>
		
		</p>
		<form action="/favourite_fruit" method="POST">
			What is your favourite food ?
			<input type="text" name="fruit" size="40"><br>
			<input type="submit" value="Submit">
		</form>	
		
	</body>
</html>