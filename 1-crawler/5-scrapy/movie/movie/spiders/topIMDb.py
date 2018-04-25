# -*- coding: utf-8 -*-
import scrapy
# Do not forget to import items, which enables data flow between models
from movie.items import MovieItem

class TopimdbSpider(scrapy.Spider):
    name = 'topIMDb'
    allowed_domains = ["imdb.com"]
    # All 250 movies' information are on one same website
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        '''
        Function to screen information:
        rank: the ranking of the movie (from 1 to 250)
        title: the title of the movie
        year: the year when the movie was released
        imdbrating: the average rating by IMDb users (from 1 to 10)
        img: the picture of the movie poster
        '''
        # Create a list to save the data of each movie
        items = []
        # Get the tag wrapping the data of each movie
        topmovie = response.xpath('//tbody[@class="lister-list"]/tr')
        # Use a loop to get data of each movie
        for movie in topmovie:
            # Apply a MovieItem to save screened results
            item = MovieItem()

            item["rank"] = movie.xpath('./td[@class="posterColumn"]/span[@name="rk"]/@data-value').extract()[0]
            # Turn data type from string to integer
            item["rank"] = int(item["rank"])

            # Be careful to encoding problems
            item["title"] = movie.xpath('./td[@class="titleColumn"]/a//text()').extract()[0]

            # Get "(1998)" and slice the string to get "1998"
            item["year"] = movie.xpath('./td[@class="titleColumn"]/span//text()').extract()[0][1:5]
            # Turn data type from string to integer
            item["year"] = int(item["year"])

            item["imdbrating"] = movie.xpath('./td[@class="posterColumn"]/span[@name="ir"]/@data-value').extract()[0]
            # Turn data type from string to float, then keep 3 decimals
            item["imdbrating"] = round(float(item["imdbrating"]),3)

            # Get the full url of the image
            item["img"] = movie.xpath('./td[@class="posterColumn"]/a/img/@src').extract()[0]

            items.append(item)

        return items
        #pass
