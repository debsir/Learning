#!/usr/bin/env python3
# put this cgi101.py in the path '/usr/lib/cgi-bin/'

import cgi

form = cgi.FieldStorage()               # parse form data
print('Content-type: text/html\n')      # hdr plus blank line
print('<title>Reply Page</title>')      # html reply page
if not 'user' in form:
    print('<hi>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))

