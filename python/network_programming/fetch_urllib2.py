#!/usr/bin/env python
# Submitting a form and retrieving a page with urllib2

import urllib, urllib2

data = urllib.urlencode({'inputstring': 'Phoenix, AZ'})
info = urllib2.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()
open('phoenix.html', 'w').write(content)
