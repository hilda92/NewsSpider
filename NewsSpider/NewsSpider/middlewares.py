# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
from scrapy.http import HtmlResponse
import time

from scrapy import signals


class NewsspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class NewsspiderDownloaderMiddleware(object):

    def process_request(self,request,spider):

        url = "http://med.sina.com/article_gategory_103.html"

        if request.url == url:
            # driver = webdriver.PhantomJS(executable_path="D:\software\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
            driver = webdriver.PhantomJS(executable_path="/Users/mac/phantomjs-2.1.1-macosx/bin/phantomjs")

            print "=" + "\n"
            try:
                driver.get(request.url)
                # driver.implicity_wait(1)
                time.sleep(1)

                clickmore = "//a[@class='clickmore']"
                for n in range(0):
                    print "+" + "\n"
                    driver.find_element_by_xpath(clickmore).click()
                    time.sleep(2)

                true_page = driver.page_source
                driver.close()
                return HtmlResponse(request.url, body = true_page,encoding='utf-8',request=request,)
            except Exception as e:
                print 'get news data failed'+e.message

        return None
