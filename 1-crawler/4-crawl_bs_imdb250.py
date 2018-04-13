# Get the movies' rank, title, year, IMDB rating and descriptionself.

import requests
import bs4
from bs4 import BeautifulSoup
import lxml
import numpy as np
import pandas as pd

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
    rank = np.array([],dtype='int')
    for rk in mv_rk:
        rank = np.append(rank,rk['data-value'])
    
    
    # Get the movies' name
    mv_nm = soup.find_all('td',class_='titleColumn')
    name = np.array([])
    for nm in mv_nm:
        nm = nm.a.contents[0]
        #nm_fr = unicode(nm).encode('utf-8')
        name = np.append(name,nm)
    
    # Get the movies' year
    mv_yr = soup.find_all('span',class_='secondaryInfo')
    year = np.array([],dtype='int')
    for yr in mv_yr:
        year = np.append(year,yr.contents[0][1:5])
    
    # Get the movies' IMDB rating
    mv_rt = soup.find_all('td',class_='ratingColumn imdbRating')
    imdbrating = np.array([],dtype='float')
    for rt in mv_rt:
        imdbrating = np.append(imdbrating,rt.strong.contents[0])
    
    col = ['Rank','Name','Year','IMDB Rating']
    data = np.arange(250,4)
    data[250,0] = rank
    data[250,1] = name
    data[250,2] = year
    data[250,3] = imdbrating
    mv_data = pd.DataFrame(data,columns=col)
    return print(mv_data.head())


getContent("http://www.imdb.com/chart/top")
