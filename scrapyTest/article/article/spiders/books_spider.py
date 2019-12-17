import scrapy
from scrapy.http import Request
from article.items import BookItem


class QuotesSpider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'https://www.biqukan.net/topallvisit/2.html',
    ]

    def parse(self, response):
        row = response.css('div.col-md-4.col-xs-4.book-coverlist')
        for x in row:
            item = BookItem()
            item['title'] = x.css('div.caption h4 a::attr(title)').get()
            item['url'] = x.css('div.caption h4 a::attr(href)').get()
            item['author'] = x.css('div.caption small::text').get()
            item['description'] = x.css('div.caption p::text').get()
            item['img_src'] = x.css('img.thumbnail::attr(src)').get()
            yield item

        # next = response.css('a.next::attr(href)').get()
        # if next:
        #     time.sleep(10)
        #     yield Request(url=parse.urljoin(response.url, next), callback=self.parse)











