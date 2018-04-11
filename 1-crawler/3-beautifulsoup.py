import requests # learn more: https://python.org/pypi/requests

from bs4 import BeautifulSoup # learn more: https://python.org/pypi/BeautifulSoup

def getHtmlText(url):
  try:
    r = requests.get(url, timeout=30)
    # If status code is not 200, raise HTTPError
    r.raise_for_status()
    # Set correct encoding
    r.encoding = r.apparent_encoding
    return r.text
  except Exception:
    return "Something wrong"
html = getHtmlText("https://www.google.fr")

soup = BeautifulSoup(html)

# Reorganize html code
soup.prettify()
print(soup)
