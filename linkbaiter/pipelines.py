# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


class LinkbaiterPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy.exceptions import DropItem

class RegexPipeline(object):

    def process_item(self, item, spider):
        if True:
            # TODO regex stuff here
            return item
        else:
            raise DropItem("Item doesn't match our link bait requirements %s" % item)

import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
