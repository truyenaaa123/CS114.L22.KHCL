import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "waterfordwhispersnews"
    start_urls = {
        'https://waterfordwhispersnews.com/category/breaking-news/page/1/',
        'https://waterfordwhispersnews.com/category/lifestyle/page/1/',
        'https://waterfordwhispersnews.com/category/politics/page/1/',
        'https://waterfordwhispersnews.com/category/entertainment/page/1/',
        'https://waterfordwhispersnews.com/category/segments/page/1/',
        'https://waterfordwhispersnews.com/tag/brexit/page/1/',
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
        for post  in response.css('.index-card'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('h2 a::text').get(),
                'article_link': post.css('h2 a::attr(href)').get(),
                'time': post.css('.byline::text').get()[-7:-3]
            }

        #Sang trang kế
        if page_numper == 1:
            next_page = response.url + "page/2/"
        else:
            next_page = response.url[:-1*(len(str(page_numper))+1)] + str(page_numper+1) + '/'
            print()
            print(response.url[:-1*(len(str(page_numper))+1)], page_numper, response.url)
            print()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

