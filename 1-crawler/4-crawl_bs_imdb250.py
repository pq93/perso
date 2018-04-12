# Get the movies' rank, title, year, IMDB rating and descriptionself.

import requests
import bs4
from bs4 import BeautifulSoup
import lxml

def getHtml(url):
    try:
        r = requests.get(url, timeout=30)
        # If status code is not 200, raise HTTPError
        r.raise_for_status()
        # Set correct encoding
        r.encoding = 'utf-8'
        #r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        return "Wrong!"

def getContent(url):
    html = getHtml(url)
    soup = bs4.BeautifulSoup(html,'lxml')
    #soup = soup.prettify()
    # Get the movies' rank
    mv_rk = soup.find_all('span',{'name':'rk'})
    for rk in mv_rk:
        print(rk['data-value'])
    # Get the movies' name
    mv_nm = soup.find_all('td',class_='titleColumn')
    for nm in mv_nm:
        print(nm.a.contents)
    # Get the movies' year


getContent("http://www.imdb.com/chart/top")
