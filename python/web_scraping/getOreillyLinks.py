from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://wiki.mbalib.com' + pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    """
    try:
        return bsObj.find('div', {'id':'bodyContent'}).findAll('a',
                href=re.compile('^(/wiki/)(?!:).*$'))
    except AttributeError:
        print("Check the name of tag!")
        exit()
    """
    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks("")
"""
links = getLinks('/wiki/Tesla')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
"""
