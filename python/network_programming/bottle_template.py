%#!/usr/bin/env python
%# The page template that goes with bottle_app.py

<html><head><title>bottle_app.py</title></head>
<body>
  %if mystring is None:
	Welcome! Enter a string:
	<form action="encode"><input name="mystring"><input type="submit"></form>
  %else:
	<tt>{{mystring}}</tt> base64 encoded is: <tt>{{myb}}</tt><br>
	<a href="/">Return to the home page</a>
  %end
 </body>
 