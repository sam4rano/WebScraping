import scrapy


class QuotesSpider(scrapy.Spider):
    name = "content"
    start_urls = [
        'https://www.bbc.com/yoruba/afrika-61544899'
    ]

    def parse(self, response):
        for link in response.css('#main-wrapper'):
            yield {
                'BBC_URL': link.css('a::attr(href)').getall()
            }



#scrapy crawl content -o links3.csv