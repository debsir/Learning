#!/usr/bin/env python

# Submitting a form and retrieving a page with mechanize.

import mechanize
br = mechanize.Browser()
br.open('http://www.weather.gov/')
br.select_form(predicate=lambda(form): 'zipcity' in form.action)
br['inputstring'] = 'Phoenix, AZ'
response = br.submit()
content = response.read()
print content
