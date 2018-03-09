# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapyDemo.items import Product

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
         filename = response.url.split("/")[-2]
         with open(filename, 'wb') as f:
            f.write(response.body)
         print response.css('title::text').extract()
#          for quote in response.css('div.quote'):
#             yield {
#                 'text': ''.split(quote.css('span.text::text').extract_first()),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }
         l = ItemLoader(item=Product(), response=response)
         l.add_xpath('name', '//div[@class="product_name"]')
         l.add_xpath('name', '//div[@class="product_title"]')
         l.add_xpath('price', '//p[@id="price"]')
#          l.add_css('stock', 'p#stock]')
         l.add_value('last_updated', 'today')  # you can also use literal values
         print l.load_item()
         return l.load_item()
#             print title1, link, desc
