# Scrapy settings for linkbaiter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'linkbaiter'

SPIDER_MODULES = ['linkbaiter.spiders']
NEWSPIDER_MODULE = 'linkbaiter.spiders'

ITEM_PIPELINES = [
	"linkbaiter.pipelines.LinkbaiterPipeline",
	"linkbaiter.pipelines.RegexPipeline",
	"linkbaiter.pipelines.JsonWriterPipeline"
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linkbaiter (+http://opyate.com)'
