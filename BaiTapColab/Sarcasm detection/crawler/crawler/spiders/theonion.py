import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "theonion"
    start_urls = {
        'https://www.theonion.com/latest',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):

        #Điều kiện dừng (số trang)

        #Crawl dử liệu
        for post  in  response.css('.cw4lnv-5'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('h2::text').get(),
                'article_link': post.css('a::attr(href)').get(),
                'time': "NaN"
            }
        #Sang trang kế
        next_page =  response.css('.sc-1uzyw0z-0.kNHeFZ a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin('https://www.theonion.com/latest' + next_page)
            yield scrapy.Request(next_page, callback=self.parse)
