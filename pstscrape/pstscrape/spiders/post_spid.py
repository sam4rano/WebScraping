import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://www.konga.com/?gclid=Cj0KCQiAu62QBhC7ARIsALXijXSKW6IW6v6XXTKZ_6ZH3gLaFUcYnLa2ZUBSlENLVwrmt8Qj71A3L2caAsETEALw_wcB'
    ] 
    
    def parse(self,response):
        for post in response.css('a.a2cf5_2S5q5'):
            yield{
                'title':post.css('section h3::text').get(),
                'currency':post.css('.d7cOf_sJAqi span::text').get(),
                'amount':post.css('div .d7cOf_sJAqi::text').get()
            }

