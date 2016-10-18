from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        return bsObj.find('div', {'id':'bodycontent'}).findAll('a',
                          href=re.compile('^(/wiki/)((?!:).)*$'))
    except AttributeError:
        print("Check the name of tag!")
        exit()

links = getLinks('/wiki/kevin_Durant')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
