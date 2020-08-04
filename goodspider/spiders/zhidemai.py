import scrapy
import json

class ZhidemaiSpider(scrapy.Spider):
    name = "zhidemai"
    allowed_domains = ["smzdm.com"]
    start_urls = [
            "https://www.smzdm.com/homepage/headline",
            "https://search.smzdm.com/?c=home&s=%E5%8E%86%E5%8F%B2%E4%BD%8E%E4%BB%B7&v=a"
            ]

    def parse(self, response):
        result = json.loads(response.body)
