# -*= coding:utf-8 -*-
import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        urls = [
                'https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
                ]
        return urls 
    
    def parse(self,response):
       #for course in response.css('div.col-9.d-inline-block'):
       #     yield {
       #            'name': course.css('div.d-inline-block.mb-1 a::text').re_first('[^\w]*(\w+)[^\w]*'),
       #            'update_time': course.css('div.f6.text-gray.mt-2 relative-time::attr(datetime)').extract_first()
       #            }
            
        for course in response.xpath('//li[contains(@class, "public")]'):
            yield {
                'name': course.xpath('.//h3/a/text()').extract_first().strip(),
                'update_time': course.xpath('.//relative-time/@datetime').extract_first()
