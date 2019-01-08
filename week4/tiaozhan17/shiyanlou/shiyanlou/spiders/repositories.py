# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepositoriesItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    #allowed_domains = ['github.com']
    #start_urls = ['http://github.com/']
    @property
    def start_urls(self):
        urls = ['https://github.com/shiyanlou?tab=repositories']
        return urls

    def parse(self, response):
        for course in response.css('div.col-9.d-inline-block'):
             item = RepositoriesItem()
             item['name'] = course.css('div.d-inline-block.mb-1 a::text').re_first('[^\w]*(\w+)[^\w]*')
             item['update_time'] = course.css('div.f6.text-gray.mt-2 relative-time::attr(datetime)').extract_first()

             course_url = response.urljoin(course.css('div.d-inline-block.mb-1 a::attr(href)').extract_first())
             request = scrapy.Request(course_url, callback=self.parse_github)
             request.meta['item'] = item
             yield request

        url_next = response.css('div.pagination span.disabled::text')
        if len(url_next) == 0 or url_next.extract()[0] != 'Next':
            next_url = response.css('div.pagination a:last-child::attr(href)').extract_first()
            yield response.follow(next_url, callback=self.parse)

    def parse_github(self,response):
        item = response.meta['item']
        for course in response.css('ul.numbers-summary'):
            item['commits'] = course.xpath('(//span[@class="num text-emphasized"])[1]/text()').re_first('[^\S]*(\S*)[^\S]*').replace(',','')
            item['branches'] = course.xpath('(//span[@class="num text-emphasized"])[2]/text()').re_first('[^\S]*(\S*)[^\S]*').replace(',','')
            item['releases'] = course.xpath('(//span[@class="num text-emphasized"])[3]/text()').re_first('[^\S]*(\S*)[^\S]*').replace(',','')
            yield item
            


