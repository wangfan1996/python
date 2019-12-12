import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'author'
    start_urls = [
        'http://quotes.toscrape.com/',
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
