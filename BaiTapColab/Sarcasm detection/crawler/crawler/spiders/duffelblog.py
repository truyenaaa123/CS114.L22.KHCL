import scrapy
import json
from pprint import pprint
from scrapy.http import headers

class duffelblogSpider(scrapy.Spider):
    name = 'duffelblog'
    allowed_domains = ['duffelblog.com']
    start_urls = [
        'https://www.duffelblog.com/api/v1/archive?'
        'sort=new&searc=&offset=12&limit=12'
        ]

    def parse(self, response):
        results = json.loads(response.body)
        if len(results) < 1:
            return
        for result in results:
            yield{
                'is_sarcastic': 1,
                'headline': result['title'],
                'article_link': result['canonical_url'],
                'time': result['post_date'][:4]

            }

        next_page = int(response.url[-10:65:-1][::-1]) + 12
        # print(next_page)
        # print(f"https://www.duffelblog.com/api/v1/archive?sort=new&search=&offset={next_page}&limit=12")
        yield scrapy.Request(f"https://www.duffelblog.com/api/v1/archive?sort=new&search=&offset={next_page}&limit=12", callback=self.parse)