# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepositoriesItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    #allowed_domains = ['github.com']
    #start_urls = ['http://github.com/']
    @property
    def start_urls(self):
        urls = ['https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxMFrOBZKVZw%3D%3D&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories']
        return urls

    def parse(self, response):
        for course in response.css('div.col-9.d-inline-block'):
            yield RepositoriesItem({
                'name': course.css('div.d-inline-block.mb-1 a::text').re_first('[^\w]*(\w+)[^\w]*'),
                'update_time': course.css('div.f6.text-gray.mt-2 relative-time::attr(datetime)').extract_first()
                })


