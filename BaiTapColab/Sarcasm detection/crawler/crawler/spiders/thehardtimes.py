import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "thehardtimes"
    start_urls = {
        'https://thehardtimes.net/',
        'https://thehardtimes.net/music/',
        'https://thehardtimes.net/blog/',
        'https://thehardtimes.net/culture/',
        'https://thehardtimes.net/hof/',
        'https://thehardtimes.net/opinion/',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):

        #Điều kiện dừng (số trang)

        #Crawl dử liệu
        for post  in  response.css('.post-title'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('a::text').get(),
                'article_link': post.css('a::attr(href)').get(),
                'time': "NaN"
            }
        #Sang trang kế
        next_page =  response.css('.next.page-numbers::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
