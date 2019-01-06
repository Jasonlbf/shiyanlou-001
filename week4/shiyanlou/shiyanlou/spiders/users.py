# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'
    #allowed_domains = ['shiyanlou.com']
    #start_urls = ['http://shiyanlou.com/']

    @property
    def start_urls(sef):
        return ('https://www.shiyanlou.com/user/{}/'.format(i) for i in range(525000,524800,-10))

    def parse(self, response):
        yield UserItem({
            'name': response.css('span.username::text').extract_first(),
            'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default='general'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'school_job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'join_date': response.css('span.join-date::text').extract_first(),
            'level':response.css('span.user-level::text').extract_first(),
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first()
            })
