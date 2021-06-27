import scrapy
from scrapy.http import headers


class ScrapSpider(scrapy.Spider):

    #thông số spider
    name = "thedailymash"
    start_urls = {
        'https://www.thedailymash.co.uk/news/science-technology/',
        'https://www.thedailymash.co.uk/news/arts-entertainment',
        'https://www.thedailymash.co.uk/news/society/',
        'https://www.thedailymash.co.uk/news',
        'https://www.thedailymash.co.uk/politics',
        'https://www.thedailymash.co.uk/news/lifestyle',
        'https://www.thedailymash.co.uk/sport',
        'https://www.thedailymash.co.uk/opinion',
        'https://www.thedailymash.co.uk/news/relationships',
        'https://www.thedailymash.co.uk/news/health',
        'https://www.thedailymash.co.uk/politics/politics-headlines',
    }

    #Hàm request
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    #Hàm crawl thông tin
    def parse(self, response):

        #Điều kiện dừng (số trang)
        #Crawl dử liệu
        for post  in  response.css('.pl-4.-mt-1'):
            yield{
                'is_sarcastic': 1,
                'headline': post.css('a::text').get(),
                'article_link': "https://www.thedailymash.co.uk" + post.css('a::attr(href)').get(),
                'time': "NaN"
            }
        #Sang trang kế
        next_page =  response.css('.relative.inline-flex.items-center.px-2.py-2.-ml-px::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin('https://www.thedailymash.co.uk' + next_page)
            yield scrapy.Request(next_page, callback=self.parse)
