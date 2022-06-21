import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

            






# import sys
# import scrapy

# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
        
#         'https://www.bbc.com/yoruba/afrika-46233001'   
#     ]
#     def parse(self,response):
#         page = response.url.split('/')[-1]
#         filename = 'posts-%s.html' % page
#         with open(filename,'wb') as f:
#             f.write(response.body)
        # for post in response.css('main div'):
        #     yield{
        #         'news_title':post.css('div h#content::text').getall(),
               
        #         'news_content':post.css('div p.px03xj::text').getall()
        #     }
# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
#         'https://www.bbc.com/yoruba/afrika-60975610'
#     ] 

#     def parse(self, response):
#         page = response.url.split('/')[-1]
#         filename = 'posts-%s.html' %page
#         with open(filename,'wb') as f:
#             f.write(response.body)


# import sys
# import scrapy

# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
        
#         'https://alaroye.org/'
        
#     ]
#     def parse(self,response):
#         for post in response.css('div.post-wrap'):
#             yield{
#                 # 'item_0':post.css('a::text').getall(),
#                 'item':post.css('h2::text').getall()
#                 # 'item_1':post.css('a::text')[1].get(),
#                 # 'item_2':post.css('p::text')[2].getall()
#             }
        # next_page = response.css('a.next::attr(href').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)    

