# Scrapy application : IMDb Top Rated Movies    

## 1. Object analysis  
https://www.imdb.com/chart/top  
Object: data of top 250 movies on IMDb  

## 2. Data screening  
All data are wrapped in:
```html
<tbody class="lister-list">
  <tr>...</tr>
  <tr>...</tr>
  <tr>...</tr>
  ...
</tbody>
```
Use selectors as bs4, xpath, css to perform the localization:  
```python
topmovie = response.xpath('//tbody[@class="lister-list"]/tr')
```

## 3. Build scrapy framework  
#### 1. Create project and crawler  
Run command lines in Terminal to create scrapy project and generate the spider automatically:
```shell
scrapy startproject movie
cd movie
scrapy genspider topIMDb imdb.com
```
#### 2. Edit items.py  
Just fill in items.py with wanted variable items:
```python
import scrapy
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    imdbrating = scrapy.Field()
    rank = scrapy.Field()
    img = scrapy.Field()
    #pass
```
#### 3. Edit spider: topIMDb.py  
As the core of the scrapy project, the spider prepares target data by screening and transmits the data to the pipeline:
```python
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
            item["title"] = movie.xpath('./td[@class="titleColumn"]/a//text()').extract()[0].encode("utf8")

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
```
#### 4. Edit pipelines.py  
Pipeline can handle the grabbed data. The grabbed data are generally saved to local:
* **Text format**: the most basic format
* **Json format**: practical for others to call
* **Database**: when data are enormous  

###### 4.1 Text format (.csv)  
```python
import os # Miscellaneous operating system interfaces
import requests # HTTP requests
import json # JSON encoder and decoder (json.dumps() & json.loads())
import codecs # Python codec (encoders and decoders) registry and base classes
import pymysql # Connecting MySQL database

class MoviePipeline(object):
    # Deal with every item transmitted from the spider topIMDb.py
    def process_item(self, item, spider):
        # Get current directory
        base_dir = os.getcwd()
        # Save the file under current directory
        filename = base_dir + "/data/movie.csv"
        # Open the file and add contents
        with codecs.open(filename,'a', encoding="utf-8") as f:
            f.write(str(item["rank"])+ \
            ","+str(item["title"])+ \
            ","+str(item["year"])+ \
            ","+str(item["imdbrating"])+ \
            "\n")

        # Download images
        with codecs.open(base_dir + "/data/img/" + str(item["rank"]) + ".jpg", "wb") as f:
            f.write(requests.get(item["img"]).content)

        return item
```
###### 4.2 Json format (.json)  
```python
class W2json(object):
    # Save grabbed information to json file for others to call
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + "/data/movie.json"
        # Open the json file and write with json.dumps()
        # Encode text into json and all strings are in unicode: ensure_ascii=False
        with codecs.open(filename, 'a', encoding="utf-8") as f:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            f.write(line)

        return item
```
###### 4.3 Database format (MySQL)  
Learn more on MySQL: http://www.runoob.com/mysql/mysql-tutorial.html  

* 4.3.1 Install mysql in local  

During the installation of mysql, the password of the user "root" need to be set. The user "root" is not the user of system but the user of mysql database.
```shell
sudo apt-get update
sudo apt-get install mysql-server
```
* 4.3.2 Sign in mysql  
```shell
# Create
mysql -uroot -p
```
* 4.3.3 Create scrapy database and table
```sql
-- Create database encoding with 'utf8', command ended with ';'
CREATE DATABASE imdb250 CHARACTER SET 'utf8';
-- Choose the database and work on it
USE imdb250;
-- Create table and its columns
CREATE TABLE movie(
  id INT AUTO_INCREMENT,
  rank INT,
  title CHAR(255),
  year INT,
  imdbrating FLOAT,
  PRIMARY KEY(id)
) ENGINE = InnoDB DEFAULT CHARSET='utf8';
-- Visualize the table summary
show columns from movie;
-- Visualize the table summary
desc movie;
-- Show all contents of the table
SELECT * FROM movie
-- ******************************
-- Delete table:
-- DROP TABLE movie
-- Delete database:
-- DROP DATABASE imdb250
```
* 4.3.4 Install mysql model in python 3
```shell
pip3 install mysql
```
* 4.3.5 Edit pipeline code
```python
class W2mysql(object):
    # Save the grabbed data to mysql
    def process_item(self, item, spider):
        # Take out the data in item
        rank = item["rank"]
        title = str(item["title"])
        year = item["year"]
        imdbrating = item["imdbrating"]

        # Build connection to local scrapy database
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            db = "imdb250",
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # SQL command to create new values
                sql = """INSERT INTO movie(rank,title,year,imdbrating) VALUES (%s,%s,%s,%s)"""
                # Execute SQL command
                cursor.execute(sql,(rank,title,year,imdbrating))
            # Commit
            connection.commit()
        finally:
            # Close connection
            connection.close()

        return item
```
#### 5. Edit settings.py  
Add a dict ITEM_PIPELINES, the numbers (300, 400, 500) can be customized. The smaller the number, the earlier the pipeline class will be executed.  
```python
BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'movie.pipelines.MoviePipeline': 300,
    'movie.pipelines.W2json': 400,
    'movie.pipelines.W2mysql': 500,
}
```

#### 6. Run the scrapy project
```shell
scrapy crawl topIMDb
```

#### 7. Results
###### 7.1 CSV  
[Here: csv file](https://github.com/qpg93/personal/blob/master/1-crawler/5-scrapy/movie/data/movie.csv)  
[Here: images](https://github.com/qpg93/personal/tree/master/1-crawler/5-scrapy/movie/data/img)  
###### 7.2 JSON  
[Here: json](https://github.com/qpg93/personal/blob/master/1-crawler/5-scrapy/movie/data/movie.json)  
###### 7.3 MySQL  
