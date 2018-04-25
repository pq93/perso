# Get the movies' rank, title, year, IMDB rating and summaryself.

import requests         # Request for HTTP
import bs4              # Pulling data out of HTML and XML files
from bs4 import BeautifulSoup
import lxml             # Processing XML and HTML
import numpy as np      # Scientific computing (N-dimensional array)
import pandas as pd     # Data structures and data analysis tools

# Get HTML text
def getHtml(url):
    try:
        # Stop waiting for response after 30 seconds
        r = requests.get(url, timeout=30)
        # If status code is not 200, raise HTTPError
        r.raise_for_status()
        # Set correct encoding
        r.encoding = 'utf-8'
        #r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        return "Wrong!"

# Get content
def getContent(url):
    # Get the web source code
    html = getHtml(url)
    # Parse the web source code with lxml
    soup = bs4.BeautifulSoup(html, 'lxml')

    # Get the movies' rank
    rank_list = soup.find_all('span', {'name':'rk'})
    # Create an array to save the rank list
    rank = np.array([], dtype='int')
    for rk in rank_list:
        rk = int(rk['data-value'])
        rank = np.append(rank, rk)

    # Get the movies' title
    title_list = soup.find_all('td', class_='titleColumn')
    # Create an array to save the title list
    title = np.array([])
    for tl in title_list:
        tl = tl.a.contents[0] # Title text
        # Set encoding for French character
        tl_fr = unicode(tl).encode('utf-8')
        tl_fr = str(tl_fr)
        title = np.append(title, tl_fr)

    # Get the movies' year
    year_list = soup.find_all('span', class_='secondaryInfo')
    # Create an array to save the year list
    year = np.array([], dtype='int32')
    for yr in year_list:
        yr = yr.contents[0][1:5] # Year list
        yr = int(yr)
        year = np.append(year, yr)

    # Get the movies' IMDB rating
    rating_list = soup.find_all('span', {'name':'ir'})
    # Create an array to save the IMDB rating list
    imdbrating = np.array([], dtype='float')
    for rt in rating_list:
        rt = float(rt['data-value'])
        rt = round(rt, 3) # Keep 3 decimals
        imdbrating = np.append(imdbrating,rt)

    # Get the movies' summary
    url_list = soup.find_all('td', class_='titleColumn')
    # Create an array to save the summary list
    text = np.array([])
    for url in url_list:
        # Website url of each movie
        url = url.a['href']
        # Complete ebsite url of each movie
        url = str("http://www.imdb.com"+url)
        # Get summary text
        txt = getSummary(url)
        # Set encoding for French character
        txt = unicode(txt).encode('utf-8')
        txt = str(txt)
        text = np.append(text, txt)

    # Combine 4 information
    col = ['Title','Year','IMDB Rating','Summary']
    mv_data = np.array([title, year, imdbrating, text])

    # Turn array into dataframe
    mv_data = pd.DataFrame(data=mv_data.T, index=rank, columns=col)

    # Visualize data
    print(mv_data.head())

    # Save data to local csv file
    mv_data.to_csv("IMDB_Top250.csv", encoding='utf-8')

    return None

# Read website of every movie in top250 list and return the summary text
def getSummary(url):
    # Get the web source code
    html = getHtml(url)
    # Parse the web source code with lxml
    soup = bs4.BeautifulSoup(html, 'lxml')
    # Get de summary text
    summary = soup.find('div', class_='summary_text')
    text = summary.contents[0][21:-13]
    return text

# Main function
def main():
    url = 'http://www.imdb.com/chart/top'
    getContent(url)

if __name__ == "__main__":
    main()
