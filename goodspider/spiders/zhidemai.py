import scrapy
import json

class ZhidemaiSpider(scrapy.Spider):
    name = "zhidemai"
    allowed_domains = ["smzdm.com"]
    start_urls = [
            "https://www.smzdm.com/homepage/headline",
            ]

    def parse(self, response):
        result = json.loads(response.body)
