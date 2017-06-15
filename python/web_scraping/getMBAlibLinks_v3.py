from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://wiki.mbalib.com' + pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="bodyContent").findAll('p')[0])
    except AttributeError:
        print('This page is missing something!')

    """
    try:
        return bsObj.find('div', {'id':'bodyContent'}).findAll('a',
                href=re.compile('^(/wiki/)(?!:).*$'))
    except AttributeError:
        print("Check the name of tag!")
        exit()
    """
    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("----------------------\n" + newPage)
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
