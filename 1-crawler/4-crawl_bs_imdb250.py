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
    rank_list = soup.find_all('span',{'name':'rk'})
    rank = np.array([],dtype='int')
    for rk in rank_list:
        rk = int(rk['data-value'])
        rank = np.append(rank,rk)

    # Get the movies' title
    title_list = soup.find_all('td',class_='titleColumn')
    title = np.array([])
    for tl in title_list:
        tl = tl.a.contents[0]
        tl_fr = unicode(tl).encode('utf-8')
        tl_fr = str(tl_fr)
        title = np.append(title,tl_fr)

    # Get the movies' year
    year_list = soup.find_all('span',class_='secondaryInfo')
    year = np.array([],dtype='int32')
    for yr in year_list:
        yr = yr.contents[0][1:5]
        yr = int(yr)
        year = np.append(year,yr)

    # Get the movies' IMDB rating
    rating_list = soup.find_all('span',{'name':'ir'})
    imdbrating = np.array([],dtype='float')
    for rt in rating_list:
        rt = float(rt['data-value'])
        rt = round(rt, 3)
        imdbrating = np.append(imdbrating,rt)

    col = ['Title','Year','IMDB Rating']

    mv_data = np.array([title, year, imdbrating])
    mv_data = pd.DataFrame(data=mv_data.T, index=rank,columns=col)
    print(mv_data)
    return None

def main():
    url = 'http://www.imdb.com/chart/top'
    getContent(url)

if __name__ == "__main__":
    main()
