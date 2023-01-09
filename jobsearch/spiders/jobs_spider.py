import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"

    start_urls = [
        'https://www.linkedin.com/jobs/',
    ]

    def parse(self, response):

        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }

        pass