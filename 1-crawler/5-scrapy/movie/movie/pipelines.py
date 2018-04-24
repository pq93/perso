# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
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
