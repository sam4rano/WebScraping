import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

import os

class Ebayspider(Spider):

    name = 'yoruba'
    allowed_domains = ['bbc.com/yoruba']
    start_urls = ['https://www.bbc.com/yoruba']
    
    try:
        os.remove('ebay2.txt')
    except OSError:
        pass

    custom_settings = {
        'CONCURRENT_REQUESTS' : 2,               
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_DEBUG': True,
        'DOWNLOAD_DELAY': 1
    }

    def __init__(self):
        self.link_extractor = LinkExtractor(allow=\
            "https://www.bbc.com/yoruba", unique=True)

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            with open('ebay2.txt','a+') as f:
                f.write(f"\n{str(link)}")

            yield response.follow(url=link, callback=self.parse)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(Ebayspider)
    process.start()



# import requests
# from bs4 import BeautifulSoup

# url_list = ['https://www.coingecko.com/en/coins/2goshi','https://www.coingecko.com/en/coins/0xcharts']

# for link in url_list:
#     result = requests.get(link)
#     src = result.content
#     soup = BeautifulSoup(src, 'lxml')

#     contract_address = soup.find(
#     'i', attrs={'data-title': 'Click to copy'})

#     print(contract_address.attrs['data-address'])

# url_list.seek(0)