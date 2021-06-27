import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "dailybonnet"
    start_urls = {
        'https://dailybonnet.com/category/quiz/',
        'https://dailybonnet.com/category/mennonitelife/',
        'https://dailybonnet.com/category/food-and-drink/',
        'https://dailybonnet.com/category/church/',
        'https://dailybonnet.com/category/outsiders/',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):

        #Điều kiện dừng (số trang)
        if response.status == 200:
            try:
                page_numper = int(response.url.split('/')[-2])
            except:
                page_numper = 1
        else : return
        # if page_numper >= 1200:
        #     return

        #Crawl dử liệu
        for post  in response.css('.mh-posts-list-header'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('.mh-posts-list-title a::text').get()[-5:6:-1][::-1],
                'article_link': post.css('.mh-posts-list-title a::attr(href)').get(),
                'time': post.css('.updated a::text').get()[-4:]
            }

        #Sang trang kế
        next_page = response.css('.next.page-numbers::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

