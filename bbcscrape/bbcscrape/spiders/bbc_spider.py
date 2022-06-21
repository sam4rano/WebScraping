# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'https://www.bbc.com/yoruba/61303843',
#         'https://www.bbc.com/yoruba/afrika-61303840',
#         'https://www.bbc.com/yoruba/afrika-61312136',
#         'https://www.bbc.com/yoruba/afrika-61303841',
#         'https://www.bbc.com/yoruba/media-61303964',
#         'https://www.bbc.com/yoruba/media-61295960',
#         'https://www.bbc.com/yoruba/afrika-61299884',
#         'https://www.bbc.com/yoruba/61296392',
#         'https://www.bbc.com/yoruba/media-61298892',
#         'https://www.bbc.com/yoruba/61290588',
#         'https://www.bbc.com/yoruba/afrika-61287757',
#         'https://www.bbc.com/yoruba/afrika-61293086',
#         'https://www.bbc.com/yoruba/afrika-61292419',
#         'https://www.bbc.com/yoruba/afrika-61289163',
#         'https://www.bbc.com/yoruba/agbaye-61292414',
#         'https://www.bbc.com/yoruba/61292564',
#         'https://www.bbc.com/yoruba/afrika-61287751',
#         'https://www.bbc.com/yoruba/media-61289160',
#         'https://www.bbc.com/yoruba/afrika-61287758',
#         'https://www.bbc.com/yoruba/afrika-61265210',
#         'https://www.bbc.com/yoruba/afrika-61202610',
#         'https://www.bbc.com/yoruba/ere-idaraya-60910848',
#         'https://www.bbc.com/yoruba/60554121',
#         'https://www.bbc.com/yoruba/afrika-61258609',
#         'https://www.bbc.com/yoruba/media-61240136',
#         'https://www.bbc.com/yoruba/awon-iroyin-miran-61227361',
#         'https://www.bbc.com/yoruba/media-61208591',
#         'https://www.bbc.com/yoruba/61206766',
#         'https://www.bbc.com/yoruba/afrika-61172350',
#         'https://www.bbc.com/yoruba/61138346',
#         'https://www.bbc.com/yoruba/afrika-61126061',
#         'https://www.bbc.com/yoruba/afrika-61116524',
#         'https:/ww.b/wbc.com/yoruba/afrika-61097471',
#         'https://www.bbc.com/yoruba/media-61289293',
#         'https://www.bbc.com/yoruba/afrika-61287297',
#         'https://www.bbc.com/yoruba/afrika-61285024',
#         'https://www.bbc.com/yoruba/61284344',
#         'https://www.bbc.com/yoruba/61272052',
#         'https://www.bbc.com/yoruba/afrika-61285027',
#         'https://www.bbc.com/yoruba/61283916',
#         'https://www.bbc.com/yoruba/56926398',
#         'https://www.bbc.com/yoruba/media-61282950',
#         'https://www.bbc.com/yoruba/afrika-61254414',
#         'https://www.bbc.com/yoruba/awon-iroyin-miran-61254078',
#         'https://www.bbc.com/yoruba/afrika-61249248',
#         'https://www.bbc.com/yoruba/afrika-61272051',
#         'https://www.bbc.com/yoruba/afrika-61276956',
#         'https://www.bbc.com/yoruba/afrika-61271495',
#         'https://www.bbc.com/yoruba/afrika-61239994',
#         'https://www.bbc.com/yoruba/afrika-61269257',
#         'https://www.bbc.com/yoruba/afrika-61254413',
                
#     ]
    
#     def parse(self, response):
#         for quote in response.css('main'):
#             yield { #main-wrapper > div > div > div.e1j2237y3.bbc-irdbz7.e57qer20 > main > div.e1j2237y6.bbc-q4ibpr.e57qer20
#                 'news_title': quote.css('div h1.bbc-13dm3d0::text').get(),
#                 'news_date': quote.css('div time.bbc-1bnmgo0::text').get(),
#                 'news_content': quote.css('div p.bbc-ph03xj::text').getall(),
#             }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)


import scrapy

class PostsSpider(scrapy.Spider):
    name ="posts"

    starts_url = ['https://bbc.com/yoruba']


    def parse(self, response):
        page = response.url.split('/')
        filename = 'posts-%s.html' %page
        with open(filename,'wb') as f:
            f.write(response.body)
