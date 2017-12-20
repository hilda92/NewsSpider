import scrapy
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from NewsSpider.items import SinaNewsItem

class SinaNewsSpider(scrapy.Spider):
    name = "sinaNews"
    allowed_domains = ["med.sina.com"]
    start_urls = ["http://med.sina.com/article_gategory_103.html"]

    def printcn(self,suni):
        for i in suni:
            print i

    def parse(self,response):

        url_set = set()
        self.driver.get(response.url)
        while True:
            wait =WebDriverWait(self.driver, 2)
            wait.until(lambda driver:driver.find_element_by_xpath('//a[@class="indextext-title"]/@href'))

        item = SinaNewsItem()
        title = response.xpath("/html/head/title/text()").extract()
        item["title"] = title
        self.printcn(title)

        indextext_title = response.xpath('//a[@class="indextext-title"]/text()').extract()
        item["indextext_title"]=indextext_title

        indextext_link = response.xpath('//a[@class="indextext-title"]/@href').extract()
        item["indextext_link"]=indextext_link

        indextext_ms = response.xpath('//p[@class="indextext-ms"]/text()').extract()
        item["indextext_ms"]=indextext_ms

        indextext_time = response.xpath('//span[@class="indextext-time"]/text()').extract()
        item["indextext_time"]=indextext_time
        return item


