import scrapy

from NewsSpider.items import SinaNewsItem

class SinaNewsSpider(scrapy.Spider):
    name = "sinaNews"
    allowed_domains = ["med.sina.com"]
    start_urls = ["http://med.sina.com/article_gategory_103.html"]

    # https://news.yaozh.com/
    # http://www.cpi.ac.cn/publish/default/hyzx/


    def parse(self,response):

        item = SinaNewsItem()

        # title = response.xpath("/html/head/title/text()").extract()
        # listItem["title"] = title
        # # self.printcn(title)
        #
        # indextext_title = response.xpath('//a[@class="indextext-title"]/text()').extract()
        # listItem["indextext_title"]=indextext_title
        #
        indextext_link = response.xpath('//a[@class="indextext-title"]/@href').extract()
        # listItem["indextext_link"]=indextext_link
        # #
        # indextext_ms = response.xpath('//p[@class="indextext-ms"]/text()').extract()
        # listItem["indextext_ms"]=indextext_ms
        # #
        # indextext_time = response.xpath('//span[@class="indextext-time"]/text()').extract()
        # listItem["indextext_time"]=indextext_time

        item["news"] = []
        # return item
        print len(indextext_link)
        url_set = set(indextext_link)
        for url in url_set:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback = self.parse_news, meta={'item':item})

    def parse_news(self, response):
        item = response.meta['item']
        textbox = response.xpath('//div[@class="textbox"]').extract()
        news_title = response.xpath('//h1[@class="news-title"]/text()').extract()
        wz_fbtime = response.xpath('//span[@class="wz-fbtime"]/text()').extract()

        news = []
        news.append(news_title[0])
        news.append(wz_fbtime[0])
        news.append(textbox[0])
        item['news'] = news

        yield item