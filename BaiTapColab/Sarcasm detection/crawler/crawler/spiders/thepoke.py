import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "thepoke"
    start_urls = {
        'https://www.thepoke.co.uk/',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):
        for rp in response.css('.nav-menu li a::attr(href)').getall():
            yield scrapy.Request(rp, callback=self.parse_full)

    def parse_full(self, response):
        #Điều kiện dừng (số trang)
        if response.status == 200:
            try:
                page_numper = int(response.url.split('/')[-2])
            except:
                page_numper = 1
        else : return

        #Crawl dử liệu
        for post  in response.css('.boxgrid'):
            yield{
                'page': response.url,
                'is_sarcastic': 1,
                'headline': post.css('.txt p::text').get(),
                'article_link': post.css('a::attr(href)').get(),
                'time': "NaN"
            }

        #Sang trang kế
        if page_numper == 1:
            next_page = response.url + "page/2/"
        else:
            next_page = response.url[:-1*(len(str(page_numper))+1)] + str(page_numper+1) + '/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_full)
