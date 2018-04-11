import requests

# Get source code of index page of Google
data = requests.get("https://www.googole.fr")
print(data.text)
