# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json
import codecs
import pymysql

class MoviePipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + "/data/movie.csv"
        with codecs.open(filename,'a', encoding="utf-8") as f:
            f.write(str(item["rank"])+ \
            ","+str(item["title"])+ \
            ","+str(item["year"])+ \
            ","+str(item["imdbrating"])+ \
            "\n")

        with codecs.open(base_dir + "/data/img/" + str(item["rank"]) + ".jpg", "wb") as f:
            f.write(requests.get(item["img"]).content)

        return item

class W2json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + "/data/movie.json"

        with codecs.open(filename, 'a', encoding="utf-8") as f:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            f.write(line)

        return item

class W2mysql(object):
    def process_item(self, item, spider):
        rank = item["rank"]
        title = str(item["title"])
        year = item["year"]
        imdbrating = item["imdbrating"]

        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            db = "imdb250",
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = """insert into movie(rank,title,year,imdbrating) VALUES (%s,%s,%s,%s)"""
                cursor.execute(sql,(rank,title,year,imdbrating))
            connection.commit()
        finally:
            connection.close()
        return item



# CREATE TABLE movie(
# id INT AUTO_INCREMENT,
# rank INT,
# title CHAR(255),
# year INT,
# imdbrating FLOAT,
# PRIMARY KEY(id)
# )ENGINE = InnoDB DEFAULT CHARSET = 'utf8';

# DROP DATABASE imdb250;
# DROP TABLE movie;
# desc movie;
# show columns from movie;
# SELECT * FROM movie;
