import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"  # Spider name to run later
    start_urls = ['https://quotes.toscrape.com/']  # Start page to scrape

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get()
            }

        # For pagination (next page)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
