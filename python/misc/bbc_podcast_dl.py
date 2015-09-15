#/usr/bin/python

from sgmllib import SGMLParser
import urllib, re, subprocess

class URLLister(SGMLParser):
    def reset(self):
	SGMLParser.reset(self)
    	self.urls = []

    def start_a(self, attrs):
        pattern = re.compile(r"http://downloads.bbc.co.uk/podcasts/.*mp3")
	href = [v for k, v in attrs if k=='href' and re.match(pattern, v)]
        if href: 
	    self.urls.extend(href)

usock = urllib.urlopen("http://www.bbc.co.uk/podcasts/series/globalnews")
parser = URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
subprocess.call(["axel", parser.urls[0]])

