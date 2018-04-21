# -*- coding: utf-8 -*-
import scrapy


class WfparisSpider(scrapy.Spider):
    name = 'wfParis'
    allowed_domains = ['foreca.fr/France/Paris?tenday']
    start_urls = ['http://foreca.fr/France/Paris?tenday/']

    def parse(self, response):
        pass
