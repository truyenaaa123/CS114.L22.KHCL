import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "walkingeaglenews"
    start_urls = {
        'https://walkingeaglenews.com/',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):

        #Điều kiện dừng (số trang)

        #Crawl dử liệu
        for post  in  response.css('.post-header'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('.post-title a::text').get(),
                'article_link': post.css('.post-title a::attr(href)').get(),
                'time': post.css('.post-byline::text').get()[-4:]
            }
        #Sang trang kế
        next_page = response.css('.next.page-numbers::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
