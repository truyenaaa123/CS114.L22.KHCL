import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):
    #thông số spider
    name = "scrap"
    domain = "https://www.huffpost.com"
    start_urls = {
        'https://www.huffingtonpost.co.uk/news/?page=2',
    }

    #Hàm request
    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#Sửa lỗi 403
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    #Hàm crawl thông tin
    def parse(self, response):
        
        #Điều kiện dừng (số trang)
        if int(response.url.split('/')[-1][6:]) >= 1200:
            return

        #Crawl dử liệu
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#sữa lỗi 403
        for post  in response.css('div.js-card'):
            web = post.css('.card__headlines a::attr(href)').get()
            new_request = scrapy.Request(web, callback=self.parse_time, headers= headers)
            yield{
                'is_sarcastic': 1,
                'headline': post.css('.card__headlines h2::text').get(),
                'article_link': web,
                #'time': new_request.meta['time']
            }
        
        #Sang trang kế
        next_page = "https://www.huffpost.com" + response.css('a.pagination__next-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse,headers=headers)


    def parse_time(self, response):
        return response.css('.timestamp span::text').get()