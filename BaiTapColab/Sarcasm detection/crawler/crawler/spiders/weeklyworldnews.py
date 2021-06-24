import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "weeklyworldnews"
    start_urls = {
        'https://weeklyworldnews.com/category/headlines/page/1/',
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
        for post  in response.css(".inside-article"):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('.entry-title a::text').get(),
                'article_link': post.css('.entry-title a::attr(href)').get(),
                'time': post.css('.entry-date::text').get()[-4:]
            }

        #Sang trang kế
        next_page = "https://weeklyworldnews.com/category/headlines/page/" + str(page_numper+1)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

