import scrapy
import pandas as pd
from ..items import TutorialItem

class QuoteSpider(scrapy.Spider):

    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]


    def parse(self, response):
        items = TutorialItem()
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            quote = quotes.css(".text::text").extract()
            author = quotes.css(".author::text").extract()
            tags = quotes.css(".tag::text").extract()

            items["quote"] = quote
            items["author"] = author
            items["tags"] = tags

            # yield {
            #     "quote": quote,
            #     "author": author,
            #     "tags": tags
            # }
            yield items
