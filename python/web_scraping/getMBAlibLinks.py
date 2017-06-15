from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen('http://wiki.mbalib.com' + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        return bsObj.find('div', {'id':'bodyContent'}).findAll('a',
                href=re.compile('^(/wiki/)(?!:).*$'))
    except AttributeError:
        print("Check the name of tag!")
        exit()

links = getLinks('/wiki/Tesla')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
