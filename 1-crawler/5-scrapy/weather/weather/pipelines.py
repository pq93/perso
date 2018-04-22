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

class WeatherPipeline(object):
    def process_item(self, item, spider):
        # Handle every item sent from wfParis
        # Get current directory
        base_dir = os.getcwd()
        # Save file in the folder 'data'
        filename = base_dir + '/data/weather.txt'
        # Open file to add data
        with open(filename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['t_min'] + '\n')
            f.write(item['t_max'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n')

        return item

class W2json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item

class W2mysql(object):
    def process_item(self, item, spider):
        date = item['date']
        week = item['week']
        t_min = item['t_min']
        t_max = item['t_max']
        weather = item['weather']
        wind = item['wind']

        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'admin',
            db = 'scrapyDB',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO WEATHER(date,week,t_min,t_max,weather,wind)VALUES(%s, %s, %s, %s, %s, %s)"""
                cursor.excute(sql,(date,week,t_min,t_max,weather,wind))
            connection.commit()
        finally:
            connection.close()
