import requests # learn more: https://python.org/pypi/requests

'''    
# Get source code of index page of Google
r = requests.get("https://www.google.fr")
print(r.text)

# Status code 200=success, 404=fail
print("Status code:", r.status_code)
# Get headers
print("Headers:", r.headers)
# Encoding acquired by header analysis
print("Encoding:", r.encoding)
# Encoding acquired by content analysis (slow but precise)
print("Apparent encoding:", r.apparent_encoding)
# Content of response
print("Content:", r.content)

# Customize header
hd = {'User-agent':'123'}
r = requests.get("https://www.google.fr", headers=hd)
print(r.request.headers)

# Customize proxypool
#pxs = {'http': 'http://user:pass@10.10.10.1:1234','https': 'https://10.10.10.1:4321'}
#r = requests.get("https://www.google.fr", proxies=pxs)
'''

# General function
def getHtmlText(url):
  try:
    r = requests.get(url, timeout=30)
    # If status code is not 200, raise HTTPError
    r.raise_for_status()
    # Set correct encoding
    r.encoding = r.apparent_encoding
    return print(r.text)
  except Exception:
    return "Something wrong"

getHtmlText("https://www.google.fr")
