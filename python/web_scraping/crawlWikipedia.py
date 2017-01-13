from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/Portal)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

print('There are {} links in this website.'.format(len(pages)))
