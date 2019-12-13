import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'https://www.biqukan.net/topallvisit/1.html',
    ]

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthDate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
# response.css('div.col-md-7 div.caption h4 a::attr(title)').getall()
#  response.css('div.col-md-7 div.caption h4 a::attr(href)').getall()
#  response.css('div.col-md-5 a img::attr(alt)').getall()
#  response.css('div.col-md-5 a img::attr(href)').getall()
