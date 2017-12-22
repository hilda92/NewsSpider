import scrapy

from NewsSpider.items import SinaNewsItem

class SinaNewsSpider(scrapy.Spider):
    name = "sinaNews"
    allowed_domains = ["med.sina.com"]
    start_urls = ["http://med.sina.com/article_gategory_103.html"]

    def printcn(self,suni):
        for i in suni:
            print i

    def parse(self,response):

        item = SinaNewsItem()
        # title = response.xpath("/html/head/title/text()").extract()
        # item["title"] = title
        # self.printcn(title)

        # indextext_title = response.xpath('//a[@class="indextext-title"]/text()').extract()
        # item["indextext_title"]=indextext_title

        indextext_link = response.xpath('//a[@class="indextext-title"]/@href').extract()
        # item["indextext_link"]=indextext_link
        #
        # indextext_ms = response.xpath('//p[@class="indextext-ms"]/text()').extract()
        # item["indextext_ms"]=indextext_ms
        #
        # indextext_time = response.xpath('//span[@class="indextext-time"]/text()').extract()
        # item["indextext_time"]=indextext_time

        item["textbox"] = []
        # return item
        print len(indextext_link)
        url_set = set(indextext_link)
        for url in url_set:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback = self.parse_news, meta={'item':item})

    def parse_news(self, response):
        item = response.meta['item']
        news_content = response.xpath('//div[@class="textbox"]').extract()
        indextext_title = response.xpath('//h1[@class="news-title"]/text()').extract()
        indextext_time = response.xpath('//span[@class="wz-fbtime"]/text()').extract()


        item['textbox'].append(indextext_title[0])
        item['textbox'].append(indextext_time[0])
        item['textbox'].append(news_content[0])

        yield item



