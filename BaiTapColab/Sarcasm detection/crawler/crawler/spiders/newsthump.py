import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "newsthump"
    start_urls = {
        'https://newsthump.com/',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):
        for rp in response.css('.menu-header-bottom-menu-container .menu li a::attr(href)').getall()[1:-1]:
            yield scrapy.Request(rp, callback=self.parse_full)

    def parse_full(self, response):
        #Điều kiện dừng (số trang)

        #Crawl dử liệu
        for post  in  response.css('.entry-title'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('a::text').get(),
                'article_link': post.css('a::attr(href)').get(),
                'time': "NaN"
            }
        #Sang trang kế
        next_page = response.css('.prev_next .previous a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_full)
