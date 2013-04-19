# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy import log
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule, XMLFeedSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector, XmlXPathSelector

from linkbaiter.items import TorrentItem, FeedItem

class MininovaSpider(CrawlSpider):

    name = 'mininova.org'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.mininova.org/yesterday']
    rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        x = HtmlXPathSelector(response)

        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = x.select("//h1/text()").extract()
        torrent['description'] = x.select("//div[@id='description']").extract()
        torrent['size'] = x.select("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent

# http://stackoverflow.com/questions/2939050/scrapy-follow-rss-links
class BusinessInspider(XMLFeedSpider):

    name = 'businessinsider.com'
    allowed_domains = ['feedburner.com']
    start_urls = ['http://feeds2.feedburner.com/businessinsider']
    iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        #log.msg('node: %s, type: %s' % (link, type(link)))

        item = FeedItem()
        item['link'] = node.select('link/text()').extract()
        item['title'] = node.select('title/text()').extract()
        return item

