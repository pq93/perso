# Scrapy application : weather forecast  

## 1. Object analysis  
(http://www.foreca.fr/France/Paris)  
http://www.foreca.fr/France/Paris?tenday  
Object: one-week weather forecast of Paris  

## 2. Data screening  
Data are wrapped in:
```html
<div class="c1 daily clr0">
<div class="c1 daily clr1">
<div class="c1 daily ">
```

Use selectors as bs4, xpath, css to perform the localization  
```python
response.xpath('//div[@class="c1 daily clr0"]')
response.xpath('//div[@class="c1 daily clr1"]')
response.xpath('//div[@class="c1 daily "]')
```

## 3. Build scrapy framework  
###### 1. Create project and crawler  
```shell
scrapy startproject weather
cd weather
scrapy genspider wfParis foreca.fr/France/Paris?tenday
```
###### 2. Edit items.py
```python
import scrapy
class WeatherItem(scrapy.Item):
    # Define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    week = scrapy.Field()
    img = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
```
###### 3. Edit spider
```python
import scrapy
from Weather.items import weatherItem
class wfParisSpider(scrapy.Spider):
    name = "wfParis"
    # Modify host, enable Scrapy to grab weather of other cities
    allowed_domains = ["Paris"]
    # Build url list
    start_urls = []
    # Cities
    cities = ["Marseille","Lyon","Lille","Rennes","Toulouse",...
    "Bordeaux","Montpellier","Nice","Nantes","Strasbourg"]
    # Generate url with different cities
    for city in cities:
        start_urls.append("http://www.foreca.fr/France/"+city+"?tenday")

    def parse(self, response):
        items = []

```
