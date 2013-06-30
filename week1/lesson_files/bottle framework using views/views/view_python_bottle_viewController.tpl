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
	</body>
</html>