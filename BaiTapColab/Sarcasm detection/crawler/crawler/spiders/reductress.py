import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "reductress"
    start_urls = {
        'https://reductress.com/news/page/1/',
        'https://reductress.com/living/page/1/',
        'https://reductress.com/entertainment/page/1/',
        'https://reductress.com/love-sex/page/1/',
        'https://reductress.com/womanspiration/page/1/',
        'https://reductress.com/print-edition/page/1/',
        'https://reductress.com/thoughts/page/1/',
        'https://reductress.com/style/page/1/',
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
        for post  in response.css('.main.archive div.box'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('h1::text').get(),
                'article_link': post.css('article a::attr(href)').get(),
                'time': "NaN"
            }

        #Sang trang kế
        next_page = response.url[:-1*(len(str(page_numper))+1)] + str(page_numper+1) + '/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

