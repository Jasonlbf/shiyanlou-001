# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem

class FlaskSpider(scrapy.Spider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/1.0']

    rules = (
            Rule(),
            )

    def parse(self, response):
        pass

    def parse(self, response):
        item = PageItem()

        yield item
