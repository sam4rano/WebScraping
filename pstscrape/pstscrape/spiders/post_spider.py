# import scrapy

# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
#         'https://punchng.com/page/1',
#         'https://punchng.com/page/2'
#     ] 
    
#     def parse(self,response):
#         for post in response.css('article.entry-item-simple'):
#             yield{
#                 'date':post.css('.entry-meta div span::text').get(),
#                 'title':post.css('h3 a::text').get()
#             }
#     # def parse(self, response):
#     #     page = response.url.split('/')[-1] 
#     #     filename = 'posts%s.html' % page 
#     #     with open(filename,'wb') as f:
#     #         f.write(response.body)



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
                'currency':post.css('span span::text').get(),
                'amount':post.css('._2f4c5_18y_P span::text').get()
            }