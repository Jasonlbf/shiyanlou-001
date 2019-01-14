# -*- coding: utf-8 -*-

import csv
import asyncio
import aiohttp
import async_timeout
from scrapy.http import HtmlResponse

results = []

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

def parse(url, body):
    response = HtmlResponse(url=url, body=body)
    for repository in response.css('li.public'):
        name = repository.css('a::text').extract_first().strip()
        update = repository.css('relative-time::attr(datetime)').extract_first()
        results.append((name,update))

async def task(url):
    async with aiohttp.ClientSession() as session:
        body = fetch(session,url)
        parse(url,body)

def main():
    loop = asyncio.get_event_loop()
    #url_template = 'https://github.com/shiyanlou?page={}&tab=repositories'
    url_template = [
           'https://github.com/shiyanlou?tab=repositories',
           'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
           'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
           'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
            ]
    tasks = [task(url) for url in url_template]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer = writerows(results)

if __name__ == '__main__':
    main()
