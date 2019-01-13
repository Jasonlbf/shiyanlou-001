# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/1.0/']
    links = LinkExtractor(allow="flask.pocoo.org/docs/1.0/.*")
    rules = (
            Rule(link_extractor=links,callback='parse_page',follow=True),
            )

    def parse_page(self, response):
        item = PageItem()
#        for res in response.xpath('//div[@id="user-s-guide"]'):
 #           item['url'] = response.urljoin(res.xpath('.//a/@href').extract_first())
  #          item['text'] = res.xpath('.//p/text()').extract_first()
        item['url'] = response.url
        item['text'] = response.xpath('//text()').extract()
        yield item
