# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class NewsspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open("SinaNews_0.json", 'wb', encoding='utf-8')
        self.html = codecs.open("SinaNews.html", 'wb', encoding='utf-8')
        self.html_open =  """
        <html>
        <head></head>
        <body>
        <ul>
        """
        self.html_close = """
        </ul>
        </body>
        </html>
        """

    def process_item(self, item, spider):
        print "item=========================="
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))


        content = dict(item)["news"]
        title = content[0]
        publishTime = content[1]
        newsContent = content[2]

        contentStr = """<li><h1>%s</h1><p>%s</p>%s</li>"""%(title,publishTime,newsContent)
        self.html.write(contentStr)

        return item

    def open_spider(self, spider):
        self.html.write(self.html_open)

    def close_spider(self,spider):
        self.html.write(self.html_close)
