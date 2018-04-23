# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem
from scrapy.selector import HtmlXPathSelector

class TopimdbSpider(scrapy.Spider):
    name = 'topIMDb'
    allowed_domains = ["imdb.com"]
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):

        items = []
        topmovie = response.xpath('//tbody[@class="lister-list"]/tr')
        for movie in topmovie:
            item = MovieItem()

            item["rank"] = movie.xpath('./td[@class="posterColumn"]/span[@name="rk"]/@data-value').extract()[0]
            item["rank"] = int(item["rank"])

            item["title"] = movie.xpath('./td[@class="titleColumn"]/a//text()').extract()[0].encode("utf8")

            item["year"] = movie.xpath('./td[@class="titleColumn"]/span//text()').extract()[0][1:5]
            item["year"] = int(item["year"])

            item["imdbrating"] = movie.xpath('./td[@class="posterColumn"]/span[@name="ir"]/@data-value').extract()[0]
            item["imdbrating"] = round(float(item["imdbrating"]),3)

            item["img"] = movie.xpath('./td[@class="posterColumn"]/a/img/@src').extract()[0]

            items.append(item)

        return items
        #pass
