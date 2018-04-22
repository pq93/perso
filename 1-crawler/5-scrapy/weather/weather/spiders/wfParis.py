# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WfparisSpider(scrapy.Spider):
    name = 'wfParis'
    # Modify host, enable Sccrapy to grab weather of other cities
    allowed_domains = ["Paris"]
    start_urls = ['http://foreca.fr/France/Paris?tenday/']
    # cities
    cities = ["Marseille","Lyon","Lille","Rennes","Toulouse","Bordeaux","Montpellier","Nice","Nantes","Strasbourg"]
    # Generate url with different cities
    for city in cities:
        cities = start_urls.append("http://www.foreca.fr/France/"+city+"?tenday")


    def parse(self, response):
        # Save information of each day
        items = []
        # Get tag content including weather information
        tenday = response.xpath('/a[@class="cell"]')
        # Get weather information of each day
        for day in tenday:
            # Apply a weatherItem to save grabbed information
            item = WeatherItem()

            date = ""
            for datetitle in day.xpath('/a/@hef').extract():
                date += datetitle[-8:]
                print(date)

            item['date'] = date
            item['week'] = day.xpath('/a/span[@class="h5"]').extract()[0]
            item['t_min'] = day.xpath('/a/strong[2]').extract()[0]
            item['t_max'] = day.xpath('/a/strong[1]').extract()[0]
            item['weather'] = day.xpath('/a/@title').extract()[0]
            item['wind'] = day.xpath('/a/span[2]/span/strong').extract()[0]
            items.append(item)

        return items
        #pass
