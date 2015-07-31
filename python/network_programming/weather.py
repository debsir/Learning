#!/usr/bin/python
# Fetch the weather forecast from the National Weather Service.

import sys, urllib, urllib2
from lxml import etree
from cssselect import CSSSelector
from BeautifulSoup import BeautifulSoup

if len(sys.argv) < 2:
    print >> sys.stderr, 'usage: weather.py CITY, STATE'
    exit(2)

data = urllib.urlencode({'inputstring': ' '.join(sys.argv[1:])})
info = urllib2.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()

# Solution #1
parser = lxml.etree.HTMLParser(encoding='utf-8')
tree = lxml.etree.fromstring(content, parser)
div = CSSSelector('div.pull-left')(tree)[0]
print 'Condition:', div[1].text.strip()
print 'Temperature:', div[2].text.strip()
tr = tree.xpath('.//td[b="Humidity"]')[0].getparent()
print 'Humidity:', tr.findall('td')[1].text
print

#Solution #2
soup = BeautifulSoup(content)
div = soup.find('div', 'pull-left')
print 'Condition:', div.contents[3].string.strip()
temp = div.contents[5].string or div.contents[7].string
print 'Temperature:', temp.replace('&deg;', ' ')
tr = soup.find('b', text='Humidity').parent.parent.parent
print 'Humidity:', tr('td')[1].string
print
