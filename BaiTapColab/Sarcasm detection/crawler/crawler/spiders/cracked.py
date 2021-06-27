import scrapy
import json
from pprint import pprint
from scrapy.http import headers

class duffelblogSpider(scrapy.Spider):
    name = 'cracked'
    allowed_domains = ['https://www.cracked.com']
    start_urls = [
        'https://www.cracked.com/?ajax=1&page=2'
        ]

    def parse(self, response):
        results = json.loads(response.body)
        x = results["contents"]
        print(x.split("/n"))
        # if len(results) < 1:
        #     return
        # for result in results:
        #     yield{
        #         'is_sarcastic': 1,
        #         'headline': result['title'],
        #         'article_link': result['canonical_url'],
        #         'time': result['post_date'][:4]

        #     }

        # next_page = int(resopnse.url[])
        # # print(next_page)
        # # print(f"https://www.duffelblog.com/api/v1/archive?sort=new&search=&offset={next_page}&limit=12")
        # yield scrapy.Request(f"https://www.duffelblog.com/api/v1/archive?sort=new&search=&offset={next_page}&limit=12", callback=self.parse)