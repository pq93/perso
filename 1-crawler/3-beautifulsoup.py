import requests # learn more: https://python.org/pypi/requests
import bs4 # learn more: https://python.org/pypi/bs4
import lxml # learn more: https://python.org/pypi/lxml
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

soup = bs4.BeautifulSoup(html,'lxml')
#soup = BeautifulSoup(html)

# Reorganize html code
soup.prettify()
#print(soup)

'''
# Get the file title
print(soup.title)

# Get the title's name value
print(soup.title.name)

# Get the title's string value
print(soup.title.string)

# Get the name of title's parent (upper level)
print(soup.title.parent.name)

# Get the 1st paragraph found
print(soup.p)

# Get the attribut of the 1st paragraph
#print(soup.p['class'])
print(soup.p['style'])

# Get the 1st tag 'a'
print(soup.a)

# Get all tags 'a'
print(soup.find_all('a'))

# Get the tag whose id = "gb_70"
print(soup.find(id="gb_70"))
'''

# Get all links
for link in soup.find_all('a'):
  print(link.get('href'))

'''
# Get all texts
print(soup.get_text())
'''
