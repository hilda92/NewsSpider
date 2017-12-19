import scrapy
from NewsSpider.items import SinaNewsItem

class SinaNewsSpider(scrapy.Spider):
    name = "sinaNews"
    allowed_domains = ["med.sina.com"]
    start_urls = ["http://med.sina.com/article_gategory_103.html"]

    def parse(self,response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        item = SinaNewsItem()
        title = response.xpath("/html/head/title/text()").extract()
        item["title"] = title[0][:-5]
        return item

